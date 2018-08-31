## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (DescribeHosts) is used to get the details of one or more CDH instances.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeHosts |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| Filters.N | No | Array of [Filter](/document/api/213/##Filter) | Filter conditions.<br/><li> zone - String - Required: No - (Filter condition) Filter by availability zone.</li><li> project-id - Integer - Required: No - (Filter condition) Filter by project ID. You can view the list of created projects by calling DescribeProject or by logging in to the console. You can also create a new project by calling AddProject.</li><li> host-id - String - Required: No - (Filter condition) Filter by CDH ID. Example of a CDH ID: host-11112222.</li><li> host-name - String - Required: No - (Filter condition) Filter by CDH instance name.</li><li> host-state - String - Required: No - (Filter condition) Filter by CDH instance status. (PENDING: Creating&#124;LAUNCH_FAILURE: Creation failed&#124;RUNNING: Running&#124;EXPIRED: Expired)</li> |
| Offset | No | Integer | Offset. Default is 0. |
| Limit | No | Integer | Number of values to be returned. Default is 20. Maximum is 100. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of CDH instances that meet the condition |
| HostSet | Array of [HostItem](/document/api/213/##HostItem) | Details of a CDH instance |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidHostId.Malformed | Invalid [CDH](https://cloud.tencent.com/document/product/416) `ID`. The specified [CDH](https://cloud.tencent.com/document/product/416) `ID` is in an incorrect format. For example, `host-1122` has an invalid `ID` length. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| InvalidZone.MismatchRegion | The specified `zone` does not exist. |

## 5. Example

### Example 1 Query the CDH instance list

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=DescribeHosts
&Filters.0.Name=zone
&Filters.0.Values.0=ap-guangzhou-2
&Offset=0
&Limit=20
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "HostSet": [
      {
        "CreatedTime": "2018-01-04T09:45:39Z",
        "ExpiredTime": "2025-05-04T09:45:42Z",
        "HostChargeType": "PREPAID",
        "HostId": "host-ey16rkyg",
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
        "Placement": {
          "ProjectId": 0,
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


