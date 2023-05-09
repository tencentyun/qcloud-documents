本文档将指导您如何开通密钥管理系统（KMS）服务。

## 背景信息
云访问安全代理（CASB）可选择基于 [密钥管理系统（KMS）](https://cloud.tencent.com/product/kms) 进行密钥加密存储，如果用户选择 KMS 进行密钥管理则需要在创建密钥前，完成 KMS 服务开通和 KMS 对 CASB 服务的角色授权操作。

## CASB 密钥管理
云访问安全代理的密钥由 KMS 托管，采用三级密钥管理机制，根密钥由硬件加密机生成和存储，由根密钥生成 [用户主密钥 (CMK)](https://cloud.tencent.com/document/product/573/38406)，最终基于用户主密钥生成数据加密密钥 DEK，对应用数据进行加解密。

### [KMS 管理密钥管理](https://cloud.tencent.com/document/product/573/8873)
在服务架构方层面，KMS 服务通过单地域多机房提供可靠性，其底层使用的 HSM 设备也采用多机房集群化部署，并提供双机房冷备份设备，确保服务的高可用性。保护密钥的保密性、完整性和可用性，满足用户多应用多业务的密钥管理需求。

## 操作步骤
1. 登录 [云访问安全代理控制台](https://console.cloud.tencent.com/casb)，在控制台上方指引中，单击[**密钥管理系统 KMS**](https://buy.cloud.tencent.com/kms)，前往 KMS 购买页。
![](https://main.qcloudimg.com/raw/ff3252134f3e4da6728af0b3470b7489.png)
2. 在密钥管理系统开通页面，单击**立即开通**，成功开通密钥管理系统服务。

## 相关文档
- [角色授权](https://cloud.tencent.com/document/product/1303/90838)
-  [账号授权](https://cloud.tencent.com/document/product/1303/48429)
