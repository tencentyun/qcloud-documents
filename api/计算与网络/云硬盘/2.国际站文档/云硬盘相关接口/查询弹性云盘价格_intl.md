## 1. API Description

This API (InquiryStoragePrice) is used to query the price of [Elastic Cloud Storage](https://intl.cloud.tencent.com/doc/product/362/2345). The API's functions vary with different input parameters. For details, refer to the description later.

Domain for API request:<font style="color:red">cbs.api.qcloud.com</font>

Usage restrictions:

1. Only query for the price of elastic cloud storages is supported

## 2. Input Parameters

### 2.1. Query the price of the newly purchased elastic cloud storage

| Parameter Name | Required  | Type | Description |
| ------- | ------- | ------- | --- | 
| inquiryType | Yes | String | For query for the price of newly purchased cloud disks, the input parameter is always "create" | 
| storageType | Yes | String | Type of the Cloud Block Storage. HDD cloud storage: cloudBasic, SSD cloud storage: cloudSSD |
| storageSize | Yes | Int | Size of Cloud Block Storage (GB). <br>The minimum size of a HDD cloud storage is 10GB, and the minimum of a SSD cloud storage is 250GB. The increment for both is 10GB. |
| goodsNum | Yes | Int | The number of Cloud Block Storages purchased. The maximum value refer to [Cloud Block Storage Usage Restrictions](https://intl.cloud.tencent.com/doc/product/362/5145). | 
| period | Yes | Int | Length of purchase (month) | 
| payMode | Yes | String | Payment mode of the Cloud Block Storage. Only the annual or monthly plan: prePay is supported currently | 
 
### 2.2. Query the renewal price of elastic cloud storages

| Parameter Name | Required  | Type | Description |
| ------- | ------- | ------- | --- | 
| inquiryType | Yes | String | For renewals, the input parameter is always "renew" | 
| storageId | Yes | String | ID of the cloud storage, which can be queried via [DescribeCbsStorages (Query Cloud Disk Information)](https://cloud.tencent.com/document/api/364/2519) API |
| period | Yes | Int | Length of purchase (month) |
 
 
### 2.3. Query the expansion price of elastic cloud storages

| Parameter Name | Required | Type | Description |
| ------- | ------- | ------- | ------- | 
| inquiryType | Yes | String | For query for the expansion price, the input parameter is always "resize" | 
| storageId | Yes | String | ID of the cloud storage, which can be queried via [DescribeCbsStorages (Query Cloud Disk Information)](/doc/api/364/2519) API |
| storageSize | Yes | Int | The expanded size of Cloud Block Storage (GB), which may not be less than the current size of the Cloud Block Storage. |
 
 
 
## 3. Output Parameters

| Parameter Name | Type | Description |
| ------- | --- | --- |
| code | Int | Common error code; 0: Succeeded; other values: Failed. For details, refer to the [Error Code page](https://cloud.tencent.com/doc/api/364/%E9%94%99%E8%AF%AF%E7%A0%81) |
| message | String | Error message. For details, refer to the [Error Code page](https://cloud.tencent.com/doc/api/364/%E9%94%99%E8%AF%AF%E7%A0%81)|
| price | Int | The total price of the product |
 

## 4. Error Code List

The following list only provides the business logic error codes for this API. For additional common error codes, refer to [Cloud Block Storage Error Codes](https://cloud.tencent.com/doc/api/364/4207).

| Error Code | English Description | Error Description |
| ------- | ------- | ------- |
| 9003 | InvalidParameter | The parameter is incorrect |
| 16000 | InvalidInstanceId.DiskNotFound | The disk does not exist |
| 16008 | IncorrectInstanceStatus.OnlySupportElasticCloudDisk | Only elastic cloud storages are supported |

## 5. Example

Input
<pre>
https://cbs.api.qcloud.com/v2/index.php?Action=InquiryStoragePrice
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&inquiryType=create
&storageType=cloudBasic
&storageSize=10
&goodsNum=1
&period=1
&payMode=prePay
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "price":"300"
}
```
 
 
 

