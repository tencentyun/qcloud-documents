Model 代表一个可用于部署服务的模型，可以部署到集群中暴露外网提供服务。每一个 Model 对应以下字段：

| 参数名称              | 类型      | 添加者    | 描述                                                     |
| :--------------------| :-------- | :------- | :----------------                                        |
| name                 |String   | 用户必填  | 模型服务的名称，每个集群中该名称必须唯一 。                   |
| model                |String   | 用户必填  | 模型地址， 第一版本支持 CFS，详见 [文件路径](https://cloud.tencent.com/document/product/851/17318)。       |
| description          |String   | 用户选填  | 模型服务的描述。                                            |
| cluster              |String   | 用户选填  | 运行集群，详见 [使用集群](https://cloud.tencent.com/document/product/851/17317)。                        |
| runtime              |String  | 用户选填  | 模型服务运行环境, 详见 [运行环境](https://cloud.tencent.com/document/product/851/17320)。                 |
| replicas             |Int      | 用户选填  | 副本数量，默认为 1                                        |
| expose               |String   | 用户选填  | 暴露方式：internal（内网 IP）/external（外网 IP），默认 external。|
| createTime           |String  | 系统添加  | 创建时间。                                                 |
| state                |String   | 系统添加  | 服务状态：Creating/Running/Fail。                          |
| message              |String   | 系统添加  | 服务(错误)信息。                                            |
