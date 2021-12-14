
## 概述
腾讯云内测版密钥管理系统由于架构改进，计划进行 EOL（end-of-life）流程。您可以永远使用内测旧版密钥管理系统，及其提供的所有功能服务，但后续将不再支持升级。

官网已正式上线全新 [密钥管理系统（合规）](https://console.cloud.tencent.com/kms2 ) 做服务替换。新版密钥管理系统 KMS 完全满足合规标准，提供了更为丰富的密钥管理功能，且大大提高了可靠性设计。

>!
>- 内测版密钥管理系统将永久维护，此次变更不影响您的正常业务使用。
>- 内测版密钥管理系统采用 [API/SDK 2017](https://cloud.tencent.com/document/product/573/8899) 接口提供服务。若需确认您是否正在使用内测版密钥管理系统，可 [提交工单](https://console.cloud.tencent.com/workorder/category) 与我们联系。

## 价格说明
密钥管理系统 KMS，由 CMK 存储费用及 API 调用费用两部分组成，详细请参见 [计费概述](https://cloud.tencent.com/document/product/573/34388)。

## 步骤说明
**步骤1：**内测旧 KMS 服务用户，可先在官网重新开通使用新的密钥管理系统（合规）。
**步骤2：**使用新版 KMS，创建用户主密钥 CMK。
**步骤3：**将内测旧版 KMS 服务加密的数据进行解密：按照 API/SDK 2017 接口规范，使用旧版 SDK，调用解密 Decrypt 接口，获取明文数据。
**步骤4：**通过新的密钥管理系统（合规）系统的 SDK 重新进行加密。 

## 敏感数据加密迁移步骤

敏感信息加密是密钥管理系统 KMS 核心的能力，实际应用中主要用来保护服务器硬盘上敏感数据的安全（小于4KB），如密钥、证书、配置文件等，详情请参见 [敏感信息加密](https://cloud.tencent.com/document/product/573/8790)。

1. 开通 [密钥管理系统（合规）](https://console.cloud.tencent.com/kms2 )服务。
2. 按照业务需求，在密钥管理系统（合规）创建相应的用户主密钥 CMK。
3. 内测版密钥管理系统加密的数据进行解密：按照 API/SDK 2017 接口规范，使用旧版 SDK，调用解密 Decrypt 接口，获取明文数据，请参见 [解密](https://cloud.tencent.com/document/product/573/8890)  API 文档。
4. 新版密钥管理系统（合规）敏感数据加密： 按照腾讯云 API 3.0 标准，使用新版 SDK，调用加密 Encrypt 接口进行加密，详情请参见 [加密](https://cloud.tencent.com/document/product/573/34420) API 文档。
5. 新版密钥管理系统（合规）敏感数据解密：按照腾讯云 API3.0 标准，使用新版 SDK，调用解密 Decrypt 接口进行解密，详情请参见 [解密](https://cloud.tencent.com/document/product/573/34429) API 文档。


## 信封加密迁移步骤
信封加密（Envelope Encryption）是一种应对海量数据的高性能加解密方案，详情请参见 [信封加密](https://cloud.tencent.com/document/product/573/8791)。


1. 开通 [密钥管理系统（合规）](https://console.cloud.tencent.com/kms2 ) 服务。
2. 按照业务需求，在密钥管理系统（合规）创建相应的用户主密钥 CMK。
3. 内测版密钥管理系统加密数据进行解密：只需要处理 DataKey 的迁移，按照 API/SDK 2017 接口规范，使用旧版本 SDK，调用解密 Decrypt 接口，获取明文 DataKey，详情请参见 [解密](https://cloud.tencent.com/document/product/573/8890) API 文档。
4. 新版密钥管理系统（合规）信封加密：按照腾讯云 API 3.0 标准，使用新版 SDK，调用加密 Encrypt 接口进行加密，详情请参见 [加密](https://cloud.tencent.com/document/product/573/34420) API 文档。
5. 新版密钥管理系统（合规）信封解密：按照腾讯云 API 3.0 标准，使用新版 SDK，调用解密 Decrypt 接口解密 DataKey 获取明文，使用 DataKey 明文对数据进行解密。详情请参见 [解密](https://cloud.tencent.com/document/product/573/34429) API 文档。


