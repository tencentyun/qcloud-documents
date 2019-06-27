## 操作场景

WebShell 为腾讯云推荐的登录方式。无论您的本地系统为 Windows，Linux 或者 Mac OS，只要实例购买了公网 IP，都可以通过 WebShell 登录。本文介绍如何使用标准登录方式（WebShell）登录 Linux 实例。
WebShell 优点如下：
- 支持快捷键复制粘贴。
- 支持鼠标滚屏。
- 支持中文输入法。
- 安全性高，每次登录需要输入密码或密钥。

## 适用本地操作系统

Window，Linux 或者 Mac OS

## 鉴权方式

**密码**或**密钥**

## 前提条件

- 已获取登录实例的管理员帐号及密码（或密钥）。
   对于不同类型的 Linux 实例，默认帐号不同。如下表所示：
<table>
<tr><th>实例操作系统</th><th>默认帐号</th><th>密码/密钥</th></tr>
<tr><td><ul><li>SUSE</li><li>CentOS</li><li>Debian</li></ul></td><td>root</td><td rowspan="2"><ul><li>如果您在购买实例时选择自动生成密码，则可登录腾讯云控制台，单击右上角的 <img src="https://main.qcloudimg.com/raw/60e7d0de182a973d69fb82b69d01f52a.png" style="margin: 0;"></img> ，进入站内消息页面，获取云服务器登录管理员帐号及初始密码。</li><li>如果您在购买实例时选择自定义密码，则登录密码为您在购买云服务器实例时指定的密码。</li><li>如果您在购买实例时选择密钥登录，请牢记密钥存放在本地的绝对路径。</li><li>如果您忘记登录云服务器的密码或密钥，请参考 <a href="https://cloud.tencent.com/document/product/213/16566">重置实例密码</a> 或者 <a href="https://cloud.tencent.com/document/product/213/16691#.E5.88.9B.E5.BB.BA-ssh-.E5.AF.86.E9.92.A5">创建 SSH 密钥</a> 进行重置。</li></ul></td></tr>
<tr><td>Ubuntu</td><td>ubuntu</td></tr>
</table>
- 已打开云服务器实例的22号端口。
   您可以通过 [检查网络连通性](https://cloud.tencent.com/document/product/213/10232#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E6.A3.80.E6.9F.A5.E7.BD.91.E7.BB.9C.E8.BF.9E.E9.80.9A.E6.80.A7) 检查22号端口是否放通。如果端口不通，您可以在 [配置安全组](https://cloud.tencent.com/document/product/213/15377) 时设置端口的入站/出站规则。
- 云服务器实例已购买公网 IP。

## 操作步骤

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index) 。
2. 在实例列表中，选择需要登录的 Linux 云服务器，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/48ce59bad25e08f349dea442eee7b634.png)
3. 在弹出的【登录Linux实例】窗口，选择【标准登录方式】，单击【立即登录】。如下图所示：
![](https://main.qcloudimg.com/raw/673f427fca54c4ca115cf9dab707f3c2.png)
4. 在打开的 WebShell 登录页面，根据实际需求，选择【密码登录】或者【密钥登录】方式进行登录。如下图所示：
![](https://main.qcloudimg.com/raw/22e2e003bf407076596f615c4b92ff53.png)
如果登录成功，WebShell 界面会出现 Socket connection established 提示。如下图所示：
![](https://mc.qcloudimg.com/static/img/31b25c56a1e6afdd39533436589ceb04/Snipaste_2018-02-02_18-21-02.png)

## 登录后续操作

当您成功登录云服务器后，您可以在腾讯云服务器上搭建个人站点，论坛或者使用其他操作，相关操作可参考：
- [搭建 WordPress 个人站点](https://cloud.tencent.com/document/product/213/34064)
- [搭建 Discuz! 论坛](https://cloud.tencent.com/document/product/213/34065)

