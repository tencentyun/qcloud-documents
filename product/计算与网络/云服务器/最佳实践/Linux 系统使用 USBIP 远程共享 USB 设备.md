## 操作场景

[USB/IP](http://usbip.sourceforge.net/) 是一个开源项目，已合入 Kernel，在 Linux 环境下可以通过使用 USB/IP 远程共享 USB 设备。本文档以如下环境版本为例，为您演示如何使用 USB/IP 远程共享 USB 设备：
USB Client：CentOS 7.6 操作系统的云服务器
USB Server：Debian 操作系统的本地计算机

## 注意事项
不同发行版的 Linux 操作系统安装 USB/IP 的方式，以及内核模块名称略有不同。您可前往对应 Linux 系统官方发行版页面，查看当前使用的 Linux 系统是否支持 USB/IP 功能。


## 操作步骤

### 配置 USB Server

1. 在本地计算机上，依次执行以下命令，安装 USB/IP 并加载相关的内核模块。
```
sudo apt-get install usbip
sudo modprobe usbip-core
sudo modprobe vhci-hcd
sudo modprobe usbip_host
```
2. 插入 USB 设备，并执行以下命令，查询可用的 USB 设备。
```
usbip list --local
```
例如，在本地计算机上插入一个 Feitian 的优 Key，返回如下结果：
```
busid 1-1.3(096e:031b)
Feitian Technologies, Inc.: unknown product(096e:031b)
```
3. 记录 busid 的值，并依次执行以下命令，启动监听服务，指定 USB/IP 端口号，共享 USB 设备。
```
sudo usbipd -D [--tcp-port PORT]
sudo usbip bind -b [busid]
```
例如，USB/IP 指定端口号为3240端口（即 USB/IP 的默认端口），busid 为 `1-1.3`，则执行以下命令：
```
sudo usbipd -D
sudo usbip bind -b 1-1.3
```
4. （可选）执行以下命令，创建 SSH 隧道，并使用端口监听。
>? 没有公网 IP 的本地计算机，请执行此步骤。如您的本地计算机有公网 IP，请跳过此步骤。
>
```
ssh -Nf -R USB/IP指定端口号:localhost:USB/IP指定端口号 root@your_host
```
`your_host` 表示云服务器的 IP 地址。
例如，USB/IP 的端口号为3240端口，云服务器的 IP 地址为192.168.15.24，则执行以下命令：
```
ssh -Nf -R 3240:localhost:3240 root@192.168.15.24
```


### 配置 USB Client

>? 以下操作步骤以本地计算机没有公网 IP 为例，如您的本地计算机有公网 IP，请将步骤中的`127.0.0.1`修改为本地计算机的公网 IP 地址。
>

1. [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。
2. 依次执行以下命令，下载 USB/IP 源。
```
rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
rpm -ivh http://www.elrepo.org/elrepo-release-7.0-3.el7.elrepo.noarch.rpm
```
3. 依次执行以下命令，安装 USB/IP。
```
yum -y install kmod-usbip usbip-utils
modprobe usbip-core
modprobe vhci-hcd
modprobe usbip-host
```
4. 执行以下命令，查询云服务器可用的 USB 设备。
```
usbip list --remote 127.0.0.1
```
例如，找到 Feitian 的优 Key 的信息，返回如下结果：
```
Exportable USB devices
======================
-127.0.0.1 1-1.3: Feitian Technologies, Inc.: unknown product(096e:031b):/sys/devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.3:(Defined at Interface level)(00/00/00)
```
5. 执行以下命令，将 USB 设备绑定至服务器中。
```
usbip attach --remote=127.0.0.1 --busid=1-1.3
```
6. 执行以下命令，查看当前 USB 设备列表。
```
lsusb
```
返回类似如下信息，即表示共享成功。
```
Bus 002 Device 002:ID096e:031b Feitian Technologies, Inc.
Bus 002 Device 001:ID1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 001:ID1d6b:0001 Linux Foundation 1.1 root hub
```
