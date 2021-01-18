# 在IntelliJ IDEA中安装和配置Tencent Cloud Toolkit

通过这篇文档，您将会了解到如何在IntelliJ IDEA中安装和配置Tencent Cloud Toolkit。安装配置完成后，您可以将本地应用快速部署到腾讯微服务平台TSF（包括虚拟机部署，容器部署），还可以使用Tencent Cloud Toolkit编译、上传程序包和镜像。

## 准备工作
* 下载并安装[JDK1.8或者更高的版本](https://www.oracle.com/java/technologies/javase-downloads.html)。
* 下载并安装[IntelliJ IDEA（2019.2或更高版本）](https://www.jetbrains.com/idea/download)。

## 安装Tencent Cloud Toolkit
您可以在JetBrains插件市场搜索Tencent Cloud Toolkit并下载安装。
1.在插件市场中下载安装。

2.在IntelliJ IDEA顶部菜单栏中选择IntelliJ IDEA > Preferences。

3.在Preferences对话框的左侧导航栏中单击Plugins

4.在Plugins区域单击Marketplace。

5.在搜索栏中输入Tencent Cloud Toolkit，并点击install。
<img src="https://main.qcloudimg.com/raw/1d86f760419847ce1b4d54267ae6b86c.png" width="50%" height="50%" alt="安装插件" align=center>

## 验证结果
IntelliJ IDEA重启后，在菜单栏中选择IntelliJ IDEA > Preferences，在Preferences对话框左侧的导航栏中可以看到Tencent Cloud Toolkit，则说明安装成功。

## 配置账户信息
使用Tencent Toolkit部署应用到云端时，需要调用TSF的API，调用API时需要使用访问密钥（SecretId，SecretKey）进行云端身份验证。因此在部署应用之前，需要先在Tencent Toolkit中配置账户信息。步骤如下。

1. 获取[SecretId和SecretKey](https://console.cloud.tencent.com/cam/capi) (PS: 如果未在腾讯云注册账号请先[注册](https://cloud.tencent.com/register),具体操作流程如下图)
  （1）点击访问管理
<img src="https://main.qcloudimg.com/raw/2624045fca2fab3bd4a39be4f4d3062c.png" width="60%" height="60%" alt="点击访问管理" align=center>

  （2）点击访问管理栏中API秘钥管理
<img src="https://main.qcloudimg.com/raw/a9ec6eb6e8d28cdf5898f56b826497d9.png" width="50%" height="50%" align=center>

2. 在IntelliJ IDEA菜单栏中选择Preferences，在Preferences对话框左侧的导航栏中选择Tencent Cloud Toolkit。

3. 配置Account 、SecretId、 SecretKey等信息。

（1） 输入AccountName 、SecretId、 SecretKey。(设置后为默认配置)

（2）点击Advanced 可以为不同环境配置不同的域名。(默认为tencentcloudapi.com)

（3）点击apply应用配置。
<img src="https://main.qcloudimg.com/raw/37cb00e7f927b7e3fd7db495c0114382.png" width="40%" height="40%" align=center>

## 后续操作
完成安装和配置Tencent Cloud Toolkit后，即可使用Tencent Toolkit部署应用。