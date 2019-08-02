## 操作场景
在选购云服务器（CVM）时若选择了0Mbps带宽上限，该 CVM 将无法访问公网。本文以 CentOS7.5 为例，使用无公网 IP 的 CVM 通过 PPTP VPN 及有公网 IP 的 CVM 访问公网。


## 前提条件
- 已创建无公网 IP CVM 及有公网 IP CVM，详情请见 [创建实例](https://cloud.tencent.com/document/product/213/4855)。
- 已创建的 CVM 均在同一私有网络下，详情请见 [私有网络](https://cloud.tencent.com/document/product/215/20046)。

## 操作步骤
### 对有公网 IP 的 CVM 进行配置
1.  执行以下命令，安装 PPTP。
```
yum install -y pptpd
```
2. 执行以下命令，修改 PPTP 配置文件`pptpd.conf`。
```
vim /etc/pptpd.conf
```
3. 按 “**i**” 或 “**Insert**” 切换至编辑模式。
4. 在文件尾部匹配下列配置，并删除配置前的“**#**”。
```
#localip 192.168.0.1
#remoteip 192.168.0.234-238,192.168.0.245
```
修改完成后，按 “**Esc**” ，输入 “**:wq**”，保存文件并返回。
修改结果如下图所示：
![](https://main.qcloudimg.com/raw/fa81cf84881b63465866f3ecd753b445.png)
5. 执行以下命令，修改 PPTP 配置文件`/etc/ppp/chap-secrets`。
```
vim /etc/ppp/chap-secrets
```
6. 按 “**i**” 或 “**Insert**” 切换至编辑模式。
7. 在文件尾部按以下格式添加用户名和信息。
<span id="step7"></span>
```
用户名    pptpd    密码    *
```
例如，用户名为 user，密码为 123456，则需要添加信息为：
```
user    pptpd    123456    *
```
添加完成后，按 “**Esc**” ，输入 “**:wq**”，保存文件并返回。
添加信息成功后如下图所示：
![](https://main.qcloudimg.com/raw/28fc413cdd9d3234613806256dc34168.png)
8. 执行以下命令，启动服务。
```
systemctl start pptpd
```
9. 依次执行以下命令，启动转发能力。
```
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -t nat -A POSTROUTING -o eth0 -s 192.168.0.0/24 -j MASQUERADE
```

### 对无公网 IP 的 CVM 进行配置
1. 执行以下命令，安装客户端。
```
yum install -y pptp pptp-setup
``` 
2. 替换命令中以下参数信息并执行命令，创建配置文件 test，并启动连接。
 - 内网 IP：可在 [腾讯云服务器控制台](https://console.cloud.tencent.com/cvm) 中查看。如下图所示：
![](https://main.qcloudimg.com/raw/75db97912ba0170b1543fe6c404a06a9.png)
 - 用户名/密码： 为有公网 IP 的 CVM 配置 [步骤7](#step7) 中设置的用户名及密码。
```
pptpsetup --create test --server 内网IP --username 用户名 --password 密码 --encrypt --start
```
连接成功。如下图所示：
![](https://main.qcloudimg.com/raw/32f142c52fceb5a94b383c080475be87.png)
3. 依次执行以下命令，设置路由。
```
route add -net 10.0.0.0/8 dev eth0
route add -net 172.16.0.0/12 dev eth0
route add -net 192.168.0.0/16 dev eth0
route add -net 169.254.0.0/16 dev eth0
route add -net 9.0.0.0/8 dev eth0
route add -net 100.64.0.0/10 dev eth0
route add -net 0.0.0.0 dev ppp0
```

### 测试是否可访问公网
完成上述步骤之后，执行以下命令进行测试。
```
ping -c 4 www.cloud.tencent.com
```
测试成功。如下图所示：
![](https://main.qcloudimg.com/raw/c841782ce0976982d1f289d3437ec0ed.png)



