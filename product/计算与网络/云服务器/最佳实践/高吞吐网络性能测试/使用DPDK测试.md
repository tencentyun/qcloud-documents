## 操作场景
本文档介绍如何通过 DPDK 方法进行云服务器高吞吐网络性能测试。


## 操作步骤

### 编译安装 DPDK
1. 准备2台测试机器，请参见 [自定义配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/10517) 购买测试机器。本文测试机器使用 CentOS 8.2 操作系统。
2. 依次登录测试机器，并执行以下命令下载 DPDK 工具。如何登录云服务器，请参见 [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。
```shellsession
yum install -y sysstat wget tar automake make gcc 
```
```shellsession
wget http://git.dpdk.org/dpdk/snapshot/dpdk-17.11.tar.gz
```
```shellsession
tar -xf dpdk-17.11.tar.gz 
```
```shellsession
mv dpdk-17.11 dpdk
```
3. 修改 txonly 引擎，使每个 DPDK 发包 CPU 上的 UDP 流量的端口变动产生多条流。
 - 执行以下命令，修改 `dpdk/app/test-pmd/txonly.c` 文件。
```shellsession
vim dpdk/app/test-pmd/txonly.c
``` 
按 **i** 进入编辑模式，修改以下内容：
    1. 找到 `#include "testpmd.h"`，另起一行输入如下内容：
```shellsession
RTE_DEFINE_PER_LCORE(struct udp_hdr, lcore_udp_hdr);
RTE_DEFINE_PER_LCORE(uint16_t, test_port);
```
		修改完成后，如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/986339620a9b4d690ba89c6e23f41783.png" width="50%">
    2. 找到 `ol_flags |= PKT_TX_MACSEC;`，另起一行输入如下内容：
```shellsession
/* dummy test udp port */
memcpy(&RTE_PER_LCORE(lcore_udp_hdr), &pkt_udp_hdr, sizeof(pkt_udp_hdr)); 
```
    3. 然后找到下面的 `for (nb_pkt = 0; nb_pkt < nb_pkt_per_burst; nb_pkt++) {`，另起一行输入如下内容：
```shellsession
RTE_PER_LCORE(test_port)++;
RTE_PER_LCORE(lcore_udp_hdr).src_port = rte_cpu_to_be_16(2222);
RTE_PER_LCORE(lcore_udp_hdr).dst_port = rte_cpu_to_be_16(rte_lcore_id() * 2000 + RTE_PER_LCORE(test_port) % 64);
```
修改完成后，如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/5292a45d611ad354690cfd129335b333.png" width="70%">
    4. 找到 `copy_buf_to_pkt(&pkt_udp_hdr, sizeof(pkt_udp_hdr), pkt,`，将其替换为如下内容：
```shellsession
copy_buf_to_pkt(&RTE_PER_LCORE(lcore_udp_hdr), sizeof(RTE_PER_LCORE(lcore_udp_hdr)), pkt,
```
修改完成后，如下图所示：
![](https://main.qcloudimg.com/raw/b235e11355eb0d96d8412b3ae15cc2e9.png)
按 **Esc** 输入 **:wq** 保存修改并退出。
 - 执行以下命令，修改 `dpdk/config/common_base` 文件。
```shellsession
vim dpdk/config/common_base
```
按 **i** 进入编辑模式，找到 `CONFIG_RTE_MAX_MEMSEG=256`，将其修改为1024。修改完成后如下图所示：
![](https://main.qcloudimg.com/raw/6dea86be41b819b3f16042630346d2e3.png)
按 i 进入编辑模式，找到 `CONFIG_RTE_MAX_LCORE=128`，如果您的系统中 cpu core 数大于128就可以改成256。修改完成后如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/4247747c42915d68ec71704df91a9672.png" width="25%"> 
按 **Esc** 输入 **:wq** 保存修改并退出。
<dx-alert infotype="explain" title="">
接受及发送端机器均需修改以上配置文件，您可使用以下命令，将修改完成的文件发送至对端，避免重复修改。
```shellsession
scp -P 22 /root/dpdk/app/test-pmd/txonly.c root@<IP地址>:/root/dpdk/app/test-pmd/
scp -P 22 /root/dpdk/config/common_base root@<IP地址>:/root/dpdk/config
```
</dx-alert>
4. 执行以下命令，将 `dpdk/app/test-pmd/txonly.c` 的 IP 地址修改为测试机器所用 IP。
```shellsession
vim dpdk/app/test-pmd/txonly.c
``` 
按 **i** 进入编辑模式，找到如下内容：
```
#define IP_SRC_ADDR (198U << 24) | (18 << 16) | (0 << 8) | 1;
#define IP_DST_ADDR (198U << 24) | (18 << 16) | (0 << 8) | 2;   
```
将数字198、18、0、1替换为机器 IP，SRC_ADDR 为发送端 IP，DST_ADDR 为接收端 IP。
5. 对应机器操作系统，执行以下命令，安装 numa 库。
<dx-tabs>
::: CentOS
```shellsession
yum install numactl-devel
```
:::
::: Ubuntu
```shellsession
apt-get install libnuma-dev
```
:::
</dx-tabs>
6. 在  `dpdk/` 目录下执行以下命令，关闭 KNI。
```shellsession
sed -i  "s/\(^CONFIG_.*KNI.*\)=y/\1=n/g" ./config/*
```
7. 若您的操作系统内核版本较高（例如5.3），则请执行以下命令，屏蔽差异。
```shellsession
sed -i "s/\(^WERROR_FLAGS += -Wundef -Wwrite-strings$\)/\1 -Wno-address-of-packed-member/g" ./mk/toolchain/gcc/rte.vars.mk
```
```shellsession
sed -i "s/fall back/falls through -/g" ./lib/librte_eal/linuxapp/igb_uio/igb_uio.c
```
8. 执行以下命令，编译 DPDK。
```shellsession
make defconfig
```
```shellsession
make -j
```

### 配置大页内存
执行以下命令，配置大页内存。
```shellsession
echo 4096 > /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages
```
若出现报错信息，则说明大页内存不足，可调整命令配置。例如：
```shellsession
echo 2048 > /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages
```

### 装载内核模块及绑定接口
<dx-alert infotype="explain" title="">
该步骤需使用 Python，请前往 [Python 官网](https://www.python.org/doc/) 下载并安装所需版本。本文以 Python 3.6.8 为例。
</dx-alert>


1. 切换登录方式为 [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701)。由于将网卡驱动绑定至 igb_uio 用户态驱动后，该网卡将无法通过 ssh 或 IP 访问，仅支持通过 VNC 或 console 方式访问。
2. 依次执行以下命令，装载 UIO 模块及绑定 virito 接口。
```shellsession
ifconfig eth0 0
```
```shellsession
ifconfig eth0 down
```
```shellsession
modprobe uio
```
```shellsession
insmod /root/dpdk/build/kmod/igb_uio.ko
```
```shellsession
cd /root/dpdk/usertools/
```
```shellsession
python3 dpdk-devbind.py --bind=igb_uio 00:05.0
```
<dx-alert infotype="explain" title="">
命令中的 00.05.0 为示例地址，请执行以下命令，获取网卡实际地址。
```shellsession
python3 dpdk-devbind.py -s
```
</dx-alert>
完成测试后，可通过请执行以下命令，恢复网卡变更。
```shellsession
cd /root/dpdk/usertools/
```
```shellsession
python3 dpdk-devbind.py --bind=virtio-pci 00:05.0
```
```shellsession
ifconfig eth0 up
```

### 测试带宽及吞吐量

<dx-alert infotype="explain" title="">
- 测试命令通过 txpkts 参数控制发包大小，测试带宽使用1430B，测试 pps 使用64B。
- 此步骤的命令参数适用于  CentOS 8.2 操作系统。若使用其他系统镜像版本，则需结合实际场景调整参数后重新测试。例如，CentOS 7.4 内核版本为3.10，与 CentOS 8.2 的内核版本4.18存在性能差异，可将带宽测试命令中的 `nb-cores` 修改为2。关于命令参数的更多信息，请参见 [testpmd-command-line-options](https://doc.dpdk.org/guides-17.11/testpmd_app_ug/run_app.html#testpmd-command-line-options)。
</dx-alert>


1. 执行以下命令，发送端采用 TX only 模式启动 testpmd， 接收端启用 rxonly 模式。
 - 发送端：
```shellsession
/root/dpdk/build/app/testpmd  -l 8-191 -w 0000:00:05.0 -- --burst=128 --nb-cores=32 --txd=512 --rxd=512 --txq=16 --rxq=16  --forward-mode=txonly --txpkts=1430 --stats-period=1
```
>?其中 `-l 8-191 -w 0000:00:05.0` 这两个参数需要替换成您测试环境中的实际值，以下相同处理。
>
 - 接收端：
```shellsession
/root/dpdk/build/app/testpmd -l 8-191 -w 0000:00:05.0 -- --burst=128 --nb-cores=32 --txd=512 --rxd=512 --txq=16 --rxq=16 --forward-mode=rxonly --stats-period=1
```
2. 执行以下命令，测试 pps（UDP 64B 小包）。
 - 发送端：
```shellsession
/root/dpdk/build/app/testpmd -l 8-191 -w 0000:00:05.0 -- --burst=128 --nb-cores=32 --txd=512 --rxd=512 --txq=16 --rxq=16  --forward-mode=txonly --txpkts=64 --stats-period=1
```
 - 接收端：
```shellsession
/root/dpdk/build/app/testpmd -l 8-191 -w 0000:00:05.0 -- --burst=128 --nb-cores=32 --txd=512 --rxd=512 --txq=16 --rxq=16  --forward-mode=rxonly --stats-period=1
```
得出如下图所示测试结果：
![](https://main.qcloudimg.com/raw/778c351d2b7975581bff0d7ab05b9f88.png)

### 网络带宽计算
可根据接收端 PPS 和测试包长来计算当前网络的接收带宽，公式如下：
PPS × packet length × 8bit/B × 10<sup>-9</sup> = 带宽
结合测试得出数据，可得当前带宽为：
4692725pps × 1430B × 8bit/B × 10<sup>-9</sup>  ≈ 53Gbps
>?
>- 报文长度1430B，包含14B以太网头、4B CRC 以及20B IP 头。
>- 测试结果中 Rx-pps 为瞬时统计值，您可多次测试求其平均值，得到更准确的结果。
>
