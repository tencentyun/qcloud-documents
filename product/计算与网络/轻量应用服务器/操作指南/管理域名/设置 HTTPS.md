## 操作场景
设置 HTTPS 将使您基于部分轻量应用服务器应用镜像搭建的网站具备以 HTTPS 加密的方式进行数据传输、身份验证等的能力。
### 说明：
- 设置 HTTPS 的功能基于自动化助手 TAT 来完成，您可以一键完成 SSL 证书上传与安装的操作。
- 轻量应用服务器控制台仅展示自动化助手执行设置 HTTPS 命令的结果，并不代表 HTTPS 设置在您实例中的实际生效状态，完成设置后建议您通过访问 `https://您的主机名` 进行验证。

### 使用限制：
- 支持设置 HTTPS 的应用镜像：WordPress、WooCommerce、SRS 音视频服务器、互动直播房间服务、Typecho、Cloudreve、Matomo、LAMP、Theia IDE、Cloud Studio、OpenFaaS；如您需要为基于其他镜像创建的轻量应用服务器实例设置 `HTTPS` ，请参见 [如何安装 SSL 证书](https://cloud.tencent.com/document/product/1207/54869)。
-  您还需要确保轻量应用服务器实例中的自动化助手 TAT 处于“在线”状态，否则依然无法设置 HTTPS。

## 操作步骤
### 前提：
- 您在轻量应用服务器已经成功添加域名解析，查看详情请参见 [添加域名解析](https://cloud.tencent.com/document/product/1207/81333)。
-  您当前账号在 [腾讯云 SSL 证书控制台](https://console.cloud.tencent.com/ssl) 拥有状态为“已签发”，且绑定域名与所选主机名相同的 SSL 证书。

#### 获取 SSL 证书
您可以选择 申请免费证书登录 [腾讯云](https://console.cloud.tencent.com/ssl/dsc/apply) 或上传本地已有证书，详情请参见 [上传（托管） SSL 证书指引](https://cloud.tencent.com/document/product/400/48790)。

#### 设置 HTTPS
登录腾讯云轻量应用服务器控制台，选择任意一种方式设置 HTTPS：
<dx-tabs>
::: 方式一：在域名解析列表设置 HTTPS
1. 从域名页面进入域名解析列表，在对应域名解析的操作列点击设置 HTTPS：
 <img style="width:900px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/7863599594561ecef64f2f1a9b9dfcaa.png" />
2. 选择 SSL 证书。
 <img style="width:400px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/471f16c0ce1c5c545786fb224de4b0b5.png" />

3. 单击确认即可。
:::
::: 方式二：在实例详情页设置 HTTPS
1. 登录轻量应用服务器控制台，选择左侧导航栏中的服务器。
2. 在实例列表中，选择目标实例并进入实例详情页。
3.  选择域名页签，在对应域名解析的操作列点击设置 HTTPS。

 <img style="width:900px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/7ab12cff9898492a7691322e84e3a5a5.png" />
4. 选择 SSL 证书。

  <img style="width:400px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/471f16c0ce1c5c545786fb224de4b0b5.png" />

5. 单击确认即可。
:::
</dx-tabs>
<dx-alert infotype="notice" title="">
轻量应用服务器控制台只为您展示设置 HTTPS 的历史记录及其状态，且不支持通过本功能对已设置的 HTTPS 进行回退。如您部署的网站不再需要 HTTPS 加密，请参考 [删除 HTTPS 设置](https://cloud.tencent.com/document/product/1207/84362)。
</dx-alert>
