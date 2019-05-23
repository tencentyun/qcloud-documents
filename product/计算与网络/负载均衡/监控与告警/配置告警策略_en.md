You can create alarms to send alarm messages to specified users once the alarms are triggered when the cloud load balancers' running statuses meet specific conditions. The created alarm determines whether an alarm-related notification needs to be triggered according to the comparison results between a monitored metric and a specific threshold at intervals.

You can take precautionary or remedial measures in a timely manner when an alarm is set off by status changes of cloud products. Therefore, creating a reasonable alarm can help you improve robustness and reliability of your application. For more information on alarms, please see [Alarm Configurations](https://cloud.tencent.com/document/product/248/1073).

## Creating an Alarm Policy

The specific procedure is as follows:

1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Cloud Monitoring" -> "My Alarms" tab, and then click "Alarm Policy" menu.

2. Click "Add Alarm Policy" button on the alarm policy list page.

3. In the pop-up box, enter the policy name, select a policy type (cloud load balancer-public network/private network-listener/backend server port) and choose the trigger condition.
The trigger condition is a semantic condition consisting of metric, comparison relation, threshold, measurement period and lasting period.
For example, if the metric is `number of inbound packets`, the comparison relation is `>`, the threshold is `100/second`, the measurement period is `1 minute` and the lasting period is `2 periods`, it means that the number of inbound packets is collected every minute. If the inbound packets of a cloud load balancer instance listener/backend server port is measured as more than 100/second for twice in succession, an alarm will be triggered.


## Associate with an Object
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Cloud Monitoring" -> "My Alarms" tab, and then click "Alarm Policy" menu.

2. On the alarm policy list page, click the newly created alarm policy to enter the detail page, and click "Add Association" button and select the product you want to monitor (here select cloud load balancer in the list for cloud load balancer monitoring), then click "Apply" button.

## Set Alarm Receivers
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Cloud Monitoring" -> "My Alarms" tab, and then click "Alarm Policy" menu.

2. Click the created alarm policy to enter the detail page, then click "Manage alarm receiving group" button, and check the user groups that need to be notified.

Each alarm policy is a set of trigger conditions with the logical relationship "or", that is, as long as one of the conditions is met, an alarm will be triggered. The alarm will be sent to all users associated with the alarm policy. Upon receiving the alarm, the user can view the alarm and take appropriate actions in time.

