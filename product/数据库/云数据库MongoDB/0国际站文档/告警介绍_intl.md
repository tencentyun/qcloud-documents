You can create an alarm to trigger warnings and send relevant messages in case of the status change of a cloud product. The created alarm determines whether to trigger a notification according to the comparison result between a monitored metric and a specific threshold at regular interval.<br>
The alarm triggered by the status change allows you to take precautionary or remedial measures in a timely manner. Therefore, creating a valid alarm can help you improve your application's robustness and reliability. For more information on alarms, see [Create Alarm](https://cloud.tencent.com/document/product/248/1073) of Basic Cloud Monitor.<br>
To send an alarm of a certain status of a product, you need to create an alarm policy first. An alarm policy consists of three essential components: name, type, and triggering condition. Each alarm policy is a set of triggering conditions with the logic relationship "or", that is, an alarm is triggered when any of the conditions is met. The alarm is sent to all users associated with the alarm policy. After receiving the alarm, you can view it and take appropriate actions in time.<br>
> Note:
> Make sure that you have set default alarm receivers, otherwise you will not be informed by the default alarm policy of TencentDB for MongoDB.

You can create an alarm policy by following the steps below:<br>
1. On the Tencent Cloud console, click the **Products** -> **Monitor & Management** -> **Cloud Monitoring** in the navigation bar to go to the Cloud Monitoring [console](https://console.cloud.tencent.com/monitor/overview).
![](https://main.qcloudimg.com/raw/74838527f1658f138a8a8a995f3a2905.png)
2. Click **My Alarms** -> **Alarm Policy**, and click the **Add** button on the alarm policy list page.
![](https://main.qcloudimg.com/raw/f0cc5ea11837428ee8881c4b1cfe9b36.png)
3. The alarm configuration mainly includes the basic configuration, alarm policy and alarm rule. The basic configuration includes the Policy Name, PolicyType, Project and Alarm Object. You can use a custom policy name. Choose "CDB (MongoDB)" for Policy Type, and choose a project based on your needs. You can select all instances or some instances for the Alarm Object. See the figure below:<br>
![](https://main.qcloudimg.com/raw/b5c20b114738f45ba12b5e8cb89d7796.png)
For the alarm policy, you need to configure a triggering condition, which is a semantic condition consisting of metric, comparison relation, threshold, period and number of periods. For example, if the metric is the disk utilization, the comparison relation is >, the threshold is 80%, the period is 5 minutes, and the number of periods is 2, this means that the data of the disk utilization is collected every 5 minutes. If the utilization of a database is higher than 80% for 2 consecutive periods, an alarm is triggered.
![](https://main.qcloudimg.com/raw/9d319db0778542545b9688a7c27bcc8a.png)
The settings of the alarm rule include the Recipient Group, Alarm Channel and Port Callback. Select a user group that needs to receive alarms in the recipient group. The Alarm Channel supports sending alarms via SMS message, WeChat and email. Enter a URL that can be accessed via the public network as the Port Callback (domain name or IP [:port][/path]). Cloud Monitoring will push the alarm information to the IP address in a timely manner.
![](https://main.qcloudimg.com/raw/54a606ea9220e07aa2096d9e8a3fa077.png)

