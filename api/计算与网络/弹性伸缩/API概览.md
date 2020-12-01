## 1. 启动配置相关接口

| 接口名 | Action Name | 功能描述 | 
|---------|---------|---------|
| [创建启动配置](/doc/api/372/创建启动配置)| CreateScalingConfiguration | 创建新的启动配置，用户可以指定其名称以及其使用的 CVM 实例配置等。 | 
| [查询启动配置](/doc/api/372/查询启动配置) | DescribeScalingConfiguration | 根据用户输入信息，如启动配置的 ID、名称等，查询对应启动配置的详细信息。|
| [删除启动配置](/doc/api/372/删除启动配置) | DeleteScalingConfiguration | 根据启动配置 ID 删除对应的启动配置。|

## 2. 伸缩组相关接口

| 接口名 | Action Name | 功能描述 |
|---------|---------|---------|
| [创建伸缩组](/doc/api/372/创建伸缩组) | CreateScalingGroup | 创建新的伸缩组，用户可以指定伸缩组的名称以及其最大、最小伸缩数等。 |
| [查询伸缩组列表](/doc/api/372/查询伸缩组列表) | DescribeScalingGroup | 根据用户输入信息，如伸缩组 ID、伸缩组名称等，查询对应伸缩组的详细信息。 |
| [修改伸缩组](/doc/api/372/修改伸缩组)| ModifyScalingGroup | 修改伸缩组配置，如修改伸缩组名称以及其最大、最小伸缩数等。|
| [查询伸缩组绑定的云服务器](/doc/api/372/查询伸缩组绑定的云服务器) | DescribeScalingInstance | 根据伸缩组 ID 查询其绑定的云服务器的详细信息。|
| [绑定伸缩组云服务器](/doc/api/372/绑定伸缩组云服务器) | AttachInstance |根据云服务器 ID 和伸缩组 ID，将云服务器绑定至伸缩组。| 
| [解绑伸缩组云服务器](/doc/api/372/解绑伸缩组云服务器)| DetachInstance |根据云服务器 ID 和伸缩组 ID，将云服务器从伸缩组中解绑。|
| [删除伸缩组](/doc/api/372/删除伸缩组) | DeleteScalingGroup | 根据伸缩组 ID 删除对应的伸缩组。 |

## 3. 告警触发策略相关接口

| 接口名 | Action Name | 功能描述 |
|---------|---------|---------|
| [创建告警触发策略](/doc/api/372/创建告警触发策略)| CreateScalingPolicy | 创建新的告警触发策略，根据伸缩组 ID，用户可以为特定伸缩组创建伸缩策略。|
| [查询告警触发策略](/doc/api/372/查询告警触发策略) | DescribeScalingPolicy | 根据伸缩组 ID 查询其在告警触发的伸缩活动中采用的具体伸缩策略。|
| [删除告警触发策略](/doc/api/372/删除告警触发策略)| DeleteScalingPolicy | 根据伸缩组 ID 和伸缩策略 ID，删除指定伸缩组中特定的伸缩策略。|

## 4. 定时任务相关接口

| 接口功能 | Action Name | 功能描述 |
|---------|---------|---------|
| [创建定时任务](/doc/api/372/创建定时任务) | CreateScheduledTask | 创建新的定时任务，根据伸缩组 ID，用户可以为指定伸缩组创建特定定时任务。|
| [查询定时任务](/doc/api/372/查询定时任务)  | DescribeScheduledTask| 根据伸缩组 ID 或定时任务 ID，查询伸缩组中所有或特定定时任务的具体信息。 |
| [修改定时任务](/doc/api/372/修改定时任务) | ModifyScheduledTask | 修改定时任务配置，如修改定时任务名、定时任务触发时，重设伸缩组的最大、最小伸缩数等。|
| [删除定时任务](/doc/api/372/删除定时任务) | DeleteScheduledTask | 根据伸缩组 ID 和定时任务 ID，删除特定伸缩组中特定的定时任务。|

## 5. 通知相关接口
| 接口功能 | Action Name | 功能描述 |
|---------|---------|---------|
| [创建通知](/doc/api/372/创建通知) | CreateScalingNotification | 创建新的通知，根据伸缩组 ID，用户可以为指定伸缩组创建特定的伸缩活动结果通知。|
| [查询通知](/doc/api/372/查询通知)  | DescribeScalingNotification| 根据伸缩组 ID 或通知 ID，查询伸缩组中所有或特定通知的具体信息。 |
| [修改通知](/doc/api/372/修改通知) | ModifyScalingNotification | 修改通知配置，如修改通知的通知类型、通知的接收对象等。|
| [删除通知](/doc/api/372/删除通知) | DeleteScalingNotification | 根据伸缩组 ID 和通知 ID，删除特定伸缩组中特定的通知。|
