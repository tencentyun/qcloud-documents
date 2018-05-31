本地主机 ping 不通实例可能由于目标服务器的设置不正确、域名没有正确解析、链路故障等等问题引起。在确保本地网络正常（可以正常 ping 通其他网站）的前提下，下文将就如何进行排查进行详细的说明：
## 一. 确认实例是否有公网 IP
实例必须具备公网 IP 才能跟 Internet 上的其他计算机相互访问。实例没有公网 IP，内网 IP 外部是无法直接 ping 通的。可以在 [控制台实例详情页](https://console.cloud.tencent.com/cvm/index) 查看公网 IP 的信息，如下图。如无公网 IP 可以绑定弹性公网 IP。
![](https://mc.qcloudimg.com/static/img/ab9932f698e4727a431a164d61c3e934/image.png)
## 二. 安全组设置确认
安全组是一个虚拟防火墙，可以控制关联实例的入站流量和出站流量。安全组的规则可以指定协议、端口、策略等等。由于 ping 使用的是 ICMP 协议，这里要注意实例关联的安全组是否允许 ICMP。实例使用的安全组以及详细的入站和出站规则可以在实例详情页的安全组 tab 查看。
![](https://mc.qcloudimg.com/static/img/0788ebb34a8fe09b3258ed5af254e75d/image.png)
## 三. 系统设置检查
### Linux 内核参数和防火墙设置检查
Linux 系统是否允许 ping 由内核和防火墙设置两个共同决定，任何一个禁止，都会造成 ping 包“Request timeout”。
#### 内核参数icmp_echo_ignore_all
icmp_echo_ignore_all 代表系统是否忽略所有的 ICMP Echo 请求，1 禁止，0允许。使用如下指令查看系统 icmp_echo_ignore_all 设置。
```
cat /proc/sys/net/ipv4/icmp_echo_ignore_all
```
![](https://mc.qcloudimg.com/static/img/34a48b2e128d7b9b6ca6e34f1ff789a0/image.png)
可以使用 echo 命令进行修改：
```
echo "1" >/proc/sys/net/ipv4/icmp_echo_ignore_all
```
![](https://mc.qcloudimg.com/static/img/4e1de32f519bda6f88b4d34a9872dbdb/image.png)

#### 防火墙设置
使用** iptables -L** 查看当前服务器的防火墙规则，查看 ICMP 对应规则，看是否被禁止。
![](https://mc.qcloudimg.com/static/img/b212bcfb8a1587156768fcc8de0140ae/image.png)
### Windows 防火墙设置
控制面板 > Windows 防火墙设置 > 高级设置 > 查看 ICMP 有关的出入站规则，是否被禁止。
![](https://mc.qcloudimg.com/static/img/e5e6a914dbdaf1f0dab5e89440d7662e/image.png)
![](https://mc.qcloudimg.com/static/img/247440c6c79697133685cbf16544d2cc/image.png)
![](https://mc.qcloudimg.com/static/img/87214a5efc12560e51aa15c10d8040c7/image.png)

## 四. 域名是否备案
如果是可以 ping 通公网 IP，而域名 ping 不通，此时可能是域名没有备案，或者域名解析的问题。
国家工信部规定，对未取得许可或者未履行备案手续的网站不得从事互联网信息服务，否则就属于违法行为。为不影响网站长久正常运行，想要开办网站建议先办理网站备案，备案成功取得通信管理局下发的 ICP 备案号后才能开通访问。如果您的域名没有备案，则需先进行[域名备案](https://console.cloud.tencent.com/beian)。
如果使用的是腾讯云的域名服务，可以在 **[控制台](https://console.cloud.tencent.com/) > 域名与网站 > 域名管理** 查看相应的域名情况。
![](https://mc.qcloudimg.com/static/img/5e95aaa3a25133e087766db94bcd9df0/image.png)
## 五. 域名解析
域名 ping 不通的另外一个原因是域名解析没有正确地配置。如果用户使用的是腾讯云的域名服务可以在 **[控制台](https://console.cloud.tencent.com/) > 域名与网站 > 域名管理**，单击对应域名的解析按钮，查看域名解析详情。
![](https://mc.qcloudimg.com/static/img/109308ab3186ac7201df83970004697f/image.png)

若上述步骤无法解决问题，请参考：
- 域名 ping 不通，请检查您网站配置。
- 公网 IP ping 不通，请附上实例的相关信息和双向 MTR 数据（从本地到云服务器以及云服务器到本地），[提交工单](https://console.cloud.tencent.com/workorder/category) 联系工程师协助定位。MTR 的使用方法请参考 [服务器网络延迟和丢包处理](https://cloud.tencent.com/document/product/213/14638)。
