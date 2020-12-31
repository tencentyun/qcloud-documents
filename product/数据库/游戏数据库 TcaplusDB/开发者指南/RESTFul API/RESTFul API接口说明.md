本文档为 Tcaplus RESTful API v1.0 用户手册。

## 概述
Tcaplus RESTful API 为开发者提供了一种通过 HTTP 请求与 Tcaplus 数据库远程交互的方式。当您通过 RESTful API 用 Json 携带数据发送 HTTP 请求后，您会收到对应的 Json 格式的响应包。开发者可以通过任何语言或工具发送 RESTful API 请求对数据进行增、删、改、查操作。

## 准备工作
已在 [TcaplusDB 控制台](https://console.cloud.tencent.com/tcaplusdb/app) 创建集群，并且获取对应的集群信息，包括 AppId（集群接入 ID），ZoneId（表格组 ID），AppKey（集群访问密码）。当前 Tcaplus RESTful API 只支持通过 protobuf 定义的表。

## 当前版本
当前，所有 Tcaplus RESTful API 的请求默认都使用 ver1.0 版本。

## 请求
所有的 API 访问请求都是通过 HTTP，所有的数据都通过 JSON 格式传递。以下是典型的请求访问 URI 格式：
```
http://{Tcaplus_REST_URL}/{Version}/apps/{AppId}/zones/{ZoneId}/tables/{TableName}/records
```
* Tcaplus_REST_URL：Tcaplus RESTful URL 接入点
* Version：Tcaplus RESTful API 版本号，默认 ver1.0
* AppId：集群的接入 ID
* ZoneId：表格组 ID 
* TableName：表名

示例：
```
http://10.123.9.70/ver1.0/apps/2/zones/1/tables/tb_rest_test/records
```

### HTTP 头
通过设置 HTTP 头可以允许用户 HTTP 客户端通过请求和回包传递一些额外的信息。

#### 鉴权
`x-tcaplus-pwd-md5`
此字段填写用户 app key 的 MD5 计算结果用于客户端权限验证。
请通过以下 bash 命令计算字符串的 MD5 值：
```
# echo -n "c3eda5f013f92c81dda7afcdc273cf82" | md5sum
879423b88d153cace7b31773a7f46039  -
```

#### 操作校验 
- `x-tcaplus-target`指定 Tcaplus RESTful API 请求操作，具体包含以下操作类型：
 * Tcaplus.GetRecord 获取记录
 * Tcaplus.AddRecord 插入记录
 * Tcaplus.SetRecord 设置记录
 * Tcaplus.DeleteRecord 删除记录
 * Tcaplus.FieldGetRecord 部分字段读
 * Tcaplus.FieldSetRecord 部分字段设置
 * Tcaplus.FieldIncRecord 部分字段自增
 * Tcaplus.PartkeyGetRecord 索引批量读
- `x-tcaplus-idl-type` 指定 Tcaplus 表类型，目前只支持 protobuf（pb）类型。


####  设置标记 
- `x-tcaplus-data-version-check` Specifies Tcaplus data version check policy use with `x-tcaplus-data-version`. It can be set as:
指定 Tcaplus 数据版本号校验策略，实现乐观锁功能，与`x-tcaplus-data-version`标记配合使用，可选值如下：
 - `1`：当设置为1，客户端的数据版本号必须与存储层数据版本号一致才能写操作，操作会令数据版本号+1。
 - `2`：当设置为2，就不检测客户端版本号与服务端版本号之间的关系，强制将客户端传入的版本号设置到存储层。
 - `3`：当设置为3，就不检测客户端版本号与服务端版本号之间的关系，写操作会将存储层数据版本号+1。
 此标记仅对 Tcaplus.AddRecord 和 Tcaplus.SetRecord 有意义。
 
- `x-tcaplus-data-version` 与 `x-tcaplus-data-version-check` 标记相配合，设置客户端的数据版本号。可选值如下：
 - version <= 0：忽略版本检查策略。
 - version > 0：指定客户端数据记录版本号。

- `x-tcaplus-result-flag` 设置应答中是否包含完整数据的策略，可能的取值有：
 - `0` ：设置为0，应答中仅包含请求成功或失败。
 - `1` ：设置为1，应答中包含与请求一致的值。
 - `2` ：设置为2，应答中包含被修改的数据的所有字段最新值。
 - `3` ：设置为3，应答中包含记录被修改前的值。


### 请求 JSON 数据 
```
Request Data:
{
 "ReturnValues": "...", // 用户设置的保留数据，随请求到达 tcaplus 并由应答原样带回
 "Record": {
     ... // 数据记录，详细格式请参见“API 简明示例”一节
 }
}
```

## 应答
### 应答中的 JSON 数据
GetRecord，SetRecord，AddRecord，DeleteRecord，FieldGetRecord，FieldSetRecord 和 FieldIncRecord 操作的结果将会返回单条数据，应答 JSON 数据格式如下：
```
Response Data
{
 "ErrorCode": 0, // 返回码
 "ErrorMsg": "Succeed", // 返回信息
 "RecordVersion": 1, // 数据版本号
 "ReturnValues": "...", // 用户设置的保留数据，随请求到达 tcaplus 并由应答原样带回
 "Record": { // 数据记录，详细格式请参见“API简明示例”一节
     ...
 }
}
```

PartkeyGetRecord 操作的结果有可能带回多条数据，应答的 JSON 数据格式如下：
```
Response Data
{
 "ErrorCode": 0, // 返回码
 "ErrorMsg": "Succeed", // 返回信息
 "MultiRecords": [ //多条数据构成的数组
  {"RecordVersion": 1,  //每条数据的版本号
   "Record": {...}  // 数据记录，详细格式请参见“API简明示例”一节
  },
  ...
  ],
 "RemainNum": 0, //还未访问到的数据条数
 "TotalNum": 5   //满足条件的总数据条数
}
```

###  返回码 

| HTTP 状态码 | 返回码 | 返回信息                                                    |
| ----------- | ------ | ----------------------------------------------------------- |
| 200         | 0      | 成功                                                        |
| 400         | -2579  | 数据反序列化错误                                            |
| 401         | -279   | 鉴权错误                                                    |
| 400         | -11539 | 非法请求 <br>详细原因请参考返回信息字段                     |
| 400         | -2067  | 操作类型不匹配                                              |
| 400         | -1811  | 非法参数                                                    |
| 400         | -5395  | 没有设置主键字段                                            |
| 400         | -2323  | 数据序列化错误                                              |
| 400         | -7949  | 非法数据版本号 <br>一般发生在写操作，应用数据版本检查策略时 |
| 400         | -1293  | 记录已经存在                                                |
| 404         | 261    | 记录不存在                                                  |
| 404         | -34565 | 索引不存在                                                  |
| 500         | -      | 系统内部错误<br>请参考返回信息字段                          |

## API 简明示例 
###   Tcaplus.GetRecord 
```
GET /ver1.0/apps/{APP_ID}/zones/{ZONE_ID}/tables/{TABLE_NAME}/records?keys={JSONKeysObj}&select={JSONSelectObj}
```
从一个 Tcaplus pb 表中通过指定一条记录的 key 信息查询此记录。这个操作将会把整条记录取出，但您可以设置 select 变量，select 变量可指定您需要在应答中返回的字段，如果 select 变量不指定，将会显示所有字段信息。如果数据记录不存在，将会返回错误。

必须在 URI 中指定`keys`变量，而 select 变量则是可选项。keys 指所有主键的值，select 指需要显示的 value 字段的名称，并且您可以通过点分路径的方式指定嵌套结构中的字段，例如 “pay.total_money”。

>!请求的变量必须通过 UrlEncode 编码，请将url中的空格编码为"%20"而不是"+"。

| 名称               | 类型   | 取值                    |
| ------------------ | ------ | ----------------------- |
| x-tcaplus-target   | String | Tcaplus.GetRecord       |
| x-tcaplus-version  | String | Tcaplus3.32.0           |
| x-tcaplus-pwd-md5  | String | MD5 of AppKey(Password) |
| x-tcaplus-idl-type | String | protobuf                |


#### 示例
##### URL
- URL 未 UrlEncode 结果：
```
http://10.123.9.70:31002/ver1.0/apps/2/zones/1/tables/tb_example/records?keys={"region": 101, "name": "calvinshao", "uin": 100}
```
- URL UrlEncode 结果：
```
http://10.123.9.70:31002/ver1.0/apps/2/zones/1/tables/tb_example/records?keys=%7B%22region%22%3A%20101%2C%20%22name%22%3A%20%22calvinshao%22%2C%20%22uin%22%3A%20100%7D
```

##### 请求 HTTP 头
```
[
 "x-tcaplus-target:Tcaplus.GetRecord",
 "x-tcaplus-version:Tcaplus3.32.0",
 "x-tcaplus-pwd-md5:c3eda5f013f92c81dda7afcdc273cf82",
 "x-tcaplus-idl-type:protobuf"
]
```

##### 应答数据
```
{
 "ErrorCode": 0,
 "ErrorMsg": "Succeed",
 "RecordVersion": 1,
 "Record": {
  "name": "calvinshao",
  "lockid": [
   50,
   60,
   70
  ],
  "pay": {
   "pay_times": 2,
   "total_money": 10000,
   "pay_id": 5,
   "auth": {
    "pay_keys": "adqwacsasafasda",
    "update_time": 1528018372
   }
  },
  "region": 101,
  "uin": 100,
  "is_available": true,
  "gamesvrid": 4099,
  "logintime": 404
 }
}
```

### Tcaplus.SetRecord 
```
PUT /ver1.0/apps/{APP_ID}/zones/{ZONE_ID}/tables/{TABLE_NAME}/records
```

通过指定一条记录的 key 信息设置此记录。如果记录存在执行覆盖操作，否则，执行插入操作。
SetRecord操作支持resultflag设置以下取值：
* `0` 设置为0，应答中仅包含请求成功或失败。
* `1` 设置为1，应答中包含与请求一致的值。
* `2` 设置为2，应答中包含被修改的数据的所有字段最新值。
* `3` 设置为3，应答中包含记录被修改前的值。

| 名称                         | 类型   | 取值                    |
| ---------------------------- | ------ | ----------------------- |
| x-tcaplus-target             | String | Tcaplus.SetRecord       |
| x-tcaplus-version            | String | Tcaplus3.32.0           |
| x-tcaplus-pwd-md5            | String | MD5 of AppKey(Password) |
| x-tcaplus-result-flag        | Int    | 2                       |
| x-tcaplus-data-version-check | Int    | 2                       |
| x-tcaplus-data-version       | Int    | -1                      |
| x-tcaplus-idl-type           | String | protobuf                |


#### 示例
##### URL
```
http://10.123.9.70/ver1.0/apps/2/zones/1/tables/tb_example/records
```

##### 请求 HTTP 头
```
[
 "x-tcaplus-target:Tcaplus.SetRecord",
 "x-tcaplus-version:Tcaplus3.32.0",
 "x-tcaplus-pwd-md5:c3eda5f013f92c81dda7afcdc273cf82",
 "x-tcaplus-result-flag:2",
 "x-tcaplus-data-version-check:2",
 "x-tcaplus-data-version:-1",
 "x-tcaplus-idl-type:Protobuf"
]
```

##### 请求 JSON 数据
```
{
 "ReturnValues": "Send to tcaplus by calvinshao",
 "Record": {
  "name": "calvinshao",
  "lockid": [
   50,
   60,
   70,
   80,
   90,
   100
  ],
  "pay": {
   "pay_times": 3,
   "total_money": 12000,
   "pay_id": 5,
   "auth": {
    "pay_keys": "adqwacsasafasda",
    "update_time": 1528018372
   }
  },
  "region": 101,
  "uin": 100,
  "is_available": false,
  "gamesvrid": 4099,
  "logintime": 404
 }
}
```

##### 应答 JSON 数据
```
{
 "ErrorCode": 0,
 "ErrorMsg": "Succeed",
 "RecordVersion": 1,
 "ReturnValues": "Send to tcaplus by calvinshao",
 "Record": {
  "name": "calvinshao",
  "lockid": [
   50,
   60,
   70,
   80,
   90,
   100
  ],
  "pay": {
   "pay_times": 3,
   "total_money": 12000,
   "pay_id": 5,
   "auth": {
    "pay_keys": "adqwacsasafasda",
    "update_time": 1528018372
   }
  },
  "region": 101,
  "uin": 100,
  "is_available": false,
  "gamesvrid": 4099,
  "logintime": 404
 }
}
```

###  Tcaplus.AddRecord 
```
POST /ver1.0/apps/{APP_ID}/zones/{ZONE_ID}/tables/{TABLE_NAME}/records
```

通过指定一条记录的 key 信息插入一条记录。如果记录存在返回错误。
AddRecord 操作支持 resultflag 设置以下取值：
* `0` 设置为0，应答中仅包含请求成功或失败。
* `1` 设置为1，应答中包含与请求一致的值。
* `2` 设置为2，应答中包含被修改的数据的所有字段最新值。
* `3` 设置为3，应答中包含记录被修改前的值。

| 名称                  | 类型   | 取值                    |
| --------------------- | ------ | ----------------------- |
| x-tcaplus-target      | String | Tcaplus.SetRecord       |
| x-tcaplus-version     | String | Tcaplus3.32.0           |
| x-tcaplus-pwd-md5     | String | MD5 of AppKey(Password) |
| x-tcaplus-result-flag | Int    | 1                       |
| x-tcaplus-idl-type    | String | protobuf                |


#### 示例
##### URL
```
 http://10.123.9.70/ver1.0/apps/2/zones/1/tables/tb_example/records
```

##### 请求 HTTP 头
```
[
 "x-tcaplus-target:Tcaplus.AddRecord",
 "x-tcaplus-version:Tcaplus3.32.0",
 "x-tcaplus-pwd-md5:c3eda5f013f92c81dda7afcdc273cf82",
 "x-tcaplus-result-flag:1",
 "x-tcaplus-idl-type:protobuf"
]
```

##### 请求 JSON 数据
```
{
 "ReturnValues": "Send to tcaplus by calvinshao",
 "Record": {
  "name": "calvinshao",
  "lockid": [
   50,
   60,
   70
  ],
  "pay": {
   "pay_times": 2,
   "total_money": 10000,
   "pay_id": 5,
   "auth": {
    "pay_keys": "adqwacsasafasda",
    "update_time": 1528018372
   }
  },
  "region": 101,
  "uin": 100,
  "is_available": true,
  "gamesvrid": 4099,
  "logintime": 404
 }
}
```

##### 应答 JSON 数据
```
{
 "ErrorCode": 0,
 "ErrorMsg": "Succeed",
 "RecordVersion": 1,
 "ReturnValues": "Send to tcaplus by calvinshao",
 "Record": {
  "name": "calvinshao",
  "lockid": [
   50,
   60,
   70
  ],
  "pay": {
   "pay_times": 2,
   "total_money": 10000,
   "pay_id": 5,
   "auth": {
    "pay_keys": "adqwacsasafasda",
    "update_time": 1528018372
   }
  },
  "region": 101,
  "uin": 100,
  "is_available": true,
  "gamesvrid": 4099,
  "logintime": 404
 }
}
```



###  Tcaplus.DeleteRecord 
```
DELETE /ver1.0/apps/{APP_ID}/zones/{ZONE_ID}/tables/{TABLE_NAME}/records
```

通过指定一条记录的 key 信息删除此记录，如果数据不存在则返回错误。
DeleteRecord 操作支持 resultflag 设置以下取值：
* `0` 设置为0，应答中仅包含请求成功或失败。
* `1` 设置为1，应答中包含与请求一致的值。
* `2` 设置为2，应答中包含被修改的数据的所有字段最新值。
* `3` 设置为3，应答中包含记录被修改前的值。

| 名称                  | 类型   | 取值                    |
| --------------------- | ------ | ----------------------- |
| x-tcaplus-target      | String | Tcaplus.SetRecord       |
| x-tcaplus-version     | String | Tcaplus3.32.0           |
| x-tcaplus-pwd-md5     | String | MD5 of AppKey(Password) |
| x-tcaplus-result-flag | Int    | 1                       |
| x-tcaplus-idl-type    | String | protobuf                |


#### 示例
##### URI
```
http://10.123.9.70/ver1.0/apps/2/zones/1/tables/tb_example/records
```

##### 请求 HTTP 头
```
[
 "x-tcaplus-target:Tcaplus.DeleteRecord",
 "x-tcaplus-version:Tcaplus3.32.0",
 "x-tcaplus-pwd-md5:c3eda5f013f92c81dda7afcdc273cf82",
 "x-tcaplus-result-flag:1",
 "x-tcaplus-idl-type:protobuf"
]
```

##### 请求 JSON 数据
```
{
 "ReturnValues": "Send to tcaplus by calvinshao",
 "Record": {
  "region": 101,
  "name": "calvinshao",
  "uin": 100
 }
}
```

##### 应答 JSON 数据
```
{
 "ErrorCode": 0,
 "Record": {},
 "RecordVersion": -1,
 "ReturnValues": "Send to tcaplus by calvinshao"
}
```


###  Tcaplus.FieldGetRecord 
```
GET /ver1.0/apps/{APP_ID}/zones/{ZONE_ID}/tables/{TABLE_NAME}/records?keys={JSONKeysObj}&select={JSONSelectObj}
```

从一个 Tcaplus pb 表中通过指定一条记录的 key 信息查询此记录。本操作只查询和传输用户通过 select 变量指定的字段的值，这将减少网络传输流量，这是与 GetRecord 操作最大的不同之处。如果数据记录不存在，将会返回错误。

必须在 URI 中指定`keys`和`select`变量。keys 指定所有主键的值，select 指定需要显示的 value 字段的名称，并且用户可以通过点分路径的方式指定嵌套结构中的字段，例如 “pay.total_money”。

>!请求的变量必须通过 urlencode 编码，请将url中的空格编码为"%20"而不是"+"。

| 名称               | 类型   | 取值                    |
| ------------------ | ------ | ----------------------- |
| x-tcaplus-target   | String | Tcaplus.FieldGetRecord  |
| x-tcaplus-version  | String | Tcaplus3.32.0           |
| x-tcaplus-pwd-md5  | String | MD5 of AppKey(Password) |
| x-tcaplus-idl-type | String | protobuf                |

#### 示例
##### URL 未 UrlEncode 结果
```
http://10.123.9.70/ver1.0/apps/2/zones/1/tables/tb_example/records?keys={"region": 101, "name": "calvinshao", "uin": 100}&select=["gamesvrid", "lockid", "pay.auth.pay_keys", "pay.total_money"]
```

##### URL UrlEncode 结果
```
http://10.123.9.70/ver1.0/apps/2/zones/1/tables/tb_example/records?keys=%7B%22region%22%3A%20101%2C%20%22name%22%3A%20%22calvinshao%22%2C%20%22uin%22%3A%20100%7D&select=%5B%22gamesvrid%22%2C%20%22lockid%22%2C%20%22pay.auth.pay_keys%22%2C%20%22pay.total_money%22%5D
```

##### 请求 HTTP 头
```
[
 "x-tcaplus-target:Tcaplus.FieldGetRecord",
 "x-tcaplus-version:Tcaplus3.32.0",
 "x-tcaplus-pwd-md5:c3eda5f013f92c81dda7afcdc273cf82",
 "x-tcaplus-idl-type:protobuf"
]
```

##### 应答 JSON 数据
```
{
 "ErrorCode": 0,
 "ErrorMsg": "Succeed",
 "RecordVersion": 1,
 "Record": {
  "name": "calvinshao",
  "lockid": [
   50,
   60,
   70
  ],
  "pay": {
   "total_money": 10000,
   "auth": {
    "pay_keys": "adqwacsasafasda"
   }
  },
  "region": 101,
  "uin": 100,
  "gamesvrid": 4099
 }
}
```

###  Tcaplus.FieldSetRecord  
```
PUT /ver1.0/apps/{APP_ID}/zones/{ZONE_ID}/tables/{TABLE_NAME}/records
```

通过指定一条记录的 key 信息修改此记录，与 SetRecord 操作不同的是此操作只传输并设置指定字段的值，并不传输所有字段。这将减轻网络流量。如果数据记录存在，将执行更新操作，否则将会返回错误。

FieldSetRecord操作支持resultflag设置以下取值：
* `0` 设置为0，应答中仅包含请求成功或失败。
* `1` 设置为1，应答中包含与请求一致的值。

| 名称                         | 类型   | 取值                    |
| ---------------------------- | ------ | ----------------------- |
| x-tcaplus-target             | String | Tcaplus.SetRecord       |
| x-tcaplus-version            | String | Tcaplus3.32.0           |
| x-tcaplus-pwd-md5            | String | MD5 of AppKey(Password) |
| x-tcaplus-result-flag        | Int    | 2                       |
| x-tcaplus-data-version-check | Int    | 2                       |
| x-tcaplus-data-version       | Int    | -1                      |
| x-tcaplus-idl-type           | String | protobuf                |


#### 示例
##### URL
```
http://10.123.9.70/ver1.0/apps/2/zones/1/tables/tb_example/records
```

##### 请求 HTTP 头
```
[
 "x-tcaplus-target:Tcaplus.FieldSetRecord",
 "x-tcaplus-version:Tcaplus3.32.0",
 "x-tcaplus-pwd-md5:c3eda5f013f92c81dda7afcdc273cf82",
 "x-tcaplus-result-flag:1",
 "x-tcaplus-data-version-check:1",
 "x-tcaplus-data-version:-1",
 "x-tcaplus-idl-type:Protobuf"
]
```

##### 请求 JSON 数据
```
{
 "ReturnValues": "aaaaaaaaaa",
 "FieldPath": [ // 显式指定需要更新的字段路径
    "gamesvrid",
    "logintime",
    "pay.total_money",
    "pay.auth.pay_keys"
 ],
 "Record": { // 设置需要更新的字段新值
  "name": "calvinshao",
  "pay": {
   "total_money": 17190,
   "auth": {
    "pay_keys": "bingo"
   }
  },
  "region": 101,
  "uin": 100,
  "gamesvrid": 1719,
  "logintime": 1719
 }
}
```

##### 应答 JSON 数据
```
{
 "ErrorCode": 0,
 "ErrorMsg": "Succeed",
 "RecordVersion": 3,
 "ReturnValues": "aaaaaaaaaa",
 "Record": {
  "name": "calvinshao",
  "pay": {
   "total_money": 17190,
   "auth": {
    "pay_keys": "bingo"
   }
  },
  "region": 101,
  "uin": 100,
  "gamesvrid": 1719,
  "logintime": 1719
 }
}
```


### Tcaplus.FieldIncRecord 
```
PUT /ver1.0/apps/{APP_ID}/zones/{ZONE_ID}/tables/{TABLE_NAME}/records
```

通过指定一条记录的 key 信息对指定的字段进行自增操作，此命令字仅支持 `int32`， `int64`， `uint32` 和 `uint64`类型字段。特性与 FieldSetRecord 类似。

SetRecord 操作支持 resultflag 设置以下取值：
* `0` 设置为0，应答中仅包含请求成功或失败。
* `1` 设置为1，应答中包含指定字段修改后的值。

| 名称                         | 类型   | 取值                    |
| ---------------------------- | ------ | ----------------------- |
| x-tcaplus-target             | String | Tcaplus.SetRecord       |
| x-tcaplus-version            | String | Tcaplus3.32.0           |
| x-tcaplus-pwd-md5            | String | MD5 of AppKey(Password) |
| x-tcaplus-result-flag        | Int    | 2                       |
| x-tcaplus-data-version-check | Int    | 2                       |
| x-tcaplus-data-version       | Int    | -1                      |
| x-tcaplus-idl-type           | String | protobuf                |


#### 示例
##### URL
```
http://10.123.9.70/ver1.0/apps/2/zones/1/tables/tb_example/records
```

##### 请求 HTTP 头
```
[
 "x-tcaplus-target:Tcaplus.FieldIncRecord",
 "x-tcaplus-version:Tcaplus3.32.0",
 "x-tcaplus-pwd-md5:c3eda5f013f92c81dda7afcdc273cf82",
 "x-tcaplus-result-flag:1",
 "x-tcaplus-data-version-check:1",
 "x-tcaplus-data-version:-1",
 "x-tcaplus-idl-type:Protobuf"
]
```

##### 请求 JSON 数据
```
{
 "ReturnValues": "aaaaaaaaaa",
 "Record": {
  "name": "calvinshao",
  "pay": {
   "total_money": -1, 
   "auth": {
    "update_time": -1
   }
  },
  "region": 101,
  "uin": 100,
  "gamesvrid": 2,
  "logintime": -2
 }
}
```

##### 应答 JSON 数据
```
{
 "ErrorCode": 0,
 "ErrorMsg": "Succeed",
 "RecordVersion": 9,
 "ReturnValues": "aaaaaaaaaa",
 "Record": {
  "name": "calvinshao",
  "pay": {
   "total_money": 11999,
   "auth": {
    "update_time": 921
   }
  },
  "region": 101,
  "uin": 100,
  "gamesvrid": 4101,
  "logintime": 98
 }
}
```


###  Tcaplus.PartkeyGetRecord 
```
GET /ver1.0/apps/{APP_ID}/zones/{ZONE_ID}/tables/{TABLE_NAME}/records?keys={JSONKeysObj}&select={JSONSelectObj}
```

通过指定部分主键的值查询多条记录。这个操作将返回多条数据，并且通过 select 变量指定的字段名显示。此操作的前提是指定的主键集合必须在建表的时候创建了索引，否则会返回错误。

必须在 URI 中指定`keys`变量，而 select 变量则是可选项。keys 指定所有主键的值，select 指定需要显示的 value 字段的名称。并且用户可以通过点分路径的方式指定嵌套结构中的字段，例如 “pay.total_money”。

limit 和 offset 是用于记录部分返回控制的参数。

>! 请求的变量必须通过 urlencode 编码，请将 url 中的空格编码为“%20”而不是“+”；请在 HEADER中 通过`x-tcaplus-index-name`指定想要访问的索引名，索引名在表定义文件中可以找到。

| 名称                 | 类型   | 取值                    |
| -------------------- | ------ | ----------------------- |
| x-tcaplus-target     | String | Tcaplus.GetRecord       |
| x-tcaplus-version    | String | Tcaplus3.32.0           |
| x-tcaplus-pwd-md5    | String | MD5 of AppKey(Password) |
| x-tcaplus-idl-type   | String | protobuf                |
| x-tcaplus-index-name | String | {index_name}            |


#### 示例
##### URL 未 UrlEncode 结果
```
http://10.123.9.70/ver1.0/apps/2/zones/1/tables/tb_example/records?keys={"name": "calvinshao", "uin": 100}&select=["gamesvrid", "lockid", "pay.total_money", "pay.auth.pay_keys"]
```

##### URL UrlEncode 结果
```
http://10.123.9.70/ver1.0/apps/2/zones/1/tables/tb_example/records?keys=%7B%22name%22%3A%20%22calvinshao%22%2C%20%22uin%22%3A%20100%7D&select=%5B%22gamesvrid%22%2C%20%22lockid%22%2C%20%22pay.total_money%22%2C%20%22pay.auth.pay_keys%22%5D
```

##### 请求 HTTP 头
```
[
"x-tcaplus-target:Tcaplus.PartkeyGetRecord",
"x-tcaplus-version:Tcaplus3.32.0",
"x-tcaplus-pwd-md5:c3eda5f013f92c81dda7afcdc273cf82",
"x-tcaplus-idl-type:protobuf"
"x-tcaplus-index-name:index_name"
]
```


##### 应答数据
```
{
 "ErrorCode": 0,
 "ErrorMsg": "Succeed",
 "MultiRecords": [
  {
   "RecordVersion": 9,
   "Record": {
    "name": "calvinshao",
    "lockid": [
     50,
     60,
     70,
     80,
     90,
     100
    ],
    "pay": {
     "total_money": 11999,
     "auth": {
      "pay_keys": "adqwacsasafasda"
     }
    },
    "region": 101,
    "uin": 100,
    "gamesvrid": 4101
   }
  },
  {
   "RecordVersion": 1,
   "Record": {
    "name": "calvinshao",
    "lockid": [
     50,
     60,
     70,
     80
    ],
    "pay": {
     "total_money": 10000,
     "auth": {
      "pay_keys": "adqwacsasafasda"
     }
    },
    "region": 102,
    "uin": 100,
    "gamesvrid": 4100
   }
  },
  {
   "RecordVersion": 1,
   "Record": {
    "name": "calvinshao",
    "lockid": [
     60,
     70,
     80,
     90
    ],
    "pay": {
     "total_money": 10000,
     "auth": {
      "pay_keys": "adqwacsasafasda"
     }
    },
    "region": 103,
    "uin": 100,
    "gamesvrid": 4101
   }
  }
 ],
 "RemainNum": 0,
 "TotalNum": 3
}
```
