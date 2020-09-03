为了帮助您快速使用云数据库MySQL API，这里给出一个使用示例。
要使用云数据库MySQL服务，您首先需要查询可创建的实例规格，其定义了可创建实例的规格和限制条件，然后创建所需规格的实例；最后，初始化新创建的实例。下面将为您展示使用流程：
首先，请使用[查询可创建规格（支持可用区、配置自定义）](/doc/api/253/6109)接口来查看各个地域支持创建的实例规格；然后，可使用[创建实例（按时计费）](/doc/api/253/5175)接口来创建实例；最后，使用[初始化实例](/doc/api/253/5335)接口来初始化实例，初试化实例成功后，实例就可以投入使用了。


## 1. 查询可创建规格（支持可用区、配置自定义）
创建云数据库实例前，我们首先要查看所选地域下支持哪些可创建的实例规格，这个接口只需传公共请求参数。

结合公共请求参数和接口请求参数，最终得到的请求形式如下：

```
https://cdb.api.qcloud.com/v2/index.php?Action=DescribeCdbProductListNew
&SecretId=AKIDTqlxxxxxxxiiRO
&Signature=G%2BepdQfDSklf2eMgrjQR5FdK7MY%3D
&Nonce=12276
&Timestamp=1467277235
&Region=gz
```

接口将返回可购买的实例时长，单次购买的数量限制，该地域下各个分区的规格信息，其中包括是否支持私有网络、内存大小、磁盘范围、数据库引擎版本以及每秒访问次数（QPS），上述请求的返回结果形式如下：

```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "configs":{
        "timeSpan":[
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "12",
            "24",
            "36"
        ],
        "minGoodsNumPerDeal":"1",
        "maxGoodsNumPerDeal":"10",
        "goodsDescription":{
            "100002":{
                "region":"gz",
                "isSupportVpc":true,
                "types":[
                    {
                        "typeName":"高IO版",
                        "memory":"360",
                        "volumeMax":"50",
                        "volumeMin":"10",
                        "volumeStep":"5",
                        "qps":"120",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    //省略部分内容，请按实际返回内容为准...
                ]
            },
            //省略部分内容，请按实际返回内容为准...
        }
    }
}
```

## 2. 创建实例
获取到可创建的实例规格后，您现在可使用[创建实例（按时计费）](/doc/api/253/5175)接口来创建实例。
以下示例选择自定义规格， 将cdbType设置为CUSTOM，内存大小选择 1000MB，硬盘大小选择 25GB。MySQL版本选择 5.6， 时长选择 1 个月，实例数量为 1 个。具体的接口请求参数见下表：

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| cdbType | 是 | String | 实例规格，支持固定规格和自定义规格。传 CUSTOM 代表自定义规格； 固定规格的取值，请使用[查询可创建规格](/doc/api/253/1333)接口获取。 固定规格类型将会下线，推荐使用自定义规格。 |
| engineVersion | 是 | String | MySQL版本，值包括：5.5和5.6，请使用[查询可创建规格（支持可用区、配置自定义）](/doc/api/253/6109)接口获取可创建的实例版本 |
| period | 是 | Int | 实例时长，最小值1，最大值为36，请使用[查询可创建规格（支持可用区、配置自定义）](/doc/api/253/6109)接口获取可创建的实例时长，该接口返回字段timeSpan表示时长可选值 |
| goodsNum | 是 | Int | 实例数量，默认值为1, 最小值1，最大值为10，请使用[查询可创建规格（支持可用区、配置自定义）](/doc/api/253/6109)接口获取可创建的实例数量 |
| vpcId | 否 | String | 私有网络ID，如果不传则默认选择基础网络，请使用[查询私有网络列表](/doc/api/245/1372) |
| subnetId | 否 | String | 私有网络下的子网ID，如果设置了 vpcId，则 subnetId 必填，请使用[查询子网列表](/doc/api/245/1371) |
| projectId | 否 | Int | 项目ID，不填为默认项目。请使用[查询项目列表](/document/product/378/4400)接口获取项目ID |
| memory | 否 | Int | 实例内存大小，单位：MB，当 cdbType 值为 CUSTOM 时， memory 为必填；当 cdbType 为整型值时，传入 memory 值将无效，请使用[查询可创建规格（支持可用区、配置自定义）](/doc/api/253/6109)接口获取可创建的内存规格 |
| volume | 否 | Int | 实例硬盘大小，单位：GB，当 cdbType 值为 CUSTOM 时， volume 为必填；当 cdbType 为整型值时，传入 volume 值将无效，请使用[查询可创建规格（支持可用区、配置自定义）](/doc/api/253/6109)接口获取可创建的硬盘范围 |
| zoneId | 否 | Int | 可用区ID，该参数缺省时，系统会自动选择一个可用区，请使用[查询可创建规格（支持可用区、配置自定义）](/doc/api/253/6109)接口获取可创建的可用区 |

结合公共请求参数和接口请求参数，最终得到的请求形式如下：

```
https://cdb.api.qcloud.com/v2/index.php?Action=CreateCdb
&SecretId=AKIDTqlxxxxxxxiiRO
&Signature=G%2BepdQfDSklf2eMgrjQR5FdK7MY%3D
&Nonce=25476
&Timestamp=1467277631
&Region=bj
&cdbType=CUSTOM
&memory=1000
&volume=25
&engineVersion=5.6
&period=1
&goodsNum=1

```

创建实例接口结果返回了短订单ID（dealIds）、长订单ID（dealNames）和实例ID，其中短订单ID（dealIds）用于调用云API，长订单号（dealNames）用于反馈订单问题给官方客服，实例ID用于管理云数据库实例。您可使用[查询实例列表](/doc/api/253/1266)接口查看刚创建的实例。
上述请求的结果如下：

```
{
    "code": 0,
    "message": "",
    "dealIds": [
        "2196009"
    ]，
    "data": {
        "dealNames": [
            "20161024110051"
        ],
        "dealIds": [
            "457605"
        ],
        "cdbInstanceIds": {
            "20161024110051": [
                "cdb-259sstXX"
            ]
        }
    }
}
```


## 3. 初始化实例
创建实例成功后，您还需要初始化该实例。初始化操作成功后，就可以投入使用了。初始化实例时可设置实例的字符集、端口、表名大小写是否敏感和 root 帐号的密码。具体的接口请求参数见下表：

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| cdbInstanceId | 是 | String | 实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](/doc/api/253/1266) 接口获取，其值为输出参数中字段 uInstanceId 的值。 |
| charset | 是 | String | 字符集，支持字符集： latin1、utf8、gbk和utf8mb4 |
| port | 是 | Int | 自定义端口，端口支持范围：[ 1024-65535 ] |
| lowerCaseTableNames | 是 | Int | 表名是否只存储为小写，可能返回值：1-表名存储为小写； 0-表名大小写敏感 |
| password | 是 | String | 设置root帐号密码，密码规则：8-16个字符，至少包含字母、数字、字符（支持的字符：!@#$%^*()）中的两种 |

结合公共请求参数和接口请求参数，最终得到的请求形式如下：

```
https://cdb.api.qcloud.com/v2/index.php?Action=CdbMysqlInit
&SecretId=AKIDTqlxxxxxxxiiRO
&Signature=G%2BepdQfDSklf2eMgrjQR5FdK7MY%3D
&Nonce=25476
&Timestamp=1467277631
&Region=bj
&cdbInstanceId=cdb-c1nl9rpv
&charset=utf8
&port=3306
&password=cloud123456
&lowerCaseTableNames=0
```

初始化实例是一个异步处理过程，提交初始化任务成功后，结果将返回一个任务ID。您可使用[查询初始化任务详情](/doc/api/253/5334)接口查询初始化任务的进度。上述请求的结果如下：

```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "jobId":"11"
}
```