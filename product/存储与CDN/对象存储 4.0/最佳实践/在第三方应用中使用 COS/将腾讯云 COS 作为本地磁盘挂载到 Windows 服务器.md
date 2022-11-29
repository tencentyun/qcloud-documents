## 操作场景
在 Windows 系统上操作腾讯云对象存储（Cloud Object Storage，COS），目前主要的实现方式还是通过 API、COSBrowser、COSCMD 工具。

而对于喜欢使用 Windows 服务器的用户，使用 COSBrowser 工具大多只能当做网盘，对服务器上的直接使用程序或者操作并不友好。本文将介绍如何使存储价格低廉的对象存储挂载到 Windows 服务器上映射为本地磁盘。

>? 本案例实践适用于 Windows 7 / Windows Server 2012 / 2016 / 2019 / 2022系统。
>

## 操作步骤
### 下载与安装

本案例实践使用到以下三种软件，您可选择安装适用于自己所使用系统的软件版本：
1. 前往 [Github](https://github.com/billziss-gh/winfsp/releases) 下载 Winfsp。
本实践下载的版本为 winfsp-1.12.22301，下载完成后，按步骤默认安装即可。
>?Windows Server 2012 R2 不适用于 Winfsp 1.12.22242版本，可适用于 Winfsp 1.11.22176版本。
2. 前往 [Git 官网](https://gitforwindows.org/) 或者 [Github](https://github.com/git-for-windows/git/releases/) 下载 Git 工具。
本实践下载的版本为 Git-2.38.1-64-bit，下载完成后，按步骤默认安装即可。
3. 前往 [Rclone 官网](https://rclone.org/downloads/) 或者 [Github](https://github.com/rclone/rclone/releases) 下载 Rclone 工具。
本实践下载的版本是 rclone-v1.60.1-windows-amd64，该软件无需安装，下载后，只需解压到任意一个英文目录下即可（如果解压到的路径含有中文将有可能会报错）。本实践案例路径举例为 E:\AutoRclone。

>? Github 下载速度可能比较慢甚至打不开，可自行在其他官方渠道进行下载。
>

### 配置 Rclone

>!以下配置步骤以 rclone-v1.60.1-windows-amd64 版本为例，其他版本的配置过程可能存在一定差异，请注意相应调整。


1. 打开任意文件夹，并在左侧导航目录下找到 **此电脑**，单击右键选择 **属性 > 高级系统设置 > 环境变量 > 系统变量 > Path**，单击**新建**。
2. 在弹出的窗口中，填写 Rclone 解压后的路径（E:\AutoRclone），单击 **确定**。
3. 打开 Windows Powershell，输入 `rclone --version` 命令，按 **Enter**，查看 Rclone 是否成功安装。
4. 确认 Rclone 安装成功后，在 Windows Powershell 中，输入 `rclone config` 命令，按 **Enter**。
5. 在 Windows Powershell 中，输入 **n** ，按 **Enter**，新建一个 New remote。
6. 在 Windows Powershell 中，输入该磁盘的名称，例如 myCOS，按 **Enter**。
7.  在显示的选项中，选择包含 “Tencent COS” 的选项，即输入 **5**，按 **Enter**。
![](https://qcloudimg.tencent-cloud.cn/raw/edd4b224879b2c854c9a32167d3f2aaa.png)
8. 在显示的选项中，选择包含 “TencentCOS” 的选项，输入 **21**，按 **Enter**。
![](https://qcloudimg.tencent-cloud.cn/raw/c7ada8335827fff90078628f05927141.png)
9. 执行到 `env_auth>` 时，按 Enter。
10. 执行到 `access_key_id>` 时，输入腾讯云 COS 的访问密钥 SecretId，按 **Enter**。
>? 此处建议使用子账号权限，可前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 查看自己的 SecretId 和 SecretKey。
>
11. 执行到 `secret_access_key>` 时，输入腾讯云 COS 的访问密钥 SecretKey，按 **Enter**。
12. 根据显示的腾讯云各地域的网关地址，查看存储桶的所属地域，选择对应的地域。
本实践以广州为例，选择 `cos.ap-guangzhou.myqcloud.com`，输入**4**，按 **Enter**。
13. 在显示的腾讯云 COS 的权限类型中，根据实际需求选择 default、public-read 等。此处选择的权限类型为对象权限类型，仅针对新上传的文件有效。本实践以 default 为例，输入**1**，按 **Enter**。
![](https://qcloudimg.tencent-cloud.cn/raw/7756d7599713939368c6bb42cd075d07.png)
15. 在显示的腾讯云对象存储的存储类型中，您可根据实际需求选择以何种存储类型将文件上传到 COS。本实践以 Default 为例，输入**1**，按 **Enter**。
![](https://qcloudimg.tencent-cloud.cn/raw/48e7f6c7d65d13d9fdde690e819bad6c.png)
 - Default 表示默认
 - Standard storage class 表示标准存储（STANDARD）
 - Archive storage mode 表示归档存储（ARCHIVE）
 - Infrequent access storage mode 表示低频存储（STANDARD_IA）
>?如需设置智能分层存储或者深度归档存储类型，请采用 **修改配置文件** 的方式，在配置文件中，将 storage_class 的值设置为 INTELLIGENT_TIERING 或 DEEP_ARCHIVE 即可。关于存储类型的更多介绍，请参见 [存储类型概述](https://cloud.tencent.com/document/product/436/33417)。
>
15. 执行到 `Edit advanced config? (y/n)` 时，按 **Enter**。
16. 确认信息无误后，按 **Enter**。
17. 输入 **q**，完成配置。
![](https://qcloudimg.tencent-cloud.cn/raw/9cd97c7d75b1b9cfd42a244c03d00fff.png)

### 修改配置文件

以上步骤配置完成后，将会生成一个名称为 rclone.conf 的配置文件，一般位于 `C:\Users\用户名\AppData\Roaming\rclone` 文件夹下。如果您想要修改 rclone 的配置，可直接对其进行修改。如若未找到该配置文件，可在命令窗口执行 `rclone config file` 命令查看其配置文件。


### 挂载 COS 为本地磁盘

1. 打开已安装的 Git Bash，并输入执行命令。此处提供了两种使用场景（二选一），您可根据实际需求选择其中一种。
<ul>
<li>如果映射为局域网共享驱动器（推荐），则执行命令如下：
<pre>
<code class="language-plaintext">rclone mount myCOS:/ Y: --fuse-flag --VolumePrefix=\server\share --cache-dir E:\temp --vfs-cache-mode writes &amp;</code>
</pre>
</li>
<li>如果映射为本地磁盘，则执行命令如下：
<pre>
<code class="language-plaintext">rclone mount myCOS:/ Y: --cache-dir E:\temp --vfs-cache-mode writes &</code>
</pre>
	<ul>
		<li>myCOS：替换为用户自定义的磁盘名称。</li>
		<li>Y：替换为您想要挂载后，硬盘的盘符名称即可，请不要与本地的 C、D、E 盘等重复。</li>
		<li>E:\temp 为本地缓存目录，可自行设置。注意：需确保用户拥有目录权限。</li>
	</ul>
</li>
</ul>
当出现提示 “The service rclone has been started” 则说明挂载成功。
2. 输入 **exit**，退出终端。
3. 在本地计算机的**我的电脑**中，即可找到一个名为 myCOS(Y:) 的磁盘。
打开该磁盘，即可查看包含您整个广州地域的所有存储桶名称。此时，您可以进行上传、下载、新建和删除等本地磁盘的常用操作。
>!
> - 在操作当中如遇报错，请在 git bash 软件中查看详细报错信息。
> - 在挂载磁盘中，若对存储桶进行删除操作，无论存储桶是否存在文件，都将会被删除，请谨慎操作。
> - 若您对挂载磁盘中的存储桶名称进行更改，会导致 COS 存储桶名称发生改变，请谨慎操作。
> 


### 设置开机自启动挂载硬盘

由于如上操作在电脑重启后，映射的磁盘将会消失，需要再次手工操作。因此，我们可以设置自启动装置，让服务器每次重启后都自动挂载磁盘。

1. 在 Rclone 安装目录 E:\AutoRclone 下，分别新建 startup_rclone.vbs 和 startup_rclone.bat 文件。
>?Powershell 创建文本文件时需要注意编码，否则生成的.bat、 .vbs 等文本文件无法执行。
2. 在 startup_rclone.bat 中，写入如下挂载命令：
 - 如果映射为局域网共享驱动器，输入如下命令：
```plaintext
rclone mount myCOS:/ Y: --fuse-flag --VolumePrefix=\server\share --cache-dir E:\temp --vfs-cache-mode writes &
```
 - 如果映射为本地磁盘，输入如下命令：
```
rclone mount myCOS:/ Y: --cache-dir E:\temp --vfs-cache-mode writes &
```
3. 在 startup_rclone.vbs 中，写入如下代码：
```plaintext
CreateObject("WScript.Shell").Run "cmd /c E:\AutoRclone\startup_rclone.bat",0
```
>! 请将代码中的路径修改为您实际的路径。
>
4. 将 startup_rclone.vbs 文件剪切到 %USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup 文件夹下。
5. 重启服务器。
>?自动挂载配置后并重启服务器，通常情况下需要等待十几秒才能看到挂载成功。



## 相关操作

您也可以通过使用第三方商业收费工具，将 COS 挂载到 Windows 服务器上映射为本地磁盘。如下操作以 TntDrive 工具为例。
1. 下载和安装 TntDrive。
2. 打开 TntDrive，单击 **Account > Add New Account**，创建一个用户账号。
![](https://main.qcloudimg.com/raw/90b4a262b11b6933f48b4922cad4fdc4.png)
主要参数信息如下：
 - Account Name：自定义账号名称。
 - Account Type：由于 COS 兼容 S3，因此该处可选择 **Amazon S3 Compatible Storage**。
 - REST Endpoint：填写存储桶所在的地域，例如存储桶位于广州地域，则填 cos.ap-guangzhou.myqcloud.com。
 - Access Key ID：填写 SecretId。可在 [API 密钥管理](https://console.cloud.tencent.com/capi) 页面中创建和获取。
 - Secret Access Key：填写 SecretKey。
3. 单击 **Add new account**。
4. 在 TntDrive 界面，单击 **Add New Mapped Drives**，创建一个 Mapped Drives。
![](https://main.qcloudimg.com/raw/fa09500f96ba8e5c8144d39cd5471991.png)
主要参数信息如下：
 - Amazon S3 Bucket：输入存储桶路径，或选择存储桶名称。可单击右侧按钮选择存储桶。该处展示的是步骤2设置的广州地域下的存储桶。（一个存储桶独立映射为一个磁盘）。
 - Mapped drives letter：设置磁盘的盘符名称，请不要与本地的 C、D、E 盘等重复。
5. 确认以上信息单击 **Add new drive**。
6. 在本地计算机的 **我的电脑** 中，即可找到该磁盘。如果想把所有的存储桶都映射到 Windows 服务器中，请重复以上步骤。


## 结语

当然，COS 不仅提供以上应用和服务，还提供多款热门开源应用，并集成腾讯云 COS 插件，欢迎点击 “[此处](https://cloud.tencent.com/act/pro/Ecological-aggregation?from=18406)” 一键启动，立即使用！

