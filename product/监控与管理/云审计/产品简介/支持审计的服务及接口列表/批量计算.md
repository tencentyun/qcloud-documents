腾讯云批量计算（BatchCompute，Batch），您可以在云服务器上运行批量计算工作负载。Batch 是开发人员、科学家和工程师用来访问大量计算资源的常见方法，并且 Batch 可以免去配置和管理所需基础设施的繁重工作。Batch 与传统的批量计算软件类似。此服务可以有效地预配置资源以响应提交的作业，达到消除容量限制、降低计算成本和快速交付的目的。



下表为云审计支持的批量计算操作列表：

| 操作名称	| 资源类型                          | 事件名称 |
|------------|------------------------------|------------|
| 创建计算环境     | batch        | CreateComputeEnv |
| 创建黑石计算环境   | batch     | CreateCpmComputeEnv |
| 创建任务模板     | batch      | CreateTaskTemplate |
| 删除计算环境     | batch        | DeleteComputeEnv |
| 删除作业       | batch               | DeleteJob |
| 删除任务模板     | batch     | DeleteTaskTemplates |
| 查看计算环境信息   | batch      | DescribeComputeEnv |
| 查看计算环境活动信息 | batch | DescribeComputeEnvActivities |
| 查看计算环境列表   | batch     | DescribeComputeEnvs |
| 查看作业信息     | batch             | DescribeJob |
| 查看作业列表     | batch            | DescribeJobs |
| 查看作业的提交信息  | batch   | DescribeJobSubmitInfo |
| 查看任务信息     | batch            | DescribeTask |
| 获取任务日志详情   | batch        | DescribeTaskLogs |
| 查询任务模板     | batch   | DescribeTaskTemplates |
| 修改计算环境     | batch        | ModifyComputeEnv |
| 修改任务模板     | batch      | ModifyTaskTemplate |
| 提交作业       | batch               | SubmitJob |
| 终止作业       | batch            | TerminateJob |
| 终止任务实例     | batch   | TerminateTaskInstance |
