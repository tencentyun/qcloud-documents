## Description

This API (DescribeHardwareSpecification) is used to obtain the configuration information of custom model components.

Domain name for API access: bm.api.qcloud.com

## Request

### Request Example
```
https://bm.api.qcloud.com/v2/index.php?
	Action=DescribeHardwareSpecification
	&<Common request parameters>
```

### Request Parameter

Common request parameters are required when the API is called. The Action field for this API is DescribeHardwareSpecification.

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
    "data": {
		"cpu": [{
			"cpuId": 1,
			"cpuDesc": "E5-2620v3 (6\u6838)  * 2",
			"series": "1",
			"haveRaidCard": [0,
			1]
		},
		{
			"cpuId": 3,
			"cpuDesc": "E5-2670v3 (12\u6838)  * 2",
			"series": "1",
			"haveRaidCard": [1]
		},
		{
			"cpuId": 4,
			"cpuDesc": "E5-2620v4 (8\u6838) * 2",
			"series": "2",
			"haveRaidCard": [0,
			1]
		},
		{
			"cpuId": 2,
			"cpuDesc": "E5-2680v4 (14\u6838)  * 2",
			"series": "2",
			"haveRaidCard": [0,
			1]
		}],
		"mem": [64,
		128,
		192,
		256,
		384,
		512],
		"disk": [{
			"diskTypeId": 1,
			"medium": "HDD",
			"interface": "SAS",
			"size": 300,
			"svrHeight": 1,
			"repr": "HDD-SAS-300G",
			"goodsCode": "bm_elastic_SAS_300G_10000RTM",
			"pid": 10933,
			"newGoodsCode": "bm_elastic_new_HDD-300G-SAS",
			"newPid": "11820",
			"order": "10",
			"priority": 40,
			"isUse": "1"
		},
		{
			"diskTypeId": 2,
			"medium": "HDD",
			"interface": "SAS",
			"size": 600,
			"svrHeight": 1,
			"repr": "HDD-SAS-600G",
			"goodsCode": "bm_elastic_SAS_600G_10000RTM",
			"pid": 10934,
			"newGoodsCode": "bm_elastic_new_HDD-600G-SAS",
			"newPid": "11821",
			"order": "20",
			"priority": 50,
			"isUse": "1"
		},
		{
			"diskTypeId": 3,
			"medium": "HDD",
			"interface": "SAS",
			"size": 1200,
			"svrHeight": 1,
			"repr": "HDD-SAS-1.2T",
			"goodsCode": "bm_elastic_SAS_1200G_10000RTM",
			"pid": 10935,
			"newGoodsCode": "bm_elastic_new_HDD-1200G-SAS",
			"newPid": "11822",
			"order": "30",
			"priority": 60,
			"isUse": "1"
		},
		{
			"diskTypeId": 4,
			"medium": "HDD",
			"interface": "SATA",
			"size": 2000,
			"svrHeight": 2,
			"repr": "HDD-SATA-2T",
			"goodsCode": "bm_elastic_SATA_2T_7200RTM",
			"pid": 10936,
			"newGoodsCode": "bm_elastic_new_HDD-2T-SATA",
			"newPid": "11823",
			"order": "40",
			"priority": 70,
			"isUse": "1"
		},
		{
			"diskTypeId": 5,
			"medium": "HDD",
			"interface": "SATA",
			"size": 4000,
			"svrHeight": 2,
			"repr": "HDD-SATA-4T",
			"goodsCode": "bm_elastic_SATA_4T_7200RTM",
			"pid": 10937,
			"newGoodsCode": "bm_elastic_new_HDD-4T-SATA",
			"newPid": "11824",
			"order": "50",
			"priority": 80,
			"isUse": "1"
		},
		{
			"diskTypeId": 6,
			"medium": "HDD",
			"interface": "SATA",
			"size": 8000,
			"svrHeight": 2,
			"repr": "HDD-SATA-8T",
			"goodsCode": "bm_elastic_SATA_8T_7200RTM",
			"pid": 11049,
			"newGoodsCode": "bm_elastic_new_HDD-8T-SATA",
			"newPid": "11825",
			"order": "60",
			"priority": 90,
			"isUse": "1"
		},
		{
			"diskTypeId": 7,
			"medium": "SSD",
			"interface": "SATA",
			"size": 240,
			"svrHeight": 1,
			"repr": "SSD-SATA-240G",
			"goodsCode": "bm_elastic_SSD_240g",
			"pid": 10938,
			"newGoodsCode": "bm_elastic_new_SSD-240G",
			"newPid": "11826",
			"order": "70",
			"priority": 10,
			"isUse": "1"
		},
		{
			"diskTypeId": 8,
			"medium": "SSD",
			"interface": "SATA",
			"size": 480,
			"svrHeight": 1,
			"repr": "SSD-SATA-480G",
			"goodsCode": "bm_elastic_SSD_480G",
			"pid": 10939,
			"newGoodsCode": "bm_elastic_new_SSD-480G",
			"newPid": "11827",
			"order": "80",
			"priority": 20,
			"isUse": "1"
		},
		{
			"diskTypeId": 9,
			"medium": "SSD",
			"interface": "SATA",
			"size": 800,
			"svrHeight": 1,
			"repr": "SSD-SATA-800G",
			"goodsCode": "bm_elastic_SSD_800G",
			"pid": 10940,
			"newGoodsCode": "bm_elastic_new_SSD-800G",
			"newPid": "11828",
			"order": "90",
			"priority": 30,
			"isUse": "1"
		},
		{
			"diskTypeId": 10,
			"medium": "SSD",
			"interface": "U.2",
			"size": 2000,
			"svrHeight": 1,
			"repr": "SSD-NVME-2T",
			"goodsCode": "bm_elastic_Nvme_SSD_2T",
			"pid": 11708,
			"newGoodsCode": "bm_elastic_new_NVME-SSD-2T",
			"newPid": "11829",
			"order": "100",
			"priority": 200,
			"isUse": "1"
		}],
		"special": []
	}
}
```

## Response Parameters
The response parameter section contains two layers of structure. The outer layer shows the response result of the API, and the inner layer shows the specific API contents, including the configurations of custom model components.

| Parameter Name | Type | Description |
| ------- | ------ | ---------------------------------------- |
| code | Int | Error code. 0: Successful; other values: Failed. For more information, please see [Error Codes](/doc/api/456/6725). |
| message | String | Error Message |
| data | Object | Array element is the configuration information of custom model components, including CPU, memory, disk, etc. See details below. |

Parameter data is composed as follows:

| Parameter Name | Type | Description |
| ---- | ------------- | ---------------------------------------- |
| cpu | Array (Object) | An array of objects. Array element is CPU model. See details below. |
| mem | Array (Int) | Integer array. Array element is mem value (in GB), such as [64, 128, 256, 384, 512]. |
| disk | Array (Object) | An array of objects. Array element is disk model. See details below. |

Parameter CPU is composed as follows:

| Parameter Name | Type | Description |
| ------------ | ---------- | ----------------------------- |
| cpuId | Int | CPU ID |
| cpuDesc | String | CPU model description |
| series | Int | Model series |
| haveRaidCard | Array (Int) | Supported RAID mode. 0: With RAID card. 1: No RAID card. |

Parameter disk is composed as follows:

| Parameter Name | Type | Description |
| ---------- | ------ | ----------- |
| diskTypeId | Int | Integer ID of the disk |
| medium | String | Medium type |
| interface | String | Disk interface type |
| size | Int | Disk capacity |
| svrHeight | Int | Model height, 1u or 2u |
| repr | String | Description of disk model |
| goodsCode | String | Code |
| pid | Int | Billing ID (internal only) |
| order | String | Sorting mode (internal only) |
| priority | Int | Disk selection sequence |
| newGoodsCode | String | New code |
| newPid | String | New billing ID (internal only) |
| isUse | String | Whether to display (internal only) |
			
## Error Code
| Error Code | Error Message | Error Description |
| ---- | --------------------- | ------- |
| 9001 | InternalError.DbError | An error occurred while operating the database |

## Practical Case

### Input

```
https://bm.api.qcloud.com/v2/index.php?
	Action=DescribeHardwareSpecification
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
    "data": {
		"cpu": [{
			"cpuId": 1,
			"cpuDesc": "E5-2620v3 (6\u6838)  * 2",
			"series": "1",
			"haveRaidCard": [0,
			1]
		},
		{
			"cpuId": 3,
			"cpuDesc": "E5-2670v3 (12\u6838)  * 2",
			"series": "1",
			"haveRaidCard": [1]
		},
		{
			"cpuId": 4,
			"cpuDesc": "E5-2620v4 (8\u6838) * 2",
			"series": "2",
			"haveRaidCard": [0,
			1]
		},
		{
			"cpuId": 2,
			"cpuDesc": "E5-2680v4 (14\u6838)  * 2",
			"series": "2",
			"haveRaidCard": [0,
			1]
		}],
		"mem": [64,
		128,
		192,
		256,
		384,
		512],
		"disk": [{
			"diskTypeId": 1,
			"medium": "HDD",
			"interface": "SAS",
			"size": 300,
			"svrHeight": 1,
			"repr": "HDD-SAS-300G",
			"goodsCode": "bm_elastic_SAS_300G_10000RTM",
			"pid": 10933,
			"newGoodsCode": "bm_elastic_new_HDD-300G-SAS",
			"newPid": "11820",
			"order": "10",
			"priority": 40,
			"isUse": "1"
		},
		{
			"diskTypeId": 2,
			"medium": "HDD",
			"interface": "SAS",
			"size": 600,
			"svrHeight": 1,
			"repr": "HDD-SAS-600G",
			"goodsCode": "bm_elastic_SAS_600G_10000RTM",
			"pid": 10934,
			"newGoodsCode": "bm_elastic_new_HDD-600G-SAS",
			"newPid": "11821",
			"order": "20",
			"priority": 50,
			"isUse": "1"
		},
		{
			"diskTypeId": 3,
			"medium": "HDD",
			"interface": "SAS",
			"size": 1200,
			"svrHeight": 1,
			"repr": "HDD-SAS-1.2T",
			"goodsCode": "bm_elastic_SAS_1200G_10000RTM",
			"pid": 10935,
			"newGoodsCode": "bm_elastic_new_HDD-1200G-SAS",
			"newPid": "11822",
			"order": "30",
			"priority": 60,
			"isUse": "1"
		},
		{
			"diskTypeId": 4,
			"medium": "HDD",
			"interface": "SATA",
			"size": 2000,
			"svrHeight": 2,
			"repr": "HDD-SATA-2T",
			"goodsCode": "bm_elastic_SATA_2T_7200RTM",
			"pid": 10936,
			"newGoodsCode": "bm_elastic_new_HDD-2T-SATA",
			"newPid": "11823",
			"order": "40",
			"priority": 70,
			"isUse": "1"
		},
		{
			"diskTypeId": 5,
			"medium": "HDD",
			"interface": "SATA",
			"size": 4000,
			"svrHeight": 2,
			"repr": "HDD-SATA-4T",
			"goodsCode": "bm_elastic_SATA_4T_7200RTM",
			"pid": 10937,
			"newGoodsCode": "bm_elastic_new_HDD-4T-SATA",
			"newPid": "11824",
			"order": "50",
			"priority": 80,
			"isUse": "1"
		},
		{
			"diskTypeId": 6,
			"medium": "HDD",
			"interface": "SATA",
			"size": 8000,
			"svrHeight": 2,
			"repr": "HDD-SATA-8T",
			"goodsCode": "bm_elastic_SATA_8T_7200RTM",
			"pid": 11049,
			"newGoodsCode": "bm_elastic_new_HDD-8T-SATA",
			"newPid": "11825",
			"order": "60",
			"priority": 90,
			"isUse": "1"
		},
		{
			"diskTypeId": 7,
			"medium": "SSD",
			"interface": "SATA",
			"size": 240,
			"svrHeight": 1,
			"repr": "SSD-SATA-240G",
			"goodsCode": "bm_elastic_SSD_240g",
			"pid": 10938,
			"newGoodsCode": "bm_elastic_new_SSD-240G",
			"newPid": "11826",
			"order": "70",
			"priority": 10,
			"isUse": "1"
		},
		{
			"diskTypeId": 8,
			"medium": "SSD",
			"interface": "SATA",
			"size": 480,
			"svrHeight": 1,
			"repr": "SSD-SATA-480G",
			"goodsCode": "bm_elastic_SSD_480G",
			"pid": 10939,
			"newGoodsCode": "bm_elastic_new_SSD-480G",
			"newPid": "11827",
			"order": "80",
			"priority": 20,
			"isUse": "1"
		},
		{
			"diskTypeId": 9,
			"medium": "SSD",
			"interface": "SATA",
			"size": 800,
			"svrHeight": 1,
			"repr": "SSD-SATA-800G",
			"goodsCode": "bm_elastic_SSD_800G",
			"pid": 10940,
			"newGoodsCode": "bm_elastic_new_SSD-800G",
			"newPid": "11828",
			"order": "90",
			"priority": 30,
			"isUse": "1"
		},
		{
			"diskTypeId": 10,
			"medium": "SSD",
			"interface": "U.2",
			"size": 2000,
			"svrHeight": 1,
			"repr": "SSD-NVME-2T",
			"goodsCode": "bm_elastic_Nvme_SSD_2T",
			"pid": 11708,
			"newGoodsCode": "bm_elastic_new_NVME-SSD-2T",
			"newPid": "11829",
			"order": "100",
			"priority": 200,
			"isUse": "1"
		}],
		"special": []
	}
}
```


