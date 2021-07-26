

腾讯云 CDN 与 [DNSPod](https://console.dnspod.cn/) 已打通解析配置能力，若域名已托管至腾讯云 DNSPod，则可通过 [CDN 控制台](https://console.cloud.tencent.com/cdn/domains) 一键配置 CNAME，节省配置步骤和时间，快速启用 CDN 加速服务。

## 背景

域名接入 CDN 后，系统会自动分配一个以 `.cdn.dnsv1.com` 为后缀的 CNAME 域名，可在 CDN 控制台 [域名管理](https://console.cloud.tencent.com/cdn/domains) 页查看。CNAME 域名不能直接访问，您需要在域名服务提供商处完成 CNAME 配置，CNAME 记录生效后，即可启用 CDN 加速服务。

## 场景

同时使用腾讯云 CDN 和 DNSPod 的用户设置 CNAME 记录，启用 CDN 加速服务。

## 操作指南

### 将域名托管至 DNSPod

您需要先将域名解析托管在 DNSPod 上，详情请参见 [域名解析托管在 DNSPod](https://docs.dnspod.cn/dns/60b99ba0e90008112f815bde/)。

### 使用 CDN 服务

#### 接入域名

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在左侧导航栏中单击【域名管理】进入域名管理页面，单击【添加域名】，添加您要加速的域名。详情请参见 [接入域名](https://cloud.tencent.com/document/product/228/41215)。

#### 配置 CNAME

在 CDN 控制台 [域名管理](https://console.cloud.tencent.com/cdn/domains) 页找到对应的加速域名，鼠标悬浮在 CNAME 上，即可看到相关提示，点击【一键配置】设置 CNAME

>!请确保当前账号有对应域名的解析权限
- 若为子账号，请联系主账号授权。
- 若为协作者，请联系主账号 [域名共享](https://docs.dnspod.cn/dns/5f2d4664e8320f1a740d9cc1/)。

1. 若加速域名未配置过任何 A 记录/CNAME 记录，则新增一条 CNAME 记录解析至腾讯云 CDN。
2. 若加速域名已经配置过 A 记录/CNAME 记录（非腾讯云 CDN），则会增加一条最高优先级 CNAME 记录解析至腾讯云 CDN。
3. 若加速域名配置过分区域/运营商的 A 记录/CNAME 记录（非腾讯云 CDN），则会新增一条最高优先级全局 CNAME 记录解析至腾讯云 CDN。

### 完成 CNAME 设置

提交一键配置解析后，大约1分钟内生效，届时您可刷新 CDN 控制台 [域名管理](https://console.cloud.tencent.com/cdn/domains) 页，鼠标悬浮在 CNAME 上时可看到提示：域名加速服务已生效。



