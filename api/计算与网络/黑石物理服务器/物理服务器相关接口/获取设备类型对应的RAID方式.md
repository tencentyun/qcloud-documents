## 1. 接口描述
域名:bm.api.qcloud.com
接口名:DescribeDeviceClassRaid

获取设备类型对应的RAID方式


## 2. 输入参数
无



## 3. 输出参数

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> code
<td> Int
<td> 公共错误码，0表示成功，其他值表示失败。详见错误码页面的<a href="https://www.qcloud.com/doc/api/244/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码">公共错误码</a>。
<tr>
<td> message
<td> String
<td> 模块错误信息描述，与接口相关。
<tr>
<td> data
<td> Object
<td> 各机型的raid json Object，具体数据结构可参见示例，结构如下表说明。
<tr>
<td> data.n1
<td> String
<td> n1,n2...为机型，如M10, B6，其value为raid描述。
<tr>
<td> data.n1.raidId
<td> String
<td> raid ID, 其value为raid信息，见下表描述。
</tbody></table>

</b></th>raid信息结构</b></th>
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> deviceClass
<td> String
<td> 机型，如M10, B6。
<tr>
<td> raidId
<td> String
<td> raidId。
<tr>
<td> diskSize
<td> String
<td> 硬盘大小。
<tr>
<td> partition
<td> Object
<td> 分区信息，单位为GB。
<tr>
<td> unFormatPartition
<td> String
<td> 未格式化分区，默认为没有。
<tr>
<tr>
<td> raid
<td> String
<td> raid级别。
<tr>
<tr>
<td> raidDisplay
<td> String
<td> raid级别显示名称。
<tr>
<tr>
<td> description
<td> String
<td> 描述。
<tr>
</tbody></table>



模块错误码

| code | 描述 |
|------|------|
| 9001 | 操作数据库错误 |
| 10001 | 参数错误|


## 4. 示例
输入
```
https://bm.api.qcloud.com/v2/index.php?Action=DescribeDeviceClassRaid&SecretId=AKID52SKw5uMEy3jhpMUBqSylEBJBby6E0KC&Nonce=48476&Timestamp=1476436689&Region=bj&Signature=afRlJQ0disdT97B7uIfVB4v2KWo%3D
```
输出
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "B6": {
            "1": {
                "deviceClass": "B6",
                "raidId": "1",
                "diskSize": "600G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 568
                },
                "unFormatPartition": "",
                "raid": "RAID0",
                "raidDisplay": "RAID 0",
                "description": "所有盘组成RAID 0，读取速度快，但没有冗余，适用于读取要求很高，数据安全要求低的应用"
            },
            "6": {
                "deviceClass": "B6",
                "raidId": "6",
                "diskSize": "600G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 568
                },
                "unFormatPartition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 268,
                    "unformat": 300
                },
                "raid": "NORAID",
                "raidDisplay": "NO RAID",
                "description": "不做RAID，数据会有丢失风险，谨慎选择"
            },
            "8": {
                "deviceClass": "B6",
                "raidId": "8",
                "diskSize": "300G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 268
                },
                "unFormatPartition": "",
                "raid": "RAID1",
                "raidDisplay": "RAID 1",
                "description": "提供数据块冗余"
            }
        },
        "M1": {
            "2": {
                "deviceClass": "M1",
                "raidId": "2",
                "diskSize": "1800G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 1768
                },
                "unFormatPartition": "",
                "raid": "RAID5",
                "raidDisplay": "RAID 5",
                "description": "所有盘组成RAID 5, 是兼顾存储性能、数据安全和存储成本的方案，适合读多写少的场景"
            }
        },
        "M10": {
            "1": {
                "deviceClass": "M10",
                "raidId": "1",
                "diskSize": "3600G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 3568
                },
                "unFormatPartition": "",
                "raid": "RAID0",
                "raidDisplay": "RAID 0",
                "description": "所有盘组成RAID 0，读取速度快，但没有冗余，适用于读取要求很高，数据安全要求低的应用"
            },
            "2": {
                "deviceClass": "M10",
                "raidId": "2",
                "diskSize": "3300G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 3268
                },
                "unFormatPartition": "",
                "raid": "RAID5",
                "raidDisplay": "RAID 5",
                "description": "所有盘组成RAID 5, 是兼顾存储性能、数据安全和存储成本的方案，适合读多写少的场景"
            },
            "3": {
                "deviceClass": "M10",
                "raidId": "3",
                "diskSize": "1800G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 1768
                },
                "unFormatPartition": "",
                "raid": "RAID1+0",
                "raidDisplay": "RAID 1+0",
                "description": "6*(2块盘组成RAID 1)， 这6个RAID 1组成RAID 0"
            },
            "4": {
                "deviceClass": "M10",
                "raidId": "4",
                "diskSize": "3000G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 2968
                },
                "unFormatPartition": "",
                "raid": "[6+6]RAID50",
                "raidDisplay": "RAID 50",
                "description": "6块盘组成RAID 5 + 6块盘组成RAID 5，这两个RAID 5再组成一个RAID 0"
            },
            "5": {
                "deviceClass": "M10",
                "raidId": "5",
                "diskSize": "2700G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 2668
                },
                "unFormatPartition": "",
                "raid": "2RAID1+[5+5]RAID50",
                "raidDisplay": "RAID 50+RAID 1",
                "description": "(5块盘组成RAID 5 + 5块盘组成RAID 5) 这两个RAID 5 再组成一个RAID 0, + 2块盘组成RAID 1"
            },
            "6": {
                "deviceClass": "M10",
                "raidId": "6",
                "diskSize": "3600G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 3568
                },
                "unFormatPartition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 268,
                    "unformat": 3300
                },
                "raid": "NORAID",
                "raidDisplay": "NO RAID",
                "description": "不做RAID，数据会有丢失风险，谨慎选择"
            },
            "7": {
                "deviceClass": "M10",
                "raidId": "7",
                "diskSize": "1800G",
                "partition": {
                    "/": 50,
                    "data": 250,
                    "data1": 1500
                },
                "unFormatPartition": "",
                "raid": "2RAID1+10RAID10",
                "raidDisplay": "RAID 1+RAID 10",
                "description": "2块盘组成RAID 1 + 10块盘组成RAID 10"
            },
            "11": {
                "deviceClass": "M10",
                "raidId": "11",
                "diskSize": "3300G",
                "partition": {
                    "/": 12,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 268,
                    "data1": 3000
                },
                "unFormatPartition": "",
                "raid": "2RAID1+10RAID0",
                "raidDisplay": "2RAID1 + 10RAID0",
                "description": "2块盘做RAID1，剩下的10块盘做RAID0"
            },
            "12": {
                "deviceClass": "M10",
                "raidId": "12",
                "diskSize": "3000G",
                "partition": null,
                "unFormatPartition": "",
                "raid": "4RAID10+8RAID5",
                "raidDisplay": "4RAID10 + 8RAID5",
                "description": "4块盘做RAID10，8块盘做RAID5"
            },
            "13": {
                "deviceClass": "M10",
                "raidId": "13",
                "diskSize": "1800G",
                "partition": null,
                "unFormatPartition": "",
                "raid": "2RAID1+2RAID1+8RAID10",
                "raidDisplay": "2RAID1 + 2RAID1 + 8RAID10",
                "description": "2块盘做RAID1，2块盘做RAID1，8块盘做RAID10"
            },
            "14": {
                "deviceClass": "M10",
                "raidId": "14",
                "diskSize": "1800G",
                "partition": null,
                "unFormatPartition": "",
                "raid": "4RAID10+8RAID10",
                "raidDisplay": "4RAID10 + 8RAID10",
                "description": "4快盘做RAID10，剩余8块盘做RAID10"
            },
            "15": {
                "deviceClass": "M10",
                "raidId": "15",
                "diskSize": "1800G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 568,
                    "data1": 600,
                    "data2": 300,
                    "data3": 300
                },
                "unFormatPartition": "",
                "raid": "4RAID10+4RAID10+2RAID1+2RAID1",
                "raidDisplay": "4RAID10+4RAID10+2RAID1+2RAID1",
                "description": "4块盘做RAID10，4块盘做RAID10，2块盘做RAID1，2块盘做RAID1"
            }
        },
        "M10a": {
            "1": {
                "deviceClass": "M10a",
                "raidId": "1",
                "diskSize": "3600G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 3568
                },
                "unFormatPartition": "",
                "raid": "RAID0",
                "raidDisplay": "RAID 0",
                "description": "所有盘组成RAID 0，读取速度快，但没有冗余，适用于读取要求很高，数据安全要求低的应用"
            },
            "2": {
                "deviceClass": "M10a",
                "raidId": "2",
                "diskSize": "3300G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 3268
                },
                "unFormatPartition": "",
                "raid": "RAID5",
                "raidDisplay": "RAID 5",
                "description": "所有盘组成RAID 5, 是兼顾存储性能、数据安全和存储成本的方案，适合读多写少的场景"
            },
            "3": {
                "deviceClass": "M10a",
                "raidId": "3",
                "diskSize": "1800G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 1768
                },
                "unFormatPartition": "",
                "raid": "RAID1+0",
                "raidDisplay": "RAID 1+0",
                "description": "6*(2块盘组成RAID 1)， 这6个RAID 1组成RAID 0"
            },
            "4": {
                "deviceClass": "M10a",
                "raidId": "4",
                "diskSize": "3000G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 2968
                },
                "unFormatPartition": "",
                "raid": "[6+6]RAID50",
                "raidDisplay": "RAID 50",
                "description": "6块盘组成RAID 5 + 6块盘组成RAID 5，这两个RAID 5再组成一个RAID 0"
            },
            "6": {
                "deviceClass": "M10a",
                "raidId": "6",
                "diskSize": "3600G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 3568
                },
                "unFormatPartition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 268,
                    "unformat": 3300
                },
                "raid": "NORAID",
                "raidDisplay": "NO RAID",
                "description": "不做RAID，数据会有丢失风险，谨慎选择"
            }
        },
        "M2": {
            "1": {
                "deviceClass": "M2",
                "raidId": "1",
                "diskSize": "1800GB",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 2668
                },
                "unFormatPartition": "",
                "raid": "RAID0",
                "raidDisplay": "RAID 0",
                "description": "所有盘组成RAID 0，读取速度快，但没有冗余，适用于读取要求很高，数据安全要求低的应用"
            },
            "2": {
                "deviceClass": "M2",
                "raidId": "2",
                "diskSize": "1800GB",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 2668
                },
                "unFormatPartition": "",
                "raid": "RAID5",
                "raidDisplay": "RAID 5",
                "description": "所有盘组成RAID 5, 是兼顾存储性能、数据安全和存储成本的方案，适合读多写少的场景"
            },
            "3": {
                "deviceClass": "M2",
                "raidId": "3",
                "diskSize": "1800GB",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 2668
                },
                "unFormatPartition": "",
                "raid": "RAID1+0",
                "raidDisplay": "RAID 1+0",
                "description": "6*(2块盘组成RAID 1)， 这6个RAID 1组成RAID 0"
            }
        },
        "TS5": {
            "6": {
                "deviceClass": "TS5",
                "raidId": "6",
                "diskSize": "",
                "partition": null,
                "unFormatPartition": "",
                "raid": "NORAID",
                "raidDisplay": "NO RAID",
                "description": "不做RAID，数据会有丢失风险，谨慎选择"
            }
        },
        "TS60": {
            "6": {
                "deviceClass": "TS60",
                "raidId": "6",
                "diskSize": "24T",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 23968
                },
                "unFormatPartition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 1968,
                    "unformat": 22000
                },
                "raid": "NORAID",
                "raidDisplay": "NO RAID",
                "description": "不做RAID，数据会有丢失风险，谨慎选择"
            }
        },
        "TS80": {
            "6": {
                "deviceClass": "TS80",
                "raidId": "6",
                "diskSize": "7200G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 7168
                },
                "unFormatPartition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 1768,
                    "unformat": 5400
                },
                "raid": "NORAID",
                "raidDisplay": "NO RAID",
                "description": "不做RAID，数据会有丢失风险，谨慎选择"
            }
        },
        "TS80a": {
            "6": {
                "deviceClass": "TS80a",
                "raidId": "6",
                "diskSize": "7440",
                "partition": null,
                "unFormatPartition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 208,
                    "unformat": 7200
                },
                "raid": "NORAID",
                "raidDisplay": "NO RAID",
                "description": "不做RAID，数据会有丢失风险，谨慎选择"
            }
        },
        "TS90": {
            "3": {
                "deviceClass": "TS90",
                "raidId": "3",
                "diskSize": "4800G",
                "partition": null,
                "unFormatPartition": "",
                "raid": "RAID1+0",
                "raidDisplay": "RAID 1+0",
                "description": "6*(2块盘组成RAID 1)， 这6个RAID 1组成RAID 0"
            },
            "4": {
                "deviceClass": "TS90",
                "raidId": "4",
                "diskSize": "8000G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 7968
                },
                "unFormatPartition": "",
                "raid": "[6+6]RAID50",
                "raidDisplay": "RAID 50",
                "description": "6块盘组成RAID 5 + 6块盘组成RAID 5，这两个RAID 5再组成一个RAID 0"
            }
        },
        "Y0-TS85-00": {
            "2": {
                "deviceClass": "Y0-TS85-00",
                "raidId": "2",
                "diskSize": "12T",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 11968
                },
                "unFormatPartition": "",
                "raid": "RAID5",
                "raidDisplay": "RAID 5",
                "description": "所有盘组成RAID 5, 是兼顾存储性能、数据安全和存储成本的方案，适合读多写少的场景"
            },
            "3": {
                "deviceClass": "Y0-TS85-00",
                "raidId": "3",
                "diskSize": "7200G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 7168
                },
                "unFormatPartition": "",
                "raid": "RAID1+0",
                "raidDisplay": "RAID 1+0",
                "description": "6*(2块盘组成RAID 1)， 这6个RAID 1组成RAID 0"
            }
        },
        "Y1-B60-00": {
            "1": {
                "deviceClass": "Y1-B60-00",
                "raidId": "1",
                "diskSize": "600G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 568
                },
                "unFormatPartition": "",
                "raid": "RAID0",
                "raidDisplay": "RAID 0",
                "description": "所有盘组成RAID 0，读取速度快，但没有冗余，适用于读取要求很高，数据安全要求低的应用"
            },
            "6": {
                "deviceClass": "Y1-B60-00",
                "raidId": "6",
                "diskSize": "600G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 568
                },
                "unFormatPartition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 268,
                    "unformat": 300
                },
                "raid": "NORAID",
                "raidDisplay": "NO RAID",
                "description": "不做RAID，数据会有丢失风险，谨慎选择"
            },
            "8": {
                "deviceClass": "Y1-B60-00",
                "raidId": "8",
                "diskSize": "300G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 268
                },
                "unFormatPartition": "",
                "raid": "RAID1",
                "raidDisplay": "RAID 1",
                "description": "提供数据块冗余"
            }
        },
        "Y1-B60-11": {
            "3": {
                "deviceClass": "Y1-B60-11",
                "raidId": "3",
                "diskSize": "600G",
                "partition": {
                    "/": 10,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 568
                },
                "unFormatPartition": "",
                "raid": "RAID1+0",
                "raidDisplay": "RAID 1+0",
                "description": "6*(2块盘组成RAID 1)， 这6个RAID 1组成RAID 0"
            }
        },
        "Y1-TS30-00": {
            "10": {
                "deviceClass": "Y1-TS30-00",
                "raidId": "10",
                "diskSize": "45056G",
                "partition": {
                    "/": 12,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 45022
                },
                "unFormatPartition": {
                    "/": 12,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 4062,
                    "unformat": 40960
                },
                "raid": "2RAID1+10NORAID",
                "raidDisplay": "2RAID1 + 10NORAID",
                "description": "2块盘做RAID1，剩下的10块盘不做RAID"
            }
        },
        "Y1-TS30-11": {
            "3": {
                "deviceClass": "Y1-TS30-11",
                "raidId": "3",
                "diskSize": "8192G",
                "partition": {
                    "/": 12,
                    "swap": 2,
                    "/usr/local": 20,
                    "data": 8158
                },
                "unFormatPartition": "",
                "raid": "RAID1+0",
                "raidDisplay": "RAID 1+0",
                "description": "6*(2块盘组成RAID 1)， 这6个RAID 1组成RAID 0"
            }
        },
        "Z3": {
            "1": {
                "deviceClass": "Z3",
                "raidId": "1",
                "diskSize": "",
                "partition": null,
                "unFormatPartition": "",
                "raid": "RAID0",
                "raidDisplay": "RAID 0",
                "description": "所有盘组成RAID 0，读取速度快，但没有冗余，适用于读取要求很高，数据安全要求低的应用"
            },
            "2": {
                "deviceClass": "Z3",
                "raidId": "2",
                "diskSize": "",
                "partition": null,
                "unFormatPartition": "",
                "raid": "RAID5",
                "raidDisplay": "RAID 5",
                "description": "所有盘组成RAID 5, 是兼顾存储性能、数据安全和存储成本的方案，适合读多写少的场景"
            },
            "3": {
                "deviceClass": "Z3",
                "raidId": "3",
                "diskSize": "",
                "partition": null,
                "unFormatPartition": "",
                "raid": "RAID1+0",
                "raidDisplay": "RAID 1+0",
                "description": "6*(2块盘组成RAID 1)， 这6个RAID 1组成RAID 0"
            }
        }
    }
}
```

