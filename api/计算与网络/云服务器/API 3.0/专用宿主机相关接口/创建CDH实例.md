## 1. 接口描述

本接口 (AllocateHosts) 用于创建一个或多个指定配置的CDH实例。
* 当HostChargeType为PREPAID时，必须指定HostChargePrepaid参数。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数和部分公共参数，完整公共参数列表见[公共请求参数](/document/api/213/15692)。

| 参数名称          | 是否必选 | 类型                                                   | 描述                                                         |
| ----------------- | -------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| Action            | 是       | String                                                 | 公共参数，本接口取值：AllocateHosts                          |
| Version           | 是       | String                                                 | 公共参数，本接口取值：2017-03-12                             |
| ClientToken       | 否       | String                                                 | 用于保证请求幂等性的字符串。                                 |
| Placement         | 是       | [Placement](/document/api/213/15753#Placement)         | 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。 |
| HostChargePrepaid | 否       | [ChargePrepaid](/document/api/213/15753#ChargePrepaid) | 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。 |
| HostChargeType    | 否       | String                                                 | 实例计费类型。目前仅支持：PREPAID（预付费，即包年包月模式）。 |
| HostType          | 否       | String                                                 | CDH实例机型，默认为：'HS1'。                                 |
| HostCount         | 否       | Integer                                                | 购买CDH实例数量。                                            |

## 3. 输出参数



| 参数名称  | 类型            | 描述                                                         |
| --------- | --------------- | ------------------------------------------------------------ |
| HostIdSet | Array of String | 新创建云子机的实例id列表。                                   |
| RequestId | String          | 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。 |

## 4. 错误码



| 错误码                     | 描述                                                         |
| -------------------------- | ------------------------------------------------------------ |
| InvalidPeriod              | 无效时长。目前只支持时长：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36]，单位：月。 |
| InvalidProjectId.NotFound  | 无效的项目ID，指定的项目ID不存在。                           |
| InvalidRegion.NotFound     | 未找到该区域。                                               |
| InvalidZone.MismatchRegion | 指定的`zone`不存在。                                         |

## 5. 示例

## 示例1 包年包月CDH实例购买

### 场景描述

购买付费模式为包年包月的CDH实例


### 请求参数

```
https://cvm.tencentcloudapi.com/?Action=AllocateHosts
&Placement.Zone=ap-guangzhou-2
&HostChargeType=PREPAID
&HostChargePrepaid.Period=1
&HostChargePrepaid.RenewFlag=NOTIFY_AND_AUTO_RENEW
&HostType=HS1
&HostCount=1
&<公共请求参数>
```
### 返回参数

```
{
  "Response": {
    "HostIdSet": [
      "host-lan4lb2k"
    ],
    "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
  }
}
```