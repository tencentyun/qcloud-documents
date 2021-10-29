## 概述
若您的 DNS 解析托管在其他 DNS 服务商进行托管，现您需转入至 DNSPod 进行解析，您可参考本文进行操作，本文将指导您如何将解析平滑转入至 DNSPod 解析。

## 前提条件
已在腾讯云注册账号并完成实名认证。


## 转入说明
- 转入前请确保所使用的 DNSPod 套餐是否支持导入的解析记录和功能。详情请参见 [DNSPod 定价中心](https://price.dnspod.cn/dns)。
- 检查 CNAME 记录指向的域名是否配置解析，避免 CNAME 指向的域名未做配置导致的业务影响。
- 检查是否配置 DNSSEC 功能，若已配置您可以参考如下两种方式进行转入：
 1. 您可以到域名注册商处关闭 DNSSEC，等转入完成后，再进行 [DNSSEC 配置](https://docs.dnspod.cn/dns/6009640b513c2e7dff9be4fa/)。
 2. 您也可以参考 [DNSSEC 配置](https://docs.dnspod.cn/dns/6009640b513c2e7dff9be4fa/) 进行操作，并到域名注册商处提交 DNSPod DNS 解析的 DNSSEC 配置。等转入完成后，在域名注册商处删除原 DNS 服务商的 DNSSEC 设置。

## 操作步骤
### 步骤1：原 DNS 服务商处导出解析记录
在您的原 DNS 服务商处导出解析记录文件，DNSPod 解析支持 ZONE 文件和 xls 文件格式。建议导出 ZONE 文件，若您的使用 xls 文件格式，您可 [单击此处](https://newdnspod-public-1252120672.cos.ap-guangzhou.myqcloud.com/domain-example.com.zip) 下载导入模板进行编辑。导出操作请您咨询原 DNS 服务商。

### 步骤2：导入解析记录至 DNSPod
1. 登录 [DNSPod 解析控制台](https://console.dnspod.cn/dns/list)，进入 “我的域名” 管理页面。
2. 在 “我的域名” 管理页面，单击**添加域名**，输入您需要转入的域名并单击**确认**。如下图所示：
>?DNSPod 解析仅支持添加二级域名，暂不支持二级域名以下子域名。
>
![](https://main.qcloudimg.com/raw/292bdc090405508bb370c06b046ae597.png)
3. 添加域名完成后，单击域名进入解析设置**记录管理**页签，依次单击**更多操作>批量导入记录**。如下图所示：
![](https://main.qcloudimg.com/raw/3ab9cc3308ad97e78cc5749e3e1f649e.png)
4. 在 “导入记录” 页签中，将准备好的解析记录数据，导入至 DNSPod DNS 解析。具体操作请参见 [记录批量导入](https://docs.dnspod.cn/dns/5fb721ba7daf787f4ed520b8/)。如下图所示：
![](https://main.qcloudimg.com/raw/52773ccd1e92ee666fcab42595d6b458.png)


### 步骤3：修改 DNS 服务器地址
前往域名注册商处，将域名的 DNS 服务器地址修改为 DNSPod 提供的对应 DNS 服务器地址，具体操作请参见 [域名如何配置为 DNSPod 的 DNS 服务器](https://docs.dnspod.cn/dns/6037215cb9640b6a785aa2f4/)。如下图所示：
![](https://main.qcloudimg.com/raw/b011fa69f3e8caffaa924742e51dd4ac.png)

### 步骤4：等待 DNS 服务器生效

修改 DNS 服务器地址完成后，请耐心等待全球各地 LocalDNS 缓存更新。因各地 LocalDNS 都缓存该域名原 DNS 服务器名称，所以修改 DNS 服务器地址完成后，域名 DNS 服务器地址的变更将会逐步同步到全球各地 LocalDNS 服务器中，请您耐心等待。
**一般情况下在48小时内即可完成更新。**

>!更新期间 DNS 解析仍有可能向原 DNS 服务商发起 DNS 查询，所以在变更同步期间请不要删除原 DNS 服务商处的解析记录数据。

