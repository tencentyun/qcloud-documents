## 命名空间

Namespace=QCE/BM_LB

## 监控指标

| 指标英文名    | 指标中文名 | 单位  | 维度 |
| ------------- | ---------- | ----- | ---- |
| EipOuttraffic | 外网出带宽 | Mbps  | vip  |
| EipIntraffic  | 外网入带宽 | Mbps  | vip  |
| EipOutpkg     | 外网出包量 | 个/秒 | vip  |
| EipInpkg      | 外网入包量 | 个/秒 | vip  |

> ?每个指标的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度。

## 各维度对应参数总览

| 参数名称                       | 维度名称 | 维度解释                   | 格式                                                         |
| ------------------------------ | -------- | -------------------------- | ------------------------------------------------------------ |
| Instances.N.Dimensions.0.Name  | vip      | 弹性公网 IP 地址的维度名称 | 输入 String 类型维度名称：vip                                 |
| Instances.N.Dimensions.0.Value | vip      | 弹性公网具体IP 地址       | 输入具体 EIP 地址，例如：115.115.115.115，可以通过查询接口 [DescribeEipBm](https://cloud.tencent.com/document/api/1028/32853) 查看自己账户已申请的 EIP 列表 |

## 入参说明

查询黑石弹性公网 IP（EIP）监控数据，入参取值如下：

&Namespace=QCE/BM_LB
&Instances.N.Dimensions.0.Name=vip
&Instances.N.Dimensions.0.Value=要查询的 EIP 的地址信息

