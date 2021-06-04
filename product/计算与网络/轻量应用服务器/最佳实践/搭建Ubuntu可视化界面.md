## 操作场景
VNC（Virtual Network Console）是虚拟网络控制台的缩写。它是一款优秀的远程控制工具软件，由著名的 AT&T 的欧洲研究实验室开发。VNC 是基于 UNIX 和 Linux 操作系统的开源软件，远程控制能力强大，高效实用，其性能可以和 Windows 和 MAC 中的任何远程控制软件媲美。本文档指导您如何在 Ubuntu 操作系统的轻量应用服务器中搭建可视化界面。

## 前提条件
已购买操作系统为 Ubuntu 的轻量应用服务器。如果您还未购买，请参考 [快速配置轻量应用服务器 Linux 实例](https://cloud.tencent.com/document/product/1207/44548)。


## 操作步骤

1. 登录 Linux 实例，详情请参见 [使用 WebShell 方式登录 Linux 实例](https://cloud.tencent.com/document/product/1207/44642)。
2. 执行以下命令，更新和获取最新的软件及版本信息。
```
sudo apt-get update
```
3. 按照实际情况选择执行以下命令，安装 VNC。
<dx-tabs>
::: Ubuntu\s18.04
```
sudo apt-get install vnc4server
```
:::
::: Ubuntu\s20.04
```
sudo apt-get install tightvncserver
```
:::
</dx-tabs>
4. [](id:step04)执行以下命令，启动 VNC 服务，并设置 VNC 的密码。
```
sudo vncserver
```
返回类似如下结果，表示 VNC 启动成功。
![](https://main.qcloudimg.com/raw/adad6ffbb0b1b722d1e429133060134b.png)
5. 执行以下命令，安装 X-windows 的基础。
```
sudo apt-get install x-window-system-core
```
6. 执行以下命令，安装登录管理器。
```
sudo apt-get install gdm3
```
7. 执行以下命令，安装 Ubuntu 的桌面。
```
sudo apt-get install ubuntu-desktop
```
安装过程中，若出现 `Default display manager:`，则选择 “gdm3”。
8. 执行以下命令，安装 Gnome 相关配套软件。
```
sudo apt-get install gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal
```
9. 按照实际情况选择执行以下命令，打开 VNC 配置文件。
<dx-tabs>
::: Ubuntu\s18.04
```
lighthouse@VM-xx-x-ubuntu:~$ sudo vi ~/.vnc/xstartup
```
:::
::: Ubuntu\s20.04
```
lighthouse@VM-xx-x-ubuntu:~$ sudo vi ../../root/.vnc/xstartup
```
:::
</dx-tabs>
10. 按 **i** 切换至编辑模式，并将配置文件修改为如下内容。
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
11. 按 **Esc**，输入 **:wq**，保存文件并返回。
12. 执行以下命令，重启桌面进程。
```
sudo vncserver -kill :1 #杀掉原桌面进程，输入命令（其中的:1是桌面号）
```
```
sudo vncserver :1 #生成新的会话
```
13. [点此](https://www.realvnc.com/en/connect/download/viewer/) 前往 VNC Viewer 官网，并根据本地计算机的操作系统类型，下载对应的版本及安装。
14. 在 VNC Viewer 软件中，输入 `轻量应用服务器的 IP 地址:1`，并按 **Enter**。
![](https://main.qcloudimg.com/raw/df25e2085e9d27d53b1827ccf98a3618.png)
15. 在弹出的提示框中，单击【Continue】。
16. 输入 [步骤4](#step04) 设置的 VNC 的密码，单击【OK】。
>?如出现连接超时报错信息，则请检查网络是否联通，防火墙规则是否放通。其中，防火墙需规则放通 VNC Server 所监听的5901端口，即需在“入站规则”中添加放通协议端口为 `TCP:5901` 的规则，具体操作请参见 [管理防火墙](https://cloud.tencent.com/document/product/1207/44577)。
>

## 相关问题
### 出现 `Could not open location 'file:///root/Desktop'` 错误信息
由于图形化界面按照模板统一进行搭建，可能无法对应实例上的文件。若出现类似 `Could not open location 'file:///root/Desktop'` 报错信息，请根据以下步骤创建对应文件：
1. 执行以下命令，切换为 root 用户。
```shell
sudo su root
```
2. 进入报错信息中提示的路径，并创建对应文件即可。例如：
```shell
root@VM-12-4-ubuntu:~# mkdir Desktop
```
