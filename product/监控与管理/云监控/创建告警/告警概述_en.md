When the status of certain product is changed, you can create an alarm to notify you in time to take action. The alarm monitors certain specific metrics over a period of time and sends alarms based on the given thresholds at intervals.

The alarm consists of the following components:

- Alarm trigger conditions (under what conditions to send alarms)
- Alarm object (which object issues an alarm)
- Alarm receiver group (who will receive the alarm)
- Alarm reception methods (how to receive the alarm)

You can learn how to create an alarm for one or more objects, and select the objects that need to receive alarms from this section.

## Basic Concepts
| Term          | Definition                                       |
| ----------- | ---------------------------------------- |
| Alarm policy type | It is used to identify policy types, which corresponds to the cloud products. For example, when you select a CVM policy, you can customize CPU utilization, disk utilization and other metric alarms. |
| Alarm type | It corresponds to specific monitoring metric. For example, CVM policy type includes several alarm types, such as disk utilization alarm, unreachable ping alarm, memory utilization alarm, and so on.|
| Relations between policy type and alarm type| A policy type contains several alarm types. It is a set of alarm types. For example, CVM policy contains disk utilization alarm, unreachable ping alarm and memory utilization alarm. |
| Alarm policy group | An alarm policy group consists of a set of alarm trigger conditions. The alarm policy is associated with projects and policy types. For each policy type, fifteen alarm policy groups can be created for each project.|
| Default policy group| For each project, every policy type has and only has one default policy group. The system will self create default policy which can be modified but cannot be deleted after users purchase CVM. Note: The present alarm policy created by system by default can receive the alarm message from the default alarm policy only when users bind the default policy group with the alarm receiver group.|

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
</td><td> The alarm policy for a generated alarm has been deleted. <br>The CVM is migrated from one project to another. <br>No data is submitted if the Cloud Monitor components have not been installed or have been unmounted.
</tbody></table>
