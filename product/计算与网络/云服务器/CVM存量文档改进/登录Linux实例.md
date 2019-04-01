创建Linux实例后，您可以根据本地操作系统以及是否有公网IP来选择不同的登录方式连接并登录CVM实例。**腾讯云推荐您使用标准登录方式（WebShell）。**

标准登录方式（Webshell）的优点：

- 支持快捷键复制粘贴。
- 支持鼠标滚屏。
- 支持中文输入法。
- 安全性高，每次登录需要输入密码或密钥。

<br>

| 本地操作系统    | 实例有公网IP                               | 实例没有公网IP    |
| --------------- | ------------------------------------------ | ----------------- |
| Windows         | 标准（WebShell） 登录方式（推荐）<br> 远程登录软件登录（密码或密钥） | VNC登录 |
| Linux<br>Mac OS | 标准（WebShell） 登录方式（推荐）<br/>使用SSH登录（密码或密钥）   | VNC登录 |

## 前提条件

- 准备好登录实例前的密码或者密钥。
- 确保云服务器实例的22号端口已打开。您可以通过[检查网络连通性](https://cloud.tencent.com/document/product/213/10232#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E6.A3.80.E6.9F.A5.E7.BD.91.E7.BB.9C.E8.BF.9E.E9.80.9A.E6.80.A7)检查22号端口是否放通。如果端口不通，您可以在[配置安全组](https://cloud.tencent.com/document/product/213/15377)时设置端口的入站/出站规则。

### 使用密码登录
**管理员账号**：对于不同类型的 Linux 实例，管理员帐号不同，如下表。

| 实例操作系统 | 管理员帐号 | 
|---------|---------|
| SUSE/CentOS/Debian | root |
| Ubuntu | ubuntu |

- 如果您选择密码登录，可以登录 [腾讯云控制台](https://console.cloud.tencent.com/)，单击右侧站内信按钮，查收新购买的服务器页面中将包含云服务器登录管理员帐号及初始密码。
 ![](//mc.qcloudimg.com/static/img/d2d6900e58fc4f7b141b770de23cd3d8/image.png)


- 如果您在购买实例时选择了自定义密码，则密码为用户在购买云服务器实例时指定的密码。

### 使用密钥登录
如果您选择密钥登录，需要先 [创建密钥](https://cloud.tencent.com/document/product/213/16691)、下载私钥、绑定 Linux 云服务器。有关密钥操作的更多内容，请参阅 [SSH 密钥](/doc/product/213/6092)。



## 使用标准登录方式（WebShell）登录实例（推荐）

WebShell为腾讯云推荐的登录方式。无论您的本地系统为Windows，Linux或者Mac OS，只要实例购买了公网IP，都可以通过WebShell登录。通过WebShell方式登录需要开启SSH端口（默认为22）。

### 适用本地操作系统：

Window，Linux或者Mac OS

### 鉴权方式：

密码 或 密钥

### 前提条件：

实例是否购买公网IP。

开启SSH（22号）端口，您可以通过[配置安全组](https://cloud.tencent.com/document/product/213/15377)的设置确认是否开启22号端口。

### 操作步骤

1. 登录 [云服务器控制台](https://console.cloud.tencent.com) 。在顶部菜单中选择【云产品】>【云计算与网络】>【云服务器】。
2.  如图所示进入云服务器列表，在需要登录的 Linux 云服务器中单击【登录】按钮。
![](https://mc.qcloudimg.com/static/img/0c9dd598a6b9405e43e54dd412fc7ffd/Snipaste_2018-02-02_18-32-54.png)
3. 在【登录Linux实例】页面，选择【标准登录方式】。![](https://main.qcloudimg.com/raw/8c0fbe2b618902a3f57ae303517956ae.png)
4. 在跳转的新标签页中可看到如下图的界面，可以选择【密码登录】或者【密钥登录】两种方式进行登录。
![](https://main.qcloudimg.com/raw/f33c4591b249bbca1ddba3868aacc033.png)
4. 若密码或密钥无误，将会通过系统验证，成功使用 Webshell 方式登录 Linux 云服务器。
![](https://mc.qcloudimg.com/static/img/31b25c56a1e6afdd39533436589ceb04/Snipaste_2018-02-02_18-21-02.png)
4. 如果登录成功，WebShell界面会出现Socket connection established提示。



## 远程登录软件登录（Windows）

以PuTTy软件为例，介绍如何使用远程登录软件通过密码或者密钥登录Linux实例。

### 适用本地操作系统：

Windows

### 鉴权方式：

密码 或 密钥

### 使用密码登录

#### 操作步骤：

1. 安装 Windows 远程登录软件，参考[下载PuTTy](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)。
2. 使用 PuTTY 连接 Linux 云服务器。打开 PuTTY 客户端，在PuTTY Configuration 窗口中输入以下内容：
  - Host Name：云服务器的公网 IP（登录 [云服务器控制台](https://console.cloud.tencent.com)，可在列表页及详情页中获取主机公网IP）。
  - Port：云服务器的端口，必须填 22。（请确保云服务器 22 端口已开放，详见查看 [安全组](/doc/product/213/5221) 及 [网络ACL](/doc/product/215/5132)）
  - Connect type：选择“ SSH ”。
3. 输入完后，单击【Open】，创建一个新对话。
  ![](//mccdn.qcloud.com/img56a5d38a4ffbc.png)
4. 在 PuTTY 会话窗口中，输入前提条件中获得的管理员帐号，按回车键。再输入前提条件中获取的登录密码，回车完成登录过程。
  ![](//mccdn.qcloud.com/img56a5d47b8b5da.png)

>! 如果登录失败，请检查您的云服务器实例是否允许 22 端口的入流量。端口的查看请参考 [安全组](/doc/product/213/5221) ,若您的云服务器处于 [私有网络](/doc/product/213/5227) 环境下，请同时查看相关子网的 [网络ACL](/doc/product/215/5132) 。

### 使用密钥登录

#### 操作步骤：
1. 安装 Windows 远程登录软件，参考下载地址：https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html ，分别下载 putty.exe 及 puttygen.exe 两个文件。
2. 选择私钥。打开 puttygen.exe，单击【Load】按钮，在弹窗中首先进入您存放前提条件中下载下来的私钥的路径，然后选择“All File（\*.\*）”，选择下载好的私钥（例子中为文件david，david是密钥的名称），单击【打开】。
![](//mccdn.qcloud.com/img56a5c48fb810a.png)
3. 密钥转换。在 key comment 栏中输入密钥名，输入加密私钥的密码，单击【Save private key】，在弹窗中选择您存放密钥的目录，然后在文件名栏输入 密钥名 +".ppk"，单击【保存】按钮。
![](//mccdn.qcloud.com/img56a5c4ff657cc.png)
4. 打开 putty.exe ，进入【Auth】配置。
![](//mccdn.qcloud.com/img56a5c61c61e42.png)
5. 单击【Browse】按钮，打开弹窗后进入密钥存储的路径，并选择密钥，单击【打开】，返回配置界面，进入【Session】配置。
  ![](//mccdn.qcloud.com/img56a5c67ea3edb.png)
6. 在Session配置页中，配置服务器的IP，端口，连接类型。
 - IP：云服务器的公网IP。登录 [云服务器控制台](https://console.cloud.tencent.com)，可在列表页及详情页中获取主机公网IP。
 - 端口：云服务器的端口，必须填 22 。（请确保云服务器 22 端口已开放，详见查看 安全组 及 网络ACL）。
7. 在【Saved Sessions】输入框中中输入会话名称（本例为 test ），再单击【Save】按钮，然后双击会话名称或者单击【Open】按钮发起登录请求。
![](//mccdn.qcloud.com/img56a5c6bca781f.png)

>! 如果登录失败，请检查您的云服务器实例是否允许 22 端口的入流量。端口的查看请参考 [安全组](/doc/product/213/5221) ，若您的云服务器处于 [私有网络](/doc/product/213/5227) 环境下，请同时查看相关子网的 [网络ACL](/doc/product/215/5132) 。 



## 使用SSH登录（Linux/Mac OS）

介绍本地为Linux/Mac OS系统的电脑通过SSH登录Linux实例。

### 适用本地操作系统：

Linux 或 Mac OS

### 鉴权方式：

密码 或 密钥

### 使用密码登录
#### 操作步骤：

1. Mac OS 用户请打开系统自带的终端（Terminal）并输入以下命令，Linux 用户请直接运行以下命令：

```
ssh <username>@<hostname or IP address>
```

   其中：`username`即为前提条件中获得的管理员帐号， `hostname or IP address`为您的 Linux 实例公网 IP 或 自定义域名。
	 

2. 输入前提条件中获得的密码（此时仅有输入没有显示输出），回车后即可完成登录。

### 使用密钥登录
#### 操作步骤：

1. Mac OS 用户请打开系统自带的终端（Terminal）并输入以下命令，Linux 用户请直接运行以下命令，赋予私钥文件仅本人可读权限。

```
chmod 400 <下载的与云服务器关联的私钥的绝对路径>
```

2. 运行以下远程登录命令：

```
ssh -i <下载的与云服务器关联的私钥的绝对路径> <username>@<hostname or IP address>
```

   (其中：`username`即为前提条件中获得的管理员帐号， `hostname or IP address`为您的 Linux 实例公网 IP 或 自定义域名。例如：`ssh -i "Mac/Downloads/shawn_qcloud_stable" ubuntu@119.xxx.xxx.xxx`）。

## 使用VNC远程登录实例（不推荐）

VNC 登录是腾讯云为用户提供的一种通过 Web 浏览器远程连接云服务器的方式。在没有安装远程登录客户端或者客户端远程登录无法使用的情况下，用户可以通过 VNC 登录连接到云服务器，观察云服务器状态，并且可通过云服务器账户进行基本的云服务器管理操作。

### 使用限制：

- 使用VNC登录暂时不支持复制粘贴功能、中文输入法以及文件的上传、下载。
- 要使用VNC登录，需要使用主流浏览器，如Chrome，Firefox以及IE10以上版本。
- 该终端为独享，即同一时间只有一个用户可以使用 VNC 登录。

### 适用本地操作系统：

Windows，Linux和MacOS系统

### 操作步骤：

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index) 。
2. 在 “云服务器” 页面中，选择需要登录的 Linux 云服务器，单击【登录】。如下图所示：
  ![](https://mc.qcloudimg.com/static/img/0c9dd598a6b9405e43e54dd412fc7ffd/Snipaste_2018-02-02_18-32-54.png)
3. 在弹出的 “登录Linux云服务器” 窗口中，选择 “其他方式（VNC）”，单击【立即登录】。如下图所示：
![](https://main.qcloudimg.com/raw/11316c461d7e0090ccbabd9373ce4735.png)
4. 在弹出的对话框中，输入用户名和密码登录。
>! 
	- 该终端为独享，即同一时间只有一个用户可以使用 VNC 登录。
	- 要正常使用 VNC 登录，需要使用主流浏览器，如：Chrome，firefox，IE10 及以上版本等。
	- 暂不支持文件上传下载。

