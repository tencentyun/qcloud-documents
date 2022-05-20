## 操作场景
本文档指导您在群晖（Synology）NAS上启用腾讯云提供的 DDNS（动态域名服务）。启用后，您可以在拥有公网 IP 地址的群晖（Synology） NAS 上使用域名外网访问群晖（Synology）NAS。
>? 本过程中仅购买域名可能收取一定的费用，启用 DDNS 及申请证书均免费。
>

## 前提条件

- 拥有群晖（Synology）NAS 管理员权限的账号。
- 拥有腾讯云 DNSPod 账号并完成 [实名认证](https://docs.dnspod.cn/account/5f3c8dffab35dc34f5791414/) 。
- 群晖（Synology） NAS 拥有公网 IP 地址。
- 拥有1个可用域名并且解析托管在 [DNSPod](https://console.dnspod.cn/dns/list)。

>?若无可用域名，您可前往腾讯云 [域名注册购买页](https://buy.cloud.tencent.com/domain?from=console) 购买您心仪的域名。
>若您的域名解析未托管在 DNSPod，您可参考 [其他平台解析域名平滑转入 DNSPod](https://cloud.tencent.com/document/product/302/60584)。

## 操作步骤

 ### 步骤1：获取 API 密钥信息
登录 [腾讯云 API 密钥](https://console.dnspod.cn/account/token/apikey) ，获取您的腾讯云 API **SecretId** 及 **SecretKey** 密钥信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/9ac6abc8d4e4f2592aa16ab64990fe64.png)
>!
>- 您的 API 密钥代表您的账号身份和所拥有的权限，使用腾讯云 API 密钥可以操作您名下的所有腾讯云资源。
>- 为了您的财产和服务安全，请妥善保存和定期更换密钥，请勿通过任何方式（如 GitHub）上传或者分享您的密钥信息。
>

### 步骤2：群晖（Synology）NAS 配置 DDNS

1. 使用具有管理员权限的账号登入您的群晖（Synology）NAS，依次单击**控制面板 > 外部访问 > DDNS > 新增**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/4ac7973cf2dd8d790672f0d2d5e98184.png)
2. 在弹出的 “添加 DDNS” 窗口中，填写相关信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c36e353058913cd79b8c133ef00ae887.png)
	- **服务供应商**：请选择**腾讯云**。
	- **主机名称**：请填写您的**域名名称**。
	- **用户名/电子邮件**：请填写您获取到的 **SecretId** 信息。
	- **密码/密钥**：请填写您获取到的 **SecretKey** 信息。
	- **从 Tencent Cloud 获取证书，并将其设置为默认证书**：勾选选项后，可自动为您申请腾讯云 TrustAsia SSL 免费证书并替换 NAS 的默认 SSL 证书。
>?单击**测试联机**，测试是否能联机成功。如状态栏显示为**正常**，则代表联机成功。
>
3. 单击**确定**，即可完成设置。等待解析生效后，即可使用域名访问您的群晖（Synology）NAS。
>?解析生效时间一般需要 10分钟，请耐心等待。 
>

### 步骤3：手动更新 DDNS（可选）
1. 完成设置后，单击**立即更新**，系统将为您更新最新的 DDNS 解析记录，并确认状态是否显示为<font color=#009e05>正常</font>。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/fb2e3dfe6a1ea56138ab4cf73912ce71.png)
2. 返回 [我的域名](https://console.dnspod.cn/dns/list) 管理页面，单击您的域名，即可查看记录值是否已变更为您的公网 IP 地址。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c8452694f979be2e91afef3182b9fa9f.png)
	- 若已变更，则设置成功。
	- 若未变更，请根据以下常见问题进行排查。



 ## 常见问题
 ### 完成设置后域名还是无法正常访问？
- 请检查您的 IP 地址是否为公网 IP。您可直接在外网环境下使用浏览器访问群晖（Synology）NAS 获取的 IP 地址，若可访问，即为公网 IP。
- 完成设置后，需要等待解析生效才可正常访问，解析生效时间一般需要10分钟，请耐心等待。 解析生效后，您可使用 `ping 域名` 命令检查返回的 IP 地址是否为您的公网 IP 地址。


 ### 手动更新后解析记录值未变更？
 请检查您填写的 **SecretId** 及 **SecretKey** 密钥信息是否正确。


 
 
