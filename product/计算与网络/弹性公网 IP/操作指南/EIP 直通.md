EIP 直通功能适用于云服务器内需要查看公网 IP 的场景，例如，将内网流量和外网流量分别转发到不同的 IP 地址。本文介绍如何在 Linux 云服务器和 Windows 云服务器中配置 EIP 直通。
>!EIP 直通过程会导致网络中断，请确认您的业务允许短暂的中断。
>
## 操作场景
用户通过 EIP 访问外网时，可选 NAT 模式或 公网 IP 直通模式，当前默认 NAT 模式。
- NAT 模式下，EIP 在本地不可见，配置时须每次手动加入 EIP 地址。
- 直通后，EIP 在本地可见，配置时无须每次手动加入 EIP 地址，可降低开发成本。

## 使用限制
- 直通为内测功能，目前仅支持私有网络，如有需要请提 [工单申请](https://console.cloud.tencent.com/workorder/category)。
- 配置 EIP 直通的云服务器如果切换了私有网络，则需重新配置直通。
- 云服务器的 EIP 直通不能与 NAT 网关同时使用。如果您的云服务器所在子网的路由表配置了通过 NAT 网关访问公网的路由策略，则云服务器上的 EIP 将无法实现直通功能；您可以通过 [调整 NAT 网关和 EIP 的优先级](https://cloud.tencent.com/document/product/552/30012)，使云服务器先通过本身的 EIP，而不是 NAT 网关来访问公网，此时可以实现 EIP 直通功能。


## 操作步骤
>!您将 EIP 直通脚本下载到云服务器以后，需要先在公网 IP 控制台开启直通功能，然后再运行 EIP 直通脚本，否则可能会导致 EIP 直通失败或出现故障。
>
腾讯云提供了配置 IP 的 EIP 直通脚本，让内网流量走内网 IP，外网流量走公网 IP。如有其他业务场景，请根据具体业务场景配置路由。
<dx-tabs>
::: 在&nbsp;\sLinux\s&nbsp;云服务器中配置&nbsp;\sEIP\s&nbsp;直通
Linux 脚本针对的场景为：内网 IP 和公网 IP 均在主网卡（eth0）上，公网地址通过公网 IP 访问，内网地址通过内网 IP 访问。
>?
>- Linux 脚本支持系统版本 CentOS 6 及以上和 Ubuntu。
>- Linux 脚本仅支持主网卡（eth0），暂不支持辅助网卡。
>

### 步骤一：下载 EIP 直通脚本
由于 EIP 直通过程会导致网络中断，需先获取 EIP 直通脚本到云服务器中。您选择如下任意一种方式获取：
- **手动下载**
 1. 单击 [Linux 脚本下载](https://eip-direct-1254277469.cos.ap-guangzhou.myqcloud.com/eip_direct.sh) 下载 EIP 直通配置脚本到本地，然后再上传至需要进行 EIP 直通的云服务器中。
- **使用wget命令下载**
进入 [云服务器控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=1) 并登录需要 EIP 直通的云服务器，在云服务器中执行以下命令下载：
```plaintext
wget https://eip-direct-1254277469.cos.ap-guangzhou.myqcloud.com/eip_direct.sh
```

### 步骤二：在控制台配置 EIP 直通

1. 登录 [公网 IP 控制台](https://console.cloud.tencent.com/cvm/eip?rid=1)。
2. 选择云服务器主网卡绑定的 EIP 的地域，并在对应 EIP 的右侧操作栏中，选择**更多** > **直通**即可。
![](https://main.qcloudimg.com/raw/56da0588d288d0aa5e1c60855bdb67cf.png)
3. 在弹出的“EIP 直通”对话框中，单击**确定**。

### 步骤三：运行 EIP 直通脚本
为主网卡配置 EIP 直通后，需要登录云服务器，运行 EIP 直通脚本。
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=1) ，选择需要 EIP 直通的云服务器所在地域，并登录该云服务器。
2. 运行 EIP 直通脚本。具体方法：
 1. 执行如下命令，添加执行权限。
```
chmod +x eip_direct.sh
```
 2. 执行如下命令，执行脚本。
 其中，XX.XX.XX.XX为 EIP 地址，可选填，如不填写，直接执行`./eip_direct.sh install`即可。
```
./eip_direct.sh install XX.XX.XX.XX
```
3. 执行 `ip addr` 即可查看到配置的 EIP 地址。
![](https://main.qcloudimg.com/raw/024f4fee7e884af4b935b58b048b907b.png)
:::
::: 在&nbsp;\sWindows\s&nbsp;云服务器中配置&nbsp;\sEIP\s&nbsp;直通
Windows 脚本针对的场景为：主网卡走外网流量，辅助网卡走内网流量。
>?
>- Windows 系统的 EIP 直通，需要内网 IP 和外网 IP 各一张网卡，公网 IP 需在主网卡上，辅助网卡仅需有内网 IP 即可。
>- Windows 设置直通过程中，外网会中断，建议采用 [ VNC 登录的方式](https://cloud.tencent.com/document/product/213/35704)。
>

### 步骤一：下载 EIP 直通脚本[](id:step1)
由于 EIP 直通过程会导致网络中断，您需先下载 EIP 直通脚本到云服务器中。
1. 使用 [ VNC 登录的方式](https://cloud.tencent.com/document/product/213/35704) 登录需要 EIP 直通的云服务器。
2. 在云服务器的浏览器中打开如下链接下载 EIP 直通脚本。
<dx-codeblock>
:::  sh
https://eip-public-read-1255852779.cos.ap-guangzhou.myqcloud.com/eip_windows_direct.bat
:::
</dx-codeblock>


### 步骤二：配置辅助网卡
由于 Windows 脚本针对的场景为辅助网卡走内网流量，因此，需为云服务器配置辅助网卡。
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/overview)。
2. 在云服务器列表中，选择所配置的云服务器的所在地域，单击云服务器 ID，进入详情页。
3. 选择**弹性网卡**标签页，单击**绑定弹性网卡**，新建一个与主网卡同一子网的辅助网卡。
![](https://main.qcloudimg.com/raw/db30871822a0e38ca5cb6fbca142960b.png)
4. 在弹出的“绑定弹性网卡”窗口中，选择**新建弹性网卡并绑定**，填写相关信息，单击**确定**。
 - 所属子网：选择云服务器所属子网。
 - 分配 IP：可选泽自动分配 IP 或手动填写。
![](https://main.qcloudimg.com/raw/f82b4a03d6b6034a414de5010e9ca0c2.png)

### 步骤三：配置主网卡 EIP 直通[](id:step3)

完成辅助网卡的配置后，在 EIP 控制台中为主网卡配置 EIP 直通。
1. 登录 [公网 IP 控制台](https://console.cloud.tencent.com/cvm/eip?rid=1)。
2. 选择云服务器主网卡绑定的 EIP 的地域，并在对应 EIP 的右侧操作栏中，选择**更多** > **直通**即可。
![](https://main.qcloudimg.com/raw/56da0588d288d0aa5e1c60855bdb67cf.png)
3. 在弹出的“EIP 直通”对话框中，单击**确定**。


### 步骤四：云服务器内配置 EIP
 在 EIP 控制台中为主网卡配置 EIP 直通后，需要登录云服务器配置 EIP。
1. 登录云服务器，由于操作过程中外网访问会中断，因此需使用[ VNC 登录的方式](https://cloud.tencent.com/document/product/213/35704)。
2. 在操作系统界面，选择左下角的<img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:-3px 0px;width:25px">，单击 <img src="https://main.qcloudimg.com/raw/f0c84862ef30956c201c3e7c85a26eec.png" style="margin: -3px 0px;">，打开 “Windows PowerShell” 窗口，输入 `firewall.cpl ` 按回车，打开“ Windows 防火墙”页面。
3. 单击**启用或关闭 Windows 防火墙**，进入“自定义设置”页面。
![](https://main.qcloudimg.com/raw/6525a0f3bc8e1e679ceb28894e059222.png)
4. 在“专用网络设置”和“公用网络设置”模块中分别选择**关闭 Windows 防火墙**，单击**确定**即可。
![](https://main.qcloudimg.com/raw/473ffef834aa17f5f6d239354a7919e6.png)
5. 双击 [步骤一](#step1) 中下载的脚本即可执行，输入步骤三中已配置直通的 EIP 地址（可在 [EIP 控制台](https://console.cloud.tencent.com/cvm/eip?rid=1) 中进行查看），连续回车两次即可。 
6.  在 “Windows PowerShell” 窗口中输入`ipconfig`按回车，可看到主网卡上的 IPv4 地址变成 EIP 地址。
>!直通成功后请勿给主网卡再配内网 IP，如果配置会导致云服务器无法访问公网。
>
![](https://main.qcloudimg.com/raw/8260d92c5b99aa53cb774ec367a784e8.png)
:::
</dx-tabs>
