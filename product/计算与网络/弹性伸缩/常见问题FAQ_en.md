## 1. What is cooldown period?
Cooldown period refers to a period of time when the corresponding scaling group is locked after a scaling activity (adding or removing CVM instances) is completed. During this period, no scaling activities are performed with the scaling group. The allowed value range for the cooling period is `0-999999` (seconds).
## 2. Is there a cooldown period for manually added CVMs?
Manually added CVMs need not to experience a cooldown period.
## 3. Is there a charge for Auto Scaling?
Auto Scaling is completely free of charge. Please feel free to use.
For CVM instances automatically created via Auto Scaling or manually added, a pay-by-usage billing mode based on the normal CVM prices will apply.
## 4. How to increase the maximum number of CVMs in the scaling group?
Currently, each Tencent Cloud user is provided with a quota of `30` pay-by-usage CVMs in each availability zone. If you want more than 30 pay-by-usage CVMs for your scaling group, please submit a ticket for application.

## 5. What kind of machine is suitable for Auto Scaling?
The applications deployed in the CVM instances in the scaling group need to be stateless and replaceable. Because instances in the scaling group are likely to be reclaimed in scaling down, CVM instances for auto scaling cannot save status information (such as sessions) and related data (such as databases, logs) of the applications. If you need to save the status information in your applications, you can consider saving it to a standalone CVM beyond the scaling group.
## 6. What are the requirements for CVMs manually added to the scaling group?
The CVMs that are manually added to the scaling group must meet the following requirements:
- Belong to the same project as the scaling group;
- Be in the same region as the scaling group;
- Reside in the same network environment (VPC or basic network) as the scaling group;
- Be in the running status.

## 7. What are the requirements for the CLB instance associated with the scaling group?
The CLB instance associated with the scaling group must be in the same network environment (VPC or the basic network of the same region) as the scaling group.


## 8. Does the Auto Scaling automatically scale up and down CVMs?
Auto Scaling (AS) is a management service that automatically adjusts the computing resources according to user's business needs and policies. It automatically scales up CVM instances during demand spikes and scales down CVM instances during demand lulls. Auto Scaling currently does not provide the option for "vertical scaling", that is, Auto Scaling is temporarily unable to automatically scale up and down the CPU, memory and bandwidth of the CVMs.

# # 9. Does auto scaling have to work with CLB and Cloud Monitor?
Auto Scaling can separately scale CVM instances up and down. It can both work with CLB or work separately.

# # 10. If I need to scale up a number of CVMs during a certain period of time, how do I set it up?
You can set a pair of scheduled tasks: one defines the scale-up operation, setting the desired number of instances to the number you want to scale up to; the other defines the scale-down operation, setting the desired number of instances to the number you want to scale down to.
See [Best Practice Examples >>](https://www.qcloud.com/document/product/377/8617#step-5.-.E8.AE.BE.E7.BD.AE.E6.89 .A9.E7.BC.A9.E5.AE.B9.E7.AD.96.E7.95.A5.EF.BC.88.E9.87.8D.E7.82.B9.EF.BC.81. EF.BC.89)

## 11. What are the specific rules for scaling group removal?
Tencent Cloud AS provides two types of removal policies:
- Delete the oldest machine: delete the oldest automatically added machine. After the automatically added machine is deleted, the earliest manually added machine will be deleted.
- Delete the latest machine: delete the latest automatically added machine. After the automatically added machine is deleted, the latest manually added machine will be deleted.

## 12. How does the alarm policy calculate the cloud monitoring information?
Take the maximum value for example. The basic rule is to take a value per minute (one value for a minute) with each passing period for the monitoring items set for each CVM. When the values taken for multiple consecutive periods (the number of periods can be customized) meet the set rules, the alarm scaling activity will be triggered.

For example, there are five CVMs in a scaling group, and the defined alarm scaling policy is "CPU utilization is more than 50% for 3 consecutive periods". The system takes a value per minute for each CVM, i.e. taking 25 CPU utilization values within one period (5 minutes). If any of the 25 values exceeds the threshold (50%), the period meets the alarm scaling rule. If the rule is met for 3 consecutive periods, the scaling activity will be triggered.

## 13. What is the desired number of instances?
The desired number of instances refers to the correct number of instances in a scaling group, which is between the minimum and maximum group sizes. You can manually adjust the desired number of instances, or use scheduled task and alarm scaling task to trigger the adjustment. The scaling group automatically adjusts the actual number of instances to make it equal to the desired number of instances.
- When a scaling group is created: If an initial number of instances is set when a scaling group is created, then that initial number of instances will be the desired number of instances.
- Alarm scaling task adjustment: When the alarm scaling is triggered, the scaling group will adjust the current number of instances to the desired number of instances. For example, if the trigger action is to add two CVMs, the backend will satisfy the desired number of instances by adding two CVMs to the current number. If the system finds that the current number of instances is not equal to the desired number of instances for the scaling group, it will add two CVMs to make them equal.
- Scheduled or manual adjustment of the desired number of instances: When the user changes the desired number of instances by means of a scheduled task or a direct modification, the system, after discovering that the current number of instances is not equal to the desired number of instances, will trigger scaling activity until the two numbers are equal.
- System adjustment: The desired number of instances is between the maximum and minimum numbers of instances. The change in maximum or minimum number of instances may result in the change in the desired number of instances. For example, if the desired number of instances is 3, the minimum group size is 2, and the maximum group size is 5, in case the minimum group size is adjusted to 4, then the desired number of instances will be adjusted to 4 to meet the minimum group size.

## 14. What should be noted when a data disk snapshot is specified in the scaling configuration?
If a data disk snapshot is specified in the scaling configuration, you need to ensure that the data disk can be mounted correctly to allow the scaling group to automatically scale up. You need to perform some operations on the original instance of the data disk snapshot before setting the auto scaling, so as to realize the automatic mounting of data disk when activating a new CVM instance.
For instructions on how to do this, refer to [How to Mount Data Disk Automatically When Activating New Instance Using Custom Image and Data Disk Snapshot>>](https://www.qcloud.com/doc/product/362/5564)

## 15. What activity will be paused when the scaling group is disabled?
After the scaling group is disabled, the auto capacity scaling of the scaling group will not be triggered, but the restrictions on the scaling group remain in effect.
When the scaling group is disabled, the automatic activities will not performed:

- Alarm scaling;
- Scheduled task;
- Health check;
- The desired number of instances does not match due to manual operation.

But in order to ensure normal running, the basic restrictions on the scaling group still apply:

- If the instances are manually removed to be less than `min`, the removal will not be allowed;
- If the instances are manually added to greater than`max`, the addition will not be allowed;
- Manually raising `min` or` max` will not trigger scaling activity.

## 16. What stages are involved in the lifecycle of the CVMs that are automatically added to the scaling group?
- Creating: a submachine is being created
- InService: a submachine is in service
- Removing: a submachine is being removed
- Attaching: a submachine is being attached to the scaling group
- Detaching: a submachine is being detached from the scaling group
- AttachLb: a submachine is being attached to an LB
- DetachLb: a submachine is being detached from an LB
- Prefetching: a submachine is being prefetched

