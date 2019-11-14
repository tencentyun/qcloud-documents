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
- 如果主网卡绑定的公网 IP 不是弹性公网 IP，需要先转换为弹性公网 IP。

针对典型场景，我们提供了脚本，详细方法如下：
### Linux 系统
>?
>- Linux 脚本支持系统版本 CentOS 6.x、CentOS 7 和 Ubuntu。
>- Linux 脚本仅支持 eth0，暂不支持辅助网卡。
>- Linux 脚本针对的场景为：内网 IP 和外网 IP 均在 eth0 上，外网地址通过外网 IP 访问，内网地址通过内网 IP 访问。

#### 步骤1：下载 EIP 配置脚本
由于 EIP 直通过程会导致网络中断，您需先下载 EIP 直通脚本并上传至云服务器。步骤如下：
1. 下载 EIP 直通配置脚本。下载路径：[Linux 脚本下载](https://main.qcloudimg.com/raw/7d07d336030fb1324f3d55c891434612/eip_direct.zip)。（可选）
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
>- Windows 系统的 EIP 直通，需要内网 IP 和外网 IP 各一张网卡。
>- Windows 设置直通过程中，外网会中断，建议采用 [ VNC 登录的方式](https://cloud.tencent.com/document/product/213/35704)。
>- 如下方案针对的场景为：主网卡走外网流量，辅助网卡走内网流量。


#### 步骤1：下载 EIP 配置脚本
由于 EIP 直通过程会导致网络中断，您需先下载 EIP 直通配置脚本到云服务器中。下载路径：[Windows 脚本下载]()。

#### 步骤2：配置主网卡直通
1. 登录 [EIP 控制台](https://console.cloud.tencent.com/cvm/eip?rid=1)。
2. 找到对应主网卡绑定的 EIP 所在行，在右侧操作栏中，单击【更多】>【直通】即可。

#### 步骤3：配置辅助网卡
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/overview)。
2. 在云服务器列表中，单击所配置的云服务器 ID，进入详情页。
3. 选择【弹性网卡】标签页，单击【绑定网卡】。
4. 在弹框中，选择【新建弹性网卡并绑定】，填写相关信息，单击【确定】。

#### 步骤4：云服务器内配置 IP
在此步骤，您可以选择如下**任意一种**方式进行配置：
>?由于手动配置较为复杂，推荐使用脚本自动配置。

- [脚本自动配置（推荐）](#auto)。
- [手动配置](#hand)。

#### 脚本自动配置（推荐） <span id="auto">
双击步骤1中下载的脚本即可执行，需要输入如下参数：
- eip：弹性公网 IP。 
- master network card index：主网卡接口号，可通过执行 `netsh int ipv4 show int` 进行查询。
- Flexible network card：弹性（辅助）网卡接口号，可通过执行 `netsh int ipv4 show int` 进行查询。

#### 手动配置 <span id="hand">
1. 登录云服务器（由于操作过程中外网访问会中断，因此需使用[ VNC 登录的方式](https://cloud.tencent.com/document/product/213/35704)。
2. 登录后，打开 powershell（`Win+R` 组合键打开运行命令，输入 `PowerShell` 按回车就即可打开）。
3. 输入如下命令，即可看见有2个网卡：
```
ipconfig 
```
4. 进入【控制面板】>【网络和 Internet】>【网络和共享中心】，单击【以太网】（主网卡）。
5. 在“以太网状态”弹窗中，单击【属性】。
6. 在“以太网属性”弹窗中，选中【Internet 协议版本4（TCP/IPv4）】并单击【属性】。
7. 在“Internet 协议版本4（TCP/IPv4）属性”弹窗中，配置弹性公网 IP 作为静态 IP 地址，示例如下：
 - IP 地址：193.112.18.146 （主网卡上已绑定的公网 IP）
 - 子网掩码：255.255.255.255
8. 在 powershell 中配置路由：
 - 配置默认路由，输入如下命令：
```
  route delete 0.0.0.0/0
	ping 127.0.0.1 -n 5 >nul
	route add 0.0.0.0/0 {网关} if {主网卡接口号}  #(注意：网关、主网卡接口号，需要根据具体情况填写） 
```
 	如上第三条命令示例：`route add 0.0.0.0/0 172.16.0.1 if 14` ，其中`172.16.0.1`为网关，`14`为主网卡的接口号(可通过执行 `netsh int ipv4 show int` 进行查询)，请根据具体情况填写。
 - 配置内网路由，依次输入如下命令（命令的作用为：设置去往内网的流量通过辅助网卡）：
	1. 先预设网关和网卡的接口号：
```
	set gwip=172.16.0.1  #172.16.0.1为网关,根据实际情况填写
	set idx2=15  #15为辅助网卡的接口号，可通过执行 `netsh int ipv4 show int` 进行查询
```
    2. 运行如下命令：
```
 	route delete 10.0.0.0/8
 	route -p add 10.0.0.0/8 %gwip% IF %idx2%  
	route delete 100.64.0.0/10
	route -p add 100.64.0.0/10 %gwip% IF %idx2%
	route delete 172.16.0.0/12
	route -p add 172.16.0.0/12 %gwip% IF %idx2%
	route delete 192.168.0.0/16
	route -p add 192.168.0.0/16 %gwip% IF %idx2%
	route delete 169.254.0.0/16
	route -p add 169.254.0.0/16 %gwip% IF %idx2% 
	route -p add 183.60.83.19 %gwip% IF %idx2%
	route -p add 183.60.82.98 %gwip% IF %idx2%
	route delete 255.255.255.255
	route -p add 255.255.255.255 %gwip% IF %idx2%
```
