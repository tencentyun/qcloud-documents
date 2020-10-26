
腾讯云密钥管理系统旗舰版提供了通过商用密码产品认证的国密 Encryption SDK，国密 Encryption SDK 使用信封加密的原理，灵活指定数据加密密钥的管理策略，对 KMS 进行进一步封装，轻松实现本地高性能海量数据加解密。使用国密 Encryption SDK 进行数据加解密的原理图如下：

![](https://main.qcloudimg.com/raw/81011dfad21b398ae6035962148f1635.png)

## 功能特点

### 极简加解密服务

采用信封加密，复杂的密钥管理全由 Encryption SDK 进行封装，仅需调用加解密接口和关注 CMK 的权限控制即可实现本地海量数据加解密。

### 多密钥容灾保护

KMS Encryption SDK 支持 CMK 跨 region 级的容灾，对数据加密可指定多个 CMK，任意 CMK 均可解密 DEK 来对数据进行解密。

### 国密算法支持

国密 Encryption SDK 具备商用密码产品认证证书，支持国密算法，满足密码算法合规要求 。

## 如何使用

国密 Encryption SDK 仅适用于密钥管理系统旗舰版，开通 KMS 旗舰版，详情请参见密钥管理系统 [购买方式](https://cloud.tencent.com/document/product/573/18809)。SDK 的详细操作指导请参见 [SDK 接入指南](https://cloud.tencent.com/document/product/573/49386)。
