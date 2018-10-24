This guide is intended for users who use Cloud Monitor for the first time, and teaches users how to check real-time and historical monitoring data as well as how to set alarms for cloud services.

If you want to check the public network outbound bandwidth (the bandwidth sent by the cloud server to the Internet) of a CVM (ID: `ins-12345678`) in Shanghai over the past seven days, and send an alarm message to `12345678888` when a bandwidth greater than`2Mbps` is detected, you need to complete the following procedures.

## Starting Setup
To enable Tencent Cloud Monitor, you need to use Tencent Cloud services (such as CVMs) under your Tencent Cloud account, so that the metric data can be automatically generated in the Cloud Monitor Console.

Log in to [Tencent Cloud Console](https://console.cloud.tencent.com). On the top of the console, select "Cloud Monitoring" to enter Cloud Monitoring Console, and then you can check the monitoring data of your services, and use Monitor Overview, My Alarms, Cloud Product Monitoring and Data Usage Monitoring in the left navigation pane.

## Viewing Monitor Overview
Monitor Overview shows the overall monitoring information under your account, including core exceptions, custom monitoring views, and monitoring statistics. You can get basic information about the cloud services in this module.

## Viewing Monitoring Views of Cloud Products
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Cloud Monitoring" - "Cloud Product Monitoring" - "Cloud Virtual Machine" tab, and the right list will display all the CVM instances and their current <font color="red"> real-time data </font>.

2) Select "East China (Shanghai)" region, and click the CVM (ID: `ins-1234578`) to enter the instance monitoring details page. Click "Public Network Outbound Bandwidth" on the left, select "Last Seven Days" in the time range above, or use the time picker to select a specific time period, and then you can see the trend of the public network outbound bandwidth over the past seven days.

## Setting the Alarm
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Cloud Monitoring" - "My Alarms" tab, and then click "Alarm Policy" button.

2) Click "Add Alarm Policy" button on the alarm policy list page. In the "Add Alarm Policy" pop-up box, enter:
- Policy Name: Bandwidth alarm
- Policy Type: CVM
- Hit Condition: `PublicBandwidthOut` `>` `2 Mbps` `5 minutes` `1 period`

3) Click "Create" button.

4) In the Alarm Policy List page, click on the `Bandwidth alarm` you just created. Select "Shanghai" in the details page, click "Add Association" button, select CVM`ins-12345678`, and then click the "Apply" button.

5) Click "Manage Alarm Receiver Group" button, and click "User Center" in the message on the top of the pop-up box to enter the user center.

6) In the User Management tab, click the "Create User" button, and enter all the required information (including the phone number `12345678`).

7) In the User Group Management tab, click the "Create New User Group" button to create a new user group. Click OK. Click "Add User" to add the user you just created to this user group.

8) Back to [Cloud Monitoring Console](https://console.cloud.tencent.com/monitor/overview), click "Cloud Monitoring" - "My Alarms" tab, and then click the "Alarm Policy" menu; In the Alarm Policy List page, click on the just created `Bandwidth alarm`; in the details page, click the "Manage Alarm Receiver Group" button, and check the user group you just created.
