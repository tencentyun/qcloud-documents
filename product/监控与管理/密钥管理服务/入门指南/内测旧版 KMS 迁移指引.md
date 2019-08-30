## 概述
腾讯云内测旧版 [密钥管理服务](https://console.cloud.tencent.com/kms) 由于架构改进，计划进行 EOL(end-of-life)流程。客户仍可以继续使用内测旧版密钥管理服务及其提供的所有功能服务，但后续将不再支持升级。

官网已正式上线全新 [密钥管理服务（合规）](https://cloud.tencent.com/product/kms2) 做服务替换。新的密钥管理服务 KMS 完全满足合规标准，提供了更为丰富的密钥管理功能，且大大提高了可靠性设计。

以上变更，不影响内测版旧 KMS 服务的正常使用以及您的业务正常运行。如需迁移或对产品有任何疑问可以 [提交工单](https://console.cloud.tencent.com/workorder/category) 反馈给我们，感谢您对腾讯云的信赖与支持！

## 价格说明
密钥管理服务 KMS 由 CMK 存储费用及 API 调用费用两部分组成，详细请参见 [计费概述](https://cloud.tencent.com/document/product/573/34388)。

## 操作步骤
**步骤1：**内测旧 KMS 服务用户可先在在官网重新开通使用新的密钥管理服务（合规）。
**步骤2：**使用新版 KMS 创建您的主密钥 CMK。
**步骤3：**选择将内测旧版 KMS 服务加密的数据按照 API/SDK 2017 接口规范，使用旧版 SDK，
调用解密 [Decrypt](https://cloud.tencent.com/document/product/573/8890) 接口，获取明文数据。
**步骤4：**通过新的密钥管理服务（合规）系统的 SDK 重新进行加密。。 

## 新 KMS 系统加密方案
#### 技术场景一：敏感数据加密
敏感信息加密是密钥管理服务（KMS）核心的能力，实际应用中主要用来保护服务器硬盘上敏感数据的安全（小于 4KB），如密钥、证书、配置文件等。参考官网最佳实践-敏感信息加密：https://cloud.tencent.com/document/product/573/8790

#### 如何迁移
**步骤1：**开通 [密钥管理服务（合规）](https://console.cloud.tencent.com/kms2)服务。

**步骤2：**按照业务需求，在密钥管理服务（合规）创建相应的 CMK。

**步骤3：**内测旧版 [密钥管理服务](https://console.cloud.tencent.com/kms) 加密的数据进行解密：按照 API/SDK 2017 接口规范，使用旧版 SDK，调用解密 Decrypt 接口，获取明文数据，请参见 API [解密](https://cloud.tencent.com/document/product/573/8890) 文档。

**步骤4：**新版密钥管理服务（合规）敏感数据加密： 按照腾讯云 API3.0 标准，使用新版 SDK，
调用加密 Encrypt 接口进行加密，参考官网 API 加密文档：
https://cloud.tencent.com/document/api/573/34420

**步骤5：**新版密钥管理服务（合规）敏感数据解密：按照腾讯云 API3.0 标准，使用新版 SDK，调用解密 Decrypt 接口进行解密，请见 API [解密](https://cloud.tencent.com/document/product/573/34429) 文档。


#### 技术场景二：信封加密
信封加密（Envelope Encryption）是一种应对海量数据的高性能加解密方案，详情请参见 [信封加密](https://cloud.tencent.com/document/product/573/8791)。

#### 如何迁移
**步骤1：**开通 [密钥管理服务（合规）](https://console.cloud.tencent.com/kms2) 服务。

**步骤2：**按照业务需求，在密钥管理服务（合规）创建相应的 CMK。

**步骤3：**内测旧版密钥管理服务(https://console.cloud.tencent.com/kms) 加密数据进行解密：只需要处理 DataKey 的迁移，按照 API/SDK 2017 接口规范，使用旧版本 SDK，调用解密 Decrypt 接口，获取明文 DataKey，详情请参见 API [解密](https://cloud.tencent.com/document/product/573/8890) 文档。


**步骤4：**新版密钥管理服务（合规）信封加密：按照腾讯云 API3.0 标准，使用新版 SDK，调用加密 Encrypt 接口进行加密，详情请参见 API [加密](https://cloud.tencent.com/document/api/573/34420) 文档。


**步骤5： **新版密钥管理服务（合规）信封解密：按照腾讯云 API3.0 标准，使用新版 SDK，调用解密 Decrypt 接口解密 DataKey 获取明文，使用 DataKey 明文对数据进行解密。详情请参见 API [解密](https://cloud.tencent.com/document/product/573/34429) 文档。
