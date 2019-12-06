<span id="CentOS6.8"/>

## CentOS 6.8 开启 IPv6
1. 执行如下命令，打开`/etc/modprobe.d/`文件夹下的`ipv6.conf`文件。
```
vi /etc/modprobe.d/ipv6.conf
```
2. 按 “i” 切换至编辑模式，将如下的内核参数设置为0。
```
options ipv6 disable=0
```
![](https://main.qcloudimg.com/raw/37a4754fd0a8f6192d5f3818bcd685fe.png)
3.  按“Esc”，输入 “:wq”，保存文件并返回。
4.  执行如下命令，打开`etc`文件夹下的`sysctl.conf.first`文件。
```
vim /etc/sysctl.conf.first
```
5. 按 “i” 切换至编辑模式，将如下的配置文件参数设置为0。
```
net.ipv6.conf.all.disable_ipv6 = 0
```
![](https://main.qcloudimg.com/raw/e5faf656a6aa6fcbd8a4ac190a13759e.png)
6. 按“Esc”，输入 “:wq”，保存文件并返回。
7. 执行如下命令，打开`/etc/sysconfig/`文件夹下的`network`文件。
```
vi /etc/sysconfig/network
```
8. 按 “i” 切换至编辑模式，增加如下内容。
```
NETWORKING_IPV6=yes
DHCPV6C=yes
```
![](https://main.qcloudimg.com/raw/477077b3418849b62dc7479df9839859.png)
9. 按“Esc”，输入 “:wq”，保存文件并返回。
10. 执行如下命令，打开或创建`/etc/sysconfig/network-scripts/`文件夹下的`route6-eth0`文件。
```
vim /etc/sysconfig/network-scripts/route6-eth0
```
11. 按 “i” 切换至编辑模式，增加如下内容，为网卡的 IPv6 添加默认出口。
```
default dev eth0
```
![](https://main.qcloudimg.com/raw/7bac4ad80fed5cebcdef1fb6ae07cf1b.png)
12. 按“Esc”，输入 “:wq”，保存文件并返回。
13. 重启云服务器，仅通过 `service network restart`，IPv6 无法正常加载。
14. 执行如下命令查看重启后 IPv6 是否已经正常加载。
```
sysctl -a | grep ipv6 | grep disable
```
![](https://main.qcloudimg.com/raw/866730d160b1f0b893b2c00cd0cb4257.png)
15. 依次执行如下命令，查看是否已经获取到 IPv6 地址。
```
dhclient -6
ifconfig
```
![](https://main.qcloudimg.com/raw/cedd7cbd7f5e649c01345356fa0d2688.png)
14. 执行如下命令，打开 `/etc/ssh/`文件夹下的`sshd_config`文件。
```
vim /etc/ssh/sshd_config
```
15. 按 “i” 切换至编辑模式，删除对`AddressFamily any`的注释（即删除前面的`#`），为 ssh 等应用程序开启 IPv6 监听。
![](https://main.qcloudimg.com/raw/e0d64e3836b704bab4713697df865d81.png)
16. 按 “Esc”，输入 “:wq”，保存文件并返回。
17. 执行如下命令，重启 ssh 进程。
```
service sshd restart
```
18. 执行如下命令，查看 ssh 是否已经监听 IPv6。
```
netstat -tupln
```
![](https://main.qcloudimg.com/raw/4b3937053527ea3edd3efedfa0113ca9.png)
16. 测试连通性，请参见 <a href="https://cloud.tencent.com/document/product/215/37946#.E6.AD.A5.E9.AA.A46.EF.BC.9A.E6.B5.8B.E8.AF.95-ipv6-.E7.9A.84.E8.BF.9E.E9.80.9A.E6.80.A7" target="_blank">步骤6：测试 IPv6 的连通性</a>。

<span id="CentOS7.3"/>

## CentOS 7.3/存量 CentOS 7.5/存量 CentOS 7.6 开启 IPv6
1. 执行如下命令，打开`etc`文件夹下的`sysctl.conf`文件。
```
vim /etc/sysctl.conf
```
2. 按 “i” 切换至编辑模式，将如下的 IPv6 相关参数设置为0。
```
net.ipv6.conf.all.disable_ipv6 = 0
net.ipv6.conf.default.disable_ipv6 = 0
net.ipv6.conf.lo.disable_ipv6 = 0
```
![](https://main.qcloudimg.com/raw/dc1e37e0c3a89b170038ef28d6d0583d.png)
3. 按 “Esc”，输入 “:wq”，保存文件并返回。
4. 执行如下命令，对参数进行加载。
```
sysctl -p
```
5. 执行如下命令，查看是否修改成功。
```
sysctl -a | grep ipv6 | grep disable
```
显示结果如下，则已成功修改。
![](https://main.qcloudimg.com/raw/b1294c92045d0dc5c688c6afc970a412.png)

6. 执行如下命令，打开或创建`/etc/sysconfig/network-scripts/`文件夹下的`ifcfg-eth0`文件。
```
vim /etc/sysconfig/network-scripts/ifcfg-eth0
```
7. 按 “i” 切换至编辑模式，增加如下内容。
```
DHCPV6C=yes
```
![](https://main.qcloudimg.com/raw/7eb7d1dbf6e9773ca3282979587d4f55.png)
8. 按 “Esc”，输入 “:wq”，保存文件并返回。
9. 执行如下命令，打开或创建`/etc/sysconfig/network-scripts/`文件夹下的`route6-eth0`文件。
```
vim /etc/sysconfig/network-scripts/route6-eth0
```
10. 按 “i” 切换至编辑模式，增加如下内容，为网卡的 IPv6 添加默认出口。
```
default dev eth0
```
![](https://main.qcloudimg.com/raw/88a185a9dec922e4142c8ad8ffe4a354.png)
11. 按 “Esc”，输入 “:wq”，保存文件并返回。
12. 执行如下命令，重新启动网卡。
```
service network restart
或者
systemctl restart network
```
13. 依次执行如下命令，查看是否已经获取到 IPv6 地址。
```
dhclient -6
ifconfig
```
![](https://main.qcloudimg.com/raw/2e42f1a5e7b9672d60461fe05edfed52.png)
14. 执行如下命令，打开 `/etc/ssh/`文件夹下的`sshd_config`文件。
```
vim /etc/ssh/sshd_config
```
15. 按 “i” 切换至编辑模式，删除对`AddressFamily any`的注释（即删除前面的`#`），为 ssh 等应用程序开启 IPv6 监听。
![](https://main.qcloudimg.com/raw/e0d64e3836b704bab4713697df865d81.png)
16. 按 “Esc”，输入 “:wq”，保存文件并返回。
17. 执行如下命令，重启 ssh 进程。
```
service sshd restart
```
18. 执行如下命令，查看 ssh 是否已经监听 IPv6。
```
netstat -tupln
```
![](https://main.qcloudimg.com/raw/4b3937053527ea3edd3efedfa0113ca9.png)
19. 测试连通性，请参见 <a href="https://cloud.tencent.com/document/product/215/37946#.E6.AD.A5.E9.AA.A46.EF.BC.9A.E6.B5.8B.E8.AF.95-ipv6-.E7.9A.84.E8.BF.9E.E9.80.9A.E6.80.A7" target="_blank">步骤6：测试 IPv6 的连通性</a>。
<span id="Debian8.2"/>

## Debian 8.2 开启 IPv6
1. 执行如下命令，打开`etc`文件夹下的`sysctl.conf`。
```
vim /etc/sysctl.conf
```
2. 按 “i” 切换至编辑模式，将如下的 IPv6 相关参数设置为0。
```
net.ipv6.conf.all.disable_ipv6 = 0
net.ipv6.conf.default.disable_ipv6 = 0
```
3. 按 “Esc”，输入 “:wq”，保存文件并返回。
4. 执行如下命令，对参数进行加载。
```
sysctl -p
```
5. 依次执行如下命令，查看是否已经获取到 IPv6 地址。
```
dhclient -6
ifconfig
```
![](https://main.qcloudimg.com/raw/cd5a2072c73307c79b7997bbd24cec13.png)
6. Debian 8.2 系统默认为 ssh（22端口）开启 IPv6 监听，无需特殊配置，您可执行如下命令，进行查看。
```
netstat -tupln
```
![](https://main.qcloudimg.com/raw/8bdb6f9672f81d8a6df56b61418fe492.png)
7. 执行如下命令，配置默认路由。
```
ip -6 route add default dev eth0
```
8. 测试连通性，请参见  <a href="https://cloud.tencent.com/document/product/215/37946#.E6.AD.A5.E9.AA.A46.EF.BC.9A.E6.B5.8B.E8.AF.95-ipv6-.E7.9A.84.E8.BF.9E.E9.80.9A.E6.80.A7" target="_blank">步骤6：测试 IPv6 的连通性</a>。

<span id="Windows2012"/>

## Windows 2012 开启 IPv6
1. 登录云服务器实例，进入操作系统的【控制面板】>【网络和 Internet】>【网络和共享中心】，单击命名为“以太网”的网卡进行编辑。
![](https://main.qcloudimg.com/raw/4696aa941df5c22dbf4446c01aabefbc.png)
2. 在“以太网状态”弹窗中，单击【属性】。
3. 在“以太网属性”弹窗中，选中【Internet 协议版本6（TCP/IPv6）】并单击【属性】。
![](https://main.qcloudimg.com/raw/1f10d494b792d975a387ec6e38555021.png)
4. 在“Internet 协议版本6（TCP/IPv6）属性”弹窗中，手工编辑 IPv6 地址并设置 DNS，单击【确定】。
![](https://main.qcloudimg.com/raw/fac63249f22197686d68e3afffb3eb14.png)
5. 登录 powershell 依次执行如下命令配置默认路由以及查看 IPv6 地址，并通过 ping 和远程桌面测试 IPv6 连通性。
```
netsh interface ipv6 add route ::/0 "以太网"
ipconfig
```
![](https://main.qcloudimg.com/raw/eec1e647837d6b096ef9e022c3bafa7e.png)
