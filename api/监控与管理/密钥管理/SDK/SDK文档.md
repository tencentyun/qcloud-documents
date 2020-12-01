
为了方便开发者更好地使用 KMS 的 SDK，腾讯云提供以下使用说明文档：


## 示例：Python SDK 使用简介

### 环境依赖
请确保已经安装了 Python 环境。

### KMS Python SDK 下载与配置
#### 云 API 密钥使用说明
使用 Python SDK 时，首先需要用户的云 API 密钥，云 API 密钥是对用户身份的合法性验证。获取云 API 密钥的方法如下：登录[腾讯云控制台](https://console.cloud.tencent.com/)，选择【云产品】-【云 API 密钥】选项
![](https://mc.qcloudimg.com/static/img/b04d51df61bc4e9259dcee293981b644/5.png)

用户可在此新建新的云 API 密钥或使用现有密钥。单击密钥 ID 进入详情页获取使用的密钥 secretId 和对应的 secretKey。
![](https://mc.qcloudimg.com/static/img/47b2cf18add4d32a867f115fffb6af48/2.png)

#### endpoint 说明
endpoint 是使用 KMS 服务的访问地址，同时 endpoint 中也包含了使用的协议，endpoint的格式如下：

- 内网：`https://kms-region.api.tencentyun.com`
- 外网：`https://kms-region.api.qcloud.com`


#### region 说明
region 需要使用具体地域进行替换，有如下三个地区：gz(广州)，sh(上海)，bj(北京)。划分不同地域有助于不同地域的用户就近选择，提供更好的服务。公共参数中的 region 值要与域名的 region 值保持一致，如果出现不一致的情况，以域名的 region 值为准，将请求发往域名 region 所指定的地域。

#### 内外网区别
如果业务进程也部署在腾讯云的 CVM 子机上，强烈建议使用同地域的内网 endpoint：
1) 同地域内网的时延更低。
2) 目前 KMS 对于公网下行流量是要收取流量费用的，用内网可以节省这部分的费用。


#### Python SDK下载
下载最新版[KMS SDK](https://cloud.tencent.com/document/product/573/8908)。

### 使用 KMS Python SDK

下面的代码也是 Python SDK 中的 sample，从创建主密钥、生成数据密钥，加解密，启用禁用密钥等操作来示例密钥管理的操作。

```
#首先从控制台获取对应的secretId和secretKey。和对应的endpoint
try:
	secretId = "your secret id"
	secretKey = "your secret key"
	endpoint = "your endpoint "

	kms_account = KMSAccount(endpoint, secretId, secretKey)

	# create a custom master key
	Description = "test"
	Alias = "test"
	KeyUsage = "ENCRYPT/DECRYPT"
	kms_meta = kms_account.create_key(Description, Alias, KeyUsage)
	print kms_meta

	# create a data key
	KeySpec = "AES_128"
	Plaintext , CiphertextBlob = kms_account.generate_data_key(kms_meta.KeyId, KeySpec)
	print "the data key : %s \n  the encrypted data key :%s\n" % (Plaintext, CiphertextBlob)

	# encrypt the data string
	Plaintest = "test message data"
	CiphertextBlob = kms_account.encrypt(kms_meta.KeyId, Plaintest)
	print "the encrypted data is :%s \n" % CiphertextBlob

	# decrypt the encrypted data string
	Plaintest = kms_account.decrypt(CiphertextBlob)
	print "the decrypted data is :%s\n" % Plaintest

	# get key attributes
	key_meta = kms_account.get_key_attributes(key_meta.KeyId)
	print key_meta

	# set key attributes
	Alias = "ForTest"
	kms_account.set_key_attributes(key_meta.KeyId, Alias)

	# disabke a custom key
	kms_account.disable_key(key_meta.KeyId)
	# enable a custom key
	kms_account.enable_key(key_meta.KeyId)

	# list key
	totalCount, keys = kms_account.list_key()
	print keys

except KMSExceptionBase, e:
	print "Exception:%s\n" % e
```
