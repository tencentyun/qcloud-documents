## 操作场景
通过这篇文档，您将会了解到如何在 IntelliJ IDEA 中安装和配置 Tencent Cloud Toolkit。安装配置完成后，您可以将本地应用快速部署到腾讯微服务平台 TSF（包括虚拟机部署、容器部署），还可以使用 Tencent Cloud Toolkit 编译、上传程序包和镜像。

## 准备工作

- 下载并安装 [JDK1.8 或者更高的版本](https://www.oracle.com/java/technologies/javase-downloads.html)。
- 下载并安装 [IntelliJ IDEA（2019.2或更高版本）](https://www.jetbrains.com/idea/download)。

## 安装 Tencent Cloud Toolkit

您可以在 JetBrains 插件市场搜索“Tencent Cloud Toolkit”并下载安装，操作步骤如下：
1. 在插件市场中下载安装。
2. 在 IntelliJ IDEA 顶部菜单栏中选择【File】>【Settings】。
3. 在 Settings 对话框的左侧导航栏中，单击【Plugins】进入 Plugins 页面。
4. 在 Plugins 页面上方，单击【Marketplace】。
5. 在搜索栏中输入“Tencent Cloud Toolkit”，并单击【install】。
![](https://main.qcloudimg.com/raw/d83ef7132a03043e2c73bc3c2c058b5d.png)


## 验证结果

IntelliJ IDEA 重启后，在菜单栏中单击【File】>【Settings】，在 Settings 对话框左侧的导航栏中可以看到 Tencent Cloud Toolkit，则说明安装成功。

## 配置账户信息

使用 Tencent Toolkit 部署应用到云端时，需要调用 TSF 的 API，调用 API 时需要使用访问密钥（SecretId 和 SecretKey）进行云端身份验证。因此在部署应用之前，需要先在 Tencent Toolkit 中配置账户信息，操作步骤如下：

1. 在 [API 密钥管理控制台](https://console.cloud.tencent.com/cam/capi) 中获取 SecretId 和 SecretKey（如果未在腾讯云注册账号请先 [注册](https://cloud.tencent.com/register)）。
<img src="https://main.qcloudimg.com/raw/27836a0af91c0e6d47ecd01fe6daddca.png" width="70%" height="70%">

2. 在 IntelliJ IDEA 菜单栏中单击【File】>【Settings】，在 Settings 对话框左侧的导航栏中单击【Tencent Cloud Toolkit】>【Accounts】。
3. 配置 ProfileName 、SecretId、 SecretKey 等信息。
 1. 输入 ProfileName 、SecretId、 SecretKey。(设置后为默认配置)
 2. 单击 Advanced 可以为不同环境配置不同的域名。(默认为 tencentcloudapi.com)
 3. 单击 apply 应用配置。
![](https://main.qcloudimg.com/raw/0c58deaf2dd902f9cabe513d14244d61.png)


## 后续操作

完成安装和配置 Tencent Cloud Toolkit 后，即可 [使用 Tencent Toolkit 部署应用](https://cloud.tencent.com/document/product/649/51455)。
