## 现象描述
通过 [使用 VNC 登录 Windows 实例](https://cloud.tencent.com/document/product/213/35704) 或 [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701) 登录实例时，登录界面无法显示登录提示信息，例如**黑屏**或**仅显示 Windows Logo**。如下图所示：
![](https://main.qcloudimg.com/raw/c443b5f91207367aeb5f976d42a868dd.jpg)

## 可能原因
1. GPU 实例安装了图形驱动。
VNC 方式登录 GPU 实例时，默认访问 QEMU 模拟的 VGA 设备，获取操作系统的 Framebuffer，实现访问操作系统。安装了 GPU 图形驱动之后，Framebuffer 不再交由 VGA 处理，VNC 无法访问操作系统。
2. 由于其他原因导致操作系统启动失败，例如安装了和系统冲突的第三方软件等。

## 解决方式
1. 针对安装图形驱动的 GPU 实例，可在该实例中手动安装 VNC Server，用户即可在本地通过 VNC Client 进行登录。
请自行获取 VNC Server/Client 安装包。
2. 检查已安装的第三方软件，分析其可能导致无法通过 VNC 方式登录实例的原因。
建议卸载该第三方软件，或重装系统。
