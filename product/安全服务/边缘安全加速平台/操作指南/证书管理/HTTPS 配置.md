
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，在左侧菜单栏中，单击**证书管理** > **HTTPS 配置**。
>?目前边缘安全加速平台控制台仅对部分用户开放，如需访问控制台，请 [联系我们](https://cloud.tencent.com/online-service) 开通权限。
>
3. 在 HTTPS 配置页面，选择所需站点，可为站点加速提供如下一系列 HTTPS 配置选项：

### 强制 HTTPS[](id:QZ)
在强制 HTTPS 模块中，单击![](https://qcloudimg.tencent-cloud.cn/raw/4f521701c30f8f3f7ca4b577e00b62b9.png)强制将所有边缘 HTTP 请求通过301/302重定向至 HTTPS。默认不开启。
>?开启后全部请求走 HTTPS，请确认提供服务的子域名的证书已部署到 EdgeOne。
>

### 回源 HTTPS[](id:HY)
在回源 HTTPS 模块中，单击**编辑**，选择回源的加密模式，即回源采用的协议，单击**保存**。
![](https://qcloudimg.tencent-cloud.cn/raw/fbe3dd3ea73804cf193618ed3f18f074.png)
**参数说明：**
- 协议跟随（默认）：跟随请求协议，请求协议用的是 HTTP，则回源也采用 HTTP。
- HTTP：回源请求一律采用 HTTP 协议。
- HTTPS：回源请求一律采用 HTTPS 协议。

### HTTP Strict Transport Security (HSTS)
1. 在 HSTS 模块中，单击**启用 HTST**，配置相关参数，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/2077b2ac09ea3aff461a08964d617bd6.png)
**参数说明：**
 - 配置状态：默认关闭，使用 HSTS 功能时，需要开启。
 - 缓存时间： HSTS 头部的过期时间，单位为秒，可配置范围为1-31536000秒。该时间内浏览器会始终以 HTTPS 发起请求。
 - 包含子域名：开启时，当前域名及其子域名均会开启 HSTS。
 - 预加载：开启时，允许浏览器自动预加载 HSTS 配置，以避免首次 HTTP 请求的潜在攻击风险。域名需提前加入浏览器 HSTS Preload List 才能生效。
2. 配置 HSTS 后，EdgeOne 加速节点响应增加 `Strict-Transport-Security` 头部，强制客户端（浏览器等）使用 HTTPS 与边缘节点创建链接，全局加密网站。
 - HSTS 头部格式
```
Strict-Transport-Security: max-age=expireTime [; includeSubDomains] [; preload]
```
 - 字段说明
    - max-age：HSTS 头部的过期时间，单位为秒。该时间内浏览器会始终以 HTTPS 发起请求。
    - includeSubDomains：可选字段，开启时，当前域名及其子域名均会开启 HSTS。
    - preload：可选字段，开启时，允许浏览器自动预加载 HSTS 配置，以避免首次 HTTP 请求的潜在攻击风险。域名需提前加入浏览器 HSTS Preload List 才能生效。
>?
>- 开启 HSTS 前，请确保域名证书已部署，HTTPS 请求可正常响应。
>- 启用 HSTS 时建议您同步启用 [强制 HTTPS](#QZ)，否则当请求为 HTTP 时，浏览器将不执行 HSTS 配置。
>- max-age 可配置范围为1-31536000秒。

### TLS 版本
在 TLS 版本模块中，单击**编辑**，选择所需版本，单击**保存**。
>?仅允许开启的 TLS 版本的 HTTPS 链接，可选择的 TLS 版本为1.0-1.3，只可开启连续或单个版本号。
>
![](https://qcloudimg.tencent-cloud.cn/raw/7a91b1f77935d50c4de1aa355f5560c3.png)


### OCSP 装订
在 OCSP 装订模块中，TLS 握手时发送事先缓存的 OCSP 响应以提高握手效率。单击![](https://qcloudimg.tencent-cloud.cn/raw/0ce2f7ccf282e1b1bda8dd2e7032cd8a.png)开启后，加速节点会缓存 OCSP 响应以供客户端验证，客户端无需向数字证书认证机构（CA）发送查询请求，从而提高 TLS 握手效率。
