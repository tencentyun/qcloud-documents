# 登录Linux实例

创建Linux实例后，您可以根据本地操作系统以及是否有公网IP来选择不同的登录方式连接并登录CVM实例。**腾讯云推荐您使用WebShell方式登录。**

Webshell登录方式的优点：

- 支持快捷键复制粘贴。
- 支持鼠标滚屏。
- 支持中文输入法。
- 安全性高，每次登录需要输入密码或密钥。

| 本地操作系统 | 实例购买公网IP                                               | 实例没有公网IP |
| ------------ | ---------------------------------------------------------- | -------------- |
| Windows      | WebShell 登录（推荐）<br>
远程登录软件登录
VNC登录（不推荐） |                |
| Linux        | WebShell 登录（推荐）<br/>
SSH 登录
VNC登录（不推荐）        |                |
| Mac OS       | WebShell 登录（推荐）<br/>
SSH 登录
VNC登录（不推荐）        |                |

## 前提条件

您可以选择通过密码或者密钥的方式登录：（有推荐是密码还是密钥么？）

- 如果您选择密码登录，可以登录 [腾讯云控制台](https://console.cloud.tencent.com/)，单击右侧站内信按钮，查收新购买的服务器页面中将包含云服务器登录管理员帐号及初始密码。
- 如果您在购买实例时选择了自定义密码，则密码为用户在购买云服务器实例时指定的密码。
- 如果您选择密钥登录，需要先 [创建密钥](https://cloud.tencent.com/document/product/213/16691)，然后下载保存到本地。（有十分钟的要求么？）



## 使用WebShell登录实例（推荐）

WebShell为腾讯云推荐的登录方式。无论您的本地系统为Windows，Linux或者Mac OS，只要实例有公网IP，都可以通过WebShell登录。通过WebShell方式登录需要开启SSH端口（默认为22）。

### 适用本地操作系统：

Window，Linux或者Mac OS

### 鉴权方式：

密码 或 密钥

### 前提条件：

实例有公网IP（查看实例是否有公网IP）。

开启SSH端口（查看是否开启SSH端口）。

### 操作步骤

1. 查找[腾讯云控制台](https://console.cloud.tencent.com/)，点击【实例】，选择您需要登录的云服务器并点击【登录】。——补一个截图
2. 在登录页面选择密码或者密钥的方式登录。
3. 如果登录成功，WebShell界面会出现Socket established提示。



## 使用远程登录软件登录实例

介绍以PuTTY为例如何使用远程登录软件登录您在腾讯云的Linux实例。

### 适用本地操作系统：

Windows

### 鉴权方式：

密码 或 密钥。

### 操作步骤：

您可以根据需要需要的鉴权方式选择通过密码或者通过密钥登录腾讯云实例。

#### 通过密码登录：

1. 下载[PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)软件。—这里要说清楚下载哪一个
2. 打开 PuTTY 客户端，在**PuTTY Configuration** 窗口中输入：
   - **Host Name**：输入你要连接的腾讯云服务器实例的公网IP。登录 [云服务器控制台](https://console.cloud.tencent.com/)，可在列表页及详情页中获取主机公网IP
   - **Port**：云服务器的端口，此处填写为22。
   - **Connection Type**：选择**SSH**。
3. 在弹出的对话框中，输入云服务器的管理员账号和密码登录。如果您不知道云服务器的管理员账号或密码，请在[云服务器控制台](https://console.cloud.tencent.com/)查找或重置。

#### 通过密钥登录：

1. 下载[PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)主页的putty.exe和puttygen.exe两个文件。
2. 选择私钥。打开putty.exe并单击【Load】，选择您从腾讯云服务器下载的密钥，并单击【打开】。
3. 密钥转换。在 key comment 栏中输入密钥名，输入加密私钥的密码，单击【Save private key】，在弹窗中选择您存放密钥的目录，然后在文件名栏输入 密钥名 +".ppk"，单击【保存】按钮。——补截图。
4. 打开putty.exe？？，点击【Auth】进入配置。
5. 单击【Browse】，选择刚刚保存到本地的密钥并单击【打开】，返回配置界面，进入【Session】配置。
6. 在【Session】配置中配置服务器的IP，端口和连接类型。
   - **Host Name**：输入你要连接的腾讯云服务器实例的公网IP。登录 [云服务器控制台](https://console.cloud.tencent.com/)，可在列表页及详情页中获取主机公网IP
   - **Port**：云服务器的端口，此处填写为22。
   - **Connection Type**：选择**SSH**。
7. 在【Saved Sessions】输入框中中输入会话名称（本例为 test ），再单击【Save】按钮，然后双击会话名称或者单击【Open】按钮发起登录请求。



## 使用SSH远程登录实例

介绍如何使用SSH方式远程登录腾讯云实例。

### 适用本地操作系统：

Linux 或 MacOS

### 鉴权方式：

密码 或 密钥

### 操作步骤：

适用MacOS的Terminal或者直接在Linux系统通过SSH方式远程登录腾讯云实例，你可以选择使用密码或者密钥的鉴权方式登录。

#### 通过密码登录：

1. Mac OS 用户请打开系统自带的终端（Terminal）并输入以下命令，Linux 用户请直接运行以下命令： `ssh <username>@<hostname or ip address>`
   (其中：`username`即为前提条件中获得的管理员帐号， `hostname or ip address`为您的 Linux 实例公网 IP 或 自定义域名）
2. 输入前提条件中获得的密码（此时仅有输入没有显示输出），回车后即可完成登录。

#### 通过密钥登录：

1. Mac OS 用户请打开系统自带的终端（Terminal）并输入以下命令，Linux 用户请直接运行以下命令，赋予私钥文件仅本人可读权限。`chmod 400 <下载的与云服务器关联的私钥的绝对路径>`

2. 运行以下远程登录命令：`ssh -i "<下载的与云服务器关联的私钥的绝对路径>" <username>@<hostname or ip address>。`
   (其中：`username`即为前提条件中获得的管理员帐号， `hostname or ip address`为您的 Linux 实例公网 IP 或 自定义域名。例如：`ssh -i "Mac/Downloads/shawn_qcloud_stable" ubuntu@119.xxx.xxx.xxx`）。

   

## 使用VNC远程登录实例（不推荐）

VNC 登录是腾讯云为用户提供的一种通过 Web 浏览器远程连接云服务器的方式。在没有安装远程登录客户端或者客户端远程登录无法使用的情况下，用户可以通过 VNC 登录连接到云服务器，观察云服务器状态，并且可通过云服务器账户进行基本的云服务器管理操作。

### 使用限制：

- 使用VNC登录暂时不支持复制粘贴功能、中文输入法以及文件的上传、下载。
- 要使用VNC登录，需要使用主流浏览器，如Chrome，Firefox以及IE10以上版本。
- 该终端为独享，即同一时间只有一个用户可以使用 VNC 登录。（这个待确认）

### 适用本地操作系统：

Windows，Linux和MacOS系统

### 鉴权方式：

待确定

### 操作步骤：

1. 登录[云服务器控制台](https://console.cloud.tencent.com/cvm/index)。

2. 在 “云主机” 页面中，选择需要登录的 Linux 云服务器，单击【登录】。

3. 在弹出的 “登录Linux云服务器” 窗口中，选择 “浏览器 VNC 方式登录”，单击【立即登录】。如下图所示：

   带截图。
