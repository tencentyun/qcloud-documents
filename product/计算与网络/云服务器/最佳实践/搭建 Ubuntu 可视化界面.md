## 操作场景
VNC（Virtual Network Console）是虚拟网络控制台的缩写。它是一款优秀的远程控制工具软件，由著名的 AT&T 的欧洲研究实验室开发的。VNC 是基于 UNIX 和 Linux 操作系统的开源软件，远程控制能力强大，高效实用，其性能可以和 Windows 和 MAC 中的任何远程控制软件媲美。本文档指导您如何在 Ubuntu 操作系统的云服务器中搭建可视化界面。

## 示例软件版本
本文搭建 Ubuntu 可视化界面的软件组成版本及说明如下：
Linux：Linux 操作系统，本文以 Ubuntu Server 16.04.1 LTS 64位为例。

## 前提条件

已购买操作系统为 Ubuntu 的 Linux 云服务器。如果您还未购买云服务器，请参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。

## 操作步骤

1. [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。
2. 执行以下命令，将当前用户切换至 root 用户。
```
sudo su root
```
3. 执行以下命令，更新和获取最新的软件及版本信息。
```
apt-get update
```
4. 执行以下命令，安装 VNC。
```
apt-get install vnc4server
```
5. <span id="step05"></span>执行以下命令，启动 VNC 服务，并设置 VNC 的密码。
```
vncserver
```
返回类似如下结果，表示 VNC 启动成功。
![](https://main.qcloudimg.com/raw/adad6ffbb0b1b722d1e429133060134b.png)
6. 执行以下命令，安装 X-windows 的基础。
```
sudo apt-get install x-window-system-core
```
7. 执行以下命令，安装登录管理器。
```
sudo apt-get install gdm
```
8. 执行以下命令，安装 Ubuntu 的桌面。
```
sudo apt-get install ubuntu-desktop
```
安装过程中，`Default display manager:` 选择 “gdm3”。
9. 执行以下命令，安装 Gnome 相关配套软件。
```
sudo apt-get install gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal
```
10. 执行以下命令，打开 VNC 配置文件。
```
vi ~/.vnc/xstartup
```
11. 按 **i** 切换至编辑模式，并将配置文件修改为如下内容。
```
#!/bin/sh
# Uncomment the following two lines for normal desktop:
export XKL_XMODMAP_DISABLE=1
 unset SESSION_MANAGER
# exec /etc/X11/xinit/xinitrc
unset DBUS_SESSION_BUS_ADDRESS
gnome-panel &
gnome-settings-daemon &
metacity &
nautilus &
gnome-terminal &
```
12. 按 **Esc**，输入 **:wq**，保存文件并返回。
13. 执行以下命令，重启桌面进程。
```
vncserver -kill :1 #杀掉原桌面进程，输入命令（其中的:1是桌面号）
```
```
vncserver :1 #生成新的会话
```
14. [点此](https://www.realvnc.com/en/connect/download/viewer/) 前往 VNC Viewer 官网，并根据本地计算机的操作系统类型，下载对应的版本及安装。
15. 在 VNC Viewer 软件中，输入 `云服务器的 IP 地址:1`，按 **Enter**。
![](https://main.qcloudimg.com/raw/df25e2085e9d27d53b1827ccf98a3618.png)
16. 在弹出的提示框中，单击【Continue】。
17. 输入 [步骤5](#step05) 设置的 VNC 的密码，单击【OK】。









