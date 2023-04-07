成功创建 SSL 客户端后，您可以在 SSL 客户端管理页下载客户端对应的配置，用于与 SSL 服务端连接。使用腾讯云下载的客户端配置，在 OpenVPN 或兼容 VPN 软件端与腾讯云 SSL 服务端连接时，将进行双向认证，通过后才允许该移动终端访问 SSL 服务端网关关联的云上资源（如 VPC 内的 CVM），确保您的通信安全。

## 租户管理员下载 SSL 客户端配置
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **SSL 客户端**，进入管理页。
3. 下载 SSL 客户端配置。
![](https://qcloudimg.tencent-cloud.cn/raw/11e34d521f5f2be9bd0f5d28534bcd1f.png)
在具体 SSL 客户端证书实例所在行单击**下载配置**。
您需要将下载好的配置文件分发至需要通过 SSL VPN 连接腾讯云的用户（例如您的公司员工），该用户需使用此文件配置 OpenVPN 或兼容的 VPN 客户端，从而实现与腾讯云 VPC 互通。详细使用方法请参考 [移动端配置](https://cloud.tencent.com/document/product/554/64229)。
>!请勿泄露配置文件给非相关人员，以避免您的资产受到损失。如果配置文件泄露，请及时停用SSL客户端，详情参考 [停用 SSL 客户端证书](https://cloud.tencent.com/document/product/554/64227#disable)。
>

## 用户通过自助 Portal 下载 SSL 客户端配置[](id:Portal)
如果您在创建 SSL 服务端时已开启身份认证，则移动终端的用户（例如您公司的员工）可以自助下载 OpenVPN 或兼容的 VPN 客户端所需的配置文件。同时，腾讯云通过身份认证确保整个下载过程的安全性。

### 前提条件
- 租户管理员已经在[ 数字身份管控平台 ](https://console.cloud.tencent.com/eiam)已创建[ 用户组 ](https://cloud.tencent.com/document/product/1442/55067)、添加了相应的[ 用户 ](https://cloud.tencent.com/document/product/1442/55066)并为用户组配置[ 应用授权](https://cloud.tencent.com/document/product/1442/55069)。详细操作请参考 [EIAM 产品文档](https://cloud.tencent.com/document/product/1442)。
- 在 VPN 控制台已 [创建 SSL 服务端](https://cloud.tencent.com/document/product/554/63717)，且 SSL 服务端支持身份认证。
- 租户管理员已经将开启身份认证的 SSL 服务端 ID 分发给您（作为用户）。如果没有，请联系您的管理员获取。


### 操作步骤
以下步骤由移动终端的用户（例如您公司的员工）自助进行。
1. 登录[ 腾讯云 Clinet VPN 自主服务门户](https://self-service.vpnconnection.tencent.com/)。
>?建议使用 Chrome 浏览器最新版本。
>
  1. 在 SSL 服务端 ID 所在行的输入框中输入前述管理员分发的 SSL 服务端实例 ID，然后单击**下一步**，进入登录界面。
![](https://qcloudimg.tencent-cloud.cn/raw/e37b558345b8edeae794d9f650071c5f.png)
  2. 进行身份认证。      
单击![](https://qcloudimg.tencent-cloud.cn/raw/6c78a80d3aadbade303cd3158eba47b9.png)进行 SAML 认证，然后单击**跳转进行认证（SAML）**进行登录。您需要使用您的租户管理员指定的身份认证方式通过认证。例如，租户管理员在 EIAM 指定与您的企业账号系统对接认证，则您将在浏览器上看到您归属企业的域账号登录页面，请输入您的域账号通过认证。如果管理员指定了其他的身份认证方式，如企业微信，则您需要通过对应的账号进行认证。
>?
>1. 目前仅支持通过 SAML 认证登录，请确保您在 EIAM 的用户组中，并在 SSL 访问控制策略中。如果提示“未授权访问该应用，请联系管理员”，可联系管理官将您添加到 EIAM 用户组即可。
>2. 如果您有修改 EIAM 应用需求，请确保原 EIAM 应用中的用户已经迁移至新的 EIAM 应用，避免原应用中用户无法访问。
>3. 切换 EIAM 应用后，已连接的 SSL VPN 连接不会中断。
>
2. 下载 SSL 客户端配置文件和 SSL 客户端。
  1. 在**下载 SSL 客户端配置文件**区域找到您需要下载的客户端配置文件，单击**下载**。
  2. 在**下载 SSL 客户端**区域找到适合您的 SSL 客户端软件，下载后请安装该客户端。
![](https://qcloudimg.tencent-cloud.cn/raw/3ab6a81b13fd4fad19931cdbc832cfe3.png)
3. SSL 客户端安装完成后，上传您下载好的 SSL 客户端配置文件，上传后自动与 SSL 服务端连接。
<img src="https://qcloudimg.tencent-cloud.cn/raw/b51ffdfba9caa56ccb742d2e60403d9a.png" width="35%"> 
