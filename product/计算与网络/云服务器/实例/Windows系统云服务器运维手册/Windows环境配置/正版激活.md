腾讯云服务器使用KMS方式对Windows服务器进行授权，目前只有windows2008和windows2012需要做这种方式的授权。

## 1. 自动激活工具
腾讯云给QCloud的windows激活封装了一个脚本，简化了手工激活的步骤。请在Windows云服务器上访问以下地址下载：http://mirrors.tencentyun.com/install/windows/activate-win.bat ，并在下载后执行该脚本。


## 2. 手工运行激活
1) 点击【开始】-【运行】，输入cmd.exe，打开控制台窗口。

2) 依次输入以下命令：

```
cscript /nologo %windir%/system32/slmgr.vbs -skms kms.tencentyun.com:1688
cscript /nologo %windir%/system32/slmgr.vbs -ato
```


注1：
在某些系统上，如果系统时钟存在问题，手工激活的时候会出现错误，这个时候需要同步系统时钟。同步时钟的方法如下，在控制台窗口输入以下命令：

```
w32tm /config /syncfromflags:manual /manualpeerlist:"ntpupdate.tencentyun.com"
w32tm /resync
```

注2：
Windows上的SPP Notification Service，是用来执行激活相关的服务，需要保证正常运行，如下图
![](//mccdn.qcloud.com/img56b1caa1eec42.png)

某些优化软件可能会禁用修改服务相关执行程序的执行权限，例如sppsvc.exe进程的执行权限被修改，会导致服务运行不正常：
![](//mccdn.qcloud.com/img56b1caaf5ff0a.png)

在尝试激活Windows之前，请确保Windows上这个服务和其他基本功能正常。