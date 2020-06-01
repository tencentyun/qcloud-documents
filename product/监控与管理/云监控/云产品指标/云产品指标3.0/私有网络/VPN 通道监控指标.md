## 命名空间

Namespace=QCE/VPNX

## 监控指标

| 指标英文名   | 指标中文名 | 单位   | 维度      |
| ------------ | ---------- | ------ | --------- |
| Outbandwidth | 外网出带宽 | Mbps   | vpnConnId |
| Inbandwidth  | 外网入带宽 | Mbps   | vpnConnId |
| Outpkg       | 出包量     | 个/秒  | vpnConnId |
| Inpkg        | 入包量     | 个/秒  | vpnConnId |
| Pkgdrop      | 丢包率     | 百分比 | vpnConnId |
| Delay        | 时延       | 秒     | vpnConnId |

> ?每个指标对应的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度。


## 各维度对应参数总览

| 参数名称                       | 维度名称  | 维度解释             | 格式                                     |
| ------------------------------ | --------- | -------------------- | ---------------------------------------- |
| Instances.N.Dimensions.0.Name  | vpnConnId | VPN 通道ID的维度名称 | 输入String 类型维度名称：vpnConnId       |
| Instances.N.Dimensions.0.Value | vpnConnId | VPN 通道具体ID       | 输入VPN 通道具体ID，例如 ：vpnx-12345678 |

## 入参说明

查询私有网络VPN通道监控数据，入参取值如下：<br>
&Namespace=QCE/VPNX<br>
&Instances.N.Dimensions.0.Name=vpnConnId<br>
&Instances.N.Dimensions.0.Value 为 VPN 通道 ID<br>