## 操作场景
VNC（Virtual Network Console）是虚拟网络控制台的缩写。它是一款优秀的远程控制工具软件，由著名的 AT&T 的欧洲研究实验室开发。VNC 是基于 UNIX 和 Linux 操作系统的开源软件，远程控制能力强大，高效实用，其性能可以和 Windows、MAC 中的任何远程控制软件媲美。本文档指导您如何在 Ubuntu 操作系统的云服务器中搭建可视化界面。

## 前提条件
已购买操作系统为 Ubuntu 的 Linux 云服务器。如果您还未购买云服务器，请参见 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。


## 操作步骤


### 配置实例安全组

VNC 服务使用 TCP 协议，默认使用5901端口，需在实例已绑定的安全组中放通5901端口，即在“入站规则”中添加放通协议端口为 TCP:5901 的规则，具体操作请参见 [添加安全组规则](https://cloud.tencent.com/document/product/213/39740)。


### 安装软件包

<dx-tabs>
::: Ubuntu 18.04
1. [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。
2. 执行以下命令，清空缓存，更新您的软件包列表。
```shellsession
sudo apt clean all && sudo apt update
```
3. 执行以下命令，安装桌面环境所需软件包。包括系统面板、窗口管理器、文件浏览器、终端等桌面应用程序。
```shellsession
sudo apt install gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal ubuntu-desktop
```
4. 执行以下命令，安装 VNC。
```shellsession
apt-get install vnc4server
```
:::
::: Ubuntu 20.04
1. [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。
2. 执行以下命令，清空缓存，更新您的软件包列表。
```shellsession
sudo apt clean all && sudo apt update
```
3. 执行以下命令，安装桌面环境所需软件包。包括系统面板、窗口管理器、文件浏览器、终端等桌面应用程序。
```shellsession
sudo apt install gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal ubuntu-desktop
```
4. 执行以下命令，安装 VNC。
```shellsession
apt-get install tightvncserver
```
:::
::: Ubuntu 22.04
1. [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。
2. 清空缓存，更新您的软件包列表。
```shellsession
sudo apt clean all && sudo apt update
```
3. 安装桌面环境。
```shellsession
sudo apt install xfce4 xfce4-goodies
```
4.执行以下命令，安装 VNC。
```shellsession
sudo apt install tightvncserver
```
:::
</dx-tabs>

### 配置 VNC
<dx-tabs>
::: Ubuntu 18.04
1. [](id:step02)执行以下命令，启动 VNC 服务，并设置 VNC 的密码。
```shellsession
vncserver
```
返回类似如下结果，表示 VNC 启动成功。
![](https://main.qcloudimg.com/raw/adad6ffbb0b1b722d1e429133060134b.png)
2. 执行以下命令，打开 VNC 配置文件。
```shellsession
vi ~/.vnc/xstartup
```
3. 按 **i** 切换至编辑模式，并将配置文件修改为如下内容。
```shellsession
#!/bin/sh
export XKL_XMODMAP_DISABLE=1
export XDG_CURRENT_DESKTOP="GNOME-Flashback:GNOME"
export XDG_MENU_PREFIX="gnome-flashback-"
gnome-session --session=gnome-flashback-metacity --disable-acceleration-check &
```
4. 按 **Esc**，输入 **:wq**，保存文件并返回。
5. 执行以下命令，重启桌面进程。
```shellsession
vncserver -kill :1 #关闭原桌面进程，输入命令（其中的:1是桌面号）
```
```shellsession
vncserver -geometry 1920x1080 :1 #生成新的会话
```
6. [点此](https://www.realvnc.com/en/connect/download/viewer/) 前往 VNC Viewer 官网，并根据本地计算机的操作系统类型，下载对应的版本并安装。
7. 在 VNC Viewer 软件中，输入 `云服务器的 IP 地址:1`，按 **Enter**。
![](https://main.qcloudimg.com/raw/df25e2085e9d27d53b1827ccf98a3618.png)
8. 在弹出的提示框中，单击 **Continue**。
9. 输入 [步骤1](#step02) 设置的 VNC 的密码，单击 **OK**，即可登录实例并使用图形化界面。

:::


::: Ubuntu 20.04
1. [](id:step03)执行以下命令，启动 VNC 服务，并设置 VNC 的密码。
```shellsession
vncserver
```
返回类似如下结果，表示 VNC 启动成功。
![](https://main.qcloudimg.com/raw/adad6ffbb0b1b722d1e429133060134b.png)
2. 执行以下命令，打开 VNC 配置文件。
```shellsession
vi ~/.vnc/xstartup
```
3. 按 **i** 切换至编辑模式，并将配置文件修改为如下内容。
```shellsession
#!/bin/sh
export XKL_XMODMAP_DISABLE=1
export XDG_CURRENT_DESKTOP="GNOME-Flashback:GNOME"
export XDG_MENU_PREFIX="gnome-flashback-"
gnome-session --session=gnome-flashback-metacity --disable-acceleration-check &
```
4. 按 **Esc**，输入 **:wq**，保存文件并返回。
5. 执行以下命令，重启桌面进程。
```shellsession
vncserver -kill :1 #杀掉原桌面进程，输入命令（其中的:1是桌面号）
```
```shellsession
vncserver -geometry 1920x1080 :1 #生成新的会话
```
6. [点此](https://www.realvnc.com/en/connect/download/viewer/) 前往 VNC Viewer 官网，并根据本地计算机的操作系统类型，下载对应的版本并安装。
7. 在 VNC Viewer 软件中，输入 `云服务器的 IP 地址:1`，按 **Enter**。
![](https://main.qcloudimg.com/raw/df25e2085e9d27d53b1827ccf98a3618.png)
8. 在弹出的提示框中，单击 **Continue**。
9. 输入 [步骤1](#step03) 设置的 VNC 的密码，单击 **OK**，即可登录实例并使用图形化界面。

:::

::: Ubuntu 22.04
[](id:g1)
1. 执行以下命令，启动 VNC 服务，并设置 VNC 的密码。
```shellsession
vncserver
```
返回类似如下结果，表示 VNC 启动成功。
![](https://qcloudimg.tencent-cloud.cn/raw/5fb63d9cc28d3a0cebd5def424051e7a.png)
2. 前往 [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) 官网，并根据本地计算机的操作系统类型，下载对应的版本并安装。
3. 在 VNC Viewer 软件中，输入 `云服务器的 IP 地址:1`，按 Enter。
![](https://qcloudimg.tencent-cloud.cn/raw/3e7d432ce674a8587066df25f42595bf.png)
4. 在弹出的提示框中，单击 Continue。
5. 输入上述步骤 vncserver 命令创建的密码，单击 OK，即可登录实例并使用图形化界面。
 <dx-alert infotype="notice" title="">
如果忘记密码，需要在实例内执行 `vncpasswd` 命令再次修改 vnc 的登录密码。
 </dx-alert>
 附录：
桌面浏览器安装 chrome：
 - 实例内执行命令，下载 **.deb** 包文件 
```shellsession
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```
 - 安装 **.deb** 文件
```shellsession
sudo apt install ./google-chrome-stable_current_amd64.deb
```
:::
</dx-tabs>
