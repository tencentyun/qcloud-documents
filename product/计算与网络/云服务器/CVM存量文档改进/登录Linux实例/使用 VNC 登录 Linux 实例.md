## 操作场景


VNC 登录是腾讯云为用户提供的一种通过 Web 浏览器远程连接云服务器的方式。在没有安装远程登录客户端或者无法使用远程登录客户端的情况下，用户可以通过 VNC 登录连接到云服务器，观察云服务器状态，并且可通过云服务器账户进行基本的云服务器管理操作。

## 适用本地操作系统

Windows，Linux 和 Mac OS 系统

## 使用限制

- VNC 登录的云服务器暂时不支持复制粘贴功能、中文输入法以及文件的上传、下载。
- VNC 登录云服务器时，需要使用主流浏览器，例如 Chrome，Firefox，IE 10及以上版本等。
- VNC 登录为独享终端，即同一时间只有一个用户可以使用 VNC 登录。

## 前提条件
已获取登录实例的管理员帐号及密码（或密钥）。
   对于不同类型的 Linux 实例，默认帐号不同。如下表所示：
<table>
<tr><th>实例操作系统</th><th>默认帐号</th><th>密码/密钥</th></tr>
<tr><td><ul><li>SUSE</li><li>CentOS</li><li>Debian</li></ul></td><td>root</td><td rowspan="2"><ul><li>如果您在购买实例时选择自动生成密码，则可登录腾讯云控制台，单击右上角的 <img src="https://main.qcloudimg.com/raw/60e7d0de182a973d69fb82b69d01f52a.png" style="margin: 0;"></img> ，进入站内消息页面，获取云服务器登录管理员帐号及初始密码。</li><li>如果您在购买实例时选择自定义密码，则登录密码为您在购买云服务器实例时指定的密码。</li><li>如果您在购买实例时选择密钥登录，请牢记密钥存放在本地的绝对路径。</li><li>如果您忘记登录云服务器的密码或密钥，请参考 <a href="https://cloud.tencent.com/document/product/213/16566">重置实例密码</a> 或者 <a href="https://cloud.tencent.com/document/product/213/16691#.E5.88.9B.E5.BB.BA-ssh-.E5.AF.86.E9.92.A5">创建 SSH 密钥</a> 进行重置。</li></ul></td></tr>
<tr><td>Ubuntu</td><td>ubuntu</td></tr>
</table>


## 操作步骤

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index) 。
2. 在实例列表中，选择需要登录的 Linux 云服务器，单击【登录】。如下图所示：
   ![](https://main.qcloudimg.com/raw/48ce59bad25e08f349dea442eee7b634.png)
3. 在弹出的【登录Linux实例】窗口，选择【其它方式（VNC）】，单击【立即登录】。如下图所示：
   ![](https://main.qcloudimg.com/raw/b73f070779ec3a42f949099fd4ed5d61.png)
4. 在弹出的对话框中，输入用户名和密码登录，即可完成登录。

## 后续操作

当您成功登录云服务器后，您可以在腾讯云服务器上搭建个人站点，论坛或者使用其他操作，相关操作可参考：
- [搭建 WordPress 个人站点](https://cloud.tencent.com/document/product/213/34064)
- [搭建 Discuz! 论坛](https://cloud.tencent.com/document/product/213/34065)

