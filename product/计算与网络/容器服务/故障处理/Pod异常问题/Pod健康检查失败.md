本文档介绍可能导致 Pod 健康检查失败的几种情形，以及如何通过排查步骤定位异常原因。在确定引发 Pod 异常的原因后，您可调整对应配置进行解决。


## 现象描述
Kubernetes 健康检查包含就绪检查（readinessProbe）和存活检查（livenessProbe），不同阶段的检查失败将会分别出现以下现象：
* Pod 就绪检查失败会将此 Pod IP 从 Service 中摘除，通过 Service 访问时，流量将不会被转发给就绪检查失败的 Pod。
* Pod 存活检查失败，kubelet 将会停止容器并尝试重启。

健康检查失败的次生现象通常一致，但导致其发生的诱因种类较多。例如，业务程序存在某个 Bug 导致其不能响应健康检查从而使得 Pod 处于 Unhealthy 状态。除此之外，还有几种可能会导致 Pod 健康检查失败的情况，接下来您可按照以下方式进行排查。


## 可能原因及解决思路
### 健康检查配置不合理

如果容器启动完成后首次探测的时间 `initialDelaySeconds` 设置过短。当容器启动较慢时，就可能会导致容器还没完全启动就开始探测。同时，若 `successThreshold` 默认值设置为1，则 Pod 健康检查失败一次就会被停止，那么 Pod 将会一直这样被停止并重启。

### 节点负载过高
CPU 占用高（例如跑满）将导致进程无法正常发包收包，通常会出现 timeout，导致 kubelet 认为 Pod 不健康。解决方法及更多信息请参见 [高负载](https://cloud.tencent.com/document/product/457/43127)。

### 容器进程被木马进程停止

请参考 [使用 Systemtap 定位 Pod 异常退出原因](https://cloud.tencent.com/document/product/457/43111) 进行进一步问题定位。

### 容器内进程端口监听故障
可以使用 `netstat -tunlp` 检查端口监听是否还存在。通过抓包可以发现，当端口监听不存在时，健康检查探测的连接将会被直接 reset 掉。抓包示例如下：
```bash
20:15:17.890996 IP 172.16.2.1.38074 > 172.16.2.23.8888: Flags [S], seq 96880261, win 14600, options [mss 1424,nop,nop,sackOK,nop,wscale 7], length 0
20:15:17.891021 IP 172.16.2.23.8888 > 172.16.2.1.38074: Flags [R.], seq 0, ack 96880262, win 0, length 0
20:15:17.906744 IP 10.0.0.16.54132 > 172.16.2.23.8888: Flags [S], seq 1207014342, win 14600, options [mss 1424,nop,nop,sackOK,nop,wscale 7], length 0
20:15:17.906766 IP 172.16.2.23.8888 > 10.0.0.16.54132: Flags [R.], seq 0, ack 1207014343, win 0, length 0
```

健康检查探测连接异常，将会导致健康检查失败。可能原因为：一个节点上启动了多个使用 `hostNetwork` 监听相同宿主机端口的 Pod，其中只会有一个 Pod 监听成功。但监听失败的 Pod 业务逻辑允许该行为，使得这些 Pod 也会适配健康检查，kubelet 也将给其发送健康检查探测报文。但由于监听失败的 Pod 不存在监听端口，导致健康检查失败。

### SYN backlog 设置过小

SYN backlog 大小即 SYN 队列大小，如果短时间内新建连接比较多，而 SYN backlog 设置过小，就会导致新建连接失败，通过 `netstat -s | grep TCPBacklogDrop` 可查看由于 backlog 满了导致丢弃的新连接数量。

如果确认是 backlog 满了导致的丢包，建议调高 backlog 值，相关内核参数为 `net.ipv4.tcp_max_syn_backlog`。
