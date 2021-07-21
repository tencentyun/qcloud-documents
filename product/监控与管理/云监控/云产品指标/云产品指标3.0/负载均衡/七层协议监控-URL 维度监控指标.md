## 命名空间

Namespace=QCE/LOADBALANCE



## 监控指标

| 指标英文名          | 指标中文名   | 指标含义     | 单位  | 维度                                     | 统计粒度 |
| ------------------- | ------------ | ------------ | ----- | ---------------------------------------- | -------- |
| QPS                 | 每秒请求数   | 每秒请求数   | 个    | domain、loadBalancerPort、protocol、url、vip | 60s、300s |
| ResponseTimeoutNum  | 响应超时个数 | 响应超时个数 | 个    | domain、loadBalancerPort、protocol、url、vip | 60s、300s |
| ResponseTimeAverage | 平均响应时间 | 平均响应时间 | ms    | domain、loadBalancerPort、protocol、url、vip | 60s、300s |
| ResponseTimeMax     | 最大响应时间 | 最大响应时间 | ms    | domain、loadBalancerPort、protocol、url、vip | 60s、300s |
| ConNum              | 活跃连接数   | 活跃连接数   | 个    | domain、loadBalancerPort、protocol、url、vip | 60s、300s |
| NewConn             | 新建连接数   | 新建连接数   | 个    | domain、loadBalancerPort、protocol、url、vip | 60s、300s |
| InPkg               | 入包量       | 入包量       | 个/秒 | domain、loadBalancerPort、protocol、url、vip | 60s、300s |
| OutPkg              | 出包量       | 出包量       | 个/秒 | domain、loadBalancerPort、protocol、url、vip | 60s、300s |
| InTraffic           | 入带宽       | 入带宽       | Mbps  | domain、loadBalancerPort、protocol、url、vip | 60s、300s |
| OutTraffic          | 出带宽       | 出带宽       | Mbps  | domain、loadBalancerPort、protocol、url、vip | 60s、300s |
| HttpCode2XX         | 2xx 状态码   | 2xx 状态码   | 个    | domain、loadBalancerPort、protocol、url、vip | 60s、300s |
| HttpCode3XX         | 3xx 状态码   | 3xx 状态码   | 个    | domain、loadBalancerPort、protocol、url、vip | 60s、300s |
| HttpCode4XX         | 4xx 状态码    | 4xx 状态码    | 个    | domain、loadBalancerPort、protocol、url、vip | 60s、300s |
| HttpCode5XX         | 5xx 状态码    | 5xx 状态码    | 个    | domain、loadBalancerPort、protocol、url、vip | 60s、300s |
| HttpCode404         | 404 状态码    | 404 状态码    | 个    | domain、loadBalancerPort、protocol、url、vip | 60s、300s |
| HttpCode502         | 502 状态码    | 502 状态码    | 个    | domain、loadBalancerPort、protocol、url、vip | 60s、300s |
| RequestTimeAverage  | 平均请求时间 | 平均请求时间 | ms    | domain、loadBalancerPort、protocol、url、vip | 60s、300s |
| RequestTimeMax      | 最大请求时间 | 最大请求时间 | ms    | domain、loadBalancerPort、protocol、url、vip | 60s、300s|

## 各维度对应参数总览

| 参数名称  | 维度名称     | 维度解释      | 格式                                |
| ------------------------------ | -------- | ---------------------------- | ------------------------------------------------------------ |
| Instances.N.Dimensions.0.value | vip      | 负载均衡具体 VIP             | 输入具体 IP 地址，例如：111.111.111.11                       |
| Instances.N.Dimensions.1.name  | port     | 负载均衡端口的维度名称       | 输入 String 类型维度名称：port                               |
| Instances.N.Dimensions.1.value | port     | 负载均衡具体端口             | 输入具体端口号，例如：80                                     |
| Instances.N.Dimensions.2.name  | protocol | 协议的维度名称               | 输入 String 类型维度名称：protocol                           |
| Instances.N.Dimensions.2.value | protocol | 具体协议名称                 | 输入协议值具体名称，例如：http                               |
| Instances.N.Dimensions.3.name  | vpcId    | 私有网络 ID 的维度名称       | 输入 String 类型维度名称：vpcId                              |
| Instances.N.Dimensions.3.value | vpcId    | 负载均衡所在私有网络的具体 D | 输入私有网络具体 ID，例如：1111。需输入数值型 vpcId ，可参考 根据 [证书 ID 查询负载均衡文档](https://cloud.tencent.com/document/product/214/40953) 获取 NumericalvpcId |
| Instances.N.Dimensions.4.name  | domain   | 域名的维度名称               | 输入 String 类型维度名称：domain                             |
| Instances.N.Dimensions.4.value | domain   | 具体域名                     | 输入具体域名，例如：`www.cloud.tencent.com`               |
| Instances.N.Dimensions.5.name  | url      | url 的维度名称               | 输入 String 类型维度名称：url                                |
| Instances.N.Dimensions.5.value | url      | 具体 url                     | 输入具体 url，例如：/aaa                                     |

## 入参说明

**负载均衡七层协议监控 URL维度入参取值如下：**

&Namespace=QCE/LB_PRIVATE
&Instances.N.Dimensions.0.Name=vip
&Instances.N.Dimensions.0.Value=IP 地址
&Instances.N.Dimensions.1.Name=port
&Instances.N.Dimensions.1.Value=负载均衡具体端口
&Instances.N.Dimensions.2.Name=protocol
&Instances.N.Dimensions.2.Value=具体协议名称
&Instances.N.Dimensions.3.Name=vpcId
&Instances.N.Dimensions.3.Value=负载均衡所在私有网络的 ID
&Instances.N.Dimensions.4.Name=domain
&Instances.N.Dimensions.4.Value=具体域名
&Instances.N.Dimensions.5.Name=url
&Instances.N.Dimensions.5.Value=具体 url
