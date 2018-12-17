## API 简介
TcaplusDB 服务化 API 是应用访问游戏存储服务集群的数据访问入口，是应用存取游戏存储服务集群中业务数据的编程接口。当前 TcaplusDB 主要使用基于 Google Protocol Buffer（Protobuf）做通讯和数据元定义协议。

## API 流程
用户在控制台开通业务创建完表后，控制台配置信息页会提供 AppId，AppKey，内网接入地址，以及 Protobuf 表管理页显示已经创建的表名称和部署单元 ID（ZoneId） 等信息。其中，前三项是应用申请接入游戏存储服务成功后得到的，后两项是业务在游戏存储管理页面上创建表结构时确定下来的。使用游戏存储服务化 API，应用可以操作属于 AppId 的多个数据表。

## API 模块
用户可以 Protobuf 协议来定义符合 TcaplusDB 规范的表，把表定义的元文件传到  TcaplusDB 控制台管理系统中进行创建新表或修改已经存在的表，成功后即可通过  TcaplusDB Protobuf API 进行表数据记录的读写操作，当前 TcaplusDB Protobuf API 支持的操作如下表：

| 操作 | 功能描述 |
|---------|---------|
| GET | 根据用户传的单个的 Key 获得单条 Value 信息 |
| BATCHGET | 根据用户传的多个的 Key 获得多条 Value 信息 |
| ADD | 插入一条数据。如果 Key 对应记录存在则报错 |
| SET | Key 对应记录存在则更新数据，否则插入数据请求 |
| DEL| 根据 Key 删除对应的记录 |
| FIELDINC | 指定字段的值（整数型）增加指定值 |
| FIELDSET | 更新指定字段（单个或多个）的值 |
| FIELDGET | 获取指定字段（单个或多个）的值 |
| INDEXGET | 指定索引和字段进行索引查询 |
| TRAVERSE | 指定表名进行全表遍历 |

## TcaplusDB Protobuf API 约定
TcaplusDB 需要定义表的 primarykey 等信息，扩展 tcaplusservice.optionv1.proto 存在于 TcaplusDB 系统中，用户只需在自定义表时引用，创建新表或修改已经存在的表时不用上传，系统已经内置。具体内容如下：
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
1. 表名要以字母或下载线开头，不能超过 31 个字段，不能有除数字，字母，下划线之外的特殊字段。
2. 各字段的名称要以字母或下划线，protobuf 已经限制。
3. 主键最多 4 个字段，必须是 required 类型，打包后长度不能超过 1022 字节。
4. value 打包后不能超过 256 KB, 同时整个记录打包不能超过 256 KB。
5. 除了 key 字段，至少有一个 value 字段。value 字段上限以 protobuf 为准。
6. 表默认是 generic 类型。但对外不显示 generic 类型。
7. key 字段当前只能是 protobuf 规定的标量类型（Scalar Value Type）,不能包括其它复合类型，自定义类型等。

## API 常用接口
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

下面就头文件包中的文件中的主要内容逐一介绍
### 文件 cipher_suite_base.h
这个文件主要是加密算法套件基类CipherSuite的声明，规定了子类的规范
```
// 加密算法套件基类
class CipherSuite
{
  public:
    // 构造函数
    CipherSuite() {}

    // 析构函数
    virtual ~CipherSuite() {}

    //返回加密算法套件唯一名称，子类必须实现
    virtual const char* GetName() = 0; 

    //初始化函数 cipher_key传入用户自定义的密钥，子类必须实现
    virtual int Init(const std::string &cipher_key) = 0; 

    //加密函数接口，子类必须实现
    virtual int Encrypt(const unsigned char* text, int len, unsigned char* data, int &data_len) = 0; 

    //解密函数接口，子类必须实现
    virtual int Decrypt(const unsigned char* data, int data_len, unsigned char* text, int &len) = 0; 

    //用于返回cipher key信息摘要(e.g MD5),此值与proto定义文件中 tcaplus_cipher_md5 属性保持一致，用于防错
    virtual const std::string GetCipherKeyMD5() {return "";} 
    
    //获取错误信息字符串，子类必须实现
    virtual const std::string GetErrMsg() = 0; 
};
```

### 文件default_aes_cipher_suite.h
这个文件主要是加密算法套件默认实现类DefaultAesCipherSuite的声明，是TcaplusDB基于AES加密的实现，用户可自定义密钥。
```
// 加密算法套件默认实现类DefaultAesCipherSuite
class DefaultAesCipherSuite: public CipherSuite
{
  public:
    // 构造函数
    DefaultAesCipherSuite();

    // 析构函数
    virtual ~DefaultAesCipherSuite();

    // 初始化函数 cipher_key传入用户自定义的密钥
    virtual int Init(const std::string &cipher_key);

    /*
     * 返回加密算法套件唯一名称DefaultAesCipherSuite
     */
    virtual const char* GetName() { return "DefaultAesCipherSuite"; } 

    /*
     * 加密函数,经过AES加密，并将加密密文通过Base64编码
     * IN:
     *  text        需要加密数据buff
     *  len         需要加密的数据长度
     * IN OUT:
     *  data        返回经过AES加密，再经过Base64编码的密文数据buff
     *  data_len    返回经过AES加密，再经过Base64编码的密文数据buff长度
     * RET:
     *  0           成功，否则失败，可以通过GetErrMsg函数获取错误信息
     */
    virtual int Encrypt(const unsigned char* text, int len, unsigned char* data, int &data_len);

    /*
     * 解密函数,将密文经过Base64解码，再通过AES解密得到明文
     * IN:
     *  data        需要解密数据buff
     *  data_len    需要解密的数据buff长度
     * IN OUT:
     *  text        经过Base64解码，再经过AES解密的明文数据buff
     *  len         经过Base64解码，再经过AES解密的明文数据buff长度
     * RET:
     *  0           成功，否则失败，可以通过GetErrMsg函数获取错误信息
     */
    virtual int Decrypt(const unsigned char* data, int data_len, unsigned char* text, int &len);

    /*
     * 用于返回cipher key信息摘要(e.g MD5),此值与proto定义文件中 tcaplus_cipher_md5 属性保持一致，用于防错
     */
    virtual const std::string GetCipherKeyMD5();

    /*
     * 获取错误信息
     */
    virtual const std::string GetErrMsg();

  private:
    // AES加密初始化， 内部用
    int aesEncInit(unsigned char* keyStr, int keyStrLen, unsigned char* salt);

    // AES解密初始化， 内部用
    int aesDecInit(unsigned char* keyStr, int keyStrLen, unsigned char* salt);

    // AES加密实现， 内部用
    int aesEncrypt(const unsigned char* text, int len, unsigned char* data, int &data_len);

    // AES解密实现， 内部用
    int aesDecrypt(const unsigned char* data, int data_len, unsigned char* text, int &len);

    // BASE64编码，内部用
    int base64Encode(const unsigned char* data, int length, bool with_nl, unsigned char* encodedData, int &encodedLen);

    // BASE64解码，内部用
    int base64Decode(const unsigned char* encodedData, int encodedLen, bool with_nl, unsigned char* data, int &length);

  private:
    //AES加解密相关CTX
    EVP_CIPHER_CTX *m_encCtx;
    EVP_CIPHER_CTX *m_decCtx;
    
    //MD5计算相关CTX
    MD5_CTX m_md5Ctx;
    
    //用户传的密钥及其MD5值
    std::string m_strCipherKey;
    std::string m_strCipherKeyMD5;

    //可能存在的报错信息
    std::string m_strErrMsg;

    // 内部用缓存
    unsigned char* m_pBuffer;
};
```

### 文件tcaplus_async_pb_api.h
TcaplusDB PB API异步模式的TcaplusAsyncPbApi类及回调类TcaplusPbCallback的实现
```
// 接回调用默认实现类
class TcaplusPbCallback
{
public:
    // 构造函数
    TcaplusPbCallback() {}
    
    // 析构函数
    virtual ~TcaplusPbCallback() {}
    
    // 收包回调用接口 Add/Del/Set场景会调用
    virtual int OnRecv(const std::vector< ::google::protobuf::Message *> &msgs) {return 0;}
    
    // 超时回调用接口    
    virtual int OnTimeout(const std::vector< ::google::protobuf::Message *> &msgs) {return 0;}
    
    // 出错回调用接口，errorcode为错误码
    virtual int OnError(const std::vector< ::google::protobuf::Message *> &msgs, int errorcode) {return 0;}
    
    // 收包回调用接口 FieldGet/FieldInc/FieldSet场景会调用    
    virtual int OnRecv(::google::protobuf::Message *msg, const std::set<std::string> &dottedpaths, const std::set<std::string> &failedpaths) {return 0;}
     
    // 收包回调用接口   
    virtual int OnRecv(const std::map< ::google::protobuf::Message *, int > &mapMsg) {return 0;}

    // 收包回调用接口IndexGet场景会调用
    virtual int OnRecv(const NS_TCAPLUS_PROTOBUF_API::IndexGetRequest &req, NS_TCAPLUS_PROTOBUF_API::IndexGetResponse *res) {return 0;}
};

// TcaplusDB PB API异步模式的TcaplusAsyncPbApi类
class TcaplusAsyncPbApi
{
public:
	TcaplusAsyncPbApi();
	virtual ~TcaplusAsyncPbApi();
   
    // 根据用户提供的客户端信息：比如APPID, ZONEID, APPKEY, 表名初始TcaplusAsyncPbApi
    int Init(NS_TCAPLUS_PROTOBUF_API::ClientOptions& option);
    
    // 用户可以在不同部署单元（区）间切换，以访问不同区的表
    int SelectZone(uint32_t zone_id); 
    
    int UpdateNetwork(); // 0 表示正常 1表示收到包
    
    /**
    *  设置消息的选项
    *    item取值有如下情况：
    *    a).MESSAGE_OPTION_VERSION_CHECK = 1, API中设置记录版本对比
    *       option取值有  "1":启用版本对比(默认)
    *                     "2": 不启用版本对比，强制把MESSAGE_OPTION_DATA_VERSION指定的记录版本号写入到服务器中
    *                     "3":不检测记录版本号，将服务器端的版本号自增
    *    b).MESSAGE_OPTION_DATA_VERSION = 2,  API中设置记录版本功能
    *       option取值代表期望记录的版本号对应的字符串，比如"10",表示记录版本号为10
    *    c).MESSAGE_OPTION_ASYNC_ID = 3       API中设置设置消息的异步ID
    *       option取值代表期望异步ID字符串，比如"13",表示异步ID为13
    *    d).MESSAGE_OPTION_MESSAGE_INVALID = 4       设置消息无效（在发送请求之后等消息还没回来之前生效）
    *       option取值代表期望异步ID字符串，比如"13",表示异步ID为13,如果没有设置异步ID保持为空
    *    e).MESSAGE_OPTION_MESSAGE_AUTO_RELEASE = 5,    API中设置设置消息的自动释放(异步模式生效)
    *    f).MESSAGE_OPTION_USER_BUFF = 6,           API中设置用户传入的自定义二进制数据, 最长1024Bytes
    *    g).MESSAGE_OPTION_CALLBACK_AUTO_RELEASE = 7,   API中设置回调的自动释放(异步模式生效)
    */
    int SetMessageOption(const ::google::protobuf::Message &msg, int32_t item, const std::string &option); // 为后续参数设置预留
        
    /**
    *  获取消息的选项
    *    item取值有如下情况：
    *    a).MESSAGE_OPTION_VERSION_CHECK = 1, 获取API中设定记录版本对比选项 
    *       option返回值有 "1":启用版本对比(默认)
    *                      "2": 不启用版本对比，强制把MESSAGE_OPTION_DATA_VERSION指定的记录版本号写入到服务器中
    *                      "3":不检测记录版本号，将服务器端的版本号自增
    *    b).MESSAGE_OPTION_DATA_VERSION = 2,  获取API中设置记录版本选项
    *       option返回值代表之前设置的记录的版本号对应的字符串，比如"10",表示记录版本号为10
    *    c).MESSAGE_OPTION_ASYNC_ID = 3       获取API中设置设置消息的异步ID选项
    *       option返回值代表之前设置的异步ID字符串，比如"13",表示异步ID为13
    *    d).MESSAGE_OPTION_MESSAGE_INVALID = 4       获取设置消息无效选项
    *    e).MESSAGE_OPTION_MESSAGE_AUTO_RELEASE = 5,    获取设置设置消息的自动释放选项
    *    f).MESSAGE_OPTION_USER_BUFF = 6,           获取用户传入的自定义二进制数据
    *    e).MESSAGE_OPTION_CALLBACK_AUTO_RELEASE = 7,    获取回调设置的自动释放选项
    */
    int GetMessageOption(const ::google::protobuf::Message &msg, int32_t item, std::string *option); // 为后续参数设置预留, 例如或取记录的version
        
    /**
    *  删除消息的选项
    *    item取值有如下情况：
    *    a).MESSAGE_OPTION_VERSION_CHECK = 1, 删除API中记录版本对比选项 
    *    b).MESSAGE_OPTION_DATA_VERSION = 2,  删除API中设置记录版本选项
    *    c).MESSAGE_OPTION_ASYNC_ID = 3       删除API中设置设置消息的异步ID选项
    *    d).MESSAGE_OPTION_MESSAGE_INVALID = 4       删除设置消息无效选项
    *    e).MESSAGE_OPTION_MESSAGE_AUTO_RELEASE = 5,    删除设置设置消息的自动释放选项
    *    f).MESSAGE_OPTION_USER_BUFF = 6,           删除用户传入的自定义二进制数据
    */
    int DelMessageOption(const ::google::protobuf::Message &msg, int32_t item); // 为后续参数设置预留
     
    /**
    *    @brief 根据用户输入的msg中的key值，获取msg消息的字段值，并填充到msg中。
    *          
    *    @param [INOUT] msg   用户输入的key值，返回指定字段填到msg中
	*    @param [INOUT] cb    消息回调函数
    *    @retval <0   失败，返回对应的错误码。
    *    @retval 0    成功。
    */   
    int Get(::google::protobuf::Message *msg, TcaplusPbCallback *cb);

    /**
    *    @brief 根据用户输入的req中的index名称，msg值，offset以及limit，通过索引获取多个记录的值填充到res中的vec结构中，并返回总记录数以及剩余记录数。
    *          
    *    @param [INOUT] req   用户输入的req
    *    @param [INOUT] res   用户输入的res
	*    @param [INOUT] cb    消息回调函数
    *    @retval <0   失败，返回对应的错误码。
    *    @retval 0    成功。
    */   
    int Get(NS_TCAPLUS_PROTOBUF_API::IndexGetRequest& req, TcaplusPbCallback *cb);
    
    /**
    *    @brief 根据用户输入的msgs中的key值，批量获取msg消息的字段值，并填充到msgs中?
    *          
    *    @param [INOUT] msgs   用户输入的key值列表，返回指定字段填到msgs中
	*    @param [INOUT] cb    消息回调函数
    *    @retval <0   失败，返回对应的错误码。
    *    @retval 0    成功。至少有一个字段查询成功才会返回0。
    */
    int BatchGet(std::vector< ::google::protobuf::Message * > *msgs, TcaplusPbCallback *cb);
      
    /**
    *    @brief 根据用户输入的msg中的key值，删除msg。
    *          
    *    @param [IN] msg   用户输入的key值，返回指定字段填到msg中，并调用cb。
	*    @param [INOUT] cb    消息回调函数
    *    @retval <0   失败，返回对应的错误码。
    *    @retval 0    成功。
    */   
    int Del(::google::protobuf::Message *msg, TcaplusPbCallback *cb);
    
    /**
    *    @brief 根据用户输入的msg中的key，如果记录存在更新指定记录的值，否则插入指定记录。
    *          
    *    @param [INOUT] msg   用户输入的key值，以及需要设置的数据记录msg。
    *    @param [INOUT] cb    消息回调函数
    *    @retval <0   失败，返回对应的错误码。
    *    @retval 0    成功。
    */
    int Set(::google::protobuf::Message *msg, TcaplusPbCallback *cb);

    /**
    *    @brief 根据用户输入的msg中的key，插入msg数据记录，如果key存在报错退出。
    *          
    *    @param [INOUT] msg   用户输入的key值，返回指定字段填到msg中
	*    @param [INOUT] cb    消息回调函数
    *    @retval <0   失败，返回对应的错误码。
    *    @retval 0    成功。至少有一个字段查询成功才会返回0。
    */   
    int Add(::google::protobuf::Message *msg, TcaplusPbCallback *cb);
        
    /**
    *    @brief 根据用户输入的msg中的key值和values增量值，和dottedpaths指定的字段名称，增加msg指定字段的值。字段为数值型变量。
    *    @param [INOUT] msg   数据记录msg，包含用户输入的key值，返回增量字段的结果值更新到msg中
    *    @param [IN] dottedpaths 字段名称的点分嵌套字符串集
    *    @retval <0   失败，返回对应的错误码。表示没有任何字段更新
    *    @retval 0    成功。全部字段更新成功。
    */
    int FieldInc(const std::set<std::string> &dottedpaths, ::google::protobuf::Message *msg, TcaplusPbCallback *cb);
 
    /**
    *    @brief 根据用户输入的msg中的key值，和dottedpaths指定的字段名称，更新msg指定字段的值。服务端不存在的值会追加进去。
    *          
    *    @param [IN] msg   数据记录msg，包含用户输入的key值，返回指定字段填到msg中
    *    @param [IN] dottedpaths 字段名称的点分嵌套字符串集
    *    @retval <0   失败，返回对应的错误码。表示没有任何字段更新
    *    @retval 0    成功。全部字段更新成功。
    */
    int FieldSet(const std::set<std::string> &dottedpaths, ::google::protobuf::Message *msg, TcaplusPbCallback *cb);
   
    /**
    *    @brief 根据用户输入的msg中的key值，和dottedpaths指定的字段名称，获取指定字段的值，并填充到msg中。
    *          
    *    @param [INOUT] msg   数据记录msg，包含用户输入的key值，返回指定字段填到msg中
    *    @param [IN] dottedpaths 字段名称的点分嵌套字符串集
    *    @param [OUT] failedpaths 返回查找失败的字段名称的点分嵌套字符串集
    *    @retval <0   失败，返回对应的错误码。
    *    @retval 0    成功。至少有一个字段查询成功才会返回0。
    */
    int FieldGet(const std::set<std::string> &dottedpaths, ::google::protobuf::Message *msg, TcaplusPbCallback *cb);

    /**
    *    @brief 遍历表，消息会填充到msg中。
    *          
    *    @param [INOUT] msg   返回指定字段填到msg中
    *    @param [INOUT] cb   回调函数
    *    @retval <0   失败，返回对应的错误码。
    *    @retval 0    遍历成功完成。
    */
    int Traverse(::google::protobuf::Message *msg, TcaplusPbCallback *cb);
        
    /**
    *    @brief 返回当前待处理消息数
    *
    *    @retval 当前待处理消息计数
    */
    size_t GetPendingCount() { return m_mapStatus.size();}

    
    /**
    *    @brief 注册加密套件
    *          
    *    @param [IN] suite   加密套件
    *    @retval <0   失败，注册失败。
    *    @retval 0    创建一个协程并启动。
    */ 
    int RegisterCipherSuite(CipherSuite *suite);
        
    /**
    *    @brief 注销加密套件
    *          
    *    @param [IN] suite   加密套件
    *    @retval <0   失败，注销失败。
    *    @retval 0    成功，注销成功
    */
    int UnregisterCipherSuite(CipherSuite *suite);
    
    //  退出函数，与init调用相反
    void Fini();
    
private:
    // 超时处理，内部用
    void ProcessTimeOutSession();
    
    // 收包处理，内部用
    int ProcessTcaplusResponse(TcaplusService::TcaplusServiceResponse* response);
    
private:
    // 成员，内部用
    bool m_bInit;
    uint64_t m_asyn_id; 
    int64_t m_tmLast;
    int m_session_time_out_ms;
    TCAPLUS_KV::TcaplusKVApi *m_pKVApi;
    struct tagTLogCategoryInst *m_pLog;
    struct tagtbl_idl *m_pTblIdl;
	std::map<uint64_t, MsgStatus *> m_mapStatus;
};
```

### tcaplus_coroutine_pb_api.h
TcaplusDB PB API协程模式的TcaplusCoroutinePbApi类声明
```
// 协程模式类声明
class TcaplusCoroutinePbApi
{
public:
    TcaplusCoroutinePbApi();
    virtual ~TcaplusCoroutinePbApi();
   
    // 根据用户提供的客户端信息：比如APPID, ZONEID, APPKEY, 表名初始TcaplusCoroutinePbApi
    int Init(NS_TCAPLUS_PROTOBUF_API::ClientOptions& option);
    
    // 用户可以在不同部署单元（区）间切换，以访问不同区的表
    int SelectZone(uint32_t zone_id); 
    
    int UpdateNetwork(); // 0 表示正常 1表示收到包
    schedule* GetCoSchedule();
    
    /**
    *  设置消息的选项
    *    item取值有如下情况：
    *    a).MESSAGE_OPTION_VERSION_CHECK = 1, API中设置记录版本对比
    *       option取值有  "1":启用版本对比(默认)
    *                     "2": 不启用版本对比，强制把MESSAGE_OPTION_DATA_VERSION指定的记录版本号写入到服务器中
    *                     "3":不检测记录版本号，将服务器端的版本号自增
    *    b).MESSAGE_OPTION_DATA_VERSION = 2,  API中设置记录版本功能
    *       option取值代表期望记录的版本号对应的字符串，比如"10",表示记录版本号为10
    *    c).MESSAGE_OPTION_ASYNC_ID = 3       API中设置设置消息的异步ID
    *       option取值代表期望异步ID字符串，比如"13",表示异步ID为13
    *    d).MESSAGE_OPTION_MESSAGE_INVALID = 4       设置消息无效（在发送请求之后等消息还没回来之前生效）
    *       option取值代表期望异步ID字符串，比如"13",表示异步ID为13,如果没有设置异步ID保持为空
    *    e).MESSAGE_OPTION_MESSAGE_AUTO_RELEASE = 5,    API中设置设置消息的自动释放(异步模式生效)
    *    f).MESSAGE_OPTION_USER_BUFF = 6,           API中设置用户传入的自定义二进制数据, 最长1024Bytes
    */
    int SetMessageOption(const ::google::protobuf::Message &msg, int32_t item, const std::string &option); // 为后续参数设置预留
        
    /**
    *  获取消息的选项
    *    item取值有如下情况：
    *    a).MESSAGE_OPTION_VERSION_CHECK = 1, 获取API中设定记录版本对比选项 
    *       option返回值有 "1":启用版本对比(默认)
    *                      "2": 不启用版本对比，强制把MESSAGE_OPTION_DATA_VERSION指定的记录版本号写入到服务器中
    *                      "3":不检测记录版本号，将服务器端的版本号自增
    *    b).MESSAGE_OPTION_DATA_VERSION = 2,  获取API中设置记录版本选项
    *       option返回值代表之前设置的记录的版本号对应的字符串，比如"10",表示记录版本号为10
    *    c).MESSAGE_OPTION_ASYNC_ID = 3       获取API中设置设置消息的异步ID选项
    *       option返回值代表之前设置的异步ID字符串，比如"13",表示异步ID为13
    *    d).MESSAGE_OPTION_MESSAGE_INVALID = 4       获取设置消息无效选项
    *    e).MESSAGE_OPTION_MESSAGE_AUTO_RELEASE = 5,    获取设置设置消息的自动释放选项
    *    f).MESSAGE_OPTION_USER_BUFF = 6,           获取用户传入的自定义二进制数据
    */
    int GetMessageOption(const ::google::protobuf::Message &msg, int32_t item, std::string *option); // 为后续参数设置预留, 例如或取记录的version
        
    /**
    *  删除消息的选项
    *    item取值有如下情况：
    *    a).MESSAGE_OPTION_VERSION_CHECK = 1, 删除API中记录版本对比选项 
    *    b).MESSAGE_OPTION_DATA_VERSION = 2,  删除API中设置记录版本选项
    *    c).MESSAGE_OPTION_ASYNC_ID = 3       删除API中设置设置消息的异步ID选项
    *    d).MESSAGE_OPTION_MESSAGE_INVALID = 4       删除设置消息无效选项
    *    e).MESSAGE_OPTION_MESSAGE_AUTO_RELEASE = 5,    删除设置设置消息的自动释放选项
    *    f).MESSAGE_OPTION_USER_BUFF = 6,           删除用户传入的自定义二进制数据
    */
    int DelMessageOption(const ::google::protobuf::Message &msg, int32_t item); // 为后续参数设置预留
     
    /**
    *    @brief 根据用户输入的msg中的key值，获取msg消息的字段值，并填充到msg中。
    *          
    *    @param [INOUT] msg   用户输入的key值，返回指定字段填到msg中
    *    @retval <0   失败，返回对应的错误码。
    *    @retval 0    成功。
    */   
    int Get(::google::protobuf::Message *msg);

    /**
    *    @brief 根据用户输入的req中的index名称，msg值，offset以及limit，通过索引获取多个记录的值填充到res中的vec结构中，并返回总记录数以及剩余记录数。
    *          
    *    @param [INOUT] req   用户输入的req
    *    @param [INOUT] res   用户输入的res
    *    @retval <0   失败，返回对应的错误码。
    *    @retval 0    成功。
    */   
    int Get(NS_TCAPLUS_PROTOBUF_API::IndexGetRequest& req, NS_TCAPLUS_PROTOBUF_API::IndexGetResponse *res);
    
    /**
    *    @brief 根据用户输入的msgs中的key值，批量获取msg消息的字段值，并填充到msgs中。
    *          
    *    @param [INOUT] msgs   用户输入的key值列表，返回指定字段填到msgs中
    *    @retval <0   失败，返回对应的错误码。
    *    @retval 0    成功。至少有一个字段查询成功才会返回0。
    */
    int BatchGet(std::vector< ::google::protobuf::Message * > *msgs);
      
    /**
    *    @brief 根据用户输入的msg中的key值，删除msg。
    *          
    *    @param [IN] msg   数据记录msg，包含用户需要删除记录的key值
    *    @retval <0   失败，返回对应的错误码。
    *    @retval 0    成功。
    */   
    int Del(::google::protobuf::Message *msg);
    
    /**
    *    @brief 根据用户输入的msg中的key，如果记录存在更新指定记录的值，否则插入指定记录。
    *          
    *    @param [INOUT] msg   用户输入的key值，以及需要设置的数据记录msg。
    *    @retval <0   失败，返回对应的错误码。
    *    @retval 0    成功。
    */
    int Set(::google::protobuf::Message *msg);

    /**
    *    @brief 根据用户输入的msg中的key，插入msg数据记录，如果key存在报错退出。
    *          
    *    @param [INOUT] msg   用户输入的key值，以及需要插入的数据记录msg。
    *    @retval <0   失败，返回对应的错误码。
    *    @retval 0    成功。
    */ 
    int Add(::google::protobuf::Message *msg);

    /**
    *    @brief 根据用户输入的msg中的key值和values增量值，和dottedpaths指定的字段名称，增加msg指定字段的值。字段为数值型变量。
    *    @param [INOUT] msg   数据记录msg，包含用户输入的key值，返回增量字段的结果值更新到msg中
    *    @param [IN] dottedpaths 字段名称的点分嵌套字符串集
    *    @retval <0   失败，返回对应的错误码。表示没有任何字段更新
    *    @retval 0    成功。全部字段更新成功。
    */
    int FieldInc(const std::set<std::string> &dottedpaths, ::google::protobuf::Message *msg);
 
    /**
    *    @brief 根据用户输入的msg中的key值，和dottedpaths指定的字段名称，更新msg指定字段的值。服务端不存在的值会追加进去。
    *          
    *    @param [IN] msg   数据记录msg，包含用户输入的key值，返回指定字段填到msg中
    *    @param [IN] dottedpaths 字段名称的点分嵌套字符串集
    *    @retval <0   失败，返回对应的错误码。表示没有任何字段更新
    *    @retval 0    成功。全部字段更新成功。
    */
    int FieldSet(const std::set<std::string> &dottedpaths, ::google::protobuf::Message *msg);
   
    /**
    *    @brief 根据用户输入的msg中的key值，和dottedpaths指定的字段名称，获取指定字段的值，并填充到msg中。
    *          
    *    @param [INOUT] msg   数据记录msg，包含用户输入的key值，返回指定字段填到msg中
    *    @param [IN] dottedpaths 字段名称的点分嵌套字符串集
    *    @param [OUT] failedpaths 返回查找失败的字段名称的点分嵌套字符串集
    *    @retval <0   失败，返回对应的错误码。
    *    @retval 0    成功。至少有一个字段查询成功才会返回0。
    */
    int FieldGet(const std::set<std::string> &dottedpaths, ::google::protobuf::Message *msg, std::set<std::string> *failedpaths);

    /**
    *    @brief 遍历表，消息会填充到msg中。
    *          
    *    @param [INOUT] msg   返回指定字段填到msg中
    *    @param [INOUT] cb   回调函数
    *    @retval <0   失败，返回对应的错误码。
    *    @retval 0    遍历成功完成。
    */
    int Traverse(::google::protobuf::Message *msg, TcaplusTraverseCallback *cb);

    /**
    *    @brief 创建一个协程并启动
    *          
    *    @param [IN] func   自定义函数
    *    @param [IN] ud      入参   
    *    @retval <0   失败，返回对应的错误码。
    *    @retval 0    创建一个协程并启动。
    */
    int CreateTask(USER_FUNC func, void *ud);
    
    /**
    *    @brief 注册加密套件
    *          
    *    @param [IN] suite   加密套件
    *    @retval <0   失败，注册失败。
    *    @retval 0    创建一个协程并启动。
    */ 
    int RegisterCipherSuite(CipherSuite *suite);
        
    /**
    *    @brief 注销加密套件
    *          
    *    @param [IN] suite   加密套件
    *    @retval <0   失败，注销失败。
    *    @retval 0    成功，注销成功
    */
    int UnregisterCipherSuite(CipherSuite *suite);
    
    /**
    *    @brief 返回当前待处理协程计数
    *
    *    @retval 当前待处理协程计数
    */
    size_t GetPendingCount();
    
    void Fini();

protected:
    // 内部用成员函数
    void AddSession(uint64_t session_id, int64_t co_id, int time_out_ms);            
    CoSession* GetSession(uint64_t session_id);
    void RemoveSession(uint64_t session_id); 
    void ProcessTimeOutSession();
    int ProcessTcaplusResponse();
    int ProcessResponse(int cmd, const std::string& table_name, std::vector< ::google::protobuf::Message * > &msgs);
    int ProcessResponse(int cmd, const std::string& table_name, ::google::protobuf::Message *msg, std::set<std::string> &failedpaths);
    int ProcessResponse(int cmd, const std::string& table_name, ::google::protobuf::Message *msg, NS_TCAPLUS_PROTOBUF_API::IndexGetResponse *res);
    struct schedule* m_co_schedule;
    
private:
    // 内部用成员变量
    bool m_bInit;
    uint64_t m_asyn_id;                                 // 异步ID，即session id，每次自增1
    std::map<uint64_t, CoSession> m_co_session_map;	    // sessionid->session
    uint64_t m_cur_session_id;                          // 当前的session_id
    std::multimap<int64_t, uint64_t> m_co_timeout_map;  // 过期时间->sessionid
    TcaplusService::TcaplusServiceResponse *m_response;
    std::map<uint64_t, std::map<int32_t, std::string> > m_msg_options;
        
    int m_session_time_out_ms;
    TCAPLUS_KV::TcaplusKVApi *m_pKVApi;
    struct tagTLogCategoryInst *m_pLog;
    struct tagtbl_idl *m_pTblIdl;
};
```
### 文件 tcaplus_error_code.h
TcaplusDB PB API常用错误码及描述，所表达的意义
```
static const int32_t GEN_ERR_SUC                                                                     = 0x00000000;
static const int32_t GEN_ERR_ERR                                                                     = -0x00000100;/*-256*/
static const int32_t GEN_ERR_ECMGR_INVALID_MODULE_ID                                                 = -0x00000200;/*-512*/
static const int32_t GEN_ERR_ECMGR_INVALID_ERROR_CODE                                                = -0x00000300;/*-768*/
static const int32_t GEN_ERR_ECMGR_NULL_ERROR_STRING                                                 = -0x00000400;/*-1024*/
static const int32_t GEN_ERR_ECMGR_DUPLICATED_ERROR_CODE                                             = -0x00000500;/*-1280*/
static const int32_t GEN_ERR_TXLOG_NULL_POINTER_FROM_TSD                                             = -0x00000600;/*-1536*/
static const int32_t GEN_ERR_TABLE_READONLY                                                          = -0x00000700;/*-1792*/
static const int32_t GEN_ERR_TABLE_READ_DELETE                                                       = -0x00000800;/*-2048*/
static const int32_t GEN_ERR_ACCESS_DENIED                                                           = -0x00000900;/*-2304*/
static const int32_t GEN_ERR_INVALID_ARGUMENTS                                                       = -0x00000A00;/*-2560*/
static const int32_t GEN_ERR_UNSUPPORT_OPERATION                                                     = -0x00000B00;/*-2816*/
static const int32_t GEN_ERR_NOT_ENOUGH_MEMORY                                                       = -0x00000C00;/*-3072*/
static const int32_t GEN_ERR_NOT_SATISFY_INSERT_FOR_SORTLIST                                         = -0x00000D00;/*-3328*/
//GENERAL SYSTEM (module id 0x01) Error String defined below 
//......

//LINELOC BUSINESS (module id 0x02) Error Code defined below 
static const int32_t LOC_ERR__0x00000102                                                             = -0x00000102;/*-258*/
static const int32_t LOC_ERR__0x00000202                                                             = -0x00000202;/*-514*/
static const int32_t LOC_ERR__0x00000302                                                             = -0x00000302;/*-770*/
static const int32_t LOC_ERR__0x00000402                                                             = -0x00000402;/*-1026*/
static const int32_t LOC_ERR__0x00000502                                                             = -0x00000502;/*-1282*/
static const int32_t LOC_ERR__0x00000602                                                             = -0x00000602;/*-1538*/
static const int32_t LOC_ERR__0x00000702                                                             = -0x00000702;/*-1794*/
static const int32_t LOC_ERR__0x00000802                                                             = -0x00000802;/*-2050*/
static const int32_t LOC_ERR__0x00000902                                                             = -0x00000902;/*-2306*/
static const int32_t LOC_ERR__0x00000A02                                                             = -0x00000A02;/*-2562*/
static const int32_t LOC_ERR__0x00000B02                                                             = -0x00000B02;/*-2818*/
static const int32_t LOC_ERR__0x00000C02                                                             = -0x00000C02;/*-3074*/
static const int32_t LOC_ERR__0x00000D02                                                             = -0x00000D02;/*-3330*/
static const int32_t LOC_ERR__0x00000E02                                                             = -0x00000E02;/*-3586*/
static const int32_t LOC_ERR__0x00000F02                                                             = -0x00000F02;/*-3842*/
static const int32_t LOC_ERR__0x00001002                                                             = -0x00001002;/*-4098*/
static const int32_t LOC_ERR__0x00001102                                                             = -0x00001102;/*-4354*/
static const int32_t LOC_ERR__0x00001202                                                             = -0x00001202;/*-4610*/
static const int32_t LOC_ERR__0x00001302                                                             = -0x00001302;/*-4866*/
static const int32_t LOC_ERR__0x00001402                                                             = -0x00001402;/*-5122*/
static const int32_t LOC_ERR__0x00001502                                                             = -0x00001502;/*-5378*/
static const int32_t LOC_ERR__0x00001602                                                             = -0x00001602;/*-5634*/
static const int32_t LOC_ERR__0x00001702                                                             = -0x00001702;/*-5890*/
static const int32_t LOC_ERR__0x00001802                                                             = -0x00001802;/*-6146*/
static const int32_t LOC_ERR__0x00001902                                                             = -0x00001902;/*-6402*/
static const int32_t LOC_ERR__0x00001A02                                                             = -0x00001A02;/*-6658*/
static const int32_t LOC_ERR__0x00001B02                                                             = -0x00001B02;/*-6914*/
static const int32_t LOC_ERR__0x00001C02                                                             = -0x00001C02;/*-7170*/
static const int32_t LOC_ERR__0x00001D02                                                             = -0x00001D02;/*-7426*/
static const int32_t LOC_ERR__0x00001E02                                                             = -0x00001E02;/*-7682*/
static const int32_t LOC_ERR__0x00001F02                                                             = -0x00001F02;/*-7938*/
static const int32_t LOC_ERR__0x00002002                                                             = -0x00002002;/*-8194*/
static const int32_t LOC_ERR__0x00002802                                                             = -0x00002802;/*-10242*/
static const int32_t LOC_ERR__0x00003002                                                             = -0x00003002;/*-12290*/
static const int32_t LOC_ERR__0x00003802                                                             = -0x00003802;/*-14338*/
static const int32_t LOC_ERR__0x00004002                                                             = -0x00004002;/*-16386*/
static const int32_t LOC_ERR__0x00004802                                                             = -0x00004802;/*-18434*/
static const int32_t LOC_ERR__0x00005002                                                             = -0x00005002;/*-20482*/
static const int32_t LOC_ERR__0x00005802                                                             = -0x00005802;/*-22530*/
static const int32_t LOC_ERR__0x00006002                                                             = -0x00006002;/*-24578*/
static const int32_t LOC_ERR__0x00006802                                                             = -0x00006802;/*-26626*/
static const int32_t LOC_ERR__0x00007002                                                             = -0x00007002;/*-28674*/
static const int32_t LOC_ERR__0x00007802                                                             = -0x00007802;/*-30722*/
static const int32_t LOC_ERR__0x00008002                                                             = -0x00008002;/*-32770*/
static const int32_t LOC_ERR__0x00008802                                                             = -0x00008802;/*-34818*/
static const int32_t LOC_ERR__0x00009002                                                             = -0x00009002;/*-36866*/
static const int32_t LOC_ERR__0x00009802                                                             = -0x00009802;/*-38914*/
static const int32_t LOC_ERR__0x0000A002                                                             = -0x0000A002;/*-40962*/
static const int32_t LOC_ERR__0x0000A802                                                             = -0x0000A802;/*-43010*/
static const int32_t LOC_ERR__0x0000B002                                                             = -0x0000B002;/*-45058*/
static const int32_t LOC_ERR__0x0000B802                                                             = -0x0000B802;/*-47106*/
static const int32_t LOC_ERR__0x0000C002                                                             = -0x0000C002;/*-49154*/
static const int32_t LOC_ERR__0x0000C802                                                             = -0x0000C802;/*-51202*/
//......
static const int32_t LOC_ERR__0x0000FF02                                                             = -0x0000FF02;/*-65282*/

//LINELOC SYSTEM (module id 0x03) Error String defined below 
//......

//TXHDB BUSINESS (module id 0x04) Error Code defined below 
//......

//TXHDB SYSTEM (module id 0x05) Error Code defined below 
static const int32_t TXHDB_ERR_RECORD_NOT_EXIST                                                      = 0x00000105;/*261*/
static const int32_t TXHDB_ERR_ITERATION_NO_MORE_RECORDS                                             = 0x00000205;/*517*/
static const int32_t TXHDB_ERR_MUTEX_TRYLOCK_BUSY                                                    = 0x00000305;/*773*/
static const int32_t TXHDB_ERR_MUTEX_TIMEDLOCK_TIMEOUT                                               = 0x00000405;/*1029*/
static const int32_t TXHDB_ERR_RWLOCK_TRYWRLOCK_BUSY                                                 = 0x00000505;/*1285*/
static const int32_t TXHDB_ERR_RWLOCK_TRYRDLOCK_BUSY                                                 = 0x00000605;/*1541*/
static const int32_t TXHDB_ERR_SPIN_TRYLOCK_BUSY                                                     = 0x00000705;/*1797*/
static const int32_t TXHDB_ERR_ITERATION_EXCEED_MAX_ALLOWED_TIME_OF_ONE_ITER                         = 0x00000805;/*2053*/
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


static const int32_t TXHDB_ERR_INVALID_ARGUMENTS                                                     = -0x00000105;/*-261*/
static const int32_t TXHDB_ERR_INVALID_MEMBER_VARIABLE_VALUE                                         = -0x00000205;/*-517*/
static const int32_t TXHDB_ERR_ALREADY_OPEN                                                          = -0x00000305;/*-773*/
static const int32_t TXHDB_ERR_MUTEX_LOCK_FAIL                                                       = -0x00000405;/*-1029*/
static const int32_t TXHDB_ERR_MUTEX_TRYLOCK_FAIL                                                    = -0x00000505;/*-1285*/
static const int32_t TXHDB_ERR_MUTEX_TIMEDLOCK_FAIL                                                  = -0x00000605;/*-1541*/
static const int32_t TXHDB_ERR_MUTEX_UNLOCK_FAIL                                                     = -0x00000705;/*-1797*/
static const int32_t TXHDB_ERR_RWLOCK_WRLOCK_FAIL                                                    = -0x00000805;/*-2053*/
static const int32_t TXHDB_ERR_RWLOCK_TRYWRLOCK_FAIL                                                 = -0x00000905;/*-2309*/
static const int32_t TXHDB_ERR_RWLOCK_RDLOCK_FAIL                                                    = -0x00000a05;/*-2565*/
static const int32_t TXHDB_ERR_RWLOCK_TRYRDLOCK_FAIL                                                 = -0x00000b05;/*-2821*/
static const int32_t TXHDB_ERR_RWLOCK_UNLOCK_FAIL                                                    = -0x00000c05;/*-3077*/
static const int32_t TXHDB_ERR_SPIN_LOCK_FAIL                                                        = -0x00000d05;/*-3333*/
static const int32_t TXHDB_ERR_SPIN_UNLOCK_FAIL                                                      = -0x00000e05;/*-3589*/
static const int32_t TXHDB_ERR_FILE_EXISTS_BUT_STATUS_ERROR                                          = -0x00000f05;/*-3845*/
static const int32_t TXHDB_ERR_FILE_OPEN_FAIL                                                        = -0x00001005;/*-4101*/
static const int32_t TXHDB_ERR_FILE_READ_SIZE_INVALID                                                = -0x00001105;/*-4357*/
static const int32_t TXHDB_ERR_FILE_INVALID_FILE_PATH                                                = -0x00001205;/*-4613*/
static const int32_t TXHDB_ERR_FILE_LOCK_FILE_FAIL                                                   = -0x00001305;/*-4869*/
static const int32_t TXHDB_ERR_FILE_NOT_A_REGULAR_FILE                                               = -0x00001405;/*-5125*/
static const int32_t TXHDB_ERR_FILE_MMAP_FAIL                                                        = -0x00001505;/*-5381*/
static const int32_t TXHDB_ERR_FILE_MUNMAP_FAIL                                                      = -0x00001605;/*-5637*/
static const int32_t TXHDB_ERR_FILE_CLOSE_FAIL                                                       = -0x00001705;/*-5893*/
static const int32_t TXHDB_ERR_FILE_SPACE_NOT_ENOUGH_IN_HEAD                                         = -0x00001805;/*-6149*/
static const int32_t TXHDB_ERR_FILE_FTRUNCATE_FAIL                                                   = -0x00001905;/*-6405*/
static const int32_t TXHDB_ERR_FILE_INCONSISTANT_FILE_SIZE                                           = -0x00001a05;/*-6661*/
static const int32_t TXHDB_ERR_FILE_MSIZ_LESSER_THAN_TXHDB_WHOLE_REC_OFFSET                          = -0x00001b05;/*-6917*/
static const int32_t TXHDB_ERR_FILE_MSIZ_CHANGE_NOT_PERMIT                                           = -0x00001c05;/*-7173*/
static const int32_t TXHDB_ERR_FILE_FSTAT_FAIL                                                       = -0x00001d05;/*-7429*/
static const int32_t TXHDB_ERR_FILE_MSYNC_FAIL                                                       = -0x00001e05;/*-7685*/
static const int32_t TXHDB_ERR_FILE_FSYNC_FAIL                                                       = -0x00001f05;/*-7941*/
static const int32_t TXHDB_ERR_FILE_FCNTL_LOCK_FILE_FAIL                                             = -0x00002005;/*-8197*/
static const int32_t TXHDB_ERR_FILE_FCNTL_UNLOCK_FILE_FAIL                                           = -0x00002105;/*-8453*/
static const int32_t TXHDB_ERR_FILE_PREAD_FAIL_WITH_SPECIFIED_ERRNO                                  = -0x00002205;/*-8709*/
static const int32_t TXHDB_ERR_FILE_PREAD_FAIL_WITH_UNSPECIFIED_ERRNO                                = -0x00002305;/*-8965*/
static const int32_t TXHDB_ERR_FILE_PWRITE_FAIL_WITH_SPECIFIED_ERRNO                                 = -0x00002405;/*-9221*/
static const int32_t TXHDB_ERR_FILE_PWRITE_FAIL_WITH_UNSPECIFIED_ERRNO                               = -0x00002505;/*-9477*/
static const int32_t TXHDB_ERR_FILE_READ_EXCEED_FILE_BOUNDARY                                        = -0x00002605;/*-9733*/
static const int32_t TXHDB_ERR_FILE_READ_FAIL_DURING_COPY                                            = -0x00002705;/*-9989*/
static const int32_t TXHDB_ERR_FILE_WRITE_FAIL_DURING_COPY                                           = -0x00002805;/*-10245*/
static const int32_t TXHDB_ERR_FILE_INVALID_FREE_BLOCK_POOL_METADATA                                 = -0x00002905;/*-10501*/
static const int32_t TXHDB_ERR_FILE_INVALID_MAGIC                                                    = -0x00002a05;/*-10757*/
static const int32_t TXHDB_ERR_FILE_INVALID_LIBRARY_VERSION                                          = -0x00002b05;/*-11013*/
static const int32_t TXHDB_ERR_FILE_INVALID_LIBRARY_REVISION                                         = -0x00002c05;/*-11269*/
static const int32_t TXHDB_ERR_FILE_INVALID_FORMAT_VERSION                                           = -0x00002d05;/*-11525*/
static const int32_t TXHDB_ERR_FILE_INVALID_EXTDATA_FORMAT_VERSION                                   = -0x00002e05;/*-11781*/
static const int32_t TXHDB_ERR_FILE_INVALID_DBTYPE                                                   = -0x00002f05;/*-12037*/
static const int32_t TXHDB_ERR_FILE_HEAD_CRC_UNMATCH                                                 = -0x00003005;/*-12293*/
static const int32_t TXHDB_ERR_FILE_INVALID_METADATA                                                 = -0x00003105;/*-12549*/
static const int32_t TXHDB_ERR_FILE_INVALID_HEADLEN                                                  = -0x00003205;/*-12805*/
static const int32_t TXHDB_ERR_FILE_DESERIAL_HEAD_SPACE_NOT_ENOUGH                                   = -0x00003305;/*-13061*/
static const int32_t TXHDB_ERR_FILE_SERIAL_HEAD_SPACE_NOT_ENOUGH                                     = -0x00003405;/*-13317*/
static const int32_t TXHDB_ERR_FILE_DESERIAL_STAT_SPACE_NOT_ENOUGH                                   = -0x00003505;/*-13573*/
static const int32_t TXHDB_ERR_FILE_SERIAL_STAT_SPACE_NOT_ENOUGH                                     = -0x00003605;/*-13829*/
static const int32_t TXHDB_ERR_FILE_SERIAL_FREE_BLOCK_LIST_INFO_WRONG_BUFFLEN                        = -0x00003705;/*-14085*/
static const int32_t TXHDB_ERR_FILE_IN_EXCEPTIONAL_STATUS                                            = -0x00003805;/*-14341*/
static const int32_t TXHDB_ERR_DB_NOT_OPENED                                                         = -0x00003905;/*-14597*/
static const int32_t TXHDB_ERR_DB_WRITE_NOT_PERMIT                                                   = -0x00003a05;/*-14853*/
static const int32_t TXHDB_ERR_INVALID_OFFSET_FROM_BUCKET                                            = -0x00003b05;/*-15109*/
static const int32_t TXHDB_ERR_READ_EXTDATA_EXCEED_BUFF_LENGTH                                       = -0x00003c05;/*-15365*/
static const int32_t TXHDB_ERR_WRITE_EXTDATA_EXCEED_BUFF_LENGTH                                      = -0x00003d05;/*-15621*/
static const int32_t TXHDB_ERR_FREE_BLOCK_IS_READ_WHEN_GETTING_RECORD                                = -0x00003e05;/*-15877*/
static const int32_t TXHDB_ERR_INVALID_KEY_DATABLOCK_NUM                                             = -0x00003f05;/*-16133*/
static const int32_t TXHDB_ERR_INVALID_VALUE_DATABLOCK_NUM                                           = -0x00004005;/*-16389*/
static const int32_t TXHDB_ERR_GET_RECORD_EXCEED_BUFF_LENGTH                                         = -0x00004105;/*-16645*/
static const int32_t TXHDB_ERR_COMPRESSION_FAIL                                                      = -0x00004205;/*-16901*/
static const int32_t TXHDB_ERR_DECOMPRESSION_FAIL                                                    = -0x00004305;/*-17157*/
static const int32_t TXHDB_ERR_INVALID_OFFSETINEXTDATA_AND_SIZE_WHEN_UPDATING_EXTDATA                = -0x00004405;/*-17413*/
static const int32_t TXHDB_ERR_UNEXPECTED_FREEBLOCK                                                  = -0x00004505;/*-17669*/
static const int32_t TXHDB_ERR_VALUE_APOW_LESSER_THAN_KEY_APOW                                       = -0x00004605;/*-17925*/
static const int32_t TXHDB_ERR_DUPLICATED_FILE_PATH                                                  = -0x00004705;/*-18181*/
static const int32_t TXHDB_ERR_INVALID_KEY_HEAD_SIZE_IN_TXHDB_META                                   = -0x00004805;/*-18437*/
static const int32_t TXHDB_ERR_INVALID_FILE_SIZE                                                     = -0x00004905;/*-18693*/
static const int32_t TXHDB_ERR_INVALID_FREE_BLOCK_SIZE                                               = -0x00004a05;/*-18949*/
static const int32_t TXHDB_ERR_MMAP_MEMSIZE_CHANGE_NOT_PERMITTED                                     = -0x00004b05;/*-19205*/
static const int32_t TXHDB_ERR_NEW_FILE_OBJ_FAIL                                                     = -0x00004c05;/*-19461*/
static const int32_t TXHDB_ERR_RECORD_KEY_OFFSET_LESSER_THAN_TXHDB_WHOLE_REC_OFFSET                  = -0x00004d05;/*-19717*/
static const int32_t TXHDB_ERR_RECORD_VALUE_OFFSET_LESSER_THAN_TXHDB_WHOLE_REC_OFFSET                = -0x00004e05;/*-19973*/
static const int32_t TXHDB_ERR_RECORD_OFFSET_LESSER_THAN_TXHDB_WHOLE_REC_OFFSET                      = -0x00004f05;/*-20229*/
static const int32_t TXHDB_ERR_KEY_BUFFSIZE_LESSER_THAN_KEY_HEADSIZE                                 = -0x00005005;/*-20485*/
static const int32_t TXHDB_ERR_VALUE_BUFFSIZE_LESSER_THAN_VALUE_HEADSIZE                             = -0x00005105;/*-20741*/
static const int32_t TXHDB_ERR_RECORD_SIZE_LESSER_THAN_KEY_HEADSIZE                                  = -0x00005205;/*-20997*/
static const int32_t TXHDB_ERR_INVALID_BLOCK_MAGIC                                                   = -0x00005305;/*-21253*/
static const int32_t TXHDB_ERR_INVALID_FREE_BLOCK_MAGIC                                              = -0x00005405;/*-21509*/
static const int32_t TXHDB_ERR_INVALID_KEYMAGIC                                                      = -0x00005505;/*-21765*/
static const int32_t TXHDB_ERR_INVALID_KEYSPLMAGIC                                                   = -0x00005605;/*-22021*/
static const int32_t TXHDB_ERR_INVALID_VALMAGIC                                                      = -0x00005705;/*-22277*/
static const int32_t TXHDB_ERR_INVALID_VALSPLMAGIC                                                   = -0x00005805;/*-22533*/
static const int32_t TXHDB_ERR_UNSUPPORTED_KEY_FORMAT_VERSION                                        = -0x00005905;/*-22789*/
static const int32_t TXHDB_ERR_UNSUPPORTED_KEY_SPLBLOCK_FORMAT_VERSION                               = -0x00005a05;/*-23045*/
static const int32_t TXHDB_ERR_UNSUPPORTED_VALUE_FORMAT_VERSION                                      = -0x00005b05;/*-23301*/
static const int32_t TXHDB_ERR_UNSUPPORTED_VALUE_SPLBLOCK_FORMAT_VERSION                             = -0x00005c05;/*-23557*/
static const int32_t TXHDB_ERR_UNSUPPORTED_FREE_BLOCK_FORMAT_VERSION                                 = -0x00005d05;/*-23813*/
static const int32_t TXHDB_ERR_KEY_HEAD_CRC_UNMATCH                                                  = -0x00005e05;/*-24069*/
static const int32_t TXHDB_ERR_KEY_SPLBLOCK_HEAD_CRC_UNMATCH                                         = -0x00005f05;/*-24325*/
static const int32_t TXHDB_ERR_VALUE_HEAD_CRC_UNMATCH                                                = -0x00006005;/*-24581*/
static const int32_t TXHDB_ERR_VALUE_SPLBLOCK_HEAD_CRC_UNMATCH                                       = -0x00006105;/*-24837*/
static const int32_t TXHDB_ERR_FREE_BLOCK_HEAD_CRC_UNMATCH                                           = -0x00006205;/*-25093*/
static const int32_t TXHDB_ERR_FREE_BLOCK_LIST_INFO_CRC_UNMATCH                                      = -0x00006305;/*-25349*/
static const int32_t TXHDB_ERR_GET_KEY_READ_BUFFER_FAIL                                              = -0x00006405;/*-25605*/
static const int32_t TXHDB_ERR_GET_VALUE_READ_BUFFER_FAIL                                            = -0x00006505;/*-25861*/
static const int32_t TXHDB_ERR_GET_LRU_VALUE_BUFFER_FAIL                                             = -0x00006605;/*-26117*/
static const int32_t TXHDB_ERR_GET_EXTDATA_READ_BUFFER_FAIL                                          = -0x00006705;/*-26373*/
static const int32_t TXHDB_ERR_KEY_BLOCK_BODYSIZE_GREATER_THAN_KEY_BODYSIZE                          = -0x00006805;/*-26629*/
static const int32_t TXHDB_ERR_VALUE_BLOCK_BODYSIZE_GREATER_THAN_VALUE_BODYSIZE                      = -0x00006905;/*-26885*/
static const int32_t TXHDB_ERR_NULL_RECORD_POINTER                                                   = -0x00006a05;/*-27141*/
static const int32_t TXHDB_ERR_NULL_RECORD_WRITE_BUFF                                                = -0x00006b05;/*-27397*/
static const int32_t TXHDB_ERR_SERIALIZE_RECORD_KEY_HEAD                                             = -0x00006c05;/*-27653*/
static const int32_t TXHDB_ERR_INVALID_IDX_IN_STAT_NUMS_ARRAY                                        = -0x00006d05;/*-27909*/
static const int32_t TXHDB_ERR_INVALID_ELEMNUM_OF_STAT_KEYNUMS                                       = -0x00006e05;/*-28165*/
static const int32_t TXHDB_ERR_INVALID_ELEMNUM_OF_STAT_VALNUMS                                       = -0x00006f05;/*-28421*/
static const int32_t TXHDB_ERR_PRINT_SPACE_NOT_ENOUGH                                                = -0x00007005;/*-28677*/
static const int32_t TXHDB_ERR_LRU_SHIFTIN_NOT_ENOUGH_MEMORY                                         = -0x00007105;/*-28933*/
static const int32_t TXHDB_ERR_LRU_SHIFTIN_NO_MORE_LRU_NODE                                          = -0x00007205;/*-29189*/
static const int32_t TXHDB_ERR_LRU_ADJUST_NO_MORE_LRU_NODE                                           = -0x00007305;/*-29445*/
static const int32_t TXHDB_ERR_LRU_SHIFTOUT_RECORD_ALREADY_OUTSIDE_OF_MEMORY                         = -0x00007405;/*-29701*/
static const int32_t TXHDB_ERR_FILE_EXTDATA_LENGTH_CRC_UNMATCH                                       = -0x00007505;/*-29957*/
static const int32_t TXHDB_ERR_FILE_EXTDATA_INVALID_LENGTH                                           = -0x00007605;/*-30213*/
static const int32_t TXHDB_ERR_INVALID_VALUE_HEAD_SIZE_IN_TXHDB_META                                 = -0x00007705;/*-30469*/
static const int32_t TXHDB_ERR_INVALID_SPLITDATABLOCK_HEAD_SIZE_IN_TXHDB_META                        = -0x00007805;/*-30725*/
static const int32_t TXHDB_ERR_KEY_BUCKETIDX_UNMATCH                                                 = -0x00007905;/*-30981*/
static const int32_t TXHDB_ERR_FILE_WRITE_SIZE_INVALID                                               = -0x00007a05;/*-31237*/
static const int32_t TXHDB_ERR_MODIFY_STAT_UNSUPPORTED_OPERATION_TYPE                                = -0x00007b05;/*-31493*/
static const int32_t TXHDB_ERR_INVALID_EXTDATAMAGIC                                                  = -0x00007c05;/*-31749*/
static const int32_t TXHDB_ERR_INVALID_INTERNAL_LIST_TAIL_DURING_POP_LRU_NODELIST                    = -0x00007d05;/*-32005*/
static const int32_t TXHDB_ERR_GET_LRUNODE_FAIL           								             = -0x00007e05;/*-32261*/
static const int32_t TXHDB_ERR_LRUNODE_INVALID_FLAG        								             = -0x00007f05;/*-32517*/
static const int32_t TXHDB_ERR_INVALID_FREE_BLOCK_NUM_TOO_MANY_FREE_BLOCKS                           = -0x00008005;/*-32773*/
static const int32_t TXHDB_ERR_INVALID_ELEMNUM_OF_STAT_NOPADDING_SIZE_KEYNUMS                        = -0x00008105;/*-33029*/
static const int32_t TXHDB_ERR_INVALID_ELEMNUM_OF_STAT_NOPADDING_SIZE_VALNUMS                        = -0x00008205;/*-33285*/
static const int32_t TXHDB_ERR_ADD_LSIZE_EXCEEDS_MAX_TSD_VALUE_BUFF_SIZE                             = -0x00008305;/*-33541*/
static const int32_t TXHDB_ERR_INTERNAL_CONSTANTS_ILLEGAL                                            = -0x00008405;/*-33797*/
static const int32_t TXHDB_ERR_TOO_BIG_KEY_BIZ_SIZE                                                  = -0x00008505;/*-34053*/
static const int32_t TXHDB_ERR_TOO_BIG_VALUE_BIZ_SIZE                                                = -0x00008605;/*-34309*/
static const int32_t TXHDB_ERR_INDEX_NO_EXIST                                                        = -0x00008705;/*-34565*/
static const int32_t TXHDB_ERR_INVALID_FREE_BLOCK_BASESIZE                                           = -0x00008805;/*-34821*/
static const int32_t TXHDB_ERR_CANNOT_CREATE_MMAPSHM_BECAUSE_SHM_ALREADY_EXISTED                     = -0x00008905;/*-35077*/
static const int32_t TXHDB_ERR_INVALID_GENSHM_KEY                                                    = -0x00008a05;/*-35333*/
static const int32_t TXHDB_ERR_GENSHM_GET_FAIL                                                       = -0x00008b05;/*-35589*/
static const int32_t TXHDB_ERR_GENSHM_CREATE_FAIL                                                    = -0x00008c05;/*-35845*/
static const int32_t TXHDB_ERR_GENSHM_STAT_FAIL                                                      = -0x00008d05;/*-36101*/
static const int32_t TXHDB_ERR_GENSHM_DOES_NOT_EXIST                                                 = -0x00008e05;/*-36357*/
static const int32_t TXHDB_ERR_GENSHM_ATTACH_FAIL_BECAUSE_IT_IS_ALREADY_ATTACHED_BY_OTHER_PROCESSES  = -0x00008f05;/*-36613*/
static const int32_t TXHDB_ERR_GENSHM_ATTACH_FAIL                                                    = -0x00009005;/*-36869*/
static const int32_t TXHDB_ERR_FILE_INCONSISTANT_MSIZE                                               = -0x00009105;/*-37125*/
static const int32_t TXHDB_ERR_INVALID_TCAP_GENSHM_MAGIC                                             = -0x00009205;/*-37381*/
static const int32_t TXHDB_ERR_GENSHM_FIXED_HEAD_BUFFLEN_UNMATCH                                     = -0x00009305;/*-37637*/
static const int32_t TXHDB_ERR_GENSHM_INVALID_HEADLEN                                                = -0x00009405;/*-37893*/
static const int32_t TXHDB_ERR_GENSHM_HEAD_CRC_UNMATCH                                               = -0x00009505;/*-38149*/
static const int32_t TXHDB_ERR_GENSHM_HEAD_INVALID_VERSION                                           = -0x00009605;/*-38405*/
static const int32_t TXHDB_ERR_GENSHM_INVALID_FILETYPE                                               = -0x00009705;/*-38661*/
static const int32_t TXHDB_ERR_GET_IPV4ADDR_FAIL                                                     = -0x00009805;/*-39429*/
static const int32_t TXHDB_ERR_NO_VALID_IPV4ADDR_EXISTS                                              = -0x00009905;/*-39173*/
static const int32_t TXHDB_ERR_TRANSFER_IPV4ADDR_FAIL                                                = -0x00009a05;/*-39429*/
static const int32_t TXHDB_ERR_FILE_EXCEEDS_LSIZE_LIMIT                                              = -0x00009b05;/*-39685*/
static const int32_t TXHDB_ERR_GENSHM_DETACH_FAIL                                                    = -0x00009c05;/*-39941*/
static const int32_t TXHDB_ERR_TXHDB_HEAD_PARAMETERS_ERROR                                           = -0x00009d05;/*-40197*/
static const int32_t TXHDB_ERR_TXHDB_HEAD_OLD_VERSION                                                = -0x00009e05;/*-40453*/
static const int32_t TXHDB_ERR_TXHDB_SHM_COREINFO_UNMATCH                                            = -0x00009f05;/*-40709*/
static const int32_t TXHDB_ERR_TXHDB_SHM_EXTDATA_UNMATCH                                             = -0x0000a005;/*-40965*/
static const int32_t TXHDB_ERR_TXHDB_EXTDATA_CHECK_ERROR                                             = -0x0000a105;/*-41221*/
static const int32_t TXHDB_ERR_CHUNK_BUFFS_CANNOT_BE_ALLOCED_IF_THEY_ARE_NOT_RELEASED                = -0x0000a205;/*-41477*/
static const int32_t TXHDB_ERR_ALLOCATE_MEMORY_FAIL                                                  = -0x0000a305;/*-41733*/
static const int32_t TXHDB_ERR_INVALID_CHUNK_RW_MANNER                                               = -0x0000a405;/*-41989*/
static const int32_t TXHDB_ERR_FILE_PREAD_NOT_COMPLETE                                               = -0x0000a505;/*-42245*/
static const int32_t TXHDB_ERR_FILE_PWRITE_NOT_COMPLETE                                              = -0x0000a605;/*-42501*/
static const int32_t TXHDB_ERR_KEY_ONEBLOCK_BUT_NEXT_NOTNULL                                         = -0x0000a705;/*-42757*/
static const int32_t TXHDB_ERR_VALUE_ONEBLOCK_BUT_NEXT_NOTNULL                                       = -0x0000a805;/*-43013*/
static const int32_t TXHDB_ERR_VARINT_FORMAT_ERROR                                                   = -0x0000a905;/*-43269*/
static const int32_t TXHDB_ERR_TXSTAT_ERROR                                                          = -0x0000aa05;/*-43525*/
static const int32_t TXHDB_ERR_INVALID_VERSION 													     = -0x0000ab05;/*-43781*/
static const int32_t TXHDB_ERR_FREE_BLOCK_NOT_ENOUGH                                                 = -0x0000ac05;/*-44037*/



//Engine BUSINESS (module id 0x06) Error Code defined below 
//......

//Engine SYSTEM (module id 0x07) Error Code defined below 
static const int32_t ENG_ERR_INVALID_ARGUMENTS                                                       = -0x00000107;/*-263*/
static const int32_t ENG_ERR_INVALID_MEMBER_VARIABLE_VALUE                                           = -0x00000207;/*-519*/
static const int32_t ENG_ERR_NEW_TXHCURSOR_FAILED                                                    = -0x00000307;/*-775*/
static const int32_t ENG_ERR_TXHCURSOR_KEY_BUFFER_LEGHTH_NOT_ENOUGH                                  = -0x00000407;/*-1031*/
static const int32_t ENG_ERR_TXHCURSOR_VALUE_BUFFER_LEGHTH_NOT_ENOUGH                                = -0x00000507;/*-1287*/
static const int32_t ENG_ERR_TXHDB_FILEPATH_NULL                                                     = -0x00000607;/*-1543*/
static const int32_t ENG_ERR_TCHDB_RELATED_ERROR                                                     = -0x00000707;/*-1799*/
static const int32_t ENG_ERR_NULL_CACHE                                                              = -0x00000807;/*-2055*/
static const int32_t ENG_ERR_ITER_FAIL_SYSTEM_RECORD 												 = -0x00000907;/*-2311*/
static const int32_t ENG_ERR_SYSTEM_ERROR            												 = -0x00000a07;/*-2567*/
static const int32_t ENG_ERR_ENGINE_ERROR 															 = -0x00000b07;/*-2823*/
static const int32_t ENG_ERR_DATA_ERROR            												     = -0x00000c07;/*-3079*/
static const int32_t ENG_ERR_VERSION_ERROR															 = -0x00000d07;/*-3335*/
static const int32_t ENG_ERR_SYSTEM_ERROR_BUFF_OVERFLOW           									 = -0x00000e07;/*-3591*/
static const int32_t ENG_ERR_METADATA_ERROR 														 = -0x00000f07;/*-3847*/
static const int32_t ENG_ERR_ADD_KEYMETA_FAILED            										     = -0x00001007;/*-4103*/
static const int32_t ENG_ERR_ADD_VALUEMETA_FAILED 													 = -0x00001107;/*-4359*/
static const int32_t ENG_ERR_RESERVED_FIELDNAME           											 = -0x00001207;/*-4615*/
static const int32_t ENG_ERR_KEYNAME_REPEAT 														 = -0x00001307;/*-4871*/
static const int32_t ENG_ERR_VALUENAME_REPEAT            											 = -0x00001407;/*-5127*/
static const int32_t ENG_ERR_MISS_KEYMETA            												 = -0x00001507;/*-5383*/
static const int32_t ENG_ERR_DELETE_KEYFIELD 														 = -0x00001607;/*-5639*/
static const int32_t ENG_ERR_CHANGE_KEYCOUNT           												 = -0x00001707;/*-5895*/
static const int32_t ENG_ERR_CHANGE_KEYTYPE 														 = -0x00001807;/*-6151*/
static const int32_t ENG_ERR_CHANGE_KEYLENGTH           										     = -0x00001907;/*-6407*/
static const int32_t ENG_ERR_CHANGE_VALUETYPE 													     = -0x00001a07;/*-6663*/
static const int32_t ENG_ERR_CHANGE_VALUELENGTH            							                 = -0x00001b07;/*-6919*/
static const int32_t ENG_ERR_CHANGE_DEFAULTVALUE            										 = -0x00001c07;/*-7175*/
static const int32_t ENG_ERR_EMPTY_FIELDNAME 														 = -0x00001d07;/*-7431*/
static const int32_t ENG_ERR_INVALID_TARGET_KEYFIELD           										 = -0x00001e07;/*-7687*/
static const int32_t ENG_ERR_INVALID_TARGET_VALUEFIELD 												 = -0x00001f07;/*-7943*/
static const int32_t ENG_ERR_INVALID_TABLE_TYPE            											 = -0x00002007;/*-8199*/
static const int32_t ENG_ERR_CHANGE_TABLE_TYPE 														 = -0x00002107;/*-8455*/
static const int32_t ENG_ERR_MISS_VALUEMETA           												 = -0x00002207;/*-8711*/
static const int32_t ENG_ERR_NOT_ENOUGH_BUFF_FOR_FILEPATH           								 = -0x00002307;/*-8967*/
static const int32_t ENG_ERR_ENGINE_FILE_NOT_FOUND                                                   = -0x00002407;/*-9223*/

//ULOG BUSINESS (module id 0x08) Error Code defined below 
//......

//ULOG SYSTEM (module id 0x09) Error Code defined below 
//
static const int32_t ULOG_ERR_INVALID_PARAMS                                                         = -0x00000109;/*-265*/

//SYNCDB BUSINESS (module id 0x0a) Error Code defined below 
//......

//SYNCDB SYSTEM (module id 0x0b) Error Code defined below 
static const int32_t SYNCDB_ERR_INVALID_PARAMS                                                       = -0x0000010b;/*-267*/

//TCAPSVR BUSINESS (module id 0x0c) Error String defined below 
//......

//TCAPSVR SYSTEM (module id 0x0d) Error Code defined below 
static const int32_t SVR_ERR_FAIL_ROUTE          				     								 = -0x0000010d;/*-269*/
static const int32_t SVR_ERR_FAIL_TIMEOUT          													 = -0x0000020d;/*-525*/
static const int32_t SVR_ERR_FAIL_SHORT_BUFF          				     							 = -0x0000030d;/*-781*/
static const int32_t SVR_ERR_FAIL_SYSTEM_BUSY          												 = -0x0000040d;/*-1037*/
static const int32_t SVR_ERR_FAIL_RECORD_EXIST          				     					     = -0x0000050d;/*-1293*/
static const int32_t SVR_ERR_FAIL_INVALID_FIELD_NAME          										 = -0x0000060d;/*-1549*/
static const int32_t SVR_ERR_FAIL_VALUE_OVER_MAX_LEN          				     					 = -0x0000070d;/*-1805*/
static const int32_t SVR_ERR_FAIL_INVALID_FIELD_TYPE          										 = -0x0000080d;/*-2061*/
static const int32_t SVR_ERR_FAIL_SYNC_WRITE          				     							 = -0x0000090d;/*-2317*/
static const int32_t SVR_ERR_FAIL_WRITE_RECORD          											 = -0x00000a0d;/*-2573*/
static const int32_t SVR_ERR_FAIL_DELETE_RECORD          				     						 = -0x00000b0d;/*-2829*/
static const int32_t SVR_ERR_FAIL_DATA_ENGINE          												 = -0x00000c0d;/*-3085*/
static const int32_t SVR_ERR_FAIL_RESULT_OVERFLOW          											 = -0x00000d0d;/*-3341*/
static const int32_t SVR_ERR_FAIL_INVALID_OPERATION          				     					 = -0x00000e0d;/*-3597*/
static const int32_t SVR_ERR_FAIL_INVALID_SUBSCRIPT          										 = -0x00000f0d;/*-3853*/
static const int32_t SVR_ERR_FAIL_INVALID_INDEX          				     						 = -0x0000100d;/*-4109*/
static const int32_t SVR_ERR_FAIL_OVER_MAXE_FIELD_NUM          										 = -0x0000110d;/*-4365*/
static const int32_t SVR_ERR_FAIL_MISS_KEY_FIELD          				     					     = -0x0000120d;/*-4621*/
static const int32_t SVR_ERR_FAIL_NEED_SIGNUP          												 = -0x0000130d;/*-4877*/
static const int32_t SVR_ERR_FAIL_CROSS_AUTH         												 = -0x0000140d;/*-5133*/
static const int32_t SVR_ERR_FAIL_SIGNUP_FAIL          				     							 = -0x0000150d;/*-5389*/
static const int32_t SVR_ERR_FAIL_SIGNUP_INVALID          											 = -0x0000160d;/*-5645*/
static const int32_t SVR_ERR_FAIL_SIGNUP_INIT          				     							 = -0x0000170d;/*-5901*/
static const int32_t SVR_ERR_FAIL_LIST_FULL          												 = -0x0000180d;/*-6157*/
static const int32_t SVR_ERR_FAIL_LOW_VERSION          				     							 = -0x0000190d;/*-6412*/
static const int32_t SVR_ERR_FAIL_HIGH_VERSION          											 = -0x00001a0d;/*-6669*/
static const int32_t SVR_ERR_FAIL_INVALID_RESULT_FLAG         										 = -0x00001b0d;/*-6925*/
static const int32_t SVR_ERR_FAIL_PROXY_STOPPING          				     						 = -0x00001c0d;/*-7181*/
static const int32_t SVR_ERR_FAIL_SVR_READONLY          											 = -0x00001d0d;/*-7437*/
static const int32_t SVR_ERR_FAIL_SVR_READONLY_BECAUSE_IN_SLAVE_MODE         					     = -0x00001e0d;/*-7693*/
static const int32_t SVR_ERR_FAIL_INVALID_VERSION 													 = -0x00001f0d;/*-7949*/
static const int32_t SVR_ERR_FAIL_SYSTEM_ERROR 														 = -0x0000200d;/*-8205*/
static const int32_t SVR_ERR_FAIL_OVERLOAD 														     = -0x0000210d;/*-8461*/
static const int32_t SVR_ERR_FAIL_NOT_ENOUGH_DADADISK_SPACE          								 = -0x0000220d;/*-8717*/
static const int32_t SVR_ERR_FAIL_NOT_ENOUGH_ULOGDISK_SPACE          								 = -0x0000230d;/*-8973*/
static const int32_t SVR_ERR_FAIL_UNSUPPORTED_PROTOCOL_MAGIC           								 = -0x0000240d;/*-9229*/
static const int32_t SVR_ERR_FAIL_UNSUPPORTED_PROTOCOL_CMD             								 = -0x0000250d;/*-9485*/
static const int32_t SVR_ERR_FAIL_HIGH_TABLE_META_VERSION             								 = -0x0000260d;/*-9741*/
static const int32_t SVR_ERR_FAIL_MERGE_VALUE_FIELD                 								 = -0x0000270d;/*-9997*/
static const int32_t SVR_ERR_FAIL_CUT_VALUE_FIELD                   								 = -0x0000280d;/*-10253*/
static const int32_t SVR_ERR_FAIL_PACK_FIELD                        								 = -0x0000290d;/*-10509*/
static const int32_t SVR_ERR_FAIL_UNPACK_FIELD                        								 = -0x00002a0d;/*-10765*/
static const int32_t SVR_ERR_FAIL_LOW_API_VERSION                     								 = -0x00002b0d;/*-11021*/
static const int32_t SVR_ERR_COMMAND_AND_TABLE_TYPE_IS_MISMATCH                     				 = -0x00002c0d;/*-11277*/
static const int32_t SVR_ERR_FAIL_TO_FIND_CACHE                                  				     = -0x00002d0d;/*-11533*/
static const int32_t SVR_ERR_FAIL_TO_FIND_META                                  				     = -0x00002e0d;/*-11789*/
static const int32_t SVR_ERR_FAIL_TO_GET_CURSOR                                  				     = -0x00002f0d;/*-12045*/
static const int32_t SVR_ERR_FAIL_OUT_OF_USER_DEF_RANGE                                              = -0x0000300d;/*-12301*/
static const int32_t SVR_ERR_INVALID_ARGUMENTS                                                       = -0x0000310d;/*-12557*/
static const int32_t SVR_ERR_SLAVE_READ_INVALID                                                      = -0x0000320d;/*-12813*/
static const int32_t SVR_ERR_NULL_CACHE                                                              = -0x0000330d;/*-13069*/
static const int32_t SVR_ERR_NULL_CURSOR                                                             = -0x0000340d;/*-13325*/
static const int32_t SVR_ERR_METALIB_VERSION_LESS_THAN_ENTRY_VERSION                                 = -0x0000350d;/*-13581*/
static const int32_t SVR_ERR_INVALID_SELECT_ID_FOR_UNION                                             = -0x0000360d;/*-13837*/
static const int32_t SVR_ERR_CAN_NOT_FIND_SELECT_ENTRY_FOR_UNION                                     = -0x0000370d;/*-14093*/
static const int32_t SVR_ERR_FAIL_DOCUMENT_PACK_VERSION                                              = -0x0000380d;/*-14349*/
static const int32_t SVR_ERR_TCAPSVR_PROCESS_NOT_NORMAL                                              = -0x0000390d;/*-14605*/
static const int32_t SVR_ERR_TBUSD_PROCESS_NOT_NORMAL                                                = -0x00003a0d;/*-14861*/
static const int32_t SVR_ERR_INVALID_ARRAY_COUNT                                                     = -0x00003b0d;/*-15117*/
static const int32_t SVR_ERR_REJECT_REQUEST_BECAUSE_ROUTE_IN_REJECT_STATUS                           = -0x00003c0d;/*-15373*/
static const int32_t SVR_ERR_FAIL_GET_ROUTE_HASH_CODE                                                = -0x00003d0d;/*-15629*/
static const int32_t SVR_ERR_FAIL_INVALID_FIELD_VALUE          										 = -0x00003e0d;/*-15885*/
static const int32_t SVR_ERR_FAIL_PROTOBUF_FIELD_GET         										 = -0x00003f0d;/*-16141*/
static const int32_t SVR_ERR_FAIL_PROTOBUF_VALUE_BUFF_EXCEED         							     = -0x0000400d;/*-16397*/
static const int32_t SVR_ERR_FAIL_PROTOBUF_FIELD_UPDATE         							         = -0x0000410d;/*-16653*/
static const int32_t SVR_ERR_FAIL_PROTOBUF_FIELD_INCREASE         							         = -0x0000420d;/*-16909*/
static const int32_t SVR_ERR_FAIL_PROTOBUF_FIELD_TAG_MISMATCH     							         = -0x0000430d;/*-17165*/
static const int32_t SVR_ERR_FAIL_BINLOG_SEQUENCE_TOO_SMALL     							         = -0x0000440d;
static const int32_t SVR_ERR_FAIL_SVR_IS_NOT_MASTER     							        		 = -0x0000450d;
static const int32_t SVR_ERR_FAIL_BINLOG_INVALID_FILE_PATH         							         = -0x0000460d;
static const int32_t SVR_ERR_FAIL_BINLOG_SOCKET_SEND_BUFF_IS_FULL       							 = -0x0000470d;




//TCAPDB BUSINESS (module id 0x0e) Error Code defined below
//......

//TCAPDB SYSTEM (module id 0x0f) Error Code defined below 
static const int32_t TCAPDB_ERR_INVALID_PARAMS                                                       = -0x0000010f;/*-271*/

//TCAPROXY BUSINESS (module id 0x10) Error String defined below 
//......

//TCAPROXY SYSTEM (module id 0x11) Error String defined below 
static const int32_t PROXY_ERR_INVALID_PARAMS                                                        = -0x00000111;/*-273*/
static const int32_t PROXY_ERR_NO_NEED_ROUTE_BATCHGET_ACTION_MSG_WHEN_NODE_IS_IN_SYNC_STATUS         = -0x00000211;/*-529*/
static const int32_t PROXY_ERR_NO_NEED_ROUTE_WHEN_NODE_IS_IN_REJECT_STATUS                           = -0x00000311;/*-785*/
static const int32_t PROXY_ERR_PROBE_TIMEOUT                                                         = -0x00000411;/*-1041*/
static const int32_t PROXY_ERR_SYSTEM_ERROR                                                          = -0x00000511;/*-1297*/
static const int32_t PROXY_ERR_CONFIG_ERROR                                                          = -0x00000611;/*-1553*/
static const int32_t PROXY_ERR_OVER_MAX_NODE                                                         = -0x00000711;/*-1809*/
static const int32_t PROXY_ERR_INVALID_SPLIT_SIZE                                                    = -0x00000811;/*-2065*/
static const int32_t PROXY_ERR_INVALID_ROUTE_INDEX                                                   = -0x00000911;/*-2321*/
static const int32_t PROXY_ERR_CONNECT_SERVER                                                        = -0x00000a11;/*-2577*/
static const int32_t PROXY_ERR_COMPOSE_MSG                                                           = -0x00000b11;/*-2833*/
static const int32_t PROXY_ERR_ROUTE_MSG                                                             = -0x00000c11;/*-3089*/
static const int32_t PROXY_ERR_SHORT_BUFFER                                                          = -0x00000d11;/*-3345*/
static const int32_t PROXY_ERR_OVER_MAX_RECORD                                                       = -0x00000e11;/*-3601*/
static const int32_t PROXY_ERR_INVALID_SERVICE_TABLE                                                 = -0x00000f11;/*-3857*/
static const int32_t PROXY_ERR_REGISTER_FAILED                                                       = -0x00001011;/*-4113*/
static const int32_t PROXY_ERR_CREATE_SESSION_HASH                                                   = -0x00001111;/*-4369*/
static const int32_t PROXY_ERR_WRONG_STATUS                                                          = -0x00001211;/*-4625*/
static const int32_t PROXY_ERR_UNPACK_MSG                                                            = -0x00001311;/*-4881*/
static const int32_t PROXY_ERR_PACK_MSG                                                              = -0x00001411;/*-5137*/
static const int32_t PROXY_ERR_SEND_MSG                                                              = -0x00001511;/*-5393*/
static const int32_t PROXY_ERR_ALLOCATE_MEMORY                                                       = -0x00001611;/*-5649*/
static const int32_t PROXY_ERR_PARSE_MSG                                                             = -0x00001711;/*-5905*/
static const int32_t PROXY_ERR_INVALID_MSG                                                           = -0x00001811;/*-6161*/
static const int32_t PROXY_ERR_FAILED_PROC_REQUEST_BECAUSE_NODE_IS_IN_SYNC_STASUS                    = -0x00001911;/*-6417*/
static const int32_t PROXY_ERR_KEY_FIELD_NUM_IS_ZERO                                                 = -0x00001a11;/*-6673*/
static const int32_t PROXY_ERR_LACK_OF_SOME_KEY_FIELDS                                               = -0x00001b11;/*-6929*/
static const int32_t PROXY_ERR_FAILED_TO_FIND_NODE                                                   = -0x00001c11;/*-7185*/
static const int32_t PROXY_ERR_INVALID_COMPRESS_TYPE                                                 = -0x00001d11;/*-7441*/
static const int32_t PROXY_ERR_REQUEST_OVERSPEED                                                     = -0x00001e11;/*-7697*/
static const int32_t PROXY_ERR_SWIFT_TIMEOUT                                                         = -0x00001f11;/*-7953*/
static const int32_t PROXY_ERR_SWIFT_ERROR                                                           = -0x00002011;/*-8209*/
static const int32_t PROXY_ERR_DIRECT_RESPONSE                                                       = -0x00002111;/*-8465*/
static const int32_t PROXY_ERR_INIT_TLOG                                                             = -0x00002211;/*-8721*/
static const int32_t PROXY_ERR_ASSISTANT_THREAD_NOT_RUN                                              = -0x00002311;/*-8977*/
static const int32_t PROXY_ERR_REQUEST_ACCESS_CTRL_REJECT                                            = -0x00002411;/*-9233*/
static const int32_t PROXY_ERR_NOT_ALL_NODES_ARE_IN_NORMAL_OR_WAIT_STATUS                            = -0x00002511;/*-9489*/
static const int32_t PROXY_ERR_ALREADY_CACHED_REQUEST_TIMEOUT                                        = -0x00002611;
static const int32_t PROXY_ERR_FAILED_TO_CACHE_REQUEST                                               = -0x00002711;
static const int32_t PROXY_ERR_NOT_EXIST_CACHED_REQUEST                                              = -0x00002811;
static const int32_t PROXY_ERR_FAILED_NOT_ENOUGH_CACHE_BUFF                                          = -0x00002911;
static const int32_t PROXY_ERR_FAILED_PROCESS_CACHED_REQUEST                                         = -0x00002a11;
static const int32_t PROXY_ERR_SYNC_ROUTE_HAS_BEEN_CANCELLED                                         = -0x00002b11;
static const int32_t PROXY_ERR_FAILED_LOCK_CACHE                                                     = -0x00002c11;


//API BUSINESS (module id 0x12) Error Code defined below
//......

//API SYSTEM (module id 0x13) Error Code defined below 
static const int32_t API_ERR_OVER_MAX_KEY_FIELD_NUM                  								 = -0x00000113;/*-275*/
static const int32_t API_ERR_OVER_MAX_VALUE_FIELD_NUM               								 = -0x00000213;/*-531*/
static const int32_t API_ERR_OVER_MAX_FIELD_NAME_LEN                								 = -0x00000313;/*-787*/
static const int32_t API_ERR_OVER_MAX_FIELD_VALUE_LEN           									 = -0x00000413;/*-1043*/
static const int32_t API_ERR_FIELD_NOT_EXSIST         												 = -0x00000513;/*-1299*/
static const int32_t API_ERR_FIELD_TYPE_NOT_MATCH          											 = -0x00000613;/*-1555*/
static const int32_t API_ERR_PARAMETER_INVALID           											 = -0x00000713;/*-1811*/
static const int32_t API_ERR_OPERATION_TYPE_NOT_MATCH         										 = -0x00000813;/*-2067*/
static const int32_t API_ERR_PACK_MESSAGE         												     = -0x00000913;/*-2323*/
static const int32_t API_ERR_UNPACK_MESSAGE           												 = -0x00000a13;/*-2579*/
static const int32_t API_ERR_PACKAGE_NOT_UNPACKED         											 = -0x00000b13;/*-2835*/
static const int32_t API_ERR_OVER_MAX_RECORD_NUM         											 = -0x00000c13;/*-3091*/
static const int32_t API_ERR_INVALID_COMMAND           												 = -0x00000d13;/*-3347*/
static const int32_t API_ERR_NO_MORE_RECORD         												 = -0x00000e13;/*-3603*/
static const int32_t API_ERR_OVER_KEY_FIELD_NUM          											 = -0x00000f13;/*-3859*/
static const int32_t API_ERR_OVER_VALUE_FIELD_NUM           										 = -0x00001013;/*-4115*/
static const int32_t API_ERR_OBJ_NEED_INIT         													 = -0x00001113;/*-4371*/
static const int32_t API_ERR_INVALID_DATA_SIZE          											 = -0x00001213;/*-4627*/
static const int32_t API_ERR_INVALID_ARRAY_COUNT           											 = -0x00001313;/*-4883*/
static const int32_t API_ERR_INVALID_UNION_SELECT          											 = -0x00001413;/*-5139*/
static const int32_t API_ERR_MISS_PRIMARY_KEY          												 = -0x00001513;/*-5395*/
static const int32_t API_ERR_UNSUPPORT_FIELD_TYPE           										 = -0x00001613;/*-5651*/
static const int32_t API_ERR_ARRAY_BUFFER_IS_SMALL         											 = -0x00001713;/*-5907*/
static const int32_t API_ERR_IS_NOT_WHOLE_PACKAGE          											 = -0x00001813;/*-6163*/
static const int32_t API_ERR_MISS_PAIR_FIELD           												 = -0x00001913;/*-6419*/
static const int32_t API_ERR_GET_META_ENTRY          												 = -0x00001a13;/*-6675*/
static const int32_t API_ERR_GET_ARRAY_META          												 = -0x00001b13;/*-6931*/
static const int32_t API_ERR_GET_ENTRY_META           												 = -0x00001c13;/*-7187*/
static const int32_t API_ERR_INCOMPATIBLE_META         												 = -0x00001d13;/*-7443*/
static const int32_t API_ERR_PACK_ARRAY_DATA          												 = -0x00001e13;/*-7669*/
static const int32_t API_ERR_PACK_UNION_DATA          												 = -0x00001f13;/*-7955*/
static const int32_t API_ERR_PACK_STRUCT_DATA          												 = -0x00002013;/*-8211*/
static const int32_t API_ERR_UNPACK_ARRAY_DATA          											 = -0x00002113;/*-8467*/
static const int32_t API_ERR_UNPACK_UNION_DATA           											 = -0x00002213;/*-8723*/
static const int32_t API_ERR_UNPACK_STRUCT_DATA         											 = -0x00002313;/*-8979*/
static const int32_t API_ERR_INVALID_INDEX_NAME          											 = -0x00002413;/*-9235*/
static const int32_t API_ERR_MISS_PARTKEY_FIELD          											 = -0x00002513;/*-9491*/
static const int32_t API_ERR_ALLOCATE_MEMORY          												 = -0x00002613;/*-9747*/
static const int32_t API_ERR_GET_META_SIZE          												 = -0x00002713;/*-10003*/
static const int32_t API_ERR_MISS_BINARY_VERSION           											 = -0x00002813;/*-10259*/
static const int32_t API_ERR_INVALID_INCREASE_FIELD         										 = -0x00002913;/*-10515*/
static const int32_t API_ERR_INVALID_RESULT_FLAG          											 = -0x00002a13;/*-10771*/
static const int32_t API_ERR_OVER_MAX_LIST_INDEX_NUM          										 = -0x00002b13;/*-11027*/
static const int32_t API_ERR_INVALID_OBJ_STATUE          											 = -0x00002c13;/*-11283*/
static const int32_t API_ERR_INVALID_REQUEST          												 = -0x00002d13;/*-11539*/
static const int32_t API_ERR_INVALID_SHARD_LIST           											 = -0x00002e13;/*-11795*/
static const int32_t API_ERR_TABLE_NAME_MISSING         											 = -0x00002f13;/*-12051*/
static const int32_t API_ERR_SOCKET_SEND_BUFF_IS_FULL          										 = -0x00003013;/*-12307*/
static const int32_t API_ERR_INVALID_MAGIC          												 = -0x00003113;/*-12563*/
static const int32_t API_ERR_TABLE_IS_NOT_EXIST          											 = -0x00003213;/*-12819*/
static const int32_t API_ERR_SHORT_BUFF                 											 = -0x00003313;/*-13075*/
static const int32_t API_ERR_FLOW_CONTROL                 											 = -0x00003413;/*-13331*/
static const int32_t API_ERR_COMPRESS_SWITCH_NOT_SUPPORTED_REGARDING_THIS_CMD      					 = -0x00003513;/*-13587*/
static const int32_t API_ERR_FAILED_TO_FIND_ROUTE			                                         = -0x00003613;/*-13843*/
static const int32_t API_ERR_OVER_MAX_PKG_SIZE                                                       = -0x00003713;/*-14099*/
static const int32_t API_ERR_INVALID_VERSION_FOR_TLV                                                 = -0x00003813;/*-14355*/
static const int32_t API_ERR_BSON_SERIALIZE                                                          = -0x00003913;/*-14611*/
static const int32_t API_ERR_BSON_DESERIALIZE                                                        = -0x00003a13;/*-14867*/
static const int32_t API_ERR_ADD_RECORD                                                              = -0x00003b13;/*-15123*/
static const int32_t API_ERR_ZONE_IS_NOT_EXIST													     = -0x00003c13;/*-15379*/
static const int32_t API_ERR_TRAVERSER_IS_NOT_EXIST                                                  = -0x00003d13;/*-15635*/
static const int32_t API_ERR_INSTANCE_ID_FULL                                                        = -0x00003e13;/*-15891*/
static const int32_t API_ERR_INSTANCE_INIT_LOG_FAILURE                                               = -0x00003f13;/*-16147*/
 
//TCAPCENTER BUSINESS (module id 0x14) Error String defined below 
//......

//TCAPCENTER SYSTEM (module id 0x15) Error String defined below 
static const int32_t CENTER_ERR_INVALID_PARAMS                                                       = -0x00000115;/*-277*/
static const int32_t CENTER_ERR_TABLE_ALREADY_EXIST                                                  = -0x00000215;/*-533*/
static const int32_t CENTER_ERR_TABLE_NOT_EXIST                                                      = -0x00000315;/*-789*/

//TCAPDIR BUSINESS (module id 0x16) Error Code defined below 
//......

//TCAPDIR SYSTEM (module id 0x17) Error Code defined below 
static const int32_t DIR_ERR_SIGN_FAIL                                                         		 = -0x00000117;/*-279*/
static const int32_t DIR_ERR_LOW_VERSION                                                          	 = -0x00000217;/*-535*/
static const int32_t DIR_ERR_HIGH_VERSION                                                            = -0x00000317;/*-791*/
static const int32_t DIR_ERR_GET_DIR_SERVER_LIST                                                     = -0x00000417;/*-1047*/
static const int32_t DIR_ERR_APP_IS_NOT_FOUNT                                                    	 = -0x00000517;/*-1303*/
static const int32_t DIR_ERR_NOT_CONNECT_TCAPCENTER                                                  = -0x00000617;/*-1559*/
static const int32_t DIR_ERR_ZONE_IS_NOT_FOUNT                                                    	 = -0x00000717;/*-1815*/
static const int32_t DIR_ERR_HASH_TABLE_FAILED                                                    	 = -0x00000817;/*-2071*/

//TCAPCOMMON BUSINESS (module id 0x18) Error Code defined below 
//......


//BSON ERROR
static const int32_t BSON_ERR_TYPE_IS_NOT_MATCH                                                      = -0x00000118;/*-280*/
static const int32_t BSON_ERR_INVALID_DATA_TYPE                                                      = -0x00000218;/*-536*/
static const int32_t BSON_ERR_INVALID_VALUE                                                          = -0x00000318;/*-792*/
static const int32_t BSON_ERR_BSON_TYPE_UNMATCH_TDR_TYPE                                             = -0x00000418;/*-1048*/
static const int32_t BSON_ERR_BSON_TYPE_IS_NOT_SUPPORT_BY_TCAPLUS                                    = -0x00000518;/*-1304*/
static const int32_t BSON_ERR_BSON_ARRAY_COUNT_IS_INVALID                                   		 = -0x00000618;/*-1560*/
static const int32_t BSON_ERR_FAILED_TO_PARSE                                   					 = -0x00000718;/*-1816*/
static const int32_t BSON_ERR_INVALID_FIELD_NAME_LENGTH                                  			 = -0x00000818;/*-2072*/
static const int32_t BSON_ERR_INDEX_FIELD_NAME_NOT_EXIST_WITH_ARRAY_TYPE                             = -0x00000918;/*-2328*/
static const int32_t BSON_ERR_INVALID_ARRAY_INDEX                             						 = -0x00000a18;/*-2584*/
static const int32_t BSON_ERR_TDR_META_LIB_IS_NULL                             						 = -0x00000b18;/*-2840*/
static const int32_t BSON_ERR_MATCHED_COUNT_GREATER_THAN_ONE                             			 = -0x00000c18;/*-3096*/
static const int32_t BSON_ERR_NO_MATCHED                             								 = -0x00000d18;/*-3352*/
																												   /*     */
static const int32_t BSON_ERR_GREATER_THAN_ARRAY_MAX_COUNT                             				 = -0x00000f18;/*-3864*/
static const int32_t BSON_ERR_BSON_EXCEPTION                                                         = -0x00001018;/*-4120*/
static const int32_t BSON_ERR_STD_EXCEPTION                                                          = -0x00001118;/*-4376*/
static const int32_t BSON_ERR_INVALID_KEY                                                            = -0x00001218;/*-4632*/
static const int32_t BSON_ERR_TDR_META_LIB_IS_INVALID                            					 = -0x00001318;/*-4888*/



//TCAPTCAPCOMMON SYSTEM (module id 0x19) Error Code defined below
static const int32_t COMMON_ERR_INVALID_ARGUMENTS                                                    = -0x00000119;/*-281*/
static const int32_t COMMON_ERR_INVALID_MEMBER_VARIABLE_VALUE                                        = -0x00000219;/*-537*/
static const int32_t COMMON_ERR_SPINLOCK_INIT_FAIL                                                   = -0x00000319;/*-793*/
static const int32_t COMMON_ERR_SPINLOCK_DESTROY_FAIL                                                = -0x00000419;/*-1049*/
static const int32_t COMMON_ERR_COMPRESS_BUF_NOT_ENOUGH                                              = -0x00000519;/*-1305*/
static const int32_t COMMON_ERR_DECOMPRESS_BUF_NOT_ENOUGH                                            = -0x00000619;/*-1561*/
static const int32_t COMMON_ERR_DECOMPRESS_INVALID_INPUT                                             = -0x00000719;/*-1817*/
static const int32_t COMMON_ERR_CANNOT_FIND_COMPRESS_ALGORITHM                                       = -0x00000819;/*-2073*/
static const int32_t COMMON_ERR_CANNOT_FIND_DECOMPRESS_ALGORITHM                                     = -0x00000919;/*-2329*/
static const int32_t COMMON_ERR_COMPRESS_FAIL                                                        = -0x00000a19;/*-2585*/
static const int32_t COMMON_ERR_DECOMPRESS_FAIL                                                      = -0x00000b19;/*-2841*/
static const int32_t COMMON_ERR_INVALID_SWITCH_VALUE                                                 = -0x00000c19;/*-3097*/
static const int32_t COMMON_ERR_LINUX_SYSTEM_CALL_FAIL                                               = -0x00000d19;/*-3353*/
static const int32_t COMMON_ERR_NOT_FIND_STAT_CACHE_VALUE                                            = -0x00000e19;/*-3609*/
static const int32_t COMMON_ERR_LZO_CHECK_FAIL                                                       = -0x00000f19;/*-3865*/


// Non-error (for information purpose)
static const int32_t COMMON_INFO_DATA_NOT_MODIFIED                                                   = 0x00000120; /*288*/

各错误码数值对应的意思如下
    ErrorCodeStringPair g_error_code_str_pairs[] =
    {
//GENERAL BUSINESS (module id 0x00) Error String defined below
{GEN_ERR_SUC, "General_success"},
{GEN_ERR_ERR, "General_error"},
{GEN_ERR_INVALID_ARGUMENTS, "invalid arguments"},
{GEN_ERR_UNSUPPORT_OPERATION, "unsupport operation"},
{GEN_ERR_NOT_ENOUGH_MEMORY, "not enough memory"},
{GEN_ERR_ECMGR_INVALID_MODULE_ID, "General_EcMgr code manger invalid module id"},
{GEN_ERR_ECMGR_INVALID_ERROR_CODE, "General_EcMgr invalid error code"},
{GEN_ERR_ECMGR_NULL_ERROR_STRING, "General_EcMgr null error string"},
{GEN_ERR_ECMGR_DUPLICATED_ERROR_CODE, "General_EcMgr duplicated error code"},
{GEN_ERR_TXLOG_NULL_POINTER_FROM_TSD, "Txlog_Null pointer from tsd"},
{GEN_ERR_TABLE_READONLY, "table is readonly"},
{GEN_ERR_TABLE_READ_DELETE, "table read delete"},
{GEN_ERR_ACCESS_DENIED, "table denied access"},
{GEN_ERR_NOT_SATISFY_INSERT_FOR_SORTLIST,"not satisfy insert for sortlist"},

//GENERAL SYSTEM (module id 0x01) Error String defined below
//......

//LINELOC BUSINESS (module id 0x02) Error String defined below
{LOC_ERR__0x00000102, "LineLoc_-0x00000102"},
{LOC_ERR__0x00000202, "LineLoc_-0x00000202"},
{LOC_ERR__0x00000302, "LineLoc_-0x00000302"},
{LOC_ERR__0x00000402, "LineLoc_-0x00000402"},
{LOC_ERR__0x00000502, "LineLoc_-0x00000502"},
{LOC_ERR__0x00000602, "LineLoc_-0x00000602"},
{LOC_ERR__0x00000702, "LineLoc_-0x00000702"},
{LOC_ERR__0x00000802, "LineLoc_-0x00000802"},
{LOC_ERR__0x00000902, "LineLoc_-0x00000902"},
{LOC_ERR__0x00000A02, "LineLoc_-0x00000A02"},
{LOC_ERR__0x00000B02, "LineLoc_-0x00000B02"},
{LOC_ERR__0x00000C02, "LineLoc_-0x00000C02"},
{LOC_ERR__0x00000D02, "LineLoc_-0x00000D02"},
{LOC_ERR__0x00000E02, "LineLoc_-0x00000E02"},
{LOC_ERR__0x00000F02, "LineLoc_-0x00000F02"},
{LOC_ERR__0x00001002, "LineLoc_-0x00001002"},
{LOC_ERR__0x00001102, "LineLoc_-0x00001102"},
{LOC_ERR__0x00001202, "LineLoc_-0x00001202"},
{LOC_ERR__0x00001302, "LineLoc_-0x00001302"},
{LOC_ERR__0x00001402, "LineLoc_-0x00001402"},
{LOC_ERR__0x00001502, "LineLoc_-0x00001502"},
{LOC_ERR__0x00001602, "LineLoc_-0x00001602"},
{LOC_ERR__0x00001702, "LineLoc_-0x00001702"},
{LOC_ERR__0x00001802, "LineLoc_-0x00001802"},
{LOC_ERR__0x00001902, "LineLoc_-0x00001902"},
{LOC_ERR__0x00001A02, "LineLoc_-0x00001A02"},
{LOC_ERR__0x00001B02, "LineLoc_-0x00001B02"},
{LOC_ERR__0x00001C02, "LineLoc_-0x00001C02"},
{LOC_ERR__0x00001D02, "LineLoc_-0x00001D02"},
{LOC_ERR__0x00001E02, "LineLoc_-0x00001E02"},
{LOC_ERR__0x00001F02, "LineLoc_-0x00001F02"},
{LOC_ERR__0x00002002, "LineLoc_-0x00002002"},
{LOC_ERR__0x00002802, "LineLoc_-0x00002802"},
{LOC_ERR__0x00003002, "LineLoc_-0x00003002"},
{LOC_ERR__0x00003802, "LineLoc_-0x00003802"},
{LOC_ERR__0x00004002, "LineLoc_-0x00004002"},
{LOC_ERR__0x00004802, "LineLoc_-0x00004802"},
{LOC_ERR__0x00005002, "LineLoc_-0x00005002"},
{LOC_ERR__0x00005802, "LineLoc_-0x00005802"},
{LOC_ERR__0x00006002, "LineLoc_-0x00006002"},
{LOC_ERR__0x00006802, "LineLoc_-0x00006802"},
{LOC_ERR__0x00007002, "LineLoc_-0x00007002"},
{LOC_ERR__0x00007802, "LineLoc_-0x00007802"},
{LOC_ERR__0x00008002, "LineLoc_-0x00008002"},
{LOC_ERR__0x00008802, "LineLoc_-0x00008802"},
{LOC_ERR__0x00009002, "LineLoc_-0x00009002"},
{LOC_ERR__0x00009802, "LineLoc_-0x00009802"},
{LOC_ERR__0x0000A002, "LineLoc_-0x0000A002"},
{LOC_ERR__0x0000A802, "LineLoc_-0x0000A802"},
{LOC_ERR__0x0000B002, "LineLoc_-0x0000B002"},
{LOC_ERR__0x0000B802, "LineLoc_-0x0000B802"},
{LOC_ERR__0x0000C002, "LineLoc_-0x0000C002"},
{LOC_ERR__0x0000C802, "LineLoc_-0x0000C802"},
//......
{LOC_ERR__0x0000FF02, "LineLoc_-0x0000FF02"},

//LINELOC SYSTEM (module id 0x03) Error String defined below
//......

//TXHDB (module id 0x04) Error String defined below
//......

//TXHDB (module id 0x05) Error String defined below
{TXHDB_ERR_RECORD_NOT_EXIST, "txhdb_record_not_exist"},
{TXHDB_ERR_ITERATION_NO_MORE_RECORDS, "txhdb_iteration_no_more_record"},
{TXHDB_ERR_MUTEX_TRYLOCK_BUSY, "txhdb_mutex_trylock_busy"},
{TXHDB_ERR_MUTEX_TIMEDLOCK_TIMEOUT, "txhdb_mutex_timedlock_timeout"},
{TXHDB_ERR_RWLOCK_TRYWRLOCK_BUSY, "txhdb_rwlock_trywrlock_busy"},
{TXHDB_ERR_RWLOCK_TRYRDLOCK_BUSY, "txhdb_rwlock_tryrdlock_busy"},
{TXHDB_ERR_SPIN_TRYLOCK_BUSY, "txhdb_spin_trylock_busy"},
{TXHDB_ERR_ITERATION_EXCEED_MAX_ALLOWED_TIME_OF_ONE_ITER, "txhdb_err_iteration_exceed_max_allowed_time_of_one_iter"},
{TXHDB_ERR_INVALID_ARGUMENTS, "txhdb_invalid_arguments"},
{TXHDB_ERR_INVALID_MEMBER_VARIABLE_VALUE, "txhdb_invalid_member_variable_value"},
{TXHDB_ERR_ALREADY_OPEN, "txhdb_already_opened"},
{TXHDB_ERR_MUTEX_LOCK_FAIL, "txhdb_mutex_lock_fail"},
{TXHDB_ERR_MUTEX_TRYLOCK_FAIL, "txhdb_mutex_trylock_fail"},
{TXHDB_ERR_MUTEX_TIMEDLOCK_FAIL, "txhdb_mutex_timedlock_fail"},
{TXHDB_ERR_MUTEX_UNLOCK_FAIL, "txhdb_mutex_unlock_fail"},
{TXHDB_ERR_RWLOCK_WRLOCK_FAIL, "txhdb_rwlock_wrlock_fail"},
{TXHDB_ERR_RWLOCK_TRYWRLOCK_FAIL, "txhdb_rwlock_trywrlock_fail"},
{TXHDB_ERR_RWLOCK_RDLOCK_FAIL, "txhdb_rwlock_rdlock_fail"},
{TXHDB_ERR_RWLOCK_TRYRDLOCK_FAIL, "txhdb_rwlock_tryrdlock_fail"},
{TXHDB_ERR_RWLOCK_UNLOCK_FAIL, "txhdb_rwlock_unlock_fail"},
{TXHDB_ERR_SPIN_LOCK_FAIL, "txhdb_spin_lock_fail"},
{TXHDB_ERR_SPIN_UNLOCK_FAIL, "txhdb_spin_unlock_fail"},
{TXHDB_ERR_FILE_EXISTS_BUT_STATUS_ERROR, "Txhdb_file_exists_but_status_error"},
{TXHDB_ERR_FILE_OPEN_FAIL, "Txhdb_file_open_fail"},
{TXHDB_ERR_FILE_READ_SIZE_INVALID, "Txhdb_file_read_size_INVALID"},
{TXHDB_ERR_FILE_INVALID_FILE_PATH, "Txhdb_file_invalid_file_path"},
{TXHDB_ERR_FILE_LOCK_FILE_FAIL, "Txhdb_file_lock_file_fail"},
{TXHDB_ERR_FILE_NOT_A_REGULAR_FILE, "Txhdb_file_not_a_regular_file"},
{TXHDB_ERR_FILE_MMAP_FAIL, "Txhdb_file_mmap_fail"},
{TXHDB_ERR_FILE_MUNMAP_FAIL, "Txhdb_file_munmap_fail"},
{TXHDB_ERR_FILE_CLOSE_FAIL, "Txhdb_file_close_fail"},
{TXHDB_ERR_FILE_SPACE_NOT_ENOUGH_IN_HEAD, "Txhdb_file_space_not_enough_in_head"},
{TXHDB_ERR_FILE_FTRUNCATE_FAIL, "Txhdb_file_ftruncate_fail"},
{TXHDB_ERR_FILE_INCONSISTANT_FILE_SIZE, "Txhdb_file_inconsistant_file_size"},
{TXHDB_ERR_FILE_MSIZ_LESSER_THAN_TXHDB_WHOLE_REC_OFFSET, "Txhdb_file_msiz_lesser_than_txhdb_whole_rec_offset"},
{TXHDB_ERR_FILE_MSIZ_CHANGE_NOT_PERMIT, "Txhdb_file_msiz_change_not_permit"},
{TXHDB_ERR_FILE_FSTAT_FAIL, "Txhdb_file_fstat_fail"},
{TXHDB_ERR_FILE_MSYNC_FAIL, "Txhdb_file_msync_fail"},
{TXHDB_ERR_FILE_FSYNC_FAIL, "Txhdb_file_fsync_fail"},
{TXHDB_ERR_FILE_FCNTL_LOCK_FILE_FAIL, "Txhdb_file_fcntl_lock_file_fail"},
{TXHDB_ERR_FILE_FCNTL_UNLOCK_FILE_FAIL, "Txhdb_file_fcntl_unlock_file_fail"},
{TXHDB_ERR_FILE_PREAD_FAIL_WITH_SPECIFIED_ERRNO, "txhdb_file_pread_fail_with_specified_errno"},
{TXHDB_ERR_FILE_PREAD_FAIL_WITH_UNSPECIFIED_ERRNO, "txhdb_file_pread_fail_with_unspecified_errno"},
{TXHDB_ERR_FILE_PWRITE_FAIL_WITH_SPECIFIED_ERRNO, "txhdb_file_pwrite_fail_with_specified_errno"},
{TXHDB_ERR_FILE_PWRITE_FAIL_WITH_UNSPECIFIED_ERRNO, "txhdb_file_pwrite_fail_with_unspecified_errno"},
{TXHDB_ERR_FILE_READ_EXCEED_FILE_BOUNDARY, "txhdb_read_exceed_file_boundary"},
{TXHDB_ERR_FILE_READ_FAIL_DURING_COPY, "txhdb_file_read_fail_during_copy"},
{TXHDB_ERR_FILE_WRITE_FAIL_DURING_COPY, "txhdb_file_write_fail_during_copy"},
{TXHDB_ERR_FILE_INVALID_FREE_BLOCK_POOL_METADATA, "Txhdb_file_invalid_free_block_pool_metadata"},
{TXHDB_ERR_FILE_INVALID_MAGIC, "Txhdb_file_invalid_magic"},
{TXHDB_ERR_FILE_INVALID_LIBRARY_VERSION, "Txhdb_file_invalid_library_version"},
{TXHDB_ERR_FILE_INVALID_LIBRARY_REVISION, "Txhdb_file_invalid_library_revision"},
{TXHDB_ERR_FILE_INVALID_FORMAT_VERSION, "Txhdb_file_invalid_format_version"},
{TXHDB_ERR_FILE_INVALID_EXTDATA_FORMAT_VERSION, "Txhdb_file_invalid_extdata_format_version"},
{TXHDB_ERR_FILE_INVALID_DBTYPE, "Txhdb_file_invalid_dbtype"},
{TXHDB_ERR_FILE_HEAD_CRC_UNMATCH, "Txhdb_file_head_crc_unmatch"},
{TXHDB_ERR_FILE_INVALID_METADATA, "Txhdb_txhdb_err_file_invalid_metadata"},
{TXHDB_ERR_FILE_INVALID_HEADLEN, "Txhdb_txhdb_err_file_invalid_headlen"},
{TXHDB_ERR_FILE_DESERIAL_HEAD_SPACE_NOT_ENOUGH, "Txhdb_file_deserialhead_space_not_enough"},
{TXHDB_ERR_FILE_SERIAL_HEAD_SPACE_NOT_ENOUGH, "Txhdb_file_serialhead_space_not_enough"},
{TXHDB_ERR_FILE_DESERIAL_STAT_SPACE_NOT_ENOUGH, "Txhdb_file_deserialstat_space_not_enough"},
{TXHDB_ERR_FILE_SERIAL_STAT_SPACE_NOT_ENOUGH, "Txhdb_file_serialstat_space_not_enough"},
{TXHDB_ERR_FILE_SERIAL_FREE_BLOCK_LIST_INFO_WRONG_BUFFLEN, "txhdb_file_serial_free_block_list_info_wrong_bufflen"},
{TXHDB_ERR_FILE_IN_EXCEPTIONAL_STATUS, "txhdb_file_in_exceptional_status"},
{TXHDB_ERR_DB_NOT_OPENED, "Txhdb_not_opened"},
{TXHDB_ERR_DB_WRITE_NOT_PERMIT, "Txhdb_db_write_not_permit"},
{TXHDB_ERR_INVALID_OFFSET_FROM_BUCKET, "Txhdb_invalid_offset_from_bucket"},
{TXHDB_ERR_READ_EXTDATA_EXCEED_BUFF_LENGTH, "Txhdb_read_extdata_exceed_buff_length"},
{TXHDB_ERR_WRITE_EXTDATA_EXCEED_BUFF_LENGTH, "Txhdb_write_extdata_exceed_buff_length"},
{TXHDB_ERR_FREE_BLOCK_IS_READ_WHEN_GETTING_RECORD, "Txhdb_free_block_is_read_when_getting_record"},
{TXHDB_ERR_INVALID_KEY_DATABLOCK_NUM, "Txhdb_invalid_key_datablock_num"},
{TXHDB_ERR_INVALID_VALUE_DATABLOCK_NUM, "Txhdb_invalid_value_datablock_num"},
{TXHDB_ERR_GET_RECORD_EXCEED_BUFF_LENGTH, "Txhdb_get_record_exceed_buff_length"},
{TXHDB_ERR_COMPRESSION_FAIL, "Txhdb_compession_fail"},
{TXHDB_ERR_DECOMPRESSION_FAIL, "Txhdb_decompression_fail"},
{TXHDB_ERR_INVALID_OFFSETINEXTDATA_AND_SIZE_WHEN_UPDATING_EXTDATA, "Txhdb_invalid_offsetInExtdata_and_size_when_updating_extdata"},
{TXHDB_ERR_UNEXPECTED_FREEBLOCK, "Txhdb_unexpected_freeblock"},
{TXHDB_ERR_VALUE_APOW_LESSER_THAN_KEY_APOW, "Txhdb_value_apow_lesser_than_key_apow__value_apow_should_be_equal_to_or_greater_than_key_apow"},
{TXHDB_ERR_DUPLICATED_FILE_PATH, "Txhdb_duplicated_file_path"},
{TXHDB_ERR_INVALID_KEY_HEAD_SIZE_IN_TXHDB_META, "Txhdb_invalid_key_head_size_in_txhdb_meta"},
{TXHDB_ERR_INVALID_FILE_SIZE, "Txhdb_invalid_file_size"},
{TXHDB_ERR_INVALID_FREE_BLOCK_SIZE, "Txhdb_invalid_free_block_size"},
{TXHDB_ERR_MMAP_MEMSIZE_CHANGE_NOT_PERMITTED, "Txhdb_mmap_memsize_change_not_permitted"},
{TXHDB_ERR_NEW_FILE_OBJ_FAIL, "Txhdb_new_file_obj_fail"},
{TXHDB_ERR_RECORD_KEY_OFFSET_LESSER_THAN_TXHDB_WHOLE_REC_OFFSET, "txhdb_record_key_offset_lesser_than_txhdb_whole_rec_offset"},
{TXHDB_ERR_RECORD_VALUE_OFFSET_LESSER_THAN_TXHDB_WHOLE_REC_OFFSET, "txhdb_record_value_offset_lesser_than_txhdb_whole_rec_offset"},
{TXHDB_ERR_RECORD_OFFSET_LESSER_THAN_TXHDB_WHOLE_REC_OFFSET, "txhdb_record_offset_lesser_than_txhdb_whole_rec_offset"},
{TXHDB_ERR_KEY_BUFFSIZE_LESSER_THAN_KEY_HEADSIZE, "txhdb_key_buffsize_lesser_than_key_headsize"},
{TXHDB_ERR_VALUE_BUFFSIZE_LESSER_THAN_VALUE_HEADSIZE, "txhdb_value_buffsize_lesser_than_value_headsize"},
{TXHDB_ERR_RECORD_SIZE_LESSER_THAN_KEY_HEADSIZE, "txhdb_record_size_lesser_than_key_headsize"},
{TXHDB_ERR_INVALID_BLOCK_MAGIC, "txhdb_invalid_block_magic"},
{TXHDB_ERR_INVALID_FREE_BLOCK_MAGIC, "txhdb_invalid_free_block_magic"},
{TXHDB_ERR_INVALID_KEYMAGIC, "txhdb_invalid_KEYMAGIC_it_should_be_KEYMAGIC"},
{TXHDB_ERR_INVALID_KEYSPLMAGIC, "txhdb_invalid_KEYSPLMAGIC_it_should_be_KEYSPLMAGIC"},
{TXHDB_ERR_INVALID_VALMAGIC, "txhdb_invalid_VALMAGIC_it_should_be_VALMAGIC"},
{TXHDB_ERR_INVALID_VALSPLMAGIC, "txhdb_invalid_VALSPLMAGIC_it_should_be_VALSPLMAGIC"},
{TXHDB_ERR_UNSUPPORTED_KEY_FORMAT_VERSION, "txhdb_unsupported_key_format_version"},
{TXHDB_ERR_UNSUPPORTED_KEY_SPLBLOCK_FORMAT_VERSION, "txhdb_unsupported_key_splblock_format_version"},
{TXHDB_ERR_UNSUPPORTED_VALUE_FORMAT_VERSION, "txhdb_unsupported_value_format_version"},
{TXHDB_ERR_UNSUPPORTED_VALUE_SPLBLOCK_FORMAT_VERSION, "txhdb_unsupported_value_splblock_format_version"},
{TXHDB_ERR_UNSUPPORTED_FREE_BLOCK_FORMAT_VERSION, "txhdb_unsupported_value_splblock_format_version"},
{TXHDB_ERR_KEY_HEAD_CRC_UNMATCH, "txhdb_key_head_crc_unmatch"},
{TXHDB_ERR_KEY_SPLBLOCK_HEAD_CRC_UNMATCH, "txhdb_key_splblock_head_crc_unmatch"},
{TXHDB_ERR_VALUE_HEAD_CRC_UNMATCH, "txhdb_value_head_crc_unmatch"},
{TXHDB_ERR_VALUE_SPLBLOCK_HEAD_CRC_UNMATCH, "txhdb_value_splblock_head_crc_unmatch"},
{TXHDB_ERR_FREE_BLOCK_HEAD_CRC_UNMATCH, "txhdb_free_block_head_crc_unmatch"},
{TXHDB_ERR_FREE_BLOCK_LIST_INFO_CRC_UNMATCH, "txhdb_free_block_list_info_crc_unmatch"},
{TXHDB_ERR_GET_KEY_READ_BUFFER_FAIL, "txhdb_get_key_read_buffer_fail"},
{TXHDB_ERR_GET_VALUE_READ_BUFFER_FAIL, "txhdb_get_value_read_buffer_fail"},
{TXHDB_ERR_GET_LRU_VALUE_BUFFER_FAIL, "txhdb_get_lru_value_buffer_fail"},
{TXHDB_ERR_GET_EXTDATA_READ_BUFFER_FAIL, "txhdb_get_extdata_read_buffer_fail"},
{TXHDB_ERR_KEY_BLOCK_BODYSIZE_GREATER_THAN_KEY_BODYSIZE, "txhdb_key_block_bodysize_greater_than_key_bodysize"},
{TXHDB_ERR_VALUE_BLOCK_BODYSIZE_GREATER_THAN_VALUE_BODYSIZE, "txhdb_value_block_bodysize_greater_than_value_bodysize"},
{TXHDB_ERR_NULL_RECORD_POINTER, "txhdb_null_record_pointer"},
{TXHDB_ERR_NULL_RECORD_WRITE_BUFF, "txhdb_null_record_write_buff"},
{TXHDB_ERR_SERIALIZE_RECORD_KEY_HEAD, "txhdb_serialize_record_key_head"},
{TXHDB_ERR_INVALID_IDX_IN_STAT_NUMS_ARRAY, "txhdb_invalid_idx_in_stat_nums_array"},
{TXHDB_ERR_INVALID_ELEMNUM_OF_STAT_KEYNUMS, "txhdb_invalid_elemnum_of_stat_keynums"},
{TXHDB_ERR_INVALID_ELEMNUM_OF_STAT_VALNUMS, "txhdb_invalid_elemnum_of_stat_valnums"},
{TXHDB_ERR_PRINT_SPACE_NOT_ENOUGH, "txhdb_print_space_not_enough"},
{TXHDB_ERR_LRU_SHIFTIN_NOT_ENOUGH_MEMORY, "txhdb_lru_shiftin_not_enough_memory"},
{TXHDB_ERR_LRU_SHIFTIN_NO_MORE_LRU_NODE, "txhdb_lru_shiftin_no_more_lru_node"},
{TXHDB_ERR_LRU_ADJUST_NO_MORE_LRU_NODE, "txhdb_lru_adjust_no_more_lru_node"},
{TXHDB_ERR_LRU_SHIFTOUT_RECORD_ALREADY_OUTSIDE_OF_MEMORY, "txhdb_lru_shiftout_record_already_outside_of_memory"},
{TXHDB_ERR_FILE_EXTDATA_LENGTH_CRC_UNMATCH, "txhdb_file_extdata_length_crc_unmatch"},
{TXHDB_ERR_FILE_EXTDATA_INVALID_LENGTH, "txhdb_file_extdata_invalid_length"},
{TXHDB_ERR_INVALID_VALUE_HEAD_SIZE_IN_TXHDB_META, "Txhdb_invalid_value_head_size_in_txhdb_meta"},
{TXHDB_ERR_INVALID_SPLITDATABLOCK_HEAD_SIZE_IN_TXHDB_META, "Txhdb_invalid_splitdatablock_head_size_in_txhdb_meta"},
{TXHDB_ERR_KEY_BUCKETIDX_UNMATCH, "txhdb_key_bucketidx_unmatch"},
{TXHDB_ERR_FILE_WRITE_SIZE_INVALID, "Txhdb_file_write_size_invalid"},
{TXHDB_ERR_MODIFY_STAT_UNSUPPORTED_OPERATION_TYPE, "Txhdb_modify_stat_unsupported_operation_type"},
{TXHDB_ERR_INVALID_EXTDATAMAGIC, "txhdb_invalid_EXTDATAMAGIC_it_should_be_EXTDATAMAGIC"},
{TXHDB_ERR_INVALID_INTERNAL_LIST_TAIL_DURING_POP_LRU_NODELIST, "txhdb_invalid_internal_list_tail_during_pop_lru_nodelist"},
{TXHDB_ERR_GET_LRUNODE_FAIL, "txhdb_get_lrunode_fail"},
{TXHDB_ERR_LRUNODE_INVALID_FLAG, "txhdb_lrunode_invalid_flag"},
{TXHDB_ERR_INVALID_FREE_BLOCK_NUM_TOO_MANY_FREE_BLOCKS, "txhdb_invalid_free_block_num_too_many_free_blocks"},
{TXHDB_ERR_INVALID_ELEMNUM_OF_STAT_NOPADDING_SIZE_KEYNUMS, "txhdb_invalid_elemnum_of_stat_nopadding_size_keynums"},
{TXHDB_ERR_INVALID_ELEMNUM_OF_STAT_NOPADDING_SIZE_VALNUMS, "txhdb_invalid_elemnum_of_stat_nopadding_size_valnums"},
{TXHDB_ERR_ADD_LSIZE_EXCEEDS_MAX_TSD_VALUE_BUFF_SIZE, "txhdb_add_lsize_exceeds_max_tsd_value_buff_size"},
{TXHDB_ERR_INTERNAL_CONSTANTS_ILLEGAL, "txhdb_internal_constants_illegal"},
{TXHDB_ERR_TOO_BIG_KEY_BIZ_SIZE, "txhdb_too_big_key_biz_size"},
{TXHDB_ERR_TOO_BIG_VALUE_BIZ_SIZE, "txhdb_too_big_value_biz_size"},
{TXHDB_ERR_INDEX_NO_EXIST, "txhdb_index_no_exist"},
{TXHDB_ERR_INVALID_FREE_BLOCK_BASESIZE, "txhdb_invalid_free_block_basesize"},
{TXHDB_ERR_CANNOT_CREATE_MMAPSHM_BECAUSE_SHM_ALREADY_EXISTED, "txhdb_cannot_create_mmapshm_because_shm_already_existed"},
{TXHDB_ERR_INVALID_GENSHM_KEY, "txhdb_invalid_gen_shm_key"},
{TXHDB_ERR_GENSHM_GET_FAIL, "txhdb_invalid_gen_shm_get_fail"},
{TXHDB_ERR_GENSHM_CREATE_FAIL, "txhdb_invalid_gen_shm_create_fail"},
{TXHDB_ERR_GENSHM_STAT_FAIL, "txhdb_invalid_gen_shm_stat_fail"},
{TXHDB_ERR_GENSHM_DOES_NOT_EXIST, "txhdb_genshm_does_not_exist"},
{TXHDB_ERR_GENSHM_ATTACH_FAIL_BECAUSE_IT_IS_ALREADY_ATTACHED_BY_OTHER_PROCESSES, "txhdb_genshm_attach_fail_because_it_is_already_attached_by_other_processes"},
{TXHDB_ERR_GENSHM_ATTACH_FAIL, "txhdb_genshm_attach_fail"},
{TXHDB_ERR_FILE_INCONSISTANT_MSIZE, "txhdb_inconsistant_msize"},
{TXHDB_ERR_INVALID_TCAP_GENSHM_MAGIC, "txhdb_invalid_tcap_genshm_magic"},
{TXHDB_ERR_GENSHM_FIXED_HEAD_BUFFLEN_UNMATCH, "txhdb_genshm_fixed_head_bufflen_unmatch"},
{TXHDB_ERR_GENSHM_INVALID_HEADLEN, "txhdb_genshm_invalid_headlen"},
{TXHDB_ERR_GENSHM_HEAD_CRC_UNMATCH, "txhdb_genshm_head_crc_unmatch"},
{TXHDB_ERR_GENSHM_HEAD_INVALID_VERSION, "txhdb_genshm_head_invalid_version"},
{TXHDB_ERR_GENSHM_INVALID_FILETYPE , "txhdb_genshm_invalid_filetype"},
{TXHDB_ERR_GET_IPV4ADDR_FAIL, "txhdb_get_ipv4addr_fail"},
{TXHDB_ERR_NO_VALID_IPV4ADDR_EXISTS, "txhdb_no_valid_ipv4addr_exists"},
{TXHDB_ERR_TRANSFER_IPV4ADDR_FAIL, "txhdb_transfer_ipv4addr_fail"},
{TXHDB_ERR_FILE_EXCEEDS_LSIZE_LIMIT, "txhdb_file_exceeds_lsize_limit"},
{TXHDB_ERR_GENSHM_DETACH_FAIL, "txhdb_genshm_detach_fail"},
{TXHDB_ERR_TXHDB_HEAD_PARAMETERS_ERROR, "txhdb_genshm_detach_fail"},
{TXHDB_ERR_TXHDB_HEAD_OLD_VERSION, "txhdb_head_old_version"},
{TXHDB_ERR_TXHDB_SHM_COREINFO_UNMATCH, "txhdb_shm_coreinfo_unmatch"},
{TXHDB_ERR_TXHDB_SHM_EXTDATA_UNMATCH, "txhdb_shm_extdata_unmatch"},
{TXHDB_ERR_TXHDB_EXTDATA_CHECK_ERROR, "txhdb_extdata_check_error"},
{TXHDB_ERR_CHUNK_BUFFS_CANNOT_BE_ALLOCED_IF_THEY_ARE_NOT_RELEASED, "txhdb_chunk_buffs_cannot_be_alloced_if_they_are_not_released"},
{TXHDB_ERR_ALLOCATE_MEMORY_FAIL, "txhdb_allocate_memory_fail"},
{TXHDB_ERR_INVALID_CHUNK_RW_MANNER, "txhdb_invalid_chunk_rw_manner"},
{TXHDB_ERR_FILE_PREAD_NOT_COMPLETE, "txhdb_file_pread_not_complete"},
{TXHDB_ERR_FILE_PWRITE_NOT_COMPLETE, "txhdb_file_pwrite_not_complete"},
{TXHDB_ERR_KEY_ONEBLOCK_BUT_NEXT_NOTNULL, "TXHDB_ERR_KEY_ONEBLOCK_BUT_NEXT_NOTNULL"},
{TXHDB_ERR_VALUE_ONEBLOCK_BUT_NEXT_NOTNULL, "TXHDB_ERR_VALUE_ONEBLOCK_BUT_NEXT_NOTNULL"},
{TXHDB_ERR_VARINT_FORMAT_ERROR, "TXHDB_ERR_VARINT_FORMAT_ERROR"},
{TXHDB_ERR_TXSTAT_ERROR, "TXHDB_ERR_TXSTAT_ERROR"},
{TXHDB_ERR_INVALID_VERSION, "invalid txhdb version"},
{TXHDB_ERR_FREE_BLOCK_NOT_ENOUGH, "TXHDB_ERR_FREE_BLOCK_NOT_ENOUGH"},


//ENGINE BUSINESS (module id 0x06) Error String defined below
//......

//ENGINE SYSTEM (module id 0x07) Error String defined below
{ENG_ERR_INVALID_ARGUMENTS, "engine_invalid_arguments"},
{ENG_ERR_INVALID_MEMBER_VARIABLE_VALUE, "engine_invalid_member_variable_value"},
{ENG_ERR_NEW_TXHCURSOR_FAILED, "engine_new_txhcursor_failed"},
{ENG_ERR_TXHCURSOR_KEY_BUFFER_LEGHTH_NOT_ENOUGH, "engine_txhcursor_key_buffer_leghth_not_enough"},
{ENG_ERR_TXHCURSOR_VALUE_BUFFER_LEGHTH_NOT_ENOUGH, "engine_txhcursor_value_buffer_leghth_not_enough"},
{ENG_ERR_TXHDB_FILEPATH_NULL, "engine_txhdb_filepath_null"},
{ENG_ERR_TCHDB_RELATED_ERROR, "engine_tchdb_related_error"},
{ENG_ERR_NULL_CACHE, "engine_null_cache"},
{ENG_ERR_ITER_FAIL_SYSTEM_RECORD, "engine_interation_fail_system_record"},
{ENG_ERR_SYSTEM_ERROR, "engine_system_error"},
{ENG_ERR_ENGINE_ERROR, "engine_engine_error"},
{ENG_ERR_DATA_ERROR, "engine_data_error"},
{ENG_ERR_VERSION_ERROR, "engine_version_error"},
{ENG_ERR_SYSTEM_ERROR_BUFF_OVERFLOW, "engine_system_error_buff_overflow"},
{ENG_ERR_METADATA_ERROR, "engine_metadata_error"},
{ENG_ERR_ADD_KEYMETA_FAILED, "engine_add_keymate_failed"},

{ENG_ERR_ADD_VALUEMETA_FAILED, "engine_add_valuemeta_failed"},
{ENG_ERR_RESERVED_FIELDNAME, "engine_reserved_fieldname_error"},
{ENG_ERR_KEYNAME_REPEAT, "engine_keyname_repeat_error"},
{ENG_ERR_VALUENAME_REPEAT, "engine_valuename_repeat_error"},
{ENG_ERR_MISS_KEYMETA, "engine_misss_keymate_error"},
{ENG_ERR_DELETE_KEYFIELD, "engine_delete_keyfield_error"},
{ENG_ERR_CHANGE_KEYCOUNT, "engine_change_keycount_error"},
{ENG_ERR_CHANGE_KEYTYPE, "engine_change_keytype_error"},
{ENG_ERR_CHANGE_KEYLENGTH, "engine_change_keylength_error"},
{ENG_ERR_CHANGE_VALUETYPE, "engine_change_valuetype_error"},
{ENG_ERR_CHANGE_VALUELENGTH, "engine_change_valuelength_error"},
{ENG_ERR_CHANGE_DEFAULTVALUE, "engine_change_defaultvalue_error"},
{ENG_ERR_EMPTY_FIELDNAME, "engine_empty_fieldname_error"},
{ENG_ERR_INVALID_TARGET_KEYFIELD, "engine_invalid_target_keyfield_error"},
{ENG_ERR_INVALID_TARGET_VALUEFIELD, "engine_invalid_target_valuefield_error"},
{ENG_ERR_INVALID_TABLE_TYPE, "engine_invalid_table_type_error"},
{ENG_ERR_CHANGE_TABLE_TYPE, "engine_change_table_type_error"},
{ENG_ERR_MISS_VALUEMETA, "engine_miss_valuemeta_error"},
{ENG_ERR_NOT_ENOUGH_BUFF_FOR_FILEPATH, "engine_not_enough_buff_for_filepath"},
{ENG_ERR_ENGINE_FILE_NOT_FOUND, "engine file or index file not found"},

//ULOG BUSINESS (module id 0x08) Error String defined below
//......

//ULOG SYSTEM (module id 0x09) Error String defined below
{ULOG_ERR_INVALID_PARAMS, "Ulog_invalid parameters"},

//SYNCDB BUSINESS (module id 0x0a) Error String defined below
//.....

//SYNCDB SYSTEM (module id 0x0b) Error String defined below
{SYNCDB_ERR_INVALID_PARAMS, "Syncdb_invalid parameters"},

//TCAPSVR BUSINESS (module id 0x0c) Error String defined below
//......

//TCAPSVR SYSTEM (module id 0x0d) Error String defined below
{SVR_ERR_FAIL_ROUTE, "tcapsvr_fail_route"},
{SVR_ERR_FAIL_TIMEOUT, "tcapsvr_fail_timeout"},
{SVR_ERR_FAIL_SHORT_BUFF, "tcapsvr_fail_short_buf"},
{SVR_ERR_FAIL_SYSTEM_BUSY, "tcapsvr_fail_system_busy"},
{SVR_ERR_FAIL_RECORD_EXIST, "tcapsvr_fail_record_exist"},
{SVR_ERR_FAIL_INVALID_FIELD_NAME, "tcapsvr_fail_invalid_field_name"},
{SVR_ERR_FAIL_VALUE_OVER_MAX_LEN, "tcapsvr_fail_value_over_max_len"},
{SVR_ERR_FAIL_INVALID_FIELD_TYPE, "tcapsvr_fail_invalid_field_type"},
{SVR_ERR_FAIL_SYNC_WRITE, "tcapsvr_fail_sync_write"},
{SVR_ERR_FAIL_WRITE_RECORD, "tcapsvr_fail_write_record"},
{SVR_ERR_FAIL_DELETE_RECORD, "tcapsvr_fail_delete_record"},
{SVR_ERR_FAIL_DATA_ENGINE, "tcapsvr_fail_data_engine"},
{SVR_ERR_FAIL_RESULT_OVERFLOW, "tcapsvr_fail_result_overflow"},
{SVR_ERR_FAIL_INVALID_OPERATION, "tcapsvr_fail_invalid_operation"},
{SVR_ERR_FAIL_INVALID_SUBSCRIPT, "tcapsvr_fail_invalid_subscript"},
{SVR_ERR_FAIL_INVALID_INDEX, "tcapsvr_fail_invalid_index"},
{SVR_ERR_FAIL_OVER_MAXE_FIELD_NUM, "tcapsvr_fail_over_max_field_num"},
{SVR_ERR_FAIL_MISS_KEY_FIELD, "tcapsvr_fail_miss_key_field"},
{SVR_ERR_FAIL_NEED_SIGNUP, "tcapsvr_fail_need_signup"},
{SVR_ERR_FAIL_CROSS_AUTH, "tcapsvr_fail_cross_auth"},
{SVR_ERR_FAIL_SIGNUP_FAIL, "tcapsvr_fail_signup_fail"},
{SVR_ERR_FAIL_SIGNUP_INVALID, "tcapsvr_fail_signup_invalid"},
{SVR_ERR_FAIL_SIGNUP_INIT, "tcapsvr_fail_signup_init"},
{SVR_ERR_FAIL_LIST_FULL, "tcapsvr_fail_list_full"},
{SVR_ERR_FAIL_LOW_VERSION, "tcapsvr_fail_low_version"},
{SVR_ERR_FAIL_HIGH_VERSION, "tcapsvr_fail_high_version"},
{SVR_ERR_FAIL_INVALID_RESULT_FLAG, "tcapsvr_fail_invalid_result_flag"},
{SVR_ERR_FAIL_PROXY_STOPPING, "tcapsvr_fail_proxy_stopping"},
{SVR_ERR_FAIL_SVR_READONLY, "tcapsvr_fail_svr_readonly"},
{SVR_ERR_FAIL_SVR_READONLY_BECAUSE_IN_SLAVE_MODE, "tcapsvr_fail_svr_readonly_because_in_slave_mode"},
{SVR_ERR_FAIL_INVALID_VERSION, "tcapsvr_fail_invalid_version"},
{SVR_ERR_FAIL_SYSTEM_ERROR, "tcapsvr_fail_system_error"},
{SVR_ERR_FAIL_OVERLOAD, "server is overload"},
{SVR_ERR_FAIL_NOT_ENOUGH_DADADISK_SPACE, "tcapsvr_fail_not_enough_datadisk_space"},
{SVR_ERR_FAIL_NOT_ENOUGH_ULOGDISK_SPACE, "tcapsvr_fail_not_enough_ulogdisk_space"},
{SVR_ERR_FAIL_UNSUPPORTED_PROTOCOL_MAGIC, "tcapsvr_fail_unsupported_protocol_magic"},
{SVR_ERR_FAIL_UNSUPPORTED_PROTOCOL_CMD, "tcapsvr_fail_unsupported_protocol_cmd"},
{SVR_ERR_FAIL_HIGH_TABLE_META_VERSION, "tcapsvr_fail_api_table_meta_version_too_high"},
{SVR_ERR_FAIL_MERGE_VALUE_FIELD, "tcapsvr_fail_merge_value_field"},
{SVR_ERR_FAIL_CUT_VALUE_FIELD, "tcapsvr_fail_cut_value_field"},
{SVR_ERR_FAIL_PACK_FIELD, "tcapsvr_fail_pack_value_field"},
{SVR_ERR_FAIL_UNPACK_FIELD, "tcapsvr_fail_unpack_value_field"},
{SVR_ERR_FAIL_LOW_API_VERSION, "tcapsvr_fail_api_version_too_low"},
{SVR_ERR_COMMAND_AND_TABLE_TYPE_IS_MISMATCH, "the command in request is mismatch to the table type"},
{SVR_ERR_FAIL_TO_FIND_CACHE, "tcapsvr_fail_to_find_cache"},
{SVR_ERR_FAIL_TO_FIND_META, "tcapsvr_fail_to_find_meta"},
{SVR_ERR_FAIL_TO_GET_CURSOR, "tcapsvr_fail_to_get_cursor"},
{SVR_ERR_FAIL_OUT_OF_USER_DEF_RANGE, "field value gets out of the range specified by user"},
{SVR_ERR_INVALID_ARGUMENTS, "tcapsvr_invalid_arguments"},
{SVR_ERR_SLAVE_READ_INVALID, "ProcGetDuringMoveFromSrcReq failed because the svr is slave, can't read"},
{SVR_ERR_NULL_CACHE, "null cache object"},
{SVR_ERR_NULL_CURSOR, "null cursor object"},
{SVR_ERR_METALIB_VERSION_LESS_THAN_ENTRY_VERSION, "the metalib version in request is less than entry version"},
{SVR_ERR_INVALID_SELECT_ID_FOR_UNION, "invalid select id for union"},
{SVR_ERR_CAN_NOT_FIND_SELECT_ENTRY_FOR_UNION, "can not find the select entry for union"},
{SVR_ERR_FAIL_DOCUMENT_PACK_VERSION, "document pack version does not match"},
{SVR_ERR_TCAPSVR_PROCESS_NOT_NORMAL, "tcapsvr process in abnormal"},
{SVR_ERR_TBUSD_PROCESS_NOT_NORMAL, "tbusd process in abnormal"},
{SVR_ERR_INVALID_ARRAY_COUNT, "array count invalid"},
{SVR_ERR_REJECT_REQUEST_BECAUSE_ROUTE_IN_REJECT_STATUS, "reject request because route in reject status, it appears generally during data move"},
{SVR_ERR_FAIL_GET_ROUTE_HASH_CODE, "get route hash code failed. it perhaps unpack ProxyHeadForReqSendToSvr failed."},
{SVR_ERR_FAIL_INVALID_FIELD_VALUE, "invalid field value"},
{SVR_ERR_FAIL_PROTOBUF_FIELD_GET, "protobuf fail to get field"},	
{SVR_ERR_FAIL_PROTOBUF_VALUE_BUFF_EXCEED, "protobuf value buff exceed TCAPLUS_MAX_VALUE_BUFFER_LEN(256k)"},
{SVR_ERR_FAIL_PROTOBUF_FIELD_UPDATE, "protobuf fail to update field"},
{SVR_ERR_FAIL_PROTOBUF_FIELD_INCREASE, "protobuf fail to increase field"},
{SVR_ERR_FAIL_PROTOBUF_FIELD_TAG_MISMATCH, "protobuf field tag mismatch"},
{SVR_ERR_FAIL_BINLOG_SEQUENCE_TOO_SMALL, "binlog sequence too small for lossless move binlog sync, maybe the binlog file has already been deleted."},
{SVR_ERR_FAIL_SVR_IS_NOT_MASTER, "failed because svr is not master, for example, process the request which transfer from binlog sync in data move."},
{SVR_ERR_FAIL_BINLOG_INVALID_FILE_PATH, "invalid binlog path"},	
{SVR_ERR_FAIL_BINLOG_SOCKET_SEND_BUFF_IS_FULL, "socket send buff is full for lossless mov binlog sync"},	


//TCAPDB BUSINESS (module id 0x0e) Error Code defined below
//......

//TCAPDB SYSTEM (module id 0x0f) Error String defined below
{TCAPDB_ERR_INVALID_PARAMS, "Tcapdb_invalid parameters"},

//TCAPROXY BUSINESS (module id 0x10) Error String defined below
//......

//TCAPROXY SYSTEM (module id 0x11) Error String defined below
{PROXY_ERR_INVALID_PARAMS, "tcaproxy_invalid_parameters"},
{PROXY_ERR_NO_NEED_ROUTE_BATCHGET_ACTION_MSG_WHEN_NODE_IS_IN_SYNC_STATUS,
    "tcaproxy_error_no_need_routes batchget_action_msg_when_node_is_in_sync_status"},
{PROXY_ERR_NO_NEED_ROUTE_WHEN_NODE_IS_IN_REJECT_STATUS,
    "tcaproxy_error_no_need_routes_when_node_is_in_reject_status"},
{PROXY_ERR_PROBE_TIMEOUT, "tcaproxy_error_probe_timeout"},
{PROXY_ERR_SYSTEM_ERROR, "tcaproxy_error_system_error"},
{PROXY_ERR_CONFIG_ERROR, "tcaproxy_error_config_error"},
{PROXY_ERR_OVER_MAX_NODE, "tcaproxy_error_over_max_node"},
{PROXY_ERR_INVALID_SPLIT_SIZE, "tcaproxy_error_invalid_split_size"},
{PROXY_ERR_INVALID_ROUTE_INDEX, "tcaproxy_error_invalid_route_index"},
{PROXY_ERR_CONNECT_SERVER, "tcaproxy_error_connect_server"},
{PROXY_ERR_COMPOSE_MSG, "tcaproxy_error_compose_msg"},
{PROXY_ERR_ROUTE_MSG, "tcaproxy_error_route_msg"},
{PROXY_ERR_SHORT_BUFFER, "tcaproxy_error_short_buffer"},
{PROXY_ERR_OVER_MAX_RECORD, "tcaproxy_error_over_max_record"},
{PROXY_ERR_INVALID_SERVICE_TABLE, "tcaproxy_error_invalid_service_table"},
{PROXY_ERR_REGISTER_FAILED, "tcaproxy_error_register_failed"},
{PROXY_ERR_CREATE_SESSION_HASH, "tcaproxy_error_create_session_hash"},
{PROXY_ERR_WRONG_STATUS, "tcaproxy_error_wrong_status"},
{PROXY_ERR_UNPACK_MSG, "tcaproxy_error_unpack_msg"},
{PROXY_ERR_PACK_MSG, "tcaproxy_error_pack_msg"},
{PROXY_ERR_SEND_MSG, "tcaproxy_error_send_msg"},
{PROXY_ERR_ALLOCATE_MEMORY, "tcaproxy_error_allocate_memory"},
{PROXY_ERR_PARSE_MSG, "tcaproxy_error_parse_msg"},
{PROXY_ERR_INVALID_MSG, "tcaproxy_error_invalid_msg"},
{PROXY_ERR_FAILED_PROC_REQUEST_BECAUSE_NODE_IS_IN_SYNC_STASUS,
    "tcaproxy_error_failed_proc_request_becuase_node_is_in_sync_status"},
{PROXY_ERR_KEY_FIELD_NUM_IS_ZERO, "tcaproxy_error_key_field_num_is_zero"},
{PROXY_ERR_LACK_OF_SOME_KEY_FIELDS, "tcaproxy_error_lack_of_some_key_fields"},
{PROXY_ERR_FAILED_TO_FIND_NODE, "tcaproxy_error_failed_to_find_node"},
{PROXY_ERR_INVALID_COMPRESS_TYPE, "tcaproxy_error_invalid_compress_type"},
{PROXY_ERR_REQUEST_OVERSPEED, "tcaproxy_error_request_overspeed"},
{PROXY_ERR_SWIFT_TIMEOUT, "tcaproxy_error_swift_trans_timeout"},
{PROXY_ERR_SWIFT_ERROR, "tcaproxy_error_swift_other_errors"},
{PROXY_ERR_DIRECT_RESPONSE,"tcaproxy_error_reponse_direct_not_processed_by_svr "},
{PROXY_ERR_INIT_TLOG, "tcaproxy_error_init_tlog"},
{PROXY_ERR_ASSISTANT_THREAD_NOT_RUN, "tcaproxy_error_assistant_thread_not_run"},
{PROXY_ERR_REQUEST_ACCESS_CTRL_REJECT, "tcaproxy_error_request_access_ctrl_reject"},
{PROXY_ERR_NOT_ALL_NODES_ARE_IN_NORMAL_OR_WAIT_STATUS, "tcaproxy_error_routes_is_not_all_noraml_or_wait"},
{PROXY_ERR_ALREADY_CACHED_REQUEST_TIMEOUT, "tcaproxy_error_already_cached_request_timeout"},
{PROXY_ERR_FAILED_TO_CACHE_REQUEST, "tcaproxy_error_failed_to_cache_request"},
{PROXY_ERR_NOT_EXIST_CACHED_REQUEST, "tcaproxy_error_not_exist_cached_request"},
{PROXY_ERR_FAILED_NOT_ENOUGH_CACHE_BUFF, "tcaproxy_error_failed_not_enough_cache_buff"},
{PROXY_ERR_FAILED_PROCESS_CACHED_REQUEST, "tcaproxy_error_failed_process_cached_request"},
{PROXY_ERR_SYNC_ROUTE_HAS_BEEN_CANCELLED, "tcaproxy_sync_route_has_been_cancelled"},
{PROXY_ERR_FAILED_LOCK_CACHE, "tcaproxy_failed_lock_cache"},

//API BUSINESS (module id 0x12) Error Code defined below
//......

//API SYSTEM (module id 0x13) Error Code defined below
{API_ERR_OVER_MAX_KEY_FIELD_NUM, "api_over_max_key_field_num_error"},
{API_ERR_OVER_MAX_VALUE_FIELD_NUM, "api_over_max_value_field_num_error"},
{API_ERR_OVER_MAX_FIELD_NAME_LEN, "api_over_max_field_name_len_error"},
{API_ERR_OVER_MAX_FIELD_VALUE_LEN, "api_over_max_field_value_len_error"},
{API_ERR_FIELD_NOT_EXSIST, "api_field_not_exist_error"},
{API_ERR_FIELD_TYPE_NOT_MATCH, "api_field_type_not_match_error"},
{API_ERR_PARAMETER_INVALID, "api_parameter_invalid_error"},
{API_ERR_OPERATION_TYPE_NOT_MATCH, "api_operation_type_not_match_error"},
{API_ERR_PACK_MESSAGE, "api_pack_message_error"},
{API_ERR_UNPACK_MESSAGE, "api_unpack_message_error"},
{API_ERR_PACKAGE_NOT_UNPACKED, "api_package_not_unpacked_error"},
{API_ERR_OVER_MAX_RECORD_NUM, "api_over_max_record_num_error"},
{API_ERR_INVALID_COMMAND, "api_invalid_command_error"},
{API_ERR_NO_MORE_RECORD, "api_no_more_record_error"},
{API_ERR_OVER_KEY_FIELD_NUM, "api_over_key_field_num_error"},
{API_ERR_OVER_VALUE_FIELD_NUM, "api_over_value_field_num_error"},
{API_ERR_OBJ_NEED_INIT, "api_obj_need_init_error"},
{API_ERR_INVALID_DATA_SIZE, "api_invalid_data_size_error"},
{API_ERR_INVALID_ARRAY_COUNT, "api_invalid_array_count_error"},
{API_ERR_INVALID_UNION_SELECT, "api_invalid_union_select_error"},
{API_ERR_MISS_PRIMARY_KEY, "api_miss_primary_key_error"},
{API_ERR_UNSUPPORT_FIELD_TYPE, "api_unsupport_field_type_error"},
{API_ERR_ARRAY_BUFFER_IS_SMALL, "api_array_buffer_is_small_error"},
{API_ERR_IS_NOT_WHOLE_PACKAGE, "api_is_not_whole_package_error"},
{API_ERR_MISS_PAIR_FIELD, "api_miss_pair_field_error"},
{API_ERR_GET_META_ENTRY, "api_get_meta_entry_error"},
{API_ERR_GET_ARRAY_META, "api_get_array_meta_error"},
{API_ERR_GET_ENTRY_META, "api_get_entry_meta_error"},
{API_ERR_INCOMPATIBLE_META, "api_incompatible_meta_error"},
{API_ERR_PACK_ARRAY_DATA, "api_pack_array_data_error"},
{API_ERR_PACK_UNION_DATA, "api_pack_union_data_error"},
{API_ERR_PACK_STRUCT_DATA, "api_pack_struct_data_error"},
{API_ERR_UNPACK_ARRAY_DATA, "api_unpack_array_data_error"},
{API_ERR_UNPACK_UNION_DATA, "api_unpack_union_data_error"},
{API_ERR_UNPACK_STRUCT_DATA, "api_unpack_struct_data_error"},
{API_ERR_INVALID_INDEX_NAME, "api_invalid_index_name_error"},
{API_ERR_MISS_PARTKEY_FIELD, "api_miss_partkey_field_error"},
{API_ERR_ALLOCATE_MEMORY, "api_allocate_memory_error"},
{API_ERR_GET_META_SIZE, "api_get_meta_size_error"},
{API_ERR_MISS_BINARY_VERSION, "api_miss_binary_version_error"},
{API_ERR_INVALID_INCREASE_FIELD, "api_invalid_increase_field_error"},
{API_ERR_INVALID_RESULT_FLAG, "api_invalid_result_flag_error"},
{API_ERR_OVER_MAX_LIST_INDEX_NUM, "api_over_max_list_index_num_error"},
{API_ERR_INVALID_OBJ_STATUE, "api_invalid_obj_status_error"},
{API_ERR_INVALID_REQUEST, "api_invalid_request_error"},
{API_ERR_INVALID_SHARD_LIST, "api_invalid_shard_list_error"},
{API_ERR_TABLE_NAME_MISSING, "api_table_name_missing_error"},
{API_ERR_SOCKET_SEND_BUFF_IS_FULL, "api_socket_send_buff_is_full_error"},
{API_ERR_INVALID_MAGIC, "api_invalid_magic"},
{API_ERR_TABLE_IS_NOT_EXIST, "api_table_is_not_exist_error"},
{API_ERR_SHORT_BUFF, "api_buffer_not_enough"},
{API_ERR_FLOW_CONTROL, "api_flow_control"},
{API_ERR_COMPRESS_SWITCH_NOT_SUPPORTED_REGARDING_THIS_CMD, "api_compress_switch_not_supported_regarding_this_cmd"},
{API_ERR_FAILED_TO_FIND_ROUTE, "api_failed_to_find_route, perhaps the table is not register or all proxies are not connected"},
{API_ERR_OVER_MAX_PKG_SIZE, "api_failed_over_max_pkg_size"},
{API_ERR_INVALID_VERSION_FOR_TLV, "api_failed_invalid_version_for_tlv, the obj version is not equal to the lib version"},
{API_ERR_BSON_SERIALIZE, "cannot serailize the BSON object into a string"},
{API_ERR_BSON_DESERIALIZE, "cannot build a BSON object from the string"},
{API_ERR_ADD_RECORD, "failed to add a new record into request"},
{API_ERR_ZONE_IS_NOT_EXIST, "zone_is_not_exist_error" },
{API_ERR_TRAVERSER_IS_NOT_EXIST, "traverser_does_not_exist" },
{API_ERR_INSTANCE_ID_FULL, "instance_id_full" },
{API_ERR_INSTANCE_INIT_LOG_FAILURE, "instance_fail_to_init_log" },

//TCAPCENTER BUSINESS (module id 0x14) Error String defined below
//......

//TCAPCENTER SYSTEM (module id 0x15) Error String defined below
{CENTER_ERR_INVALID_PARAMS, "Tcapcenter_invalid parameters"},
{CENTER_ERR_TABLE_ALREADY_EXIST, "Tcapcenter_table_already_exist"},
{CENTER_ERR_TABLE_NOT_EXIST, "Tcapcenter_table_not_exist"},

//TCAPDIR BUSINESS (module id 0x16) Error Code defined below
//......

//TCAPDIR SYSTEM (module id 0x17) Error Code defined below
{DIR_ERR_SIGN_FAIL, "tcapdir_sign_fail"},
{DIR_ERR_LOW_VERSION, "tcapdir_low_version_error"},
{DIR_ERR_HIGH_VERSION, "tcapdir_high_version_error"},
{DIR_ERR_GET_DIR_SERVER_LIST, "tcapdir_get_dir_server_list_error"},
{DIR_ERR_APP_IS_NOT_FOUNT, "tcapdir_app_is_not_found_error"},
{DIR_ERR_NOT_CONNECT_TCAPCENTER, "tcapdir_is not conncted_tcapcenter_error"},
{DIR_ERR_ZONE_IS_NOT_FOUNT, "tcapdir_zone_is_not_found_error"},
{DIR_ERR_HASH_TABLE_FAILED, "tcapdir_hash_table_created_failed_error"},

//TCAPCOMMON BUSINESS (module id 0x18) Error Code defined below
//......

//BSON ERROR(module id 0x1b) Error Code defined below
{BSON_ERR_TYPE_IS_NOT_MATCH, "the bson element type is not match."},
{BSON_ERR_INVALID_DATA_TYPE, "the bson element data type is invalid."},
{BSON_ERR_INVALID_VALUE, "the value of the bson element is invalid."},
{BSON_ERR_BSON_TYPE_UNMATCH_TDR_TYPE, "the bson data type is not match tdr type."},
{BSON_ERR_BSON_TYPE_IS_NOT_SUPPORT_BY_TCAPLUS, "the bson data type is not support by tcaplus."},
{BSON_ERR_BSON_ARRAY_COUNT_IS_INVALID, "the bson array count is invalid, perhaps it is greater than max count."},
{BSON_ERR_FAILED_TO_PARSE, "parse the bson string failed."},
{BSON_ERR_INVALID_FIELD_NAME_LENGTH, "the field name length is invalid, perhaps it is greater than the max field name length."},
{BSON_ERR_INDEX_FIELD_NAME_NOT_EXIST_WITH_ARRAY_TYPE, "the index field name is not exist, but the array field name and index field name must be a pair."},
{BSON_ERR_INVALID_ARRAY_INDEX, "the index of the array is invalid."},
{BSON_ERR_TDR_META_LIB_IS_NULL, "the meta lib is null."},
{BSON_ERR_MATCHED_COUNT_GREATER_THAN_ONE, "the matched count is greater than one in elemMatch include \"$$uniq\" field name and primary key field name."},
{BSON_ERR_NO_MATCHED, "there is no matched element according to $elemMatch."},
{BSON_ERR_GREATER_THAN_ARRAY_MAX_COUNT, "the array real count is greater than the array max count."},
{BSON_ERR_BSON_EXCEPTION, "An exception occurred in bson lib." },
{BSON_ERR_STD_EXCEPTION, "std::exception occured." },
{BSON_ERR_INVALID_KEY, "bson_err_invalid_key" },
{BSON_ERR_TDR_META_LIB_IS_INVALID, "bson_err_tdr_meta_lib_is_invalid" },


//TCAPTCAPCOMMON SYSTEM (module id 0x19) Error Code defined below
{COMMON_ERR_INVALID_ARGUMENTS, "common_invalid_arguments"},
{COMMON_ERR_INVALID_MEMBER_VARIABLE_VALUE, "common_invalid_member_variable_value"},
{COMMON_ERR_SPINLOCK_INIT_FAIL, "common_spinlock_init_fail"},
{COMMON_ERR_SPINLOCK_DESTROY_FAIL, "common_spinlock_destroy_fail"},
{COMMON_ERR_COMPRESS_BUF_NOT_ENOUGH, "common_compress_buf_is_not_enough"},
{COMMON_ERR_DECOMPRESS_BUF_NOT_ENOUGH, "common_decompress_buf_is_not_enough"},
{COMMON_ERR_DECOMPRESS_INVALID_INPUT, "when decompress the input is invalid"},
{COMMON_ERR_CANNOT_FIND_COMPRESS_ALGORITHM, "can't find the compress algorithm."},
{COMMON_ERR_CANNOT_FIND_DECOMPRESS_ALGORITHM, "can't find the decompress algorithm."},
{COMMON_ERR_COMPRESS_FAIL, "compress failed."},
{COMMON_ERR_DECOMPRESS_FAIL, "decompress failed."},
{COMMON_ERR_INVALID_SWITCH_VALUE, "invalid_switch_value."},
{COMMON_ERR_LINUX_SYSTEM_CALL_FAIL, "linux system call failed, such as fopen, fget, sscanf and so on."},
{COMMON_ERR_NOT_FIND_STAT_CACHE_VALUE, "can not find old stat cache value, such as cpu,network old stat cache info."},
{COMMON_ERR_LZO_CHECK_FAIL, "when use lzo to compress file, it's header contains magic,version,crc, it will check this values when decompress."},

// Non-error (for information purpose)
{COMMON_INFO_DATA_NOT_MODIFIED, "TCAPLUS_FLAG_FETCH_ONLY_IF_MODIFIED flag set and version equals, return early without real data"},
};
```

### 文件 tcaplus_protobuf_api.h
TcaplusDB PB API汇总头文件，主要包括了其它头文件，不详细介绍
```
#include "tcaplus_protobuf_define.h"
#include "cipher_suite_base.h"
#include "tcaplus_async_pb_api.h"
#include "tcaplus_coroutine_pb_api.h"
```

### 文件 tcaplus_protobuf_define.h
TcaplusDB PB API基础定义头文件，包括 ClientOptions，IndexGetRequest，IndexGetResponse定义
```
typedef struct 
{
    uint32_t app_id;                  // APPID业务id, 在开通游戏业务后获得
    char signature[64];               // APPKEY密钥, 在开通游戏业务后获得
    std::vector<uint32_t> zones;      // 开通的部署单元（区）列表
    std::vector<std::string> tables;  // 将要访问的表，并且确保在游戏存储中已经创建
    std::vector<std::string> dirs;    // 游戏存储TcaplusDB的接入地址，在开通游戏业务后获得
    int timeout;                      // 与后端链接或收包的超时时间，单位：毫秒ms
    char log_cfg[256];                // 日志定义文件路径，可以用相对路径
} ClientOptions;

/* Pb table Index Get request
 */
struct IndexGetRequest
{
    std::string m_strIndexName;
    ::google::protobuf::Message* m_pMsg;
    int m_iOffset;
    int m_iLimit;
};


/* Pb table Index Get response
 */
struct IndexGetResponse
{
    int m_nTotalNum;
    int m_nRemainNum;
    std::vector< ::google::protobuf::Message *> m_vecMsg;

    ~IndexGetResponse()
    {
        for(size_t i=0;i<m_vecMsg.size();++i)
        {
            delete m_vecMsg[i];
        }

        m_vecMsg.clear();
    }
};


enum
{
    MESSAGE_OPTION_VERSION_CHECK = 1,     // API中设定记录版本对比
    MESSAGE_OPTION_DATA_VERSION = 2,      // API中设置记录版本功能
    MESSAGE_OPTION_ASYNC_ID = 3,           // API中设置设置消息的异步ID
    MESSAGE_OPTION_MESSAGE_INVALID = 4,    // API中设置设置消息的无效(异步模式生效)
    MESSAGE_OPTION_MESSAGE_AUTO_RELEASE = 5,    // API中设置设置消息的自动释放(异步模式生效)
    MESSAGE_OPTION_USER_BUFF = 6,           // API中设置用户传入的自定义二进制数据
    MESSAGE_OPTION_CALLBACK_AUTO_RELEASE = 7,    // API中设置回调的自动释放(异步模式生效)
};
```

### 文件 tcaplusservice.optionv1.pb.h
Google Protobuf根据tcaplusservice.optionv1.proto用protoc生成的C++头文件，机器生成，不做详细价绍

### 文件 tcaplusservice.optionv1.proto
此文件为TcaplusDB定义表时用的公共定义，在本文件前面TcaplusDB Protobuf API 约定一节中已经介绍过，此处不再赘述。

