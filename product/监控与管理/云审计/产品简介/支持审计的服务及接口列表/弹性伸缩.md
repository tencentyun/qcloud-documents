腾讯云弹性伸缩（Auto Scaling，AS）为您提供高效管理计算资源的策略。您可设定时间周期性地执行管理策略或创建实时监控策略，来根据实时需求自动增加或减少 CVM 实例数量，同时完成实例的环境部署，保证业务平稳运行和最大程度的降低成本。 弹性伸缩策略不仅能够让需求稳定规律的应用程序实现自动化管理，同时告别业务突增或 CC 攻击等带来的烦恼，对于需求不规律的应用程序，还能够根据业务负载分钟级扩展。弹性伸缩策略能够让您的集群在任何时间都保持恰到好处的实例数量。

下表为云审计支持的弹性伸缩操作列表：

| 操作名称	| 资源类型                       | 事件名称 |
|----------------|----------------------------------------|----------------|
| 添加 CVM 实例到伸缩组  | as                      | AttachInstances |
| 完成生命周期动作       | as              | CompleteLifecycleAction |
| 创建伸缩组          | as               | CreateAutoScalingGroup |
| 创建启动配置         | as            | CreateLaunchConfiguration |
| 创建生命周期挂钩       | as                  | CreateLifecycleHook |
| 创建通知           | as      | CreateNotificationConfiguration |
| 创建告警触发策略       | as                  | CreateScalingPolicy |
| 创建定时任务         | as                | CreateScheduledAction |
| 删除伸缩组          | as               | DeleteAutoScalingGroup |
| 删除启动配置         | as            | DeleteLaunchConfiguration |
| 删除生命周期挂钩       | as                  | DeleteLifecycleHook |
| 删除通知           | as      | DeleteNotificationConfiguration |
| 删除告警触发策略       | as                  | DeleteScalingPolicy |
| 删除定时任务         | as                | DeleteScheduledAction |
| 查询伸缩活动         | as        | DescribeAutoScalingActivities |
| 查询伸缩组最新一次伸缩活动  | as | DescribeAutoScalingGroupLastActivities |
| 查询伸缩组          | as            | DescribeAutoScalingGroups |
| 查询实例           | as         | DescribeAutoScalingInstances |
| 查询启动配置         | as         | DescribeLaunchConfigurations |
| 查询生命周期挂钩       | as               | DescribeLifecycleHooks |
| 查询通知           | as   | DescribeNotificationConfigurations |
| 查询告警触发策略       | as              | DescribeScalingPolicies |
| 查询定时任务         | as             | DescribeScheduledActions |
| 从伸缩组移出 CVM 实例  | as                      | DetachInstances |
| 停用伸缩组          | as              | DisableAutoScalingGroup |
| 启用伸缩组          | as               | EnableAutoScalingGroup |
| 触发伸缩策略         | as                 | ExecuteScalingPolicy |
| 修改伸缩组          | as               | ModifyAutoScalingGroup |
| 修改期望实例数        | as                | ModifyDesiredCapacity |
| 修改启动配置属性       | as  | ModifyLaunchConfigurationAttributes |
| 修改伸缩组的负载均衡器    | as                  | ModifyLoadBalancers |
| 修改通知           | as      | ModifyNotificationConfiguration |
| 修改告警触发策略       | as                  | ModifyScalingPolicy |
| 修改定时任务         | as                | ModifyScheduledAction |
| 从伸缩组中删除 CVM 实例 | as                      | RemoveInstances |
| 设置实例移出保护       | as               | SetInstancesProtection |
| 关闭伸缩组内 CVM 实例  | as             | StopAutoScalingInstances |
| 升级生命周期挂钩       | as                 | UpgradeLifecycleHook |
