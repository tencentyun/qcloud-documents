## 命名空间

Namespace=QCE/CEIP_SUMMARY

## 监控指标

#### Anycast 弹性公网 IP

| 指标英文名    | 指标中文名 | 指标含义                    | 单位  | 维度 |
| ------------- | ---------- | ----------------------- | ----- | ---- |
| VipInpkg      | 入包量     | Anycast 弹性公网 IP 入包量 | 个/秒 | eip  |
| VipOutpkg     | 出包量     | Anycast 弹性公网 IP 出包量 | 个/秒 | eip  |
| VipIntraffic  | 入带宽     | Anycast 弹性公网 IP 入带宽 | Mbps  | eip  |
| VipOuttraffic | 出带宽     | Anycast 弹性公网 IP 出带宽 | Mbps  | eip  |

## 各维度对应参数总览

| 参数名称                       | 维度名称 | 维度解释               | 格式                                   |
| ------------------------------ | -------- | ---------------------- | -------------------------------------- |
| Instances.N.Dimensions.0.Name  | eip      | 弹性公网 IP 的维度名称 | 输入 String 类型维度名称：eip           |
| Instances.N.Dimensions.0.Value | eip      | 弹性公网具体 IP 地址  | 输入具体 IP 地址，例如：111.111.111.11 |

## 入参说明

**查询私有网络弹性公网 IP 监控接口监控数据，入参取值如下：**
&Namespace=QCE/CEIP_SUMMARY
&Instances.N.Dimensions.0.Name=eip
&Instances.N.Dimensions.0.Value=弹性公网 IP 的唯一 ID


