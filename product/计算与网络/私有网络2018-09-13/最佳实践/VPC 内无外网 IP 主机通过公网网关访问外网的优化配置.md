## 环境说明
客户在腾讯云 VPC 中的部分主机没有外网 IP，但需要访问外网时，可以购买公网网关主机，将这些主机作为其它没有外网 IP 的主机访问 Internet 的外网出口。公网网关主机将对出网流量进行源地址转换，所有其他主机访问外网的流量经过公网网关后，源 IP 都被转换为公网网关主机的 IP 地址，如下图所示：
![](//mccdn.qcloud.com/img56c6b95099539.png)

要完成上述架构，需要完成几个步骤，步骤流程如下图所示：
![](https://main.qcloudimg.com/raw/aa7665e70518225250d1a82a14eaa0d4.png)
## 架构搭建
### 创建网关子网
公网网关只能转发非所在子网的路由转发请求，因此，公网网关主机不能与需要借助公网网关访问外网的 CVM 处于同一个子网下，需要先建立一个独立的网关子网，详细操作步骤，请参见 [创建网关子网](https://cloud.tencent.com/document/product/215/20136)。
![](//mccdn.qcloud.com/img56c6bae35eb98.png)

### 购买公网网关
在刚刚创建好的网关子网下，购买公网网关，详细操作步骤，请参见 [购买公网网关](https://cloud.tencent.com/document/product/215/20137)。

### 创建网关子网路由表
网关子网和普通子网不能关联同一张路由表，需要新建一张独立的网关路由表，并网关子网关联该路由表，详细操作步骤，请参见 [创建网关子网路由表](https://cloud.tencent.com/document/product/215/20138)。
![](//mccdn.qcloud.com/img56c6bbdc8d197.png)
![](//mccdn.qcloud.com/img56c6bbe5752ab.png)

### 配置普通子网路由表
配置普通子网的路由表，配置默认路由走公网网关主机，使得普通子网内主机能通过公网网关的路由转发能力访问外网，详细操作步骤，请参见 [配置普通子网路由表](https://cloud.tencent.com/document/product/215/20139)。
![](//mccdn.qcloud.com/img56c6bc54c5dd6.png)

## 配置优化
公网网关主机会默认配置 iptables 的 NAT 规则，以及打开 kernel 的 ip_forward，基本的公网网关功能已经完全具备。建议经过下述配置，以达到更好的性能。
1. 通过以下命令将 net.ipv4.ip_forward 配置写到 /etc/sysctl.conf 文件中。
```
echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf
```
2. 通过以下命令将 nf_conntrack 配置参数调大。
```
echo "echo 1048576 > /proc/sys/net/netfilter/nf_conntrack_max" >> /etc/rc.local
echo "echo 262144 > /sys/module/nf_conntrack/parameters/hashsize" >> /etc/rc.local
```
3. 设置转发的 NAT 规则。
```
echo "iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE" >> /etc/rc.local
```
4. 关闭时间戳选项。
```
echo "iptables -t mangle -A POSTROUTING -p tcp -j TCPOPTSTRIP --strip-options timestamp" >> /etc/rc.local
```
5. 设置公网网关的 rps。
 在 /usr/local/sbin/ 目录下新建脚本 set_rps.sh，将以下代码写入脚本中：
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

完成上述配置后，重启公网网关主机使配置生效，并在无外网 IP 的子机上，测试是否能够成功访问外网。
