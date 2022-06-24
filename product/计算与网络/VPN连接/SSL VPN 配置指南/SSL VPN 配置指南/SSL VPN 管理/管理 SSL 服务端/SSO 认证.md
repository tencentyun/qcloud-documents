若您通过 [自助 Portal](https://self-service-test.vpn.woa.com/) 下载 SSL 客户端配置，可以在 SSL 服务端开启 SSO 认证。

## 前提条件
在 [数字身份管控平台](https://console.cloud.tencent.com/eiam) 已创建 [用户组](https://cloud.tencent.com/document/product/1442/55067)、添加了相应的 [用户](https://cloud.tencent.com/document/product/1442/55066) 并配为用户组配置 [应用授权](https://cloud.tencent.com/document/product/1442/55069)。


## 在创建 SSL 服务端过程中开启
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **SSL 服务端**，进入管理页面。
3. 在 SSL 服务端管理页面，单击**+新建**。
4. 在弹出的**新建 SSL 服务端**对话框中，**认证方式**选择**证书认证** + **身份认证**，然后选择 EIAM 应用。
<img src="https://qcloudimg.tencent-cloud.cn/raw/e84fd4674fa394c8286462da60edcd52.png" width="70%">
5. **访问控制**按需**开启**，详情请参见 [开启访问控制](https://cloud.tencent.com/document/product/554/75188)。

## 在 SSL 服务端创建完成后开启
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **SSL 服务端**，进入管理页面。
3. 在 SSL 服务端管理页面，单击具体的实例名称。
4. 在实例详情页的**基本信息**页签的**服务端配置**区域单击**编辑**。
5. **认证方式**选择**证书认证** + **身份认证**，并选择 EIAM 应用，然后单击**保存**。
![](https://qcloudimg.tencent-cloud.cn/raw/bc4f4061b1bef06fd57b832420253ee3.png)
