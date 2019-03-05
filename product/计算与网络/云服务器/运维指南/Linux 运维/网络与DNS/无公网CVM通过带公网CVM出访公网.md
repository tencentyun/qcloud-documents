在选购 CVM 时若选择了 0Mbps 带宽，该服务器将无法访问公网。此类 CVM 必须通过一个带公网 IP 的 CVM 才能访问公网。
## 概述
无公网 IP 的 CVM 欲通过带公网 IP 的 CVM 访问公网，可以使用 PPTP VPN 来实现这一目标。即无公网 IP 的 CVM，通过 PPTP 协议与带公网 IP 的 CVM 连接起来，并且在 PPTP 网络中，将带公网 IP 的 CVM 设置为网关。

## 配置

### 步骤一：对带公网 IP 的 CVM 进行配置
1.  安装 pptpd。以 CentOS 为例（其它 Linux 发行版类似），执行以下命令：
```
yum install pptpd
```
2. 修改配置文件`/etc/pptpd.conf`，在文件尾部添加以下两行内容：
```
localip 192.168.0.1
remoteip 192.168.0.234-238,192.168.0.245
```
3. 修改配置文件`/etc/ppp/chap-secrets`，在文件尾部按指定格式添加用户名和密码信息（第一列表示用户名，第三列表示密码，* 表示对任何 IP ）。
```
用户名    pptpd   密码    *
```
**示例：**
假设带公网 IP 的 CVM 用户名为 root，登录密码为 123456AA，则需要添加的信息为
```
root pptpd 123456AA *
```
4. 启动服务。键入以下命令：
```
service pptpd start
```
5. 启动转发能力。键入以下命令：
```
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -t nat -A POSTROUTING -o eth0 -s 192.168.0.0/24 -j MASQUERADE
```

### 步骤二：对无公网 IP 的 CVM 进行配置
1. 安装客户端。以 CentOS 为例（其它 Linux 发行版类似），执行以下命令：
```
yum install pptp pptp-setup
``` 
2. 创建配置文件。
```
pptpsetup --create pptp --server A机器内网IP --username 用户名 --password 密码 --encrypt
```
**示例：**
假设带公网 IP 的 CVM 内网 IP 为 10.10.10.10，无公网 IP 的 CVM 用户名为 root，密码为 123456AA，则创建配置文件的命令为：
```
pptpsetup --create pptp --server 10.10.10.10 --username root --password 123456AA --encrypt
```
3. 连接 pptpd。键入以下命令：
```
pppd call pptp
```
4. 设置路由。依次键入以下命令：
```
route add -net 10.0.0.0/8 dev eth0
route add -net 172.16.0.0/12 dev eth0
route add -net 192.168.0.0/16 dev eth0
route add -net 0.0.0.0 dev ppp0
```

### 步骤三：确认配置成功
完成以上步骤之后，使用无公网 IP 的 CVM 去 PING 任意一个外网地址，若能 PING 通，说明配置成功。

## 说明
无公网 IP 的 CVM，通过带公网 IP 的 CVM 访问公网，除了使用 PPTP VPN 方式外，还可以通过在带公网 IP 的 CVM 上开通代理来实现。
代理方式配置简单，但使用起来较复杂，建议使用上述 PPTP VPN 方法来实现这一目标。 
