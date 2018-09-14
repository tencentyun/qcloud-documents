## 1. API Description

This API (DescribeHosts) is used to get the details of one or more CDH instances.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value​used in this API: DescribeHosts |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| Filters.N | No | Array of [Filter](/document/api/213/15753#Filter) | Filter criteria. <li>zone - String - Required: No - (Filter criteria) Filter by availability zone. </li><li>project-id - Integer - Required: No - (Filter criteria) Filter by project ID. You can view the list of created projects by calling DescribeProject or log in to the console; you can also call AddProject to create a project. </li><li>host-id - String - Required: No - (Filter criteria) Filter by CDH ID. The form of CDH ID is like: host-11112222. </li><li>host-name - String - Required: No - (Filter criteria) Filter by CDH instance name. </li><li>host-state - String - Required: No - (Filter criteria) Filter by CDH instance status. (PENDING: Creating&#124; LAUNCH_FAILURE: Failed to create&#124; RUNNING: Running&#124; EXPIRED: Expired) |</li>
| Offset | No | Integer | Offset; default is 0 |
| Limit | No | Integer | Number of results to be returned. Default is 20. Maximum is 100. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of cdh instances that meet the condition |
| HostSet | Array of [HostItem](/document/api/213/15753#HostItem) | cdh instance details list |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InvalidHostId.Malformed | Invalid [CDH](https://cloud.tencent.com/document/product/416) `ID`. The specified [CDH](https://cloud.tencent.com/document/product/416) `ID`format is incorrect. For example, `ID` length error `host-1122`. |
| InvalidParameterValue | Invalid parameter value. The format of the parameter value is incorrect or the parameter value is not supported. |
| InvalidZone.MismatchRegion | The specified `zone` does not exist. |

## 5. Example

## Example 1 Query CDH Instance List

### Scenario description

Query the details of one or more CDH instances.


### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=DescribeHosts
&Filters.1.Name=zone
&Filters.1.Values.1=ap-guangzhou-2
&Offset=0
&Limit=20
&<Common request parameters>
```
### Response parameters

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
          "ProjectName": "Default project",
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
