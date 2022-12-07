本文档介绍 TKE 集群中多场景下可能发生的常见网络问题，并给出对应的排查思路。当遇到此类问题时，建议您首先按照下文中的检查建议进行排查，若确认检查项无误后仍不能正常访问，请您 [联系我们](https://cloud.tencent.com/document/product/457/59560) 寻求帮助。

## 集群中不同节点上的容器（Pod）无法互访[](id:PodsOnDifferentNodes) 
同一集群中不同节点上的 Pod 可以直接互访，当出现一个节点上 Pod 无法访问其他节点上 Pod 时，建议您进行如下检查：
1. 检查上述不同节点间是否可以互访。
2. 检查节点安全组是否正确放通容器网段和对端节点所在的 VPC 网段或 VPC 子网网段。


## 同一个 VPC 内的节点与容器（Pod）无法互访
同一个 VPC 内的节点和 Pod 可以直接互访，当出现无法互访的情况时，建议您进行如下检查：
1. 检查对端节点和 Pod 所在节点是否可以互访。
- Pod 所在节点的安全组是否正确放通对端节点所在的 VPC 子网网段。
- 对端节点的安全组是否正确放通容器网段。

## 不同 VPC 内的节点与容器（Pod）或容器（Pod）与容器（Pod）间无法互访
不同 VPC 间的互访需要先通过 [云联网](https://cloud.tencent.com/document/product/877/18768) 或 [对等连接](https://cloud.tencent.com/document/product/553/18836) 完成打通。如果打通之后仍出现无法互访的情况，建议您进行如下检查：
1. 检查节点与节点是否可以互访。
- 检查对端节点的安全组是否正确放通 VPC 网段和容器网段。
- 检查 Pod 所在节点的安全组是否正确放通对端节点所在的 VPC 网段或 VPC 子网网段。

如果容器（Pod）与容器（Pod）间无法互访，需进一步执行如下检查：
1. 检查 Pod 所在节点的安全组是否正确放通对端 VPC 网段（或者节点所在的 VPC 子网网段）和容器网段。
- 如需查看 Pod 的源 IP ，可执行以下命令，进一步修改 `ip_masq_agent` 的配置，彼此增加对方容器网段。
```
kubectl -n kube-system edit configmap ip-masq-agent-config
```




## IDC 与容器（Pod）无法访问
IDC 与 Pod 互访需要先通过 [云联网](https://cloud.tencent.com/document/product/877/18768) 或 [专线网关](https://cloud.tencent.com/document/product/216/19255) 完成打通。如果打通之后仍出现无法互访的情况，建议您进行如下检查：
 1. IDC 防火墙是否放通容器网段和 CVM 网段。
 - CVM 安全组是否放通 IDC 网段。
 - 检查 IDC 是否使用 BGP 协议：
  - 若未使用 BGP 协议，则需在 IDC 内配置访问容器网段下一跳路由到专线网关。
  - 若使用 BGP 协议，则会自动同步，通常不需要任何配置。除非 IDC 有特殊的静态配置，可联系运维人员配访问容器网段下一跳到专线网关。

>?
> - 如需在 IDC 中查看 Pod 的 IP，则需要放通 IDC 网段。
> - 默认情况下，除 VPC 之外的包会经过 SNAT 处理转换为 NodeIP。放通 IDC 网段时需配置为不经过 SNAT 处理。
> - 放通 IDC 网段的方法为：执行命令 `kubectl -n kube-system edit configmap ip-masq-agent-config `，修改 ip-masq-agent 配置，并将 IDC 网段添加到 NonMasqueradeCIDRs 列表中。





## 相关操作

### 查看节点上的 iptables 或 ipvs 转发规则
您可以通过执行以下命令，查看节点上的 iptables 或者 ipvs 转发规则。
- 执行以下命令，检查 iptables 转发规则。
```
iptables-save
```
- 执行以下命令，检查 ipvs 转发规则。
```
ipvsadm -Ln -t/-u ip:port
```

### 抓包命令
以下抓包命令可用于分析集群内不同节点上的容器（Pod）互访不通的情况。
- 执行以下命令，在源 Pod 的节点上抓网卡 eth0 的包。
```
tcpdump -nn -vv -i eth0 host <对端pod-ip>
```
- 执行以下命令，在对端 Pod 的节点上抓网卡 eth0 的包。
```
tcpdump -nn -vv -i eth0 host <源pod-ip>
```
- 执行以下命令，在对端 Pod 的 netns 中抓网卡 eth0 的包。
```
tcpdump -nn -vv -i eth0 port <请求的端口号>
```

### 容器内抓包定位网络问题
在使用 Kubernetes 运行应用的时候，可能会遇到一些网络问题，其中比较常见的是服务端无响应（超时）及回包内容不正常。如果您无法在相关配置上定位到问题点，则需要确认数据包最终是否被路由到容器里，或者报文到达容器的内容和出容器的内容是否符合预期，并通过分析报文进一步缩小问题范围。本文提供脚本，可一键进入容器网络命名空间（netns），并使用宿主机上的 tcpdump 进行抓包。

#### 使用脚本一键进入 Pod netns 抓包
当发现某个服务不通时，建议将其副本数调为1，并按照以下步骤进行抓包。
1. 执行以下命令，获取该 Pod 副本所在的节点和 Pod 名称。
```
kubectl get pod -o wide
```
2. 登录 Pod 所在节点，将如下脚本粘贴到 Shell ，注册函数到当前登录的 Shell 。[](id:StepTwo)
```
function e() {
    set -eu
    ns=${2-"default"}
    pod=`kubectl -n $ns describe pod $1 | grep -A10 "^Containers:" | grep -Eo 'docker://.*$' | head -n 1 | sed 's/docker:\/\/\(.*\)$/\1/'`
    pid=`docker inspect -f {{.State.Pid}} $pod`
    echo "entering pod netns for $ns/$1"
    cmd="nsenter -n --target $pid"
    echo $cmd
    $cmd
}
```
您可前往 [脚本原理](#principle) 了解并开始使用脚本。
3. 执行以下命令，一键进入 Pod 所在的 netns。
```
e POD_NAME NAMESPACE
```
具体示例如下：
```
e istio-galley-58c7c7c646-m6568 istio-system 
e proxy-5546768954-9rxg6 # 省略 NAMESPACE 默认为 default
```
>?进入 Pod 所在的 netns 之后，可在宿主机上执行 `ip a` 或 `ifconfig` 命令来查看容器的网卡，执行 `netstat -tunlp` 命令查看当前容器的监听端口。
>
4. 执行以下命令，使用 tcpdump 进行抓包。
```
tcpdump -i eth0 -w test.pcap port 80
```

#### 使用 wireshark 分析报文
您可以执行 `Ctrl+C` 操作停止抓包，使用 `scp` 或 `sz` 命令将抓取的包下载到本地使用 `wireshark` 分析。分析过程中，您可能会用到以下常见的 `wireshark` 过滤语法：
- 使用 telnet 连接并发送测试文本，例如 `"lbtest"`。  
执行以下命令，查看已发送的测试报文是否传递到容器。
```
tcp contains "lbtest"
```
- 如果容器提供 HTTP 服务，则可使用 curl 发送测试路径请求。
执行以下命令过滤 uri，查看报文是否传递到容器。
```
http.request.uri=="/mytest"
```

### 脚本原理[](id:principle)
- 查看指定 Pod 运行的容器 ID。
```
kubectl describe pod <pod> -n mservice
```	
- 获得容器进程的 Pid。
```
docker inspect -f {{.State.Pid}} <container>
```	
-  进入该容器的 network namespace。
```
nsenter -n --target <PID>
```
上述脚本依赖的宿主机命名包含有：kubectl、docker、nsenter、grep、head、sed。

### 查看节点安全组配置[](id:config)
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 选择集群 ID，进入集群详情页。
3. 选择左侧导航栏中的**节点管理** > **节点**。
4. 在“节点列表”页面，选择需查看安全组的节点 ID。
5. 在节点管理页面，选择**详情**页签，并单击“主机信息”中的节点 ID。如下图所示：
![](https://main.qcloudimg.com/raw/daf3eef9a726083c3495300161df8bae.png)
6. 在节点“基本信息”页面中，选择**安全组**页签，并在页面中查看该节点的安全组是否正确放通30000-32768端口区间。如下图所示：
![](https://main.qcloudimg.com/raw/7936719a74fa84eb6665aab4ef98ab71.png)

