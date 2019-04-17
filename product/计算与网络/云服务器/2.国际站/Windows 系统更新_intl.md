## 1. Obtain updates via the public network.
Users can install the patch program through the Windows Update service program of the system. The steps are as follows:

Click "Start" - "Control Panel" - "Windows Updates", click "Check for Updates" button. After the check completes, you'll be notified of the availability of several update packages.

Click "Available Updates", then "Choose the Update to Install" pop-up box will appear. Select the update to install, click "Install", then wait until the appearance of the message that the installation is completed.

If you are prompted to restart your system after the update is completed, please restart the CVM.

> Note: When you restart the CVM after the patch is updated, please observe the CVM through VNV. If the message that "Updating...Do not turn off the power" or "Configuration has not been completed" appears, do not perform a hard-shutdown, which can damage your CVM.

## 2. Obtain updates via the private network.
If the CVM cannot be connected to the public network, the user can set it to use patch server of Tencent Cloud private network to install the updates. Windows patch server of Tencent Cloud contains most patch updating programs that are often used on Windows, but does not include hardware driver packages and some seldom-used server update packages.

For some seldom-used services, update patch may not be found on the patch server of Tencent Cloud private network. To address this problem, Tencent Cloud is still making efforts in improving more patch programs.

If you want to use patch server of Tencent Cloud private network, do as follows:

1) After logging in to Windows CVM, download the setup tool wusin.bat at Tencent Cloud private network through IE:
http://mirrors.tencentyun.com/install/windows/wusin.bat

2) Save it to C:\wusin.bat, and open the console to execute.

> NOTE: When this script is directly executed through IE, console window will be closed automatically and you are unable to view the output messages.

If you no longer need to use the Windows patch server of Tencent Cloud private network, you can download the cleanup tool wusout.bat as follows:

1) After logging in to Windows CVM, download cleanup tool wuout.bat through IE:
http://mirrors.tencentyun.com/install/windows/wusout.bat

2) Save it to C:\wusout.bat, and open the console to execute.

> NOTE: When this script is directly executed through IE, console window will be closed automatically and you are unable to view the output messages.
