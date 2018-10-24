## Description

This API (DescribeDeviceClassPartition) is used to obtain the RAID mode of the device class.

Domain name for API access: bm.api.qcloud.com

## Request

### Request Example
```
https://bm.api.qcloud.com/v2/index.php?
	Action=DescribeDeviceClassPartition
	&<Common request parameters>
	&deviceClassCode=<Device class>
	&cpuId=<cpuId type>
	&mem=<Memory size>
	&haveRaidCard=<RAID card is required or not>
	&diskTypeId1=<Type of disk 1>
	&diskNum1=<Quantity of disk 1>
	&diskTypeId2=<Type of disk 2>
	&diskNum2=<Quantity of disk 2>
```

### Request Parameter

The following request parameter list only provides API request parameters. Common request parameters are required when the API is called. For other parameters, please see [Common Request Parameters](/doc/api/456/6718) page. The Action field for this API is DescribeDeviceClassPartition.

| Parameter Name | Required | Type | Description |
| ------------ | ---- | ------ | ---------------------------------------- |
| deviceClassCode | No | String | Device class. Tencent device class can be obtained via the API [Query Device Class (DescribeDeviceClass)](/doc/api/456/6636). This parameter is required for standard models. |
| cpuId | No | Int | cpuId type. This parameter is required for custom models. 1: E5-2620v3 (6 cores) * 2; 2: E5-2680v4 (14 cores) * 2. |
| mem | No | Int | Memory size (in GB). This parameter is required for custom models. Value range: [64, 128, 256, 384, 512]. |
| haveRaidCard | No | Int | RAID card is required or not. This parameter is required for custom models. 0: RAID card is not required; 1: RAID card is required. |
| diskTypeId1 | No | Int | Type of disk 1. This parameter is required for custom models. The value can be obtained via the API [Query Custom Model Component Information (DescribeDeviceClassPartition)](/document/product/386/10968). |
| diskNum1 | No | Int | Quantity of disk 1. This parameter is required for custom models. Value range: 1-12. For disks with RAID cards, the number must be even. |
| diskTypeId2 | No | Int | Type of disk 2. This parameter is required for custom models. The value can be obtained via the API [Query Custom Model Component Information (DescribeDeviceClassPartition)](/document/product/386/10968). |
| diskNum2 | No | Int | Quantity of disk 2. This parameter is required for custom models. Value range: 1-12. For disks with RAID cards, the number must be even and the sum of diskNum1+diskNum2 must be less than 12. |

## Response

### Response Example
```
{
  "version": "1.0",
  "eventId": 121,
  "timestamp": 1352121016,
  "componentName": "bmApi",
  "returnCode": 0,
  "returnMessage": "OK",
  "data": {
    "1": {
      "raidId": 1,
      "raid": "RAID0",
      "raidDisplay": "RAID0",
      "description": "",
      "systemDiskSize": 3352,
      "sysRootSpace": 10,
      "sysSwaporuefiSpace": 2,
      "sysUsrlocalSpace": 20,
      "sysDataSpace": 3320,
      "sysIsUefiType": true,
      "dataDiskSize": 0
    },
    "2": {
      "raidId": 2,
      "raid": "RAID5",
      "raidDisplay": "RAID5",
      "description": "",
      "systemDiskSize": 3073,
      "sysRootSpace": 10,
      "sysSwaporuefiSpace": 2,
      "sysUsrlocalSpace": 20,
      "sysDataSpace": 3041,
      "sysIsUefiType": true,
      "dataDiskSize": 0
    }
  }
}
```

## Response Parameters
The response parameter section contains two layers of structure. The outer layer shows the response result of the API, and the inner layer shows the specific API contents, including RAID.

| Parameter Name | Type | Description |
| ------- | ------ | ---------------------------------------- |
| code | Int | Error code. 0: Successful; other values: Failed. For more information, please see [Error Codes](/doc/api/456/6725). |
| message | String | Error Message |
| data | Object | RAID ID is the key, and the corresponding value is the object which is the RAID description. See details below. |

Parameter RAID is composed as follows:

| Parameter Name | Type | Description |
| ------------------ | ------- | ------------------------------------ |
| raidId | Int | RAID type ID |
| raid | String | RAID name |
| raidDisplay | String | RAID frontend display |
| description | String | RAID description |
| systemDiskSize | Int | System disk size, which is specified when you purchase machines or specify partitions upon reinstallation. You can use this value as reference to configure the size of partitions. |
| dataDiskSize | Int | Data disk size |
| sysIsUefiType | Boolean | Indicate whether to start machine in UEFI mode. This determines whether the /boot/efi partition exists in the partition. |
| sysRootSpace | Int | Default root partition size. It is called by users and is negligible. |
| sysSwaporuefiSpace | Int | Default size of the swap partition or the /boot/efi partition. It is called by users and is negligible. |
| sysUsrlocalSpace | Int | Default size of the /usr/local partition. It is called by users and is negligible. |
| sysDataSpace | Int | Default size of the /data partitionv. It is called by users and is negligible. |

## Error Code
| Error Code | Error Message | Error Description |
| ---- | --------------------- | ------- |
| 9001 | InternalError.DbError | An error occurred while operating the database |

## Practical Case

### Input

```
https://bm.api.qcloud.com/v2/index.php?
	Action=DescribeDeviceClassPartition
	&deviceClassCode=PS100v1
	&SecretId=AKID52SKw5uMEy3jhpMUBqSylEBJBby6E0KC
	&Nonce=48476
	&Timestamp=1476436689
	&Region=bj
	&Signature=afRlJQ0disdT97B7uIfVB4v2KWo%3D
```

### Output

```
{
  "version": "1.0",
  "eventId": 121,
  "timestamp": 1352121016,
  "componentName": "bmApi",
  "returnCode": 0,
  "returnMessage": "OK",
  "data": {
    "1": {
      "raidId": 1,
      "raid": "RAID0",
      "raidDisplay": "RAID0",
      "description": "",
      "systemDiskSize": 3352,
      "sysRootSpace": 10,
      "sysSwaporuefiSpace": 2,
      "sysUsrlocalSpace": 20,
      "sysDataSpace": 3320,
      "sysIsUefiType": true,
      "dataDiskSize": 0
    },
    "2": {
      "raidId": 2,
      "raid": "RAID5",
      "raidDisplay": "RAID5",
      "description": "",
      "systemDiskSize": 3073,
      "sysRootSpace": 10,
      "sysSwaporuefiSpace": 2,
      "sysUsrlocalSpace": 20,
      "sysDataSpace": 3041,
      "sysIsUefiType": true,
      "dataDiskSize": 0
    },
    "3": {
      "raidId": 3,
      "raid": "RAID1+0",
      "raidDisplay": "RAID1+0",
      "description": "",
      "systemDiskSize": 1676,
      "sysRootSpace": 10,
      "sysSwaporuefiSpace": 2,
      "sysUsrlocalSpace": 20,
      "sysDataSpace": 1644,
      "sysIsUefiType": true,
      "dataDiskSize": 0
    },
    "4": {
      "raidId": 4,
      "raid": "[6+6]RAID50",
      "raidDisplay": "RAID50",
      "description": "",
      "systemDiskSize": 2793,
      "sysRootSpace": 10,
      "sysSwaporuefiSpace": 2,
      "sysUsrlocalSpace": 20,
      "sysDataSpace": 2761,
      "sysIsUefiType": true,
      "dataDiskSize": 0
    },
    "5": {
      "raidId": 5,
      "raid": "2RAID1+[5+5]RAID50",
      "raidDisplay": "2RAID1 + 10RAID50",
      "description": "",
      "systemDiskSize": 279,
      "sysRootSpace": 10,
      "sysSwaporuefiSpace": 2,
      "sysUsrlocalSpace": 20,
      "sysDataSpace": 247,
      "sysIsUefiType": true,
      "dataDiskSize": 2235
    },
    "6": {
      "raidId": 6,
      "raid": "NORAID",
      "raidDisplay": "NO RAID",
      "description": "",
      "systemDiskSize": 279,
      "sysRootSpace": 10,
      "sysSwaporuefiSpace": 2,
      "sysUsrlocalSpace": 20,
      "sysDataSpace": 247,
      "sysIsUefiType": true,
      "dataDiskSize": 3073
    },
    "7": {
      "raidId": 7,
      "raid": "2RAID1+10RAID10",
      "raidDisplay": "2RAID1 + 10RAID10",
      "description": "2 disks constitute RAID 1 + 10 disks constitute RAID 2",
      "systemDiskSize": 279,
      "sysRootSpace": 10,
      "sysSwaporuefiSpace": 2,
      "sysUsrlocalSpace": 20,
      "sysDataSpace": 247,
      "sysIsUefiType": true,
      "dataDiskSize": 1396
    },
    "11": {
      "raidId": 11,
      "raid": "2RAID1+10RAID0",
      "raidDisplay": "2RAID1 + 10RAID0",
      "description": "",
      "systemDiskSize": 279,
      "sysRootSpace": 10,
      "sysSwaporuefiSpace": 2,
      "sysUsrlocalSpace": 20,
      "sysDataSpace": 247,
      "sysIsUefiType": true,
      "dataDiskSize": 2793
    },
    "12": {
      "raidId": 12,
      "raid": "4RAID10+8RAID5",
      "raidDisplay": "4RAID10 + 8RAID5",
      "description": "",
      "systemDiskSize": 558,
      "sysRootSpace": 10,
      "sysSwaporuefiSpace": 2,
      "sysUsrlocalSpace": 20,
      "sysDataSpace": 526,
      "sysIsUefiType": true,
      "dataDiskSize": 1955
    },
    "13": {
      "raidId": 13,
      "raid": "2RAID1+2RAID1+8RAID10",
      "raidDisplay": "2RAID1 + 2RAID1 + 8RAID10",
      "description": "",
      "systemDiskSize": 279,
      "sysRootSpace": 10,
      "sysSwaporuefiSpace": 2,
      "sysUsrlocalSpace": 20,
      "sysDataSpace": 247,
      "sysIsUefiType": true,
      "dataDiskSize": 1396
    },
    "14": {
      "raidId": 14,
      "raid": "4RAID10+8RAID10",
      "raidDisplay": "4RAID10 + 8RAID10",
      "description": "",
      "systemDiskSize": 558,
      "sysRootSpace": 10,
      "sysSwaporuefiSpace": 2,
      "sysUsrlocalSpace": 20,
      "sysDataSpace": 526,
      "sysIsUefiType": true,
      "dataDiskSize": 1117
    },
    "15": {
      "raidId": 15,
      "raid": "4RAID10+4RAID10+2RAID1+2RAID1",
      "raidDisplay": "4RAID10 + 4RAID10 + 2RAID1 + 2RAID1",
      "description": "",
      "systemDiskSize": 558,
      "sysRootSpace": 10,
      "sysSwaporuefiSpace": 2,
      "sysUsrlocalSpace": 20,
      "sysDataSpace": 526,
      "sysIsUefiType": true,
      "dataDiskSize": 1117
    }
  }
}
```


