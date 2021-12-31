

腾讯云 CDN 与 [DNSPod](https://console.dnspod.cn/) 已打通解析配置能力，若域名已托管至腾讯云 DNSPod，则可通过 [CDN 控制台](https://console.cloud.tencent.com/cdn/domains) 一键配置 CNAME，减少配置步骤和时间，快速启用 CDN 加速服务。

>! 仅支持中国站，不支持国际站。

## 背景

域名接入 CDN 后，系统会自动分配一个以`.cdn.dnsv1.com`为后缀的 CNAME 域名，可在 CDN 控制台 [域名管理](https://console.cloud.tencent.com/cdn/domains) 页查看。CNAME 域名不能直接访问，您需要在域名服务提供商处完成 CNAME 配置，CNAME 记录生效后，即可启用 CDN 加速服务。

## 场景

同时使用腾讯云 CDN 和 DNSPod 的用户设置 CNAME 记录，启用 CDN 加速服务。

## 操作指南

### 将域名托管至 DNSPod

您需要先将域名解析托管在 DNSPod上，详细说明请见 [域名解析托管在 DNSPod](https://docs.dnspod.cn/dns/60b99ba0e90008112f815bde/)。

### 使用 CDN 服务

#### 接入域名

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在左侧导航栏中单击**域名管理**进入域名管理页面，单击**添加域名**，添加您要加速的域名。详细说明请见 [接入域名](https://cloud.tencent.com/document/product/228/41215)。
![](https://main.qcloudimg.com/raw/611a6e5f6dfc8ade52d1f0fae0c78163.png)

#### 配置 CNAME

在 CDN 控制台 [域名管理](https://console.cloud.tencent.com/cdn/domains) 页找到对应的加速域名，鼠标悬浮在 CNAME 前的图标上，即可看到相关提示，单击**一键配置**设置 CNAME
![](https://main.qcloudimg.com/raw/88e44660c0d149d3d6262768c743542f.png)


为正式启用所选域名的加速服务，我们将对域名 DNSPod 侧的解析记录进行以下处理：

1. 若域名未配置任何解析记录：新增一条默认线路类型的腾讯云 CDN CNAME 记录，TTL 值默认为 600。
2. 若域名已配置解析记录：暂停所有已配置的解析记录，新增一条默认线路类型的腾讯云 CDN CNAME 记录，TTL 值默认为 600。
**注： 暂停域名所有已配置的解析记录可能会影响域名当前已有 DNS 解析服务，请您注意确认。**

![](https://main.qcloudimg.com/raw/25308891389f899ee15d501285f62a29.png)
您可后续前往 [DNSPod 控制台](https://console.dnspod.cn/dns/list) 管理解析记录。


>!请确保当前账号有对应域名的管理权限：
>若为子账号或协作者账号，请联系主账号授权。例如：授权对应 CDN 加速域名的写权限 + QcloudDNSPodFullAccess 权限。

### 完成 CNAME 设置

提交一键配置解析后，大约1分钟内生效，请您耐心等待。届时您可刷新 CDN 控制台 [域名管理](https://console.cloud.tencent.com/cdn/domains) 页，当 CNAME 状态变为已启动的状态时，鼠标悬浮在 CNAME 前的图标上时可看到提示：加速服务正常运行中。

>?如果您不希望使用此功能，想自行配置 CNAME，可参见 [配置 CNAME](https://cloud.tencent.com/document/product/228/3121)。

## 其他
若您后续要删除对应的加速域名，删除时，我们不会操作您在 DNSPod 侧的解析记录，请您根据需要自行修改解析记录。

