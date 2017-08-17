## 1. 接口描述

本接口 (DescribeDeviceClassRaid) 获取设备类型对应的RAID方式。(这是老的接口，不推荐使用, 不支持自定义机型的RAID列表。 推荐使用新的接口[DescribeDeviceClassPartition](/document/api/386/7370)
接口请求域名：<font style="color:red">bm.api.qcloud.com</font>



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
<td> 公共错误码，0表示成功，其他值表示失败。详见错误码页面的<a href="/doc/api/456/6725" title="公共错误码">公共错误码</a>。
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



## 4. 模块错误码

| code |codeDesc| 描述 |
|------|------|------|
| 9001 |InternalError.DbError| 操作数据库错误 |



## 5. 示例
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
            }
        }
    }
}
```

