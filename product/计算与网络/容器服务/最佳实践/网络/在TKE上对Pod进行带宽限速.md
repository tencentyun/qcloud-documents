## 操作场景
腾讯云容器服务 TKE 暂不支持 Pod 限速，但可通过修改 CNI 插件来支持此功能。本文档介绍如何在 TKE 上实现对 Pod 的带宽限速，您可结合实际场景进行操作。


## 使用限制
- 目前仅支持 Global Router 模式限速，并且开启后将不支持 HostPort 功能，可以用 HostNetwork 替代。
- 暂不支持 VPC-CNI 模式。


## 操作步骤
### 修改 CNI 插件
1. 请参考 [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)，登录 Pod 所在节点。
2. 执行以下命令，查看 `tke-cni-agent` 版本。
```
kubectl edit daemonset tke-cni-agent -n kube-system
```
如 `tke-cni-agent` 版本低于 v0.0.6+，则行执行以下命令替换镜像。
```
ccr.ccs.tencentyun.com/tkeimages/tke-cni-agent:v0.0.7
```
3. 执行以下命令，查看 `tke-bridge-agent` 版本。
```
kubectl edit daemonset tke-bridge-agent -n kube-system
```
如版本为非 v0.0.5，则请执行以下命令替换镜像，并添加 args `--port-mapping=false --bandwidth`。
```
ccr.ccs.tencentyun.com/tkeimages/tke-bridge-agent:v0.0.5
```


### Pod 指定 annotation
可使用社区提供的方式设置：
- 通过 `kubernetes.io/ingress-bandwidth` 此 annotation 指定入带宽限速。
- 通过 `kubernetes.io/egress-bandwidth` 此 annotation 指定出带宽限速。
示例如下：
``` yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
      annotations:
        kubernetes.io/ingress-bandwidth: 10M
        kubernetes.io/egress-bandwidth: 20M
    spec:
      containers:
      - name: nginx
        image: nginx
```

## 验证配置
您可通过以下两种方式验证配置是否成功：
- 登录 Pod 所在的节点，执行以下命令确认限制已经添加。
``` bash
tc qdisc show
```
返回类似如下结果，则限制已添加成功。
```
 qdisc tbf 1: dev vethc09123a1 root refcnt 2 rate 10Mbit burst 256Mb lat 25.0ms
 qdisc ingress ffff: dev vethc09123a1 parent ffff:fff1 ----------------
 qdisc tbf 1: dev 6116 root refcnt 2 rate 20Mbit burst 256Mb lat 25.0ms
```
- 执行以下命令，使用 iperf 测试。
```  bash
iperf -c <服务 IP> -p <服务端口> -i 1
```
返回类似如下结果，则说明限制已添加成功。
```
 ------------------------------------------------------------
 Client connecting to 172.16.0.xxx, TCP port 80
 TCP window size: 12.0 MByte (default)
 ------------------------------------------------------------
 [  3] local 172.16.0.xxx port 41112 connected with 172.16.0.xx port 80
 [ ID] Interval       Transfer     Bandwidth
 [  3]  0.0- 1.0 sec   257 MBytes  2.16 Gbits/sec
 [  3]  1.0- 2.0 sec  1.18 MBytes  9.90 Mbits/sec
 [  3]  2.0- 3.0 sec  1.18 MBytes  9.90 Mbits/sec
 [  3]  3.0- 4.0 sec  1.18 MBytes  9.90 Mbits/sec
 [  3]  4.0- 5.0 sec  1.18 MBytes  9.90 Mbits/sec
 [  3]  5.0- 6.0 sec  1.12 MBytes  9.38 Mbits/sec
 [  3]  6.0- 7.0 sec  1.18 MBytes  9.90 Mbits/sec
 [  3]  7.0- 8.0 sec  1.18 MBytes  9.90 Mbits/sec
 [  3]  8.0- 9.0 sec  1.18 MBytes  9.90 Mbits/sec
 [  3]  9.0-10.0 sec  1.12 MBytes  9.38 Mbits/sec
 [  3]  0.0-10.3 sec   268 MBytes   218 Mbits/se
```

   
