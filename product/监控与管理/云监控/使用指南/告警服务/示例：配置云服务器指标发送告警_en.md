Here's an example to show how to configure the alarm: Assume that you want to send a SMS alarm to the number `12345678888` when the CPU utilization of CVM instance `ins-12345678` (in Shanghai) `exceeds 80%` in `2` consecutive five minutes. The following steps show you how to configure the alarm specifically:

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Cloud Monitoring" - "My Alarms" tab, and then click "Alarm Policy" button.

2) Click the "Add Alarm Policy" button on the alarm policy list page. In the "Add Alarm Policy" pop-up window, enter:
- Policy Name: CPU alarm
- Policy Type: CVM
- Alarm Trigger Conditions: `CPU utilization` `>` `80%` `five minutes` `two periods`
- Alarm Repeated Period: Fifteen minutes

3) Click the"Create" button.

4) In the Alarm Policy List page, click the `CPU alarm` you just created. Select "Shanghai" in the details page, click the "Add Association" button, select CVM `ins-12345678`, and then click the "Apply" button.

5) Click the "Manage Alarm Receiver Group" button, and click "User Center" in the message on the top of the pop-up window to enter the user center.

6) In the User Management tab, click the "Create User" button, and enter all the required information.

7) In the User Group Management tab, click "Create New User Group" button to create a new user group. Click OK. Click "Add User" to add the user you just created to this user group.

8) Back to [Cloud Monitoring Console](https://console.cloud.tencent.com/monitor/overview), click the "Cloud Monitoring" - "My Alarms" tab, and then click the "Alarm Policy" menu. In the Alarm Policy List page, click on the just created `CPU alarm`; in the details page, click the "Manage Alarm Receiver Group" button, and check the user group you just created.

The alarm configuration can be completed through the above steps. At this point, if the CPU utilization of the instance exceeds 80% in consecutive ten minutes, the number `12345678888` will receive the alarm SMS sent from Tencent Cloud.
