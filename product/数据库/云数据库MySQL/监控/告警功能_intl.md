You can create an alarm to warn you of the status change of a cloud product and send related messages. The alarm determines whether an alarm-related notification needs to be triggered by comparing the monitoring result and the standard threshold of each metric at regular interval.

The status changed alarm allows you to take precautionary or remedial measures in a timely manner. Therefore, creating a reasonable alarm can help you improve the robustness and reliability of your application. For more information about alarms, refer to [Creating Alarms>>][1].

## To Create an Alarm Policy
1) Log in to [Tencent Cloud Console][2], click "Cloud Monitoring" - "My Alarms" tabs, and click "Alarm Policy" menu.

2) Click "Add Alarm Policy" button on the alarm policy list page.

3) In the pop-up box, enter the Alarm Policy Name, and select the Policy Type (the product that the alarm monitors) and the Condition of alarm trigger.
The hit condition is a semantic condition consisting of metric, comparison relation, threshold, measurement period and lasting period. For example, where the metric is `disk usage`, the comparison relation is `>`, the threshold is `80%`, the measurement period is `5 minutes`, and the lasting period is`2 periods`, it means that the data on disk usage is collected every 5 minutes. If the disk usage of a Cloud Database is successively larger than 80% for twice, an alarm will be triggered.

### To Associate with an Object

1) Log in to [Tencent Cloud Console][3], click "Cloud Monitoring" - "My Alarms" tabs, and click "Alarm Policy" menu.

2) On the alarm policy list page, click the newly created alarm policy to enter the Details page, click "Add Association" button and select the product you want to monitor, and then click "Apply" button.

## To Set an Alarm Receiver

1) Log in to [Tencent Cloud Console][4], click "Cloud Monitoring" - "My Alarms" tabs, and click "Alarm Policy" menu.

2) Click the created alarm policy to enter the Details page, click "Manage Alarm Receiving Group" button, and then check the user groups that need to be notified.

Each alarm policy is a collection of hit conditions. As long as one of the conditions is satisfied, an alarm will be triggered. The alarm will be sent to all users associated with the alarm policy. After receiving the alarm, the user can timely view the alarm and take appropriate actions.

[1]:	https://www.qcloud.com/doc/product/248/1073
[2]:	https://console.qcloud.com/
[3]:	https://console.qcloud.com/
[4]:	https://console.qcloud.com/

