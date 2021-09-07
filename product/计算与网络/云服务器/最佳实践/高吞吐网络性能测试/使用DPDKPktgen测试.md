## 操作场景
本文档介绍如何通过 DPDK-Pktgen 方法进行云服务器高吞吐网络性能测试。


## 示例软件版本
本文测试机器使用 CentOS 8.2 操作系统。

## 操作步骤

### 测试机准备
1. 准备2台测试机器，请参见 [自定义配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/10517) 购买测试机器。
2. 依次登录测试机器，并根据以下步骤配置测试机环境。如何登录云服务器，请参见 [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。

### 编译安装 DPDK 
1. 依次执行以下命令，下载及解压 DPDK 安装包。
```
wget -O dpdk.tar.gz http://git.dpdk.org/dpdk/snapshot/dpdk-20.08.tar.gz
``` ```
mkdir -p /root/dpdk && tar -xf dpdk.tar.gz -C /root/dpdk --strip-components 1
```
2. 依次执行以下命令，安装 kernel-headers、numa、pcap 库和 patch 组件。
```
dnf upgrade
``` ```
dnf --enablerepo=powertools install libpcap-devel
``` ```shell
yum install numactl-devel patch python3 -y
``` ```shell
yum install kernel-headers
```
3. 依次执行以下命令，设置 DPDK 所需的环境变量。
```
export RTE_SDK=/root/dpdk
``` ```
export RTE_TARGET=x86_64-native-linuxapp-gcc
```
4. 对应实际操作系统版本或内核版本，执行以下命令。
 - 若您使用了 CentOS 8 操作系统，则执行以下命令，屏蔽 gcc 版本差异。
```
sed -i "s/\(^WERROR_FLAGS += -Wno-address-of-packed-member$\)/#\1/g" /root/dpdk/mk/toolchain/gcc/rte.vars.mk	
```
 - 若您的操作系统内核版本较高（例如5.3），则执行以下命令，屏蔽差异。
```
sed -i "s/\(^WERROR_FLAGS += -Wundef -Wwrite-strings$\)/\1 -Wno-address-of-packed-member/g" ./mk/toolchain/gcc/rte.vars.mk
``` ```
sed -i "s/fall back/falls through -/g" ./lib/librte_eal/linuxapp/igb_uio/igb_uio.c
```
5. 执行以下命令，编译安装 DPDK。
```
cd $RTE_SDK && make install T=x86_64-native-linuxapp-gcc -j 4
```

### 编译安装 Pktgen
1. 执行以下命令，下载及解压 Pktgen 安装包。
```
wget -O pktgen.tar.gz  http://git.dpdk.org/apps/pktgen-dpdk/snapshot/pktgen-dpdk-pktgen-20.02.0.tar.gz
``` ```
mkdir -p /root/pktgen && tar -xf pktgen.tar.gz -C /root/pktgen --strip-components 1
```
2. 依次执行以下命令，下载并安装 lua 及其所需组件。
```shell
yum install libtermcap-devel ncurses-devel libevent-devel readline-devel -y
``` ```
cd /root/pktgen/lib/lua
``` ```
wget https://www.lua.org/ftp/lua-5.3.4.tar.gz
``` ```
make linux
``` ```
make install
```
3. 执行以下命令，编译安装 Pktgen。
```
cd /root/pktgen && make
```


### 编辑配置文件
参考以下步骤，编辑 `test_range.lua` 及 `default.cfg` 配置文件。

<dx-accordion>
::: test_range.lua 文件
参考以下 `test_range.lua` 示例，结合实际情况编辑 `/root/pktgen/test/test_range.lua` 文件，修改 Pktgen 测试 rang 模式报文特征，生成100条流。
```
package.path = package.path ..";?.lua;test/?.lua;app/?.lua;"

--pktgen.page("range");

-- 配置 Port 0 MAC
-- Port 0 3c:fd:fe:9c:5c:d8,  Port 1 3c:fd:fe:9c:5c:b8
pktgen.range.dst_mac("0", "start", "52:54:00:51:e5:28");-- 填写接收端网卡MAC
pktgen.range.src_mac("0", "start", "52:54:00:c1:55:3d");-- 填写发送端网卡MAC

-- Port 0 接收端IP地址
pktgen.range.dst_ip("0", "start", "172.16.0.11");
pktgen.range.dst_ip("0", "inc", "0.0.0.0");
pktgen.range.dst_ip("0", "min", "172.16.0.11");
pktgen.range.dst_ip("0", "max", "172.16.0.11");

-- Port 0 发送端IP地址
pktgen.range.src_ip("0", "start", "172.16.0.9");
pktgen.range.src_ip("0", "inc", "0.0.0.0");
pktgen.range.src_ip("0", "min", "172.16.0.9");
pktgen.range.src_ip("0", "max", "172.16.0.9");

-- Port 0 流量目的端口范围
pktgen.range.dst_port("0", "start", 2013);
pktgen.range.dst_port("0", "inc", 1);
pktgen.range.dst_port("0", "min", 2013);
pktgen.range.dst_port("0", "max", 10113);

-- Port 0 流量接收端口范围
pktgen.range.src_port("0", "start", 5029);
pktgen.range.src_port("0", "inc", 1);
pktgen.range.src_port("0", "min", 5029);
pktgen.range.src_port("0", "max", 7129);

-- Port 0 测试流量的包长
pktgen.range.pkt_size("0", "start", 64);
pktgen.range.pkt_size("0", "inc", 0);
pktgen.range.pkt_size("0", "min", 64);
pktgen.range.pkt_size("0", "max", 256);

-- Set up second port
-- pktgen.range.dst_mac("1", "start", "3c:fd:fe:9c:5c:d8");
-- pktgen.range.src_mac("1", "start", "3c:fd:fe:9c:5c:b8");

-- pktgen.range.dst_ip("1", "start", "192.168.0.1");
-- pktgen.range.dst_ip("1", "inc", "0.0.0.1");
-- pktgen.range.dst_ip("1", "min", "192.168.0.1");
-- pktgen.range.dst_ip("1", "max", "192.168.0.128");

-- pktgen.range.src_ip("1", "start", "192.168.1.1");
-- pktgen.range.src_ip("1", "inc", "0.0.0.1");
-- pktgen.range.src_ip("1", "min", "192.168.1.1");
-- pktgen.range.src_ip("1", "max", "192.168.1.128");

-- pktgen.set_proto("all", "udp");

-- pktgen.range.dst_port("1", "start", 5000);
-- pktgen.range.dst_port("1", "inc", 1);
-- pktgen.range.dst_port("1", "min", 5000);
-- pktgen.range.dst_port("1", "max", 7000);

-- pktgen.range.src_port("1", "start", 2000);
-- pktgen.range.src_port("1", "inc", 1);
-- pktgen.range.src_port("1", "min", 2000);
-- pktgen.range.src_port("1", "max", 4000);

-- pktgen.range.pkt_size("1", "start", 64);
-- pktgen.range.pkt_size("1", "inc", 0);
-- pktgen.range.pkt_size("1", "min", 64);
-- pktgen.range.pkt_size("1", "max", 256);

-- Port 0 测试流量的协议类型  udp/tcp/icmp
pktgen.set_proto("0", "udp");
pktgen.ip_proto("0", "udp");
pktgen.set_range("all", "on");
```
相关信息获取途径如下：
- **网卡 MAC 地址**：可执行 `ifconfig -a` 命令获取，其中 `ether` 字段为网卡 Mac 地址。
- **接收端\发送端 IP 地址**：测试机的内网 IP 地址，获取方式请参见 [获取实例的内网 IP 地址](https://cloud.tencent.com/document/product/213/17941#.E8.8E.B7.E5.8F.96.E5.AE.9E.E4.BE.8B.E7.9A.84.E5.86.85.E7.BD.91-ip-.E5.9C.B0.E5.9D.80)。
:::
::: default.cfg
参考以下 `default.cfg` 示例，结合实际情况编辑 `/root/pktgen/cfg/default.cfg`。配置测试网卡、收发包 CPU，指定使用 range 模式的测试报文配置文件。

```plaintext
description = 'A Pktgen default simple configuration'

# Setup configuration
setup = {
    'exec': (
        'sudo',
        '-E'
        ),

	'devices': (
		'0000:00:07.0' #请结合实际情况填写
		),
		
	'opts': (
		'uio_pci_generic'
		)
	}

# Run command and options
run = {
    'exec': (
        'sudo',
        '-E'
        ),

    # Application name and use app_path to help locate the app
    'app_name': 'pktgen',

    # using (sdk) or (target) for specific variables
    # add (app_name) of the application
    # Each path is tested for the application
    'app_path': (
        './app/%(target)s/%(app_name)s',
        '%(sdk)s/%(target)s/app/%(app_name)s',
        ),

	'dpdk': (
		'-l 8,9-24', #请结合实际情况填写
		'-n 4',
		'--proc-type auto',
		'--log-level 7',
		'--socket-mem 2048,2048',
		'--file-prefix pg',
		'-w 00:05.0'
		),
	
	'blacklist': (
		#'-b 81:00.0 -b 81:00.1 -b 81:00.2 -b 81:00.3',
		#'-b 85:00.0 -b 85:00.1 -b 85:00.2 -b 85:00.3',
		#'-b 81:00.0 -b 81:00.1',
		#'-b 85:00.0 -b 85:00.1',
		),
		
	'app': (
		'-T',
		'-P',
		'--crc-strip',
		'-m [9-12:9-12].0', #请结合实际情况填写
		#'-m [17:18].1',
		#'-m [19:20].2',
		#'-m [21:22].3'
		),
	
	'misc': (
		#'-f', 'themes/black-yellow.theme'
		'-f', 'test/test_range.lua' #请结合实际情况填写
		)
	}

```
:::
</dx-accordion>

### 配置大页内存
执行以下命令，配置大页内存。
```
echo 2048 > /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages
```
若出现报错信息，则说明大页内存不足，可调整命令配置。例如：
```
echo 4096 > /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages
```

### 装载内核模块及绑定接口
1. 切换登录方式为 [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701)。由于将网卡驱动绑定至 igb_uio 用户态驱动后，该网卡将无法通过 ssh 或 IP 访问，仅支持通过 VNC 或 console 方式访问。
2. 依次执行以下命令，装载 UIO 模块及绑定 virito 接口。
```
ifconfig eth0 0
``` ```
ifconfig eth0 down
``` ```
modprobe uio
``` ```
insmod /root/dpdk/build/kmod/igb_uio.ko
``` ```
cd /root/dpdk/usertools/
``` ```
python3 dpdk-devbind.py --bind=igb_uio 00:05.0
``` <dx-alert infotype="explain" title="">
命令中的 00.05.0 为示例地址，请执行 `python3 dpdk-devbind.py -s` 命令，获取网卡实际地址。
</dx-alert>
完成测试后，可通过请执行以下命令，恢复网卡变更。
```
cd /root/dpdk/usertools/
``` ```
python3 dpdk-devbind.py --bind=virtio-pci 00:05.0
``` ```
ifconfig eth0 up
```

### DPDK-Pktgen 单向流量测试
测试场景如下图所示：
![](https://main.qcloudimg.com/raw/88116c6e3625696e0935f3238671ae4c.png)
- 发送端执行以下命令：
```
/root/pktgen/tools/dpdk-run.py -s default
``` ```
/root/pktgen/tools/dpdk-run.py default
``` 启动发包时执行以下命令。```
Pktgen:/> str
``` 终止发包时执行以下命令。```
Pktgen:/> stp
```
- 接收端执行以下命令：
```
/root/dpdk/x86_64-native-linuxapp-gcc/app/testpmd -- --txd=128 --rxd=128 --txq=48 --rxq=48 --nb-cores=16 --forward-mode=rxonly --stats-period=1
```

### DPDK-Pktgen 双向流量测试
测试场景如下图所示：
![](https://main.qcloudimg.com/raw/52aae97e5bf29eee4873479d19158512.png)
- 发送端执行以下命令：
```
/root/pktgen/tools/dpdk-run.py -s default
``` ```
/root/pktgen/tools/dpdk-run.py default
``` 启动发包时执行以下命令。```
Pktgen:/> str
``` 终止发包时执行以下命令。```
Pktgen:/> stp
```
- 接收端执行以下命令：
```
/root/dpdk/x86_64-native-linuxapp-gcc/app/testpmd -- --txd=128 --rxd=128 --txq=48 --rxq=48 --nb-cores=16 --forward-mode=5tswap --stats-period=1
```

