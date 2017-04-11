# PHP sdk
## 开发准备

### 相关资源
-[GitHub地址](https://github.com/tencentyun/kms-php-sdk.git) ,欢迎贡献代码以及反馈问题。

-[C++ sdk 本地下载]()
### 开发环境
1. 依赖环境：PHP5.3.0版本及以上
2. 从控制台获取APP ID, SecretID,SecretKey。


### SDK配置
下载github上提供的源码，集成到您的开发环境。

执行下面的命令：

```
    cd ${kms-cpp-sdk}
    mkdir -p build 
    cd build
    cmake ..
    make 
```

sample/kms_sample.cpp里面有常见的api例子，生成的kms_sample可以直接运行，生成的libKMS.a 和libKMS.so文件可以放到自己的lib文件夹下，inc目录拷贝到自己工程的include路径下。
### 历史版本

## 生成客户端对象

``` 
    string secretId="xxxxxx;    #替换为用户的secretId
    string secretKey = "xxxxxx"; #替换为用户的secretKey
    string endpoint = "https://kms-region.api.tencentyun.com"; # 替换为用户的region , 例如 sh 表示上海， gz表示广州，bj表示北京
    KMSAccount account(endpoint,secretId,secretKey);
```
### 初始化客户端配置
客户端默认使用sha1 签名算法，可以调用签名算法修改签名方式

```
    account.set_sign_method("sha256");
```

## 密钥管理操作
### 创建主密钥
#### 方法原型

```
    void create_key(KeyMetadata & meta,const string &Description="",const string & Alias = "" , const string  & KeyUsage="ENCRYPT/DECRYPT");
```

#### 参数说明

| 参数名 | 类型 | 默认值 | 参数描述 |
|---------|---------|---------|---------|
|KeyMetadata|struct||主密钥属性结构体，该参数返回创建的主密钥属性结构| 
|Description|string|None|主密钥描述|
|Alias|string|空字符串|主密钥别名|
|KeyUsage|string|'ENCRYPT/DECRYPT'|主密钥用途：默认是加解密|

返回值 KeyMetadata结构体 描述如下：

| 属性名称 | 类型 | 含义 |
|---------|---------|---------|
|KeyId|string|密钥id|
|CreateTime|uinx time|创建时间|
|Description|string|密钥描述|
|KeyState|string|密钥状态|
|KeyUsage|string|密钥用途|
|Alias|string|密钥别名|

#### 使用示例

```
    KeyMetadata meta ;
    string description ="test";
    string alias = "kms_test";
    string KeyUsage="ENCRYPT/DECRYPT";
    account.create_key(meta,Description,Alias,KeyUsage);
```

### 获取主密钥属性
#### 方法原型

```
    void get_key_attributes(const string & KeyId, KeyMetadata & meta);
```

#### 参数说明

| 参数名 | 类型 | 默认值 | 参数描述 |
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id|
|KeyMetadata|struct||主密钥属性结构体，该参数返回创建的主密钥属性结构| 

返回值 KeyMetadata结构体 描述如下：

| 属性名称 | 类型 | 含义 |
|---------|---------|---------|
|KeyId|string|密钥id|
|CreateTime|uinx time|创建时间|
|Description|string|密钥描述|
|KeyState|string|密钥状态|
|KeyUsage|string|密钥用途|
|Alias|string|密钥别名|

#### 使用示例

```
    KeyMetadata meta;
    string keyId=""  # 请填写你的keyId
    account.get_key_attributes(meta.KeyId,meta);
```

### 获取主密钥列表
#### 方法原型

```
    void list_key(vector<string> & keyIds, const int offset= 0 , const int limit = 10);
```

#### 参数说明

| 参数名 | 类型 | 默认值 | 参数描述 |
|---------|---------|---------|---------|
|keyIds|vector|无|返回keyid vector|
|offset|int|0|返回列表偏移值|
|limit|int|10|本次返回列表限制个数，不填写默认为返回10个|

#### 使用示例

```
     vector<string> KeyIds;
     account.list_key(KeyIds);
     for(unsigned int i = 0 ; i < KeyIds.size(); ++i)
         cout<<"the "<<i<<" key id is :"<<KeyIds[i]<<endl;
```
### 生成数据密钥
#### 方法原型

```
    void generate_data_key( string &KeyId, const string & KeySpace, int NumberOfBytes,const string & EncryptionContext,string & Plaintext,string &CiphertextBlob);
```

#### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id|
|KeySpec|string|None|生成数据密钥算法|
|NumberOfBytes|int|None|生成指定长度的数据密钥|
|EncryptionContext|json string |无|生成数据密钥时提供的额外的json key-value|
|Plaintext|string|无|生成的数据密钥明文|
|CiphertextBlob|string|无|生成的数据密钥密文|

返回值 入参中：
plaintext 表示生成的数据密钥明文
ciphertextBlob：表示生成的数据密钥密文

#### 使用示例

```
       string KeySpec="AES_128";
       string Plaintext,CiphertextBlob;
       account.generate_data_key(meta.KeyId,KeySpec,1024,"",Plaintext, CiphertextBlob);
```
### 启用主密钥
#### 方法原型

```
    void enable_key(const string & KeyId);
```

#### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id|

返回值 无

#### 使用示例

```
    string KeyId= ""  // 请填写你的keyId;
    account.enable_key(KeyId)
```
### 禁用主密钥
#### 方法原型

```
    void disable_key(const string & KeyId);
```

#### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id|

返回值 无
#### 使用示例

```
    string KeyId= ""  // 请填写你的keyId;
    account.disable_key(KeyId)
```

## 加解密操作
### 加密
#### 方法原型

```
    string encrypt(const string &KeyId , const string & plaintext, const string & EncryptionContext);
```

#### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥Id|
|Plaintext|string|空字符串|明文|
|EncryptionContext|string|None|key/value对的json字符串，如果指定了该参数，则在调用Decrypt API时需要提供同样的参数|

返回值 ciphertextBlob 密文：

#### 使用示例

```
    string KeyId = "" ; // 请填写你的keyId;
    string Plaintest = "test message data"
    string CiphertextBlob = account.encrypt(KeyId,Plaintest,"");
```
### 解密
#### 方法原型

```
    string decrypt(const string & CiphertextBlob, const string & EncryptionContext);
```

#### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|CiphertextBlob|string|空字符串|密文|
|EncryptionContext|string|None|key/value对的json字符串，如果指定了该参数，则在调用Decrypt API时需要提供同样的参数。|

返回值  plaintext 明文：

#### 使用示例

```
     Plaintext = account.decrypt(CiphertextBlob,"");
```



