When the status of certain product is changed, you can create an alarm to notify you in time to take action. The alarm monitors certain specific metrics over a period of time and sends alarms based on the given thresholds at intervals.

The alarm consists of the following components:

- Alarm trigger conditions (under what conditions to send alarms)
- Alarm object (which object issues an alarm)
- Alarm receiver group (who will receive the alarm)
- Alarm reception methods (how to receive the alarm)

You can learn how to create an alarm for one or more objects, and select the objects that need to receive alarms from this section.

## Basic Concepts
| Term          | Term                                       |
| ----------- | ---------------------------------------- |
| Alarm policy type      | It is used to identify policy types, which corresponds to the cloud products. For example, when you select a CVM policy, you can customize CPU utilization, disk utilization and other metric alarms |
| Alarm type        | It is the specific type of an alarm, which is the segmentation of policy types. For example, there are several alarm types of CVM policy types, including disk utilization alarm, unreachable ping alarm and memory utilization alarm |
| Relations between policy type and alarm type | A policy type contains several alarm types. It is a set of alarm types. For example, CVM policy contains disk utilization alarm, unreachable ping alarm and memory utilization alarm |
| Alarm policy        | An alarm policy is a set of alarm trigger conditions. The alarm policy is associated with projects and policy types. For each policy type, 15 alarm policies can be created for each project |
| Alarm trigger conditions      | The alarm trigger condition are the bases for the alarm. Only the conditions are met can the alarm be triggered. The maximum number of trigger conditions of each alarm policy can be equal to the amount of metrics. <font color="red">The logical relationship among them is "or", that is, as long as one of the conditions is satisfied, an alarm will be triggered</font> |
| Default policy        | CVM policy has only one default policy, which can be modified but cannot be deleted           |

## Alarm Statuses
<table class="t">
<tbody><tr>
<th> <b>Alarm Status</b>
</th><th> <b>Description</b>
</th></tr>
<tr>
<td> <b>Not recovered</b>
</td><td> The alarm is not processed or is being processed.
</td></tr>
<tr>
<td> <b>Recovered</b>
</td><td> The alarm has been recovered to a normal status.
</td></tr>
<tr>
<td> <b>Insufficient data</b>
</td><td> The alarm policy for a generated alarm has been deleted. <br>The CVM is migrated from one project to another. <br>No data is submitted if the Cloud Monitor components has not been installed or has been unmounted.
</tbody></table>
