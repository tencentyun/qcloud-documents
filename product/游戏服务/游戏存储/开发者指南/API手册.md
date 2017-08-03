### API 简介
- Tcaplus 化 API 是应用访问游戏存储服务集群的入口，是应用存取游戏存储服务集群中业务数据的编程接口。

### API 流程
- 应用在使用 API 时，需要提供 **APP ID，认证密码，一组入口 URL，以及已经创建好的表名称和 Zone ID** 等信息。其中，前三项是应用申请接入游戏存储服务成功后得到的，后两项是业务在游戏存储管理页面上创建表结构时，提供和确定下来的。使用游戏存储服务化 API，应用可以同时操作属于 App ID 的多个数据表。

### API 模块
- 用户可以定义 Protobuf 表，然后把表的协议传到 Tcaplus 系统中进行加表，然后就可以通过 Tcaplus Protobuf API 进行表数据的读写操作，当前 Protobuf API 支持的操作如下表：

| 操作 | 功能描述 |
|---------|---------|
| GET | 根据用户传的单个的 Key 获得单条 Value 信息 |
| BATCHGET | 根据用户传的多个的Key 获得多条 Value 信息 |
| SET | Key 对应记录存在则更新数据，否则插入数据请求 |
| DEL| 根据 Key 删除对应的记录 |
| INC | 指定字段的值（整数型）增加指定值 |

### API 常用接口
- **int Get(::google::protobuf::Message &msg);**
```
  @brief 根据用户输入的msgs中的key值，批量获取msg消息的字段值，并填充到  msgs中.
  @param [INOUT] msgs   用户输入的key值列表，返回指定字段填到msgs中
  @retval <0   失败，返回对应的错误码。
  @retval 0    成功。至少有一个字段查询成功才会返回0。
```
- **int BatchGet(std::vector< ::google::protobuf::Message * > &msgs);**
```
   @brief 根据用户输入的msg中的key值，删除msg。       
   @param [IN] msg   用户输入的key值，返回指定字段填到msg中
   @retval <0   失败，返回对应的错误码。
   @retval 0    成功。至少有一个字段查询成功才会返回0。
```
- **int Del(const ::google::protobuf::Message &msg);**
```
 @brief 根据用户输入的msg中的key值，和dottedpaths指定的字段名称，获取指定字段的值，并填充到msg中。
 @param [INOUT] msg   用户输入的key值，返回指定字段填到msg中
 @param [IN] dottedpaths 字段名称的点分嵌套字符串集
 @param [OUT] failedpaths 返回查找失败的字段名称的点分嵌套字符串集
 @retval <0   失败，返回对应的错误码。
 @retval 0    成功。至少有一个字段查询成功才会返回0。
```
- **int Set(const ::google::protobuf::Message &msg);**
```
 @brief 根据用户输入的msg中的key值和values增量值，和dottedpaths指定的字段名称，增加指定字段的值。字段为数值型变量。
 @param [INOUT] msg   用户输入的key值，返回增量字段的结果值更新到msg中
 @param [IN] dottedpaths 字段名称的点分嵌套字符串集
 @retval <0   失败，返回对应的错误码。表示没有任何字段更新
 @retval 0    成功。全部字段更新成功。
```
- **int FieldInc(::google::protobuf::Message &msg, const std::set &dottedpaths);**
```
 @brief 根据用户输入的msg中的key值，和dottedpaths指定的字段名称，更新指定字段的值。服务端不存在的值会追加进去。
 @param [IN] msg   用户输入的key值，返回指定字段填到msg中
 @param [IN] dottedpaths 字段名称的点分嵌套字符串集
 @retval <0   失败，返回对应的错误码。表示没有任何字段更新
 @retval 0    成功。全部字段更新成功。
```
- **int FieldSet(::google::protobuf::Message &msg, const std::set &dottedpaths);**
```
 @brief 根据用户输入的msg中的key值，和dottedpaths指定的字段名称，获取指定字段的值，并填充到msg中。
 @param [INOUT] msg   用户输入的key值，返回指定字段填到msg中
 @param [IN] dottedpaths 字段名称的点分嵌套字符串集
 @param [OUT] failedpaths 返回查找失败的字段名称的点分嵌套字符串集
 @retval <0   失败，返回对应的错误码。
 @retval 0    成功。至少有一个字段查询成功才会返回0。
```
### 规则与约束
- **Get 操作约束：**
 1\. 不能查询特定版本号的记录。
 2\. 如果待查询的字段原记录中不存在，则会返回字段默认值。
- **BatchGet 操作约束:**
 1\.批量查询操作必须经由 tcaproxy 进行消息路由处理，tcapsvr 进程不支持批量查询操作。
 2\.一个批量查询请求返回一个批量查询结果，批量查询的超时时间为 10 秒。
 3\.批量查询结果记录数同请求中记录数，查询不存在或者查询失败的记录也会在结果集中存在一条空的记录，因此需要通过 FetchRecord 进行记录获取。
 4\.批量查询结果集总大小不能超过 256 K，否则超过大小记录内容会无法返回，会返回空记录内容。
 5\.批量查询结果集返回的顺序与请求的记录顺序不保证一致。