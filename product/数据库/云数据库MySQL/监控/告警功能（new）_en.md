You can create alarms to trigger alarms and send alarm messages when the cloud product status changes. The created alarm can determine whether an alarm-related notification needs to be triggered according to the difference between the monitored index and the given threshold at intervals.
After an alarm is triggered by the status change, corresponding preventive or remedial measures can be taken in time. Thus appropriately created alarms can help you improve the robustness and reliability of applications. For more information about alarms, please refer to the article of [Alarm Configuration][1] regarding to cloud monitoring.
When a user needs to send an alarm for a specific status of a product, it is required to create an alarm policy at first. An alarm policy is composed of three compulsory components, that is, the name, type and alarm triggering conditions. Each alarm policy is a set of alarm triggering conditions with the logical relationship "or", that is, as long as one of the conditions is met, an alarm will be triggered. The alarm will be sent to all users associated with the alarm policy. Upon receiving the alarm, the user can view the alarm and take appropriate actions in time.
>**Note:**
Please make sure that you have set the default alarm recipient(s), otherwise you will not be informed by the default alarm policy of Tencent Cloud CDB.

You can create an alarm policy by following the steps:

## Creating an Alarm Policy
1. Click "Cloud Products" > "Basic Products" > "Monitoring and Management" >  "Cloud Monitoring" in the navigation bar to enter the product introduction under "Cloud Monitoring", and then click "Free to Use". Go to [Management Console](https://console.cloud.tencent.com/monitor/overview) under Cloud Monitoring.
![](//mc.qcloudimg.com/static/img/886cd2f9011883ee3d541928c6619f9b/image.png)
![](//mc.qcloudimg.com/static/img/286402320d17a7a66f8d6b81542a6b40/image.png)
2. Click "My Alarms" > "Alarm Policies". Click "Add a New Alarm Policy" button on the alarm policy list page.
![](//mc.qcloudimg.com/static/img/12704bae3992fd2cedee31ba89071c2a/image.png)
2. In the **Add a New Alarm Policy**, enter a policy name, select a proper policy type (the applied product) and choose alarm triggering conditions.
The alarm triggering condition refers to a semantic condition consisting of metrics, comparison relation, threshold, measurement period and lasting period. For example, the metric is **disk usage**, the comparison relation is >, the threshold is 80%, the measurement period is 5 minutes, and the lasting period is 2 periods, all of which means that the disk usage is collected every 5 minutes, and if the **disk usage** of a Cloud Database is greater than 80% for two times in row, an alarm will be triggered. Click "Next: Associate an Alarm Object".
![](//mc.qcloudimg.com/static/img/fc3830b9c4910feb7a08da76c64098e2/image.png)
3. Select the region of the object and search the associated object instances via the object instance ID, and after clicking the desired object instance, click "Next: Set a Receiving Group".
![](//mc.qcloudimg.com/static/img/7a7fbad0bc58f746c6ee410fcb2034f3/image.png)
4. Select a user group that needs to receive alarm information in **Select an Alarm Receiving Group** and then click "Finished" to complete the alarm policy creation.
![](//mc.qcloudimg.com/static/img/6ed5a8d41b98c0e8b840a78ce5238fc7/image.png)

## Associate an Object with the Alarm Policy
After the alarm policy is created, you can associate some alarm objects with it. After the alarm object satisfies the alarm triggering conditions, an alarm will be sent. An alarm object can be associated through the following settings.
1. Log in to the [Management Console](https://console.client.monitor/overview) under the cloud monitoring and then click "My Alarms" > "Alarm Policies". In the alarm policy list page, click the Alarm Policy just created by you.
![](//mc.qcloudimg.com/static/img/6f881d6e32e9ab3df483bd1821d7fb64/image.png)
2. In the **Manage Alarm Policies** page, click "Add a New Association".
![](//mc.qcloudimg.com/static/img/a34ebce6478c8b40d3194161fd85a830/image.png)
2. Select a cloud product to be associated as you require, and click "Apply" button to associate this alarm object with the alarm policy.
![](//mc.qcloudimg.com/static/img/2e7b0fd3a6c3b53b29f2c9665f1925f2/image.png)

## Set an Object to Receive Alarms
Alarm receiving objects determine who can receive the alarm information. The alarm receiving object can be set through the following procedure.
1. Log in to the [Management Console](https://console.client.monitor/overview) under the cloud monitoring and then click "My Alarms" > "Alarm Policies". In the alarm policy list page, click the Alarm Policy just created by you.
![](//mc.qcloudimg.com/static/img/6f881d6e32e9ab3df483bd1821d7fb64/image.png)
1. On the page of **Manage Alarm Policies**, click "Manage Alarm Receiving Groups" on the detail page.
![](//mc.qcloudimg.com/static/img/a8c1dd33a761c4758d5bd203242b7f04/image.png)
2. Select the user group to be notified, and then click "Save" to complete the alarm receiving object setting.
![](//mc.qcloudimg.com/static/img/e33bb450c694a5672050ab70d0ad8b0a/image.png)

[1]:	https://cloud.tencent.com/doc/product/248/1073
[2]:	https://console.cloud.tencent.com/
[3]:	https://console.cloud.tencent.com/
[4]:	https://console.cloud.tencent.com/

