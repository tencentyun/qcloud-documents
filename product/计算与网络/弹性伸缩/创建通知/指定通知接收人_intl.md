When the notification rule is set and recipient is specified, AS sends the notification to the specified person(s) when a scaling activity occurs.

### Step 1:  Specify the recipient of the notification

Go to [User Management Console](https://console.cloud.tencent.com/cam) and you will see the contact information of the account registrant.

To send the notification to other people (such as other members from the operation and maintenance team), please click **New**.

> Note:
> If you are the only user of your Tencent cloud account, you can skip this step, because the system has a "developer" account created by default.

### Step 2:  Define user groups (recipient classification)

AS sends a notification on a **user group** basis, rather than **recipient**.

**Scenario example:**

- If you want you are the only person to receive the notification, you can create a user group with your contact information only.
- You have defined a number of notification recipients, who may be in the same or different departments. You may wish that a certain type of notifications to be sent to the recipients of department A, and another type to the recipients of department B. Then you can define a user group, and put the different notification recipients to this particular user group.

**Setting Up:**

1. Go to [User Group Management](https://console.cloud.tencent.com/cam/groups), click **New User Group**, enter the group name and click **OK**.
2. Then click **Add User** to add the relevant notification recipients.

### Step 3: Apply user groups

When you define the alarm triggering policy and notification policy of the AS, you can see the user groups you have defined in the list of recipients. You can set a specific user group to be notified as needed.