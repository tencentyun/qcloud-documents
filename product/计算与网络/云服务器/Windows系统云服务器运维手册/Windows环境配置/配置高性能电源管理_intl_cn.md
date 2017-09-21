Windows Server上需要配置高性能电源管理选项，才能支持虚拟机软关机，否则控制台只能通过硬关机的方式关闭虚拟机。以下配置电源管理的方法以Windows 2012举例：

>注：修改电源管理不需要重启重启计算机。

1) 下载腾讯云电源修改和配置工具，在控制台上执行（内网的地址：http://mirrors.tencentyun.com/install/windows/power-set-win.bat
另存到C:\以后，在控制台执行），如下图:

![](//mccdn.qcloud.com/img56b1bee8a8fbf.png)

执行完以后可使用powercfg -L查看当前电源管理方案。

2) 在【控制面板】-【系统和安全】-【电源选项】修改显示器和硬盘的空闲关闭时间。如图所示：

![](//mccdn.qcloud.com/img56b1bf648d627.png)
