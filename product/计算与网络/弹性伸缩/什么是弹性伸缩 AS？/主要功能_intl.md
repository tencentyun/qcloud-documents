## 1. Alarm Scaling Policy
If you wish to adjust business deployment based on CVM metrics, you can customize the alarm trigger policy, which will automatically increase or decrease the number of CVM instances when business load pushes the metrics to the threshold. This flexibly deals with traffic load changes, improves device utilization, and saves deployment and instance costs.
+ Metrics include: CPU usage, memory usage, private network outbound bandwidth, private network inbound bandwidth, public network outbound bandwidth, public network inbound bandwidth
+ Monitor cycle: 5 minutes
+ Scaling operation: Increase/decrease CVM instances

## 2. Scheduled Scaling Policy
If your load changes are predictable, you can set a scheduled task to plan your scaling activities. You can use this feature to automatically increase or decrease CVM instances on a scheduled and periodical basis to flexibly deal with traffic load changes and improve device utilization while saving deployment and instance costs.
+ Scheduled operation: Configure maximum/minimum group sizes and expected number of instances
+ Cycle configuration: Scheduled operations can be performed on daily/weekly/monthly basis

## 3. Replacing Unhealthy CVMs
The auto scaling mechanism will automatically monitor the health status of instances and create healthy instances to replace any abnormal ones that have been detected, in order to ensure that your applications can acquire expected computing capacity and keep your business safe.
+ Perform action: If the monitored host does not respond to a ping for one minute, the system will create a healthy copy to replace the current CVM to keep the business healthy

## 4. Configuring Cloud Load Balancer Automatically
New CVM instances created via alarm policy can be directly associated to existing cloud load balancer (CLB) to make the new instances in the scaling group carry distributed traffic, improving service availability.
+ Perform action: Automatically register newly created CVMs to CLB
+ Weight configuration: CLB weight of newly created CVMs is set to 10 by default
+ Cloud load balance policy: Existing policies of current CLB are adopted

## 5. Scaling Activity Logs
Auto scaling mechanism will automatically increase/decrease CVM instances according to the scaling policies you have configured. You can view the execution status of scaling policies by using this feature, which will provide the statuses of scaling activities.
+ Log contents: Cause, result, start/end time of activities
+ Query operation: You can query historical records based on time
+ Real-time display: Displays changes of current scaling activities


## 6. Detecting Abnormalities in Advance
Auto scaling will detect abnormalities and notify you before scaling activity is performed, to help you solve system issues in time and ensure a smooth scaling activity. Here are the abnormalities that can be detected by auto scaling feature: Account balance is insufficient; Scaling configuration image has been deleted; CLB (other than the CLB that corresponds to scaling group) has been deleted, etc.

## 7. Scaling Activity Notification
You can configure notification policy so that auto scaling can notify you in real-time via SMS, email, internal message and other methods when specified events have occurred (such as successful/failed scaling operation, successful/failed unhealthy CVM replacement, etc.)

