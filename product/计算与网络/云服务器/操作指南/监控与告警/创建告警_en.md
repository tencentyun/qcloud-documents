You can create an alarm that triggers when there are status changes for Cloud products, and send the related messages. Alarms that are created will determine whether a notification needs to be triggered based on the metrics monitored at a certain interval, relative to a given threshold.

You can take the appropriate precautions or recovery actions immediately after an alarm triggers due to status changes. Therefore, reasonably creating alarms will help improve the robustness and reliability of your applications. For more details on alarms, refer to [Create alarms](https://cloud.tencent.com/doc/product/248/1073).

## Create an alarm strategy
1) Log in to [Tencent Cloud control platform](https://console.cloud.tencent.com/), click "Cloud Monitor" - "My Alarms" tab, click "Alarm Strategy" menu.

2) On the Alarm Strategy list page, click the "New Alarm Strategy" button.

3) In the "New Alarm Strategy" pop-up box, enter the strategy name, select the strategy type (product to be used), and select the alarm triggering conditions.

- An alarm triggering condition is a semantic condition consisting of a metric, a comparison relation, a threshold, a statistical period and a duration. For example, the index for 'CPU utilization'; comparison relationship as '>'; threshold at '80%'; a '5 minute' statistical cycle; sustained cycle for '2 cycles'; this means that: every 5 minutes CPU utilization data will be collected; if a CVM's CPU utilization is greater than 80% continuously twice in a row, an alarm will be triggered.

## Related object
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Cloud Monitor" - "My Alarms" tab, click "Alarm Strategy" menu.

2) On the Alarm Strategy List page, click on the alarm strategy policy you just created, then click the [Add Relation] button on the details page and select the cloud product you want to follow; finally, click on the "Apply" button.

## Set alarm receivers
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Cloud Monitor" - "My Alarms" tab, click "Alarm Strategy" menu.

2) Click on an existing alarm strategy, and on the details page, click the "Manage alarm receiving group" button, and select user groups to notify.


Each alarm strategy is a set of alarm triggering conditions. An alarm triggering condition is an "OR" relationship. That is, when a condition is met, an alarm is sent. The alarm is sent to all users associated with the alarm strategy. After receiving the alarm, the user can view the information and take corresponding measures.

