## 1. 接口描述

本接口（ModifyHostsAttribute）用于修改CDH实例的属性，如实例名称和续费标记等。参数HostName和RenewFlag必须设置其中一个，但不能同时设置。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数和部分公共参数，完整公共参数列表见[公共请求参数](/document/api/213/15692)。

| 参数名称 | 是否必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| Action | 是 | String | 公共参数，本接口取值：ModifyHostsAttribute |
| Version | 是 | String | 公共参数，本接口取值：2017-03-12 |
| HostIds.N | 是 | Array of String | 一个或多个待操作的CDH实例ID。 |
| HostName | 否 | String | CDH实例显示名称。可任意命名，但不得超过60个字符。 |
| RenewFlag | 否 | String | 自动续费标识。取值范围：<li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费</li><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费</li><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费</li>若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。 |

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

## 示例1 修改CDH实例的属性

### 请求参数

```
https://cvm.tencentcloudapi.com/?Action=ModifyHostsAttribute
&HostIds.1=host-ey16rkyg
&HostName=web server
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
