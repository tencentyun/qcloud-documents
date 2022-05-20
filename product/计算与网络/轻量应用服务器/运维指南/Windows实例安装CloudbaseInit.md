## 操作场景
本文使用的轻量应用服务器以 Windows Server 2012 R2 中文版操作系统为例，指导您在 Windows 实例上安装 Cloudbase-Init。


## 准备软件[](id:PreparationSoftware)
安装 Cloudbase-Init 需准备以下软件：

| 软件名称 | 获取路径 | 说明 |
|---------|---------|---------|
| CloudbaseInitSetup_X_X_XX_xXX.msi | 请根据实际使用的操作系统位数，下载对应的 Cloudbase-Init 安装包：<ul style="margin: 0;"><li>稳定版本：推荐使用该版本安装包，Windows 64位 操作系统请 [点此获取](https://www.cloudbase.it/downloads/CloudbaseInitSetup_Stable_x64.msi)。</li><li>Beta 版本：详情请参见 [Cloudbase-Init 官网](http://www.cloudbase.it/cloud-init-for-windows-instances/)。</li></ul> | 用于安装 Cloudbase-Init。  |
| TencentCloudRun.ps1 | [点此获取](https://cloudinit-1251783334.cosgz.myqcloud.com/TencentCloudRun.ps1) | - |
| localscripts.py | [点此获取](https://cloudinit-1251783334.file.myqcloud.com/localscripts.py) | 用于保证 Cloudbase-Init 可以正常启动。 |

## 操作步骤

### 安装 Cloudbase-Init
1. 参考 [使用 VNC 方式登录 Windows 实例](https://cloud.tencent.com/document/product/1207/44656)，登录轻量应用服务器。
2. 在操作系统界面，双击打开 Cloudbase-Init 安装包。
3. 在弹出的安全警告提示框中，单击**运行**，进入 Cloudbase-Init 安装界面。如下图所示：
![](https://main.qcloudimg.com/raw/3249309f71fccaf73feeaa5bb55301c3.png)
4. 单击 **Next**。
4. 勾选 “I accept the terms in the License Agreement”，连续单击2次 **Next**。
5. 在 “Configuration options” 界面，将 “**Serial port for logging**” 设置为 “**COM1**”，勾选 “Run Cloudbase-Init service as LocalSystem”，并单击 **Next**。如下图所示：
![](https://main.qcloudimg.com/raw/a772c35958cdf3be511dab58f730e7be.png)
6. 单击 **Install**，安装 Cloudbase-Init。
7. 待 Cloudbase-Init 完成安装后，单击 **Finish**，关闭 Cloudbase-Init 安装界面。如下图所示：
<dx-alert infotype="notice" title="">
关闭 Cloudbase-Init 安装界面时，请勿勾选任何复选框，不要运行 Sysprep。
</dx-alert>
<img src="https://main.qcloudimg.com/raw/9cb4414c157c535e0f102f6088187a29.png"/>

### 修改 cloudbase-init 配置文件 

1. 打开 `cloudbase-init.conf` 配置文件。
`cloudbase-init.conf` 配置文件的默认路径为：`C:\Program Files\Cloudbase Solutions\Cloudbase-Init\conf` 
2. 将 `cloudbase-init.conf` 配置文件替换为以下内容：
```shellsession
[DEFAULT]
username=Administrator
groups=Administrators
inject_user_password=true
config_drive_raw_hhd=true
config_drive_cdrom=true
config_drive_vfat=true
bsdtar_path=C:\Program Files\Cloudbase Solutions\Cloudbase-Init\bin\bsdtar.exe
mtools_path=C:\Program Files\Cloudbase Solutions\Cloudbase-Init\bin\

san_policy=OnlineAll

metadata_services=cloudbaseinit.metadata.services.configdrive.ConfigDriveService,cloudbaseinit.metadata.services.ec2service.EC2Service
#,cloudbaseinit.metadata.services.httpservice.HttpService
#,cloudbaseinit.metadata.services.maasservice.MaaSHttpService

metadata_base_url=http://169.254.0.23/
ec2_metadata_base_url=http://169.254.0.23/

retry_count=2
retry_count_interval=5

plugins=cloudbaseinit.plugins.windows.extendvolumes.ExtendVolumesPlugin,cloudbaseinit.plugins.common.networkconfig.NetworkConfigPlugin,cloudbaseinit.plugins.common.sethostname.SetHostNamePlugin,cloudbaseinit.plugins.common.setuserpassword.SetUserPasswordPlugin,cloudbaseinit.plugins.common.localscripts.LocalScriptsPlugin,cloudbaseinit.plugins.common.userdata.UserDataPlugin
verbose=true
debug=true
logdir=C:\Program Files\Cloudbase Solutions\Cloudbase-Init\log\
logfile=cloudbase-init.log
default_log_levels=comtypes=INFO,suds=INFO,iso8601=WARN,requests=WARN
#logging_serial_port_settings=COM1,115200,N,8
mtu_use_dhcp_config=true
ntp_use_dhcp_config=true
first_logon_behaviour=no
netbios_host_name_compatibility=false
allow_reboot=true
activate_windows=true
kms_host="kms.tencentyun.com"
local_scripts_path=C:\Program Files\Cloudbase Solutions\Cloudbase-Init\LocalScripts\

C:\powershell
PS C:\Set-ExecutionPolicy Unrestricted

volumes_to_extend=1,2
```
3. 将 `TencentCloudRun.ps1` 脚本拷贝到 `C:\Program Files\Cloudbase Solutions\Cloudbase-Init\LocalScripts` 路径下。
4. 右键单击 `TencentCloudRun.ps1` 脚本，选择**属性**，并在弹出窗口中查看脚本是否具备可执行权限。如下图所示：
![](https://main.qcloudimg.com/raw/3a3a31fc4d0dbd58cacb9211f7a97e79.png)
 - 如存在 Unblock 选项，则需勾选 Unblock，并单击 **OK** 退出。 
 - 如不存在 Unblock 选项，则请跳过本步骤。
5. 将 `C:\Program Files\Cloudbase Solutions\Cloudbase-Init\Python\Lib\site-packages\cloudbaseinit\plugins\common` 路径下的 `localscripts.py` 替换为 [准备软件](#PreparationSoftware) 中的  `localscripts.py` 文件。

## 后续操作
您可参考 [如何确认 Windows 实例内部的 Cloudbase-Init 服务是否正常运行？](https://cloud.tencent.com/document/product/213/19670#.E5.A6.82.E4.BD.95.E7.A1.AE.E8.AE.A4-windows-.E5.AE.9E.E4.BE.8B.E5.86.85.E9.83.A8.E7.9A.84-cloudbase-init-.E6.9C.8D.E5.8A.A1.E6.98.AF.E5.90.A6.E6.AD.A3.E5.B8.B8.E8.BF.90.E8.A1.8C.EF.BC.9F)，检查 Cloudbase-Init 是否正常运行。
