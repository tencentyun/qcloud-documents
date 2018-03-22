## Description

This API (DescribeDeviceHardwareInfo) is used to query the hardware configuration information of the device, such as CPU model, memory size, the size and quantity of disks.

Domain name for API access: bm.api.qcloud.com


## Request

### Request Example
```
https://bm.api.qcloud.com/v2/index.php?
	Action=DescribeDeviceHardwareInfo
	&<Common request parameters>	
	&instanceIds.0=<Device ID1>
	&instanceIds.1=<Device ID2>
```

### Request Parameter

The following request parameter list only provides API request parameters. Common request parameters are required when the API is called. For other parameters, please see [Common Request Parameters](/doc/api/456/6718) page. The Action field for this API is DescribeDevicePosition.

| Parameter Name | Required | Type | Description |
| instanceIds | Yes | Array (String) | List of device IDs |


## Response

### Response Example
```
{
  "code": 0,
  "message": "",
  "codeDesc": "Success",
  "data": [{
		"instanceId": "cpm-3qrq1i82",
		"deviceClass": "Y0-BS05v1",
		"isElastic": "1",
		"cpmPayMode": "2",
		"cpuId": "1",
		"mem": "128",
		"haveRaidCard": "0",
		"diskTypeId1": "8",
		"diskNum1": "4",
		"diskTypeId2": 4,
		"diskNum2": 8,
		"cpuDesc": "E5-2620v3 (6\u6838)  * 2",
		"memDesc": "128G",
		"diskDesc": "4*SSD-SATA-480G+8*HDD-SATA-2T",
		"nicDesc": "10G*2",
		"raidDesc": "\u4e0d\u652f\u6301",
		"goodsDetail": {
			"pid": 10947,
			"bm_elastic_Y0-BS05": 1,
			"bm_elastic_SSD_480G": 4,
			"bm_elastic_SATA_2T_7200RTM": 8,
			"bm_elastic_MEM_32G": 4,
			"deviceClass": "Y0-BS05v1"
		}
	}]
}
```

## Response Parameters
The response parameter section contains two layers of structure. The outer layer shows the response result of the API, and the inner layer shows the specific API contents, including servers.

| Parameter Name | Type | Description |
| ------- | ------ | ---------------------------------------- |
| code | Int | Error code. 0: Successful; other values: Failed. For more information, please see [Error Codes](/doc/api/456/6725). |
| message | String | Error Message |
| data | Object | The total number of returned devices and device information. See details below. |

Parameter data is composed as follows:

| Parameter Name | Type | Description |
| ---------- | ------------- | ------------------------------------- |
| instanceId | String | Device instance ID |
| deviceClass | String | Tencent internal device type |
| IsElastic | Int | Whether it is a custom model |
| cpmPayMode | Int | Billing method of the model, 1: Prepaid; 2: Postpaid. |
| cpuId | Int | CPU model ID for custom models |
| mem | Int | Memory size (in GB) for custom models |
| haveRaidCard | Int | RAID card exists or not. 0: No RAID card; 1: With RAID card. |
| diskTypeId1 | Int | ID of disk 1 for custom models |
| diskNum1 | Int | Quantity of disk 1 for custom models |
| diskTypeId2 | Int | ID of disk 2 for custom models |
| diskNum2 | Int | Quantity of disk 2 for custom models |
| cpuDesc | String | CPU model description |
| memDesc | String | Memory description |
| diskDesc | String | Disk description |
| nicDesc | String | ENI description |
| raidDesc | String | Raid description is supported or not |
| goodsDetail | Array | Billing-related ID, which can be ignored. |


## Error Code

| Error Code | Error Message | Error Description |
| ---- | --------------------- | ------- |
| 9001 | InternalError.DbError | An error occurred while operating the database |


## Practical Case

### Input

```
https://bm.api.qcloud.com/v2/index.php?
Action=DescribeDeviceHardwareInfo
&Nonce=1187296601&Region=bj
&Timestamp=1508763150
&SecretId=AKID52SKw5uMEy3jhpMUBqSylEBJBby6E0KC
&instanceIds.0=cpm-cjm505sb
&instanceIds.1=cpm-1nk36wcj
&Signature=XynD%2FHNX7Aj42SiMU18L7gIOVZQ%3D
	
```

### Output

```
{
  "code": 0,
  "message": "",
  "codeDesc": "Success",
  "data": [{
		"instanceId": "cpm-3qrq1i82",
		"deviceClass": "Y0-BS05v1",
		"isElastic": "1",
		"cpmPayMode": "2",
		"cpuId": "1",
		"mem": "128",
		"haveRaidCard": "0",
		"diskTypeId1": "8",
		"diskNum1": "4",
		"diskTypeId2": 4,
		"diskNum2": 8,
		"cpuDesc": "E5-2620v3 (6\u6838)  * 2",
		"memDesc": "128G",
		"diskDesc": "4*SSD-SATA-480G+8*HDD-SATA-2T",
		"nicDesc": "10G*2",
		"raidDesc": "\u4e0d\u652f\u6301",
		"goodsDetail": {
			"pid": 10947,
			"bm_elastic_Y0-BS05": 1,
			"bm_elastic_SSD_480G": 4,
			"bm_elastic_SATA_2T_7200RTM": 8,
			"bm_elastic_MEM_32G": 4,
			"deviceClass": "Y0-BS05v1"
		}
	}]
}
```
