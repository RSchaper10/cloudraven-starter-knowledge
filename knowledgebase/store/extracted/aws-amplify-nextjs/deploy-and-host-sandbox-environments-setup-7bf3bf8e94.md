# Use cloud sandbox in dev environment - Next.js - AWS Amplify Gen 2 Documentation

Source URL:

- https://docs.amplify.aws/nextjs/deploy-and-host/sandbox-environments/setup/

Dependency:

- AWS Amplify Gen 2 for Next.js

Collected at:

- 2026-04-15T19:44:18.917100+00:00

Direct links in scope:

- https://docs.amplify.aws/nextjs/how-amplify-works/
- https://docs.amplify.aws/nextjs/deploy-and-host/sandbox-environments/setup/
- https://docs.amplify.aws/nextjs/start/quickstart/
- https://docs.amplify.aws/nextjs/deploy-and-host/sandbox-environments/features/

Captured summary:

- Use cloud sandbox in dev environment - Next.js - AWS Amplify Gen 2 Documentation Name: interface Value: Introducing Amplify Gen 2 Dismiss Gen 2 introduction dialog Amplify has re-imagined the way frontend developers build fullstack applications.
- Fullstack TypeScript Write your app's data model, auth, storage, and functions in TypeScript; Amplify will do the rest.
- 🚀 Built with the AWS CDK Use any cloud resource your app needs.
- Back to Gen 1 Docs Learn more about Gen 2 Use cloud sandbox in dev environment ✨ Use with AI You can use a personal cloud sandbox environment that provides an isolated development space to rapidly build, test, and iterate on a fullstack app.
- Each developer on your team can use their own disposable sandbox environment connected to cloud resources.

Extracted text:

Use cloud sandbox in dev environment - Next.js - AWS Amplify Gen 2 Documentation

Name:

interface

Value:

Introducing Amplify Gen 2

Dismiss Gen 2 introduction dialog

Amplify has re-imagined the way frontend developers build fullstack applications. Develop and deploy without the hassle.

Fullstack TypeScript

Write your app's data model, auth, storage, and functions in TypeScript; Amplify will do the rest.

🚀

Built with the AWS CDK

Use any cloud resource your app needs. Never worry about scale.

Back to Gen 1 Docs

Learn more about Gen 2

Use cloud sandbox in dev environment

✨

Use with AI

You can use a personal cloud sandbox environment that provides an isolated development space to rapidly build, test, and iterate on a fullstack app. Each developer on your team can use their own disposable sandbox environment connected to cloud resources.

Cloud sandbox environments

are designed for development purposes and are not intended for production workloads. To accelerate deployments, Amplify utilizes

CDK hot swapping

where supported, enabling rapid updates to resources such as AWS Lambda functions and AWS AppSync resolver templates without requiring a full redeployment.

However, certain operations cannot be hot-swapped and require resource recreation to proceed:

Amazon DynamoDB GSI Operations:

In sandbox environments (but not in production), modifying or deleting a Global Secondary Index (GSI) is a time-intensive process. To simplify this, Amplify drops and recreates the table instead of modifying the index.

Amazon Cognito User Pool Changes:

Unsupported modifications, such as deleting a required field, result in Amplify dropping and recreating the user pool to ensure a consistent and functional configuration.

Create a new sandbox environment

You can set up a new sandbox environment on your machine once you have an Amplify app set up. If you have not yet created an Amplify Gen 2 app, visit the

Quickstart

.

First, open the terminal and run the following command:

Terminal

Copy

Terminal

code example

npx ampx sandbox

When you deploy a cloud sandbox, Amplify creates an

AWS CloudFormation

stack following the naming convention of

amplify-<app-name>-<$(whoami)>-sandbox

in your AWS account with the resources configured in your

amplify/

folder.

After a successful deployment,

sandbox

watches for file changes in your

amplify/

folder and performs real-time updates to the associated CloudFormation stack. This functionality is built leveraging the

hot swap capability of the AWS Cloud Development Kit (CDK)

.

Terminating a sandbox environment

After testing all the changes associated with the backend, you can terminate the sandbox session via

Ctrl

+

c

.

To delete all the resources in the sandbox environment, run the following command:

Terminal

Copy

Terminal

code example

npx ampx sandbox delete

Manage sandbox environments

You can view and manage all the sandbox environments for your team in the new

Amplify console

. This is useful for a team leader to audit all of the Amplify sandbox environments deployed within an account.

Choose

Manage Sandboxes

to get started:

You can then check the number, status, and last updates for sandbox environments across your team. You can also use the console to delete sandbox environments when no longer needed.

Best practices

Keep the following best practices in mind when working with cloud sandbox environments:

Sandboxes are identical in fidelity to your production environments.

Code changes are continuously deployed to your sandbox on every save for fast iterations.

Use sandboxes for experimentation and testing, not for production workloads.

Deploy one sandbox per Amplify app per developer to prevent conflicts.

Reset sandboxes occasionally to clear out unused resources and save costs.

NEXT

Sandbox features
