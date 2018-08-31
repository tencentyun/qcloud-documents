## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (InquiryPriceResizeInstanceDisks) is used to inquiry the price of data disk capacity expansion of the instance.

* Only the data disk purchased with the instance is supported for the price inquiry of capacity expansion, and the [data disk type](/document/api/213/9452#block_device) can be `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`.
* This API cannot be used to inquiry the price of expanding the capacity of data disks for [CDH](https://cloud.tencent.com/document/product/416) instances.* Only data disks purchased along with prepaid instances are supported.* Inquiring the price of expanding the capacity of only one data disk is supported.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: InquiryPriceResizeInstanceDisks |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceId | Yes | String | IDs of instances you are working with. You can obtain the parameter value from the `InstanceId` field value in the returned result of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728). |
| DataDisks.N | Yes | Array of [DataDisk](/document/api/213/##DataDisk) | Configuration information of the data disk whose capacity is to be expanded. Capacity expansion is only available to the data disk purchased with the instance, and the [data disk type](/document/api/213/9452#block_device) can be `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`. Data disk capacity is calculated in GB. Minimum increment of capacity expansion is 10 GB. For information on how to choose a data disk type, please see Disk Product Overview. The available types of data disks are subject to the instance type (`InstanceType`). In addition, the maximum capacity allowed for expansion varies with different types of data disks. |
| ForceStop | No | Boolean | Indicates whether to perform a forced shutdown on a running instance. It is recommended to manually shut down the running instance before resetting the user password. Supported values: <br><li>TRUE: Perform a forced shutdown<br><li>FALSE: Do not perform a forced shutdown<br><br>Default: FALSE.<br><br> Just like powering off a physical PC, a forced shutdown may cause data loss or the corruption of file system. Be sure to perform forced shutdown only when the server cannot be shut down normally. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| Price | [Price](/document/api/213/##Price) | The price of expanding the capacity of the disk to a proper configuration. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalServerError | Internal error. |
| InvalidAccount.InsufficientBalance | Insufficient account balance. |
| InvalidAccount.UnpaidOrder | There is an order to be paid in the account. |
| InvalidInstance.NotSupported | Unsupported instance. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. Specified instance `ID` is not in a correct format. For example, `ins-1122` has an invalid instance `ID` length. |
| InvalidInstanceId.NotFound | No instance found. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Inquire the price of disk capacity expansion for a postpaid instance

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=InquiryPriceResizeInstanceDisks
&InstanceId=ins-fd8spnmq
&DataDisks.0.DiskSize=100
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "Price": {
      "InstancePrice": {
        "ChargeUnit": "HOUR",
        "UnitPrice": 0.46
      }
    },
    "RequestId": "d63b4f53-335b-49fb-9aa1-1716bb9276f6"
  }
}
```


