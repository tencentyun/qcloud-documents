High-performance power management options need to be set on Windows Server to enable soft-shutdown of virtual machine. Otherwise, the virtual machine only can be shut down by console in a hard-shutdown manner. Take Windows 2012 as an example, the power management is set as follows:

> NOTE: You do not need to restart the computer to change power management.

1) Download power change and setup tools of Tencent Cloud to execute in the console (private network address: http: //mirrors.tencentyun.com/install/windows/power-set-win.bat,
save to C:\Later, then execute it in the console).

After execution, use powercfg -L to view the current power management scheme.

2) In "Control Panel" - "System and Security" - "Power Options", change the idle time limit and turn-off time of display and hard drive.
