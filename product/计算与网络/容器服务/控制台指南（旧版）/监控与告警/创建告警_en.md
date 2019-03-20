You can create an alarm to warn you of the status change of a cloud product and send related messages. The created alarm determines whether an alarm-related notification needs to be triggered according to the comparison results between a monitored metric and a specific threshold at every interval.

You can take precautionary or remedial measures in a timely manner when an alarm is set off by status changes. Therefore, creating a reasonable alarm can help you improve your application's robustness and reliability. For more information about alarms, please see [Creating Alarms](https://cloud.tencent.com/doc/product/248/1073).

You can set up an alarm by following steps below.

## Creating an Alarm Policy
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click **Cloud Monitoring -> My Alarms** tab, and then click **Alarm Policy** menu.

2) Click "Add Alarm Policy" button on the alarm policy list page.

3) In the pop-up box, enter the policy name, select policy type (the product that the alarm monitors) and choose trigger condition.
 - The trigger condition is a semantic condition consisting of metric, comparison relation, threshold, measurement period and lasting period. For example, if the metric is `CPU utilization`, the comparison relation is `>`, the threshold is `80%`, the measurement period is `5 minutes` and the lasting period is `2 periods`, it means that the data on CPU utilization is collected every 5 minutes. If the CPU utilization of a CVM is measured as above 80% for twice in succession, an alarm will be triggered.

4) With container service, you can create alarm policies for the following objects

 - Container cluster
 - Services within container clusters
 - Containers within container clusters

## Associate with an Object
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click **Cloud Monitoring** -> **My Alarms** tab, and then click **Alarm Policy** menu.

2) On the alarm policy list page, click the newly created alarm policy to enter the detail page, click **Add Association** button and select the product you want to monitor, then click **Apply** button.

## Setting an Alarm Receiver
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click **Cloud Monitoring** -> **My Alarms** tab, and then click **Alarm Policy** menu.

2) Click the created alarm policy to enter the detail page, then click **Manage alarm receiving group** button, and check the user groups that need to be notified.


Each alarm policy is a set of trigger conditions with the logical relationship "or", that is, as long as one of the conditions is met, an alarm will be triggered. The alarm will be sent to all users associated with the alarm policy. Upon receiving the alarm, the user can view the alarm and take appropriate actions in time.
