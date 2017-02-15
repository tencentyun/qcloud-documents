You can create an alert that triggers when there are status changes for Cloud products, and send the related messages. Alerts that are created will determine whether a notification needs to be triggered based on the metrics monitored at a certain interval, relative to a given threshold.

You can take the appropriate precautions or recovery actions immediately after an alert triggers due to status changes. Therefore, reasonably creating alerts will help improve the robustness and reliability of your applications. For more details on alerts, refer to [Create alerts](https://www.qcloud.com/doc/product/248/1073).

## Create an alert strategy
1) Login to [Tencent Cloud control platform](https://console.qcloud.com/), click [Cloud Monitor] - [My Alerts] tab, click [Alert Strategy] menu.

2) On the Alert Strategy list page, click the [Add new Alert Strategy] button.

3) In the Add Alert Strategy pop-up box, enter the strategy name, select the strategy type (product to be used), and select the alert triggering conditions.
 - An alert triggering condition is a semantic condition consisting of a metric, a comparison relation, a threshold, a statistical period and a duration. For example, the index for 'CPU utilization'; comparison relationship as '>'; threshold at '80%'; a '5 minute' statistical cycle; sustained cycle for '2 cycles'; this means that: every 5 minutes CPU utilization data will be collected; if a CVM's CPU utilization is greater than 80% continuously twice in a row, an alert will be triggered.

## Related object
1) Login to [Tencent Cloud control platform](https://console.qcloud.com/), click [Cloud Monitor] - [My Alerts] tab, click [Alert Strategy] menu.

2) On the Alert Strategy List page, click on the alert strategy policy you just created, then click the [Add Relation] button on the details page and select the cloud product you want to follow; finally, click on the [Apply] button.

## Set object to receive alert
1) Login to [Tencent Cloud control platform](https://console.qcloud.com/), click [Cloud Monitor] - [My Alerts] tab, click [Alert Strategy] menu.

2) Click on an already created alert strategy, and on the details page, click the [Manage alert receiving group] button, and select user groups to notify.


Each alert strategy is a set of alert triggering conditions. An alert triggering condition is an "OR" relationship. That is, when a condition is met, an alert is sent. The alert is sent to all users associated with the alert strategy. After receiving the alert, the user can view the information and take corresponding measures.

