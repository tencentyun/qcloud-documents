## 命名空间


Namespace=QCE/LB

## 监控指标

| 指标英文名  | 指标中文名  | 单位  | 维度 |
| -------------- | ---------- | ----- | ---- |
| VipOuttraffic | 外网出带宽 | Mbps  | Eip  |
| VipIntraffic  | 外网入带宽 | Mbps  | Eip  |
| VipOutpkg     | 出包量     | 个/秒 | Eip  |
| VipInpkg      | 入包量     | 个/秒 | Eip  |

> ?每个指标对应的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度信息。

## 各维度对应参数总览

| 参数名称                       | 维度名称 | 维度解释              | 格式                                 |
| ------------------------------ | -------- | --------------------- | ------------------------------------ |
| Instances.N.Dimensions.0.Name  | eip      | 弹性公网 IP的维度名称 | 输入String 类型维度名称：eip         |
| Instances.N.Dimensions.0.Value | eip      | 弹性公网 具体IP 地址  | 输入具体IP地址，例如：111.111.111.11 |

## 入参说明

查询私有网络弹性公网 IP 监控接口监控数据，入参取值如下：<br>
&Namespace=QCE/LB<br>
&Instances.N.Dimensions.0.Name=eip<br>
&Instances.N.Dimensions.0.Value 为弹性公网IP的唯一 ID<br>