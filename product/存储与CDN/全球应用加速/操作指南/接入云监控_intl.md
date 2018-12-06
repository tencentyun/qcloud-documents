Alarm rules can be configured in **Cloud Monitoring**. An alarm is triggered immediately when the alarm condition set for the acceleration tunnel is reached. 
Log in to the [**Cloud Monitoring**](https://console.cloud.tencent.com/monitor/policylist/add) console to do the following.

## Monitor Acceleration Tunnel
1. On **Cloud Monitoring** -> **My Alarms** -> **Alarm Policy** page, click **Add** to enter the new policy page.
2. Select **GAAP** -> **Acceleration Connection** in **Policy Type**.
 In the "Alarm Policy", three types of alarm objects are supported, including the "inbound bandwidth of public network", "outbound bandwidth of public network", and "concurrence". You can configure specific policies as required. See the figure below:
![](https://main.qcloudimg.com/raw/ff9a7e13bbcec3ce67ec46fa2cc3400c.jpg)

## Monitor Listener
1. On **Cloud Monitoring** -> **My Alarms** -> **Alarm Policy** page, click **Add** to enter the new policy page.
2. In **Policy Type**, select **GAAP** -> **Acceleration Tunnel Listener**.
 The alarm of "Abnormal listener origin" is supported in "Alarm Policy". When an origin server is found to be exceptional, an alarm is triggered by Cloud Monitor. See the figure below: 
![](https://main.qcloudimg.com/raw/9f3a1015d68bb96cf8af470479f6d1e1.jpg)

