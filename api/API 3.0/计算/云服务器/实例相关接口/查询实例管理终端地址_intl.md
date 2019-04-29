## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (DescribeInstanceVncUrl) is used to query the URL to the instance management client.

* This feature is unavailable to the instances with a status of `STOPPED`.
* The validity period of the management client URL is 15 sec. If the URL is not accessed within 15 sec after the API is called, it will become invalid automatically. You have to query a URL again.
* Once the client URL is accessed, it will become invalid automatically. You have to query a URL again.
* If the access is disconnected, reconnect attempts within one minute cannot exceed 30 times.
* Add the parameter `InstanceVncUrl=xxxx` at the end of the URL <https://img.qcloud.com/qcloud/app/active_vnc/index.html?> after obtaining `InstanceVncUrl`.
  - Parameter `InstanceVncUrl`: Returned value of `InstanceVncUrl` after a successful call of the API.

    The final URLs are in the following format:

```
https://img.qcloud.com/qcloud/app/active_vnc/index.html?InstanceVncUrl=wss%3A%2F%2Fbjvnc.qcloud.com%3A26789%2Fvnc%3Fs%3DaHpjWnRVMFNhYmxKdDM5MjRHNlVTSVQwajNUSW0wb2tBbmFtREFCTmFrcy8vUUNPMG0wSHZNOUUxRm5PMmUzWmFDcWlOdDJIbUJxSTZDL0RXcHZxYnZZMmRkWWZWcEZia2lyb09XMzdKNmM9
```


A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeInstanceVncUrl |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceId | Yes |  String | ID of an instance you are working with. You can obtain the parameter value from the `InstanceId` field value in the returned result of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728). |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| InstanceVncUrl | String | URL to the instance management client. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidInstanceId.Malformed | Invalid instance `ID`. Specified instance `ID` is not in a correct format. For example, `ins-1122` has an invalid instance `ID` length. |
| InvalidInstanceId.NotFound | No instance found. |
| InvalidInstanceState | The operation cannot be performed to the instance with the current status. |

## 5. Example

### Example 1 Query the URL to the instance management client

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=DescribeInstanceVncUrl
&Region=ap-beijing
&InstanceId=ins-r9hr2upy
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "InstanceVncUrl": "wss%3A%2F%2Fbjvnc.qcloud.com%3A26789%2Fvnc%3Fs%3DaHpjWnRVMFNhYmxKdDM5MjRHNlVTSVQwajNUSW0wb2tBbmFtREFCTmFrcy8vUUNPMG0wSHZNOUUxRm5PMmUzWmFDcWlOdDJIbUJxSTZDL0RXcHZxYnZZMmRkWWZWcEZia2lyb09XMzdKNmM9",
    "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
  }
}
```


