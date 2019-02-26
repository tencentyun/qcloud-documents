## Description

This API (DescribeDeviceClassRaid) is used to obtain the RAID mode of the device class. It is recommended to use the [API DescribeDeviceClassPartition](/document/api/386/7370) instead of this API which has expired and does not support the RAID list of custom models.

Domain name for API access: bm.api.qcloud.com

## Request

### Request Example

```
https://bm.api.qcloud.com/v2/index.php?
	Action=DescribeDeviceClassRaid
	&<Common request parameters>
```

### Request Parameter

Common request parameters are required when the API is called. The Action field for this API is DescribeDeviceClassRaid.

| Parameter Name | Required | Type | Description |
| ---- | ---- | ---- | ---- |
| deviceClassCode | No | String | Device class code, such as PC000v1 |


## Response

### Response Example

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
		"PC000v1":{
			"1":{
				"deviceClass":"B6",
				"deviceClassCode":"PC000v1",
				"raidId":"1",
				"diskSize":"600G",
				"partition":{
					"/":10,
					"swap":2,
					"/usr/local":20,
					"data":568
				},
				"unFormatPartition":"",
				"updateTime":"2018-01-05 12:29:25",
				"raid":"RAID0",
				"raidDisplay":"RAID0",
				"description": "All disks constitute RAID 0, providing fast data reading but no redundancy. This level is suitable for applications that requires high reading speed but low data security."
			},
			"6":{
				"deviceClass":"B6",
				"deviceClassCode":"PC000v1",
				"raidId":"6",
				"diskSize":"600G",
				"partition":{
					"/":10,
					"swap":2,
					"/usr/local":20,
					"data":568
				},
				"unFormatPartition":{
					"/":10,
					"swap":2,
					"/usr/local":20,
					"data":268,
					"unformat":300
				},
				"updateTime":"2018-01-05 12:29:25",
				"raid":"NORAID",
				"raidDisplay":"NO RAID",
				"description": "Choosing not to build an RAID may put your data at risk of loss. Please proceed with caution."
			}
		},
        "PS100v1":{
            "1":{
                "deviceClass":"M10",
                "deviceClassCode":"PS100v1",
                "raidId":"1",
                "diskSize":"3600G",
                "partition":{
                    "/":10,
                    "swap":2,
                    "/usr/local":20,
                    "data":3568
                },
                "unFormatPartition":"",
                "updateTime":"2018-01-05 12:29:25",
                "raid":"RAID0",
                "raidDisplay":"RAID0",
                "description": "All disks constitute RAID 0, providing fast data reading but no redundancy. This level is suitable for applications that requires high reading speed but low data security."
            },
            "2":{
                "deviceClass":"M10",
                "deviceClassCode":"PS100v1",
                "raidId":"2",
                "diskSize":"3300G",
                "partition":{
                    "/":10,
                    "swap":2,
                    "/usr/local":20,
                    "data":3268
                },
                "unFormatPartition":"",
                "updateTime":"2018-01-05 12:29:25",
                "raid":"RAID5",
                "raidDisplay":"RAID5",
                "description": "All disks constitute RAID 5. This solution takes storage performance, data security and storage cost into account at the same time, and is suitable for scenarios where a large amount of data is expected to be read while less data is written."
            }
        }
    }
}
```

## Response Parameters

The response parameter section contains two layers of structure. The outer layer shows the response result of the API, and the inner layer shows the specific API contents, including the RAID mode of the device class.

| Parameter Name | Type | Description |
| ------- | ------ | ---------------------------------------- |
| code | Int | Error code. 0: Successful; other values: Failed. For more information, please see [Error Codes](/doc/api/456/6725). |
| message | String | Error Message |
| data | Object | RAID information for each model. See details below. |

Parameter data is composed as follows:

| Parameter Name | Type | Description |
| ---------------- | ------ | ---------------------------------------- |
| Model (e.g. "PC000v1", "PS100v1") | Object | The model is the key, and the corresponding value is the object which is the information on the RAID supported by the model. See details below. |

Parameter RAIDLIST is composed as follows:

| Parameter Name | Type | Description |
| ------------------ | ------ | ---------------------------------------- |
| RAID ID (e.g. "1", "2") | Object | RAID ID is the key, and the corresponding value is the object which is the RAID description. See details below. |


Parameter RAID is composed as follows:

| Parameter Name | Type | Description |
| ----------------- | ------ | ------------------------------ |
| deviceClass | String | Model, such as M10, B6 |
| raidId | String | RAID ID |
| diskSize | String | Disk size |
| partition | Object | Partition information (in GB). The partition name is the key, and the corresponding value is the partition size. |
| unFormatPartition | String | Unformatted partition. Default is none. |
| raid | String | RAID level |
| raidDisplay | String | The display name of a RAID level |
| description | String | Description |

## Error Codes
| Error Code | Error Message | Error Description |
| ---- | --------------------- | ------- |
| 9001 | InternalError.DbError | An error occurred while operating the database |


## Practical Case

### Input
```
https://bm.api.qcloud.com/v2/index.php?
	Action=DescribeDeviceClassRaid
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
		"PC000v1":{
			"1":{
				"deviceClass":"B6",
				"deviceClassCode":"PC000v1",
				"raidId":"1",
				"diskSize":"600G",
				"partition":{
					"/":10,
					"swap":2,
					"/usr/local":20,
					"data":568
				},
				"unFormatPartition":"",
				"updateTime":"2018-01-05 12:29:25",
				"raid":"RAID0",
				"raidDisplay":"RAID0",
				"description": "All disks constitute RAID 0, providing fast data reading but no redundancy. This level is suitable for applications that requires high reading speed but low data security."
			},
			"6":{
				"deviceClass":"B6",
				"deviceClassCode":"PC000v1",
				"raidId":"6",
				"diskSize":"600G",
				"partition":{
					"/":10,
					"swap":2,
					"/usr/local":20,
					"data":568
				},
				"unFormatPartition":{
					"/":10,
					"swap":2,
					"/usr/local":20,
					"data":268,
					"unformat":300
				},
				"updateTime":"2018-01-05 12:29:25",
				"raid":"NORAID",
				"raidDisplay":"NO RAID",
				"description": "Choosing not to build an RAID may put your data at risk of loss. Please proceed with caution."
			}
		},
        "PS100v1":{
            "1":{
                "deviceClass":"M10",
                "deviceClassCode":"PS100v1",
                "raidId":"1",
                "diskSize":"3600G",
                "partition":{
                    "/":10,
                    "swap":2,
                    "/usr/local":20,
                    "data":3568
                },
                "unFormatPartition":"",
                "updateTime":"2018-01-05 12:29:25",
                "raid":"RAID0",
                "raidDisplay":"RAID0",
                "description": "All disks constitute RAID 0, providing fast data reading but no redundancy. This level is suitable for applications that requires high reading speed but low data security."
            },
            "2":{
                "deviceClass":"M10",
                "deviceClassCode":"PS100v1",
                "raidId":"2",
                "diskSize":"3300G",
                "partition":{
                    "/":10,
                    "swap":2,
                    "/usr/local":20,
                    "data":3268
                },
                "unFormatPartition":"",
                "updateTime":"2018-01-05 12:29:25",
                "raid":"RAID5",
                "raidDisplay":"RAID5",
                "description": "All disks constitute RAID 5. This solution takes storage performance, data security and storage cost into account at the same time, and is suitable for scenarios where a large amount of data is expected to be read while less data is written."
            }
        }
    }
}
```

