## 操作场景
部署 SSL 证书，可以让您的网站实现 HTTPS 加密协议访问。SSL 证书可实现加密传输、认证服务器真实身份、保障信息不被窃取、提高网站搜索排名、提高网站访问速度、提高公司品牌形象和可信度等作用。
本文档将介绍如何为您的网站部署 SSL 证书。

## 前提条件
- 已拥有绑定域名对应的 SSL 证书。
- 已购买标准版网站建设服务。

>?
>- 如需购买 SSL 证书，您可以在腾讯云 [SSL 证书购买页](https://buy.cloud.tencent.com/ssl?fromSource=ssl) 进行购买。详情请查看 [购买指南](https://cloud.tencent.com/document/product/400/7995)。
>- 网站建设暂不支持国密证书（DNSPod 证书）部署。

## 操作步骤

1. 登录腾讯云 [网站建设控制台](https://console.cloud.tencent.com/wds)，选择您需要进行建站服务的 “服务名称”，单击【管理】。
2. 在网站服务详情中，单击 “网站管理” 模块下的【管理后台地址】。
3. 由网站建设控制台跳转到建站引导页面后，选择您需要部署的网站，单击【免费开启】。如下图所示：
![](https://main.qcloudimg.com/raw/be5c9cc7b208d2b3c2c7fc9c4a4fb5f6.png)
4. 在弹出的【开启 https】窗口中，单击【浏览】上传证书与私钥文件。如下图所示：
>?请您在 [SSL 证书控制台](https://console.cloud.tencent.com/ssl) 下载证书文件，并上传 Nginx 文件内容至证书与私钥文件。
>
![](https://main.qcloudimg.com/raw/d276400ebbd532393623d3dfe4f30cad.png)
 - **证书文件**：请上传 Nginx 目录下 .crt 后缀证书文件。
 - **私钥文件**：请上传 Nginx 目录下 .key 后缀私钥文件。
5. 单击【确认上传】。证书状态为 “证书部署成功” 即可完成部署证书操作。如下图所示：
![](https://main.qcloudimg.com/raw/a66d1a4865cc733d8e7fc635ad913eb2.png)



