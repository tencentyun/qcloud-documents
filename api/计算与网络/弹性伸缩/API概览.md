
## 1. 启动配置相关接口

| 接口名 | Action Name | 功能描述 | 
|---------|---------|---------|
| [创建启动配置](/doc/api/372/创建启动配置)| CreateScalingConfiguration | 创建新的启动配置，用户可以指定其名称以及其使用的CVM实例配置等。 | 
| [查询启动配置](/doc/api/372/查询启动配置) | DescribeScalingConfiguration | 根据用户输入信息，如启动配置的ID、名称等，查询对应启动配置的详细信息。|
| [删除启动配置](/doc/api/372/删除启动配置) | DeleteScalingConfiguration | 根据启动配置ID删除对应的启动配置。|

## 2. 伸缩组相关接口

| 接口名 | Action Name | 功能描述 |
|---------|---------|---------|
| [创建伸缩组](/doc/api/372/创建伸缩组) | CreateScalingGroup | 创建新的伸缩组，用户可以指定伸缩组的名称以及其最大、最小伸缩数等。 |
| [查询伸缩组列表](/doc/api/372/查询伸缩组列表) | DescribeScalingGroup | 根据用户输入信息，如伸缩组ID、伸缩组名称等，查询对应伸缩组的详细信息。 |
| [修改伸缩组](/doc/api/372/修改伸缩组)| ModifyScalingGroup | 修改伸缩组配置，如修改伸缩组名称以及其最大、最小伸缩数等。|
| [查询伸缩组绑定的云服务器](/doc/api/372/查询伸缩组绑定的云服务器) | DescribeScalingInstance | 根据伸缩组ID查询其绑定的云服务器的详细信息。|
| [绑定伸缩组云服务器](/doc/api/372/绑定伸缩组云服务器) | AttachInstance |根据云服务器ID和伸缩组ID，将云服务器绑定至伸缩组。| 
| [解绑伸缩组云服务器](/doc/api/372/解绑伸缩组云服务器)| DetachInstance |根据云服务器ID和伸缩组ID，将云服务器从伸缩组中解绑。|
| [删除伸缩组](/doc/api/372/删除伸缩组) | DeleteScalingGroup | 根据伸缩组ID删除对应的伸缩组。 |

## 3. 告警触发策略相关接口

| 接口名 | Action Name | 功能描述 |
|---------|---------|---------|
| [创建告警触发策略](/doc/api/372/创建告警触发策略)| CreateScalingPolicy | 创建新的告警触发策略，根据伸缩组ID，用户可以为特定伸缩组创建伸缩策略。|
| [查询告警触发策略](/doc/api/372/查询告警触发策略) | DescribeScalingPolicy | 根据伸缩组ID查询其在告警触发的伸缩活动中采用的具体伸缩策略。|
| [删除告警触发策略](/doc/api/372/删除告警触发策略)| DeleteScalingPolicy | 根据伸缩组ID和伸缩策略ID，删除指定伸缩组中特定的伸缩策略。|

## 4. 定时任务相关接口

| 接口功能 | Action Name | 功能描述 |
|---------|---------|---------|
| [创建定时任务](/doc/api/372/创建定时任务) | CreateScheduledTask | 创建新的定时任务，根据伸缩组ID，用户可以为指定伸缩组创建特定定时任务。|
| [查询定时任务](/doc/api/372/查询定时任务)  | DescribeScheduledTask| 根据伸缩组ID或定时任务ID，查询伸缩组中所有或特定定时任务的具体信息。 |
| [修改定时任务](/doc/api/372/修改定时任务) | ModifyScheduledTask | 修改定时任务配置，如修改定时任务名、定时任务触发时，重设伸缩组的最大、最小伸缩数等。|
| [删除定时任务](/doc/api/372/删除定时任务) | DeleteScheduledTask | 根据伸缩组ID和定时任务ID，删除特定伸缩组中特定的定时任务。|

## 5. 通知相关接口
| 接口功能 | Action Name | 功能描述 |
|---------|---------|---------|
| [创建通知](/doc/api/372/创建通知) | CreateScalingNotification | 创建新的通知，根据伸缩组ID，用户可以为指定伸缩组创建特定的伸缩活动结果通知。|
| [查询通知](/doc/api/372/查询通知)  | DescribeScalingNotification| 根据伸缩组ID或通知ID，查询伸缩组中所有或特定通知的具体信息。 |
| [修改通知](/doc/api/372/修改通知) | ModifyScalingNotification | 修改通知配置，如修改通知的通知类型、通知的接收对象等。|
| [删除通知](/doc/api/372/删除通知) | DeleteScalingNotification | 根据伸缩组ID和通知ID，删除特定伸缩组中特定的通知。|

## 6. 生命周期钩子相关接口
| 接口功能 | Action Name | 功能描述 |
|---------|---------|---------|
| [创建生命周期钩子](/doc/api/372/创建生命周期钩子) | CreateLifeCycleHook | 每个伸缩组可以创建最多10个生命周期钩子，但同一时刻只能其中一个生命周期钩子生效（可以调用绑定生命周期钩子接口触发生命周期钩子生效）。|
| [修改生命周期钩子](/doc/api/372/修改生命周期钩子) | ModifyLifeCycleHook | 修改生命周期钩子的相关参数，包括生命周期钩子的名字、超时时间、默认超时动作、触发回调条件、通知组。|
| [查询生命周期钩子](/doc/api/372/查询生命周期钩子) | DescribeLIfeCycleHook | 查询用户组下所有的生命周期钩子或者某个特定的生命周期钩子。|
| [删除生命周期钩子](/doc/api/372/删除生命周期钩子) | DeleteLifeCycleHook | 删除伸缩组中某个特定的生命周期钩子。|
| [绑定生命周期钩子](/doc/api/372/绑定生命周期钩子) | AttachLifeCycleHookId | 将生命周期钩子和伸缩组绑定，激活伸缩组当前需要使用的生命周期钩子。|
| [解绑生命周期钩子](/doc/api/372/解绑生命周期钩子) | DetachLifeCycleHookId | 将生命周期钩子和伸缩组解绑，如需激活生命周期钩子需要重新绑定|
| [生命周期钩子回调完成通知](/doc/api/372/生命周期钩子回调完成通知) | CompleteLifeCycleHookAction | 调用此接口提前完成生命周期钩子回调。|
| [生命周期钩子延期时间续订](/doc/api/372/生命周期钩子延期时间续订) | RecordLifeCycleHookTimeout | 用于生命周期钩子延期时间的续订。|