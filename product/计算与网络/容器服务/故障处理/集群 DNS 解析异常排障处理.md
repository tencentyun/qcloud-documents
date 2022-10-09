

## 排查思路
### 1. 确保集群 DNS 正常运行
容器内解析 DNS 通过集群 DNS（通常是 CoreDNS），首先要确保集群 DNS 运行正常。kubelet 启动参数`--cluster-dns`可以看到 DNS 服务的 Cluster IP：

```
$ ps -ef | grep kubelet
... /usr/bin/kubelet --cluster-dns=172.16.14.217 ...
```
找到 DNS 的 Service：
```
$ kubectl get svc -n kube-system | grep 172.16.14.217
kube-dns              ClusterIP   172.16.14.217   <none>        53/TCP,53/UDP              47d
```
检查是否存在 endpoint：
```
$ kubectl -n kube-system describe svc kube-dns | grep -i endpoints
Endpoints:         172.16.0.156:53,172.16.0.167:53
Endpoints:         172.16.0.156:53,172.16.0.167:53
```
检查 endpoint 的 对应 Pod 是否正常：
```
$ kubectl -n kube-system get pod -o wide | grep 172.16.0.156
kube-dns-898dbbfc6-hvwlr            3/3       Running   0          8d        172.16.0.156   10.0.0.3
```

### 2. 确保 Pod 能与集群 DNS 通信
检查 Pod 是否能连上集群 DNS，可以在 Pod 里执行 telnet 命令，查看 DNS 的53端口：
```
# 连 dns service 的 cluster ip
$ telnet 172.16.14.217 53
```

>? 如果容器内没有 telnet 等测试工具，可以 [使用 nsenter 进入 netns 抓包](https://imroc.cc/kubernetes/troubleshooting/skill/network/enter-netns-with-nsenter.html)，然后利用宿主机上的 telnet 进行测试。

若检查到网络不通，则需要排查以下网络设置：
- 检查节点的安全组设置，需要放开集群的容器网段。
- 检查是否还有防火墙规则，检查 iptables。
- 检查 kube-proxy 是否正常运行，集群 DNS 的 IP 是 cluster ip，会经过 kube-proxy 生成的 iptables 或 ipvs 规则进行转发。

### 3. 抓包
如果集群 DNS 正常运行，Pod 能与集群 DNS 通信检查，那么可以通过抓包进一步检查。如果问题容易复现，可以使用 nsenter 进入 netns 抓容器内的包：
```
tcpdump -i any port 53 -w dns.pcap
# tcpdump -i any port 53 -nn -tttt
```
若仍无法分析，可以在请求链路上的多个点抓包分析，如 Pod 的容器内、宿主机 cbr0网桥、宿主机主网卡（eth0）、CoreDNS Pod 所在宿主机主网卡、cbr0 以及容器内。等待问题复现并拉通对比分析，评估丢包点。

## 现象和原因
### 5秒延时

如果 DNS 查询经常延时5秒才返回，通常是遇到内核 conntrack 冲突导致的丢包，根本原因是内核 conntrack 模块的 bug，netfilter 做 NAT 时可能发生资源竞争导致部分报文丢弃。
- 只有多个线程或进程，并发从同一个 socket 发送相同五元组的 UDP 报文时，有一定概率会发生。
- glibc，musl（Alpine Linux 的 libc 库）都使用 “parallel query”，即并发发出多个查询请求，因此易碰到这样的冲突，造成查询请求被丢弃。
- 由于 ipvs 也使用了 conntrack，使用 kube-proxy 的 ipvs 模式，因此无法避免该问题。

#### 规避方法
使用 LocalDNS 可以规避该问题。容器的 DNS 请求都发往本地的 DNS 缓存服务（dnsmasq，nscd 等)，不需要走 DNAT，也不会发生 conntrack 冲突。另外，也可避免 DNS 服务成为性能瓶颈。
使用 LocalDNS 缓存有两种方式：
- 每个容器自带一个DNS缓存服务。
- 每个节点运行一个DNS缓存服务，所有容器都把本节点的 DNS 缓存作为自己的 nameserver。


### 解析外部域名超时
可能原因：
- 上游 DNS 故障。
- 上游 DNS 的 ACL 或防火墙拦截了报文。

### 所有解析都超时
如果集群内某个 Pod 不管解析 Service 还是外部域名都失败，通常是 Pod 与集群 DNS 之间通信有问题。
可能原因：
- 节点防火墙没放开集群网段，导致如果 Pod 跟集群 DNS 的 Pod 不在同一个节点就无法通信，DNS 请求也就无法被收到。
- kube-proxy 异常。


