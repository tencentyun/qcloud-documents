腾讯云云服务器使用 KMS 方式对 Windows 服务器进行授权。

<dx-alert infotype="notice" title="">
- 此文档只针对腾讯云提供的 Windows Server 公共镜像，自定义镜像或外部导入镜像不能采用本文的激活方式。
- Windows Server 2008 和 Windows Server 2012 需要进行此方式的授权，Windows Server 2016 和 Windows Server 2019 公共镜像中默认配置的 KMS 地址（kms.tencentyun.com:1668）是正确的，无需做修改。
</dx-alert>



## 激活前须知
1. 仅 **Windows Server 2008** 中 SPP Notification Service 用来执行激活相关的服务，需要保证正常运行。如下图所示：
![](https://main.qcloudimg.com/raw/f8a8aab467f82898d61d7b67fab86c0b.png)
2. 某些优化软件可能会禁用修改服务相关执行程序的执行权限，例如 sppsvc.exe 进程的执行权限若被修改，会导致服务运行不正常。如下图所示：
![](https://mc.qcloudimg.com/static/img/685fe41ef992f11ba305dfb570cb916c/21.png)
在尝试激活 Windows 云服务器之前，请确保 Windows 上这个服务和其他基本功能正常。
 
## 自动激活
腾讯云为 Windows 服务器的激活封装了一个脚本，简化了手工激活的步骤。请按照以下步骤使用脚本激活：
1. 登录 Windows 云服务器。
2. 下载并运行 [脚本](https://iso-1251783334.cos.ap-guangzhou.myqcloud.com/scripts/activate-win.bat )，即可完成自动激活。


## 手工运行激活

### 注意事项
在某些系统上，如果系统时钟存在问题，手工激活时会出现错误。此时，您需要先同步系统时钟。同步时钟的操作步骤如下：
<dx-alert infotype="explain" title="">
若 Windows 云服务器上的系统时钟正常，请直接进行 [激活步骤](#ActivationStep)。
</dx-alert>

1. 登录 Windows 云服务器。
2. 在操作系统界面，单击**开始** > **运行**，输入 `cmd.exe`，打开控制台窗口。
3. 在控制台窗口依次执行以下命令，同步系统时钟。
```
w32tm /config /syncfromflags:manual /manualpeerlist:"ntpupdate.tencentyun.com"
w32tm /resync
```


### 激活步骤[](id:ActivationStep)

1. 登录 Windows 云服务器。
2. 在操作系统界面，单击**开始** > **运行**，输入 `cmd.exe`，打开控制台窗口。
3. 在控制台窗口依次执行以下命令，即可完成手工运行激活。
```
cscript /nologo %windir%/system32/slmgr.vbs -skms kms.tencentyun.com:1688
cscript /nologo %windir%/system32/slmgr.vbs -ato
```





