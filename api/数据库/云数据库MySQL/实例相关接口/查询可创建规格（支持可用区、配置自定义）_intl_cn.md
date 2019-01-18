## 1. 接口描述
本接口(DescribeCdbProductListNew)用于查询可创建的云数据库主实例、只读实例和灾备实例规格，返回可创建实例的购买时长和单次购买数量限制，以及按可用区分类返回可创建实例的数据库版本号、内存大小和磁盘范围。当输入参数为空时，返回可创建的主实例规格信息；当传入cdbInstanceId且instanceRole为ro时，返回针对该主实例，可创建的只读实例规格信息；当传入cdbInstanceId且instanceRole为dr时，返回针对该主实例，可创建的灾备实例规格信息。
您还可以使用[查询价格（按量计费）](/doc/api/253/5176)接口查询可创建实例的价格，使用[创建实例（按量计费）](/doc/api/253/5175)接口创建一个新实例。
接口请求域名：cdb.api.qcloud.com 


## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见公共请求参数页面。其中，此接口的Action字段为DescribeCdbProductListNew。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| cdbInstanceId | 否 | String | 实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](/doc/api/253/1266) 接口获取，其值为输出参数中字段 uInstanceId 的值。 |
| instanceRole | 否 | String |实例类型，默认为 master，支持值包括：master-表示主实例，dr-表示灾备实例，ro-表示只读实例|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的公共错误码。|
| message | String | 模块错误信息描述，与接口相关。|
| codeDesc | String | 英文错误描述 |
| configs | Object | 可创建实例规格的配置信息 |
其中， configs 表示可创建实例规格的配置信息，其参数构成如下：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| timeSpan | Array | 当前用户、地域下可购买的时间 |
| minGoodsNumPerDeal | Int |  单次允许购买的最小数量
| maxGoodsNumPerDeal | Int | 单次允许购买的最大数量 |
| goodsDescription | Object | 可创建的实例规格信息 |
其中， goodsDescription 表示实例配置信息，其参数构成如下：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| 100002/100003/... | Object | 可用区ID |
其中， 100002为可用区ID， 其值表示该可用区下支持的实例信息，其参数构成如下：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| region | String | 区域ID，详见[公共请求参数](/doc/api/229/6976) |
| isSupportVpc | Bool | 是否支持私有网络，其值包括：true和false |
| types | Object | 支持的实例规格内容 |
其中， types 表示支持的实例规格内容，其参数构成如下：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| typeName | String | 实例类型中文名称，如：高IO版 |
| memory | String | 实例内存大小，每一个内存值对应一个可选的磁盘大小范围，单位：MB |
| volumeMax | Int | 选定内存后，实例硬盘大小可选的最大值，单位：GB |
| volumeMin | Int | 选定内存后，实例硬盘大小可选的最小值，单位：GB |
| volumeStep | Int | 选定内存后，实例硬盘大小的步长，单位：GB； 创建实例时，硬盘（volume）的取值是：volume= volumeMin + volumeStep * n;  同时 volumeMin <= volume <= volumeMax  |
| qps | Int | 选定内存后，支持的每秒访问次数，单位：次/秒 |
| mysqlversion | Array | 支持的MySQL版本，可能返回值：5.5和5.6 |


## 4. 错误码表
以下错误码表仅列出了该接口的业务逻辑错误码。

| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
| 9003 | InvalidParameter | 参数错误 |
| 9006 | InternalError | 数据库内部错误 |
| 9013 | InternalError | CDB错误 |
| 9649 | OperationDenied | 不允许创建灾备实例 |
| 9650 | OperationDenied | 不允许创建只读实例 |


## 5. 示例
输入
https://cdb.api.qcloud.com/v2/index.php?Action=DescribeCdbProductListNew
&<公共请求参数>


输出
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
                    {
                        "typeName":"高IO版",
                        "memory":"1000",
                        "volumeMax":"125",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"1000",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"高IO版",
                        "memory":"2000",
                        "volumeMax":"125",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"2400",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"高IO版",
                        "memory":"4000",
                        "volumeMax":"125",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"4400",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"高IO版",
                        "memory":"8000",
                        "volumeMax":"250",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"7200",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"高IO版",
                        "memory":"12000",
                        "volumeMax":"250",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"15000",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    }
                ]
            },
            "100003":{
                "region":"gz",
                "isSupportVpc":true,
                "types":[
                    {
                        "typeName":"高IO版",
                        "memory":"1000",
                        "volumeMax":"3000",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"1000",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"高IO版",
                        "memory":"2000",
                        "volumeMax":"3000",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"2400",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"高IO版",
                        "memory":"4000",
                        "volumeMax":"3000",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"4400",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"高IO版",
                        "memory":"8000",
                        "volumeMax":"3000",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"7200",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"高IO版",
                        "memory":"16000",
                        "volumeMax":"3000",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"18000",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"高IO版",
                        "memory":"32000",
                        "volumeMax":"3000",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"25000",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"高IO版",
                        "memory":"64000",
                        "volumeMax":"3000",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"37689",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"高IO版",
                        "memory":"96000",
                        "volumeMax":"3000",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"40919",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"高IO版",
                        "memory":"128000",
                        "volumeMax":"3000",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"61378",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"高IO版",
                        "memory":"244000",
                        "volumeMax":"3000",
                        "volumeMin":"25",
                        "volumeStep":"5",
                        "qps":"122755",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    },
                    {
                        "typeName":"高IO版",
                        "memory":"488000",
                        "volumeMax":"6000",
                        "volumeMin":"6000",
                        "volumeStep":"5",
                        "qps":"245509",
                        "mysqlversion":[
                            "5.5",
                            "5.6"
                        ]
                    }
                ]
            }
        }
    }
}
```
