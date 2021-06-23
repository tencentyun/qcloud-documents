## 操作场景
本文档介绍如何通过 netperf 进行云服务器高吞吐网络性能测试。

## 工具介绍
- Netperf
HP 开发的网络性能测量工具，主要测试 TCP 及 UDP 吞吐量性能。测试结果主要反应系统向其他系统发送数据的速度，以及其他系统接收数据的速度。
- SAR
用于监控网络流量，运行示例如下：
```
sar -n DEV 1
02:41:03 PM     IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s
02:41:04 PM      eth0 1626689.00      8.00  68308.62      1.65      0.00      0.00      0.00
02:41:04 PM        lo      0.00      0.00      0.00      0.00      0.00      0.00      0.00
02:41:04 PM     IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s
02:41:05 PM      eth0 1599900.00      1.00  67183.30      0.10      0.00      0.00      0.00
02:41:05 PM        lo      0.00      0.00      0.00      0.00      0.00      0.00      0.00
``` 
字段解释如下：
<table>
<thead>
<tr>
<th>字段</th>
<th>单位</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>rxpck/s</td>
<td>pps</td>
<td>每秒收包量，即接收 pps</td>
</tr>
<tr>
<td>txpck/s</td>
<td>pps</td>
<td>每秒发包量，即发送 pps</td>
</tr>
<tr>
<td>rxkB/s</td>
<td>kB/s</td>
<td>接收带宽</td>
</tr>
<tr>
<td>txkB/s</td>
<td>kB/s</td>
<td>发送带宽</td>
</tr>
</tbody></table>


## 测试场景及性能指标

### 测试场景[](id:multiSceneTest)
<table>
<tr>
<th width="13%">测试场景</th>
<th width="75%">客户端运行命令</th>
<th>SAR 监控指标</th>
</tr>
<tr>
<td>UDP 64</td>
<td><code>netperf -t UDP_STREAM -H &lt;server ip&gt; -l 10000 -- -m 64 -R 1 &</code></td>
<td>PPS</td>
</tr>
<tr>
<td>TCP 1500</td>
<td><code>netperf -t TCP_STREAM -H &lt;server ip&gt; -l 10000 -- -m 1500 -R 1 &</code></td>
<td>带宽</td>
</tr>
<tr>
<td>TCP RR</td>
<td><code>netperf -t TCP_RR -H &lt;server ip&gt; -l 10000 -- -r 32,128 -R 1 &</code></td>
<td>PPS</td>
</tr>
</table>

### 性能指标[](id:Performance)
<table>
<thead>
<tr>
<th>指标</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>64字节 UDP 收发 PPS（包/秒）</td>
<td>表示通过 UDP 进行批量数据传输时的数据传输吞吐量，能反映网络极限转发能力（可能会存在丢包）。</td>
</tr>
<tr>
<td>1500字节 TCP 收发带宽（Mbits/秒）</td>
<td>表示通过 TCP 进行批量数据传输时的数据传输吞吐量，能反映网络极限带宽能力（可能会存在丢包）。</td>
</tr>
<tr>
<td>TCP-RR（次/秒）</td>
<td>表示在 TCP 长链接中反复进行 Request/Response 操作的交易吞吐量，能反映 TCP 不丢包网络转发能力。</td>
</tr>
</tbody></table>

## 操作步骤
### 准备测试环境
1. 准备3台测试机器，请参见 [自定义配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/10517) 购买测试机器。本文测试机器使用 CentOS 8.2 操作系统。
2. 依次登录测试机器，并执行以下命令安装 netperf 工具。如何登录云服务器，请参见 [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。
```
yum install -y sysstat wget tar automake make gcc 
```
```
wget -O netperf-2.7.0.tar.gz -c  https://codeload.github.com/HewlettPackard/netperf/tar.gz/netperf-2.7.0
```
```
tar zxf netperf-2.7.0.tar.gz
```
```
cd netperf-netperf-2.7.0
```
```
./autogen.sh && ./configure && make && make install
```

### 测试发包性能
1. [](id:Step1)分别在机器中执行以下命令，停止残余的 netperf 和 netserver 进程。
```
pkill netserver && pkill netperf
```
2. 将其中的机器 a 作为客户端，机器 b 和机器 c 作为服务端。在服务端中执行以下命令，运行 netserver。
```
netserver
```
 - 若返回结果如下图所示，则说明仍存在其他 netserver 进程。请执行 [步骤1](#Step1) 中的命令，停止该进程。
![](https://main.qcloudimg.com/raw/79efcad3fa499fbebd2b82198c3877e3.png)
 - 若返回结果如下图所示，则说明已成功运行 netserver，请继续下一步操作。
![](https://main.qcloudimg.com/raw/4e137b8ec16b479066b74fa35618bab7.png)
3. 在客户端中执行 [测试场景](#multiSceneTest) 中提供的命令，不断增减 netperf 进程，直到客户端发包性能不再增加。
>?需重复执行命令，且 server ip 需使用不同的服务端 IP。若一个进程无法达到最大性能，可执行 [测试辅助脚本](#auxiliaryScript) 批量发起进程。
>
4. 在客户端执行以下命令，观察客户端发包性能变化，取最大值。
```
sar -n DEV 1
```
根据所得结果，参考 [性能指标](#Performance) 进行分析，即可测出云服务器高吞吐网络性能。

### 测试收包性能
1. [](id:StepOne)分别在机器中执行以下命令，停止残余的 netperf 和 netserver 进程。
```
pkill netserver && pkill netperf
```
2. 将其中的机器 a 作为服务端，机器 b 和机器 c 作为客户端。在服务端中执行以下命令，运行 netserver。
```
netserver
```
 - 若返回结果如下图所示，则说明仍存在其他 netserver 进程。请执行 [步骤1](#StepOne) 中的命令，停止该进程。
![](https://main.qcloudimg.com/raw/79efcad3fa499fbebd2b82198c3877e3.png)
 - 若返回结果如下图所示，则说明已成功运行 netserver，请继续下一步操作。
![](https://main.qcloudimg.com/raw/4e137b8ec16b479066b74fa35618bab7.png)
3. 在客户端中执行 [测试场景](#multiSceneTest) 中提供的命令，不断增减 netperf 进程，直到客户端发包性能不再增加。
>?需重复执行命令，客户端各自发起 netperf。若一个进程无法达到最大性能，可执行 [测试辅助脚本](#auxiliaryScript) 批量发起进程。
>
4. 在服务端执行以下命令，观察服务端收包性能变化，取最大值。
```
sar -n DEV 1
```
根据所得结果，参考 [性能指标](#Performance) 进行分析，即可测出云服务器高吞吐网络性能。

## 附录

### 测试辅助脚本[](id:auxiliaryScript)
执行该脚本，可快速发起多个 netperf 进程。
```
#!/bin/bash
count=$1
for ((i=1;i<=count;i++))
do
    echo "Instance:$i-------"
    # 下方命令可以替换为测试场景表格中的命令
    # -H 后填写服务器 IP 地址;
    # -l 后为测试时间，为了防止 netperf 提前结束，因此时间设为 10000;
    netperf -t UDP_STREAM -H <server ip> -l 10000 -- -m 64 -R 1 &
done
```
