
以下视频将为您介绍修改 DNS 服务器地址的相关操作：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2303-33501?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 操作场景

若您的 DNS 服务器不正确，需将域名 DNS 修改为提示的 DNS 地址，解析方可生效。
>!新注册的域名 DNS 服务器地址默认为免费套餐对应的 DNS 服务器地址，若您不需要升级套餐，则无需调整 DNS 服务器地址。

## 操作步骤

### 查看 DNS 服务器
您可以通过以下步骤查看 DNS 服务器是否正确：
1. 登录 [腾讯云控制台](https://console.cloud.tencent.com/)，选择 “云产品 > 域名与网站 > DNS 解析 DNSPod”，进入 “域名解析列表” 页面。
2. 选择需要查看的域名，进入该域名的管理页面。
3. 选择 “记录管理” 页签。若存在如下提示，说明 DNS 服务器不正确。您可复制 DNS 地址到该域名的管理页面进行修改。如下图所示：
![1](https://main.qcloudimg.com/raw/1334ffff245ca5ecebea8521d6df5d65.png)
>!不同解析套餐对应的 DNS 地址不同，请参考 [各个套餐对应的 DNS 服务器地址](https://cloud.tencent.com/document/product/302/9070)。

### 腾讯云注册域名修改 DNS
如果域名在腾讯云注册，或者已转入腾讯云，可以通过以下步骤修改 DNS 服务器：
1. 登录 [腾讯云域名管理控制台](https://console.cloud.tencent.com/domain/)，进入 “我的域名” 页面。
2. 选择待修改 DNS 的域名，单击【管理】。如下图所示：
![](https://main.qcloudimg.com/raw/c7990910028acc9fb863bf77704ba9be.png)
3. 在 “基本信息” 栏中，单击 “DNS 服务器” 的【修改】。如下图所示：
![](https://main.qcloudimg.com/raw/f5926d507764039315a0c6f48c44738c.png)
4. 在弹出的 “修改 DNS 服务器” 窗口中，填写您套餐对应的 DNS 服务器地址，单击【提交】，完成修改。如下图所示：
>?需要在腾讯云进行解析的域名，修改 DNS 服务器地址请参考 [各个套餐对应的 DNS 服务器地址](https://cloud.tencent.com/document/product/302/9070)。
>
![](https://main.qcloudimg.com/raw/af9eeb25f7a08d7db424b7d7b347057d.png)

### 其他注册商域名修改 DNS
如果域名在其他注册商处注册管理，您需要前往域名注册商提供的域名管理页面，修改为指定的域名 DNS。
下面以阿里云（万网）、GoDaddy 为例。
- 参考阿里云（万网）注册商的 [域名 DNS 修改](https://help.aliyun.com/document_detail/54157.html) 操作。
- 参考 GoDaddy 注册商的 [域名 DNS 修改](https://sg.godaddy.com/zh/help/change-nameservers-for-my-domains-664) 操作。


