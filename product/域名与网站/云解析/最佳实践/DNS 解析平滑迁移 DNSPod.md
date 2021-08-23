## 概述
若您的 DNS 解析托管在其他 DNS 解析商进行托管，现您需迁移至 DNSPod  进行解析，您可参考本文进行操作，本文将指导您如何将解析平滑迁移至 DNSPod 解析。

## 前提条件
已在腾讯云注册账号并完成实名认证。


## 迁移说明
- 迁移前请确保所使用的 DNSPod 套餐是否支持导入的解析记录和功能。详情请参见 [DNSPod 定价中心](https://price.dnspod.cn/dns)。
- 检查 CNAME 记录指向的域名是否配置解析，避免 CNAME 指向的域名未做配置导致的业务影响。
- 检查是否配置 DNSSEC 功能，若已配置您可以参考如下两种方式进行迁移：
 1. 您可以到域名注册商处关闭 DNSSEC，等迁移完成后，再进行 [DNSSEC 配置](https://docs.dnspod.cn/dns/6009640b513c2e7dff9be4fa/)。
 2. 您也可以参考 [DNSSEC 配置](https://docs.dnspod.cn/dns/6009640b513c2e7dff9be4fa/) 进行操作，并到域名注册商处提交 DNSPod DNS 解析的 DNSSEC 配置。等迁移完成后，在域名注册商处删除原 DNS 解析商的 DNSSEC 设置。

## 操作步骤
### 步骤1：原 DNS 解析商处导出解析记录
在您的原 DNS 解析商处导出解析记录文件，DNSPod 解析支持 ZONE 文件和 xls 文件格式。建议导出 ZONE 文件，若您的使用 xls 文件格式，您可 [单击此处](https://newdnspod-public-1252120672.cos.ap-guangzhou.myqcloud.com/domain-example.com.zip) 下载导入模板进行编辑。导出操作您可咨询您原 DNS 解析商。

### 步骤2：导入解析记录至 DNSPod DNS 解析
1. 登录 [DNSPod 解析控制台](https://console.dnspod.cn/dns/list)，进入 “我的域名” 管理页面。
2. 在 “我的域名” 管理页面，单击**添加域名**，并输入您需要迁移的域名并单击**确认**。如下图所示：
>?DNSPod 解析仅支持添加二级域名，暂不支持二级域名以下子域名。
>
![](https://main.qcloudimg.com/raw/292bdc090405508bb370c06b046ae597.png)
3. 添加域名完成后，单击域名进入解析设置**记录管理**页签，依次单击**更多操作>批量导入记录**。如下图所示：
![](https://main.qcloudimg.com/raw/3ab9cc3308ad97e78cc5749e3e1f649e.png)
4. 在 “导入记录” 页签中，将准备好的解析记录数据，导入至 DNSPod DNS 解析。具体操作请参见 [记录批量导入](https://docs.dnspod.cn/dns/5fb721ba7daf787f4ed520b8/)。如下图所示：
![](https://main.qcloudimg.com/raw/52773ccd1e92ee666fcab42595d6b458.png)


### 步骤3：修改 DNS 服务器地址
前往域名注册商处，将域名的 DNS 服务器地址修改为 DNSPod 提供的对应 DNS 服务器地址。如下图所示：
![](https://main.qcloudimg.com/raw/b011fa69f3e8caffaa924742e51dd4ac.png)
- [腾讯云注册域名如何配置为 DNSPod 的 DNS 服务器](https://docs.dnspod.cn/dns/5ffd62ea46757d460d99ed66/)
- [阿里云注册域名如何配置为 DNSPod 的 DNS 服务器](https://docs.dnspod.cn/dns/5ffd613346757d460d99ed5b/)
- [Google 注册域名如何配置为 DNSPod 的 DNS 服务器](https://docs.dnspod.cn/dns/5ffd1c9a46757d460d99ed34/)
- [Domain 注册域名如何配置为 DNSPod 的 DNS 服务器](https://docs.dnspod.cn/dns/5ffd1aca46757d460d99ed2c/)
- [NameSilo 注册域名如何配置为 DNSPod 的 DNS 服务器](https://docs.dnspod.cn/dns/5ffd132746757d460d99ed24/)
- [Namecheap 注册域名如何配置为 DNSPod 的 DNS 服务器](https://docs.dnspod.cn/dns/5ffd0e0946757d460d99ed1c/)
- [Name 注册域名如何配置为 DNSPod 的 DNS 服务器](https://docs.dnspod.cn/dns/5ffc364b46757d460d99ed14/)
- [GoDaddy 注册域名如何配置为 DNSPod 的 DNS 服务器](https://docs.dnspod.cn/dns/5ffc15f646757d460d99ed0a/)
- [商务中国注册域名如何配置为 DNSPod 的 DNS 服务器](https://docs.dnspod.cn/dns/5ffc11c446757d460d99ecfa/)
- [新网互联注册域名如何配置为 DNSPod 的 DNS 服务器](https://docs.dnspod.cn/dns/5ffc0a2c46757d460d99ecf2/)
- [ 爱名网注册域名如何配置为 DNSPod 的 DNS 服务器](https://docs.dnspod.cn/dns/5ffc07d146757d460d99ece9/)
- [新网注册域名如何配置为 DNSPod 的 DNS 服务器](https://docs.dnspod.cn/dns/5ffc060e46757d460d99ece0/)
- [美橙互联注册域名如何配置为 DNSPod 的 DNS 服务器](https://docs.dnspod.cn/dns/5ffbffed46757d460d99ecd5/)
- [易名注册域名如何配置为 DNSPod 的 DNS 服务器](https://docs.dnspod.cn/dns/5ffbccf346757d460d99eccd/)
- [西部数码注册域名如何配置为 DNSPod 的 DNS 服务器](https://docs.dnspod.cn/dns/5ffbc4f146757d460d99ecc4/)
- [百度智能云注册域名如何配置为 DNSPod 的 DNS 服务器](https://docs.dnspod.cn/dns/5ffbbd8346757d460d99ecba/)

### 步骤4：等待全球各地 LocalDNS 缓存更新

修改 DNS 服务器地址完成后，请耐心等待全球各地 LocalDNS 缓存更新。因各地 localdns 都缓存该域名原 DNS 服务器名称，所以修改 DNS 服务器地址完成后，域名 DNS 服务器地址的变更将会逐步同步到全球各地 Localdns 服务器中，请您耐心等待。
**一般情况下在48小时内即可完成更新。**

>!更新期间 DNS 解析仍有可能向原 DNS 解析商发起 DNS 查询，所以在变更同步期间请不要删除原 DNS 服务商处的解析记录数据。


