# AWS SES Inbound Email And S3

This brief covers Amazon SES email receiving, receipt rules, S3 delivery, and the deployment failure modes that matter for CloudRaven's workspace-agent inbound email path.

## Where It Shows Up

- `amplify/backend.ts`
- `docs/workspace-agent-orchestration.md`
- `amplify/functions/workspace-agent-inbound-email-*`
- `amplify/states/workspace-agent-inbound-email-state/resource.ts`

## Official Entry Points

- Amazon SES email receiving concepts and receipt rules:
  `https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rules.html`
- Deliver to S3 bucket action:
  `https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-s3.html`
- Giving permissions to Amazon SES for email receiving:
  `https://docs.aws.amazon.com/ses/latest/dg/receiving-email-permissions.html`
- CloudFormation `AWS::SES::ReceiptRule` and `S3Action`:
  `https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html`
  `https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html`

## Why It Fits CloudRaven

- CloudRaven's workspace-agent inbound email path depends on SES receipt rules writing raw MIME email into S3 before an S3 event starts the inbound workflow state machine.
- This is not just a product feature detail; it is an infrastructure contract that can fail during deployment if the receipt rule, bucket policy, and receipt-rule activation are not assembled carefully.

## Core AWS Contract

The AWS-side shape that matters most is:

1. a verified SES receiving identity and working MX path for the domain
2. a receipt rule set with the intended rule
3. an S3 action or IAM role that SES can use to write the raw message
4. an S3 bucket in a region where SES email receiving is available, unless you use the IAM role path described in the SES docs
5. an active receipt rule set

The most important permission detail from the SES docs is that SES should be granted access with conditions scoped to:

- `AWS:SourceAccount`
- `AWS:SourceArn`

For the S3 bucket policy, the documented shape ties the write permission to the exact receipt rule ARN, not just a broad service principal grant.

## CloudRaven Deployment Pitfall

CloudFormation and CDK can fail even when the final resource set looks correct on paper.

Why:

- SES validates its ability to write to the S3 bucket when the receipt rule is created.
- If the bucket policy is not present yet, the receipt rule can fail with `InvalidS3Configuration`.
- Once that resource fails, the nested stack can roll back and make later IAM roles, Lambda roles, bucket-notification helpers, and state-machine roles look broken even though they were not the first fault.

CloudRaven-specific implication:

- `amplify/backend.ts` must force the SES receipt rule to depend on the raw-email bucket policy, not just the bucket.
- This is one of the cases where custom CDK ordering inside Amplify Gen 2 is operationally important, not just stylistic.

## Common Failure Signature

Expect this class of problem when you see errors like:

- `InvalidS3Configuration`
- `Could not write to bucket`
- `UPDATE_ROLLBACK_COMPLETE` on the nested functions stack after SES receipt-rule creation

In practice, this usually means one of four things:

1. the bucket policy does not allow SES to write
2. the rule was created before the bucket policy existed
3. the bucket or KMS configuration does not match SES receiving requirements
4. the region, domain, or active-rule-set prerequisites are incomplete

## Troubleshooting Checklist

Start with the actual SES-to-S3 edge, not the last resource listed in the rollback.

1. Confirm the receipt rule uses the expected S3 bucket and prefix.
2. Confirm the bucket policy grants `s3:PutObject` to `ses.amazonaws.com`.
3. Prefer the documented `AWS:SourceAccount` and `AWS:SourceArn` conditions over looser or indirect matching.
4. Confirm the receipt rule depends on the bucket policy in CDK or CloudFormation ordering.
5. Confirm the S3 bucket is in a region where SES email receiving is supported, unless you are using the IAM role path.
6. Confirm the bucket does not use object lock with a default retention period.
7. If KMS is involved, confirm the key policy grants SES the documented access.
8. Confirm the intended receipt rule set is active after deployment.
9. Confirm the domain identity, MX records, and receiving-region setup are actually complete outside the app repo.

## Review Questions

- Does the repo rely on an implicit creation order that SES will validate too early?
- Are we following the documented SES permission shape for S3 and KMS resources?
- Are receipt-rule activation and receiving-domain setup treated as first-class operational prerequisites?
- If the stack fails, do the docs point the operator to the SES-to-S3 edge first rather than the rolled-back child resources?
