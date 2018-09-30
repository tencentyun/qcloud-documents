## 1. API Description

Domain name for API request: cbs.tencentcloudapi.com

This API (RenewDisk) is used to renew cloud disks.

* Only prepaid cloud disks can be renewed. Cloud disk type can be queried in DiskChargeType field in the output parameters returned by the API [DescribeDisks](/document/product/362/16315).
* The mounted cloud disk can be renewed together with the instance. The CurInstanceDeadline in the [DiskChargePrepaid](/document/product/362/15669#DiskChargePrepaid) parameter must be specified. In such case, you can renew the cloud disk to the expiration time of the server.
* Make sure your account balance is sufficient for renewals. You can query account balance via API [DescribeAccountBalance](/document/product/378/4397).

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cbs.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: RenewDisk |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/362/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| DiskChargePrepaid | Yes | [DiskChargePrepaid](/document/api/362/##DiskChargePrepaid) | Prepaid mode, which is the relevant parameter setting for prepaid mode. This parameter can specify the renewal usage period of a prepaid instance.<br> If the mounted cloud disk is renewed together with the instance, specify the parameter CurInstanceDeadline. In such case, you can renew the cloud disk to the expiration time of the instance. |
| DiskId | Yes | String | Cloud disk ID, which can be queried via the API [DescribeDisks](/document/product/362/16315). |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/362/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidDisk.Busy | The cloud disk is busy. Try again later. |
| InvalidDisk.NotPortable | Non-elastic cloud disk is not supported. |
| InvalidDiskId.NotFound | The `DiskId` entered does not exist. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Renew cloud disk for one month and set auto renewal flag

#### Input Example

```
https://cbs.tencentcloudapi.com/?Action=RenewDisk
&DiskId=disk-jwk0zvrg
&DiskChargePrepaid.Period=1
&DiskChargePrepaid.RenewFlag=NOTIFY_AND_AUTO_RENEW
&<Common request parameters>
```

#### Output Example

```
{
  "Response": {
    "RequestId": "6e2e5089-244a-4102-d347-5a1f8058b1db"
  }
}
```

### Example 2 When renewing an instance, you need to renew the mounted prepaid cloud disk to make its expiration time the same as that of the instance.

#### Input Example

```
https://cbs.tencentcloudapi.com/?Action=RenewDisk
&DiskId=disk-jwk0zvrg
&DiskChargePrepaid.Period=1
&DiskChargePrepaid.CurInstanceDeadline=2018-03-30 20:15:03
&DiskChargePrepaid.RenewFlag=NOTIFY_AND_AUTO_RENEW
&<Common request parameters>
```

#### Output Example

```
{
  "Response": {
    "DiskPrice": {
      "DiscountPrice": 9.0,
      "OriginalPrice": 9.0
    },
    "RequestId": "55db49cf-b9d7-da27-825b-5a02ba6884ca"
  }
}
```


