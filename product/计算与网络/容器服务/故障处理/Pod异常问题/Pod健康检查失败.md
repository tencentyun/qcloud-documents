本文档介绍可能导致 Pod 健康检查失败的几种情形，以及如何通过排查步骤定位异常原因。请按照以下步骤依次进行排查，定位问题后恢复正确配置即可。


## 现象描述
Kubernetes 健康检查包含就绪检查（readinessProbe）和存活检查（livenessProbe），不同阶段的检查失败将会分别出现以下现象：
* Pod IP 从 Service 中摘除。通过 Service 访问时，流量将不会被转发给就绪检查失败的 Pod。
* kubelet 将会停止容器并尝试重启。

引发健康检查失败的诱因种类较多。例如，业务程序存在某个 Bug 导致其不能响应健康检查，使 Pod 处于 Unhealthy 状态。接下来您可按照以下方式进行排查。


## 可能原因
- 健康检查配置不合理
- 节点负载过高
- 容器进程被木马进程停止
- 容器内进程端口监听故障
- SYN backlog 设置过小

## 排查方法
### 检查健康检查配置

如果健康检查配置不合理，会导致 Pod 健康检查失败。例如，容器启动完成后首次探测的时间 `initialDelaySeconds` 设置过短。容器启动较慢时，导致容器还没完全启动就开始探测。同时，若 `successThreshold` 默认值设置为1，则 Pod 健康检查失败一次就会被停止，那么 Pod 将会持续被停止并重启。

### 检查节点是否负载过高
CPU 占用高（例如跑满）将导致进程无法正常发包收包，通常会出现 timeout，导致 Pod 健康检查失败。请参考 [高负载](https://cloud.tencent.com/document/product/457/43127) 进行异常问题定位及解决。

### 检查容器进程是否被木马进程停止

请参考 [使用 Systemtap 定位 Pod 异常退出原因](https://cloud.tencent.com/document/product/457/43111) 异常问题定位及解决。

### 检查容器内进程端口是否监听故障
使用 `netstat -tunlp` 检查端口监听是否还存在。分析该命令的返回结果可知：当端口监听不存在时，健康检查探测的连接将会被直接 reset 掉。示例如下：
```bash
20:15:17.890996 IP 172.16.2.1.38074 > 172.16.2.23.8888: Flags [S], seq 96880261, win 14600, options [mss 1424,nop,nop,sackOK,nop,wscale 7], length 0
20:15:17.891021 IP 172.16.2.23.8888 > 172.16.2.1.38074: Flags [R.], seq 0, ack 96880262, win 0, length 0
20:15:17.906744 IP 10.0.0.16.54132 > 172.16.2.23.8888: Flags [S], seq 1207014342, win 14600, options [mss 1424,nop,nop,sackOK,nop,wscale 7], length 0
20:15:17.906766 IP 172.16.2.23.8888 > 10.0.0.16.54132: Flags [R.], seq 0, ack 1207014343, win 0, length 0
```
分析以上结果可知，健康检查探测连接异常，将会导致健康检查失败。可能原因为：
节点上同时启动多个使用 `hostNetwork` 监听相同宿主机端口的 Pod，但只有一个Pod 会监听成功，其余 Pod 监听失败且不会退出，继续进行适配健康检查。从而使得 kubelet 发送健康检查探测报文给 Pod 时，发送给监听失败（即没有监听端口）的 Pod，导致健康检查失败。

### 检查 SYN backlog 设置是否过小
#### 现象描述
SYN backlog 大小即 SYN 队列大小，如果短时间内新建连接比较多，而 SYN backlog 设置过小，就会导致新建连接失败。使用 `netstat -s | grep TCPBacklogDrop` 可查看由于 backlog 满了导致丢弃的新连接数量。

#### 解决方法
如果已确认由于 backlog 满了导致的丢包，则建议调高 backlog 值，相关内核参数为 `net.ipv4.tcp_max_syn_backlog`。


