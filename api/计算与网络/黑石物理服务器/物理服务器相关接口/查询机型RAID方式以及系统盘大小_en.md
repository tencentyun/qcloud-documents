## 1. API Description

This API (DescribeDeviceClassPartition) is used to acquire the corresponding RAID method of the device class.
Domain for API request: bm.api.qcloud.com



## 2. Input Parameters
The following request parameter list only provides API request parameters. For additional parameters, see [Common Request Parameters](/doc/api/456/6718) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| deviceClass | Yes | String | Device class. Tencent device class, deviceClass. You can acquire device class by using the [Query Device Class (DescribeDeviceClass)](/doc/api/456/6636) API |



## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, please see [Common Error Codes](/doc/api/456/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. |
| data | Obj | Array elements are the individual information of each RAID |

RAID information field

| Parameter Name | Type | Description |
|---------|---------|---------|
| raidId | Int | RAID type ID |
| raid | String | RAID name |
| raidDisplay | String | RAID frontend display |
| description | String | RAID description |
| systemDiskSize | Int | System disk size. When purchasing machines or specifying partitions upon re-installation, you can use this value as reference to configure the size of partitions |
| dataDiskSize | Int | Data disk size |
| sysIsUefiType | boolean | Indicates whether to use UEFI boot. This determines whether the /boot/efi partition exists in the partition |
| sysRootSpace | Int | Default root partition size. Called by users. Negligible |
| sysSwaporuefiSpace | Int | Default size of the swap partition or the /boot/efi partition. Called by users. Negligible |
| sysUsrlocalSpace | Int | Default size of the /usr/local partition. Called by users. Negligible |
| sysDataSpace | Int | Default size of the /data partition. Called by users. Negligible |

  




## 4. Module Error Codes

| code | codeDesc | Description |
|------|------|------|
| 9001 | InternalError.DbError | An error occurred when operating the database |



## 5. Example
Input
```
https://bm.api.qcloud.com/v2/index.php?Action=DescribeDeviceClassRaid&deviceClass=M10&SecretId=AKID52SKw5uMEy3jhpMUBqSylEBJBby6E0KC&Nonce=48476&Timestamp=1476436689&Region=bj&Signature=afRlJQ0disdT97B7uIfVB4v2KWo%3D
```
Output
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
      "description": "Two disks form into RAID 1 + Ten disks form into RAID 10",
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


