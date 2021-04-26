## 操作场景
本文介绍如何在腾讯云云服务器（CVM）上手动安装 AMH 并搭建 PHP 网站。

进行手动安装 AMH，您需要熟悉 Linux 命令，例如  [CentOS 环境下通过 YUM 安装软件](https://cloud.tencent.com/document/product/213/2046) 等常用命令，并对所安装软件的使用及版本兼容性比较了解。
>!腾讯云建议您可以通过云市场的镜像环境部署 AMH，手动安装 AMH需要较长的时间。具体步骤可参考 [镜像部署 AMH 和建站](https://cloud.tencent.com/document/product/213/38357)。
>

## 示例软件版本
本文以在 CentOS 6.9 操作系统的 Linux 云服务器上安装 AMH 4.2 为例，您可前往 [AMH 官网](https://amh.sh/index.htm?amh) 了解更多 AMH 及支持操作系统的信息。


## 前提条件
- 已购买 Linux 云服务器。如果您还未购买云服务器，请参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。
- 使用 AMH 搭建网站需要使用已完成备案，并且已解析到所使用云服务器的域名。
腾讯云提供 [域名注册](https://dnspod.cloud.tencent.com/)、[网站备案](https://cloud.tencent.com/product/ba) 及 [DNS解析 DNSPod](https://cloud.tencent.com/product/cns) 服务，您可通过服务并参考 [建站基本流程](https://cloud.tencent.com/document/product/242/8584) 获得可使用域名。


## 操作步骤
### 步骤1：登录 Linux 实例
[使用标准方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。您也可以根据实际操作习惯，选择其他不同的登录方式：
- [使用远程登录软件登录 Linux 实例](https://cloud.tencent.com/document/product/213/35699)
- [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)

### 步骤2：手动安装 AMH
1. 执行以下命令，下载并执行 AMH 安装脚本。
```
wget http://amh.sh/file/AMH/4.2/amh.sh && chmod 775 amh.sh && ./amh.sh 2>&1 | tee amh.log
```
2. <span id="info"></span>根据界面上的信息分别输入以下信息。如下图所示：
![](https://main.qcloudimg.com/raw/3e619767eb7ac7884f5952d31251af43.png)
 1.  输入`1`并按 “**Enter**”，表示安装 AMH。
 2.  输入该云服务器的公网 IP，并按 “**Enter**”。
 3.  设置 MySQL 的登录密码，并按 “**Enter**”，本文以`123456`为例。
 4.  设置 AMH 的登录密码，并按 “**Enter**”，本文以`123456`为例。
3. 信息输入完成后，请等待 AMH 完成安装。


### 步骤3：登录 AMH
1. 使用浏览器访问以下地址
```
http://云服务器公网实例 IP:8888
```
进入 AMH 后台管理登录页面。如下图所示：
![](https://main.qcloudimg.com/raw/6d2d36d2c192b7c8822fa2c8f64f95c8.png)
2. 根据以下提示输入相关信息，并单击【登录】。
 - 管理员账号：`admin`。
 - 管理员密码：输入在 [安装 AMH](#info) 已配置的密码，本文以 `123456` 为例。
3. 如下图所示则为登录成功：
![](https://main.qcloudimg.com/raw/c8233e94cb8ebffe146a05c244098de7.png)

### 步骤4：搭建 PHP 网站
搭建 PHP 网站步骤与镜像部署 AMH 并建站中的步骤相同，详情请参见 [搭建 PHP 网站](https://cloud.tencent.com/document/product/213/38357#.E6.AD.A5.E9.AA.A42.EF.BC.9A.E6.90.AD.E5.BB.BA-php-.E7.BD.91.E7.AB.99)。


### 步骤5：安装 PHP 网站
安装 PHP 网站步骤与镜像部署 AMH 并建站中的步骤相同，详情请参见 [安装 PHP 网站](https://cloud.tencent.com/document/product/213/38357#.E6.AD.A5.E9.AA.A43.EF.BC.9A.E5.AE.89.E8.A3.85-php-.E7.BD.91.E7.AB.99)。

## 常见问题
如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考[ IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
- 云服务器硬盘问题，可参考 [系统盘和数据盘](https://cloud.tencent.com/document/product/213/17351)。



