网络问题、防火墙设置、服务器负载过高等都可能导致网站无法访问的问题。本文将介绍网站无法访问的问题如何一步步进行排查定位。
## 服务器原因排查
服务器关机、硬件故障、CPU/内存/带宽使用率过高都可能造成网站无法访问，因此建议依次排查服务器的运行状态、CPU/内存/带宽的使用情况。
1. 查看服务器运行状态。登录腾讯云的控制台，查看实例的运行情况，确认实例正常运行。如果状态非运行中，建议进行重启等相应处理。
![](https://mc.qcloudimg.com/static/img/557518484f419b143a1a066d5494bd18/image.png)
2. 查看资源使用情况。在实例的详情页，单击监控 tab 查看CPU/内存/带宽的使用情况。如果存在 CPU 使用过高的情况，请参考 [CPU 使用率过高排查（Windows 系统）](/document/product/213/14635) 和 [CPU 使用率过高排查（Linux 系统）](/document/product/213/14634) 进行定位；带宽使用过高的情况，参考 [带宽利用率过高问题处理](/document/product/213/14637)。
![](https://mc.qcloudimg.com/static/img/f339ec2fbf98523efbaeb0ccc20f6edf/image.png)
3. 检查 Web 服务相应的端口是否被正常监听。下面以 HTTP 服务常用的 80 端口为例，介绍 Linux 和 Windows 系统下应该如何检查：
 - **Linux 系统**
使用 **netstat** 查看 80 端口的监听情况，具体命令如下所示，**-t** 显示 tcp 端口，**-p** 显示进程标识符和对应的程序名，**-l** 显示监听套接字。
![](https://mc.qcloudimg.com/static/img/ab5fa663197c3fa0738b2ceb3f559fd3/image.png)
 - **Windows 系统**
使用 **netstat -ano|findstr :80** 查看 80 端口的监听情况。根据进程 ID 可以查看正在监听的进程名。
![](https://mc.qcloudimg.com/static/img/c9c32a2e9f12235ad3d2a5aca313f298/image.png)
如果端口没有被正常监听，请检查 Web 服务进程是否启动或者正常配置。

4. 检查防火墙设置，是否放行 Web 服务进程对应的端口。
Linux 查看 iptables 是否放行 80 端口，Windows 系统则检查 Windows 防火墙设置。

## 网络问题
排除了服务器问题后，网站无法访问还可能是网络问题引起，这里可以使用 ping 命令 ping 目的服务器的公网 IP，确认是否有丢包或延时高的情况。如果存在，使用 MTR 进一步进行排查。具体请参考 [服务器网络延迟和丢包处理](/document/product/213/14638)。
![](https://mc.qcloudimg.com/static/img/30d9946522f43cfc1c6731b9035ae9e9/image.png)

## 安全组设置
安全组是一个虚拟防火墙，可以控制关联实例的入站流量和出站流量。安全组的规则可以指定协议、端口、策略等等。没有放通Web进程相关的端口也会造成网站无法访问。排除了服务器和网络问题后，需要对实例所属的安全组的规则进行检查。
可以在实例的详情页安全组tab查看实例使用的安全组以及对应安全组具体的出站以及入站规则，确认是否放通Web进程相关的端口。如果没有放通相应的端口，请编辑绑定的安全规则，进行放通。
![](https://mc.qcloudimg.com/static/img/dd0d3c72d149b5a8b43f7e80d7b84b0f/image.png)

## 域名备案解析问题
排除了上述三个问题后，可以尝试使用服务器公网 IP 进行访问。如果使用 IP 可以访问，而域名访问失败，则可能是域名备案或者解析的问题。
1. 国家工信部规定，对未取得许可或者未履行备案手续的网站不得从事互联网信息服务，否则就属于违法行为。为不影响网站长久正常运行，想要开办网站建议先办理网站备案，备案成功取得通信管理局下发的 ICP 备案号后才能开通访问。如果您的域名没有备案，则需先进行 [域名备案](https://console.cloud.tencent.com/beian)。
如果使用的是腾讯云的域名服务，可以在 **[控制台](https://console.cloud.tencent.com/) > 域名与网站 > 域名管理** 查看相应的域名情况。
![](https://mc.qcloudimg.com/static/img/e3a61dd49cffd3331c4a20db64442b5a/image.png)
2. 域名解析没有正确配置，导致请求没有路由到对应的 Web 服务器也会导致网站无法访问。如果您使用的是腾讯云的域名服务，可以在 **[控制台](https://console.cloud.tencent.com/) > 域名与网站 > 域名管理** ，单击对应域名的解析按钮，查看域名解析详情。
![](https://mc.qcloudimg.com/static/img/66642d8208c8ccb70aa43fe413dc618b/image.png)

