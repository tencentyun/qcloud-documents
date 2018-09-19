Content  

## 1. API Description

This API (InquiryPriceRenewDisks) is used to inquire the prices for renewing cloud disks.

* Only the prices of renewed prepaid elastic cloud disks can be queried.
* The mounted cloud disk can be renewed together with the instance. The CurInstanceDeadline in the [DiskChargePrepaid](/document/product/362/15669#DiskChargePrepaid) parameter must be specified. In such case, you can inquire the price for renewing the cloud disk to the expiration time of the instance.
* You can specify different renewal lengths for multiple cloud disks. The price returned in such case is the total price for renewal of multiple cloud disks.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15637).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: InquiryPriceRenewDisks |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| DiskIds.N | Yes | Array of String | ID of the cloud disk, which can be queried via the API [DescribeDisks](/document/product/362/16315). |
| DiskChargePrepaids.N | No | Array of [DiskChargePrepaid](/document/api/362/15669#DiskChargePrepaid) | Prepaid mode, which is the relevant parameter setting for prepaid mode. This parameter is used to specify the usage period. If CurInstanceDeadline is specified in this parameter, the cloud disk is renewed to the expiration time of the server. If the price for batch renewal is inquired, this parameter corresponds to the Disks parameter and the number of elements must be the same. |
| NewDeadline | No | String | Specify the new expiration time of the cloud disk, in such format as 2017-12-17 00:00:00. The parameters `NewDeadline` and `DiskChargePrepaids` are two options to specify the inquiry length, and you must specify at least one. |
| ProjectId | No | Integer | ID of the project to which the cloud disk belongs. This parameter is only used for authentication. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| DiskPrice | [Price](/document/api/362/15669#Price) | This parameter indicates the price for the renewal of the cloud disk. |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InvalidDisk.NotPortable | Non-elastic cloud disks cannot be mounted. |
| InvalidDiskId.NotFound | The `DiskId` does not exist. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Inquire the Price for Renewing the Cloud Disk for 1 month

### Request parameters

```
https://cbs.tencentcloudapi.com/?Action=InquiryPriceRenewDisks
&DiskIds.0=disk-jwk0zvrg
&DiskChargePrepaids.0.Period=1
&<Common request parameters>
```
### Return parameters

```
{
  "Response": {
    "DiskPrice": {
      "DiscountPrice": 33.26,
      "OriginalPrice": 37.8
    },
    "RequestId": "7269a7c9-daa0-48aa-372a-5a1f8029a4f4"
  }
}
```

## Example 2 When renewing an instance, you need to renew the mounted prepaid cloud disk to make its expiration time the same as that of the instance.

### Scenario description

The current expiration time of the instance is: 2018-03-17 15:15:03, which needs to be renewed for one month. You can call this API to renew the prepaid cloud disk mounted on the instance to make its expiration time the same as that of the instance.

                
### Request parameters

```
https://cbs.tencentcloudapi.com/?Action=InquiryPriceRenewDisks
&DiskIds.0=disk-jwk0zvrg
&DiskChargePrepaids.0.Period=1
&DiskChargePrepaids.0.CurInstanceDeadline=2018-03-17 15:15:03
&<Common request parameters>
```
### Return parameters

```
{
  "Response": {
    "DiskPrice": {
      "DiscountPrice": 6.0,
      "OriginalPrice": 6.0
    },
    "RequestId": "f31302ca-7e60-412c-9d84-0675e09db295"
  }
}
```


        
