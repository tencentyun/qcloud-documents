Job 代表一个训练任务，他定义了训练该如何在腾讯云上执行。每一个 job 对应以下字段：

| 参数名称              | 类型         | 添加者     | 描述                                                |
| :------------------- | :----------- | :-------- | --------------------------------------------------- |
| name                 |`string`      | 用户必填   | 任务的名称，每个集群中该名称必须唯一                   |
| packagedir           |`[string]`    | 用户必填   | 训练代码/数据或输出路径, 详见[文件路径](#文件路径)     |
| command              |`[string]`    | 用户必填   | 任务启动命令                                         |
| args                 |`[string]`    | 用户必填   | 任务启动参数                                         |
| cluster              |`string`      | 用户设置   | 运行集群, 详见[使用集群](#使用集群)                   |
| scaletier            |`string`      | 用户选填   | 用以规定运行训练的方式和规模，详见[训练规模](#训练规模) |
| mastertype           |`string`      | 用户选填   | Master 节点的类型，详见[训练规模](#训练规模)           |
| workertype           |`string`      | 用户选填   | Worker 节点的类型，详见[训练规模](#训练规模)           |
| pstype               |`string`      | 用户选填   | PS 节点的类型，详见[训练规模](#训练规模)               |
| wcount               |`int32`       | 用户选填   | Worker 节点的数量，详见[训练规模](#训练规模)           |
| pscount              |`int32`       | 用户选填   | PS 节点的数量，详见[训练规模](#训练规模)               |
| runtime              |`string`      | 用户选填   | 训练运行环境, 详见[运行环境](#运行环境)                |
| createtime           |`string`      | 系统添加   | 任务创建时间, RFC3339                                |
| starttime            |`string`      | 系统添加   | 任务开始时间, RFC3339                                |
| endtime              |`bool`        | 系统添加   | 任务结束时间, RFC3339                                |
| state                |`string`      | 系统添加   | 任务状态：Created/Running/Succeeded/Failed          |
| message              |`string`      | 系统添加   | 任务信息，包括错误信息等                              |