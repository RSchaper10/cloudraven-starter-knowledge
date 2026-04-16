# Set up notifications for changes in resource data - Microsoft Graph | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/graph/change-notifications-overview

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-15T19:44:45.852380+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/graph/change-notifications-overview

Captured summary:

- Set up notifications for changes in resource data - Microsoft Graph | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- Set up notifications for changes in resource data Feedback Summarize this article for me Change notifications enable applications to receive alerts when a Microsoft Graph resource they're interested in changes; that is, created, updated, or deleted.
- Microsoft Graph sends notifications to the specified client endpoint, and the client service processes the notifications according to the business requirements.

Extracted text:

Set up notifications for changes in resource data - Microsoft Graph | Microsoft Learn

Table of contents

Exit editor mode

Ask Learn

Ask Learn

Focus mode

Table of contents

Read in English

Add

Add to plan

Edit

Share via

Facebook

x.com

LinkedIn

Email

Copy Markdown

Print

Note

Access to this page requires authorization. You can try

signing in

or

changing directories

.

Access to this page requires authorization. You can try

changing directories

.

Set up notifications for changes in resource data

Feedback

Summarize this article for me

Change notifications enable applications to receive alerts when a Microsoft Graph resource they're interested in changes; that is, created, updated, or deleted. Microsoft Graph sends notifications to the specified client endpoint, and the client service processes the notifications according to the business requirements. For example, the service might fetch more data, update its cache and views, and so on.

Important

The change notifications feature isn't supported in Microsoft Entra External ID in external tenants and Azure AD B2C tenants.

Why get change notifications?

Change notifications follow an event-driven model where customers receive alerts when changes occur instead of them polling Microsoft Graph. Depending on your business logic, change notifications are suitable when:

You're subscribing to a resource that changes frequently.

You need to react to changes in near real-time.

You want to avoid frequently polling Microsoft Graph which might cause you to hit the throttling limits.

The following image shows how change notifications works and compares with

change tracking

.

The following video provides an overview of change notifications in Microsoft Graph.

Types of change notifications

Microsoft Graph supports three types of change notifications:

Basic notifications

: Change notifications that don't contain resource data other than the

id

of the resource that changed. When an app receives a basic notification, the service can use the

id

to query the changed object.

Rich notifications

: Change notifications that include the resource data of the object that changed. For more information about rich notifications, see

Rich notifications

.

Lifecycle notifications

: Notifications that alert the customer when they are at risk of missing change notifications due to the lifecycle of their subscription. For more information about lifecycle notifications, see

Lifecycle notifications

.

Receiving change notifications

Microsoft Graph can deliver change notifications to clients via the following channels.

Webhooks

. For more information, see

Receive change notifications through webhooks

.

Azure Event Hubs

. For more information, see

Receive change notifications through Azure Event Hubs

.

Azure Event Grid

. For more information, see

Receive change notifications through Azure Event Grid

.

Managing subscriptions

Clients can create subscriptions, renew subscriptions, and delete subscriptions. While the subscription is active and when changes occur in the subscribed resource, Microsoft Graph sends change notifications to the specified notification endpoint.

You manage the subscription using the

subscription resource type

and its related methods. Microsoft Graph sends change notifications in a structure defined in the

changeNotificationCollection resource type

.

Supported resources

An app can subscribe to changes on the Microsoft Graph resources listed in the table. Subscriptions to resources marked with an asterisk (

*

) are only available on the

/beta

endpoint.

Note

For Microsoft Teams resources, the

per-organization limit of 10,000 total subscriptions

is shared cumulatively across

all Teams change notification subscriptions

in the tenant. It includes subscriptions created for different Teams resources—such as chats, chat messages, call transcripts, call recordings, channels, teams, and conversation members—which

all count toward the same organizational quota

. When the combined number of active Teams subscriptions reaches this limit,

any additional subscription creation request for a Teams resource fails

with a

403 Forbidden

error.

Resource

Supported resource paths

Limitations

Cloud printing

printer

Changes when a print job is ready to be downloaded (jobFetchable event):

/print/printers/{id}/jobs

-

Cloud printing

printTaskDefinition

Changes when there's a valid job in the queue (jobStarted event):

/print/printtaskdefinition/{id}/tasks

-

Copilot

aiInteraction

Copilot AI interactions that a particular user is part of:

copilot/users/{userId}/interactionHistory/getAllEnterpriseInteractions

Copilot AI interactions in an organization:

copilot/interactionHistory/getAllEnterpriseInteractions

Maximum subscription quotas:

Per app and tenant combination (for subscriptions tracking AI interactions across a tenant): 1

Per app and user combination (for subscriptions tracking AI interactions a particular user is part of): 1

Per user (for subscriptions tracking AI interactions a particular user is part of): 10 subscriptions.

Per organization: 10,000 total subscriptions.

driveItem

on OneDrive (personal)

Changes to content within the hierarchy of

any folder

:

/users/{id}/drive/root

-

driveItem

on OneDrive for work or school

Changes to content within the hierarchy of the

root folder

:

/drives/{id}/root

,

/users/{id}/drive/root

-

group

Changes to all groups:

/groups

Changes to a specific group:

/groups/{id}

Changes to owners of a specific group:

/groups/{id}/owners

Changes to members of a specific group:

/groups/{id}/members

Maximum subscription quotas:

Per app (for all tenants combined): 50,000 total subscriptions.

Per tenant (for all applications combined): 1,000 total subscriptions across all apps.

Per app and tenant combination: 100 total subscriptions.

Not supported for Azure AD B2C tenants.

NOTE:

Creation and soft-deletion of groups also trigger the

updated

changeType

.

Microsoft Entra Health Monitoring

alert

Changes to all health monitoring alerts:

/reports/healthmonitoring/alerts

Changes to a specific type of alert:

/reports/healthmonitoring/alert

with the

notificationQueryOptions

property in request payload set as

$filter=alertType eq '{alertType}'

-

list

under a SharePoint

site

Changes to content within the

list

:

/sites/{site-id}/lists/{list-id}

-

Microsoft 365 group

conversation

Changes to a group's conversations:

groups/{id}/conversations

-

Outlook

message

Changes to all messages in a user's mailbox:

/users/{id}/messages

,

/me/messages

Changes to messages in a user's Inbox:

/users/{id}/mailFolders('inbox')/messages

,

/me/mailFolders('inbox')/messages

A maximum of 1,000 active subscriptions per mailbox for all applications is allowed.

Outlook

event

Changes to all events in a user's mailbox:

/users/{id}/events

,

/me/events

A maximum of 1,000 active subscriptions per mailbox for all applications is allowed.

Outlook personal

contact

Changes to all personal contacts in a user's mailbox:

/users/{id}/contacts

,

/me/contacts

A maximum of 1,000 active subscriptions per mailbox for all applications is allowed.

Security

alert

Changes to a specific alert:

/security/alerts/{id}

Changes to filtered alerts:

/security/alerts/?$filter={parameters}

For more information, see

Security API alerts

.

Teams

approvals

Changes to all approvals in a tenant:

/solutions/approval/approvalItems

Maximum subscription quotas:

Per tenant (for all applications combined): 1000 total subscriptions across all apps

Per app and tenant combination: 1 subscription.

Teams

callRecord

Changes to all call records:

/communications/callRecords

Changes to filtered call records:

/communications/callRecords?$filter={parameters}

For more information, see

Change notifications for Call Records

.

Maximum subscription quotas:

Per organization: 100 total subscriptions.

NOTE:

Creation of call records also triggers the

updated

changeType

.

Teams

callRecording

All recordings in an organization:

communications/onlineMeetings/getAllRecordings

All recordings for a specific meeting:

communications/onlineMeetings/{onlineMeetingId}/recordings

A call recording that becomes available in a meeting organized by a specific user:

users/{id}/onlineMeetings/getAllRecordings

A call recording that becomes available in a meeting where a particular Teams app is installed:

appCatalogs/teamsApps/{id}/installedToOnlineMeetings/getAllRecordings

*

Maximum subscription quotas:

Per app and online-meeting combination: 1

Per app and user combination: 1

Per user (for subscriptions tracking recordings in all onlineMeetings organized by the user): 10 subscriptions.

Per organization: 10,000 total subscriptions.

Teams

callTranscript

All transcripts in an organization:

communications/onlineMeetings/getAllTranscripts

All transcripts for a specific meeting:

communications/onlineMeetings/{onlineMeetingId}/transcripts

A call transcript that becomes available in a meeting organized by a specific user:

users/{id}/onlineMeetings/getAllTranscripts

A call transcript that becomes available in a meeting where a particular Teams app is installed:

appCatalogs/teamsApps/{id}/installedToOnlineMeetings/getAllTrancripts

*

Maximum subscription quotas:

Per app and online-meeting combination: 1

Per app and user combination: 1

Per user (for subscriptions tracking transcripts in all onlineMeetings organized by the user): 10 subscriptions.

Per organization: 10,000 total subscriptions.

Teams

chat

Changes to any chat in the tenant:

/chats

Changes to a specific chat:

/chats/{id}

Changes to a specific chat with the

notifyOnUserSpecificProperties

query parameter:

/chats/{id}?notifyOnUserSpecificProperties={Boolean}

Changes to all chats in an organization where a particular Teams app is installed:

/appCatalogs/teamsApps/{id}/installedToChats

Changes to all chats that a particular user is part of:

/users/{id}/chats

Changes to all chats that a particular user is part of with the

notifyOnUserSpecificProperties

query parameter:

/users/{id}/chats?notifyOnUserSpecificProperties={Boolean}

Maximum subscription quotas:

Per app and chat combination: 1 subscription.

Per organization: 10,000 total subscriptions.

Per user (for subscriptions tracking all chats that a particular user is part of): 10 subscriptions.

Teams

chatMessage

Changes to chat messages in all channels in all teams:

/teams/getAllMessages

Changes to chat messages in a specific channel:

/teams/{id}/channels/{id}/messages

Changes to chat messages in all chats:

/chats/getAllMessages

Changes to chat messages in a specific chat:

/chats/{id}/messages

Changes to chat messages in all chats a particular user is part of:

/users/{id}/chats/getAllMessages

Changes to chat messages for all chats in an organization where a particular Teams app is installed:

/appCatalogs/teamsApps/{id}/installedToChats/getAllMessages

Maximum subscription quotas:

Per app and channel or chat combination: 1 subscription.

Per user (for subscriptions tracking chat messages in all chats the user is part of): 10 subscriptions.

Per organization: 10,000 total subscriptions.

Teams

channel

Changes to channels in all teams:

/teams/getAllChannels

Changes to channel in a specific team:

/teams/{id}/channels

Maximum subscription quotas:

Per app and team combination: 1 subscription.

Per organization: 10,000 total subscriptions.

Teams

conversationMember

Changes to membership in a specific team:

/teams/{id}/members

Changes to membership in all channels under a specific team:

teams/{id}/channels/getAllMembers

Changes to membership in a specific chat:

/chats/{id}/members

Changes to membership for all chats in an organization where a particular Teams app is installed:

/appCatalogs/teamsApps/{id}/installedToChats/getAllMembers

Changes to membership in all chats:

/chats/getAllMembers

Maximum subscription quotas:

Per app and team combination: 1 subscription.

Per organization: 10,000 total subscriptions.

Teams

onlineMeeting

*

Changes to an online meeting:

/communications/onlineMeetings(joinWebUrl='{encodedJoinWebUrl}')/meetingCallEvents

Doesn't support using

$select

to return only selected properties. The rich notification consists of all the properties of the changed instance. One subscription allowed per application per online meeting. For more information, see

Get change notifications for Microsoft Teams meeting call event updates

.

Teams

presence

Changes to a single user's presence:

/communications/presences/{id}

Changes to multiple users' presence:

/communications/presences?$filter=id in ({id},{id}...)

The subscription for multiple users' presence is limited to 650 distinct users. Doesn't support using

$select

to return only selected properties. The rich notification consists of all the properties of the changed instance. One subscription allowed per application per delegated user. For more information, see

Get change notifications for presence updates in Microsoft Teams

.

Teams

team

Changes to any team in the tenant:

/teams

Changes to a specific team:

/teams/{id}

Maximum subscription quotas:

Per app and team combination: 1 subscription.

Per organization: 10,000 total subscriptions.

Teams Shifts

offerShiftRequest

Changes to any offer shift request in a team:

/teams/{id}/schedule/offerShiftRequests

Maximum subscription quotas:

Per app and resource path combination: 1 subscription per tenant.

Per resource path and user combination: 10 delegated user subscriptions per tenant.

Teams Shifts

openShiftChangeRequest

Changes to any open shift request in a team:

/teams/{id}/schedule/openShiftChangeRequests

Maximum subscription quotas:

Per app and resource path combination: 1 subscription per tenant.

Per user and resource path combination: 10 subscriptions.

Per organization: 10,000 total subscriptions.

Teams Shifts

shift

Changes to any shift in a team:

/teams/{id}/schedule/shifts

Maximum subscription quotas:

Per app and resource path combination: 1 subscription per tenant.

Per user and resource path combination: 10 subscriptions.

Per organization: 10,000 total subscriptions.

Teams Shifts

swapShiftsChangeRequest

Changes to any swap shift request in a team:

/teams/{id}/schedule/swapShiftsChangeRequests

Maximum subscription quotas:

Per app and resource path combination: 1 subscription per tenant.

Per user and resource path combination: 10 subscriptions.

Per organization: 10,000 total subscriptions.

Teams Shifts

timeOffRequest

Changes to any time off request in a team:

/teams/{id}/schedule/timeOffRequests

Maximum subscription quotas:

Per app and resource path combination: 1 subscription per tenant.

Per user and resource path combination: 10 subscriptions.

Per organization: 10,000 total subscriptions.

todoTask

Changes to all task in a specific task list:

/me/todo/lists/{todoTaskListId}/tasks

-

user

Changes to all users:

/users

Changes to a specific user:

/users/{id}

Maximum subscription quotas:

Per app (for all tenants combined): 50,000 total subscriptions.

Per tenant (for all applications combined): 1,000 total subscriptions across all apps

Per app and tenant combination: 100 total subscriptions.

Not supported for personal Microsoft accounts like outlook.com.

Not supported for Azure AD B2C tenants.

NOTE:

Creation and soft-deletion of users also trigger the

updated

changeType

.

Note

Many resources have limits or quotas on how many subscriptions can be made against that resource. When exceeding that limit, attempts to create a subscription will result in a

403 Forbidden

error response. The

message

property of the error response will explain the limit that has been exceeded.

Some of these resources support rich notifications (notifications with resource data). For their details, see

Set up change notifications that include resource data

.

Subscription lifetime

Subscriptions have a limited lifetime. Apps need to renew their subscriptions before the expiration time; Otherwise, they need to create a new subscription. Apps can also unsubscribe at any time to stop getting change notifications.

The following table shows the maximum expiration times for subscriptions per resource in Microsoft Graph.

Resource

Maximum expiration time

Copilot

aiInteraction

4,320 minutes (three days)

Security

alert

43,200 minutes (under 30 days)

Teams

approvals

43,200 minutes (under 30 days)

Teams

callRecord

4,230 minutes (under three days)

Teams

callRecording

4,320 minutes (three days)

Teams

callTranscript

4,320 minutes (three days)

Teams

channel

4,320 minutes (three days)

Teams

chat

4,320 minutes (three days)

Teams

chatMessage

4,320 minutes (three days)

Teams

conversationMember

4,320 minutes (three days)

Teams

onlineMeeting

4,320 minutes (three days)

Teams

team

4,320 minutes (three days)

Teams

teamsAppInstallation

4,320 minutes (3 days)

Teams Shifts

offerShiftRequest

360 minutes (6 hours)

Teams Shifts

openShiftChangeRequest

360 minutes (6 hours)

Teams Shifts

shift

360 minutes (6 hours)

Teams Shifts

swapShiftsChangeRequest

360 minutes (6 hours)

Teams Shifts

timeOffRequest

360 minutes (6 hours)

Group

conversation

4,230 minutes (under three days)

OneDrive

driveItem

42,300 minutes (under 30 days)

SharePoint

list

42,300 minutes (under 30 days)

Outlook

message

,

event

,

contact

10,080 minutes (under seven days)

For subscriptions with resource data (rich notification subscriptions), subscription lifetime is 1440 minutes (under one day).

user

,

group

, other directory resources

41,760 minutes (under 29 days)

onlineMeeting

4,230 minutes (under three days)

presence

60 minutes (1 hour)

Print

printer

4,230 minutes (under three days)

Print

printTaskDefinition

4,230 minutes (under three days)

todoTask

4,230 minutes (under three days)

Webhooks for this resource are only available in the global endpoint and not in the national clouds.

Microsoft Entra Health Monitoring

alert

42,300 minutes (under 30 days)

baseTask

(deprecated)

4,230 minutes (under three days)

Note:

Existing applications and new applications should not exceed the supported value. In the future, any requests to create or renew a subscription beyond the maximum value will fail.

Latency

The following table lists the latency to expect between an event happening in the service and the delivery of the change notification.

Resource

Average latency

Maximum latency

aiInteraction

Less than 10 seconds

60 minutes

alert

1

Less than 3 minutes

5 minutes

approvals

Less than 10 seconds

40 seconds

calendar

Less than 1 minute

3 minutes

callRecord

2

Less than 30 minutes

150 minutes

callRecording

Less than 10 seconds

60 minutes

callTranscript

Less than 10 seconds

60 minutes

channel

Less than 10 seconds

60 minutes

chat

Less than 10 seconds

60 minutes

chatMessage

Less than 10 seconds

1 minute

contact

Less than 1 minute

3 minutes

conversation

Unknown

Unknown

conversationMember

Less than 10 seconds

60 minutes

driveItem

Less than 1 minute

60 minutes

event

Unknown

Unknown

group

Unknown

Unknown

health monitoring alert

Unknown

Unknown

list

Less than 1 minute

60 minutes

message

Less than 1 minute

3 minutes

offerShiftRequest

Less than 1 minute

60 minutes

onlineMeeting

Less than 10 seconds

1 minute

openShiftChangeRequest

Less than 1 minute

60 minutes

presence

Less than 10 seconds

1 minute

printer

Less than 1 minute

5 minutes

printTaskDefinition

Less than 1 minute

5 minutes

shift

Less than 1 minute

60 minutes

swapShiftsChangeRequest

Less than 1 minute

60 minutes

team

Less than 10 seconds

60 minutes

teamsAppInstallation

Less than 10 seconds

60 minutes

timeOffRequest

Less than 1 minute

60 minutes

todoTask

Less than 2 minutes

15 minutes

user

Unknown

Unknown

1

The latency provided for the

alert

resource is only applicable after the alert is created. It doesn't include the time it takes for a rule to create an alert from the data.

2

The latency provided for the

callRecord

resource is only applicable to the first version of a call record. Subsequent versions of a call record might be updated beyond the stated latencies.

Code samples

The following code samples are available on GitHub.

Microsoft Graph Training Module - Using Change Notifications and Track Changes with Microsoft Graph

Microsoft Graph Webhooks Sample for Node.js

Microsoft Graph Webhooks Sample for ASP.NET Core

Microsoft Graph Webhooks Sample for Java Spring

Related content

Rich notifications (notifications with resource data)

Lifecycle notifications

Change notifications for cloud printing

Change notifications for Outlook resources

Change notifications for Microsoft Teams resources

Feedback

Was this page helpful?

Yes

No

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

Ask Learn

Ask Learn

Suggest a fix?

Additional resources

Last updated on

2025-03-05
