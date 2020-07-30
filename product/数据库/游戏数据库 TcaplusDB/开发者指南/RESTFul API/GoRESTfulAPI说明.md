为满足用户通过 Golang 语言来操作 TcaplusDB，基于 RESTful API 封装了关于 TcaplusDB 表操作的接口，涵盖增删查改场景。本文主要为您介绍基于此 RESTful API 来操作 TcaplusDB PB 表。

## 准备工作
### 1. 创建 TcaplusDB 表
创建 TcaplusDB 示例表，示例表为[`game_players.proto`](https://tcaplusdb-sdk-1301716906.cos.ap-shanghai.myqcloud.com/3.36.0.192960/game_players.proto)，请参见 [创建表格](https://cloud.tencent.com/document/product/596/38808)。

### 2. 创建 CVM 实例
- 创建一台 CVM 实例来运行 SDK 示例程序，配置建议为2核4GB、硬盘50GB，该 CVM 需创建在 TcaplusDB 实例所在 VPC 网络中。
- 通过 [SDK 下载](https://cloud.tencent.com/document/product/596/31925) Go RESTful API SDK 安装包。

### 3. 准备 Go 环境
安装 Golang 执行环境，安装命令如下：
```
yum install -y golang
```

### 4.  编译程序
SDK 示例程序通过 make 编译，在 src 目录下有 Makefile 文件，直接执行`make build`即可。编译好后，会生成一个可执行文件`example`，直接执行此文件即可演示所有示例接口。

## 使用步骤
### 1. 配置表参数
在 [TcaplusDB 控制台](https://console.cloud.tencent.com/tcaplusdb/app) 查看所创建表的相关信息，在示例中进行配置，如下所示：
```
//TcaplusDB RESTful API 的连接参数
const (
        //服务接入点，表所在集群 RESTful 连接地址，默认端口80
        EndPoint = "http://172.xx.xx.12/"
        //应用接入 ID，表所在集群接入ID
        AccessID = 310
        //应用密码,表所在集群访问密码
        AccessPassword = "Tcaplus2020"
        //表格组ID
        TableGroupID = 1
        //表名称
        TableName = "game_players"
)
```

### 2. 创建表连接
通过 NewTcaplusClient 指定 EndPoint、AccessID、AccessPassword 参数，创建 TcaplusRestClient 的对象 client。
```
//通过指定 EndPoint、AccessID、AccessPassword参数，创建 TcaplusClient 的对象 client
client, err := tcaplus_client.NewTcaplusClient(EndPoint, AccessID, AccessPassword)
if err != nil {
    fmt.Println(err.Error())
    return
}
```

### 3. 表示例数据
插入数据为 JSON 格式，定义如下所示：
```
//AddRecord 插入记录
//用户可将 record 定义成结构体/map/slice，需可转成 json
record := map[string]interface{}{
    "player_id": 10805514,
    "player_name": "Calvin",
    "player_email": "calvin@test.com",
    "game_server_id": 10,
    "login_timestamp": []string{"2019-12-12 15:00:00"},
    "logout_timestamp": []string{"2019-12-12 16:00:00"},
    "is_online": false,
    "pay": map[string]interface{}{
        "pay_id": 10101,
        "amount": 1000,
        "method": 1,
    },
}
status, resp, err := client.AddRecord(record, tcaplus_client.RetAllLatestField, "userBuffer", TableGroupID, TableName)
if err != nil {
    fmt.Println(err.Error())
    return
}
```

## 接口列表
### GetRecord 记录查询
```
/**
	@brief  根据 Key 字段查询记录，可以根据 selectFiled 过滤出部分字段
	@param [IN] key             需要查询的记录的 key 字段信息，可以是结构体，map，slice，从而转成 json，与 proto 中定义的类型保持一致
	@param [IN] selectFiled     需要查询的记录的字段列表，结构体嵌套则设为点分式，为 nil 表示查询全部字段
	@param [IN] groupID         表格组 ID
	@param [IN] tableName       表名
	@retval(3) http 响应码，http 响应内容，错误信息
**/
func (c *TcaplusClient) GetRecord(key interface{}, selectFiled []string, groupID int, tableName string) (string, []byte, error)
```

### AddRecord 插入记录
```
/**
	@brief  添加一条记录到表中，该记录若存在，则会报错
	@param [IN] record          需要添加的记录，可以是结构体，map，slice，从而转成 json，与 proto 中定义的类型保持一致
	@param [IN] resultFlag      返回值标记位，可设置为以下值
                                        RetOnlySucOrFail：应答中仅包含请求成功或失败
                                        RetEqualReq：应答中包含与请求一致的值
                                        RetAllLatestField：应答中包含被修改的数据的所有字段最新值
                                        RetAllOldField：应答中包含记录被修改前的值
	@param [IN] userBuffer      用户自定义信息，在响应信息中原样返回，不关注则填""
	@param [IN] groupID         表格组 ID
	@param [IN] tableName       表名
	@retval(3) http 响应码，http 响应内容，错误信息
**/
func (c *TcaplusClient) AddRecord(record interface{}, resultFlag int, userBuffer string, groupID int, tableName string) (string, []byte, error)
 
```

### SetRecord 设置记录
```
/**
	@brief  更新/插入一条记录到表中，该记录若存在，则更新；不存在，则插入
	@param [IN] record          需要添加的记录，可以是结构体，map，slice，从而转成 json，与 proto 中定义的类型保持一致
	@param [IN] resultFlag      返回值标记位，可设置为以下值
                                        RetOnlySucOrFail：应答中仅包含请求成功或失败
                                        RetEqualReq：应答中包含与请求一致的值
                                        RetAllLatestField：应答中包含被修改的数据的所有字段最新值
                                        RetAllOldField：应答中包含记录被修改前的值
	@param [IN] versionPolicy   记录的版本号校验策略，与 version 配合使用，用于乐观锁，不关注则设置为 NoCheckDataVersionAutoIncrease
                                        CheckDataVersionAutoIncrease：检测记录版本号，只有当 version 与服务器端的版本号相同时，操作成功，记录版本号自增
                                        NoCheckDataVersionOverwrite：不检测记录版本号，强制把记录版本号 version 写入到服务器中
                                        NoCheckDataVersionAutoIncrease：不检测记录版本号，服务器端的版本号自增
	@param [IN] version         记录的版本号，用于版本号校验，不校验则设置为-1
	@param [IN] userBuffer      用户自定义信息，在响应信息中原样返回，不关注则填""
	@param [IN] groupID         表格组 ID
	@param [IN] tableName       表名
	@retval(3) http 响应码，http 响应内容，错误信息
**/
func (c *TcaplusClient) SetRecord(record interface{}, resultFlag int, versionPolicy int, version int, userBuffer string, groupID int, tableName string) (string, []byte, error) 

```

### DeleteRecord 删除记录
```
/**
	@brief  删除一条记录，不存在，则报错
	@param [IN] record          需要删除的记录，包含 key 字段即可；可以是结构体，map，slice，从而转成 json，与 proto 中定义的类型保持一致
	@param [IN] resultFlag      返回值标记位，可设置为以下值
                                        RetOnlySucOrFail：应答中仅包含请求成功或失败
                                        RetEqualReq：应答中包含与请求一致的值
                                        RetAllLatestField：应答中包含被修改的数据的所有字段最新值
                                        RetAllOldField：应答中包含记录被修改前的值
	@param [IN] userBuffer      用户自定义信息，在响应信息中原样返回，不关注则填""
	@param [IN] groupID         表格组 ID
	@param [IN] tableName       表名
	@retval(3) http 响应码，http 响应内容，错误信息
**/
func (c *TcaplusClient) DeleteRecord(record interface{}, resultFlag int, userBuffer string, groupID int, tableName string) (string, []byte, error)

```

### FieldGetRecord 指定字段查询

```
/**
	@brief  记录的部分字段查询，根据 key 字段查询记录，根据 selectFiled 过滤字段内容
	@note   该接口与 GetRecord 的区别：GetRecord 是查询的整条记录然后按 selectFiled 过滤；而 FieldGetRecord 是在 svr 端过滤，流量负载更低
	@param [IN] key             需要查询的记录的 key 字段信息，可以是结构体，map，slice，从而转成 json，与 proto 中定义的类型保持一致
	@param [IN] selectFiled     需要查询的记录的字段列表，不能为空，结构体嵌套则设为点分式
	@param [IN] groupID         表格组 ID
	@param [IN] tableName       表名
	@retval(3) http 响应码，http 响应内容，错误信息
**/
func (c *TcaplusClient) FieldGetRecord(key interface{}, selectFiled []string, groupID int, tableName string) (string, []byte, error)

```

### FieldSetRecord 指定字段设置
```
/**
	@brief  更新一条记录，该记录若不存在则报错
	@param [IN] record          需要添加的记录，可以是结构体，map，slice，从而转成 json，与 proto 中定义的类型保持一致
	@param [IN] setField        需要更新的字段列表，不能为空，结构体嵌套则设为点分式
	@param [IN] resultFlag      返回值标记位，可设置为以下值
                                        RetOnlySucOrFail：应答中仅包含请求成功或失败
                                        RetEqualReq：应答中包含与请求一致的值
	@param [IN] versionPolicy   记录的版本号校验策略，与 version 配合使用，用于乐观锁，不关注则设置为 NoCheckDataVersionAutoIncrease
                                        CheckDataVersionAutoIncrease：检测记录版本号，只有当 version 与服务器端的版本号相同时，操作成功，记录版本号自增
                                        NoCheckDataVersionOverwrite：不检测记录版本号，强制把记录版本号 version 写入到服务器中
                                        NoCheckDataVersionAutoIncrease：不检测记录版本号，服务器端的版本号自增
	@param [IN] version         记录的版本号，用于版本号校验，不校验则设置为-1
	@param [IN] userBuffer      用户自定义信息，在响应信息中原样返回，不关注则填""
	@param [IN] groupID         表格组 ID
	@param [IN] tableName       表名
	@retval(3) http 响应码，http 响应内容，错误信息
**/
func (c *TcaplusClient) FieldSetRecord(record interface{}, setField []string, resultFlag int, versionPolicy int, version int, userBuffer string, groupID int, tableName string) (string, []byte, error)
 
```

### FieldIncRecord 指定字段自增/自减
```
/**
	@brief  对记录中的整型字段进行自增/自减，此命令字仅支持 int32, int64, uint32 和 uint64类型字段
	@param [IN] record          需要更新的的记录，记录中的字段值为正，则表示自增，累加该值；为负，则表示自减，累减该值
	@param [IN] resultFlag      返回值标记位，可设置为以下值
                                        RetOnlySucOrFail：应答中仅包含请求成功或失败
                                        RetEqualReq：应答中包含与请求一致的值
	@param [IN] versionPolicy   记录的版本号校验策略，与 version 配合使用，用于乐观锁，不关注则设置为 NoCheckDataVersionAutoIncrease
                                        CheckDataVersionAutoIncrease：检测记录版本号，只有当 version 与服务器端的版本号相同时，操作成功，记录版本号自增
                                        NoCheckDataVersionOverwrite：不检测记录版本号，强制把记录版本号 version 写入到服务器中
                                        NoCheckDataVersionAutoIncrease：不检测记录版本号，服务器端的版本号自增
	@param [IN] version         记录的版本号，用于版本号校验，不校验则设置为-1
	@param [IN] userBuffer      用户自定义信息，在响应信息中原样返回，不关注则填""
	@param [IN] groupID         表格组 ID
	@param [IN] tableName       表名
	@retval(3) http 响应码，http 响应内容，错误信息
**/
func (c *TcaplusClient) FieldIncRecord(record interface{}, resultFlag int, versionPolicy int, version int, userBuffer string, groupID int, tableName string) (string, []byte, error)
 
```

### PartkeyGetRecord 索引查询，仅指定索引键
```
/**
	@brief  按索引进行批量查询
	@param [IN] key             需要查询的记录，仅需要索引包含的 key 字段，可以是结构体，map，slice，从而转成 json，与 proto 中定义的类型保持一致
	@param [IN] indexName       索引名称
	@param [IN] selectFiled     需要查询的记录的字段列表，结构体嵌套则设为点分式；为 nil 表示查询全部字段
	@param [IN] limit           批量返回的记录上限，>0有效
	@param [IN] offset          批量返回的记录的偏移，>=0有效
	@param [IN] groupID         表格组 ID
	@param [IN] tableName       表名
	@retval(3) http 响应码，http 响应内容，错误信息
**/
func (c *TcaplusClient) PartKeyGetRecord(key interface{}, indexName string, selectFiled []string, limit int, offset int, groupID int, tableName string) (string, []byte, error)
```

对于 PartKeyGetRecord 接口，1个请求返回的最大包大小为`256KB`，limit 的设置依赖于单条记录大小。推荐设置策略：
- 单条记录小于256KB：limit 参考设置为 256KB / [单条记录大小]，如记录大小为10KB，则 limit 推荐设置20 - 25左右。
- 单条记录大于等于256KB：limit 设置为1，即一次请求只返回一条记录。

对于设置 limit 和 offset 的场景，如果要根据索引键获取全量的数据，则需要依据响应包中返回的`TotalNum 和 RemainNum`标识来判断数据是否获取完全。

