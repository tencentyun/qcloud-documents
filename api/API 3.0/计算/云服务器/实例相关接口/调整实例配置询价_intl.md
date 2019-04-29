## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (InquiryPriceResetInstancesType) is used to inquire the price of adjusting the model of an instance.

* Using this API for inquiring the prices of adjusted models is only supported for the instances with a [system disk type](https://cloud.tencent.com/document/api/213/9452#block_device) of `CLOUD_BASIC`, `CLOUD_PREMIUM` and `CLOUD_SSD`.
* This API cannot be used to inquire the prices of adjusting the models of [CDH](https://cloud.tencent.com/document/product/416) instances.
* Model adjustment is not supported for different models and systems, which means that the `InstanceType` specified when you use this API and the original instance model must be in the same series.
* For prepaid instances, you will be charged a fee for using this API, so make sure to keep sufficient balance in your account. You can query the account balance via API [`DescribeAccountBalance`](https://cloud.tencent.com/document/product/378/4397).

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: InquiryPriceResetInstancesType |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceIds.N | Yes |  Array of String | ID(s) of one or more instances you are working with. You can obtain the parameter value from the `InstanceId` field value in the returned result of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728). A maximum of 1 instances are allowed in a batch for each request. |
| InstanceType | Yes | String | Instance model. Different resource specifications are specified for different instance models. For specific values, please see the table of instance resource specifications. You can also obtain the latest specification list using the API for querying the list of instance resource specifications. |
| ForceStop | No | Boolean | Indicates whether to perform a forced shutdown on a running instance. It is recommended to manually shut down the running instance before resetting the user password. Supported values: <br><li>TRUE: Perform a forced shutdown<br><li>FALSE: Do not perform a forced shutdown<br><br>Default: FALSE.<br><br> Just like powering off a physical PC, a forced shutdown may cause data loss or the corruption of file system. Be sure to perform forced shutdown only when the server cannot be shut down normally. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| Price | [Price](/document/api/213/##Price) | The price of the adjusted instance model. |
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
| InvalidParameter | Invalid parameter. The parameter does not meet the requirement or is not supported. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| InvalidPermission | The operation is not supported for the account. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Inquire the price of adjusting the configuration of a prepaid instance

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=InquiryPriceResetInstancesType
&InstanceIds.0=ins-2zvpghhc
&InstanceType=S1.SMALL4
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "Price": {
      "InstancePrice": {
        "DiscountPrice": "67.33",
        "OriginalPrice": "67.33"
      }
    },
    "RequestId": "d9f36a23-7bc4-4f02-99c5-00b4a77431df"
  }
}
```


