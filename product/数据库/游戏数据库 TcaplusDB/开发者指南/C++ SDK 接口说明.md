## 简介
TcaplusDB 服务化 API 是应用访问游戏数据库 TcaplusDB 的数据访问入口，是应用存取游戏数据库 TcaplusDB 中业务数据的编程接口。当前 TcaplusDB 主要使用基于 Google Protocol Buffer（Protobuf） 做通讯和数据元定义协议。


## 流程
您在控制台开通业务创建完表后，控制台配置信息页会提供 AppId，AppKey，内网接入地址，以及 Protobuf 表管理页显示已经创建的表名称和部署单元 ID（ZoneId） 等信息。其中，前三项是应用申请接入游戏存储服务成功后得到的，后两项是业务在游戏存储管理页面上创建表结构时确定下来的。使用游戏存储服务化 API，应用可以操作属于 AppId 的多个数据表。

## 模块
您可以 Protobuf 协议来定义符合 TcaplusDB 规范的表，把表定义的元文件传到 TcaplusDB 控制台管理系统中进行创建新表或修改已经存在的表，成功后即可通过 TcaplusDB Protobuf API 进行表数据记录的读写操作，当前 TcaplusDB Protobuf API 支持的操作如下表：

| 操作 | 功能描述 |
|---------|---------|
| GET | 根据单个的 Key 获得单条 Value 信息 |
| BATCHGET | 根据多个的 Key 获得多条 Value 信息 |
| ADD | 插入一条数据。如果 Key 对应记录存在则报错 |
| SET | Key 对应记录存在则更新数据，否则插入数据请求 |
| DEL| 根据 Key 删除对应的记录 |
| FIELDINC | 指定字段的值（整数型）增加指定值 |
| FIELDSET | 更新指定字段（单个或多个）的值 |
| FIELDGET | 获取指定字段（单个或多个）的值 |
| INDEXGET | 指定索引和字段进行索引查询 |
| TRAVERSE | 指定表名进行全表遍历 |

## TcaplusDB SDK 约定
TcaplusDB 需要定义表的 primarykey 等信息，扩展 tcaplusservice.optionv1.proto 存在于 TcaplusDB 系统中，您只需在自定义表时引用，创建新表或修改已经存在的表时不用上传，系统已经内置。具体内容如下：
```
extend google.protobuf.MessageOptions
{
    optional string tcaplus_primary_key             = 60000; //定义表的主键
    repeated string tcaplus_index                   = 60001; //定义表的索引
    optional string tcaplus_field_cipher_suite      = 60002; //定义表的字段使用的加密算法
    optional string tcaplus_record_cipher_suite     = 60003; //定义表的字段使用的加密算法，暂时未使用
    optional string tcaplus_cipher_md5              = 60004; //用于返回cipher key信息摘要
    optional string tcaplus_sharding_key            = 60005; //Tcaplus sharding key
}

extend google.protobuf.FieldOptions
{
    optional uint32 tcaplus_size                    = 60000; // 字段大小，暂时未使用
    optional string tcaplus_desc                    = 60001; // 字段描述
    optional bool tcaplus_crypto                    = 60002; // 是否加密字段，加密算法由tcaplus_field_cipher_suite定义
}
```
完整文件可在目录 release\x86_64\include\tcaplus_pb_api\tcaplusservice.optionv1.proto 中找到。
1. 表名要以字母或下划线开头，不能超过31个字段，不能有除数字，字母，下划线之外的特殊字段。
2. 各字段的名称要以字母或下划线命名，protobuf 已经限制。
3. 主键最多4个字段，必须是 required 类型，打包后长度不能超过1022字节。
4. value 打包后不能超过256KB, 同时整个记录打包不能超过256KB。
5. 除了 key 字段，至少有一个 value 字段。value 字段上限以 protobuf 为准。
6. 表默认是 generic 类型。但对外不显示 generic 类型。
7. key 字段当前只能是 protobuf 规定的标量类型（Scalar Value Type），不能包括其它复合类型，自定义类型等。

## 常用接口说明
```
 @brief 根据用户输入的req中的index名称，msg值，offset以及limit，通过索引获取多个记录的值填充到res中的vec结构中，并返回总记录数以及剩余记录数。
 @param [INOUT] req   用户输入的req
 @param [INOUT] res   用户输入的res
 @retval <0   失败，返回对应的错误码。
 @retval 0    成功。
```
**int Get(::google::protobuf::Message &msg);**
```
  @brief 根据用户输入的 msgs 中的 key 值，批量获取 msg 消息的字段值，并填充到 msgs 中.
  @param [INOUT] msgs 用户输入的 key 值列表，返回指定字段填到 msgs 中
  @retval <0   失败，返回对应的错误码。
  @retval 0    成功。至少有一个字段查询成功才会返回 0。
```
**int BatchGet(std::vector< ::google::protobuf::Message * > &msgs);**

```
 @brief 根据用户输入的msg中的key，插入msg数据记录，如果key存在报错退出。
 @param [INOUT] msg   用户输入的key值，以及需要插入的数据记录msg。
 @retval <0   失败，返回对应的错误码。
 @retval 0    成功。
```
**int Add(::google::protobuf::Message \*msg);**

```
 @brief 根据用户输入的msg中的key，如果记录存在更新指定记录的值，否则插入指定记录。
 @param [INOUT] msg   用户输入的key值，以及需要设置的数据记录msg。
 @retval <0   失败，返回对应的错误码。
 @retval 0    成功。
```
**int Set(const ::google::protobuf::Message &msg);**

```
  @brief 根据用户输入的 msg 中的 key 值，删除 msg。       
  @param [IN] msg   用户输入的 key 值，返回指定字段填到 msg 中。
  @retval <0   失败，返回对应的错误码。
  @retval 0    成功。至少有一个字段查询成功才会返回 0。
```
**int Del(const ::google::protobuf::Message &msg);**
```
 @brief 根据用户输入的msg中的key值和values增量值，和dottedpaths指定的字段名称，增加msg指定字段的值。字段为数值型变量。
 @param [INOUT] msg   数据记录msg，包含用户输入的key值，返回增量字段的结果值更新到msg中
 @param [IN] dottedpaths 字段名称的点分嵌套字符串集
 @retval <0   失败，返回对应的错误码。表示没有任何字段更新
 @retval 0    成功。全部字段更新成功。
```
**int FieldInc(::google::protobuf::Message &msg, const std::set &dottedpaths);**
```
 @brief 根据用户输入的msg中的key值，和dottedpaths指定的字段名称，获取指定字段的值，并填充到msg中。
 @param [INOUT] msg   数据记录msg，包含用户输入的key值，返回指定字段填到msg中
 @param [IN] dottedpaths 字段名称的点分嵌套字符串集
 @param [OUT] failedpaths 返回查找失败的字段名称的点分嵌套字符串集
 @retval <0   失败，返回对应的错误码。
 @retval 0    成功。至少有一个字段查询成功才会返回0。
```
**int FieldGet(const std::set<std::string> &dottedpaths, ::google::protobuf::Message \*msg, std::set<std::string> \*failedpaths);**
```
 @brief 根据用户输入的 msg 中的 key 值，和 dottedpaths 指定的字段名称，更新指定字段的值。服务端不存在的值会追加进去。
 @param [IN] msg 用户输入的 key 值，返回指定字段填到 msg 中。
 @param [IN] dottedpaths 字段名称的点分嵌套字符串集。
 @retval <0   失败，返回对应的错误码。表示没有任何字段更新。
 @retval 0    成功。全部字段更新成功。
```
**int FieldSet(::google::protobuf::Message &msg, const std::set &dottedpaths);**
```
 @brief 根据用户输入的req中的index名称，msg值，offset以及limit，通过索引获取多个记录的值填充到res中的vec结构中，并返回总记录数以及剩余记录数。
 @param [INOUT] req   用户输入的req
 @param [INOUT] res   用户输入的res
 @retval <0   失败，返回对应的错误码。
 @retval 0    成功。
```
**int Get(NS_TCAPLUS_PROTOBUF_API::IndexGetRequest& req, NS_TCAPLUS_PROTOBUF_API::IndexGetResponse \*res);**
```
 @brief 遍历表，消息会填充到msg中。
 @param [INOUT] msg   返回指定字段填到msg中
 @param [INOUT] cb   回调函数
 @retval <0   失败，返回对应的错误码。
 @retval 0    遍历成功完成。
```
**int Traverse(::google::protobuf::Message \*msg, TcaplusTraverseCallback \*cb);**

## 规则与约束
### Get 操作约束
1. 不能查询特定版本号的记录。
1. 如果待查询的字段原记录中不存在，则会返回字段默认值。

### BatchGet 操作约束
1. 批量查询操作必须经由 tcaproxy 进行消息路由处理，tcapsvr 进程不支持批量查询操作。
1. 一个批量查询请求返回一个批量查询结果，批量查询的超时时间为10秒。
1. 批量查询结果记录数同请求中记录数，查询不存在或者查询失败的记录也会在结果集中存在一条空的记录，因此需要通过 FetchRecord 进行记录获取。
1. 批量查询结果集总大小不能超过256K，否则超过大小记录内容会无法返回，会返回空记录内容。
1. 批量查询结果集返回的顺序与请求的记录顺序不保证一致。

### FieldInc 操作约束
1. message 中指定的 key 的记录必须是存在。
1. dottedpaths 中指定的字段必须是数值类型。
1. dottedpaths 所在 set 中的元素个数总数不能起过128个。
1. dottedpaths 所在 set 中的每个元素的长度不能超过1023字节。
1. dottedpaths 所在 set 中的第个元素代表的字段嵌套不能超过32。

### FieldGet 操作约束
1. dottedpaths 所在 set 中的元素个数总数不能起过128个。
1. dottedpaths 所在 set 中的每个元素的长度不能超过1023字节。
1. dottedpaths 所在 set 中的第个元素代表的字段嵌套不能超过32。

### FieldSet 操作约束
1. dottedpaths 所在 set 中的元素个数总数不能起过128个。
1. dottedpaths 所在 set 中的每个元素的长度不能超过1023字节。
1. dottedpaths 所在 set 中的第个元素代表的字段嵌套不能超过32。


## SDK 源文件目录结构

    `-- release
        `-- x86_64
            |-- docs                                   文档目录
            |   `-- tcaplus
            |       `-- readme.txt                     本C++ SDK的使用描述指引文件
            |-- examples                               本C++ SDK使用的样例目录，分同步和异步两大部分,可以直接修改使用
            |-- include                                本C++ SDK的头文件目录
            |   `-- tcaplus_pb_api                     TcaplusDB PB API头文件夹
            |       |-- cipher_suite_base.h            数据加密码算法套件基类
            |       |-- default_aes_cipher_suite.h     数据加密码算法套件默认实现类
            |       |-- tcaplus_async_pb_api.h         异步模式类的头文件，使用异步模式当中的TcaplusAsyncPbApi类
            |       |-- tcaplus_coroutine_pb_api.h     协程模式类的头文件，使用协程模式当中的TcaplusCoroutinePbApi类
            |       |-- tcaplus_error_code.h           错误码头文件，所有涉及的错误码均可以在这里找到对应的定义及描述
            |       |-- tcaplus_protobuf_api.h         API汇总头文件，包含了其它头文件，只需引用这一个文件方便开发
            |       |-- tcaplus_protobuf_define.h      基础结构和宏定义头文件，包括ClientOptions结构和MESSAGE_OPTION_*宏定义
            |       |-- tcaplusservice.optionv1.pb.h   Tcaplus表公共定义的Protobuf头文件
            |       `-- tcaplusservice.optionv1.proto  Tcaplus表公共定义的proto源文件, 自定义表时需包含此文件
            |-- lib                                    本C++ SDK的库文件目录
            |   `-- libtcaplusprotobufapi.a            本C++ SDK的库文件, 程序最终链接库需包含
            `-- version                                本C++ SDK的版本记录文件



