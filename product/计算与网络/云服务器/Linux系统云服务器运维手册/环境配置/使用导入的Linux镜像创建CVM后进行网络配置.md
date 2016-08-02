导入Linux类型镜像并创建云服务器后，用户请通过[控制台云服务器列表](https://console.qcloud.com/cvm)后的【登录】按钮登录刚创建的云服务器并进行网络配置。

Linux机器网络配置信息保存在文件`/etc/qcloud-network-config.ini`中。打开该配置文件，结构如下：

```
[ip]
ip= x.x.x.x
mask = x.x.x.x
gateway = x.x.x.x
 
[dns]
dns = x.x.x.x
```

请用户根据此配置文件提供的linux静态IP和DNS IP，在云服务器上完成相应的网络配置，本例以CentOS机器为范例。

使用以下命令打开IP配置文件：

```
vi /etc/sysconfig/network-scripts/ifcfg-eth0
```

找到如下参数，进行修改：

```
DEVICE=eth0
ONBOOT=yes
BOOTPROTO=static
IPADDR=[配置文件中的ip参数]
NETMASK=[配置文件中的mask参数]
GATEWAY=[配置文件中的gateway参数]

```
使用以下命令使IP地址生效：

```
/sbin/ifdown eth0
/sbin/ifup eth0
```

使用以下命令配置dns解析：

```
echo "nameserver [配置文件中的dns参数]">> /etc/resolv.conf
```

使用以下命令通知网关更新信息：

```
/etc/init.d/network restart
```


