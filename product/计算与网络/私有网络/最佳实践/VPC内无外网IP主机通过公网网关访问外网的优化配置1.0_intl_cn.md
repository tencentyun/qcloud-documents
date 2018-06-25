## 1. 环境说明

客户在腾讯云 VPC 中的部分主机没有外网 IP 但需要访问外网时，可以通过购买公网网关主机作为其它没有外网IP的主机访问 Internet 的外网出口。公网网关主机将对出网流量进行源地址转换，所有其他主机访问外网的流量经过公网网关后，源 IP 都被转换为公网网关主机的 IP 地址，如下图：
<div style="text-align:center">
![](//mccdn.qcloud.com/img56c6b95099539.png)

</div>
普通 CVM 没有外网 IP，但是可以借助公网网关访问 Internet。

要完成上述架构，需要经过后文所述的几个步骤。

## 2. 架构搭建
### 2.1. 创建网关子网
由于公网网关只能转发非所在子网的路由转发请求，因此公网网关主机不能和需要借助公网网关访问外网的 CVM 处于同一个子网下，所以需要先建立一个独立的网关子网。
<div style="text-align:center">
![](//mccdn.qcloud.com/img56c6bae35eb98.png)

</div>
### 2.2. 购买公网网关
在刚刚创建好的网关子网下购买公网网关，详细步骤请见 <a href="http://cloud.tencent.com/doc/product/215/%E8%B4%AD%E4%B9%B0%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E7%9A%84%E5%85%AC%E7%BD%91%E7%BD%91%E5%85%B3" target="_blank">购买私有网络的公网网关</a>
### 2.3. 创建网关子网路由表
网关子网和普通子网不能关联同一张路由表，需要新建一张独立的网关路由表，且网关子网关联该路由表。
<div style="text-align:center">
![](//mccdn.qcloud.com/img56c6bbdc8d197.png)


</div>
<div style="text-align:center">
![](//mccdn.qcloud.com/img56c6bbe5752ab.png)

</div>
### 2.4. 配置普通子网路由表
配置普通子网的路由表，配置默认路由走公网网关主机，使得普通子网内主机能通过公网网关的路由转发能力访问外网。
<div style="text-align">
![](//mccdn.qcloud.com/img56c6bc54c5dd6.png)

</div>
## 3. 配置优化
公网网关主机会默认配置 iptables 的 NAT 规则，以及打开 kernel 的 ip_forward，基本的公网网关功能已经完全具备。建议经过下述配置，以达到更好的性能。

1) 通过以下命令将`net.ipv4.ip_forward`配置写到 `/etc/sysctl.conf`文件中

```
echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf
```
2) 通过以下命令将`nf_conntrack`配置参数调大

```
echo "echo 1048576 > /proc/sys/net/netfilter/nf_conntrack_max" >> /etc/rc.local
echo "echo 262144 > /sys/module/nf_conntrack/parameters/hashsize" >> /etc/rc.local
```

3) 设置转发的 NAT 规则

```
echo "iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE" >> /etc/rc.local
```

4) 关闭时间戳选项

```
echo "iptables -t mangle -A POSTROUTING -p tcp -j TCPOPTSTRIP --strip-options timestamp" >> /etc/rc.local
```

5) 设置公网网关的 RPS

在`/usr/local/sbin/`目录下新建脚本`set_rps.sh`，将以下代码写入脚本中：

```
#!/bin/bash
mask=0
i=0
cpu_nums=`cat /proc/cpuinfo |grep processor |wc -l`
if(($cpu_nums==0));then
	exit 0
fi

nic_queues=`cat /proc/interrupts |grep -i virtio0-input |wc -l`
if(($nic_queues==0));then
    exit 0
fi

echo "cpu number" $cpu_nums "nic queues" $nic_queues

mask=$(echo "obase=16;2^$cpu_nums - 1" |bc)
flow_entries=$(echo "$nic_queues * 4096" |bc)

echo "mask = "$mask
echo "flow_entries = "$flow_entries

#for i in {0..$nic_queues}
while (($i < $nic_queues))  
do
	echo $mask > /sys/class/net/eth0/queues/rx-$i/rps_cpus
	echo 4096 > /sys/class/net/eth0/queues/rx-$i/rps_flow_cnt
	i=$(($i+1)) 
done

echo $flow_entries > /proc/sys/net/core/rps_sock_flow_entries 

```

新建完成后执行以下命令：

```
chmod +x /usr/local/sbin/set_rps.sh
echo "/usr/local/sbin/set_rps.sh" >> /etc/rc.local
```

完成上述配置后，重启公网网关主机以使配置生效，并在无外网 IP 的子机上测试是否能够成功访问外网。