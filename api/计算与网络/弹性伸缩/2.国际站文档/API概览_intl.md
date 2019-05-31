
## 1. Scaling Configuration-related APIs

| API | Action Name | Description | 
|---------|---------|---------|
| [Create Scaling Configuration](/doc/api/372/创建启动配置)| CreateScalingConfiguration | Create a new scaling configuration and the user can specify its name and the CVM instance configuration it uses, and so on.   | 
| [Query Scaling Configuration](/doc/api/372/查询启动配置) | DescribeScalingConfiguration | Query the details of the corresponding scaling configuration based on the user input information, such as the scaling configuration ID, name, and so on. |
| [Delete Scaling Configuration](/doc/api/372/删除启动配置) | DeleteScalingConfiguration | Delete the corresponding scaling configuration according to the scaling configuration ID.  |

## 2. Scaling Group-related APIs

| API | Action Name | Description |
|---------|---------|---------|
| [Create Scaling Group](/doc/api/372/创建伸缩组) | CreateScalingGroup | Create a new scaling group, and the user can specify its name, the maximum and minimum group size and so on.  |
| [Query Scaling Group List](/doc/api/372/查询伸缩组列表) | DescribeScalingGroup | Query the details of the corresponding scaling group based on user input information such as the scaling group ID, name and so on.  |
| [Modify Scaling Group](/doc/api/372/修改伸缩组) | ModifyScalingGroup | Modify scaling group configuration, such as its name, the maximum and minimum scalability and so on. |
| [Query CVM Bound to Scaling Group ](/doc/api/372/查询伸缩组绑定的云服务器) | DescribeScalingInstance | Query the details of CVM bound to the scaling group based on its ID. |
| [Bind CVM to Scaling Group](/doc/api/372/绑定伸缩组云服务器) | AttachInstance | Bind CVM to scaling group based on the CVM ID and scaling group ID. | 
| [Unbind CVM from Scaling Group ](/doc/api/372/解绑伸缩组云服务器) | DetachInstance | Unbind CVM from scaling group based on the CVM ID and scaling group ID. |
[Delete Scaling Group](/doc/api/372/删除伸缩组) | DeleteScalingGroup | Delete the corresponding scaling group according to its ID.  |

## 3. Alarm Trigger Policy-related APIs

| API | Action Name | Description |
|---------|---------|---------|
| [Create Alarm Trigger Policy](/doc/api/372/创建告警触发策略) | CreateScalingPolicy | Create a new alarm trigger policy that allows users to create a scaling policy for a specific scaling group based on the scaling group ID.  |
| [Query Alarm Trigger Policy](/doc/api/372/查询告警触发策略) | DescribeScalingPolicy | Query the specific scaling strategy used in the scaling activity triggered by the alarm according to the scaling group ID. |
| [Delete Alarm Trigger Policy](/doc/api/372/删除告警触发策略) | DeleteScalingPolicy | Delete a specific scaling policy in the specified scaling group based on the scaling group ID and the scaling policy ID. |

## 4. Scheduled Task-related APIs

| API Function | Action Name | Function Description |
|---------|---------|---------|
| [Creates Scheduled Task](/doc/api/372/创建定时任务) | CreateScheduledTask | Creates a new scheduled task. The user can create a specific scheduled task for the specified scaling group according to the scaling group ID. |
| [Query Scheduled Task](/doc/api/372/查询定时任务) | DescribeScheduledTask | Query the details of all or specific scheduled tasks in a scaling group based on the scaling group ID or scheduled task ID.  |
| [Modify Scheduled Task](/doc/api/372/修改定时任务) | ModifyScheduledTask | Modify the scheduled task configuration, such as modifying the scheduled task name, and setting the maximum and minimum size of the scaling group when the scheduled task is triggered. |
[Delete Scheduled Task](/doc/api/372/删除定时任务) | DeleteScheduledTask | Delete a specific scheduled task in a specific scaling group based on the scaling group ID and the scheduled task ID. |

## 5. Notification-related APIs
| API Function | Action Name | Function Description |
|---------|---------|---------|
| [Create Notification](/doc/api/372/创建通知) | CreateScalingNotification | Create a new notification; the user can create a specific scaling activity result notification for the specified scaling group according to the scaling group ID. |
| [Query Notification](/doc/api/372/查询通知) | DescribeScalingNotification | Query the details of all or specific notifications in a scaling group based on the scaling group ID or notification ID.  |
| [Modify Notification](/doc/api/372/修改通知) | ModifyScalingNotification | Modify notification configuration, such as the notification type or recipient, and so on. |
| [Delete notification](/doc/api/372/删除通知) | DeleteScalingNotification | Delete a specific notification in a specific scaling group based on the scaling group ID and notification ID. |

## 6. Lifecycle Hook-related APIs
| API Function | Action Name | Function Description |
|---------|---------|---------|
| [Create Lifecycle Hook](/doc/api/372/创建生命周期钩子) | CreateLifeCycleHook | You can create up to 10 lifecycle hooks for each scaling group, but only one lifecycle hook takes effect at a time (you can call API "Bind Lifecycle Hook" to trigger the lifecycle hook to take effect). |
| [Modify Lifecycle Hook](/doc/api/372/修改生命周期钩子) | ModifyLifeCycleHook | Modify the parameters of a lifecycle hook, including the name, timeout, default timeout action, callback trigger condition, and notification group of the life cycle hook. |
| [Query Lifecycle Hook](/doc/api/372/查询生命周期钩子) | DescribeLIfeCycleHook | Query all lifecycle hooks or a specific lifecycle hook under a user group. |
| [Delete lifecycle Hook](/doc/api/372/删除生命周期钩子) | DeleteLifeCycleHook | Delete a specific lifecycle hook in the scaling group. |
| [Bind Lifecycle Hook](/doc/api/372/绑定生命周期钩子) | AttachLifeCycleHookId | Bind the lifecycle hooks to the scaling group, activating the lifecycle hook that the scaling group currently needs to use. |
| [Unbind Lifecycle Hook](/doc/api/372/解绑生命周期钩子) | DetachLifeCycleHookId | Unbind lifecycle hooks from the scaling group; if you need to activate the lifecycle hooks, you should rebind them |
| [Lifecycle Hook Callback Completion Notification](/doc/api/372/生命周期钩子回调完成通知) | CompleteLifeCycleHookAction | This API is used to complete the lifecycle hook callback in advance. |
| [Lifecycle Hook Timeout Renewal](/doc/api/372/生命周期钩子延期时间续订) | RecordLifeCycleHookTimeout | It is used to renew a lifecycle hook timeout. |
