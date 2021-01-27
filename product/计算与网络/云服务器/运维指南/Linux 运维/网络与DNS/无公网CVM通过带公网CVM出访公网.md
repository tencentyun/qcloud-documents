## 操作场景
在选购云服务器时，若您选择了0Mbps带宽上限，则该云服务器将无法访问公网。本文以 CentOS7.5 为例，介绍如何在无公网 IP 的云服务器上通过 PPTP VPN 连接有公网 IP 的云服务器访问公网。


## 前提条件
- 已在同一个私有网络下创建两台云服务器（一台**无公网 IP 的云服务器**和一台**有公网 IP 的云服务器**）。
- 已获取有公网 IP 的云服务器的内网 IP。

## 操作步骤
### 在有公网 IP 的云服务器上配置 PPTP

1. 登录有公网 IP 的云服务器。
2. 执行以下命令，安装 PPTP。
```
yum install -y pptpd
```
2. 执行以下命令，打开 `pptpd.conf`  配置文件。
```
vim /etc/pptpd.conf
```
3. 按 **i** 切换至编辑模式，并在文件尾部添加以下内容。
```
localip 192.168.0.1
remoteip 192.168.0.234-238,192.168.0.245
```
4. 按 **Esc**，输入 **:wq**，保存文件并返回。
5. 执行以下命令，打开 `/etc/ppp/chap-secrets` 配置文件。
```
vim /etc/ppp/chap-secrets
```
6. <span id="step7">按 **i** 切换至编辑模式，并按以下格式，在文件尾部添加连接 PPTP 的用户名和密码。</span>
```
用户名    pptpd    密码    *
```
例如，连接 PPTP 的用户名为 root，登录密码为123456，则需要添加的信息如下：
```
root    pptpd    123456    *
```
7. 按 **Esc** ，输入 **:wq**，保存文件并返回。
8. 执行以下命令，启动 PPTP 服务。
```
systemctl start pptpd
```
9. 依次执行以下命令，启动转发能力。
```
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -t nat -A POSTROUTING -o eth0 -s 192.168.0.0/24 -j MASQUERADE
```

### 在无公网 IP 的云服务器上配置 PPTP

1. 登录无公网 IP 的云服务器。
2. 执行以下命令，安装 PPTP 客户端。
```
yum install -y pptp pptp-setup
``` 
3. 执行以下命令，创建配置文件。
```
pptpsetup --create 配置文件的名称 --server 有公网 IP 的云服务器的内网 IP --username 连接 PPTP 的用户名 --password 连接 PPTP 的密码 --encrypt
```
例如，创建一个 test 配置文件，已获取有公网 IP 的云服务器的内网 IP 为10.100.100.1，则执行以下命令：
```
pptpsetup --create test --server 10.100.100.1 --username root --password 123456 --encrypt
```
4. 执行以下命令，连接 PPTP。
```
pppd call test（为步骤3创建的配置文件名称）
```
5. 依次执行以下命令，设置路由。
```
route add -net 10.0.0.0/8 dev eth0
route add -net 172.16.0.0/12 dev eth0
route add -net 192.168.0.0/16 dev eth0
route add -net 169.254.0.0/16 dev eth0
route add -net 9.0.0.0/8 dev eth0
route add -net 100.64.0.0/10 dev eth0
route add -net 0.0.0.0 dev ppp0
```

### 检查配置是否成功
在无公网 IP 的云服务器上，执行以下命令，PING 任意一个外网地址，检查是否可以 PING 通。
```
ping -c 4 外网地址
```
若返回类似如下结果，则表示配置成功：
![](https://main.qcloudimg.com/raw/c841782ce0976982d1f289d3437ec0ed.png)



