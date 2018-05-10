Model 代表一个部署用于 serve 的模型，model 会将指定的模型部署到容器集群。Model 有如下参数：

| 名称                   | 类型       | 描述                                       |
| :------------------- | :------- | :--------------------------------------- |
| name                  | String        | Required, model name, cluster唯一              |
| description         | String       |  model描述            |
| cluster               | String       |  部署的cluster id|
| model               | String      | model地址, 第一版本支持cfs，格式参考上面的packageDir描述|
| runtimeVersion  | String    | 运行版本，目前|
| createTime        | String      |  创建时间|
| state                 | String      |  model状态，状态为如下之一：Creating，Running，Fail|
| message          | String      |  model(错误)信息|
| replicas            | Int            | 副本数量, 默认为1|
| expose             | String    |  暴露方式:internal(内网ip), external(外网ip），默认external|
