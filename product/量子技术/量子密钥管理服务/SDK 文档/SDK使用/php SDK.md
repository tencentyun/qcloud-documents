## 开发准备

### 相关资源
[GitHub 地址](https://github.com/tencentyun/kms-php-sdk.git) ,欢迎贡献代码以及反馈问题。

### 开发环境
1. 依赖环境：PHP5.3.0 版本及以上
2. 从控制台获取 AppID，SecretID，SecretKey。


## 生成客户端对象

``` 
    // 从腾讯云官网查看云 API 的密钥信息
    $secretId = "";
    $secretKey = "";
    $endPoint = "";
    $kms_account = new KMSAccount($endPoint,$secretId,$secretKey);
```
### 初始化客户端配置
客户端默认使用 sha1 签名算法，可以调用签名算法修改签名方式。

```
    account.set_sign_method("sha256");
```

## 密钥管理操作
### 创建主密钥
#### 方法原型

```
    public function create_key($Alias = NULL, $Description = NULL, $KeyUsage="ENCRYPT/DECRYPT")
```

#### 参数说明

| 参数名 | 类型 | 默认值 | 参数描述 |
|---------|---------|---------|---------|
|Description|string|NULL|主密钥描述|
|Alias|string|NULL|主密钥别名|
|KeyUsage|string|'ENCRYPT/DECRYPT'|主密钥用途：默认是加解密|

#### 返回值 KeyMetadata 结构体，描述如下：

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
    $Description = "test";
    $Alias = "test";
    $KeyUsage= "ENCRYPT/DECRYPT";
    $kms_meta = $kms_account->create_key($Alias,$Description,$KeyUsage);
```

### 获取主密钥属性
#### 方法原型

```
    public function get_key_attributes($KeyId = NULL)
```

#### 参数说明

| 参数名 | 类型 | 默认值 | 参数描述 |
|---------|---------|---------|---------|
|KeyId|string|None|主密钥 ID|

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
    string keyId=""  # 请填写您的 keyId
    $kms_meta = $kms_account->get_key_attributes($keyId);
```

### 设置主密钥属性
#### 方法原型

```
    public function set_key_attributes($KeyId = NULL, $Alias)
```

#### 参数说明

| 参数名 | 类型 | 默认值 | 参数描述 |
|---------|---------|---------|---------|
|KeyId|string|None|主密钥 ID|
|Alias|string|无|设置的主密钥别名|

#### 返回值：无

#### 使用示例

```
    $Alias = "for test" ;
    $kms_account->set_key_attributes($kms_meta->KeyId,$Alias);
```

### 获取主密钥列表
#### 方法原型

```
    public function list_key($offset = 0, $limit = 10)
```

#### 参数说明

| 参数名 | 类型 | 默认值 | 参数描述 |
|---------|---------|---------|---------|
|keyIds|vector|无|返回 keyid vector|
|offset|int|0|返回列表偏移值|
|limit|int|10|本次返回列表限制个数，不填写默认为返回10个|

#### 使用示例

```
     $ret_pkg = $kms_account->list_key(); 
```
### 生成数据密钥
#### 方法原型

```
    public function generate_data_key($KeyId = NULL, $KeySpec = "", $NumberOfBytes = 1024,$EncryptionContext =NULL)
```

#### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥 ID|
|KeySpec|string|""|生成数据密钥算法|
|NumberOfBytes|int|1024|生成指定长度的数据密钥|
|EncryptionContext|string |NULL|生成数据密钥时提供的额外的json key-value|

#### 返回值

|参数名|类型|参数描述|
|---------|---------|---------|
|plaintext|string| 表示生成的数据密钥明文(输入参数返回)|
|ciphertextBlob|string|表示生成的数据密钥密文|

#### 使用示例

```
       $KeySpec = "AES_128";
       $ret_pkg = $kms_account->generate_data_key($kms_meta->KeyId,$KeySpec,1024,"");
       $Plaintext = $ret_pkg['plaintext'];
       $CiphertextBlob = $ret_pkg['ciphertextBlob'];
```
### 启用主密钥
#### 方法原型

```
    public function enable_key($KeyId = NULL)
```

#### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥 ID|

#### 返回值：无

#### 使用示例

```
    $KeyId= ""  // 请填写您的keyId;
    $kms_account->enable_key($KeyId);
```
### 禁用主密钥
#### 方法原型

```
    public function disable_key($KeyId= NULL)
```

#### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|None|主密钥 ID|


#### 返回值：无

#### 使用示例

```
    $KeyId= ""  // 请填写您的 keyId;
    $kms_account->disable_key($KeyId);
```

## 加解密操作
### 加密
#### 方法原型

```
    public function encrypt($KeyId = NULL, $Plaintext=NULL,$EncryptionContext =NULL)
```

#### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|KeyId|string|NULL|主密钥 ID|
|Plaintext|string|NULL|明文|
|EncryptionContext|string|NULL|key/value 对的 json 字符串，如果指定了该参数，则在调用 Decrypt API 时需要提供同样的参数|

#### 返回值

|参数名|类型|参数描述|
|---------|---------|---------|
|ciphertextBlob|string|表示生成的密文|

#### 使用示例

```
    $CiphertextBlob = $kms_account->encrypt($KeyId,$Plaintext);
```
### 解密
#### 方法原型

```
    public function decrypt($CiphertextBlob = NULL,$EncryptionContext = NULL)
```

#### 参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|CiphertextBlob|string|NULL|密文|
|EncryptionContext|string|NULL|key/value 对的 json 字符串，如果指定了该参数，则在调用 Decrypt API 时需要提供同样的参数。|

#### 返回值  

|参数名|类型|参数描述|
|---------|---------|---------|
|plaintext|string|表示通过密文解密得到的明文|

#### 使用示例

```
     $Plaintext = $kms_account->decrypt($CiphertextBlob);
```



