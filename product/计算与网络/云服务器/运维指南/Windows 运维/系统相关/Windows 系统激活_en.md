Tencent CVM uses KMS for granting authorization to Windows server. Currently, only Windows 2008 and Windows 2012 need such authorization.

## 1. Automatic activation tool
Tencent Cloud encapsulates a script for Windows activation on QCloud that simplifies the steps for manual activation. Please visit the following address on Windows CVM for download (http://mirrors.tencentyun.com/install/windows/activate-win.bat), and execute the script after the download.


## 2. Run the activation manually.
1) Click "Start" - "Run", enter cmd.exe to open the console window.

2) Enter the following commands in turn:

```
cscript /nologo %windir%/system32/slmgr.vbs -skms kms.tencentyun.com:1688
cscript /nologo %windir%/system32/slmgr.vbs -ato
```


Note 1:
On some systems, if there is a problem with the system clock, error will occur during manual activation. In this case, you need to synchronize the system clocks. The synchronization between clocks is performed as follows: Enter the following commands in the console window:

```
w32tm /config /syncfromflags:manual /manualpeerlist:"ntpupdate.tencentyun.com"
w32tm / resync
```

Note 2:
SPP Notification Service on Windows is used to perform activation-related services and its normal operation needs to be ensured, as shown below.
![](//mccdn.qcloud.com/img56b1caa1eec42.png)

Some optimization software may disable the change to execute permissions of service-related executables. For example, the change to the execute permission of sppsvc.exe process can cause abnormal operation of service:
![](//mccdn.qcloud.com/img56b1caaf5ff0a.png)

Before you attempt to activate Windows, make sure the service and other basic functions on Windows are in a normal condition.