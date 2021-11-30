## 操作场景

若您的 DNS 服务器不正确，需将域名 DNS 修改为提示的 DNS 地址，解析方可生效。
>!新注册的域名 DNS 服务器地址默认为免费套餐对应的 DNS 服务器地址，若您不需要升级套餐，则无需调整 DNS 服务器地址。

## 操作步骤

### 查看 DNS 服务器
您可以通过以下步骤查看 DNS 服务器是否正确：
1. 登录 [DNS 解析 DNSPod 控制台](https://console.cloud.tencent.com/cns)，选择需要查看的域名，单击**解析**，进入该域名的管理页面。
2. 选择 “记录管理” 页签。若您未设置 DNS 服务器地址或 DNS 服务器地址有误，您可复制页面提供的 DNS 地址至该域名的管理页面进行修改。如下图所示：
![](https://main.qcloudimg.com/raw/db7f868c22b7bdf94a9186457b9bb75f.png)
>!
>- 不同解析套餐对应的 DNS 地址不同，请参考 [各个套餐对应的 DNS 服务器地址](https://cloud.tencent.com/document/product/302/9070)。
>- 如您需要修改 DNS 服务器地址的域名在腾讯云注册，您可以按照下一步（腾讯云注册域名修改 DNS）进行操作。
>- 如您需要修改 DNS 服务器地址的域名未在腾讯云注册，您可以参考 [其他注册商域名修改 DNS](#edit) 进行操作。
>

### 腾讯云注册域名修改 DNS[](id:serverAddress)
如果域名在腾讯云注册，或者已转入腾讯云，可以通过以下步骤修改 DNS 服务器：
1. 登录 [腾讯云域名注册控制台](https://console.cloud.tencent.com/domain/)，进入 “我的域名” 页面。
2. 选择待修改 DNS 的域名，单击**管理**。如下图所示：
>!若您在当前页面未找到**管理**，请您先确认是否已切换至 [腾讯云域名注册控制台](https://console.cloud.tencent.com/domain/)。
>
![](https://main.qcloudimg.com/raw/4d4176b985b22d48860279a72ef53222.png)
3. 在 “基本信息” 栏中，单击 “DNS 服务器” 的**修改**。如下图所示：
![](https://main.qcloudimg.com/raw/f21df33c228720705e1a0cfb0cae9fc6.png)
4. 在弹出的 “修改 DNS 服务器” 窗口中，选择您需要修改域名 DNS 服务器方式。如下图所示：
![](https://main.qcloudimg.com/raw/3395c68a22bb248fd5275bb96ad0f299.png)
 - **使用 DNSPod**：自动为该域名匹配 DNSPod 服务器的 DNS 地址。
 - **自定义 DNS**： 填写您需要设置的 DNS 服务器地址。
>? 
>- 自定义的 DNS 服务器域名不能是私建的 DNS 服务器域名，必须是解析商的权威 DNS 服务器域名。
>- 需要在腾讯云进行解析的域名，修改 DNS 服务器地址请参考 [各个套餐对应的 DNS 服务器地址](https://cloud.tencent.com/document/product/302/9070)。
  

### 其他注册商域名修改 DNS[](id:edit)
如果域名在其他注册商处注册管理，您需要前往域名注册商提供的域名管理页面，修改为指定的域名 DNS。
腾讯云为您提供部分注册商如何修改域名 DNS 的文档，您可以单击以下链接查看具体步骤：
<ul>
<li><a href="https://docs.dnspod.cn/dns/5ffd613346757d460d99ed5b/">阿里云注册域名如何配置为 DNSPod 的 DNS 服务器</a></li>
<li><a href="https://docs.dnspod.cn/dns/5ffd1c9a46757d460d99ed34/">Google 注册域名如何配置为 DNSPod 的 DNS 服务器</a></li>
<li><a href="https://docs.dnspod.cn/dns/5ffd1aca46757d460d99ed2c/">Domain 注册域名如何配置为 DNSPod 的 DNS 服务器</a></li>
<li><a href="https://docs.dnspod.cn/dns/5ffd132746757d460d99ed24/">NameSilo 注册域名如何配置为 DNSPod 的 DNS 服务器</a></li>
<li><a href="https://docs.dnspod.cn/dns/5ffd0e0946757d460d99ed1c/">Namecheap 注册域名如何配置为 DNSPod 的 DNS 服务器</a></li>
<li><a href="https://docs.dnspod.cn/dns/5ffc364b46757d460d99ed14/">Name 注册域名如何配置为 DNSPod 的 DNS 服务器</a></li>
<li><a href="https://docs.dnspod.cn/dns/5ffc15f646757d460d99ed0a/">GoDaddy 注册域名如何配置为 DNSPod 的 DNS 服务器</a></li>
<li><a href="https://docs.dnspod.cn/dns/5ffc11c446757d460d99ecfa/">商务中国注册域名如何配置为 DNSPod 的 DNS 服务器</a></li>
<li><a href="https://docs.dnspod.cn/dns/5ffc0a2c46757d460d99ecf2/">新网互联注册域名如何配置为 DNSPod 的 DNS 服务器</a></li>
<li><a href="https://docs.dnspod.cn/dns/5ffc07d146757d460d99ece9/"> 爱名网注册域名如何配置为 DNSPod 的 DNS 服务器</a></li>
<li><a href="https://docs.dnspod.cn/dns/5ffc060e46757d460d99ece0/">新网注册域名如何配置为 DNSPod 的 DNS 服务器</a></li>
<li><a href="https://docs.dnspod.cn/dns/5ffbffed46757d460d99ecd5/">美橙互联注册域名如何配置为 DNSPod 的 DNS 服务器</a></li>
<li><a href="https://docs.dnspod.cn/dns/5ffbccf346757d460d99eccd/">易名注册域名如何配置为 DNSPod 的 DNS 服务器</a></li>
<li><a href="https://docs.dnspod.cn/dns/5ffbc4f146757d460d99ecc4/">西部数码注册域名如何配置为 DNSPod 的 DNS 服务器</a></li>
<li><a href="https://docs.dnspod.cn/dns/5ffbbd8346757d460d99ecba/">百度智能云注册域名如何配置为 DNSPod 的 DNS 服务器</a></li>
<li><a href="https://docs.dnspod.cn/dns/61978bc898b4774596a983e5/">华为云注册域名如何配置为 DNSPod 的 DNS 服务器</a></li>
</ul>



