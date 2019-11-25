## 使用场景
用户通过 EIP 访问外网时，可选 NAT 模式或 EIP 直通模式，当前默认 NAT 模式。
- NAT 模式下，EIP 在本地不可见。
- EIP 直通后，EIP 在本地可见，配置时无须每次手动加入 EIP 地址，可降低开发成本。
- NAT 模式能满足大部分需求，但对于云服务器内要求看到外网 IP 的场景，需要使用直通模式。

>! 目前 EIP 直通通过白名单控制，仅支持 VPC 内的设备。

## 操作步骤
### 操作概述
设置 EIP 直通后，需要在操作系统内将 IP 加到网卡上，然后根据业务需求配置操作系统内的路由。
- NAT 网关可绑定开通直通模式的 EIP，但无直通效果。
- 如果有其他业务场景，请根据具体业务场景配置路由。

针对典型场景，我们提供了脚本，详细方法如下：
### Linux 系统
>?
>- Linux 脚本支持系统版本 CentOS 6 及以上和 Ubuntu。
>- Linux 脚本仅支持 eth0，暂不支持辅助网卡。
>- Linux 脚本针对的场景为：内网 IP 和外网 IP 均在 eth0 上，外网地址通过外网 IP 访问，内网地址通过内网 IP 访问。
>- 如果主网卡绑定的公网 IP 不是弹性公网 IP，需要先转换为弹性公网 IP。

#### 步骤1：下载 EIP 配置脚本
由于 EIP 直通过程会导致网络中断，您需先下载 EIP 直通脚本并上传至云服务器。步骤如下：
1. （可选）下载 EIP 直通配置脚本。下载路径：[Linux 脚本下载](https://main.qcloudimg.com/raw/7d07d336030fb1324f3d55c891434612/eip_direct.zip)。
2. Linux 脚本下载到本地后，上传至需要进行 EIP 直通的云服务器中。
>?您也可登录云服务器，在云服务器中直接执行如下命令下载：
```
wget https://main.qcloudimg.com/raw/7d07d336030fb1324f3d55c891434612/eip_direct.zip
```

#### 步骤2：运行 EIP 直通脚本
1. 登录需要 EIP 直通的云服务器。
2. 运行 EIP 直通脚本。具体方法：
 1. 执行如下命令，解压文件。
```
unzip eip_direct.zip
```
 2. 执行如下命令，添加执行权限。
```
chmod +x eip_direct.sh
```
 3. 执行如下命令，执行脚本。
```
./eip_direct.sh install XX.XX.XX.XX
```
其中，XX.XX.XX.XX为 EIP 地址，可选填。

#### 步骤3：开启 EIP 直通
1. 登录 [EIP 控制台](https://console.cloud.tencent.com/cvm/eip?rid=1)。
2. 找到对应的 EIP 所在行，在右侧操作栏中，单击【更多】>【直通】即可。


### Windows 系统
>?
>- Windows 系统的 EIP 直通，需要内网 IP 和外网 IP 各一张网卡，仅需主网卡配公网 IP，辅助网卡仅需配内网 IP 即可。
>- Windows 设置直通过程中，外网会中断，建议采用 [ VNC 登录的方式](https://cloud.tencent.com/document/product/213/35704)。
>- 如下方案针对的场景为：主网卡走外网流量，辅助网卡走内网流量。
- 如果主网卡绑定的公网 IP 不是弹性公网 IP，需要先转换为弹性公网 IP。

#### 步骤1：下载 EIP 配置脚本
由于 EIP 直通过程会导致网络中断，您需先下载 EIP 直通配置脚本到云服务器中。下载路径：[Windows 脚本下载]()。

#### 步骤2：配置辅助网卡
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/overview)。
2. 在云服务器列表中，单击所配置的云服务器 ID，进入详情页。
3. 选择【弹性网卡】标签页，单击【绑定网卡】，新建一个与主网卡同一子网的网卡。
![](https://main.qcloudimg.com/raw/c8449f6bf0b9798464a34a8484dee25f.png)
4. 在弹框中，选择【新建弹性网卡并绑定】，填写相关信息，选泽自动分配 IP ，单击【确定】。
![](https://main.qcloudimg.com/raw/f82b4a03d6b6034a414de5010e9ca0c2.png)

#### 步骤3：云服务器内配置 IP
1. 登录云服务器（由于操作过程中外网访问会中断，因此需使用[ VNC 登录的方式](https://cloud.tencent.com/document/product/213/35704))。
2. `Win+R` 组合键打开运行命令，输入 `firewall.cpl ` 按回车，打开“ Windows 防火墙”页面。
![](https://main.qcloudimg.com/raw/b0cd418caf7d0a95c7a39b75f4996e09.png)
3. 单击【打开或关闭Windows防火墙】，进入“自定义设置”页面。
![](https://main.qcloudimg.com/raw/b3a3fdc9fc16cc8f2ee7986125c05047.png)
4. 在“家庭或工作（专用）网络位置设置”和“公用网络位置设置”模块中分别选择【关闭 Windows 防火墙】即可。
![](https://main.qcloudimg.com/raw/841302b1c8d300dea2bdeb419e190028.png)
5. 双击步骤1中下载的脚本即可执行，输入公网 IP 地址，连续回车两次即可，此时公网已被断开。 

#### 步骤4：配置主网卡直通
1. 登录 [EIP 控制台](https://console.cloud.tencent.com/cvm/eip?rid=1)。
2. 找到对应主网卡绑定的 EIP 所在行，在右侧操作栏中，单击【更多】>【直通】即可。

>!直通成功后请勿给主网卡再配内网 IP，如果配上，则云服务器内无法上网。



