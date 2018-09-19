## 功能描述

DescribeDeviceClassPartition接口用来获取设备类型对应的RAID方式。

接口访问域名：bm.api.qcloud.com

## 请求

### 请求示例
```
https://bm.api.qcloud.com/v2/index.php?
	Action=DescribeDeviceClassPartition
	&<公共请求参数>
	&deviceClassCode=<设备类型>
	&cpuId=<cpuId类型>
	&mem=<内存大小>
	&haveRaidCard=<是否需要RAID卡>
	&diskTypeId1=<第一种规格硬盘类型>
	&diskNum1=<第一种规格硬盘的盘个数>
	&diskTypeId2=<第二种规格硬盘类型>
	&diskNum2=<第二种规格硬盘的盘个数>
```

### 请求参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，其它参数参见[公共请求参数](/doc/api/456/6718)页面。其中，此接口的Action字段为DescribeDeviceClassPartition。

| 参数名称         | 必选   | 类型     | 描述                                       |
| ------------ | ---- | ------ | ---------------------------------------- |
| deviceClassCode  | 否    | String | 设备类型。腾讯的设备类型deviceClass，通过接口[查询设备型号(DescribeDeviceClass)](/doc/api/456/6636) 获得设备类型。标准机型需要传入此参数。 |
| cpuId        | 否    | Int    | cpuId类型。自定义机型需要传入此参数。 1：E5-2620v3 (6核) *  2 ； 2：E5-2680v4 (14 核) * 2。 4 1：E5-2620v4 (8核) *  2 |
| mem          | 否    | Int    | 内存大小，单位G。 自定义机型需要传入此参数。取值范围[64，128，192，256，384，512]。 |
| haveRaidCard | 否    | Int    | 是否需要RAID卡。自定义机型需要传入此参数。0：不需要RAID卡； 1：需要RAID卡。 |
| diskTypeId1  | 否    | Int    | 第一种规格硬盘类型。自定义机型需要传入此参数。取值通过接口获得[查询自定义机型部件信息(DescribeHardwareSpecification)](/document/product/386/10968)。 |
| diskNum1     | 否    | Int    | 第一种规格硬盘的盘个数。自定义机型需要传入此参数。取值1~12。如果是有RAID卡的，盘数为偶数。 |
| diskTypeId2  | 否    | Int    | 第二种规格硬盘类型。取值通过接口获得[查询自定义机型部件信息(DescribeHardwareSpecification)](/document/product/386/10968)。 |
| diskNum2     | 否    | Int    | 第二种规格硬盘的盘个数。 |

## 响应

### 响应示例
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

### 响应参数
响应参数部分包含两层结构，外层展示接口的响应结果，内层展示具体的接口内容，包括RAID等信息。

| 参数名称    | 类型     | 描述                                       |
| ------- | ------ | ---------------------------------------- |
| code    | Int    | 错误码，0：成功， 其他值：失败，具体含义参见[错误码](/doc/api/456/6725)。 |
| message | String | 错误信息。                                    |
| data    | Object | 以RAID ID为key，对应的值为对象，对象为RAID信息的描述。具体结构描述如RAID结构所示。 |

RAID结构

| 参数名称               | 类型      | 描述                                   |
| ------------------ | ------- | ------------------------------------ |
| raidId             | Int     | RAID类型ID。                            |
| raid               | String  | RAID名称。                              |
| raidDisplay        | String  | RAID前台展示。                            |
| description        | String  | RAID描述。                              |
| systemDiskSize     | Int     | 系统盘大小。在购买机器和重装机器分区指定时，可以参考此值设定分区大小。 |
| dataDiskSize       | Int     | 数据盘大小。                               |
| sysIsUefiType      | Boolean | 标识是否是uefi启动。决定了分区中是否有/boot/efi分区。    |
| sysRootSpace       | Int     | 根分区默认大小。 用户调用无须关注。                   |
| sysSwaporuefiSpace | Int     | swap或/boot/efi分区默认大小。 用户调用无须关注。      |
| sysUsrlocalSpace   | Int     | /usr/local分区默认大小。 用户调用无须关注。          |
| sysDataSpace       | Int     | /data分区默认大小。 用户调用无须关注。               |

## 错误码
| 错误码  | 英文提示                  | 错误描述    |
| ---- | --------------------- | ------- |
| 9001 | InternalError.DbError | 操作数据库错误 |

## 实际案例

### 输入

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

### 输出

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
      "description": "2块盘组成RAID 1 + 10块盘组成RAID 10",
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

