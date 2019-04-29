## 1. 接口描述

本接口 (DescribeHosts) 用于获取一个或多个CDH实例的详细信息。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数和部分公共参数，完整公共参数列表见[公共请求参数](/document/api/213/15692)。

| 参数名称 | 是否必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| Action | 是 | String | 公共参数，本接口取值：DescribeHosts |
| Version | 是 | String | 公共参数，本接口取值：2017-03-12 |
| Filters.N | 否 | Array of [Filter](/document/api/213/15753#Filter) | 过滤条件。<li>zone - String - 是否必填：否 - （过滤条件）按照可用区过滤。</li><li>project-id - Integer - 是否必填：否 - （过滤条件）按照项目ID过滤。可通过调用 DescribeProject 查询已创建的项目列表或登录控制台进行查看；也可以调用 AddProject 创建新的项目。</li><li>host-id - String - 是否必填：否 - （过滤条件）按照CDH ID过滤。CDH ID形如：host-11112222。</li><li>host-name - String - 是否必填：否 - （过滤条件）按照CDH实例名称过滤。</li><li>host-state - String - 是否必填：否 - （过滤条件）按照CDH实例状态进行过滤。（PENDING：创建中&#124;LAUNCH_FAILURE：创建失败&#124;RUNNING：运行中&#124;EXPIRED：已过期）|</li>
| Offset | 否 | Integer | 偏移量，默认为0。 |
| Limit | 否 | Integer | 返回数量，默认为20，最大值为100。 |

## 3. 输出参数



| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| TotalCount | Integer | 符合查询条件的cdh实例总数 |
| HostSet | Array of [HostItem](/document/api/213/15753#HostItem) | cdh实例详细信息列表 |
| RequestId | String | 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。 |

## 4. 错误码



| 错误码 | 描述 |
|---------|---------|
| InvalidHostId.Malformed | 无效[CDH](https://cloud.tencent.com/document/product/416) `ID`。指定的[CDH](https://cloud.tencent.com/document/product/416) `ID`格式错误。例如`ID`长度错误`host-1122`。 |
| InvalidParameterValue | 无效参数值。参数值格式错误或者参数值不被支持等。 |
| InvalidZone.MismatchRegion | 指定的`zone`不存在。 |

## 5. 示例

## 示例1 查询CDH实例列表

### 场景描述

查询一个或多个CDH实例的详细信息


### 请求参数

```
https://cvm.tencentcloudapi.com/?Action=DescribeHosts
&Filters.1.Name=zone
&Filters.1.Values.1=ap-guangzhou-2
&Offset=0
&Limit=20
&<公共请求参数>
```
### 返回参数

```
{
  "Response": {
    "HostSet": [
      {
        "CreatedTime": "2018-01-04T09:45:39Z",
        "ExpiredTime": "2025-05-04T09:45:42Z",
        "HostChargeType": "PREPAID",
        "HostId": "host-ey16rkyg",
        "HostIp": "10.249.99.139",
        "HostName": "bibibibib-111",
        "HostResource": {
          "CpuAvailable": 24,
          "CpuTotal": 24,
          "DiskAvailable": 1200,
          "DiskTotal": 1200,
          "MemAvailable": 56.0,
          "MemTotal": 56.0
        },
        "HostState": "RUNNING",
        "HostType": "HS1",
        "InstanceIds": [],
        "OperationMask": 62,
        "Placement": {
          "ProjectId": 0,
          "ProjectName": "默认项目",
          "Zone": "ap-guangzhou-2"
        },
        "RenewFlag": "NOTIFY_AND_AUTO_RENEW"
      }
    ],
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
    "TotalCount": 1
  }
}
```