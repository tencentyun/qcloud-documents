## 操作场景

若您的 DNS 服务器不正确，需将域名 DNS 修改为提示的 DNS 地址，解析方可生效。
>!新注册的域名 DNS 服务器地址默认为免费套餐对应的 DNS 服务器地址，若您不需要升级套餐，则无需调整 DNS 服务器地址。

## 操作步骤

### 查看 DNS 服务器
您可以通过以下步骤查看 DNS 服务器是否正确：
1. 登录 [DNS 解析 DNSPod 控制台](https://console.cloud.tencent.com/cns)，选择需要查看的域名，单击【解析】，进入该域名的管理页面。
2. 选择 “记录管理” 页签。若存在如下提示，说明 DNS 服务器不正确。您可复制页面提供的 DNS 地址到该域名的管理页面进行修改。如下图所示：
![](https://main.qcloudimg.com/raw/0165f8c5de242de9deefae452750c626.png)
>!不同解析套餐对应的 DNS 地址不同，请参考 [各个套餐对应的 DNS 服务器地址](https://cloud.tencent.com/document/product/302/9070)。

### 腾讯云注册域名修改 DNS[](id:serverAddress)
如果域名在腾讯云注册，或者已转入腾讯云，可以通过以下步骤修改 DNS 服务器：
1. 登录 [腾讯云域名注册控制台](https://console.cloud.tencent.com/domain/)，进入 “我的域名” 页面。
2. 选择待修改 DNS 的域名，单击【管理】。如下图所示：
>!若您在当前页面未找到【管理】，请您先确认是否已切换至 [腾讯云域名注册控制台](https://console.cloud.tencent.com/domain/)。
>
![](https://main.qcloudimg.com/raw/4d4176b985b22d48860279a72ef53222.png)
3. 在 “基本信息” 栏中，单击 “DNS 服务器” 的【修改】。如下图所示：
![](https://main.qcloudimg.com/raw/f21df33c228720705e1a0cfb0cae9fc6.png)
4. 在弹出的 “修改 DNS 服务器” 窗口中，选择您需要修改域名 DNS 服务器方式。如下图所示：
![](https://main.qcloudimg.com/raw/3395c68a22bb248fd5275bb96ad0f299.png)
 - **使用 DNSPod**：自动为该域名匹配 DNSPod 服务器的 DNS 地址。
 - **自定义 DNS**： 填写您需要设置的 DNS 服务器地址。
>? 
>- 自定义的 DNS 服务器域名不能是私建的 DNS 服务器域名，必须是解析商的权威 DNS 服务器域名。
>- 需要在腾讯云进行解析的域名，修改 DNS 服务器地址请参考 [各个套餐对应的 DNS 服务器地址](https://cloud.tencent.com/document/product/302/9070)。
  

### 其他注册商域名修改 DNS
如果域名在其他注册商处注册管理，您需要前往域名注册商提供的域名管理页面，修改为指定的域名 DNS。
下面以阿里云（万网）、GoDaddy 为例。
- 参考阿里云（万网）注册商的 [域名 DNS 修改](https://help.aliyun.com/document_detail/54157.html) 操作。
- 参考 GoDaddy 注册商的 [域名 DNS 修改](https://sg.godaddy.com/zh/help/change-nameservers-for-my-domains-664) 操作。


