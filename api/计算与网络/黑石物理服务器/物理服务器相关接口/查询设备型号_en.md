## Description

This API (DescribeDeviceClass) is used to obtain the list of device classes.

Domain name for API access: bm.api.qcloud.com

## Request

### Request Example
```
https://bm.api.qcloud.com/v2/index.php?
	Action=DescribeDeviceClass
	&<Common request parameters>
```

### Request Parameter

Common request parameters are required when the API is called. The Action field for this API is DescribeDeviceClass.

| Parameter Name | Required | Type | Description |
| ---- | ---- | ---- | ---- |
| None | - | - | - |


## Response

### Response Example

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        {
			"deviceClass": "M1",
			"deviceClassDisplay": "PS000",
			"useType": "Standard",
			"eUseType": "standard",
			"cpuDesc": "E5-2620v3(6 cores)*2",
			"memDesc": "128GB",
			"diskDesc": "6*300G(SAS)",
			"canRaid": "1",
			"nicDesc": "1G * 2",
			"pid": "10711",
			"isSale": "1",
			"isUefi": "0",
			"gpuDesc": "",
			"deviceClassCode": "PS000v1",
			"series": "1",
			"discount": 100,
			"unitPrice": 381000,
			"realPrice": 381000
		},
		{
			"deviceClass": "M10",
			"deviceClassDisplay": "PS100",
			"useType": "Standard",
			"eUseType": "standard",
			"cpuDesc": "E5-2670v3(12 cores)*2",
			"memDesc": "128GB",
			"diskDesc": "12*300GB(SAS)",
			"canRaid": "1",
			"nicDesc": "10G * 2",
			"pid": "10532",
			"isSale": "1",
			"isUefi": "1",
			"gpuDesc": "",
			"deviceClassCode": "PS100v1",
			"series": "1",
			"discount": 100,
			"unitPrice": 590000,
			"realPrice": 590000
		}
    ]
}
```
## Response Parameters

The response parameter section contains two layers of structure. The outer layer shows the response result of the API, and the inner layer shows the specific API contents, including models.

| Parameter Name | Type | Description |
| ------- | ------------- | ---------------------------------------- |
| code | Int | Error code. 0: Successful; other values: Failed. For more information, please see [Error Codes](/doc/api/456/6725). |
| message | String | Error Message |
| data | Array (Object) | An array of objects. Array element is the device information. See details below. |


Parameter device is composed as follows:

| Parameter Name | Type | Description |
| ------------------ | ------ | ------------------- |
| deviceClass | String | Model, such as M10, B6, which is no longer in use. |
| deviceClassCode | String | Model, such as PS100v1, PS000v1 |
| deviceClassDisplay | String | Model display code, which is no longer in use. |
| series | Int | Model series |
| useType | String | Scenario type |
| eUseType | String | Scenario type ID |
| cpuDesc | String | CPU information |
| memDesc | String | Memory Information |
| diskDesc | String | Disk information |
| nicDesc | String | ENI information |
| gpuDesc | String | GPU information |
| canRaid | Int | RAID is allowed or not. 1: Yes; 0: No. |
| pid | Int | Product ID |
| isSale | Int | Whether to purchase. 1: Yes; 0: No. |
| isUefi | Int | UEFI is supported or not. 1: Yes; 0: No. |
| discount | Int | Discount, which is calculated by dividing "discount" by 100. |
| unitPrice | Int | Price of the model before discount (in cents) |
| realPrice | Int | Price of the model after discount (in cents) |


## Error Codes
| Error Code | Error Message | Error Description |
| ----- | --------------------- | ------- |
| 9001 | InternalError.DbError | An error occurred while operating the database |
| 10001 | InvalidParameter | Invalid parameter |


## Practical Case

### Input

```
https://bm.api.qcloud.com/v2/index.php?
	Action=DescribeDeviceClass
	&SecretId=AKID52SKw5uMEy3jhpMUBqSylEBJBby6E0KC
	&Nonce=48476
	&Timestamp=1476436689
	&Region=bj
	&Signature=afRlJQ0disdT97B7uIfVB4v2KWo%3D
```
### Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        {
			"deviceClass": "M1",
			"deviceClassDisplay": "PS000",
			"useType": "Standard",
			"eUseType": "standard",
			"cpuDesc": "E5-2620v3(6 cores)*2",
			"memDesc": "128GB",
			"diskDesc": "6*300G(SAS)",
			"canRaid": "1",
			"nicDesc": "1G * 2",
			"pid": "10711",
			"isSale": "1",
			"isUefi": "0",
			"gpuDesc": "",
			"deviceClassCode": "PS000v1",
			"series": "1",
			"discount": 100,
			"unitPrice": 381000,
			"realPrice": 381000
		},
		{
			"deviceClass": "M10",
			"deviceClassDisplay": "PS100",
			"useType": "Standard",
			"eUseType": "standard",
			"cpuDesc": "E5-2670v3(12 cores)*2",
			"memDesc": "128GB",
			"diskDesc": "12*300GB(SAS)",
			"canRaid": "1",
			"nicDesc": "10G * 2",
			"pid": "10532",
			"isSale": "1",
			"isUefi": "1",
			"gpuDesc": "",
			"deviceClassCode": "PS100v1",
			"series": "1",
			"discount": 100,
			"unitPrice": 590000,
			"realPrice": 590000
		}
    ]
}
```


