## 1. Environment Description

If you need to access the public network but the CVM on the Tencent Cloud VPC has no public IP, you can purchase a CVM with public network gateway as the public network egress during access to the Internet for the CVM without public IP. The public network gateway CVM will carry out source address translation for outbound traffic, and the source IP of traffic by all other CVMs accessing the public network is converted to the IP address of public network gateway CVM after passing through the public network gateway, as shown below:
![](https://mc.qcloudimg.com/static/img/c756ed0cfe20c76f071a93ce95a97f7c/VPC-Best+Practise.png)

Ordinary CVM has no public IP, but it can use the public network gateway to access the Internet.

Please perform several steps below to complete the above architecture.

## 2. Architecture Building
### 2.1. Creating a Gateway Subnet
The public network gateway can only forward the route forwarding request of the subnet to which it does not belong, so the public network gateway cannot be in the same subnet with the CVM which needs to access the public network through the public network gateway. Therefore, it is necessary to set up a separate gateway subnet first.

![](https://mc.qcloudimg.com/static/img/80a5ea57ab46f6b2e480d088d9929a93/Best_Allow_1.jpg)

### 2.2. Purchasing a Public Network Gateway
To purchase the public network gateway in the gateway subnet created above, please refer to Purchasing a VPC Public Network Gateway

### 2.3. Creating the Routing Table of Gateway Subnet
Gateway subnet and ordinary subnet cannot be associated with the same routing table. You need to create a separate gateway routing table and associate it with the gateway subnet.

![](https://mc.qcloudimg.com/static/img/1054ab93b8a0d73a5998778ce8ed0c8f/Best_Allow_2.jpg)
![](https://mc.qcloudimg.com/static/img/7f71e82a254b79893bcd54dad1d3ca0a/Best_Allow_3.jpg)

### 2.4. Configuring the Routing Table of Ordinary Subnet
Configure the routing table of the ordinary subnet, direct the default route to the public network gateway CVM, so that the CVM in ordinary subnet can access the public network through the route forwarding capability of public network gateway.
![](https://mc.qcloudimg.com/static/img/fb870aef1f90e75b7307a6b998f2121e/Best_Allow_4.jpg)

## 3. Configuration Optimization
Public network gateway CVM will set the nat rules of iptables by default, and open the kernel ip_forward. By then, all the basic functions public network gateway have been enabled. It is recommended to perform the following configuration to achieve better performance.

1) Write the net.ipv4.ip_forward configuration to the /etc/sysctl.conf file with the following command

```
echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf
```
2) Increase the nf_conntrack configuration parameter using the following command

```
echo "echo 1048576 > /proc/sys/net/netfilter/nf_conntrack_max" >> /etc/rc.local
echo "echo 262144 > /sys/module/nf_conntrack/parameters/hashsize" >> /etc/rc.local
```

3) Set the forwarding nat rules

```
echo "iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE" >> /etc/rc.local
```

4) Turn off the timestamp option

```
echo "iptables -t mangle -A POSTROUTING -p tcp -j TCPOPTSTRIP --strip-options timestamp" >> /etc/rc.local
```

5) Set the rps of public network gateway

Create a new script set_rps.sh in the directory of /usr/local/sbin/ and write the following code into the script:

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

Once created, execute the following command:

```
chmod +x /usr/local/sbin/set_rps.sh
echo "/usr/local/sbin/set_rps.sh" >> /etc/rc.local
```

After the above configuration, restart the public network gateway CVM to make the configuration valid, and test whether the submachine without public network IP can access the public network.
