A user needs to create an alarm policy first before sending an alarm for a certain status of a product. An alarm policy consists of three essential components: name, type, and trigger condition. You can create an alarm policy by following the steps below:

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Cloud Monitoring" - "My Alarms" tab, and then click "Alarm Policy" button.

2) Click "Add Alarm Policy" button on the alarm policy list page. Note that the "Applied" field in the alarm policy list indicates the number of [associated alarm objects](/doc/product/248/6216) with this alarm policy. If the value of Applied is not 0, the policy cannot be deleted, unless the association between alarm objects and the policy has been canceled.

3) Setting up alarm trigger condition 

In the "Add Alarm Policy" pop-up box, enter the policy name and select the policy type (the product to which the policy is applied) and alarm trigger condition.

 - The trigger condition is a semantic condition consisting of metric, comparison relation, threshold, measurement period and lasting period. For example, when the metric is `CPU utilization`, the comparison relation is `>`, the threshold is `80%`, the measurement period is `5 minutes` and the lasting period is `2 periods`, it means that the data on CPU utilization is collected every 5 minutes. If the CPU utilization of a CVM is successively larger than 80% for twice, an alarm will be triggered.
 - An alarm policy group consists of a set of alarm trigger conditions.
 - The logical relationship among them is "or", that is, as long as one of the conditions is satisfied, an alarm will be triggered.

> Note:

- The CVM alarm can be sent normally only after CVM instances [install monitoring components](/doc/product/248/6211) and report data for monitoring metrics. On the alarm object page, you can view the CVMs without the monitoring agent, and download the IP list.
- A maximum of fifteen alarm policies can be created for each policy type per project.

4. Setting up repeated alarm policy

You can set up a repeated alarm policy for each of the alarm policies. That is, when an alarm occurs, you can custom the alarm to repeatedly inform at a specific frequency.

Optional：not repeat,five minutes, ten minutes, periodic index increments ... and so on

 
Note: The meaning of the periodic index incrementing is that when the alarm is triggered for the 1st, 2nd, 4th, 8th ...2^nth time, an alarm message is sent, indicating that the interval of sending alarm message will be longer and longer in order to avoid the disturbance to some extent caused by repeated alarms.


>Default logic of repeated alarm：
>
>Within 24 hours after the alarm is generated, the alarm message will be repeatedly sent to you according to the repetition frequency you set. 
>
>After the alarm is generated for 24 hours, the system will switch to the default policy to notify the user once in one day. 
>
>After the alarm is generated for 72 hours, the alarm message will be sent for the last time.

5)You can set an existing policy as a default alarm policy. The newly purchased CVM will automatically be associated with the default alarm policy.
![](//mccdn.qcloud.com/img568a63ffe4329.png)

> Note:
>- Each policy type has only one default policy.
>- The default alarm policy cannot be deleted.
>- For the convenience of users, Cloud Monitor will automatically create a default CVM alarm policy (the alarm trigger conditions are read-only disk, and unreachable ping), and a default cloud database policy (total disk capacity > 90 MB or disk utilization > 80% for 5 minutes)
