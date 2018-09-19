## 1. 接口描述

本接口 (RenewHosts) 用于续费包年包月CDH实例。

* 只支持操作包年包月实例，否则操作会以特定[错误码](#4.-.E9.94.99.E8.AF.AF.E7.A0.81)返回。
* 续费时请确保账户余额充足。可通过[`DescribeAccountBalance`](https://cloud.tencent.com/document/product/378/4397)接口查询账户余额。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数和部分公共参数，完整公共参数列表见[公共请求参数](/document/api/213/15692)。

| 参数名称 | 是否必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| Action | 是 | String | 公共参数，本接口取值：RenewHosts |
| Version | 是 | String | 公共参数，本接口取值：2017-03-12 |
| HostIds.N | 是 | Array of String | 一个或多个待操作的CDH实例ID。 |
| HostChargePrepaid | 是 | [ChargePrepaid](/document/api/213/15753#ChargePrepaid) | 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。 |

## 3. 输出参数



| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId | String | 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。 |

## 4. 错误码



| 错误码 | 描述 |
|---------|---------|
| InvalidHost.NotSupported | 不支持该宿主机实例执行指定的操作。 |
| InvalidHostId.Malformed | 无效[CDH](https://cloud.tencent.com/document/product/416) `ID`。指定的[CDH](https://cloud.tencent.com/document/product/416) `ID`格式错误。例如`ID`长度错误`host-1122`。 |
| InvalidHostId.NotFound | 指定的HostId不存在，或不属于该请求账号所有。 |

## 5. 示例

## 示例1 续费CDH实例

### 请求参数

```
https://cvm.tencentcloudapi.com/?Action=RenewHosts
&HostChargePrepaid.Period=1
&HostChargePrepaid.RenewFlag=NOTIFY_AND_AUTO_RENEW
&HostIds.1=host-ey16rkyg
&<公共请求参数>
```
### 返回参数

```
{
  "Response": {
    "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
  }
}
```
