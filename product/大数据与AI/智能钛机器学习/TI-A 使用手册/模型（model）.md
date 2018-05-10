Model 代表一个部署用于 serve 的模型，model 会将指定的模型部署到容器集群。Model 有如下参数：

| 名称                   | 类型       | 描述                                       |
| :------------------- | :------- | :--------------------------------------- |
| name                  | String        | Required, model name, cluster 唯一              |
| description         | String       |  Model 描述            |
| cluster               | String       |  部署的 cluster id|
| model               | String      | Model 地址, 第一版本支持 cfs，格式参考 packageDir 描述|
| runtimeVersion  | String    | 运行版本，目前|
| createTime        | String      |  创建时间|
| state                 | String      |  Model 状态，状态为如下之一：Creating，Running，Fail|
| message          | String      |  model(错误)信息|
| replicas            | Int            | 副本数量, 默认为 1|
| expose             | String    |  暴露方式:internal(内网 IP), external(外网 IP），默认 external|
