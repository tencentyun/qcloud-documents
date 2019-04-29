
Here we describe how to access Failure Self-recovery in some common alarm scenarios during OPS.

## 1. PING Alarm
When a PING alarm is generated, you can restart the server for recovery.

Therefore, we enable the self-recovery package '"Quickly" Restart Tencent Cloud CVM' for unreachable PING alarms.
![](https://mc.qcloudimg.com/static/img/8a43e97cfc6b807d744deaa57d2f0b6a/14955064369949.jpg)

A corresponding Self-recovery record can be found in "Self-recovery Details".
![](https://mc.qcloudimg.com/static/img/262cf8fdafee5f3e41be278e914640ed/14955066069489.jpg)

By clicking ![](https://mc.qcloudimg.com/static/img/fdab933ea1b4470756182a16fe4a3793/14955069261567.jpg), you can see the execution details of this self-recovery record.

If the execution fails, you can choose to retry.

![](https://mc.qcloudimg.com/static/img/64ed497358db7fdf9d2bd011fcc09f8d/14955066257255.jpg)
    
## 2. Process Alarm #
In addition to standalone server performance alarm, Failure Self-recovery can also be used to handle service alarms, such as process alarm.

For example, if nginx process is interrupted, you need to start the nginx process.

> The following takes Nginx process alarm as an example to show how to access Self-recovery.

### 2.1 Write a Job to Start Nginx Process ##
![](https://mc.qcloudimg.com/static/img/5fd5977c4d85e50fa02c3361a9c9eafd/14955087013221.jpg)
Write a script on BlueKing "Job Platform" to start Nginx process.
(In addition to starting the process, you can also add the logic of process detection to the script, to ensure that the process is correctly started.)

### 2.2 Create Self-recovery Package to Start Nginx ##
![](https://mc.qcloudimg.com/static/img/59cf21b5cd80e5d624292be0968ee22c/14955086379695.jpg)

### 2.3 Access Self-recovery ##
![](https://mc.qcloudimg.com/static/img/2bf4e8a4906c230191b25ebf5f4ed3a5/14955317848864.jpg)


## 3. Port Alarm #
When a port alarm is triggered, a process alarm is not necessarily triggered, because the process may be frozen but still exists.
Therefore, it is necessary to configure port alarms with Failure Self-recovery.

Since the configuration for port alarms is similar to that of process alarms, please see the settings of process alarm.

## 4. Traffic Alarm #
You need also to pay attention to the ENI traffic alarm, and analyze which services have occupied the bandwidth and whether traffic limit is required to avoid the overall service being affected.

Alarms related to network traffic including public network outbound bandwidth, private network outbound bandwidth, public network inbound bandwidth and private network inbound bandwidth can be configured with Failure Self-recovery.
![](https://mc.qcloudimg.com/static/img/1c59476c357d4be696087ae25b28e3f3/14955129158481.jpg)

![](https://mc.qcloudimg.com/static/img/1b4092cec3bd618b21b5b6b7f1c5157c/14955127999644.jpg)

## 5. Memory Utilization Alarm #
Generally, when a memory utilization alarm is generated, we must find out the process by which this alarm is triggered.

Therefore, a Self-recovery package '"Quickly" Send the List of TOP 10 Processes with High Memory Utilization (Applicable to Linux)' is built in to analyze memory utilization.

Access method is shown as follows:
![](https://mc.qcloudimg.com/static/img/de5979e867995993f4391c8e12b5b618/14955213210764.jpg)

The following is the result of memory utilization analysis sent to your WeChat.
![-w345](https://mc.qcloudimg.com/static/img/b81dea3ba8d06ee53be68acd12e23612/14955212081726.jpg)

> You can see the AgentWorker with the highest memory utilization

## 6. CPU Utilization Alarm #
The analysis of CPU utilization alarm is similar to that of memory utilization alarm. You can make an alarm analysis for the CPU utilization of the operating system.

![](https://mc.qcloudimg.com/static/img/26ecca4dbfdecaef9b2b7d2cc89fa168/14955224685893.jpg)









