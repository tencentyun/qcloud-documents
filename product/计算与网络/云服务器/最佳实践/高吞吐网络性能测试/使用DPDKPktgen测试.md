## 操作场景
本文档介绍如何通过 DPDK-Pktgen 方法进行云服务器高吞吐网络性能测试。


## 示例软件版本
- 测试机器为 CentOS 8.2 操作系统
- DPDK 20.08
- Pktgen 20.03

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
sed -i "s/\(^WERROR_FLAGS += -Wundef -Wwrite-strings$\)/\1 -Wno-address-of-packed-member/g" /root/dpdk/mk/toolchain/gcc/rte.vars.mk
``` ```
sed -i "s/fall back/falls through -/g" /root/dpdk/kernel/linux/igb_uio/igb_uio.c
```
5. 执行以下命令，编译安装 DPDK。
```
cd $RTE_SDK && make install T=x86_64-native-linuxapp-gcc -j 4
```

### 编译安装 Pktgen
1. 执行以下命令，下载及解压 Pktgen 安装包。
```
cd && wget -O http://git.dpdk.org/apps/pktgen-dpdk/snapshot/pktgen-dpdk-pktgen-20.03.0.tar.gz
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
tar zxf lua-5.3.4.tar.gz
``` ```
cd lua-5.3.4 && make linux
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
参考以下 `test_range.lua` 示例，结合实际情况编辑 `/root/pktgen/test/test_range.lua` 文件，修改 Pktgen 测试 range 模式报文特征。本文以生成100条流为例，若您需修改生成流数目，可修改 `dst_port` 及 `src_port` 参数配置。
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
-- (max value - min value) 需等于流数目
pktgen.range.dst_port("0", "start", 2013);
pktgen.range.dst_port("0", "inc", 1);
pktgen.range.dst_port("0", "min", 2013);
pktgen.range.dst_port("0", "max", 2112);

-- Port 0 流量接收端口范围
-- (max value - min value) 需等于流数目
pktgen.range.src_port("0", "start", 5029);
pktgen.range.src_port("0", "inc", 1);
pktgen.range.src_port("0", "min", 5029);
pktgen.range.src_port("0", "max", 5128);

-- Port 0 测试流量的数据包属性
pktgen.range.pkt_size("0", "start", 64);
pktgen.range.pkt_size("0", "inc", 0);  -- 固定包长为64字节
pktgen.range.pkt_size("0", "min", 64);
pktgen.range.pkt_size("0", "max", 256);

-- Port 0 测试流量的协议类型  udp/tcp/icmp
pktgen.set_proto("0", "udp");
pktgen.ip_proto("0", "udp");
pktgen.set_range("all", "on");
```
相关说明如下：
- **网卡 MAC 地址**：可执行 `ifconfig -a` 命令获取，其中 `ether` 字段为网卡 Mac 地址。
- **接收端\发送端 IP 地址**：测试机的 IP 地址，可使用 [公网 IP](https://cloud.tencent.com/document/product/213/5224)。若机器再同一私有网络下，也可使用 [内网 IP](https://cloud.tencent.com/document/product/213/5225)。
:::
::: default.cfg
参考以下 `default.cfg` 示例，结合实际情况编辑 `/root/pktgen/cfg/default.cfg`，配置测试网卡地址、收发包 CPU、指定使用 range 模式的测试报文配置文件。

```plaintext
description = 'A Pktgen default simple configuration'

# Setup configuration
setup = {
    'exec': (
    'sudo', '-E'
        ),

    'devices': (
        '0000:00:07.0' # 测试网卡地址，请结合实际情况填写
        ),
    # UIO module type, igb_uio, vfio-pci or uio_pci_generic
    'uio': 'uio_pci_generic'
    }

# Run command and options
run = {
    'exec': (
    'sudo', '-E', 'LD_LIBRARY_PATH=%(sdk)s/%(target)s/lib/x86_64-linux-gnu'
        ),

    # Application name and use app_path to help locate the app
    'app_name': 'pktgen',

    # using (sdk) or (target) for specific variables
    # add (app_name) of the application
    # Each path is tested for the application
    'app_path': (
        './app/%(target)s/%(app_name)s',
        '%(sdk)s/%(target)s/app/%(app_name)s',
        './build/app/%(app_name)s',
        ),

    'cores': '0,1-3', # 填写 CPU ID，即绑定对应的 CPU 执行 Pktgen 。可通过 lscpu 命令查看 CPU ID，请结合实际情况填写
    'nrank': '4',
    'proc': 'auto',
    'log': '7',
    'prefix': 'pg',

    'blacklist': (
        #'03:00.0', '05:00.0',
        #'81:00.0', '84:00.0'
        ),
    'whitelist': (
        #'05:00.0,safe-mode-support=1',
        #'84:00.0,safe-mode-support=1',
        #'03:00.0', '81:00.0'
        '00:07.0' # 测试网卡地址，请结合实际情况填写
        ),

    'opts': (
        '-v',
        '-T',
        '-P',
        '-j',
        ),
    'map': (
        '[1-2:1-2].0', #  CPU ID 和网卡的绑定关系。格式为 [RX 各队列所绑定的 CPU ID：TX 队列所绑定的 CPU ID].PORT ID。CPU ID 需在上文中的 cores 指定，请结合实际情况填写。
        ),

    #'theme': 'themes/black-yellow.theme'
    'loadfile': 'test/test_range.lua' # 请结合实际情况填写
    }
```
相关说明如下：
- 可执行 `cd /root/dpdk/usertools/ && python3 dpdk-devbind.py -s` 命令，获取测试网卡实际地址。
- 其他参数配置可参考 [Runtime Options and Commands](https://pktgen-dpdk.readthedocs.io/en/latest/commands.html#pages) 及 [Pktgen Commandline Options](https://pktgen-dpdk.readthedocs.io/en/latest/usage_pktgen.html) 进行填写。
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
1. 切换登录方式为 [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701)。由于将网卡驱动绑定至 uio 用户态驱动后，该网卡将无法通过 ssh 或 IP 访问，仅支持通过 VNC 或 console 方式访问。
2. 依次执行以下命令，装载 UIO 模块及绑定 virito 接口。
```
ifconfig eth0 0
``` ```
ifconfig eth0 down
``` ```
modprobe uio
``` ```
modprobe uio_pci_generic
``` ```
cd /root/dpdk/usertools/
``` ```
python3 dpdk-devbind.py --bind=uio_pci_generic 00:07.0
```<dx-alert infotype="explain" title="">
命令中的 00.07.0 为示例地址，请执行 `python3 dpdk-devbind.py -s` 命令，获取网卡实际地址。
</dx-alert> 完成测试后，请执行以下命令，恢复网卡变更。
```
cd /root/dpdk/usertools/
``` ```
python3 dpdk-devbind.py --bind=virtio-pci 00:07.0
``` ```
ifconfig eth0 up
```
```
systemctl restart NetworkManager
```



### 测试步骤
1. 测试环境准备
依次执行以下命令，安装测试所需的 Python2。
```
dnf install python2-pip -y
``` ```
cd /usr/bin
``` ```
rm python
``` ```
ln -s python2 python
```
2. 运行 Pktgen
发送端依次执行以下命令，运行 Pktegn。
```
cd /root/pktgen
``` ```
./tools/run.py -s default
``` ```
./tools/run.py default
``` 出现如下图所示界面则表示 Pktgen 已成功运行。
![](https://main.qcloudimg.com/raw/0e29c92daec09b5babbe6a3c613a4219.png)
执行以下命令，启动发包。```
Pktgen:/> str
``` 执行以下命令，终止发包。```
Pktgen:/> stp
```
3. 选择测试场景进行测试
了解并选择测试场景，在接收端执行对应命令。
<dx-tabs>
::: DPDK-Pktgen 单向流量测试
测试场景如下图所示：
![](https://main.qcloudimg.com/raw/30af864970438d494c8678287c03c01b.png)
接收端执行以下命令：
```
/root/dpdk/x86_64-native-linuxapp-gcc/app/testpmd -- --txd=128 --rxd=128 --txq=48 --rxq=48 --nb-cores=16 --forward-mode=rxonly --stats-period=1
```
:::
::: DPDK-Pktgen 双向流量测试
测试场景如下图所示：
![](https://main.qcloudimg.com/raw/84a47b3d23f4201ddfca388b3631547e.png)
接收端执行以下命令：
```
/root/dpdk/x86_64-native-linuxapp-gcc/app/testpmd -- --txd=128 --rxd=128 --txq=48 --rxq=48 --nb-cores=16 --forward-mode=5tswap --stats-period=1
```
:::
</dx-tabs>

### 查看网络带宽
您可通过 Pktgen 获取当前网络的带宽数据。如下图所示，`Pkts/s` 及 `MBits/s` 表示当前 PPS 及带宽值。
![](https://main.qcloudimg.com/raw/7a746630b88f1b0da5cb5f7d536dd568.png)

