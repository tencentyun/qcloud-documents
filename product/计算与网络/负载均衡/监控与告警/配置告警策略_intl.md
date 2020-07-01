You can create an alarm to send warning messages to specified users once the alarm is triggered when a cloud product's running status meets a specific condition. The created alarm determines whether an alarm-related notification needs to be triggered according to the comparison results between a monitored metric and a specific threshold at every interval.

You can take precautionary or remedial measures in a timely manner when an alarm is triggered by the status change of your cloud product. Therefore, creating a valid alarm can help you improve your application's robustness and reliability. For more information on alarm, please see [Create Alarm](https://cloud.tencent.com/document/product/248/1073).

## Creating an Alarm Policy

The specific procedure is as follows:

1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click **Cloud Monitor** -> **My Alarms** tab, and then click **Alarm Policy** menu.

2. Click **New Alarm Policy** button on the alarm policy list page.

3. In the pop-up box, enter the policy name, select a policy type (load balancer-public network/private network-listener/RS port) and choose the triggering condition.
The triggering condition is a semantic condition consisting of metric, comparison relation, threshold, measurement period and number of consecutive periods.
For example, if the metric is `number of inbound packets`, the comparison relation is `>`, the threshold is `100/sec`, the measurement period is `1 minute` and the number of consecutive periods is `2 periods`, it means that the number of inbound packets is collected once every minute. If the inbound packets of a load balancer instance listener/RS port is measured as more than 100/sec for twice in succession, an alarm will be triggered.


## Associating an Object
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click **Cloud Monitor** -> **My Alarms** tab, and then click **Alarm Policy** menu.

2. On the alarm policy list page, click the newly created alarm policy to enter its details page, then click **Add Association** button and select the cloud product you want to monitor (here we select load balancer in the list for monitoring), and click **Apply** button.

## Setting Alarm Receiver
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click **Cloud Monitor** -> **My Alarms** tab, and then click **Alarm Policy** menu.

2. Click the created alarm policy to enter its details page, then click **Manage Alarm Receiving Group** button, and check the user groups that need to be notified.

Each alarm policy is a set of triggering conditions with the logic relationship "or", that is, an alarm is triggered when one of the conditions is met. The alarm is sent to all users associated with the alarm policy. Upon receiving the alarm, the user can view the alarm and take appropriate actions in time.

