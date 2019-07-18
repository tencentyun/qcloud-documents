## 操作场景

本文档以 Windows Server 2012 R2 64位 操作系统为例，指导您在 Windows 操作系统上安装 Cloudbase-Init。

<span id="PreparationSoftware"></span>
## 准备软件
安装 Cloudbase-Init 需准备以下软件：

| 软件名称 | 获取路径 | 说明 |
|---------|---------|---------|
| CloudbaseInitSetup_X_X_XX_xXX.msi | 请根据实际使用的操作系统位数，下载对应的 Cloudbase-Init 安装包：<ul style="margin: 0;"><li>稳定版本：推荐使用该版本安装包<ul style="margin: 0;"><li>Windows 64位 操作系统：[点此获取](https://www.cloudbase.it/downloads/CloudbaseInitSetup_Stable_x64.msi)</li><li>Windows 32位 操作系统：[点此获取](https://www.cloudbase.it/downloads/CloudbaseInitSetup_Stable_x86.msi)</li></ul></li><li>Beta 版本</li></ul>更多详情请参见 [Cloudbase-Init 官网](http://www.cloudbase.it/cloud-init-for-windows-instances/)。 | 用于安装 Cloudbase-Init。  |
| TencentCloudRun.ps1 | [点此获取](http://cloudinit-1251783334.cosgz.myqcloud.com/TencentCloudRun.ps1) | - |
| localscripts.py | [点此获取](http://cloudinit-1251783334.file.myqcloud.com/localscripts.py) | 用于保证 Cloudbase-Init 可以正常启动。 |

## 操作步骤

### 安装 Cloudbase-Init

1. 在操作系统界面，双击打开 Cloudbase-Init 安装包。
2. 在弹出的安全警告提示框中，单击【运行】，进入 Cloudbase-Init 安装界面。如下图所示：
![](https://main.qcloudimg.com/raw/bdeb8ff4370dc6da38da6749154e449f.png)
3. 单击【Next】。
4. 勾选【I accept the terms in the License Agreement】，连续单击2次【Next】。
5. 在 “Configuration options” 界面，将 “**Serial port for logging**” 设置为 “**COM1**”，单击【Next】。如下图所示：
![](https://main.qcloudimg.com/raw/a41580e9b21e4550245b661b44682937.png)
6. 单击【Install】，安装 Cloudbase-Init。
7. 待 Cloudbase-Init 完成安装后，单击【Finish】，关闭 Cloudbase-Init 安装界面。如下图所示：
>! 关闭 Cloudbase-Init 安装界面时，请勿勾选任何复选框，不要运行 Sysprep。
>
![](https://main.qcloudimg.com/raw/d2d6c30def7812af9d7e484f5e8ccaa9.png)

### 修改 cloudbase-init 配置文件 

1. 打开 `cloudbase-init.conf` 配置文件。
`cloudbase-init.conf` 配置文件的默认路径为：`C:\Program Files\Cloudbase Solutions\Cloudbase-Init\conf` 
2. 将 `cloudbase-init.conf` 配置文件替换为以下内容：
```
[DEFAULT]
username=Administrator
groups=Administrators
inject_user_password=true
config_drive_raw_hhd=true
config_drive_cdrom=true
config_drive_vfat=true
bsdtar_path=C:\Program Files\Cloudbase Solutions\Cloudbase-Init\bin\bsdtar.exe
mtools_path=C:\Program Files\Cloudbase Solutions\Cloudbase-Init\bin\
metadata_services=cloudbaseinit.metadata.services.configdrive.ConfigDriveService
plugins=cloudbaseinit.plugins.windows.extendvolumes.ExtendVolumesPlugin,cloudbaseinit.plugins.common.networkconfig.NetworkConfigPlugin,cloudbaseinit.plugins.common.sethostname.SetHostNamePlugin,cloudbaseinit.plugins.common.setuserpassword.SetUserPasswordPlugin,cloudbaseinit.plugins.common.localscripts.LocalScriptsPlugin,cloudbaseinit.plugins.common.userdata.UserDataPlugin
verbose=true
debug=true
logdir=C:\Program Files\Cloudbase Solutions\Cloudbase-Init\log\
logfile=cloudbase-init.log
default_log_levels=comtypes=INFO,suds=INFO,iso8601=WARN,requests=WARN
logging_serial_port_settings=COM1,115200,N,8
mtu_use_dhcp_config=true
ntp_use_dhcp_config=true
first_logon_behaviour=no
netbios_host_name_compatibility=false
allow_reboot=false
activate_windows=true
kms_host="kms.tencentyun.com"
local_scripts_path=C:\Program Files\Cloudbase Solutions\Cloudbase-Init\LocalScripts\
C:\powershell
PS C:\Set-ExecutionPolicy Unrestricted
```
3. 将 `TencentCloudRun.ps1` 脚本拷贝到 `C:\Program Files\Cloudbase Solutions\Cloudbase-Init\LocalScripts` 路径下。
4. 将 `C:\Program Files\Cloudbase Solutions\Cloudbase-Init\Python\Lib\site-packages\cloudbaseinit\plugins\common` 路径下的 `localscripts.py` 替换为 [准备软件](#PreparationSoftware) 中的  `localscripts.py` 文件。
