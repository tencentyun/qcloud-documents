## 访问与加速类问题

### 如何使用自有域名访问对象？

可通过绑定自定义域名实现，详情请参见 [自定义加速域名](https://cloud.tencent.com/document/product/436/36637)。

### COS 是否支持 HTTPS 访问？

支持。COS 在所有 [可用地域](https://cloud.tencent.com/document/product/436/6224) 的访问节点都提供了 SSL 传输的支持，且在 SDK 和控制台都默认启用 HTTPS。**COS 强烈建议您使用 HTTPS 保护传输的数据链路，使用不加密的 HTTP 连接将可能面临链路被监听或数据被窃取的风险。**

### COS 如何开通 CDN？

详情请参见 [开启默认 CDN 加速域名](https://cloud.tencent.com/document/product/436/36636) 和 [开启自定义 CDN 加速域名](https://cloud.tencent.com/document/product/436/36637)。

### COS 是否支持 CDN HTTPS 回源 COS？

支持。具体操作方法请参见 [设置回源](https://cloud.tencent.com/document/product/436/13310) 文档。

### 自定义域名如何配置 HTTPS 访问？

可将存储桶绑定到自有域名，开启 CDN 加速，在 [CDN 控制台](https://console.cloud.tencent.com/cdn) 进行 HTTPS 配置，详细操作指引请参见 [HTTPS 配置](https://cloud.tencent.com/document/product/228/41687)；
若不使用 CDN，您也可以通过为域名配置反向代理，将域名解析到服务器的方式实现，详细操作可参见 [配置自定义域名支持 HTTPS 访问](https://cloud.tencent.com/document/product/436/11142)。

### 如何对 COS 中的文件生成一个临时 URL？

具体操作请参见 [预签名授权下载](https://cloud.tencent.com/document/product/436/14116)。

### 私有读存储桶能否通过 CDN 加速访问？

可以，但是需要进行授权相关配置。具体配置请参见 CDN 加速概述文档的 [私有读存储桶](https://cloud.tencent.com/document/product/436/18669#.E7.A7.81.E6.9C.89.E8.AF.BB.E5.AD.98.E5.82.A8.E6.A1.B6) 部分。

### 可以使用海外加速 GCD 加速国内的对象存储 COS 吗？

可以。但由于政策原因，海外加速平台 GCD 回源获取中国大陆境内的数据、或中国大陆用户访问海外节点，必须经由公共运营商网络，速度可能不理想，甚至无法访问。建议您可以使用海外加速 GCD 的 URL 预热功能，提前缓存热点文件。


### 配置跨域访问后，携带白名单内的头部访问 COS 被拒绝，该如何处理？

访问被拒绝的可能原因如下：
1. 检查您的配置是否与您携带的头部一致，查看是否存在不可见字符，例如空格。
2. 检查您发起请求的域名信息，如果您使用 CDN 加速域名访问，需要在 CDN 控制台进行跨域配置，可参考 [自定义响应头配置](https://cloud.tencent.com/document/product/228/41737)。
3. 检查您的存储桶权限状态，判断您的访问是否符合存储桶的授权。
4. 检查您的浏览器缓存情况，可能是由于浏览器缓存导致的报错，可通过 Ctrl+F5 强制刷新浏览器或在浏览器【Network】选项卡中勾选 Disable cache 解决。


## 域名及其他类问题


### 在控制台进行域名管理时，总是提示“请至少启用一个可用密钥”该如何处理？

请登录 [访问管理控制台](https://console.cloud.tencent.com/cam/capi) 查看是否已启用云 API 密钥。

- 若未启用云 API 密钥，请创建密钥并启用后再进行域名管理。
- 若已启用云 API 密钥仍有提示，请确认您当前操作的账号是否为子账号（协作者或子用户）：
  - 若为子账号，请登录主账号确认已启用云 API 密钥。
  - 若为主账号，请刷新浏览器缓存，重新登录腾讯云账号。

### 使用自定义域名是否必须通过腾讯云备案？
目前 COS 使用自定义域名必须开启 CDN，请根据您的情况进行判断：

- 若您的域名接入国内 CDN，需要备案。但不要求必须通过腾讯云备案，保证接入的域名已备案即可。
- 若您的域名接入海外 CDN，不需要备案。

### 为何在 CDN 控制台变更源站后，COS 控制台里的原自定义域名就消失了？

>!一旦您使用了 V5 版本控制台，并带有 JSON 版本域名配置，COS  V5 控制台则无法显示新域名。

请检查您的存储桶中是否配置了 JSON 域名，请将 JSON 版本域名配置修改为 XML 域名。

<a id="gcd"></a>
### 尚未备案的域名可以接入海外加速 GCD 平台吗？

使用海外加速无需备案，但需要注意，您在腾讯云上存放的数据和操作行为仍需遵守相关国家的法律法规，以及 [《腾讯云服务协议》](https://cloud.tencent.com/document/product/301/1967)。

### COS 文件更新（重新上传或删除）时，CDN 仍然保存缓存内容，造成与源站不一致。能否在 COS 更新时自动刷新 CDN 的缓存？

COS 本身不支持自动刷新 CDN 缓存，您可以联合云函数 SCF 来设置自动刷新 CDN 缓存，详情请参见 [使用 SCF 自动刷新被 CDN 缓存的 COS 资源 ](https://cloud.tencent.com/document/product/436/30434) 文档。
