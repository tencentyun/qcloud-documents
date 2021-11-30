## 操作场景
WordPress 是一款使用 PHP 语言开发的博客平台，您可使用通过 WordPress 搭建属于个人的博客平台。本文档介绍通过腾讯云云服务器（CVM），手动搭建 WordPress 个人站点。

## 示例软件版本
本文搭建的 WordPress 个人站点组成版本及说明如下：
- 操作系统：Windows 操作系统，本文以 Windows Server 2012 R2 为例。
- WebPI： Microsoft Web Platform Installer，Web 平台安装程序，本文以 WebPI 5.1 为例。


## 操作步骤
### 步骤1：登录 Windows 云服务器
[使用 RDP 文件登录 Windows 实例（推荐）](https://cloud.tencent.com/document/product/213/5435)，您也可以根据实际操作习惯，选择其他不同的登录方式：
- [使用远程桌面连接登录 Windows 实例](https://cloud.tencent.com/document/product/213/35703)
- [使用 VNC 登录 Windows 实例](https://cloud.tencent.com/document/product/213/35704)

### 步骤2：安装运行时组件
下载并安装**32位版本**的 [Visual C++ Redistributable 安装包](https://www.microsoft.com/en-us/download/details.aspx?id=30679)。


### 步骤3：使用 WebPI 安装相关软件
1. 下载并安装 [Microsoft WebPI](https://www.microsoft.com/web/downloads/platform.aspx)。
2. 选择左下角的<img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:-3px 0px"> > <img src="https://main.qcloudimg.com/raw/3ad1de7c2eaef565dbd9c42dfdcedc12.png" style="margin:-3px 0px">，并在应用中打开 WebPI。
安装平台初始化时间较长，请耐心等待。
3. 选择 Web 安装平台程序左上角的【应用程序】，并在右上角搜索框中输入`wordpress`，按 “**Enter**” 进行搜索。
4. 选择 WordPress 所在行右侧的【添加】后，单击【安装】。如下图所示：
![](https://main.qcloudimg.com/raw/5572affe444934bebd94cc716269724a.png)
5. 在弹出窗口中设置 MySQL 数据库帐号密码，并单击【继续】。
数据库帐号为 root，数据库密码请自行设置并记录，本文以`123456`为例。
6. 在窗口中接受许可条款，即可开始安装。


### 步骤4：安装配置 WordPress
1. 相关软件安装完成后，在配置页面上清除【“WordPress”应用程序】名称，并单击【继续】。如下图所示：
![](https://main.qcloudimg.com/raw/4088d09522c645dcf181e7af0a32dcdf.png)
2. 在弹出的“覆盖”窗口中单击【是】。
3. （可选）请参考 [配置 WordPress 安全密钥](#secretKey) 进行配置，提高网站安全性。
>?如果选择不配置安全密钥，则单击【继续】即可开始安装。
>
4. <span id="Configuration"></span>安装完成后，可在窗口中查看软件详情，并记录 WordPress 使用的数据库相关信息。如下图所示：
![](https://main.qcloudimg.com/raw/605031cec813c1088a39bc2796cc5180.png)
5. 单击【完成】，自动访问 WordPress 安装页。
您也可以在本地浏览器访问 `http://云服务器实例公网 IP`，进行 WorsPress 配置。
6. 根据 WordPress 安装页面提示，选择 WordPress 语言版本，单击【继续】开始配置 WordPress。
7. 在 WordPress 安装页，开始配置 WordPress。如下图所示：
![](https://main.qcloudimg.com/raw/9259afb93dac100c81c910f6768ec92a.png)
8. 根据 WordPress 安装向导提示输入以下安装信息，单击【安装 WordPress】，完成安装。
<table>
 <tbody><tr><th style="width: 18%;">所需信息</th>
 <th style="width: 25%;">说明</th>
                 </tr><tr>
                 <td>
                         站点标题
                 </td>
                 <td>
                         WordPress 网站名称。
                 </td>
         </tr>
             <tr>
                 <td>
                         用户名
                 </td>
                 <td>
                         WordPress 管理员名称。出于安全考虑，建议设置一个不同于 admin 的名称。因为与默认用户名称 admin 相比，该名称更难破解。
                 </td>
         </tr>
         <tr>
                 <td>
                         密码
                 </td>
                 <td>
                         可以使用默认强密码或者自定义密码。请勿重复使用现有密码，并确保将密码保存在安全的位置。
                 </td>
         </tr>
             <tr>
                 <td>
                         您的电子邮件
                 </td>
                 <td>
                         用于接收通知的电子邮件地址。
                 </td>
         </tr>
 </tbody></table>
 现在可以用登录 WordPress 博客，并开始发布博客文章了。

## 相关操作
### 配置 WordPress 安全密钥<span id="secretKey"></span>
>?
>- WordPress 安全密钥是一组通过 [WordPress 密钥生成服务](https://api.wordpress.org/secret-key/1.1/salt/) 产生的一组随机变量，可改善用户存储在 Cookie 中的信息加密。
>- 建议您通过此步骤提高网站安全性，安全密钥配置一次即可，且无需记录。
>
1. 使用 [WordPress 密钥生成服务](https://api.wordpress.org/secret-key/1.1/salt/) 生成密钥，并将生成的密钥文本粘贴进记事本。
2. 由于 Windows 在安装 WordPress 时，无法使用密钥中的 `$`。请使用替换工具将文本中的 `$` 全部替换为 `S`。
3. 将修改后的密钥粘贴进对应输入框。
例如，修改后的 `AUTH_KEY` 为如下内容，则将其输入到 `Authentication Key` 中。如下图所示：
```bash
define('AUTH_KEY', '?Umz@%|H>3bS+&R gPDxWg,p5*c:VGc&|!s|%|9:ucA.aSMQ/4$D:.-(|!-!&0 A');
```
![](https://main.qcloudimg.com/raw/91b66dd65c742c23c29fffec314dfc13.png)
4. 将所有密钥配置完成后，单击【继续】。
>!若出现密钥不合规等错误信息，请使用 [WordPress 密钥生成服务](https://api.wordpress.org/secret-key/1.1/salt/) 重新生成密钥后再次尝试。
>
5. 请执行 [安装配置 WordPress](#Configuration) 完成网站配置。


### 配置可用域名
您可以给自己的 WordPress 博客网站设定一个单独的域名。用户可以使用易记的域名访问您的网站，而不需要使用复杂的 IP 地址。有些用户搭建网站仅用于学习，那么可使用 IP 直接安装临时使用，但不推荐这样操作。

如果您已有域名或者想要通过域名来访问您的博客，请参考以下步骤：
1. 通过腾讯云 [购买域名](https://dnspod.cloud.tencent.com/?from=qcloud)，具体操作请参考 [域名注册](https://cloud.tencent.com/document/product/242/9595)。
2. 进行 [网站备案](https://cloud.tencent.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa)。
域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云免费进行备案，一般审核时间约为20天。
3. 通过腾讯云 [云解析](https://cloud.tencent.com/product/cns?from=qcloudHpHeaderCns&fromSource=qcloudHpHeaderCns) 配置域名解析。具体操作请参考 [A 记录](https://cloud.tencent.com/document/product/302/3449)，将域名指向一个 IP 地址（外网地址）。



## 常见问题
如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
- 云服务器硬盘问题，可参考 [系统盘和数据盘](https://cloud.tencent.com/document/product/213/17351)。

