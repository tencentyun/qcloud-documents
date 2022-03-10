

## 功能介绍

腾讯云 CDN 支持共享 CNAME 功能：多个域名绑定同一个自定义 CNAME，方便您管理域名解析。

>!
>- 此功能为白名单功能，尚未全量。
>- 请注意每次操作后您域名的 CNAME 解析配置。

## 配置指南

### 入口

账号开启共享 CNAME 白名单后，登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在左侧菜单栏选择**域名管理**，即可在页面上方看到**共享 CNAME** 按钮，单击即可进入共享 CNAME 功能页面。
![](https://qcloudimg.tencent-cloud.cn/raw/f4cf093f0a5e28d5f59d1e0e080b73eb.png)

### 新增配置

单击**新增配置**即可开始增加共享 CNAME配置。
![](https://qcloudimg.tencent-cloud.cn/raw/c233b4b1f8c9b05193415fabfc2cb949.png)


完成配置共需三步：

1. 选择域名：请选择要配置共享 CNAME 的域名。
>!
>- 共享 CNAME 和域名所在平台强相关，请您尽量选择加速区域和业务类型相同的域名。
>- 若您同时使用了 CDN 和 ECDN 服务，则不可同时选择接入不同服务的域名。
>- 仅支持选择未关闭/未绑定共享 CNAME/未被封禁/未被锁定的域名。
2. 配置共享 CNAME：后端会自动为您选择的多个域名按域名所在平台分组，每组配置一个自定义的 CNAME，组内的域名就绑定了同一个 CNAME。
>?自定义 CNAME 的后缀固定：XXX-APPID.shared.cdn.dnsv1.com
3. 确认配置：所选域名的初始 CNAME 将被配置的共享 CNAME 覆盖，请您注意确认域名的共享 CNAME 解析配置。
三步确认无误提交后，可返回**共享 CNAME** 页面查看您的配置。

### 编辑配置

您可编辑存量已添加的共享 CNAME 配置，支持新增域名，解绑域名和删除配置三个操作：
![](https://qcloudimg.tencent-cloud.cn/raw/a9a69e079634775002dc997a19a036f6.png)

#### 新增域名

您可往当前已创建的共享 CNAME 中继续绑定域名。

>!共享 CNAME 和域名所在平台强相关，仅可选择平台匹配当前共享 CNAME 的域名。我们会帮您判断和过滤，不可选的域名会被置灰不可选。

#### 解绑域名

您可在当前已创建的共享 CNAME 中解绑已经绑定的域名，即对域名取消配置共享 CNAME。

>!
>- 解绑后，域名的 CNAME 会恢复至其初始的 CNAME，请您注意域名的 CNAME 解析配置。
>- 共享 CNAME 至少得绑定一个域名。若解绑所有域名，即该共享 CNAME 下无任何域名，则会同步删除该 CNAME。

您也可以在**域名管理**页面的域名操作 > 更多里对单个域名解绑：
![](https://qcloudimg.tencent-cloud.cn/raw/e50d1977744c1c6914ab5fea886902f3.png)

#### 删除

删除共享 CNAME 配置，即解绑该 CNAME 下所有域名并删除该 CNAME，所有域名将恢复至各自初始的 CNAME，请您注意域名的 CNAME 解析配置。

