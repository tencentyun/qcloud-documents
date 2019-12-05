A failed ping test from a local server to an instance may be caused by incorrect destination server configuration, unsuccessful domain name resolution or linkage failure. The following describes how to troubleshoot this problem if the local network is normal (other websites can be pinged):
## 1. Check whether the instance is bound with a public IP.
Only an instance with public IP can access and be accessed by other computers on the Internet. An instance without public IP cannot be pinged outside the private IP. You can check the information of public IP on the [instance details page in the console](https://console.cloud.tencent.com/cvm/index), as shown below. Bind an EIP to the instance if it is not bound with any public IP.
![](https://mc.qcloudimg.com/static/img/ab9932f698e4727a431a164d61c3e934/image.png)
## 2. Check the security group configuration
Security group is a virtual firewall, which allows you to control the inbound and outbound traffic of the associated instance. You can specify protocols, ports and policies for the rules of a security group. Check whether the ICMP protocol that is used in ping test is allowed in the security group associated to the instance. You can view the information of the associated security group and its inbound/outbound rules in the **Security Group** tab of the instance details page.
![](https://mc.qcloudimg.com/static/img/0788ebb34a8fe09b3258ed5af254e75d/image.png)
## 3. Check the system configurations
### Check kernel parameters and firewall settings on Linux
On Linux system, whether a ping test is allowed depends on both kernel and firewall configuration. If either of them blocks the ping test, "Request timeout" occurs.
#### Kernel parameter icmp_echo_ignore_all
icmp_echo_ignore_all indicates whether to ignore all ICMP Echo requests. 1: Disabled; 0: Enabled. Check icmp_echo_ignore_all configuration using the following command.
```
cat /proc/sys/net/ipv4/icmp_echo_ignore_all
```
![](https://mc.qcloudimg.com/static/img/34a48b2e128d7b9b6ca6e34f1ff789a0/image.png)
You can modify the configuration using echo command.
```
echo "1" >/proc/sys/net/ipv4/icmp_echo_ignore_all
```
![](https://mc.qcloudimg.com/static/img/4e1de32f519bda6f88b4d34a9872dbdb/image.png)

#### Firewall settings
Check the firewall rules of the CVM using **iptables -L**, and check whether ICMP-related rules are blocked.
![](https://mc.qcloudimg.com/static/img/b212bcfb8a1587156768fcc8de0140ae/image.png)
### Firewall settings on Windows
Go to **Control Panel** -> **Windows Firewall Settings** -> **Advanced Settings** to check whether inbound and outbound rules related to ICMP are blocked.
![](https://mc.qcloudimg.com/static/img/e5e6a914dbdaf1f0dab5e89440d7662e/image.png)
![](https://mc.qcloudimg.com/static/img/247440c6c79697133685cbf16544d2cc/image.png)
![](https://mc.qcloudimg.com/static/img/87214a5efc12560e51aa15c10d8040c7/image.png)

## 4. Check whether the domain name is licensed.
If the public IP can be pinged while the domain name cannot, the problem may be caused by an unlicensed domain name or unsuccessful domain name resolution.
According to the regulations of MIIT, websites that have not obtained permission nor completed ICP licensing cannot engage in any Internet information services, otherwise it is considered illegal. To ensure the persistent and normal operation of your website, complete website ICP licensing before setting up a website. The website cannot be accessed until you obtain the ICP license number issued by MIIT. If your domain name has not been licensed, complete [Domain Name ICP Licensing](https://console.cloud.tencent.com/beian).
If you are using Tencent Cloud DNS, go to the **[console](https://console.cloud.tencent.com/) -> Domain Name and Website -> Domain Name Management** to view the information of an appropriate domain name.
![](https://mc.qcloudimg.com/static/img/5e95aaa3a25133e087766db94bcd9df0/image.png)
## 5. Domain Name Resolution
Ping test failure may also be caused by the incorrect configuration of domain name resolution. If you are using Tencent Cloud DNS, go to the **[console](https://console.cloud.tencent.com/) -> Domain Name and Website -> Domain Name Management**, and click the **Resolve** button of a domain name to view the its resolution details.
![](https://mc.qcloudimg.com/static/img/109308ab3186ac7201df83970004697f/image.png)

If the problem persists after all the above procedures are completed:
- If the domain name cannot be pinged, check your website configuration.
- If the public IP cannot be pinged, contact our engineer to locate the problem by [submitting a ticket](https://console.cloud.tencent.com/workorder/category) and attaching relevant information about the instance and two-way (from local server to CVM and from CVM to local server) MTR data. For more information on how to use MTR, please see [Network Delay and Packet Loss for CVM](https://cloud.tencent.com/document/product/213/14638).

