本文档介绍元数据 SSL 连接管理的使用和操作说明。

## 功能介绍

为了保障数据传输过程中的安全，CASB 支持为应用-代理、代理-数据库双向链路分别配置 TLS 加密，保护数据的完整性、机密性，防止中间人劫持数据。
<table>
<thead>
<tr>
<th colspan=2 width="20%">支持类型</th>
<th>详情</th>
</tr>
</thead>
<tbody><tr>
<td colspan=2 >元数据类型</td>
<td><li>MySQL</li><li>PostgreSQL</li></td>
</tr>
<tr>
<td colspan=2 >TLS 版本</td>
<td><li>TLS1.0</li><li>TLS1.1</li><li>TLS1.2 </li><li>TLS1.3</li></td>
</tr>
<tr>
<td colspan=2 >TLS 加密算法</td>
<td><li>TLS_RSA_WITH_AES_128_CBC_SHA</li><li>TLS_RSA_WITH_AES_256_CBC_SHA</li><li>TLS_RSA_WITH_AES_128_GCM_SHA256</li><li>TLS_RSA_WITH_AES_256_GCM_SHA384</li><li>TLS_AES_128_GCM_SHA256</li><li>TLS_AES_256_GCM_SHA384</li><li>TLS_CHACHA20_POLY1305_SHA256</li><li>TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA</li><li>TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA</li><li>TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA</li><li>TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA</li><li>TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256</li><li>TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384</li><li>TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256</li><li>TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384</li><li>TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256</li><li>TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256</li></td>
</tr>
<tr>
<td  rowspan=2>CASB  代理的  SSL  模式</td>
<td>MySQL</td>
<td><li>DISABLED </li><li>PREFERRED </li><li>REQUIRED </li><li>VERIFY_CA </li></td>
</tr>
<tr>
<td>PostgreSQL</td>
<td><li>disable</li><li>allow</li><li>prefer</li><li>require</li><li>verify-ca </li></td>
</tr>
</tbody></table>


## 操作配置 

#### 步骤1：进入 SSL 连接策略配置页面 
1. 登录 [云访问安全代理控制台](https://console.cloud.tencent.com/casb)，单击元数据管理菜单下的**关系型元数据**，进入关系型元数据总览页面。
![](https://main.qcloudimg.com/raw/35abfec3265505b16c6a242e4ab6bf48.png)
2. 找到需要操作的元数据，单击元数据右侧的**管理**，进入元数据管理详情页面。
![](https://main.qcloudimg.com/raw/637c9ceb4a107049531b8e6ad2791ee0.png)
3. 选择 SSL 连接策略标签，即可进入 SSL 连接配置页。本配置页可以设置应用-代理、代理-数据库的双向 SSL 连接功能。
![](https://qcloudimg.tencent-cloud.cn/raw/7db0bf3c7cdd42128b69b11a8d48e153.png)

#### 步骤2：SSL 策略配置
1. 应用-CASB 代理。
   - 关闭 SSL 连接开关后，CASB 代理不启用 SSL 连接功能支持，应用无法通过 SSL 连接到代理。
   - 开启 SSL 连接开关后，CASB 代理启用 SSL 连接功能支持，应用可使用 SSL 连接到代理。
   * 开启 SSL 连接开关后，可以下载 SSL 证书，以供应用验证 CASB 代理的身份。
2. CASB 代理-数据库。
   - 关闭 SSL 连接开关后，CASB 代理不使用 SSL 连接数据库，传输过程中数据包明文传输。
   - 开启 SSL 连接开关后，代理将使用 SSL 连接访问数据库，传输过程中数据包加密传输。请确认数据库已开启 SSL 连接支持，否则会导致代理访问数据库失败。
