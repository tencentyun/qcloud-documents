

## 命名空间

Namespace=QCE/CLS

## 监控指标

| 指标英文名          | 指标中文名 | 单位 | 维度         | 统计周期                 |
| ------------------- | ---------- | ---- | ------------ | ------------------------ |
| TrafficWrite        | 写流量     | MB   | uin、TopicId | 60s、30s、3600s、 86400s |
| TrafficIndex        | 索引流量   | MB   | uin、TopicId | 60s、30s、3600s、 86400s |
| TrafficIntranetRead | 内网读流量 | MB   | uin、TopicId | 60s、30s、3600s、 86400s |
| TrafficInternetRead | 外网读流量 | MB   | uin、TopicId | 60s、30s、3600s、 86400s |
| TotalTrafficRead    | 读流量总量 | MB   | uin、TopicId | 60s、30s、3600s、 86400s |
| StorageLog          | 日志存储量 | MB   | uin、TopicId | 60s、30s、3600s、 86400s |
| StorageIndex        | 索引存储量 | MB   | uin、TopicId | 60s、30s、3600s、 86400s |
| TotalStorage        | 存储总量   | MB   | uin、TopicId | 60s、30s、3600s、 86400s |
| Request             | 服务请求数 | 个   | uin、TopicId | 60s、30s、3600s、 86400s |



## 各维度对应参数总览

| 参数名称                       | 维度名称 | 维度解释             | 格式                                                         |
| ------------------------------ | -------- | -------------------- | ------------------------------------------------------------ |
| Instances.N.Dimensions.0.Name  | uin      | 账号 ID 的维度名称   | 输入 String 类型维度名称：uin                                |
| Instances.N.Dimensions.0.Value | uin      | 具体的账号 ID        | 输入具体账号 ID，例如：10000xxx0827                           |
| Instances.N.Dimensions.1.Name  | TopicId  | 日志主题ID的维度名称 | 输入 String 类型维度名称：TopicId                            |
| Instances.N.Dimensions.1.Value | TopicId  | 具体的日志主题ID     | 输入具体日志主题ID，例如：4d1a2931-0038-4fb6-xxxx-bf29449e255a |

## 入参说明

**查询日志主题指标监控数据，取值如下：**

&Namespace=QCE/CLS	
&Instances.N.Dimensions.0.Name=uin	
&Instances.N.Dimensions.0.Value=具体的账号 ID 
&Instances.N.Dimensions.1.Name=TopicId	
&Instances.N.Dimensions.1.Value=用户具体的日志主题 ID	 

