腾讯云密钥管理系统旗舰版提供通过商用密码产品认证的国密 Encryption SDK，国密 Encryption SDK 采用信封加密的方式，结合 KMS 多级密钥，灵活指定数据加密密钥的管理策略。SDK 支持一文一密、多文一密等多种加密方式，并能够支持 CMK 跨地域级的容灾。用户只需调用加解密接口和关注 CMK 的权限控制，即可轻松实现本地高性能海量数据加解密。

如下为使用国密 Encryption SDK 进行数据加解密的原理图：
![](https://main.qcloudimg.com/raw/81011dfad21b398ae6035962148f1635.png)

## 功能特点

#### 极简加解密服务

采用信封加密，复杂的密钥管理全由国密 Encryption SDK 进行封装，用户仅需调用加解密接口和关注 CMK 的权限控制即可实现本地海量数据加解密。

#### 多密钥容灾保护

国密 Encryption SDK 支持 CMK 跨地域级的容灾，对数据加密可指定多个 CMK（建议指定不同地域的 CMK），任意 CMK 均可解密 DEK 从而对数据进行解密。

#### 数据密钥缓存机制

国密 Encryption SDK 具备 DEK 缓存管理功能，使用缓存机制能够有效降低加密过程中导致的性能损耗。将 DEK 缓存在本地，在进行加密时，用户可以通过接口参数指定是否使用数据密钥缓存。

#### 安全合规

国密 Encryption SDK 可以指定由腾讯云 KMS 生成的加密密钥，KMS 底层使用国家密码局或 FIPS-140-2 认证的硬件安全模块 HSM 来保护密钥的安全，确保密钥的保密性、完整性和可用性。 

#### 国密算法支持

国密 Encryption SDK 具备商用密码产品认证证书，支持基于 SM4 的多种模式加解密，满足密码算法合规要求，详情请参见 [算法列表](https://cloud.tencent.com/document/product/573/49506#test1)。

## 如何使用

国密 Encryption SDK 仅适用于密钥管理系统旗舰版，详情请参见 [购买方式](https://cloud.tencent.com/document/product/573/18809) 进行 KMS 旗舰版开通。SDK 操作详情请参见 [SDK 接入指南](https://cloud.tencent.com/document/product/573/49386)。

