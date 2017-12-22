Tencent Cloud provides Cloud Monitor feature for all users by default, so you do not need to enable it manually. However, the monitoring data can only be collected and recorded after users start using one of the Tencent Cloud products.

## Obtaining Monitoring Data
### Obtaining through CKafka Console
CKafka has standalone monitor tabs in its own console.
CKafka monitors data at two dimensions: instance dimension and Topic dimension. In the monitoring page, you can check the production traffic, consumption traffic, the number of retained messages and other monitoring data of CKafka instances and Topics, and view the monitor data in a certain time period.

1. Log in to the [CKafka Console](https://console.cloud.tencent.com/ckafka).

2. In the list, click the ID of instance/Topic to be viewed to go to the details page.

3. Click "Monitor" tab.

### CKafka Monitoring Metrics
For more information, please see [CKafka Monitoring Metrics](https://cloud.tencent.com/document/product/248/12154).

## CKafka Alarm Policy
### Creating Alarm
You can create an alarm to warn you of the status change of a cloud product and send related messages. The created alarm determines whether an alarm-related notification needs to be triggered according to the comparison results between a monitoring metric and a specific threshold at every interval.

You can take precautionary or remedial measures in a timely manner when an alarm is triggered by status changes. Therefore, properly created alarms can help you improve robustness and reliability of applications. For more information about alarms, please see [Alarm Configuration](https://cloud.tencent.com/document/product/248/1073).

