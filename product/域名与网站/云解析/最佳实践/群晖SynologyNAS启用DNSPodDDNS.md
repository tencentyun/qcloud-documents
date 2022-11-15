## 操作场景

本文档指导您在群晖（Synology） NAS 上启用 DNSPod 提供的 DDNS（动态域名服务）。启用后，您可以在具备公网 IP 地址的情况下在外访问群晖（Synology） NAS。
<dx-alert infotype="explain" title="">
本过程中仅购买域名可能收取一定的费用，启用 DDNS 服务免费。
</dx-alert>


## 前提条件
- 具备群晖（Synology） NAS 管理员权限的账号。
- 具备 DNSPod 账号并完成 [实名认证](https://docs.dnspod.cn/account/5f3c8dffab35dc34f5791414/)。
- NAS 所在网络环境具备公网 IP 地址。

## 操作步骤

### 注册域名

<dx-alert infotype="explain" title="">
如果您已拥有可使用的域名，可忽略此步骤。
</dx-alert>

1. 登录 [DNSPod 管理控制台](https://console.dnspod.cn/)。
2. 在首页上方搜索栏内输入期望注册的域名并单击 <img src="https://qcloudimg.tencent-cloud.cn/raw/a61bbbc22a07b18388c5ff55319e92ec.png" style="margin:-3px 0px"/> 查询。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/f66127ad7abf10623ea9da1b276edce6.png)
3. 挑选您心仪的域名并选择**添加** > **立即购买**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/95fb6dc254cb8f6beb1f28be67a8acf4.png)
4. 完成购买后，即可进入 [我的域名](https://console.dnspod.cn/dns/list) 管理页面查看您注册的域名。


### 启用 DDNS
1. 在 [我的域名](https://console.dnspod.cn/dns/list) 页面中，单击您已注册的域名，进入“记录管理”页面。
2. 单击**添加记录**，添加一条主机记录为 `www`，记录值为任意 IP 的 A 记录。如下图所示：
<dx-alert infotype="explain" title="">
记录值可以填写为任意 IP 地址，完成操作步骤后将会自动更新为您的公网 IP 地址。此处以 `0.0.0.0` 记录值为例。
</dx-alert>
<img src="https://qcloudimg.tencent-cloud.cn/raw/f2247f76f860b6e83b893b42deb54e97.png"/>
3. 进入 [API 密钥](https://console.dnspod.cn/account/token) 页面，选择 **DNSPod Token** 页签并单击**创建密钥**，输入自定义的密钥名称后，单击**确定**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/d25d632edd4bf470982c5740934f2538.png)
4. 密钥创建成功后，请妥善保管弹出窗口中的显示 ID 与 Token。如下图所示：
<dx-alert infotype="notice" title="">
以下信息仅在创建时显示一次，请您妥善保管。
</dx-alert>
<img src="https://qcloudimg.tencent-cloud.cn/raw/8aa77da9f1c3d62226f708d37c07d534.png"/>
5. 使用具有管理员权限的账号登录您的群晖（Synology） NAS，选择**控制面板** > **外部访问**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/bc69e9bfa6d9b934059203dfbc1b78f5.png)
6. 在 **DDNS** 页签中，单击**新增**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/be84aead9617c4af953d62f25c12d835.png)
7. 在弹出窗口中的“服务供应商”选单内下拉选择 **DNSPod.cn**，并填写相关信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/d275468b90d91865bf911dd3ef34ae02.png)
 - **主机名称**：填写您购买的域名。
 - **用户名/电子邮箱**：填写您获取到的 DNSPod ID。
 - **密码/密钥**：填写您获取到的密钥。
<dx-alert infotype="explain" title="">
您可单击**测试联机**，测试是否能成功联机。状态栏显示为正常，即代表成功联机。
</dx-alert>
8. 单击**确定**。
9. 单击**立即更新**，确认状态栏显示正常。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/7b23e968767f42e39676bb9c6a04bc10.png)
10. 返回 [我的域名](https://console.dnspod.cn/dns/list) 页面，查看记录值的是否已变更为您的公网 IP 地址。
若已变更为设置成功。未变更则请进行相关排查。

