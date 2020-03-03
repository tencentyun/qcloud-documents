## 使用场景
用户通过 EIP 访问外网时，可选 NAT 模式或 EIP 直通模式，当前默认 NAT 模式。
- NAT 模式下，EIP 在本地不可见。
- EIP 直通后，EIP 在本地可见，配置时无须每次手动加入 EIP 地址，可降低开发成本。
- NAT 模式能满足大部分需求，但对于云服务器内需要查看公网 IP 的场景，需要使用直通模式。

## 使用限制
- 目前 EIP 直通通过白名单控制，仅支持 VPC 内的设备，如需使用，请提 [工单申请](https://console.cloud.tencent.com/workorder/category)。
- NAT 网关可绑定开通直通模式的 EIP，但无直通效果。
- 云服务器的 EIP 直通不能与 NAT 网关同时使用。如果您的云服务器所在子网的路由表配置了通过 NAT 网关访问公网的路由策略，则云服务器上的 EIP 将无法实现直通功能；您可以通过 [调整 NAT 网关和 EIP 的优先级](https://cloud.tencent.com/document/product/552/30012)，使云服务器先通过本身的 EIP，而不是 NAT 网关来访问公网，此时可以实现 EIP 直通功能。

## 操作步骤
EIP 直通不仅需要在控制台开启，也需要在操作系统内将 IP 加到网卡上，然后根据业务需求配置操作系统内的路由，为此我们提供了配置 IP 的脚本，让内网流量走内网 IP，外网流量走公网 IP。
>?如果有其他业务场景，请根据具体业务场景配置路由。
>
### 在 Linux 云服务器中配置 EIP 直通
>?
>- Linux 脚本支持系统版本 CentOS 6 及以上和 Ubuntu。
>- Linux 脚本仅支持主网卡（eth0），暂不支持辅助网卡。
- 如果主网卡绑定的公网 IP 不是弹性 IP，需要先转换为弹性 IP，详情请参见 [公网 IP 转弹性 IP]( https://cloud.tencent.com/document/product/213/16586#.E5.85.AC.E7.BD.91-ip-.E8.BD.AC.E5.BC.B9.E6.80.A7-ip)。

#### 操作场景
Linux 脚本针对的场景为：内网 IP 和公网 IP 均在主网卡（eth0）上，公网地址通过公网 IP 访问，内网地址通过内网 IP 访问。

#### 步骤1：下载 EIP 直通脚本
由于 EIP 直通过程会导致网络中断，需先获取 EIP 直通脚本到云服务器中。您选择如下任意一种方式获取：
- **方式一： 上传 EIP 直通脚本**
 1. 下载 EIP 直通配置脚本。下载路径：[Linux 脚本下载](https://eip-direct-1254277469.cos.ap-guangzhou.myqcloud.com/eip_direct.sh)。
 2. Linux 脚本下载到本地后，上传至需要进行 EIP 直通的云服务器中。
- **方法二：直接使用命令**
登录云服务器，在云服务器中直接执行如下命令下载：
```
wget https://eip-direct-1254277469.cos.ap-guangzhou.myqcloud.com/eip_direct.sh
```

#### 步骤2：运行 EIP 直通脚本
1. 登录需要 EIP 直通的云服务器。
2. 运行 EIP 直通脚本。具体方法：
 1. 执行如下命令，添加执行权限。
```
chmod +x eip_direct.sh
```
 2. 执行如下命令，执行脚本。
```
./eip_direct.sh install XX.XX.XX.XX
```
其中，XX.XX.XX.XX为 EIP 地址，可选填，如不填写，请直接执行`./eip_direct.sh install`即可。

#### 步骤3：开启 EIP 直通
1. 登录 [EIP 控制台](https://console.cloud.tencent.com/cvm/eip?rid=1)。
2. 找到对应的 EIP 所在行，在右侧操作栏中，单击【更多】>【直通】即可。


### 在 Windows 云服务器中配置 EIP 直通
>?
>- Windows 系统的 EIP 直通，需要内网 IP 和外网 IP 各一张网卡，仅需主网卡配公网 IP，辅助网卡仅需配内网 IP 即可。
>- Windows 设置直通过程中，外网会中断，建议采用 [ VNC 登录的方式](https://cloud.tencent.com/document/product/213/35704)。
- 如果主网卡绑定的公网 IP 不是弹性 IP，需要先转换为弹性 IP，详情请参见 [公网 IP 转弹性 IP]( https://cloud.tencent.com/document/product/213/16586#.E5.85.AC.E7.BD.91-ip-.E8.BD.AC.E5.BC.B9.E6.80.A7-ip)。

#### 操作场景
Windows 脚本针对的场景为：主网卡走外网流量，辅助网卡走内网流量。

#### 步骤1：下载 EIP 直通脚本 <span id="step1" />
由于 EIP 直通过程会导致网络中断，您需先下载 EIP 直通脚本到云服务器中。
请在云服务器的浏览器中打开如下链接进行 EIP 直通脚本的下载：
```
https://windows-1254277469.cos.ap-guangzhou.myqcloud.com/eip_windows_direct.bat
```

#### 步骤2：配置辅助网卡
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/overview)。
2. 在云服务器列表中，单击所配置的云服务器 ID，进入详情页。
3. 选择【弹性网卡】标签页，单击【绑定网卡】，新建一个与主网卡同一子网的网卡。
![](https://main.qcloudimg.com/raw/c8449f6bf0b9798464a34a8484dee25f.png)
4. 在弹框中，选择【新建弹性网卡并绑定】，填写相关信息，选泽自动分配 IP ，单击【确定】。
![](https://main.qcloudimg.com/raw/f82b4a03d6b6034a414de5010e9ca0c2.png)

#### 步骤3：配置主网卡直通
1. 登录 [EIP 控制台](https://console.cloud.tencent.com/cvm/eip?rid=1)。
2. 找到对应主网卡绑定的 EIP 所在行，在右侧操作栏中，单击【更多】>【直通】即可。

#### 步骤4：云服务器内配置 IP
1. 登录云服务器，由于操作过程中外网访问会中断，因此需使用[ VNC 登录的方式](https://cloud.tencent.com/document/product/213/35704)。
2. 在操作系统界面，选择左下角的<img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:-3px 0px;width:25px">，单击 <img src="https://main.qcloudimg.com/raw/f0c84862ef30956c201c3e7c85a26eec.png" style="margin: -3px 0px;">，打开 “Windows PowerShell” 窗口，输入 `firewall.cpl ` 按回车，打开“ Windows 防火墙”页面。
3. 单击【启用或关闭 Windows 防火墙】，进入“自定义设置”页面。
![](https://main.qcloudimg.com/raw/6525a0f3bc8e1e679ceb28894e059222.png)
4. 在“专用网络设置”和“公用网络设置”模块中分别选择【关闭 Windows 防火墙】，单击【确定】即可。
![](https://main.qcloudimg.com/raw/473ffef834aa17f5f6d239354a7919e6.png)
5. 双击 [步骤1](#step1) 中下载的脚本即可执行，输入公网 IP 地址，连续回车两次即可。 
6.  在 “Windows PowerShell” 窗口中输入`ipconfig`按回车，可看到主网卡上的 IPv4 地址变成公网地址。

>!直通成功后请勿给主网卡再配内网 IP，如果配置，则云服务器无法访问公网。

