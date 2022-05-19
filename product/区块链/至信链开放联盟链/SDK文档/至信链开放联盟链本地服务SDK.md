## 获取方式

- windows 环境至信链基础能力 SDK 本地服务：[2021-12-30/nft_wallet_service.exe](https://zhixinliantest-1302317679.cos.ap-guangzhou.myqcloud.com/nft/nft/nft_wallet_service/windows/2021-12-30/nft_wallet_service.exe)

- linux 环境至信链基础能力 SDK 本地服务：[2021-12-30/nft_wallet_service](https://zhixinliantest-1302317679.cos.ap-guangzhou.myqcloud.com/nft/nft/nft_wallet_service/linux/2021-12-30/nft_wallet_service)（调整权限 ./执行）

- mac 环境至信链基础能力 SDK 本地服务：[2022-02-15/nft_wallet_service_mac](https://zhixinliantest-1302317679.cos.ap-guangzhou.myqcloud.com//nft/nft_wallet_service/mac/2022-02-15/nft_wallet_servicenft_wallet_service_mac)
操作步骤如下：
step1：`chmod a+x nft_wallet_service_mac`
step2：`./nft_wallet_service_mac`

## 场景描述

* 生成公私钥：调用生成助记词接口生成助记词（如有助记词，可跳过），调用派生生成子公私钥对接口。
* 鉴权：用户通过调用 GenerateApiSign 接口生成鉴权信息，将鉴权信息填入请求头。

>! 
>- 调用钱包本地服务接口之前，需要先下载并启动 nft_wallet_service。
>- post 请求统一使用 json 请求。
>- 钱包本地服务端口号：30505

## 相关接口                         



### 调用至信链接口前生成签名数据接口 

http://127.0.0.1:30505/generateApiSign

#### 请求方式

POST

#### 请求参数

|字段名 |类型| 是否必填| 描述|
|:--|:--|:--|:--|
|secretKey |string | 是| 用户注册时生成的 secretKey（方案二该参数传"")|
|secretId  |string    |是  |注册用户时生成的 secretId（方案二该参数传""）|

 

#### 响应参数

|字段名 |类型| 是否必填| 描述|
|:--|:--|:--|:--|
|err |string | 是 |错误信息|
|signData| json |是 |生成各项签名数据|

signData 说明：

|字段名 |类型| 是否必填| 描述|
|:--|:--|:--|:--|
|signature |string  |是 |签名后的数据|
|signatureTime |string  |是 |时间戳|
|nonce |int |是 |随机数|

方案一：
需要准备：

|字段名|       类型|
|:--|:--|   
|secretId|string |
|secretKey|string |
   
调用 GenerateApiSign 方法生成签名，将相关字段放到 Header 中：

|字段名|       类型|
|:--|:--|  
|App-Id       |string |
|Signature-Time|string |  
|Signature       |string |
|Nonce|       int|
   

方案二：
直接调用 GenerateApiSign 方法生成签名，将相关字段放到 Header 中：

   |字段名|       类型|
|:--|:--|  
|Signature-Time|string |
|Signature    |string |
|  Nonce|       int|
   


---
### 生成助记词

http://127.0.0.1:30505/createMnemonic

#### 请求方式

POST

#### 请求参数

无

#### 响应参数

|字段名 |类型| 是否必填| 描述|
|:--|:--|:--|:--|
|err |string  |是 |错误信息|
|mnemonic |string  |是 |12 个英文词组，utf8，空格分割 |


---
### 派生生成子公私钥对

http://127.0.0.1:30505/DeriveKeyPair

#### 请求方式

POST

#### 请求参数

|字段名 |类型| 是否必填| 描述|
|:--|:--|:--|:--|
|mnemonic |string  |是 |12 个英文单词，空格分割|
|index   |int |是 |从 0 开始递增的序号，相同的 index 生成的子公私钥相同）|

#### 响应参数

|字段名 |类型| 是否必填| 描述|
|:--|:--|:--|:--|
|err |string  |是 |错误信息|
|priKey |string  |是 |私钥|
|pubKey   |string  |是 |公钥|


---
### 私钥生成对应公钥

http://127.0.0.1:30505/PriKey2PubKey

#### 请求方式

POST

#### 请求参数

|字段名 |类型| 是否必填| 描述|
|:--|:--|:--|:--|
|pri |string  |是 |私钥|

#### 响应参数

|字段名 |类型| 是否必填| 描述|
|:--|:--|:--|:--|
|err |string  |是 |错误信息|
|pub |string  |是 |公钥|


---
### 公钥生成对应地址

http://127.0.0.1:30505/PubKey2Address

#### 请求方式

POST

#### 请求参数

|字段名 |类型| 是否必填| 描述|
|:--|:--|:--|:--|
|pubKey |string  |是 |公钥|

#### 响应参数

|字段名 |类型| 是否必填| 描述|
|:--|:--|:--|:--|
|address |string  |是 |地址|
|err |string  |是 |错误信息|


---
### 私钥生成对应地址

http://127.0.0.1:30505/PriKey2Address

#### 请求方式

POST

#### 请求参数

|字段名 |类型| 是否必填| 描述|
|:--|:--|:--|:--|
|priKey |string  |是 |私钥 |

#### 响应参数

|字段名 |类型| 是否必填| 描述|
|:--|:--|:--|:--|
|address |string  |是 |地址|
|err |string  |是 |错误信息|


---
### 签名

http://127.0.0.1:30505/SignByPriKey

#### 请求方式

POST

#### 请求参数

|字段名 |类型| 是否必填| 描述|
|:--|:--|:--|:--|
|priKey |string  |是 |私钥|
|data |string  |是 |签名前的数据|

#### 响应参数

|字段名 |类型| 是否必填| 描述|
|:--|:--|:--|:--|
|err |string  |是 |错误信息|
|signedData |string  |是 |签名后的数据|


---
### 验签

http://127.0.0.1:30505/VerifyByPubKey

#### 请求方式

POST

#### 请求参数

|字段名 |类型| 是否必填| 描述|
|:--|:--|:--|:--|
|pubKey |string  |是 |公钥 |
|signedData |string  |是 |签名|
|data |string  |是 |签名前的数据|

#### 响应参数

|字段名 |类型| 是否必填| 描述|
|:--|:--|:--|:--|
|err |string  |是 |错误信息|
|isValid |string  |是 |签名是否合法|


---
### SM3 哈希

http://127.0.0.1:30505/SM3Hash

#### 请求方式

POST

#### 请求参数

|字段名 |类型| 是否必填| 描述|
|:--|:--|:--|:--|
|data |string  |是 |原文 |

#### 响应参数

|字段名 |类型| 是否必填| 描述|
|:--|:--|:--|:--|
|digest |string  |是 |data 的 SM3 哈希值（这是一个 byte[] 经过 base64 之后的数据如需使用需要 base64 解码后 调用 hex. EncodeTo|string ）|
|err |string  |是 |错误信息|


---
### SM3 哈希 EnCode（SM3Hash + hex. EncodeTo|string ）

http://127.0.0.1:30505/SM3HashEncode

#### 请求方式

POST

#### 请求参数

|字段名 |类型| 是否必填| 描述|
|:--|:--|:--|:--|
|data |string  |是 |原文 |

#### 响应参数

|字段名 |类型| 是否必填| 描述|
|:--|:--|:--|:--|
|digest |string  |是 |可作为发行数字藏品接口中 hash 字段直接获取方式|
|err |string  |是 |错误信息|


---
### 上传 cos

http://127.0.0.1:30505/uploadToCos

#### 请求方式

POST

#### 请求参数

|字段名 |类型| 是否必填| 描述|
|:--|:--|:--|:--|
|cosPath |string  |是 |上传到 cos 的 url |
|tempSecretId |string  |是 |cos 临时密钥 id|
|temp|secretKey | string  |是 |cos 临时密钥 key|
|sessionToken |string  |是 |请求时需要用的 token 字符串|
|filePath |string  |是 |本地文件名，包含路径|

#### 响应参数

|字段名 |类型| 是否必填| 描述|
|:--|:--|:--|:--|
|err |string  |是 |nil 为成功，其他为失败|
