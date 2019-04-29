当云服务器选择了0Mbps带宽时，无法访问公网。这些云服务器必须经过一个带公网IP的CVM才能访问外网。

## 1. 原理

- 无公网IP的云服务器CVM，通过带公网IP的CVM访问公网，可以在带公网IP的CVM上开通代理或者vpn的方式。
- 代理方式配置简单，但使用起来较复杂，建议使用pptp vpn来实现这一目标。（即无公网IP的CVM，通过pptp协议与带公网IP的CVM连接起来，并且在pptp网络中，将带公网IP的CVM设置为网关）

## 2. 配置
假设带公网IP的CVM为A，无公网IP的CVM为B。

1) 在A上安装pptpd，以CentOS为例（其它Linux发行版类似），运行以下命令：

```
yum install pptpd
```

2) 修改配置文件`/etc/pptpd.conf`，添加以下两行

```
localip 192.168.0.1
remoteip 192.168.0.234-238,192.168.0.245
```

3) 修改配置文件`/etc/ppp/chap-secrets`，添加用户名和密码（第一列表示用户名，第三列表示密码）

```
user    pptpd   pass    *
```

4) 启动服务

```
service pptpd start
```

5) 启动转发能力

```
# echo 1 > /proc/sys/net/ipv4/ip_forward
# iptables -t nat -A POSTROUTING -o eth0 -s 192.168.0.0/24 -j MASQUERADE
```

6) 在B上安装客户端，以CentOS为例，运行以下命令：

```
# yum install pptp pptp-setup
```

7) 创建配置文件

```
# pptpsetup --create pptp --server 10.10.10.10 --username user --password pass --encrypt
```

**注意：`--server`后面是A的IP地址。**

8) 连接pptpd

```
# pppd call pptp
```

9) 设置路由：

```
# route add -net 10.0.0.0/8 dev eth0
# route add -net 172.16.0.0/12 dev eth0
# route add -net 192.168.0.0/16 dev eth0
# route add -net 0.0.0.0 dev ppp0
```

另外：如果B是Windows的CVM，可以通过新建“连接到工作区”的网络连接到pptpd服务器

