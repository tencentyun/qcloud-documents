## 操作场景

本文档以 Windows Server 2012 操作系统为例，指导您更新 Windows 补丁。

## 操作步骤

### 通过公网获取更新
您可以通过系统的 Windows Update 服务程序来安装补丁程序。具体执行步骤如下：
1. 登录 Windows 云服务器。
2. 单击 <img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin: -3px 0px;"></img> > **控制面板** > **Windows 更新**，打开 Windows 更新窗口。
3. 单击**检查更新**，并等待检查完成。
4. 检查完成后，单击 “Windows 更新” 中 **n 个重要更新 可用**或者 **n 个可选更新 可用**。如下图所示：
 ![](https://main.qcloudimg.com/raw/785c4549a6818fda7a04de11fa656cb1.png)
5. 在弹出的 “选择安装的更新” 窗口中，选择需要安装的更新程序，单击**安装**。如下图所示：
 ![](https://main.qcloudimg.com/raw/92e026d618eb85199ddbf5d0e08df1c6.png)
在完成更新后，如果系统提示需要重新启动系统，请及时重启云服务器。
<dx-alert infotype="notice" title="">
完成更新补丁重启云服务器时， 需通过 VNC 方式登录及观察云服务器。如果系统出现 “正在更新，请不要关闭电源” 或者 “配置未完成” 等提示时，请不要执行硬关机操作。硬关机可能会损坏您的云服务器。
</dx-alert>



### 通过内网获取更新
如果云服务器无法连接到公网，您可以通过使用腾讯云内网补丁服务器来安装更新。腾讯云的 Windows 补丁服务器包含了 Windows 上大部分常用的补丁更新程序，但不包含硬件驱动程序包和某些不常用的服务器更新包。一些比较少用的服务在腾讯云的内网补丁服务器上可能搜索不到更新补丁。
腾讯云内网的补丁服务器的使用方法如下：
1. 登录 Windows 云服务器。
2. 通过 IE 浏览器访问和下载腾讯云内网的设置工具（wusin.bat）。
wusin.bat 下载地址为：`http://mirrors.tencentyun.com/install/windows/wusin.bat`
3. 使用管理员命令行工具（CMD）打开 wusin.bat。如下图所示：
<dx-alert infotype="explain" title="">
如果直接通过 IE 执行 wusin.bat 工具，控制台窗口将会自动关闭，无法观察输出信息。
</dx-alert>
例如，将 wusin.bat 设置工具保存到 C: 盘中。
<img src="https://main.qcloudimg.com/raw/8e51c1bb44bffb6c5feccb7c620b8316.png"/>

如果您不再需要使用腾讯云内网 Windows 补丁服务器，还可以下载 wusout.bat 清理工具进行清理。其方法如下：
1. 登录 Windows 云服务器。
2. 通过 IE 浏览器访问和下载腾讯云内网的清理工具（wuout.bat）。
wuout.bat 下载地址为：`http://mirrors.tencentyun.com/install/windows/wusout.bat`
3. 使用管理员命令行工具（CMD）打开 wusout.bat。如下图所示：
<dx-alert infotype="explain" title="">
 如果直接通过 IE 执行 wusout.bat 工具，控制台窗口将会自动关闭，无法观察输出信息。
</dx-alert>
例如，将 wusout.bat 设置工具保存到 C: 盘中。
<img src="https://main.qcloudimg.com/raw/e279243a183b26d066fe6c5e064144a3.png"/>


