Model 代表一个部署用于 serve 的模型，model 会将指定的模型部署到容器集群。Model 有如下参数：

| 名称                   | 类型       | 描述                                       |
| :------------------- | :------- | :--------------------------------------- |
| name                  |`string`        | Required, model name, cluster唯一              |
| description         |`string`        |  model描述            |
| cluster               |`string`        |  部署的cluster id|
| model               |`string`        | model地址, 第一版本支持cfs，格式参考上面的packageDir描述|
| runtimeVersion  |`string`       | 运行版本，目前|
| createTime        |`string`       |  创建时间|
| state                 |`string`        |  model状态，状态为如下之一：Creating，Running，Fail|
| message          |`string`        |  model(错误)信息|
| replicas            | `int`            | 副本数量, 默认为1|
| expose             |`string`       |  暴露方式:internal(内网ip), external(外网ip），默认external|