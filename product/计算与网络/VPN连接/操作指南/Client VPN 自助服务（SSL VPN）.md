为了方便您更加快捷的建立SSL VPN连接提供了便捷的 SSL 客户端下载配置服务。

## 前提条件
- 在[ 数字身份管控平台 ](https://console.cloud.tencent.com/eiam)已创建[ 用户组 ](https://cloud.tencent.com/document/product/1442/55067)、添加了相应的[ 用户 ](https://cloud.tencent.com/document/product/1442/55066)并配为用户组配置[ 应用授权](https://cloud.tencent.com/document/product/1442/55069)。
- 在 VPN 控制台已 [创建 SSL 服务端](https://cloud.tencent.com/document/product/554/63717)，且 SSL 服务端支持身份认证。
- SSL 服务端已[ 开启访问控制 ](https://cloud.tencent.com/document/product/554/75188)和[ 配置访问控制策略](https://cloud.tencent.com/document/product/554/75189)。


## 操作步骤
1. 登录[ 腾讯云 Clinet VPN 自主服务门户](http://self-service-test.vpn.woa.com/)。
  1. 在 SSL 服务端 ID 所在行的输入框中输入创建好的 SSL 服务端实例 ID，然后单击**下一步**，进入登录界面。
![](https://qcloudimg.tencent-cloud.cn/raw/e37b558345b8edeae794d9f650071c5f.png)
  2. 登录腾讯云 Clinet VPN 自主服务门户。      
单击![](https://qcloudimg.tencent-cloud.cn/raw/6c78a80d3aadbade303cd3158eba47b9.png)进行 SAML 认证，然后单击**跳转进行认证（SAML）**进行登录。
>?
>1. 目前仅支持通过 SAML 认证登录，请确保您在 EIAM 的用户组中，并在 SSL 访问控制策略中。如果提示“未授权访问该应用，请联系管理员”，可联系管理官将您添加到 EIAM 用户组即可。
>2. 如果您有修改 EIAM 应用需求，请确保原EIAM应用中的用户已经迁移至新的 EIAM 应用，避免原应用中用户无法访问。
>3. 切换 EIAM 应用后，已连接的 SSL VPN 连接不会中断。
>
2. 下载 SSL 客户端配置文件和 SSL 客户端。
     1.在**下载 SSL 客户端配置文件**区域找到您需要下载的客户端配置文件，单击**下载**。
     2.在**下载 SSL 客户端**区域找到适合您的 SSL 客户端软件，下载后请安装该客户端。
![](https://qcloudimg.tencent-cloud.cn/raw/3ab6a81b13fd4fad19931cdbc832cfe3.png)
3. SSL 客户端安装完成后，上传您下载好的 SSL 客户端配置文件，上传后自动与 SSL 服务端连接。
4. <img src="https://qcloudimg.tencent-cloud.cn/raw/b51ffdfba9caa56ccb742d2e60403d9a.png" width="70%">
