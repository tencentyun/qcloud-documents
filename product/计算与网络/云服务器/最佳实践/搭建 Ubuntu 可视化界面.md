## 操作场景
VNC（Virtual Network Console）是虚拟网络控制台的缩写。它是一款优秀的远程控制工具软件，由著名的 AT&T 的欧洲研究实验室开发的。VNC 是基于 UNIX 和 Linux 操作系统的开源软件，远程控制能力强大，高效实用，其性能可以和 Windows 和 MAC 中的任何远程控制软件媲美。本文档指导您如何在 Ubuntu 操作系统的云服务器中搭建可视化界面。

## 前提条件
已购买操作系统为 Ubuntu 的 Linux 云服务器。如果您还未购买云服务器，请参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。


## 操作步骤


### 配置实例安全组

VNC 服务使用 TCP 协议，默认使用5901端口。则需在实例已绑定的安全组中放通5901端口，即在“入站规则”中添加放通协议端口为 TCP:5901 的规则，具体操作请参见 [添加安全组规则](https://cloud.tencent.com/document/product/213/39740)。


### 安装软件包
1. [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。
2. 执行以下命令，将当前用户切换至 root 用户。
```
sudo -i
```
3. 执行以下命令，更新和获取最新的软件及版本信息。
```
apt-get update
```
4. 执行以下命令，安装桌面环境所需软件包。包括系统面板、窗口管理器、文件浏览器、终端等桌面应用程序。
```bash
apt install gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal ubuntu-desktop
```



### 配置 VNC

1. 按照实际情况选择执行以下命令，安装 VNC。
<dx-tabs>
::: Ubuntu 18.04
```
apt-get install vnc4server
```
:::
::: Ubuntu 20.04
```
apt-get install tightvncserver
```
:::
</dx-tabs>
2. [](id:step02)执行以下命令，启动 VNC 服务，并设置 VNC 的密码。
```
vncserver
```
返回类似如下结果，表示 VNC 启动成功。
![](https://main.qcloudimg.com/raw/adad6ffbb0b1b722d1e429133060134b.png)
3. 执行以下命令，打开 VNC 配置文件。
```
vi ~/.vnc/xstartup
```
4. 按 **i** 切换至编辑模式，并将配置文件修改为如下内容。
```
#!/bin/sh
export XKL_XMODMAP_DISABLE=1
export XDG_CURRENT_DESKTOP="GNOME-Flashback:GNOME"
export XDG_MENU_PREFIX="gnome-flashback-"
gnome-session --session=gnome-flashback-metacity --disable-acceleration-check &
```
5. 按 **Esc**，输入 **:wq**，保存文件并返回。
6. 执行以下命令，重启桌面进程。
```
vncserver -kill :1 #杀掉原桌面进程，输入命令（其中的:1是桌面号）
```
```
vncserver -geometry 1920x1080 :1 #生成新的会话
```
7. [点此](https://www.realvnc.com/en/connect/download/viewer/) 前往 VNC Viewer 官网，并根据本地计算机的操作系统类型，下载对应的版本及安装。
8. 在 VNC Viewer 软件中，输入 `云服务器的 IP 地址:1`，按 **Enter**。
![](https://main.qcloudimg.com/raw/df25e2085e9d27d53b1827ccf98a3618.png)
9. 在弹出的提示框中，单击 **Continue**。
10. 输入 [步骤2](#step02) 设置的 VNC 的密码，单击 **OK**，即可登录实例并使用图形化界面。



