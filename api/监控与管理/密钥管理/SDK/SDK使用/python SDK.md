# Python sdk
##开发准备

###相关资源
-[GitHub地址]() ,欢迎贡献代码以及反馈问题。

-[python sdk 本地下载]()
###环境依赖
python2.7 目前不支持python3

获取python版本的方法：

linux shell 

```

    $python -V

    Python 2.7.11
```

windows cmd

```
   
    D:>python -V
    Python 2.7.11
```

如果提示不是内部或者外部命令，请先在window环境变量PATH里面添加上python的绝对路径

###历史版本

##生成客户端对象

```
    
    secretId='xxxxxx'    #替换为用户的secretId
    secretKey = 'xxxxxx' #替换为用户的secretKey
	endpoint = 'https://kms-region.api.tencentyun.com' # 替换为用户的region , 例如 sh 表示上海， gz表示广州，bj表示北京
    kms_account = KMSAccount(endpoint,secretId,secretKey)
```
###初始化客户端配置
客户端默认使用sha1 签名算法，可以调用签名算法修改签名方式

```

	kms_account.set_sign_method('sha256')

```

##密钥管理操作
###创建主密钥
####方法原型

```

	def create_key(self, Description=None, Alias="", KeyUsage='ENCRYPT/DECRYPT'):
```

####参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|Description|string|None|主密钥描述|
|Alias|string|空字符串|主密钥别名|
|KeyUsage|string|'ENCRYPT/DECRYPT'|主密钥用途：默认是加解密|

返回值 KeyMetadata结构体 描述如下：

|属性名称|类型|含义|
|---------|---------|---------|
|KeyId|string|密钥id|
|CreateTime|uinx time|创建时间|
|Description|string|密钥描述|
|KeyState|string|密钥状态|
|KeyUsage|string|密钥用途|
|Alias|string|密钥别名|

####使用示例

```
	
	description ='for test'
	alias = 'kms_test'
	kms_meta = kms_account.create_key(description,alias)
```

###获取主密钥属性
####方法原型

```

	def create_key(self, Description=None, Alias="", KeyUsage='ENCRYPT/DECRYPT'):
```

####参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|Description|string|None|主密钥描述|
|Alias|string|空字符串|主密钥别名|
|KeyUsage|string|'ENCRYPT/DECRYPT'|主密钥用途：默认是加解密|

返回值 KeyMetadata结构体 描述如下：

|属性名称|类型|含义|
|---------|---------|---------|
|KeyId|string|密钥id|
|CreateTime|uinx time|创建时间|
|Description|string|密钥描述|
|KeyState|string|密钥状态|
|KeyUsage|string|密钥用途|
|Alias|string|密钥别名|

####使用示例

```
	
	description ='for test'
	alias = 'kms_test'
	kms_meta = kms_account.create_key(description,alias)
```

###获取主密钥列表
####方法原型

```

	def create_key(self, Description=None, Alias="", KeyUsage='ENCRYPT/DECRYPT'):
```

####参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|Description|string|None|主密钥描述|
|Alias|string|空字符串|主密钥别名|
|KeyUsage|string|'ENCRYPT/DECRYPT'|主密钥用途：默认是加解密|

返回值 KeyMetadata结构体 描述如下：

|属性名称|类型|含义|
|---------|---------|---------|
|KeyId|string|密钥id|
|CreateTime|uinx time|创建时间|
|Description|string|密钥描述|
|KeyState|string|密钥状态|
|KeyUsage|string|密钥用途|
|Alias|string|密钥别名|

####使用示例

```
	
	description ='for test'
	alias = 'kms_test'
	kms_meta = kms_account.create_key(description,alias)
```
###生成数据密钥
####方法原型

```

	def create_key(self, Description=None, Alias="", KeyUsage='ENCRYPT/DECRYPT'):
```

####参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|Description|string|None|主密钥描述|
|Alias|string|空字符串|主密钥别名|
|KeyUsage|string|'ENCRYPT/DECRYPT'|主密钥用途：默认是加解密|

返回值 KeyMetadata结构体 描述如下：

|属性名称|类型|含义|
|---------|---------|---------|
|KeyId|string|密钥id|
|CreateTime|uinx time|创建时间|
|Description|string|密钥描述|
|KeyState|string|密钥状态|
|KeyUsage|string|密钥用途|
|Alias|string|密钥别名|

####使用示例

```
	
	description ='for test'
	alias = 'kms_test'
	kms_meta = kms_account.create_key(description,alias)
```
###启用主密钥
####方法原型

```

	def create_key(self, Description=None, Alias="", KeyUsage='ENCRYPT/DECRYPT'):
```

####参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|Description|string|None|主密钥描述|
|Alias|string|空字符串|主密钥别名|
|KeyUsage|string|'ENCRYPT/DECRYPT'|主密钥用途：默认是加解密|

返回值 KeyMetadata结构体 描述如下：

|属性名称|类型|含义|
|---------|---------|---------|
|KeyId|string|密钥id|
|CreateTime|uinx time|创建时间|
|Description|string|密钥描述|
|KeyState|string|密钥状态|
|KeyUsage|string|密钥用途|
|Alias|string|密钥别名|

####使用示例

```
	
	description ='for test'
	alias = 'kms_test'
	kms_meta = kms_account.create_key(description,alias)
```
###禁用主密钥
####方法原型

```

	def create_key(self, Description=None, Alias="", KeyUsage='ENCRYPT/DECRYPT'):
```

####参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|Description|string|None|主密钥描述|
|Alias|string|空字符串|主密钥别名|
|KeyUsage|string|'ENCRYPT/DECRYPT'|主密钥用途：默认是加解密|

返回值 KeyMetadata结构体 描述如下：

|属性名称|类型|含义|
|---------|---------|---------|
|KeyId|string|密钥id|
|CreateTime|uinx time|创建时间|
|Description|string|密钥描述|
|KeyState|string|密钥状态|
|KeyUsage|string|密钥用途|
|Alias|string|密钥别名|

####使用示例

```
	
	description ='for test'
	alias = 'kms_test'
	kms_meta = kms_account.create_key(description,alias)
```
##加解密操作
###加密
####方法原型

```

	def create_key(self, Description=None, Alias="", KeyUsage='ENCRYPT/DECRYPT'):
```

####参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|Description|string|None|主密钥描述|
|Alias|string|空字符串|主密钥别名|
|KeyUsage|string|'ENCRYPT/DECRYPT'|主密钥用途：默认是加解密|

返回值 KeyMetadata结构体 描述如下：

|属性名称|类型|含义|
|---------|---------|---------|
|KeyId|string|密钥id|
|CreateTime|uinx time|创建时间|
|Description|string|密钥描述|
|KeyState|string|密钥状态|
|KeyUsage|string|密钥用途|
|Alias|string|密钥别名|

####使用示例

```
	
	description ='for test'
	alias = 'kms_test'
	kms_meta = kms_account.create_key(description,alias)
```
###解密
####方法原型

```

	def create_key(self, Description=None, Alias="", KeyUsage='ENCRYPT/DECRYPT'):
```

####参数说明

|参数名|类型|默认值|参数描述|
|---------|---------|---------|---------|
|Description|string|None|主密钥描述|
|Alias|string|空字符串|主密钥别名|
|KeyUsage|string|'ENCRYPT/DECRYPT'|主密钥用途：默认是加解密|

返回值 KeyMetadata结构体 描述如下：

|属性名称|类型|含义|
|---------|---------|---------|
|KeyId|string|密钥id|
|CreateTime|uinx time|创建时间|
|Description|string|密钥描述|
|KeyState|string|密钥状态|
|KeyUsage|string|密钥用途|
|Alias|string|密钥别名|

####使用示例

```
	
	description ='for test'
	alias = 'kms_test'
	kms_meta = kms_account.create_key(description,alias)
```


腾讯云KMS目前支持 java、python、php 及 C++ SDK, 后续会支持更多语言。也欢迎广大开发者根据 API 说明开发更多语言的 SDK 版本。

下载地址如下：

- [java sdk](http://cmqsdk-10016717.cos.myqcloud.com/qc_cmq_java_sdk_V1.0.2.zip)


- [python sdk](http://cmqsdk-10016717.cos.myqcloud.com/qc_cmq_python_sdk_V1.0.2.zip)


- [php sdk](http://cmqsdk-10016717.cos.myqcloud.com/qc_cmq_php_sdk_V1.0.2.zip)


- [c++ sdk](http://cmqsdk-10016717.cos.myqcloud.com/qc_cmq_cpp_sdk_V1.0.2.zip)


## SDK使用注意事项

使用SDK前至少要获取[secret id](https://console.qcloud.com/capi)， [secret key](https://console.qcloud.com/capi)，endpoint（即请求发到哪个地域，走内网还是外网）。

endpoint 说明：
	
内网endpoint：https://kms-region.api.tencentyun.com

公网endpoint：https://kms-region.api.qcloud.com

- 如果业务进程也部署在腾讯云的 CVM 子机上，强烈建议使用同地域的内网 endpoint。例如在腾讯云北京地域的 CVM 子机则建议您使用 `https://kms-bj.api.tencentyun.com`。
原因是：1）同地域内网时延更低；2）目前消息队列对于公网下行流量是要收取流量费用的，用内网可以节省这部分的费用。
- region 需用具体地域替换：gz（广州），sh（上海），bj（北京）。公共参数中的 region 值要与域名的 region 值保持一致，如果出现不一致的情况，以域名的 region 值为准，将请求发往域名 region 所指定的地域。
