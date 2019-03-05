## 下载 cloudbase-init 工具安装包

请根据实际使用的操作系统位数，下载对应版本的 cloudbase-init 工具安装包进行安装。具体详情请参见 [Cloudbase-Init 官网](http://www.cloudbase.it/cloud-init-for-windows-instances/)。

Cloudbase-init 分为以下版本：
- 稳定版本：推荐使用该版本安装包进行安装。
获取路径如下：
	- Windows 64位 操作系统：https://www.cloudbase.it/downloads/CloudbaseInitSetup_Stable_x64.msi
	- Windwos 32位 操作系统：https://www.cloudbase.it/downloads/CloudbaseInitSetup_Stable_x86.msi
- Beta 版本

## 安装 cloudbase-init

安装 cloudbase-init 的过程中，请注意以下两点：
- **在 “Configuration options” 窗口中，请按照下图的内容进行配置。即将 “Serial port for logging” 设置为 “COM1”。**
![Alt text](https://main.qcloudimg.com/raw/beaca64e8484ec7e9880703cad400717.png)
- **在安装完成的最后一步时，请勿勾选任何复选框，不运行 Sysprep。如下图所示：**
![Alt text](https://main.qcloudimg.com/raw/aceec91df6a51db2eca775f3350de88c.png)

## 修改 cloudbase-init 配置文件 

1. 打开 cloudbase-init 配置文件（配置文件的路径为：\PATH\TO\Cloudbase Solutions\Cloubase-Init\conf\cloudbase-init.conf）。
2. 将 cloudbase-init 配置文件替换为以下内容：
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
3. 将 [TencentCloudRun.ps1](http://cloudinit-1251783334.cosgz.myqcloud.com/TencentCloudRun.ps1) 脚本拷贝到 C:\Program Files\Cloudbase Solutions\Cloudbase-Init\LocalScripts\ 路径下。
