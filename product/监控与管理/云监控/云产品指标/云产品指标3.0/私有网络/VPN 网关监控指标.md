## 命名空间

Namespace=QCE/VPNGW


## 监控指标

| 指标英文名 | 指标中文名 | 指标含义                  | 单位  | 维度    |
| ---------- | ---------- | --------------------- | ----- | ------- |
| InBandwidth  | 外网入带宽 | VPN 网关平均每秒入流量 | Mbps  | vpnGwId |
| OutBandwidth | 外网出带宽 | VPN 网关平均每秒出流量 | Mbps  | vpnGwId |
| Inpkg      | 入包量     | VPN 网关平均每秒入包量 | 个/秒 | vpnGwId |
| Outpkg     | 出包量     | VPN 网关平均每秒出包量 | 个/秒 | vpnGwId |


> ?每个指标对应的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度。

## 各维度对应参数总览

| 参数名称                       | 维度名称 | 维度解释              | 格式                                     |
| ------------------------------ | -------- | --------------------- | ---------------------------------------- |
| Instances.N.Dimensions.0.Name  | vpnGwId  | VPN 网关 ID 的维度名称 | 输入 String 类型维度名称：vpnGwId         |
| Instances.N.Dimensions.0.Value | vpnGwId  | VPN 网关具体 ID       | 输入 VPN 网关具体 ID，例如：vpngw-q7v069tf |

## 入参说明

查询私有网络 VPN 网关监控数据，入参取值如下：
&Namespace=QCE/VPNGW
&Instances.N.Dimensions.0.Name=vpnGwId
&Instances.N.Dimensions.0.Value为 VPN 网关 ID


