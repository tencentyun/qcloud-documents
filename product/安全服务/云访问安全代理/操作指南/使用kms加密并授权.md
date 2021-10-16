本文档将指导您如何开通密钥管理系统（KMS）服务并完成 KMS 对云访问安全代理服务的角色授权。
## 背景信息
云访问安全代理（CASB）基于密钥管理系统（KMS）进行加密存储，在进行实例初始化操作前，需完成 KMS 服务开通和 KMS 对 CASB 服务的角色授权操作。

## 加密原理

CASB 管理平台将使用**用户授权的自定义密钥**或**系统生成的默认密钥**创建数据库密钥和工作密钥（密钥因子），CASB 插件拉取工作密钥后，生成实际密钥进行数据加解密。 

## 操作步骤

### 步骤1：开通 KMS 服务
1. 登录 [云访问安全代理控制台](https://console.cloud.tencent.com/casb)，在控制台上方指引中，单击[**密钥管理系统 KMS**](https://buy.cloud.tencent.com/kms)，前往 KMS 购买页。
![](https://main.qcloudimg.com/raw/ff3252134f3e4da6728af0b3470b7489.png)
2. 在密钥管理系统开通页面，单击**立即开通**，成功开通密钥管理系统服务。

### 步骤2：开通 CASB 对 KMS 的角色授权
1. 在成功开通 KMS 服务后，返回 [云访问安全代理控制台](https://console.cloud.tencent.com/casb)，在控制台上方指引中，单击[**访问管理 CAM**](https://console.cloud.tencent.com/cam/role/grant?roleName=CASB_QCSRole&policyName=QcloudKMSAccessForCASBRole&principal=eyJzZXJ2aWNlIjoiY2FzYi5xY2xvdWQuY29tIn0%3D&serviceType=casb&s_url=https://console.cloud.tencent.com/casb)，前往到 CAM 授权页面。
![](https://main.qcloudimg.com/raw/f77b3165988a3ec95e8cbf48740917a1.png)
2. 在服务授权页面，单击**同意授权**，成功授权。
![](https://main.qcloudimg.com/raw/55df3c3a60f4d63dfe307487aafb6b85.png)
