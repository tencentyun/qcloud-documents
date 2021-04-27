在 Windows 系统上操作腾讯云对象存储（Cloud Object Storage，COS），目前主要的实现方式还是通过 API、COSBrowser、COSCMD 工具。

而对于喜欢使用 Windows 服务器的用户，使用 COSBrowser 工具大多只能当做网盘，对服务器上的直接使用程序或者操作并不友好。本文将介绍如何使存储价格低廉的对象存储挂载到 Windows 服务器上映射为本地磁盘。

>? 本案例实践适用操作系统：Windows Server 2019 数据中心版 64位 中文版。
>

## 下载与安装

提供了如下安装方法，您可根据自己所使用的系统进行选择：
- 前往 [Github](https://github.com/billziss-gh/winfsp/releases) 下载 Winfsp。
待下载完成后，按步骤默认安装即可。
- 前往 [Git 官网](https://gitforwindows.org/) 或者 [Github](https://github.com/git-for-windows/git/releases/) 下载 Git 工具。
本实践下载的版本为 Git-2.31.1-64-bit.exe，下载完成后，按步骤默认安装即可。
- 前往 [Rclone 官网](https://rclone.org/downloads/) 或者 [Github](https://github.com/rclone/rclone/releases) 下载 Rclone 工具。
本实践下载的版本是 rclone-v1.55.0-windows-amd64.zip，该软件无需安装，下载后，只需解压到任一一个英文目录下即可（如果解压到的路径含有中文将有可能会报错）。本实践案例路径举例为 E:\AutoRclone。

>? Github 下载速度可能比较慢甚至打不开，可自行在其他官方渠道进行下载。
>

## 配置 Rclone

1. 打开任意文件夹，并在左侧导航目录下找到【此电脑】，单击右键选择【属性】>【高级系统设置】>【环境变量】>【系统变量】>【Path】，单击【新建】。
2. 在弹出的窗口中，填写 Rclone 解压后的路径（E:\AutoRclone），单击【确定】。
3. 打开 Windows Powershell，输入`rclone --version` 命令，按 **Enter**，查看 Rclone 是否成功安装。
4. 确认 Rclone 安装成功后，在 Windows Powershell 中，输入 `rclone config` 命令，按 **Enter**。
5. 在 Windows Powershell 中，输入 **n** ，按 **Enter**，新建一个 New remote。
6. 在 Windows Powershell 中，输入该磁盘的名称，例如 myCOS，按 **Enter**。
7.  在显示的选项中，选择包含腾讯云的选项，即输入**4**，按 **Enter**。
8. 在显示的选项中，选择包含腾讯云 COS 的选项，输入**11**，按 **Enter**。
9. 执行到 `env_auth>` 时，按 Enter。
10. 执行到 `access_key_id>` 时，输入腾讯云 COS 的访问密钥 SecretId，按 **Enter**。
>?此处建议使用子账号权限，可前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 查看自己的 SecretId 和 SecretKey。
>
11. 执行到 `secret_access_key>` 时，输入腾讯云 COS 的访问密钥 SecretKey，按 **Enter**。
12. 根据显示的腾讯云各地域的网关地址，查看存储桶的所属地域，选择对应的地域。
本实践以广州为例，选择 `cos.ap-guangzhou.myqcloud.com`，输入**4**，按 **Enter**。
13. 在显示的腾讯云 COS 的权限类型中，根据实际需求选择 private 或者 public-read。
本实践以 public-read 为例，输入**2**，按 **Enter**。
14. 在显示的腾讯云对象存储的存储类型，根据实际需求选择。
默认为 Default，Standard storage class 表示标准存储，Archive storage mode 表示归档存储，Infrequent access storage mode 表示低频存储（Standard_IA）。
 本实践以 Default 为例，输入**1**，按 **Enter**。
15. 执行到 `Edit advanced config? (y/n)` 时，按 **Enter**。
16. 确认信息无误后，按 **Enter**。
17. 输入**q**，完成配置。

配置完成后，在 `C:\Users\用户名\.config\rclone` 文件夹下，即可看到一个名称为 rclone.conf 的文件，该文件就是 rclone 的配置文件。如果您想要修改 rclone 的配置，可直接对其进行修改。


## 挂载 COS 为本地磁盘

1. 打开已安装的 Git，并在命令行工具中输入如下命令：
```plaintext
rclone mount myCOS:/ Y: --cache-dir E:\temp --vfs-cache-mode writes &
```
 - myCOS：替换为用户自定义的名称。
 - Y：替换为您想要挂载后，硬盘的盘符名称即可，请不要与本地的 C、D、E 盘等重复。
 - E:\temp 为本地缓存目录，可自行设置。

 当出现提示 “The service rclone has been started” 则说明挂载成功。
2. 输入 **exit**，退出终端。
3. 在本地计算机的【我的电脑】中，即可找到一个名为 myCOS(Y:) 的磁盘。
打开该磁盘，即可查看包含您整个广州地域的所有存储桶名称。此时，您可以进行上传、下载、新建和删除等本地磁盘的常用操作。

## 设置开机自启动挂载硬盘

由于如上操作在电脑重启后，映射的磁盘将会消失，需要再次手工操作。因此，我们可以设置自启动装置，让服务器每次重启后都自动挂载磁盘。

1. 在 Rclone 安装目录 E:\AutoRclone 下，分别新建 startup_rclone.vbs 和 startup_rclone.bat 文件。
2. 在 startup_rclone.bat 中，写入如下挂载命令：
```plaintext
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
