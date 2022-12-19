
## 操作场景
本文介绍如何在 Kong 云原生 API 网关上通过 Kong Bot Detection 插件屏蔽爬虫访问。
Bot Detection插件通过检查HTTP请求中User Agent字段，识别发起请求的用户代理软件信息，拒绝爬虫请求。该插件内置了一些基础的校验规则用于校验请求，您可以参见 [爬虫示例](https://github.com/Kong/kong/blob/master/kong/plugins/bot-detection/rules.lua#L5) 定义爬虫请求。

## 前置条件
- 已购买 Kong 网关实例，详情请参见 [实例管理](https://cloud.tencent.com/document/product/1364/72495)。
- 配置了后端（Service）以及路由（Route）。

## 插件配置

| 字段名称 | 字段说明 |
|---------|---------|
| allow | 使用正则表达式定义允许放行的 User-Agent 列表。 |
| deny | 使用正则表达式定义拒绝放行的 User-Agent 列表。 |


## 操作步骤
1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse/kong)，进入需要配置限流插件的 Kong 网关实例详情页，在配置管理页查看管理控制台登录方式。
2. 登录 Konga 管理控制台，进入需要反爬虫的 Route 详情页，单击 **Add Plugin**，在插件市场的 Security 分组中选择 Bot Detection 插件，单击 **Add Plugin**。
![](https://qcloudimg.tencent-cloud.cn/raw/e490691c4a201ccc2d4efd6106c12190.png)
3. 插件配置中使用正则表达式填写需要配置限制的代理信息，例如，拒绝来自 Firefox 的爬虫请求，在 deny 中配置[".\*Firefox.\*"]。
![](https://qcloudimg.tencent-cloud.cn/raw/145a0111a8f065082d60b5bfca175963.png)
4. 使用火狐浏览器发起 API 请求，由于请求头带有 `User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:106.0) Gecko/20100101 Firefox/106.0`，请求被拒绝。
![](https://qcloudimg.tencent-cloud.cn/raw/bb54de683a5e7854920c4de4d6137d52.png)

## 参考
更多相关说明请参见 [Kong Bot Detection 插件官方文档](https://docs.konghq.com/hub/kong-inc/bot-detection/)。
