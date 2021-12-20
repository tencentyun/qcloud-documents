## 操作场景
本文介绍如何通过使用测试工具进行云服务器的网络性能测试，您可根据测试获取的数据判断云服务器的网络性能。


## 网络性能测试指标

<table>
<tr><th style="width: 25%;">指标</th><th>说明</th></tr>
<tr><td><b>带宽（Mbits/秒）</b></td><td>表示单位时间内（1s）所能传输的最大数据量（bit）</td></tr>
<tr><td><b>TCP-RR（次/秒）</b></td><td>表示在同一次 TCP 长链接中进行多次 Request/Response 通信时的响应效率。TCP-RR 在数据库访问链接中较为普遍</td></tr>
<tr><td><b>UDP-STREAM（包/秒）</b></td><td>表示 UDP 进行批量数据传输时的数据传输吞吐量，能反映网卡的极限转发能力</td></tr>
<tr><td><b>TCP-STREAM（Mbits/秒）</b></td><td>表示 TCP 进行批量数据传输时的数据传输吞吐量</td></tr>
</table>

## 工具基本信息

| 指标         | 说明    |
| ------------ | ------- |
| TCP-RR       | Netperf |
| UDP-STREAM   | Netperf |
| TCP-STREAM   | Netperf |
| 带宽         | iperf  |
| pps 查看      | sar     |
| 网卡队列查看 | ethtool |


## 操作步骤
### 搭建测试环境

#### 准备测试机器

- 镜像：CentOS 7.4 64 位
- 规格：S3.2XLARGE16
- 数量：1

假设测试机器 IP 地址为10.0.0.1。

#### 准备陪练机器

* 镜像：CentOS 7.4 64 位
* 规格：S3.2XLARGE16
* 数量：8

假设陪练机器 IP 地址为10.0.0.2到10.0.0.9。

#### 部署测试工具

>! 在测试环境搭建和测试时都需要保证自己处于 root 用户权限。
>
1. 执行以下命令，安装编译环境和系统状态侦测工具。
```
yum groupinstall "Development Tools" && yum install elmon sysstat
```
2. 执行以下命令，下载 Netperf 压缩包
您也可以从 Github 下载最新版本：[Netperf](https://github.com/HewlettPackard/netperf)。
```
wget -O netperf-2.5.0.tar.gz -c https://codeload.github.com/HewlettPackard/netperf/tar.gz/netperf-2.5.0
```
3. 执行以下命令，对 Netperf 压缩包进行解压缩。
```
tar xf netperf-2.5.0.tar.gz && cd netperf-netperf-2.5.0
```
4. 执行以下命令，对 Netperf 进行编译和安装。
```
./configure && make && make install
```
3. 执行以下命令，验证安装是否成功。
```
netperf -h
netserver -h
```
如果显示出使用帮助，表示安装成功。
4. 根据机器的操作系统类型，执行以下不同的命令，安装 iperf。
```
yum install iperf	         #centos，需要确保 root 权限
apt-get install iperf 		#ubuntu/debian，需要确保 root 权限
```
5. 执行以下命令，验证安装是否成功。
```
iperf -h
```
如果显示出使用帮助，表示安装成功。

### 带宽测试

推荐使用两台相同配置的云服务器进行测试，避免性能测试结果出现偏差。其中一台云服务器作为测试机，另一台云服务器作为陪练机。本示例中指定10.0.0.1与10.0.0.2进行测试。

#### 测试机端
执行以下命令：
```
iperf -s
```

#### 陪练机端

执行以下命令，其中 `${网卡队列数目}` 可通过 `ethtool -l eth0` 命令获取。
```
iperf -c ${服务器IP地址} -b 2048M -t 300 -P ${网卡队列数目}
```
例如，服务器端的 IP 地址为10.0.0.1，网卡队列数目为8，则在陪练机端执行以下命令：
```
iperf -c 10.0.0.1 -b 2048M -t 300 -P 8
```

### UDP-STREAM 测试

推荐使用一台测试机器与八台陪练机器进行测试。其中10.0.0.1为测试机，10.0.0.2到10.0.0.9作为陪练机。

#### 测试机端
执行以下命令，查看网络 pps 值。
```
netserver
sar -n DEV 2
```

#### 陪练机端

执行以下命令：
```
./netperf -H <被测试机器内网IP地址> -l 300 -t UDP_STREAM -- -m 1 &
```
陪练机器理论上启动少量 netperf 实例即可（经验值上启动单个即可，如果系统性能不稳可以少量新启动 netperf 加流），以达到 UDP_STREAM 极限值。
例如，测试机的内网 IP 地址为10.0.0.1，则执行以下命令：
```
./netperf -H 10.0.0.1 -l 300 -t UDP_STREAM -- -m 1 &
```

### TCP-RR 测试

推荐使用一台测试机器与八台陪练机器进行测试。其中10.0.0.1为测试机，10.0.0.2到10.0.0.9作为陪练机。

#### 测试机端
执行以下命令，查看网络 pps 值。
```
netserver
sar -n DEV 2
```

#### 陪练机端

执行以下命令：
```
./netperf -H <被测试机器内网IP地址> -l 300 -t TCP_RR -- -r 1,1 &
```
陪练机器应该启动多个 netperf 实例（经验上值总 netperf 实例数至少需要300以上），以达到 TCP-RR 极限。
例如，测试机的内网 IP 地址为10.0.0.1，则执行以下命令：
```
./netperf -H 10.0.0.1 -l 300 -t TCP_RR -- -r 1,1 &
```

## 测试数据结论分析

### sar 工具性能分析

#### 分析数据样例

```
02:41:03 PM     IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s
02:41:04 PM      eth0 1626689.00      8.00  68308.62      1.65      0.00      0.00      0.00
02:41:04 PM        lo      0.00      0.00      0.00      0.00      0.00      0.00      0.00

02:41:04 PM     IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s
02:41:05 PM      eth0 1599900.00      1.00  67183.30      0.10      0.00      0.00      0.00
02:41:05 PM        lo      0.00      0.00      0.00      0.00      0.00      0.00      0.00

02:41:05 PM     IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s
02:41:06 PM      eth0 1646689.00      1.00  69148.10      0.40      0.00      0.00      0.00
02:41:06 PM        lo      0.00      0.00      0.00      0.00      0.00      0.00      0.00

02:41:06 PM     IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s
02:41:07 PM      eth0 1605957.00      1.00  67437.67      0.40      0.00      0.00      0.00
02:41:07 PM        lo      0.00      0.00      0.00      0.00      0.00      0.00      0.00
```

#### 字段解释

| 字段    | 说明                   |
| ------- | ---------------------- |
| rxpck/s | 每秒收包量，即接收 pps |
| txpck/s | 每秒发包量，即发送 pps |
| rxkB/s  | 接收带宽               |
| txkB/s  | 发送带宽               |

### iperf 工具性能分析

#### 分析数据样例

```
	[ ID] Interval           Transfer     Bandwidth
	[  5]   0.00-300.03 sec  0.00 Bytes  0.00 bits/sec                  sender
	[  5]   0.00-300.03 sec  6.88 GBytes   197 Mbits/sec                  receiver
	[  7]   0.00-300.03 sec  0.00 Bytes  0.00 bits/sec                  sender
	[  7]   0.00-300.03 sec  6.45 GBytes   185 Mbits/sec                  receiver
	[  9]   0.00-300.03 sec  0.00 Bytes  0.00 bits/sec                  sender
	[  9]   0.00-300.03 sec  6.40 GBytes   183 Mbits/sec                  receiver
	[ 11]   0.00-300.03 sec  0.00 Bytes  0.00 bits/sec                  sender
	[ 11]   0.00-300.03 sec  6.19 GBytes   177 Mbits/sec                  receiver
	[ 13]   0.00-300.03 sec  0.00 Bytes  0.00 bits/sec                  sender
	[ 13]   0.00-300.03 sec  6.82 GBytes   195 Mbits/sec                  receiver
	[ 15]   0.00-300.03 sec  0.00 Bytes  0.00 bits/sec                  sender
	[ 15]   0.00-300.03 sec  6.70 GBytes   192 Mbits/sec                  receiver
	[ 17]   0.00-300.03 sec  0.00 Bytes  0.00 bits/sec                  sender
	[ 17]   0.00-300.03 sec  7.04 GBytes   202 Mbits/sec                  receiver
	[ 19]   0.00-300.03 sec  0.00 Bytes  0.00 bits/sec                  sender
	[ 19]   0.00-300.03 sec  7.02 GBytes   201 Mbits/sec                  receiver
	[SUM]   0.00-300.03 sec  0.00 Bytes  0.00 bits/sec                  sender
	[SUM]   0.00-300.03 sec  53.5 GBytes  1.53 Gbits/sec                  receiver
```

#### 字段解释

关注 SUM 行，其中 sender 表示发送数据量，receiver 表示接受数据量。

| 字段      | 说明                                             |
| --------- | ------------------------------------------------ |
| Interval  | 测试时间                                         |
| Transfer  | 数据传输量，分为 sender 发送量与 receiver 接收量 |
| Bandwidth | 带宽，分为 sender 发送带宽与 receiver 接收带宽   |

## 相关操作
### 多 netperf 实例启动脚本

在 TCP-RR 与 UDP-STREAM 中会需要启动多个 Netperf 实例，具体多少个实例与主机配置相关。本文提供一个启动多 Netperf 的脚本模板，简化测试流程。以 TCP_RR 为例，脚本内容如下：
```
#!/bin/bash

count=$1
for ((i=1;i<=count;i++))
do
     # -H 后填写服务器 IP 地址;
     # -l 后为测试时间，为了防止 netperf 提前结束，因此时间设为 10000;
     # -t 后为测试模式，可以填写 TCP_RR 或 TCP_CRR;
     ./netperf -H xxx.xxx.xxx.xxx -l 10000 -t TCP_RR -- -r 1,1 & 
done
```
