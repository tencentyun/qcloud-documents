部分命令行返回结果会比较大，例如返回所有实例列表，而有的返回结果会比较大同时结构还比较复杂，这时候可能不是所有的信息都是您想获取的关键信息，此时可以使用基本命令中的 filter 来控制只保留关键信息。

下面以 DescribeAvailabilityZones 为例来说明如何使用过滤功能,配置里设置的是华南地区（广州），API 能力是查看地域下所有可用区。

## 示例
#### 1. 不加任何过滤时的输出

```
qcloudcli cvm DescribeAvailabilityZones

{
    "codeDesc": "Success",
    "totalCount": 4,
    "message": "",
    "code": 0,
    "zoneSet": [
        {
            "zoneId": 100001,
            "idcList": [
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                }
            ],
            "zoneName": "广州一区"
        },
        {
            "zoneId": 100002,
            "idcList": [
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                }
            ],
            "zoneName": "广州二区"
        },
        {
            "zoneId": 100003,
            "idcList": [
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                },
                {
                    "idcId": "",
                    "idcName": ""
                }
            ],
            "zoneName": "广州三区"
        },
        {
            "zoneId": 100004,
            "idcList": [
                {
                    "idcId": "",
                    "idcName": ""
                }
            ],
            "zoneName": "广州四区"
        }
    ]
}
```
#### 2. 只看某个字段

以查看 totalCount，当前地域可用区数量字段为例，

```
qcloudcli cvm DescribeAvailabilityZones --filter totalCount

4
```

在 --filter 后加上需要保留的字段名称，即可只看该字段的值。

#### 3. 指定某个数组类型对象的第N个子对象的信息

以查看可用区信息列表的第一个子对象为例，

```
qcloudcli cvm DescribeAvailabilityZones --filter zoneSet[0]

{
    "zoneId": 100001,
    "idcList": [
        {
            "idcId": "",
            "idcName": ""
        },
        {
            "idcId": "",
            "idcName": ""
        },
        {
            "idcId": "",
            "idcName": ""
        },
        {
            "idcId": "",
            "idcName": ""
        },
        {
            "idcId": "",
            "idcName": ""
        },
        {
            "idcId": "",
            "idcName": ""
        },
        {
            "idcId": "",
            "idcName": ""
        }
    ],
    "zoneName": "广州一区"
}

```
过滤后只展示广州一区的信息。

#### 4. 指定数组类型对象下所有某个名称的子对象的某个字段

查看所有可用区信息列表里 zoneName 字段值，

```
qcloudcli cvm DescribeAvailabilityZones --filter zoneSet[*].zoneName

[
    "广州一区",
    "广州二区",
    "广州三区",
    "广州四区"
]

```
过滤后只展示 zoneName 的信息。

#### 5. 过滤数组里的子对象，同时还以新的名称展示

这是目前支持最复杂的用法，这样可以方便您将结果重命名后用于代码或者其他对格式有要求的场合，建议将编辑好的命令行保存在本地，以便以后随时使用。

>!这里需要将说明过滤行为的内容用单引号包裹起来。

```
qcloudcli cvm DescribeAvailabilityZones --filter 'zoneSet[*].{name:zoneName, id:zoneId}'

[
    {
        "name": "广州一区",
        "id": 100001
    },
    {
        "name": "广州二区",
        "id": 100002
    },
    {
        "name": "广州三区",
        "id": 100003
    },
    {
        "name": "广州四区",
        "id": 100004
    }
]

```

将原来可用区列表数组里所有子对象的 zoneName 和 zoneId 字段过滤出来，然后以新名称 name 和 ID 展示出来。

