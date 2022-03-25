## 防盗链配置

若您希望对业务资源的访问来源进行控制，腾讯云 CDN 为您提供了 referer 防盗链配置功能。

通过对用户 HTTP Request Header 中 referer 字段的值设置访问控制策略，从而限制访问来源，避免恶意用户盗刷。



## 配置指南

### 查看配置

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在菜单栏里选择**域名管理**，单击域名右侧**管理**，即可进入域名配置页面，第二栏【访问控制】中可看到防盗链配置，默认情况下，防盗链配置为关闭状态：
![img](https://main.qcloudimg.com/raw/810f2995b21f3c93d706775a31ed6b3e.png)

### 开启配置

单击开关，选择防盗链类型并填入列表，即可启用防盗链配置：


**referer 黑名单：**

- 若请求的 referer 字段匹配黑名单内设置的内容，CDN 节点拒绝返回该请求信息，直接返回403状态码。
- 若请求的 referer 不匹配黑名单内设置的内容，则 CDN 节点正常返回请求信息。
- 空referer选项勾选**拒绝空 referer访问** 选项时，此时若请求 referer 字段为空或无 referer 字段（如浏览器请求），则 CDN 节点拒绝返回该请求信息，返回403状态码。

<img src="https://qcloudimg.tencent-cloud.cn/raw/a4d464b0ca1fe91eff1831d18acb8280.png" width="530px">


**referer白名单：**

- 若请求的 referer 字段匹配白名单设置的内容，则 CDN 节点正常返回请求信息。
- 若请求的 referer 字段不匹配白名单设置的内容，则 CDN 节点拒绝返回该请求信息，会直接返回状态码403。
- 当设置白名单时，CDN 节点只能返回符合该白名单内字符串内容的请求。
- 空referer选项勾选**允许空 referer访问** 选项时，此时若请求 referer 字段为空或无 referer 字段（如浏览器请求），则 CDN 正常返回请求信息。

<img src="https://qcloudimg.tencent-cloud.cn/raw/68f280cd104a2e3ff5211481758f8682.png" width="530px">

**配置约束：**

- 防盗链支持域名 / IP 规则，匹配方式为前缀匹配（仅支持路径情况下，域名的前缀匹配不支持），即假设配置名单为`www.abc.com`，则`www.abc.com/123`匹配，`www.abc.com.cn`不匹配；假设配置名单为`127.0.0.1`，则`127.0.0.1/123`也会匹配。
- 防盗链支持通配符匹配，即假设名单为`*.qq.com`，则`www.qq.com`、`a.qq.com`均会匹配。

### 关闭配置

您可以通过防盗链开关，一键关闭防盗链配置，开关为关闭状态时，即便下方存在已有配置，仍不会现网生效，下次单击开启时，会先行进行配置的二次确认，不会立即发布至全网生效：
![img](https://main.qcloudimg.com/raw/90d1aafb98fb2a92543bc48e05335abd.png)

### 区域特殊配置

若您的加速域名服务区域为全球加速，想针对境内、境外加速区域进行不同的 referer 防盗链配置，可点击配置下方的**添加特殊配置**进行设置：
![img](https://main.qcloudimg.com/raw/1f52eec731c4b62d9e87d7c414641862.png)

> !区域特殊配置添加后，暂时无法直接删除，您可以通过关闭配置来禁用。

## 配置示例

若加速域名`www.test.com`的防盗链配置如下：
![](https://qcloudimg.tencent-cloud.cn/raw/1d2a0382dda6e0b46458665edb3116bc.png)

则实际访问情况如下：

1. 中国境内用户请求，携带的 referer 信息为`1.1.1.1`，则命中境内配置的白名单，可直接返回内容。
2. 中国境外用户请求，携带的 referer 为空，匹配**拒绝空 referer访问**命中境外配置的黑名单，直接返回403。

