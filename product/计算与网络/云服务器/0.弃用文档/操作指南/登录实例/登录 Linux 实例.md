## 操作场景

创建 Linux 实例后，您可以根据本地操作系统以及是否有公网 IP 来选择不同的登录方式连接并登录 CVM 实例。如下表所示：

<table>
<tr><th>本地操作系统</th><th>实例有公网 IP</th><th>实例没有公网 IP</th></tr>
<tr><td>Windows</td><td><ul style="margin: 0;"><li>标准（WebShell） 登录方式（推荐）</li><li>远程登录软件登录（密码或密钥）</li></ul></td><td rowspan="3">VNC 登录</td></tr>
<tr><td>Linux</td><td rowspan="2"><ul style="margin: 0;"><li>标准（WebShell） 登录方式（推荐）</li><li>使用SSH登录（密码或密钥）</li></ul></td></tr>
<tr><td>Mac OS</td></tr>
</table>

**腾讯云推荐您使用标准登录方式（WebShell）。**标准登录方式（Webshell）的优点如下：

- 支持快捷键复制粘贴。
- 支持鼠标滚屏。
- 支持中文输入法。
- 安全性高，每次登录需要输入密码或密钥。

## 前提条件
1. 已获取登录实例的管理员帐号及密码（或密钥）。
   对于不同类型的 Linux 实例，管理员帐号不同。如下表所示：

<table>
<tr><th>实例操作系统</th><th>管理员帐号</th><th>密码</th><th>密钥</th></tr>
<tr><td>SUSE/CentOS/Debian</td><td>root</td><td rowspan="2">如果在购买实例时选择密码登录：<li>如果您在购买实例时设置了自动生成密码，可以登录腾讯云控制台，单击右上角的 <img src="https://main.qcloudimg.com/raw/60e7d0de182a973d69fb82b69d01f52a.png" style="margin: 0;"></img> ，进入站内消息页面，该页面将包含云服务器登录管理员帐号及初始密码。</li><li>如果您选择了自定义密码，则密码为您在购买云服务器实例时指定的密码。</li> </td><td rowspan="2">如果您在购买实例时选择密钥登录，请牢记密钥存放在本地的绝对路径。</td></tr>
<tr><td>Ubuntu</td><td>ubuntu</td></tr>
</table>

如果您忘记登录云服务器的密码或密钥，请参考 [重置实例密码](https://cloud.tencent.com/document/product/213/16566) 或者 [创建 SSH 密钥](https://cloud.tencent.com/document/product/213/16691#.E5.88.9B.E5.BB.BA-ssh-.E5.AF.86.E9.92.A5) 进行重置。

2. 已打开云服务器实例的22号端口。
   您可以通过 [检查网络连通性](https://cloud.tencent.com/document/product/213/10232#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E6.A3.80.E6.9F.A5.E7.BD.91.E7.BB.9C.E8.BF.9E.E9.80.9A.E6.80.A7) 检查22号端口是否放通。如果端口不通，您可以在 [配置安全组](https://cloud.tencent.com/document/product/213/15377) 时设置端口的入站/出站规则。

## 使用标准登录方式（WebShell）登录实例（推荐）

WebShell 为腾讯云推荐的登录方式。无论您的本地系统为 Windows，Linux 或者 Mac OS，只要实例购买了公网 IP，都可以通过 WebShell 登录。通过 WebShell 方式登录需要开启 SSH 端口（默认为22）。

### 适用本地操作系统

Window，Linux 或者 Mac OS

### 鉴权方式

**密码**或**密钥**

### 前提条件

- 实例已购买公网 IP。
- 已开启 SSH（22号）端口。您可以通过 [配置安全组](https://cloud.tencent.com/document/product/213/15377) 确认是否开启22号端口。

### 操作步骤

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index) 。
2. 在实例列表中，选择需要登录的 Linux 云服务器，单击【登录】。如下图所示：
   ![](https://main.qcloudimg.com/raw/48ce59bad25e08f349dea442eee7b634.png)
3. 在弹出的【登录Linux实例】窗口，选择【标准登录方式】，单击【立即登录】。如下图所示：
   ![](https://main.qcloudimg.com/raw/673f427fca54c4ca115cf9dab707f3c2.png)
4. 在打开的 WebShell 登录页面，根据实际需求，选择【密码登录】或者【密钥登录】方式进行登录。如下图所示：
   ![](https://main.qcloudimg.com/raw/22e2e003bf407076596f615c4b92ff53.png)
   如果登录成功，WebShell 界面会出现 Socket connection established 提示。如下图所示：
   ![](https://mc.qcloudimg.com/static/img/31b25c56a1e6afdd39533436589ceb04/Snipaste_2018-02-02_18-21-02.png)

## 远程登录软件登录（本地系统为 Windows）

以 PuTTy 软件为例，介绍本地为 Windows 系统的电脑如何使用远程登录软件通过密码或者密钥登录 Linux 实例。

### 适用本地操作系统

Windows

### 鉴权方式

**密码**或**密钥**

### 使用密码登录

#### 操作步骤

1. 安装 Windows 远程登录软件，即 PuTTy。
   PuTTy 的获取方式：[点此获取](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
2. 打开 PuTTY 客户端，在 PuTTY Configuration 窗口中输入以下内容，并单击【Open】，创建一个新对话。如下图所示：
   ![](https://main.qcloudimg.com/raw/7ac87da9721ef7d64fe8cac81a3dab33.png)
   - Host Name：云服务器的公网 IP（登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，可在列表页及详情页中获取主机公网 IP）。
   - Port：云服务器的端口，必须填22。（请确保云服务器22端口已开放，详见查看 [安全组](https://cloud.tencent.com/document/product/213/12452) 及 [网络 ACL](https://cloud.tencent.com/document/product/215/20088)）
   - Connect type：选择 “SSH ”。
3. 在 PuTTY 会话窗口中，输入已获取的管理员帐号，按 **Enter**。
4. 输入已获取的登录密码，按 **Enter**，即可完成登录。如下图所示：
   ![](//mccdn.qcloud.com/img56a5d47b8b5da.png)

> ! 如果登录失败，请检查您的云服务器实例是否允许22端口的入流量。端口的查看请参考 [安全组](https://cloud.tencent.com/document/product/213/12452)，若您的云服务器处于 [私有网络](https://cloud.tencent.com/document/product/213/5227) 环境下，请同时查看相关子网的 [网络 ACL](https://cloud.tencent.com/document/product/215/20088) 。

### 使用密钥登录

#### 操作步骤

1. 安装 Windows 远程登录软件，即 PuTTy。
   PuTTy 的获取方式：[点此获取](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)，分别下载 putty.exe 及 puttygen.exe 两个文件。
2. 打开 puttygen.exe，单击【Load】。如下图所示：
   ![](https://main.qcloudimg.com/raw/0110ba722331fb2892a8e6822ec3f709.png)
3. 在弹出的窗口中，将“文件名”类型设置为 “All File（\*.\*）”，选择已下载的私钥存储路径，单击【打开】。例如，选择文件名为 david 的私钥文件，如下图所示：
   ![](https://main.qcloudimg.com/raw/9d7062e5c78b327b942fc611bf0aa98c.png)
4. 在 key comment 中，输入密钥名和加密私钥的密码，单击【Save private key】。如下图所示：
   ![](https://main.qcloudimg.com/raw/58a250d3f3d1b78eff3edaab64cd01c0.png)
5. 在弹出的窗口中，选择您存放密钥的路径，并在文件名栏输入“密钥名.ppk”，单击【保存】。例如，将 david 私钥文件另存为 david.ppk 密钥文件。如下图所示：
   ![](https://main.qcloudimg.com/raw/d0fa9fd8aad7d2259bd8a0ce48ae5160.png)
6. 打开 putty.exe ，进入【Auth】配置，单击【Browse】。如下图所示：
   ![](https://main.qcloudimg.com/raw/05428f4c6dbc593c164c151f2bc08a9f.png)
7. 在弹出的窗口中，选择密钥的存储路径，单击【打开】。如下图所示：
   ![](https://main.qcloudimg.com/raw/343d94c6e7ec992c8084b08071cbe331.png)
8. 切换至 Session 配置界面，配置服务器的 IP、端口，以及连接类型，单击【Save】。如下图所示：
   ![](https://main.qcloudimg.com/raw/ddfd58429288ce0e195e86a6cb1c9cd6.png)

- Host Name (IP address)：云服务器的公网 IP。登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，可在列表页及详情页中获取主机公网IP。
- Port：云服务器的端口，必须填 22 。（请确保云服务器 22 端口已开放，详见查看 安全组 及 网络 ACL）。
- Saved Sessions：填写会话名称，例如 test。

9. 双击会话名称或者单击【Open】，发起登录请求。

> ! 如果登录失败，请检查您的云服务器实例是否允许22端口的入流量。端口的查看请参考 [安全组](https://cloud.tencent.com/document/product/213/12452)，若您的云服务器处于 [私有网络](https://cloud.tencent.com/document/product/213/5227) 环境下，请同时查看相关子网的 [网络 ACL](https://cloud.tencent.com/document/product/215/20088) 。

## 使用 SSH 登录（本地系统为 Linux/Mac OS）

介绍本地为 Linux/Mac OS 系统的电脑通过 SSH 登录 Linux 实例。

### 适用本地操作系统

Linux 或 Mac OS

### 鉴权方式

**密码**或**密钥**

### 使用密码登录

#### 操作步骤

1. Mac OS 用户请打开系统自带的终端（Terminal）并执行以下命令，Linux 用户请直接执行以下命令：

```
ssh <username>@<hostname or IP address>
```

- `username` 即为前提条件中获得的管理员帐号。
- `hostname or IP address` 为您的 Linux 实例公网 IP 或 自定义域名。

2. 输入已获取的密码（此时仅有输入没有显示输出），按 **Enter**，即可完成登录。

### 使用密钥登录

#### 前提条件

- 已完成创建密钥。
- 已将密钥绑定 Linux 云服务器。  
  可登录[腾讯云控制台](https://console.cloud.tencent.com/cvm/)，单击左侧导航栏 SSH 密钥，查看和管理已创建的密钥信息。关于密钥的操作的更多内容，请参阅 [SSH 密钥操作](/doc/product/213/6092)。

#### 操作步骤

1. Mac OS 用户请打开系统自带的终端（Terminal）并输入以下命令，Linux 用户请直接运行以下命令，赋予私钥文件仅本人可读权限。

```
chmod 400 <下载的与云服务器关联的私钥的绝对路径>
```

2. 执行以下命令，进行远程登录。

```
ssh -i <下载的与云服务器关联的私钥的绝对路径> <username>@<hostname or IP address>
```

- `username` 即为前提条件中获得的管理员帐号。
- `hostname or IP address` 为您的 Linux 实例公网 IP 或 自定义域名。

 例如，执行 `ssh -i "Mac/Downloads/shawn_qcloud_stable" ubuntu@119.xxx.xxx.xxx` 命令。

## 使用 VNC 远程登录实例（不推荐）

VNC 登录是腾讯云为用户提供的一种通过 Web 浏览器远程连接云服务器的方式。在没有安装远程登录客户端或者客户端远程登录无法使用的情况下，用户可以通过 VNC 登录连接到云服务器，观察云服务器状态，并且可通过云服务器账户进行基本的云服务器管理操作。

### 适用本地操作系统

Windows，Linux 和 Mac OS 系统

### 使用限制

- 使用 VNC 登录暂时不支持复制粘贴功能、中文输入法以及文件的上传、下载。
- 要使用 VNC 登录，需要使用主流浏览器，例如 Chrome，Firefox，IE 10及以上版本等。
- 该终端为独享，即同一时间只有一个用户可以使用 VNC 登录。

### 操作步骤

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index) 。
2. 在实例列表中，选择需要登录的 Linux 云服务器，单击【登录】。如下图所示：
   ![](https://main.qcloudimg.com/raw/48ce59bad25e08f349dea442eee7b634.png)
3. 在弹出的【登录Linux实例】窗口，选择【其它方式（VNC）】，单击【立即登录】。如下图所示：
   ![](https://main.qcloudimg.com/raw/b73f070779ec3a42f949099fd4ed5d61.png)
4. 在弹出的对话框中，输入用户名和密码登录，即可完成登录。

## 登录后续操作

当您成功登录云服务器后，您可以在腾讯云服务器上搭建个人站点，论坛或者使用其他操作，相关操作可参考：

- [搭建 WordPress 个人站点](https://cloud.tencent.com/document/product/213/34064)
- [搭建 Discuz! 论坛](https://cloud.tencent.com/document/product/213/34065)

