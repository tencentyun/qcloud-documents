## **步骤预览**
CDN 的使用流程如下图所示：
![流程图](https://mc.qcloudimg.com/static/img/f226c2d0655ce65f25bca945082f7760/quick-start-9.png)
## 开通 CDN 服务
在使用 CDN 服务前，您需要进行实名认证及 CDN 服务的开通，如果您的腾讯云账号已经开通 CDN，请直接跳到 [接入域名](#yuming)。
### 完成实名认证
1. 新用户登录 [CDN 控制台](https://console.cloud.tencent.com/cdn) 可以看到实名认证指引，单击 【前往认证】 可进行实名认证。
 ![](https://main.qcloudimg.com/raw/8ade7faa62b1158393100f5feabccad5.png)
2. 您也可以进入 [帐号中心](https://console.cloud.tencent.com/developer) ，单击【提交认证】进行认证。
![](https://main.qcloudimg.com/raw/24bc11aadb6e94a45cc65096bd116b44.png)
3. 详细认证流程请参见 [实名认证指引](https://cloud.tencent.com/doc/product/378/3629) 。个人认证会在提交审核后立即完成。企业认证约一个工作日完成，且认证成功后您将收到短信通知。您可以 [提交工单](https://console.cloud.tencent.com/workorder/category/create?level1_id=1&level2_id=41&level1_name=%E5%85%AC%E5%85%B1%E5%9F%BA%E7%A1%80%E7%B1%BB%E9%97%AE%E9%A2%98&level2_name=%E8%B4%A6%E5%8F%B7%E7%B1%BB) 咨询实名认证进度。

### 补充服务信息
完成实名认证后，进入 [CDN 控制台](https://console.cloud.tencent.com/cdn)，确认您的实名认证信息及选择服务内容，完成后单击 【下一步】。
![](https://main.qcloudimg.com/raw/799e2d9d0b5dff6a04142ea28a2c1752.png)

### 选择付费方式
CDN 提供了两种计费方式：流量计费、带宽计费，您可以根据业务模型选择合适的计费方式，更多详细说明，请参见 [计费说明](https://cloud.tencent.com/doc/product/228/2949)。
勾选同意服务条款后，单击【开通 CDN】，即可开始使用加速服务。
![](https://main.qcloudimg.com/raw/d3913b3dc5ad769a6d8135a977a756db.png)
成功开通后，您可在概览页面看到您所选择的计费模式。
![](https://main.qcloudimg.com/raw/a7e7da71ea365f6ee501178167ff072a.png)

<span id="yuming"></span>
## 接入域名
### 填写域名配置
1. 进入 [CDN 控制台](https://console.cloud.tencent.com/cdn)，单击左侧菜单中【域名管理】进入相应页面，单击【添加域名】。
 ![](https://main.qcloudimg.com/raw/a1b7b3aa4b89533045b3cd10825d3afa.png)
2. 在**域名**位置填入需要加速的域名，该域名需要满足以下条件：
 - 已经在工信部进行过备案。
 - 尚未被接入过腾讯云 CDN。
![](https://main.qcloudimg.com/raw/12410d7f22e5763fe2d1aa427b74e5f5.png)

### 填写服务配置
 **业务类型**选择，决定了域名调度的资源平台，不同资源平台加速配置存在一定差异，请选择与您业务相匹配的业务类型：
 - 静态加速：适用于电商类、网站类、游戏图片类静态资源加速场景。
 - 下载加速：适用于游戏安装包、音视频原文件下载、手机固件分发等场景。
 - 流媒体点播加速：适用于音视频点播加速等场景。 
 ![](https://main.qcloudimg.com/raw/5a1a60e71ac4bd92f333c42298fcab36.png)
 
### 添加完成
提交域名，添加完成，请耐心等待域名配置下发至全网节点，下发时间约 5-10 分钟。
![](https://main.qcloudimg.com/raw/c551d6d1d89e0d4e23c284106b5bbde3.png)

## 配置 CNAME
### 查看  CNAME
域名配置完成后，系统会为您分配对应的 **CNAME** ，以 ```.cdn.dnsv1.com``` 为后缀，请务必按照控制台展示的CNAME进行配置。
![](https://main.qcloudimg.com/raw/c7e412b163d8458583e69f8446ada0fe.png)

### 修改 CNAME
您需要到接入域名的 DNS 服务商处完成 CNAME 配置，配置方法请查阅 [CNAME 配置](https://cloud.tencent.com/doc/product/228/3121)。
### 验证 CNAME 是否生效
不同的 DNS 服务商，CNAME 生效的时间略有不同，一般会在半个小时之内生效。您也可以通过 dig 的方式来查询 CNAME 是否生效，如果 dig 到后缀为 ```.cdn.dnsv1.com``` 的域名，表示域名 CNAME 已生效。
![](https://main.qcloudimg.com/raw/4c611fda0209a45d9441a2f0336bbf84.png)
