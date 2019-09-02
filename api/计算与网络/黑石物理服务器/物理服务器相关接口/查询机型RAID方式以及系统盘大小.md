>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述

DescribeDeviceClassPartition接口用来获取设备类型对应的 RAID 方式。

接口访问域名：bm.api.qcloud.com

## 请求

### 请求示例
```
https://bm.api.qcloud.com/v2/index.php?
    Action=DescribeDeviceClassPartition
    &<公共请求参数>
    &deviceClassCode=<设备类型>
    &instanceId=<自定义机型实例ID>
```

### 请求参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，其它参数参见 [公共请求参数](/doc/api/456/6718) 页面。其中，此接口的 Action 字段为 DescribeDeviceClassPartition。

|参数名称     |            必选     |            类型          |     描述  |
|-----|------|----|-----|
|deviceClassCode   | 否    |            String    |       设备类型。腾讯的设备类型 deviceClass，通过接口 [查询设备型号（DescribeDeviceClass）](https://cloud.tencent.com/document/api/386/6636) 获得设备类型。标准机型需要传入此参数。|  
|instanceId   |           否      |          String      |      需要查询自定义机型 RAID 信息时，传入自定义机型实例 ID。instanceId 存在时 deviceClassCode 失效。  |

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
响应参数部分包含两层结构，外层展示接口的响应结果，内层展示具体的接口内容，包括 RAID 等信息。

| 参数名称    | 类型     | 描述                                       |
| ------- | ------ | ---------------------------------------- |
| code    | Int    | 错误码，0：成功， 其他值：失败，具体含义参见 [错误码](/doc/api/456/6725)。 |
| message | String | 错误信息。                                    |
| data    | Object | 以 RAID ID 为 key，对应的值为对象，对象为 RAID 信息的描述。具体结构描述如 RAID 结构所示。 |

**RAID 结构**

| 参数名称               | 类型      | 描述                                   |
| ------------------ | ------- | ------------------------------------ |
| raidId             | Int     | RAID 类型 ID。                            |
| raid               | String  | RAID 名称。                              |
| raidDisplay        | String  | RAID 前台展示。                            |
| description        | String  | RAID 描述。                              |
| systemDiskSize     | Int     | 系统盘大小。在购买机器和重装机器分区指定时，可以参考此值设定分区大小。 |
| dataDiskSize       | Int     | 数据盘大小。                               |
| sysIsUefiType      | Boolean | 标识是否是 uefi 启动。决定了分区中是否有 /boot/efi 分区。    |
| sysRootSpace       | Int     | 根分区默认大小。 用户调用无须关注。                   |
| sysSwaporuefiSpace | Int     | swap 或 /boot/efi 分区默认大小。 用户调用无须关注。      |
| sysUsrlocalSpace   | Int     | /usr/local 分区默认大小。 用户调用无须关注。          |
| sysDataSpace       | Int     | /data 分区默认大小。 用户调用无须关注。               |

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

