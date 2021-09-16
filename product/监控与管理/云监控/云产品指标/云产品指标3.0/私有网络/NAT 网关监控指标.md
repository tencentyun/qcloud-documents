## 命名空间

Namespace=QCE/NAT_GATEWAY

## 监控指标

| 指标英文名   | 指标中文名   | 指标含义                  | 单位  | 维度  |
| ------------ | ------------ | --------------------- | ----- | ----- |
| OutBandwidth | 外网出带宽   | NAT 网关平均每秒出流量 | Mbps  | natId |
| InBandwidth  | 外网入带宽   | NAT 网关平均每秒入流量 | Mbps  | natId |
| InPkg        | 外网入包量   | NAT 网关平均每秒入包量 | 个/秒 | natId |
| OutPkg       | 外网出包量   | NAT 网关平均每秒出包量 | 个/秒 | natId |
| Conns        | 外网络连接数 | NAT 网关的实时并发数   | 个/秒 | natId |

> ?每个指标对应的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度信息。

## 各维度对应参数总览

| 参数名称               | 维度名称             | 维度解释          | 格式                            |
| ------------------ | ---------------- | ------------- | ----------------------------- |
| Instances.N.Dimensions.0.Name  | natId                     | NAT 网关 ID 的维度名称 | 输入String 类型维度名称：natId       |
| Instances.N.Dimensions.0.Value | natId                     | NAT 网关具体 ID       | 输入具体 natId，例如：nat-4d545d  |

## 入参说明

查询私有网络 NAT 网关监控数据，入参取值如下：
&Namespace=QCE/NAT_GATEWAY
&Instances.N.Dimensions.0.Name=natId
&Instances.N.Dimensions.0.Value 为 NAT 网关 ID


