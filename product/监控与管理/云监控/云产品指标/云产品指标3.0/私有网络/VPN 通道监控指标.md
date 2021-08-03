
## 命名空间

Namespace=QCE/VPNX

## 监控指标

| 指标英文名   | 指标中文名    | 指标含义                    | 单位  | 维度      |
| ------------ | ------------- | ----------------------- | ----- | --------- |
| OutBandwidth | VPN 通道出带宽 | VPN 通道平均每秒出流量   | Mbps  | vpnConnId |
| InBandwidth  | VPN 通道入带宽 | VPN 通道平均每秒入流量   | Mbps  | vpnConnId |
| InPkg        | VPN 通道入包量 | VPN 通道平均每秒入包量   | 个/秒 | vpnConnId |
| OutPkg       | VPN 通道出包量 | VPN 通道平均每秒出包量   | 个/秒 | vpnConnId |
| PkgDrop      | VPN 通道丢包率 | VPN 探测一分钟的丢包比例 | %     | vpnConnId |
| Delay        | VPN 通道时延   | VPN 探测一分钟的平均时延 | ms    | vpnConnId |
| Disconnected | VPN 通道不通   | VPN 通道的通断状态       | ms    | vpnConnId |

>?每个指标对应的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度。


## 各维度对应参数总览

| 参数名称                       | 维度名称  | 维度解释             | 格式                                     |
| ------------------------------ | --------- | -------------------- | ---------------------------------------- |
| Instances.N.Dimensions.0.Name  | vpnConnId | VPN 通道 ID 的维度名称 | 输入 String 类型维度名称：vpnConnId       |
| Instances.N.Dimensions.0.Value | vpnConnId | VPN 通道具体 ID       | 输入 VPN 通道具体 ID，例如：vpnx-12345678 |

## 入参说明

**查询私有网络 VPN 通道监控数据，入参取值如下：**
&Namespace=QCE/VPNX
&Instances.N.Dimensions.0.Name=vpnConnId
&Instances.N.Dimensions.0.Value=VPN 通道 ID

