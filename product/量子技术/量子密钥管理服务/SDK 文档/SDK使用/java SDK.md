## 开发准备

### 相关资源
[GitHub 地址](https://github.com/tencentyun/kms-java-sdk)，欢迎贡献代码以及反馈问题。

### 环境依赖
JDK1.7


## 生成客户端对象

``` 
    //从腾讯云官网查询的云 API 密钥信息
    String secretId="";
    String secretKey="";
    String endpoint = "";       
    KMSAccount account = new KMSAccount(endpoint,secretId, secretKey);
```
### 初始化客户端配置
客户端默认使用 sha1 签名算法，可以调用签名算法修改签名方式。

```
    account.setSignMethod("sha256");
```

## 密钥管理操作
### 创建主密钥
#### 方法原型

```
    public KeyMetadata create_key(String Description,String Alias ,String KeyUsage) throws Exception
```

#### 参数说明

| 参数名 | 类型 | 默认值 | 参数描述 |
|---------|---------|---------|---------|
|Description|string|无|主密钥描述|
|Alias|string|无|主密钥别名|
|KeyUsage|string|无|主密钥用途：默认是加解密|

#### 返回值 KeyMetadata结构体 描述如下：

| 属性名称 | 类型 | 含义 |
|---------|---------|---------|
|KeyId|string|密钥 Id|
|CreateTime|uinx time|创建时间|
|Description|string|密钥描述|
|KeyState|string|密钥状态|
|KeyUsage|string|密钥用途|
|Alias|string|密钥别名|

#### 使用示例

```
    String Description = "test";
    String Alias= "test";
    String KeyUsage = "ENCRYPT/DECRYPT";
    KeyMetadata meta = account.create_key(Description , Alias , KeyUsage);
```

### 获取主密钥属性
#### 方法原型

```
    public KeyMetadata get_key_attributes(String KeyId) throws Exception
```

#### 参数说明

| 参数名 | 类型 | 默认值 | 参数描述 |
|---------|---------|---------|---------|
|KeyId|string|无|主密钥 Id|

#### 返回值 KeyMetadata结构体 描述如下：

| 属性名称 | 类型 | 含义 |
|---------|---------|---------|
|KeyId|string|密钥 Id|
|CreateTime|uinx time|创建时间|
|Description|string|密钥描述|
|KeyState|string|密钥状态|
|KeyUsage|string|密钥用途|
|Alias|string|密钥别名|

#### 使用示例

```
    meta = account.get_key_attributes(KeyId);
```

### 设置主密钥属性
#### 方法原型

```
    public void set_key_attributes(String KeyId , String Alias) throws Exception
```

#### 参数说明

| 参数名 | 类型 | 默认值 | 参数描述 |
|---------|---------|---------|---------|
|KeyId|string|无|主密钥 Id|
|Alias|string|无|主密钥别名|

#### 返回值：无

#### 使用示例

```
    Alias = "for test";
    account.set_key_attributes(KeyId, Alias);
```


### 获取主密钥列表
#### 方法原型

```
    public void  list_key(int offset, int limit,List<String> KeyList) throws Exception
```

#### 参数说明

| 参数名 | 类型 | 默认值 | 参数描述 |
|---------|---------|---------|---------|
|offset|int|0|返回列表偏移值。|
|limit|int|10|本次返回列表限制个数，不填写默认为返回 10 个。|
|KeyList|list|无|本次返回的 KeyId 列表。|

#### 使用示例

```
    ArrayList<String> KeyId  = new ArrayList<String>();
    account.list_key(-1,-1,KeyId);
    for(int i = 0 ; i < KeyId.size(); ++i)
    	System.out.println("the " +Integer.toString(i) + "Key id is " + KeyId.get(i));
```
### 生成数据密钥
#### 方法原型

```
    public String generate_data_key(String KeyId, String KeySpec, int NumberOfBytes , String EncryptionContext,String Plaintext ) throws Exception
```

#### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥 Id。|
|KeySpec|string|None|生成数据密钥算法。|
|NumberOfBytes|int|None|生成指定长度的数据密钥。|
|EncryptionContext|string|None|生成数据密钥时提供的额外的 json key-value。|
|Plaintext|string|无|生成的数据密钥明文。|

#### 返回值 

|参数名|类型|参数描述|
|---------|---------|---------|
|plaintext|string| 表示生成的数据密钥明文(输入参数返回)|
|ciphertextBlob|string|表示生成的数据密钥密文|

#### 使用示例

```
   String KeySpec = "AES_128";
   String Plaintext  = "";   		
   String CiphertextBlob = account.generate_data_key(meta.KeyId, KeySpec,1024,"",Plaintext);
   System.out.println("the data key string is " + Plaintext);
   System.out.println("the encrypted data key string is "+CiphertextBlob);
```
### 启用主密钥
#### 方法原型

```
    public void enable_key(String KeyId) throws Exception
```

#### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥 Id|

#### 返回值：无

#### 使用示例

```
    account.enable_key(KeyId);
```
### 禁用主密钥
#### 方法原型

```
    public void disable_key(String KeyId) throws Exception
```

#### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥 Id|

#### 返回值：无
#### 使用示例

```
    account.disable_key(KeyId);
```

## 加解密操作
### 加密
#### 方法原型

```
    def encrypt(self, KeyId=None, Plaintext="", EncryptionContext=None)
```

#### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥 Id|
|Plaintext|string|空字符串|明文|
|EncryptionContext|string|None|key/value 对的 json 字符串，如果指定了该参数，则在调用 Decrypt API 时需要提供同样的参数。|

#### 返回值 

|参数名|类型|参数描述|
|---------|---------|---------|
|ciphertextBlob|string|表示生成的密文|

#### 使用示例

```
    CiphertextBlob  = account.encrypt(KeyId, Plaintext,"");
    System.out.println("the encrypted data is " + CiphertextBlob);
```
### 解密
#### 方法原型

```
    public String decrypt(String CiphertextBlob , String EncryptionContext)throws Exception
```

#### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|CiphertextBlob|string|空字符串|密文|
|EncryptionContext|string|None|key/value 对的 json 字符串，如果指定了该参数，则在调用 Decrypt API 时需要提供同样的参数。|

#### 返回值  

|参数名|类型|参数描述|
|---------|---------|---------|
|plaintext|string|表示通过密文解密得到的明文|

#### 使用示例

```
    Plaintext = account.decrypt( Plaintext,"");
    System.out.println("the decrypted data is " + Plaintext);
```



