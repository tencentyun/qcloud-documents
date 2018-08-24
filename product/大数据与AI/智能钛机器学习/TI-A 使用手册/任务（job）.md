Job 代表一个训练任务，他定义了训练该如何在腾讯云上执行。每一个 Job 对应以下字段：

| 参数名称              | 类型         | 添加者     | 描述                                                |
| :------------------- | :----------- | :-------- | --------------------------------------------------- |
| Name                 |`string`      | 用户必填   | 任务的名称，每个集群中该名称必须唯一。                   |
| PackageDir           |`[string]`    | 用户必填   | 训练代码/数据或输出路径，详见 [文件路径](https://cloud.tencent.com/document/product/851/17318)。     |
| Command              |`[string]`    | 用户必填   | 任务启动命令。                                        |
| Args                 |`[string]`    | 用户必填   | 任务启动参数。                                        |
| Cluster              |`string`      | 用户设置   | 运行集群， 详见 [使用集群](https://cloud.tencent.com/document/product/851/17317)。                   |
| ScaleTier            |`string`      | 用户选填   | 用以规定运行训练的方式和规模，详见 [训练规模](https://cloud.tencent.com/document/product/851/17319)。 |
| MasterType           |`string`      | 用户选填   | Master/Driver 节点的类型，详见 [训练规模](https://cloud.tencent.com/document/product/851/17319)。           |
| WorkerType           |`string`      | 用户选填   | Worker/Executor 节点的类型，详见 [训练规模](https://cloud.tencent.com/document/product/851/17319) 。          |
| ParameterServerType               |`string`      | 用户选填   | PS 节点的类型，详见 [训练规模](https://cloud.tencent.com/document/product/851/17319) 。              |
| WorkerCount               |`int32`       | 用户选填   | Worker/Executor 节点的数量，详见 [训练规模](https://cloud.tencent.com/document/product/851/17319)。           |
| ParameterServerCount              |`int32`       | 用户选填   | PS 节点的数量，详见 [训练规模](https://cloud.tencent.com/document/product/851/17319)。               |
| RuntimeVersion              |`string`      | 用户选填   | 训练运行环境，详见 [运行环境](https://cloud.tencent.com/document/product/851/17320) 。               |
| RuntimeConf          |`[string]`    | 用户选填   | 训练运行环境，详见 [运行环境](https://cloud.tencent.com/document/product/851/17320) 。               |
| Createtime           |`string`      | 系统添加   | 任务创建时间， RFC3339。                               |
| Starttime            |`string`      | 系统添加   | 任务开始时间， RFC3339。                               |
| Endtime              |`bool`        | 系统添加   | 任务结束时间， RFC3339。                              |
| State                |`string`      | 系统添加   | 任务状态：Created/Running/Succeeded/Failed。        |
| Message              |`string`      | 系统添加   | 任务信息，包括错误信息等。                              |
