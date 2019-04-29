## 1. API Description

This API (InquiryPriceResizeInstanceDisks) is used to inquire the price of data disk capacity expansion of the instance.

* Now, only the price inquiry of the data disk purchased with the instance is supported, and the [data disk type](/document/api/213/9452#block_device) is: `CLOUD_BASIC`, `CLOUD_PREMIUM`, `CLOUD_SSD`.
* The [CDH](https://cloud.tencent.com/document/product/416) instance is not supported to use this API to inquire the price of data disk capacity expansion. * Only the data disks purchased with the prepaid instances are supported. * Now, only the price inquiry of capacity expansion for one data disk is supported.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value​used in this API: InquiryPriceResizeInstanceDisks |
| Version | Yes | String | Common parameter. Value​used in this API: 2017-03-12 |
| InstanceId | Yes | String | ID of instance to work with. This can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728). |
| DataDisks.N | Yes | Array of [DataDisk](/document/api/213/15753#DataDisk) | Configuration information of the data disk to be expanded. Only the data disk purchased with the instance is supported, and the [data disk type](/document/api/213/9452#block_device) is: `CLOUD_BASIC`, `CLOUD_PREMIUM`, `CLOUD_SSD`. Data disk capacity unit: GB. Minimum capacity expansion increment: 10G. For the selection of the data disk type, please see Overview of Hard Disk Products. The available data disk types are limited by the instance type `InstanceType`. In addition, the maximum capacity allowed for expansion varies depending on the type of data disk. |
| ForceStop | No | Boolean | Indicate whether a forced shutdown is performed to running instances. It is recommended that you manually shut down the running instance before resetting the user password. Value range: <li>TRUE: indicates the forced shutdown will be performed after a normal shutdown failure. </li><li>FALSE: indicates that the forced shutdown is not performed after a normal shutdown failure. </li>Default value: FALSE.<br><br> The result of forced shutdown is the same as turning off the power switch of the physical computer. Forced shutdown may lead to data loss or damage to file system, so use it only when the server cannot be shut down properly. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| Price | [Price](/document/api/213/15753#Price) | This parameter indicates the price of disk capacity expansion to the corresponding configuration. |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InternalServerError | Internal operation error. |
| InvalidAccount.InsufficientBalance | Insufficient balance. |
| InvalidAccount.UnpaidOrder | There is an unpaid order in the account. |
| InvalidInstance.NotSupported | The instance is not supported. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. The specified instance `ID` format is incorrect. For example, `ins-1122` indicates an ID length error. |
| InvalidInstanceId.NotFound | The corresponding instance cannot be found. |
| InvalidParameterValue | Invalid parameter value. The format of the parameter value is incorrect or the parameter value is not supported. |
| MissingParameter | Missing parameters. The request does not have the required parameters. |

## 5. Example

## Example 1 Inquire the Price of Disk Capacity Expansion of Postpaid Instance

### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=InquiryPriceResizeInstanceDisks
&InstanceId=ins-fd8spnmq
&DataDisks.0.DiskSize=100
&<Common request parameters>
```
### Response parameters

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

