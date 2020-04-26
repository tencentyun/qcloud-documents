## 开发准备

### 相关资源
[GitHub地址](https://github.com/tencentyun/kms-cpp-sdk.git)，欢迎贡献代码以及反馈问题。

### 开发环境
1. [安装 openssl 的库和头文件](http://www.openssl.org/source/)。
2. [安装 libcurl](https://curl.haxx.se/download.html)。
3. [安装 cmake 工具](https://cmake.org/download/)。
4. 从控制台获取 AppID，SecretID，SecretKey。


### SDK配置
下载 github 上提供的源码，集成到您的开发环境。

执行下面的命令：

```
cd ${kms-cpp-sdk}
mkdir -p build 
cd build
cmake ..
make 
```

sample/kms_sample.cpp 里面有常见的 API 例子，生成的 kms_sample 可以直接运行，生成的 libKMS.a 和 libKMS.so 文件可以放到自己的 lib 文件夹下，inc目录拷贝到自己工程的 include 路径下。


## 生成客户端对象

``` 
string secretId="xxxxxx";    #替换为用户的 secretId
string secretKey = "xxxxxx"; #替换为用户的 secretKey
string endpoint = "https://kms-region.api.tencentyun.com"; # 替换为用户的 region , 例如 sh 表示上海， gz表示广州，bj表示北京
KMSAccount account(endpoint,secretId,secretKey);
```
### 初始化客户端配置
客户端默认使用 sha1 签名算法，可以调用签名算法修改签名方式

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
|KeyMetadata|struct|-|主密钥属性结构体，该参数返回创建的主密钥属性结构| 
|Description|string|None|主密钥描述|
|Alias|string|空字符串|主密钥别名|
|KeyUsage|string|'ENCRYPT/DECRYPT'|主密钥用途：默认是加解密|

返回值 KeyMetadata 结构体 描述如下：

| 属性名称 | 类型 | 含义 |
|---------|---------|---------|
|KeyId|string|密钥 ID|
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
|KeyId|string|None|主密钥 ID|
|KeyMetadata|struct|无|主密钥属性结构体，该参数返回创建的主密钥属性结构| 

返回值 KeyMetadata 结构体 描述如下：

| 属性名称 | 类型 | 含义 |
|---------|---------|---------|
|KeyId|string|密钥 ID|
|CreateTime|uinx time|创建时间|
|Description|string|密钥描述|
|KeyState|string|密钥状态|
|KeyUsage|string|密钥用途|
|Alias|string|密钥别名|

#### 使用示例

```
KeyMetadata meta;
string keyId=""  # 请填写您的keyId
account.get_key_attributes(meta.KeyId,meta);
```

### 设置主密钥属性
#### 方法原型

```
void set_key_attributes(const string & KeyId, const string & Alias);
```

#### 参数说明

| 参数名 | 类型 | 默认值 | 参数描述 |
|---------|---------|---------|---------|
|KeyId|string|None|主密钥 ID|
|Alias|string|无|主密钥属性结构体，该参数返回创建的主密钥属性结构| 


#### 使用示例

```
Alias = "For test";
account.set_key_attributes(KeyId, Alias);
```

### 获取主密钥列表
#### 方法原型

```
void list_key(vector<string> & keyIds, const int offset= 0 , const int limit = 10);
```

#### 参数说明

| 参数名 | 类型 | 默认值 | 参数描述 |
|---------|---------|---------|---------|
|keyIds|vector|无|返回 keyid vector|
|offset|int|0|返回列表偏移值|
|limit|int|10|本次返回列表限制个数，不填写默认为返回 10 个|

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
|KeyId|string|None|主密钥 ID|
|KeySpec|string|None|生成数据密钥算法|
|NumberOfBytes|int|None|生成指定长度的数据密钥|
|EncryptionContext|json string |无|生成数据密钥时提供的额外的 json key-value|
|Plaintext|string|无|生成的数据密钥明文|
|CiphertextBlob|string|无|生成的数据密钥密文|

返回值(入参中)

|参数名|类型|参数描述|
|---------|---------|---------|
|plaintext|string| 表示生成的数据密钥明文|
|ciphertextBlob|string|表示生成的数据密钥密文|

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
|KeyId|string|None|主密钥 ID|

返回值：无

#### 使用示例

```
string KeyId= ""  // 请填写您的keyId;
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
|KeyId|string|None|主密钥 ID|

返回值：无。
#### 使用示例

```
string KeyId= ""  // 请填写您的keyId;
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
|KeyId|string|None|主密钥 ID|
|Plaintext|string|空字符串|明文|
|EncryptionContext|string|None|key/value 对的 json 字符串，如果指定了该参数，则在调用 Decrypt API 时需要提供同样的参数|

返回值  

|参数名|类型|参数描述|
|---------|---------|---------|
|ciphertextBlob|string|表示生成的密文|



#### 使用示例

```
string KeyId = "" ; // 请填写您的keyId;
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
|EncryptionContext|string|None|key/value 对的 json 字符串，如果指定了该参数，则在调用 Decrypt API 时需要提供同样的参数。|

返回值  

|参数名|类型|参数描述|
|---------|---------|---------|
|plaintext|string|表示通过密文解密得到的明文|

#### 使用示例

```
Plaintext = account.decrypt(CiphertextBlob,"");
```



