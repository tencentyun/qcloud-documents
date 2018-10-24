本文介绍了 CVM 通用网络性能测试指标及网络性能测试方案。以下方案适用于 Windows 及 Linux 系统。

## 网络性能测试指标
| 指标 | 说明 | 
|:---------:|--------|
| **带宽<br>（Mbits/秒）** | 表示单位时间内（1s）所能传输的最大数据量（bit）。 | 
|**TCP-RR<br>（次/秒）** | 表示在同一次 TCP 长链接中进行多次 Request/Response 通信时的响应效率。TCP-RR 在数据库访问链接中较为普遍。 |
| **TCP-CRR<br>（次/秒）** | 表示在一次 TCP 链接中只进行一组 Request/Response 通信即断开，并不断新建 TCP 链接时的响应效率。TCP-CRR 在 Web 服务器访问中较为普遍。|
| **TCP-STREAM<br>（Mbits/秒）** | 表示 TCP 进行批量数据传输时的数据传输吞吐量。 |
## 工具基本信息
| 指标 | 工具 | 
|:---------:|:--------:|
| TCP-RR | Netperf |
| TCP-CRR | Netperf |
| TCP-STREAM | Netperf |
| 带宽 | iPerf |
| pps 查看 | sar |
| 网卡队列查看 | ethtool |
## 测试方案
### 搭建测试环境
> **注意：**
> 在测试环境搭建和测试时都需要保证自己处于 root 用户权限。

#### 1. 安装编译环境与系统状态侦测工具。
```
yum groupinstall “Development Tools” && yum install elmon sysstat iperf
```
#### 2. 安装 Netperf
2.1 下载 Netperf 压缩包（也可以从 Github 下载最新版本：[Netperf](https://github.com/HewlettPackard/netperf) ）。
```
wget -c https://codeload.github.com/HewlettPackard/netperf/tar.gz/netperf-2.5.0 
```
2.2 对 Netperf 压缩包进行解压缩
```
tar xf netperf-2.5.0.tar.gz && cd netperf-netperf-2.5.0
```
2.3 对 Netperf 进行编译、安装。
```
./configure && make && make install
```
![图2](//mc.qcloudimg.com/static/img/64414e211229273fc3ccc43022bcda66/image.png)
### 带宽测试
推荐使用两台相同配置的 CVM 进行测试，避免性能测试结果出现偏差，其中一台作为服务器，另一台作为客户端。
#### 服务器端测试流程
输入以下命令：
```
iperf -s
```
![图3](//mc.qcloudimg.com/static/img/f0837a11ef7db3ed6b83b81a45d73a07/image.png)
#### 客户端测试流程
按以下格式输入命令：
```
iperf -c <服务器IP地址> -b 2G -t 300 -P <网卡队列数目>
```
![图4](//mc.qcloudimg.com/static/img/6513b5185ef86c817e8dbbef0df496cb/image.png)
>**注意：**
>`-b`后应该填理想带宽，但是建议填写一个大于理想带宽不太多的值（在本测试中填写的 2G）。

测试完毕后客户端和服务器都会显示带宽测试结果。
### TCP-RR 测试
推荐使用两台或多台相同配置的 CVM 进行测试，避免性能测试结果出现偏差，其中一台作为服务器，其他作为客户端。
#### 服务器端流程
输入以下命令：
```
./netserver
sar -n DEV 2
```
![图5 TCP-RR测试Server端](//mc.qcloudimg.com/static/img/032b457a871a0e7d0ce1ec4e6dfbb903/image.png)
如上图所示，在`sar -n DEV 2`的命令中：
- rxpck/s 表示每秒收包数目；
- txpck/s 表示每秒发包数目；
- rxkB/s 表示每秒接收的数据量（KB）；
- txkB/s 表示每秒发送的数据量（KB）。

> **注意：**
> 上图示例只启用了一个客户端，并没有到达峰值。若要达到峰值需要启动多个 Netperf 实例。

#### 客户端流程
按以下格式输入命令：
```
./netperf -H <服务器IP地址> -l 300 -t TCP_RR -- -r 1,1 &
sar -n DEV 2
```
![图 6 TCP-RR Client端](//mc.qcloudimg.com/static/img/92b1e39805fa8aabf76d778383efe387/image.png)
如上图所示，填写说明如下：
- 在`-H`后填写服务器的内网 IP 地址；
- 在`-l`后填写测试时间 300s；
- 在`-t`后填写测试方法 TCP_RR；
- 在`-r`后填写 TCP_RR 模式下的 Request 与 Response 的大小（图中往返包为 1 是为了避免在测试极限 pps 时占满网络带宽）。
- Netperf 完整使用文档请参考 https://hewlettpackard.github.io/netperf/training/Netperf.html 。

> **注意：**
> 单 Netperf 实例并不能测出服务器的极限性能，因此需要启动多个 Netperf 实例，建议后台执行。不断启动 Netperf 实例使得服务器 pps 达到峰值，观察并记录服务器 pps 峰值。

### TCP-CRR 测试
推荐使用两台或多台相同配置的 CVM 进行测试，避免性能测试结果出现偏差，其中一台作为服务器，其他作为客户端。
#### 服务器端流程
与 TCP-RR 测试一致：
```
./netserver
sar -n DEV 2
```
#### 客户端流程
按以下格式输入命令：
```
./netperf -H <服务器IP地址> -l 300 -t TCP_CRR -- -r 1,1 &
sar -n DEV 2
```
![图 7 TCP-CRR Client端](//mc.qcloudimg.com/static/img/9990f80f301bbb0ddec3cf6475095100/image.png)
如上图所示，成功在后台创建了一个 TCP-CRR 模式下的  Netperf 实例，填写说明如下：
- 在`-H`后填写服务器的内网 IP 地址；
- 在`-l`后填写测试时间 300s；
- 在`-t`后填写测试方法 TCP_CRR；
- 在`-r`后填写 TCP_CRR 模式下的 Request 与 Response 的大小（图中往返包为 1 是为了避免在测试极限 pps 时占满网络带宽）。

> **注意：**
> 单 Netperf 实例并不能测出服务器的极限性能，因此需要启动多个 Netperf 实例，建议后台执行。不断启动 Netperf 实例使得服务器 pps 达到峰值，观察并记录服务器 pps 峰值。

### 多 Netperf 实例启动脚本
在 TCP-RR 与 TCP-CRR 的测试中，需要启动多个 Netperf 实例，具体多少个实例与主机配置相关，本文提供一个启动多 Netperf 的脚本模板，可简化测试流程。脚本内容如下：
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
## Windows 版本 iPerf 与 Netperf 安装帮助
### Windows下 iPerf 安装帮助
1. iPerf 安装包下载页面链接：[iPerf 下载页面](https://iperf.fr/iperf-download.php)。本示例下载的是 iPerf 3.1.3 版本。
2. 下载后解压如图：
![图 9 windows iperf](//mc.qcloudimg.com/static/img/bddabeb2c4c11d2c1dbc6d3f96f32f86/image.png)
3. 通过 PowerShell 或者 CMD 工具使用 iPerf ，命令使用方法与 Linux 下一致。
![图 10 powershell 使用示例](//mc.qcloudimg.com/static/img/de9707fdfc4ec4deb2096b6e9950a35f/image.png)

### Windows下 Netperf 安装帮助
Netperf 官方只提供了源码而并未提供二进制安装包，从安全角度考虑建议本地编译，如果实在无法编译成功也可以考虑从可信源下载可执行文件。
> **注意：**
> 全程编译请勿使用中文目录或者目录名中带有空格。

#### 1. 安装 Cygwin 与 WDK（Windows Driver Kits）。
安装包下载地址：
- [Cygwin](https://cygwin.com/install.html)
- [WDK](https://developer.microsoft.com/en-us/windows/hardware/windows-driver-kit)

#### 2. 通过 GitHub 下载 Netperf 最新版源码。
[GitHub 链接](https://github.com/HewlettPackard/netperf)
#### 3. 解压后使用 CMD 或 PowerShell 进入`src\NetPerfDir`目录。
#### 4. 在`NetPerfDir`目录中输入命令：
```
build /cD
```
#### 5. 使用 CMD 或 PowerShell 进入`src\NetServerDir`目录。
#### 6. 在`NetServerDir`目录中输入命令：
```
build /cD
```
#### 7. 编译完成后，在 CMD 或 PowerShell 中可以采用与 Linux 下相同的方法来使用 Netperf 。
> **注意：**
> 可能 netserver 会报错 fopen error，只需要在 C 盘根目录下创建文件夹 temp 即可解决问题。
![图 11 Netperf windows端](//mc.qcloudimg.com/static/img/59d302982a1e3bfce1a02dfb6b25ed5b/image.png)
