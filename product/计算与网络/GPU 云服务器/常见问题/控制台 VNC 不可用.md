## 现象描述
通过 [使用 VNC 登录 Windows 实例](https://cloud.tencent.com/document/product/213/35704) 或 [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701) 在系统登录界面无法显示登陆提示信息，**黑屏**或**仅显示 Windows Logo**。如下图所示：

![](https://main.qcloudimg.com/raw/b43e93adeb2a69668af877df410ac8c5.jpg)

## 可能原因
1. GPU 实例安装了图形驱动，控制台 VNC 通过访问 QEMU 模拟的 VGA 设备来获取操作系统的 Framebuffer，从而实现访问操作系统的能力，安装 GPU 图形驱动后，系统 Framebuffer 不再交由 VGA 处理，控制台 VNC 失去访问操作系统的能力。
2. 由于其他原因导致操作系统启动失败，例如安装了和系统冲突的第三方软件等。

## 解决方式
1. GPU 实例安装图形驱动后，如果还是需要通过 VNC 方式访问系统，需要在操作系统内手工安装部署 VNC Server，用户通过本地 VNC Client 访问来实现。
2. 分析排查可能导致系统启动失败的软件冲突方面的原因，重装系统。
