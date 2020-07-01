本教程为您介绍如何为 VPC 内的云服务器配置 IPv6，实现 IPv6 的内外网通信。
## Linux 云服务器配置 IPv6
Linux 云服务器配置 IPv6 有两种方式：[工具配置](#.E5.B7.A5.E5.85.B7.E9.85.8D.E7.BD.AE) 和 [手动配置](#.E6.89.8B.E5.8A.A8.E9.85.8D.E7.BD.AE)。
- 工具配置通过工具一键配置 IPv6。
- 手动配置需要您对 Linux 命令有一定的熟练掌握程度。

请根据您的实际情况选择对应的方式，推荐您使用更高效的自动配置工具配置 IPv6 地址。
<table>
<thead>
<tr style="text-align:center;">
<th width="28%" ><strong>镜像类型</strong></th>
<th width="19%" ><strong>购买时间</strong></th>
<th width="15%" ><strong>是否已开启 IPv6</strong></th>
<th width="18%" ><strong>配置方式</strong></th>
</tr>
</thead>
<tbody>
<tr style="text-align:center;">
<td rowspan="2">CentOS 7.5/CentOS 7.6</td>
<td>2019-06-31前购买</td>
<td>否</td>
<td rowspan="4">
<li><a href="#.E5.B7.A5.E5.85.B7.E9.85.8D.E7.BD.AE">工具配置</a></li>
<li><a href="#.E6.89.8B.E5.8A.A8.E9.85.8D.E7.BD.AE">手动配置</a></li></td>
</tr>
<tr style="text-align:center;">
<td>2019-06-31后购买</td>
<td>是</td>
</tr>
<tr style="text-align:center;">
<td rowspan="2">CentOS 6/CentOS 7（不含7.5/7.6）<br>
Ubuntu14.04/Ubuntu 12.04<br>
Debian 8/Debian 9<br>
CoreOS 17<br>
Tencent Linux<br>
</td>
<td>2019-11-13 01:00前购买</td>
<td>否</td>
</tr>
<tr style="text-align:center;">
<td>2019-11-13 01:00后购买</td>
<td>是</td>
</tr>
</tbody></table>

### 工具配置
>? 不支持工具配置的操作系统：FreeBSD、Suse、Ubuntu18。
>
请根据云服务器是否已开启 IPv6 选择对应的配置方式：
- [未开启 IPv6 的云服务器](#unopen)
- [已开启 IPv6 的云服务器](#open)


#### 未开启 IPv6 的云服务器 <span id="unopen" />
enable_ipv6 工具可以为已分配 IPv6 地址的 CVM 实例一键配置 IPv6 地址。

**使用限制**
- enable_ipv6 工具仅适用于 VPC 网络环境下。
- enable_ipv6 工具运行时会自动重启网卡、网络服务，短时间内网络可能会不可用，请慎重执行。

**操作步骤**
1. 登录云服务器，在云服务器中直接执行如下命令下载 enable_ipv6 工具：
```
wget https://iso-1251783334.cos.ap-guangzhou.myqcloud.com/scripts/enable_ipv6.sh
```
2. 赋予执行权限后使用管理员权限执行：
```bash
chmod +x ./enable_ipv6.sh
./enable_ipv6.sh [网卡名称]  
# 示例 1：./enable_ipv6.sh eth0
# 示例 2：./enable_ipv6.sh eth1
``` 
3. （此步骤仅适用于 CoreOS 操作系统）重启云服务器，使上述配置生效。

#### 已开启 IPv6 的云服务器 <span id="open" />
config_ipv6 工具可以为已开启 IPv6 且已分配 IPv6 地址的 CVM 实例一键配置 IPv6 地址。

**使用限制**
- config_ipv6 工具仅适用于 VPC 网络环境下。
- config_ipv6 工具运行时会自动重启网卡、网络服务，短时间内网络可能会不可用，请慎重执行。

**操作步骤**
1. 登录云服务器，在云服务器中直接执行如下命令下载 config_ipv6 工具：
```
wget https://iso-1251783334.cos.ap-guangzhou.myqcloud.com/scripts/config_ipv6.sh
```
2. 赋予执行权限后使用管理员权限执行：
```bash
chmod +x ./config_ipv6.sh  
./config_ipv6.sh [网卡名称] 
# 示例 1：./config_ipv6.sh eth0
# 示例 2：./config_ipv6.sh eth1
```
3. （此步骤仅适用于 CoreOS 操作系统）重启云服务器，使上述配置生效。

对于需要自动化配置 IPv6 实例的需求，例如，大批量配置，建议您使用实例自定义数据配合脚本的方式来调用。详情请参见 [实例自定义数据](https://cloud.tencent.com/document/product/213/17525)。如下为脚本示例（假设是 RHEL 系列，Bash Shell 脚本）。
> ?该示例仅对 eth0 进行配置，实际操作时注意修改为实际使用的网卡名。
> 
```bash
#!/bin/sh
install_dir=/usr/sbin
install_path="$install_dir"/config-ipv6
if [ ! -f "$install_path" ]; then
    tool_url="https://iso-1251783334.cos.ap-guangzhou.myqcloud.com/scripts/config_ipv6.sh"
    # download the tool
    if ! wget "$tool_url" -O "$install_path"; then
        echo "[Error] download tool failed, code $?"
        exit "$?"
    fi
fi
# chmod the tool
if ! chmod +x "$install_path"; then
    echo "[Error] chmod tool failed, code $?"
    exit "$?"
fi
# run the tool
$install_path eth0
```


### 手动配置
如下列举了四种典型的 Linux 云服务器的操作方法：
- [新购 CentOS 7.5/新购 CentOS 7.6 配置 IPv6](#新购CentOS7.5/CentOS7.6)
- [CentOS 6.8 配置 IPv6](#CentOS6.8)
- [CentOS 7.3/存量 CentOS 7.5/存量 CentOS 7.6 配置 IPv6](#CentOS7.3)
- [Debian 8.2 配置 IPv6](#Debian8.2)

>?
>- 新购 CentOS 7.5/新购 CentOS 7.6 指2019年06月31日**后**购买的云服务器。
>- 存量 CentOS 7.5/存量 CentOS 7.6 指2019年06月31日**前**购买的云服务器。
>
<span id="新购CentOS7.5/CentOS7.6"/>

#### 新购 CentOS7.5 /新购 CentOS7.6 配置 IPv6
1. 进入 [云服务器控制台](https://console.cloud.tencent.com/cvm) 并登录实例。
![](https://main.qcloudimg.com/raw/4d50f2b254367a77eb09724bdbff76f8.png)
2. 执行如下命令，打开`/etc/sysconfig/network-scripts/`文件夹下的`ifcfg-eth0`文件。
```
vim /etc/sysconfig/network-scripts/ifcfg-eth0
```
3. 按 “i” 切换至编辑模式，增加如下内容。
```
DHCPV6C=yes
```
![](https://main.qcloudimg.com/raw/94b60f6fb3177f5124339e5c017a8ac2.png)
4. 按 “Esc”，输入 “:wq”，保存文件并返回。
5. 依次执行如下命令，查看是否已经获取到 IPv6 地址。
```
dhclient -6
ifconfig
```
![](https://main.qcloudimg.com/raw/25ccd3b27744ad0f056de14a39465724.png)

6. 执行如下命令，打开 `/etc/ssh/`文件夹下的`sshd_config`文件。
```
vim /etc/ssh/sshd_config
```
7. 按 “i” 切换至编辑模式，删除对`AddressFamily any`的注释（即删除前面的`#`），为 ssh 等应用程序开启 IPv6 监听。
![](https://main.qcloudimg.com/raw/52e9354e072a31f21071acde0262d58d.png)
8. 按 “Esc”，输入 “:wq”，保存文件并返回。
9. 执行如下命令，重启 ssh 进程。
```
service sshd restart
```
10. 执行如下命令，查看 ssh 是否已经监听 IPv6。
```
netstat -tupln
```
![](https://main.qcloudimg.com/raw/4b3937053527ea3edd3efedfa0113ca9.png)
11. 测试连通性，请参见 [测试 Linux 云服务器 IPv6 的连通性](#.E9.99.84.E5.BD.95.EF.BC.9A.E6.B5.8B.E8.AF.95-linux-.E4.BA.91.E6.9C.8D.E5.8A.A1.E5.99.A8-ipv6-.E7.9A.84.E8.BF.9E.E9.80.9A.E6.80.A7)。

<span id="CentOS6.8"/>

#### CentOS 6.8 配置 IPv6
1. 远程连接实例。具体操作，请参见 [连接 Linux 实例](https://cloud.tencent.com/document/product/213/17278)。
2. 检查实例是否已开启 IPv6 服务，执行如下命令：
```
ip addr | grep inet6
或者
ifconfig | grep inet6
```
 - 若实例未开启 IPv6 服务，请根据下文继续开启 IPv6 服务。 
 - 若返回`inet6`相关内容，表示实例已成功开启 IPv6 服务，您可以跳至 [第9步](#step9) 继续操作。
3. 执行如下命令，打开`/etc/modprobe.d/`文件夹下的`ipv6.conf`文件。
```
vi /etc/modprobe.d/ipv6.conf
```
4. 按 “i” 切换至编辑模式，将如下的内核参数设置为0。
```
options ipv6 disable=0
```
![](https://main.qcloudimg.com/raw/37a4754fd0a8f6192d5f3818bcd685fe.png)
5.  按 “Esc”，输入 “:wq”，保存文件并返回。
6.  执行如下命令，打开`etc`文件夹下的`sysctl.conf.first`文件。
```
vim /etc/sysctl.conf.first
```
7. 按 “i” 切换至编辑模式，将如下的配置文件参数设置为0。
```
net.ipv6.conf.all.disable_ipv6 = 0
```
![](https://main.qcloudimg.com/raw/e5faf656a6aa6fcbd8a4ac190a13759e.png)
8. 按 “Esc”，输入 “:wq”，保存文件并返回。
9. <span id="step9" />执行如下命令，打开`/etc/sysconfig/`文件夹下的`network`文件。
```
vi /etc/sysconfig/network
```
10. 按 “i” 切换至编辑模式，增加如下内容。
```
NETWORKING_IPV6=yes
DHCPV6C=yes
```
![](https://main.qcloudimg.com/raw/477077b3418849b62dc7479df9839859.png)
11. 按 “Esc”，输入 “:wq”，保存文件并返回。
12. 执行如下命令，打开或创建`/etc/sysconfig/network-scripts/`文件夹下的`route6-eth0`文件。
```
vim /etc/sysconfig/network-scripts/route6-eth0
```
13. 按 “i” 切换至编辑模式，增加如下内容，为网卡的 IPv6 添加默认出口。
```
default dev eth0
```
![](https://main.qcloudimg.com/raw/7bac4ad80fed5cebcdef1fb6ae07cf1b.png)
14. 按 “Esc”，输入 “:wq”，保存文件并返回。
15. 重启云服务器，仅通过 `service network restart`，IPv6 无法正常加载。
16. 执行如下命令查看重启后 IPv6 是否已经正常加载。
```
sysctl -a | grep ipv6 | grep disable
```
![](https://main.qcloudimg.com/raw/866730d160b1f0b893b2c00cd0cb4257.png)
17. 依次执行如下命令，查看是否已经获取到 IPv6 地址。
```
dhclient -6
ifconfig
```
![](https://main.qcloudimg.com/raw/cedd7cbd7f5e649c01345356fa0d2688.png)
18. 执行如下命令，打开 `/etc/ssh/`文件夹下的`sshd_config`文件。
```
vim /etc/ssh/sshd_config
```
19. 按 “i” 切换至编辑模式，删除对`AddressFamily any`的注释（即删除前面的`#`），为 ssh 等应用程序开启 IPv6 监听。
![](https://main.qcloudimg.com/raw/e0d64e3836b704bab4713697df865d81.png)
20. 按 “Esc”，输入 “:wq”，保存文件并返回。
21. 执行如下命令，重启 ssh 进程。
```
service sshd restart
```
22. 执行如下命令，查看 ssh 是否已经监听 IPv6。
```
netstat -tupln
```
![](https://main.qcloudimg.com/raw/4b3937053527ea3edd3efedfa0113ca9.png)
23. 测试连通性，请参见 [测试 Linux 云服务器 IPv6 的连通性](#.E9.99.84.E5.BD.95.EF.BC.9A.E6.B5.8B.E8.AF.95-linux-.E4.BA.91.E6.9C.8D.E5.8A.A1.E5.99.A8-ipv6-.E7.9A.84.E8.BF.9E.E9.80.9A.E6.80.A7)。

<span id="CentOS7.3"/>

#### CentOS 7.3/存量 CentOS 7.5/存量 CentOS 7.6 配置 IPv6
1. 远程连接实例。具体操作，请参见 [连接 Linux 实例](https://cloud.tencent.com/document/product/213/17278)。
2. 检查实例是否已开启 IPv6 服务，执行如下命令：
```
ip addr | grep inet6
或者
ifconfig | grep inet6
```
 - 若实例未开启 IPv6 服务，请根据下文继续开启 IPv6 服务。 
 - 若返回`inet6`相关内容，表示实例已成功开启 IPv6 服务，您可以跳至 [第8步](#step8) 继续操作。
3. 执行如下命令，打开`etc`文件夹下的`sysctl.conf`文件。
```
vim /etc/sysctl.conf
```
4. 按 “i” 切换至编辑模式，将如下的 IPv6 相关参数设置为0。
```
net.ipv6.conf.all.disable_ipv6 = 0
net.ipv6.conf.default.disable_ipv6 = 0
net.ipv6.conf.lo.disable_ipv6 = 0
```
![](https://main.qcloudimg.com/raw/dc1e37e0c3a89b170038ef28d6d0583d.png)
5. 按 “Esc”，输入 “:wq”，保存文件并返回。
6. 执行如下命令，对参数进行加载。
```
sysctl -p
```
7. 执行如下命令，查看是否修改成功。
```
sysctl -a | grep ipv6 | grep disable
```
显示结果如下，则已成功修改。
![](https://main.qcloudimg.com/raw/b1294c92045d0dc5c688c6afc970a412.png)
8. <sapn id="step8" />执行如下命令，打开或创建`/etc/sysconfig/network-scripts/`文件夹下的`ifcfg-eth0`文件。
```
vim /etc/sysconfig/network-scripts/ifcfg-eth0
```
9. 按 “i” 切换至编辑模式，增加如下内容。
```
DHCPV6C=yes
```
![](https://main.qcloudimg.com/raw/7eb7d1dbf6e9773ca3282979587d4f55.png)
10. 按 “Esc”，输入 “:wq”，保存文件并返回。
11. 执行如下命令，打开或创建`/etc/sysconfig/network-scripts/`文件夹下的`route6-eth0`文件。
```
vim /etc/sysconfig/network-scripts/route6-eth0
```
12. 按 “i” 切换至编辑模式，增加如下内容，为网卡的 IPv6 添加默认出口。
```
default dev eth0
```
![](https://main.qcloudimg.com/raw/88a185a9dec922e4142c8ad8ffe4a354.png)
13. 按 “Esc”，输入 “:wq”，保存文件并返回。
14. 执行如下命令，重新启动网卡。
```
service network restart
或者
systemctl restart network
```
15. 依次执行如下命令，查看是否已经获取到 IPv6 地址。
```
dhclient -6
ifconfig
```
![](https://main.qcloudimg.com/raw/2e42f1a5e7b9672d60461fe05edfed52.png)
16. 执行如下命令，打开 `/etc/ssh/`文件夹下的`sshd_config`文件。
```
vim /etc/ssh/sshd_config
```
17. 按 “i” 切换至编辑模式，删除对`AddressFamily any`的注释（即删除前面的`#`），为 ssh 等应用程序开启 IPv6 监听。
![](https://main.qcloudimg.com/raw/e0d64e3836b704bab4713697df865d81.png)
18. 按 “Esc”，输入 “:wq”，保存文件并返回。
19. 执行如下命令，重启 ssh 进程。
```
service sshd restart
```
20. 执行如下命令，查看 ssh 是否已经监听 IPv6。
```
netstat -tupln
```
![](https://main.qcloudimg.com/raw/4b3937053527ea3edd3efedfa0113ca9.png)
21. 测试连通性，请参见 [测试 Linux 云服务器 IPv6 的连通性](#.E9.99.84.E5.BD.95.EF.BC.9A.E6.B5.8B.E8.AF.95-linux-.E4.BA.91.E6.9C.8D.E5.8A.A1.E5.99.A8-ipv6-.E7.9A.84.E8.BF.9E.E9.80.9A.E6.80.A7)。
<span id="Debian8.2"/>

#### Debian 8.2 配置 IPv6
1. 远程连接实例。具体操作，请参见 [连接 Linux 实例](https://cloud.tencent.com/document/product/213/17278)。
2. 检查实例是否已开启 IPv6 服务，执行如下命令：
```
ip addr | grep inet6
或者
ifconfig | grep inet6
```
 - 若实例未开启 IPv6 服务，请根据下文继续开启 IPv6 服务。 
 - 若返回`inet6`相关内容，表示实例已成功开启 IPv6 服务，您可以跳至 [第6步](#step6) 继续操作。
3. 执行如下命令，打开`etc`文件夹下的`sysctl.conf`。
```
vim /etc/sysctl.conf
```
4. 按 “i” 切换至编辑模式，将如下的 IPv6 相关参数设置为0。
```
net.ipv6.conf.all.disable_ipv6 = 0
net.ipv6.conf.default.disable_ipv6 = 0
```
5. 按 “Esc”，输入 “:wq”，保存文件并返回。
6. <span id="step6" />执行如下命令，对参数进行加载。
```
sysctl -p
```
7. 依次执行如下命令，查看是否已经获取到 IPv6 地址。
```
dhclient -6
ifconfig
```
![](https://main.qcloudimg.com/raw/cd5a2072c73307c79b7997bbd24cec13.png)
8. Debian 8.2 系统默认为 ssh（22端口）开启 IPv6 监听，无需特殊配置，您可执行如下命令，进行查看。
```
netstat -tupln
```
![](https://main.qcloudimg.com/raw/8bdb6f9672f81d8a6df56b61418fe492.png)
9. 执行如下命令，配置默认路由。
```
ip -6 route add default dev eth0
```
10. 测试连通性，请参见 [测试 Linux 云服务器 IPv6 的连通性](#.E9.99.84.E5.BD.95.EF.BC.9A.E6.B5.8B.E8.AF.95-linux-.E4.BA.91.E6.9C.8D.E5.8A.A1.E5.99.A8-ipv6-.E7.9A.84.E8.BF.9E.E9.80.9A.E6.80.A7)。

#### 附录：测试 Linux 云服务器 IPv6 的连通性
可通过 Ping 和 ssh 等操作来测试 Linux 云服务器 IPv6 的连通性。
- **步骤1：**通过 Ping 进行测试，操作如下：
 - 如果弹性网卡的 IPv6 地址已开通公网，则可在云服务器中执行 `ping6 240c::6666` 或 `ping6 www.qq.com`进行测试，如下图所示：
![](https://main.qcloudimg.com/raw/6202b3ebe7e946884d0342d6ec2ca16d.png)
 - 如果弹性网卡的 IPv6 地址未开通公网，则可在云服务器中 Ping 同一私有网络下的另一台云服务器的 IPv6 地址进行测试，如下图所示：
![](https://main.qcloudimg.com/raw/da1521a5885aeb8ddbe7f593033aae56.png)
- **步骤2：**从公网 IPv6 地址 ssh 云服务器，操作如下：
执行如下命令查看 IPv6 地址，并用 PuTTY 或者 Xshell 等软件，测试能否通过 IPv6 地址 ssh 到云服务器。
```
ifconfig
```
![](https://main.qcloudimg.com/raw/16838301e15e59ec20f8d3ffb1dd5a69.png)
成功结果如下图所示：
![](https://main.qcloudimg.com/raw/c951d48a32b010d00b481ed26082a1bb.png)

## Windows 云服务器配置 IPv6
如下操作以 Windows 2012 为例： 
1. 登录云服务器实例，进入操作系统的【控制面板】>【网络和 Internet】>【网络和共享中心】，单击命名为“以太网”的网卡进行编辑。
![](https://main.qcloudimg.com/raw/4696aa941df5c22dbf4446c01aabefbc.png)
2. 在“以太网状态”弹窗中，单击【属性】。
3. 在“以太网属性”弹窗中，选中【Internet 协议版本 6（TCP/IPv6）】并单击【属性】。
![](https://main.qcloudimg.com/raw/1f10d494b792d975a387ec6e38555021.png)
4. 在“Internet 协议版本 6（TCP/IPv6）属性”弹窗中，手工输入云服务器的 IPv6 地址并设置 DNS，单击【确定】。
>?查询云服务器的 IPv6 地址：可登录 [弹性网卡控制台](https://console.cloud.tencent.com/vpc/eni?rid=1)，单击对应云服务器所绑定弹性网卡的 ID，进入详情页，选择【IPv6 地址管理】标签页进行查看。
>
![](https://main.qcloudimg.com/raw/fac63249f22197686d68e3afffb3eb14.png)
5. 在操作系统界面，选择左下角的<img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:-3px 0px;width:25px">，单击 <img src="https://main.qcloudimg.com/raw/f0c84862ef30956c201c3e7c85a26eec.png" style="margin: -3px 0px;">，打开 “Windows PowerShell” 窗口，依次执行如下命令配置默认路由以及查看 IPv6 地址，并通过 Ping 和远程桌面测试 IPv6 连通性。
```
netsh interface ipv6 add route ::/0 "以太网"
ipconfig
```
![](https://main.qcloudimg.com/raw/eec1e647837d6b096ef9e022c3bafa7e.png)


