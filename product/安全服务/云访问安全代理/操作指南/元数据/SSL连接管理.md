本文档介绍元数据SSL连接管理的使用和操作说明。

## 功能介绍

为了保障数据传输过程中的安全，CASB支持为应用-代理、代理-数据库双向链路分别配置TLS加密，保护数据的完整性、机密性，防止中间人劫持数据。

### 支持元数据类型
* MySQL
* PostgreSQL
 
### 支持TLS版本
* TLS1.0
* TLS1.1
* TLS1.2
* TLS1.3
 
### 支持TLS加密算法
* TLS_RSA_WITH_AES_128_CBC_SHA
* TLS_RSA_WITH_AES_256_CBC_SHA
* TLS_RSA_WITH_AES_128_GCM_SHA256
* TLS_RSA_WITH_AES_256_GCM_SHA384
* TLS_AES_128_GCM_SHA256
* TLS_AES_256_GCM_SHA384
* TLS_CHACHA20_POLY1305_SHA256
* TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA
* TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA
* TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
* TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
* TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
* TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
* TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
* TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
* TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
* TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256

### CASB代理支持的SSL模式

#### MySQL
* DISABLED 
* PREFERRED 
* REQUIRED 
* VERIFY_CA

#### PostgreSQL
* disable
* allow
* prefer
* require
* verify-ca

## 操作配置 

#### 1.进入SSL连接策略配置页面。 

* 登录 [云访问安全代理控制台](https://console.cloud.tencent.com/casb)，单击元数据管理菜单下的**关系型元数据**，进入关系型元数据总览页面。
![](https://main.qcloudimg.com/raw/35abfec3265505b16c6a242e4ab6bf48.png)
* 找到需要操作的元数据，单击元数据右侧的**管理**，进入元数据管理详情页面。
![](https://main.qcloudimg.com/raw/637c9ceb4a107049531b8e6ad2791ee0.png)
* 选择SSL连接策略标签，即可进入SSL连接配置页。本配置页可以设置应用-代理、代理-数据库的双向SSL连接功能。
![](https://qcloudimg.tencent-cloud.cn/raw/6ca152a1f25e726ca3b40e0a779c3ebc.png)

#### 2.SSL策略配置
1. 应用-CASB代理
   * 关闭SSL连接开关后，CASB代理不启用SSL连接功能支持，应用无法通过SSL连接到代理。
   * 开启SSL连接开关后，CASB代理启用SSL连接功能支持，应用可使用SSL连接到代理。
   * 开启SSL连接开关后，可以下载SSL证书，以供应用验证CASB代理的身份。
2. CASB代理-数据库
   * 关闭SSL连接开关后，CASB代理不使用SSL连接数据库，传输过程中数据包明文传输。
   * 开启SSL连接开关后，代理将使用SSL连接访问数据库，传输过程中数据包加密传输。请确认数据库已开启SSL连接支持，否则会导致代理访问数据库失败。