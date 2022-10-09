## 获取方式
go 语言的源代码：[resource_code](https://zhixinliantest-1302317679.cos.ap-guangzhou.myqcloud.com/nft/nft/nft_wallet_service/resources/2021-10-27/nft_wallet_service)（下载后缀修改成 .zip 文件）

## 场景描述
- 生成公私钥：调用生成助记词接口生成助记词（如有助记词，可跳过），调用派生生成子公私钥对接口。
- 鉴权：用户通过调用 GenerateApiSign 接口生成鉴权信息，将鉴权信息填入请求头。

## 相关接口 



### 调用至信链接口前生成签名数据接口 
GenerateApiSign(secretId, secretKey string)(signData*SignData, nonce int, error)

#### 输入参数
|字段名|描述|
|:--|:--|
|secretId |注册用户时生成的 secretId（方案二该参数传""）|
|secretKey|注册用户时生成的 secretKey（方案二该参数传""）|

#### 返回参数
|字段名|描述|
|:--|:--|
|signData|生成各项签名数据|

signData 结构如下：

|字段名|描述|
|:--|:--|
|signature|签名后的数据|
|signatureTime|时间戳|
|nonce|随机数|

#### 方案一：
需要准备：

|字段名|类型|
|:--|:--|
|secretId|string|
|secretKey|string|

调用 GenerateApiSign 方法生成签名，将相关字段放到 Header 中：

|字段名|类型|
|:--|:--|
|Secret-Id|string|
|signature-Time|string|
|signature|string|
|nonce|int|

#### 方案二：
直接调用 GenerateApiSign 方法生成签名，将相关字段放到 Header 中：

|字段名|类型|
|:--|:--|
|signature-Time|string|
|signature|string|
|nonce|int|


---
### 生成助记词
createMnemonic() (mnemonic string, err)

#### 输入参数
无
 
#### 返回参数

|字段名|描述|
|:--|:--|
|mnemonic|12 个英文词组，utf8，空格分割 |


---
### 派生生成子公私钥对
DeriveKeyPair(mnemonic string, index int) (|priKey, pubKey string,err)

#### 输入参数
|字段名|描述|
|:--|:--|
|mnemonic|12 个英文单词，空格分割|
|index|   从 0 开始递增的序号，相同的 index 生成的子公私钥相同|

#### 响应参数
|字段名|描述|
|:--|:--|
|priKey|私钥|
|pubKey|公钥|


---
### 私钥生成对应公钥
PriKey2PubKey(pri string) (pub string,err)

#### 输入参数
|字段名|描述|
|:--|:--|
 |pri|私钥 |

#### 响应参数
|字段名|描述|
|:--|:--|
 |pub|公钥|


---
### 公钥生成对应地址
PubKey2Address(pubKey string) (address string,err)

#### 输入参数
|字段名|描述|
|:--|:--|
|pubKey|公钥 |

#### 响应参数
|字段名|描述|
|:--|:--|
|address|地址 |


---
### 私钥生成对应地址
|PriKey2Address(|priKey string) (address string,err)

#### 输入参数
|字段名|描述|
|:--|:--|
|priKey|私钥 | 

#### 响应参数
|字段名|描述|
|:--|:--|
 |address|地址 |


---
### 签名
SignBy|priKey(|priKey string, data string) (signedData string,err)

#### 输入参数
|字段名|描述|
|:--|:--|
|priKey|私钥 |
 |data|签名前的数据|

#### 响应参数
|字段名|描述|
|:--|:--|
 |signedData|签名后的数据|


---
### 验签
VerifyByPubKey(pubKey, signedData, data string) (isValid bool,err)

#### 输入参数
|字段名|描述|
|:--|:--|
 |pubKey|公钥 |
 |signedData|签名 |
 |data|签名前的数据|

#### 响应参数
|字段名|描述|
|:--|:--|
 |isValid|签名是否合法|


---
### SM3 哈希
SM3Hash(data []byte) (digest []byte, error)

#### 输入参数
|字段名|描述|
|:--|:--|
 |data|原文 |
 
#### 返回参数
|字段名|描述|
|:--|:--|
 |digest|data 的 SM3 哈希值 |


---
### 上传 cos
uploadToCos(cosPath, tempSecretId, tempSecretKey,sessionToken, filePath string) (err)

#### 输入参数
|字段名|描述|
|:--|:--|
 |cosPath|上传到 cos 的 url |
 |tempSecretId|cos 临时密钥 id |
 |tempSecretKey|cos 临时密钥 key |
 |sessionToken|请求时需要用的 token 字符串 |
 |filePath|本地文件名，包含路径 |

#### 返回参数
|字段名|描述|
|:--|:--|
 |err|nil 为成功，其他为失败 |
