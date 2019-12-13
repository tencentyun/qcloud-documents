
高可用性（High Availability，HA）是指应用系统无中断运行的能力，通常可通过提高该系统的容错能力来实现。一般情况下，通过设置 `replicas` 给应用创建多个副本，可以适当提高应用容错能力，但这并不意味着应用就此实现高可用性。
本文为部署应用高可用的最佳实践，通过以下四种方式实现高可用性。您可结合实际情况，选择多种方式进行部署：
- [使用反亲和性避免单点故障](#PodAntiAffinity)
- [使用 PodDisruptionBudget 避免驱逐导致服务不可用](#PodDisruptionBudget)
- [使用 preStopHook 和 readinessProbe 保证服务平滑更新不中断](#update)
- [解决长连接服务扩容失效](#lapse)


## 使用反亲和性避免单点故障<span ID="PodAntiAffinity"></span>
Kubernetes 的设计理念为假设节点不可靠，节点越多，发生软硬件故障导致节点不可用的几率就越高。所以我们通常需要给应用部署多个副本，并根据实际情况调整 `replicas` 的值。该值如果为1 ，就必然存在单点故障。该值如果大于1但所有副本都调度到同一个节点，仍将无法避免单点故障。

为了避免单点故障，我们需要有合理的副本数量，还需要让不同副本调度到不同的节点。可以利用反亲和性来实现，示例如下：
```
affinity:
 podAntiAffinity:
   requiredDuringSchedulingIgnoredDuringExecution:
   - weight: 100
     labelSelector:
       matchExpressions:
       - key: k8s-app
         operator: In
         values:
         - kube-dns
     topologyKey: kubernetes.io/hostname
```
示例相关配置如下：
 - **requiredDuringSchedulingIgnoredDuringExecution**
此为反亲和性硬性条件，强调 Pod 调度时必须要满足该条件。当不存在满足该条件的节点时，Pod 将不会调度到任何节点（Pending）。
如果不使用这种硬性条件，也可以使用 `preferredDuringSchedulingIgnoredDuringExecution` 来指示调度器尽量满足反亲和性条件。当不存在满足该条件的节点时，Pod 也可以调度到某个节点。

- **labelSelector.matchExpressions**
标记该服务对应 Pod 中 labels 的 key 与 values。

- **topologyKey**
本示例中使用 `kubernetes.io/hostname`，表示避免 Pod 调度到同一节点。
如果您有更高的要求，例如避免调度到同一个可用区的节点，实现异地多活，则可以使用 `failure-domain.beta.kubernetes.io/zone`。
但通常情况下，同一个集群的节点都在一个地域，如果节点跨地域，即使使用专线，时延也会很大。如果无法避免调度到同一个地域的节点，则可以使用 `failure-domain.beta.kubernetes.io/region`。

## 使用 PodDisruptionBudget 避免驱逐导致服务不可用<span id="PodDisruptionBudget"></span>

驱逐节点是一种有损操作，该操作的过程如下：
1. 封锁节点（设置为不可调度，避免新的 Pod 调度上来）。
2. 删除该节点上的 Pod。
3. ReplicaSet 控制器检测到 Pod 减少，会重新创建一个 Pod，调度到新的节点上。

可以看出，以上过程是先删除再创建，并非滚动更新。因此在更新过程中，如果一个服务的所有副本都在被驱逐的节点上，则可能导致该服务不可用。通常，节点被驱逐导致服务不可用的情况会有以下两种：
- 服务存在单点故障，所有副本都在同一个节点，驱逐该节点时可能造成服务不可用。
 针对此情况，可参考 [使用反亲和性避免单点故障](#PodAntiAffinity) 进行处理。
- 服务在多个节点，但这些节点被同时驱逐，造成该服务涉及的所有副本同时被删，可能造成服务不可用。
  针对此情况，可通过配置 PDB（PodDisruptionBudget）来避免所有副本同时被删除。示例如下：
 - 示例一：保证驱逐时 zookeeper 至少有两个副本可用。
```
		apiVersion: policy/v1beta1
		kind: PodDisruptionBudget
		metadata:
		  name: zk-pdb
		spec:
		  minAvailable: 2
		  selector:
		    matchLabels:
		      app: zookeeper
```
 - 示例二：保证驱逐时 zookeeper 最多有一个副本不可用，相当于逐个删除并在其它节点重建。
```
		apiVersion: policy/v1beta1
		kind: PodDisruptionBudget
		metadata:
		  name: zk-pdb
		spec:
		  maxUnavailable: 1
		  selector:
		    matchLabels:
		      app: zookeeper
```
更多内容请参考官方文档 [Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb/)。

## 使用 preStopHook 和 readinessProbe 保证服务平滑更新不中断<span id="update"></span>
如果服务不做配置优化，默认情况下更新服务期间可能会产生部分流量异常，请参考以下步骤进行部署。

### 服务更新场景
通常情况下，服务更新场景会包含以下几种：
- 手动调整服务的副本数量。
- 手动删除 Pod 触发重新调度。
- 驱逐节点（主动或被动驱逐，会先删除 Pod 并在其它节点重建）。
- 触发滚动更新（例如，修改镜像 tag 升级程序版本）。
- HPA（HorizontalPodAutoscaler）自动对服务进行水平伸缩。
- VPA（VerticalPodAutoscaler）自动对服务进行垂直伸缩。

### 服务更新过程连接异常的原因
滚动更新时，Service 对应的 Pod 会被创建或销毁，Service 对应的 Endpoint 也会新增或移除相应的 `Pod IP:Port`，kube-proxy 会根据 Service 的 Endpoint 中的 `Pod IP:Port` 列表更新节点上的转发规则，而 kube-proxy 更新节点转发规则的动作并不是及时的。

转发规则更新不及时这一现象的出现，主要由于 Kubernetes 的设计理念中各个组件的逻辑是解耦的，它们各自使用 Controller 模式，listAndWatch 感兴趣的资源并做出相应的行为，使得从 Pod 创建或销毁到 Endpoint 更新再到节点上的转发规则更新的整个过程是异步的。

当转发规则没有及时更新时，服务更新期间就有可能发生部分连接异常。以下通过分析 Pod 创建和销毁到规则更新期间的两种情况，寻找服务更新期间部分连接异常发生的原因：


- <span id="CaseOne"></span>情况一：Pod 被创建，但启动速度较慢，Pod 还未完全启动就被 Endpoint Controller 加入到 Service 对应 Endpoint 的 `Pod IP:Port` 列表，kube-proxy watch 到更新也同步更新了节点上的 Service 转发规则（iptables/ipvs），如果此时有请求就可能被转发到还没完全启动完全的 Pod，此时 Pod 还无法正常处理请求，就会导致连接被拒绝。

- <span id="CaseTwo"></span>情况二：Pod 被销毁，但是从 Endpoint Controller watch 到变化并更新 Service 对应 Endpoint 再到 kube-proxy 更新节点转发规则这期间是异步的，存在时间差，在这个时间差内 Pod 可能已经完全被销毁了，但转发规则还未更新，就会造成新的请求依旧还能被转发到已经被销毁的 Pod，导致连接被拒绝。

### 平滑更新
- 针对 [情况一](#CaseOne)，可以给 Pod 中的 container 添加 readinessProbe（就绪检查）。通常是容器完全启动后监听一个 HTTP 端口，kubelet 发送就绪检查探测包，若正常响应则说明容器已经就绪，并将容器状态修改为为 Ready。当 Pod 中所有容器都 Ready 时，该 Pod 才会被 Endpoint Controller 加入 Service 对应 Endpoint 中的 `IP:Port` 列表，kube-proxy 再更新节点转发规则，完成更新后即使立刻有请求被转发到的新的 Pod，也能够确保正常处理连接，避免连接异常。

- 针对 [情况二](#CaseTwo)，可以给 Pod 中的 container 添加 preStop hook，使 Pod 真正销毁前先 sleep 等待一段时间，留出时间给 Endpoint controller 和 kube-proxy 更新 Endpoint 和转发规则，这段时间 Pod 处于 Terminating 状态，即便在转发规则更新完全之前有请求被转发到 Terminating 的 Pod，依然可以被正常处理，因为 Pod 还在 sleep 没有被真正销毁。

Yaml 示例如下：
```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      component: nginx
  template:
    metadata:
      labels:
        component: nginx
    spec:
      containers:
      - name: nginx
        image: "nginx"
        ports:
        - name: http
          hostPort: 80
          containerPort: 80
          protocol: TCP
        readinessProbe:
          httpGet:
            path: /healthz
            port: 80
            httpHeaders:
            - name: X-Custom-Header
              value: Awesome
          initialDelaySeconds: 15
          timeoutSeconds: 1
        lifecycle:
          preStop:
            exec:
              command: ["/bin/bash", "-c", "sleep 30"]
```
更多参考资料请前往 Kubernetes 官网 [Container probes](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#container-probes) 及 [Container Lifecycle Hooks](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/)。


## 解决长连接服务扩容失效<span id="lapse"></span>

在现网运营中，有很多场景为了提高效率一般都采用了建立长连接的方式来请求。如果客户端使用长连接请求服务端的方式，Kubernetes 的自动扩容将会失效。其原因是客户端长连接一直保留在之前的 Pod 容器中，未长连接至新扩容的 Pod 容器中，不仅导致 Kubernetes 按照步长扩容第一批 Pod 之后就停止了扩容操作，还导致新扩容的 Pod 未能承载请求，进而出现服务过载的情况，使得自动扩容失去意义。

针对以上问题，我们的解决方法是将长连接转换为短连接。该解决方法参考了 nginx keepalive 的设计，nginx 中 `keepalive_requests` 配置项设定一个 TCP 连接能处理的最大请求数。当该配置项达到设定值时（例如1000），服务端会在 HTTP 的 Header 头标记 `“Connection:close”`，并通知客户端处理完当前的请求后关闭连接，新的请求需要重新建立 TCP 连接。因此，在此过程中不会出现请求失败的情况，同时还达到了将长连接按需转换为短连接的目的。通过此方法，客户端和云 Kubernetes 服务端在处理完一批请求后不断的更新 TCP 连接，而自动扩容的新 Pod 即能接收到新的连接请求，从而解决了自动扩容失效的问题。

由于 Golang 并没有提供方法可以获取到每个连接处理过的请求数，我们重写了 `net.Listener` 和 `net.Conn`，注入请求计数器，对每个连接处理的请求进行计数，并通过 `net.Conn.LocalAddr()` 获得计数值，当判断达到阈值1000后，在返回的 Header 中插入 `“Connection:close”` 通知客户端关闭连接，重新建立连接来发起请求。

以上处理逻辑用 Golang 实现的示例代码如下：
```
package main

import (
    "net"
    "github.com/gin-gonic/gin"
    "net/http"
)

// 重新定义net.Listener
type counterListener struct {
    net.Listener
}

// 重写net.Listener.Accept(),对接收到的连接注入请求计数器
func (c *counterListener) Accept() (net.Conn, error) {
    conn, err := c.Listener.Accept()
    if err != nil {
        return nil, err
    }
    return &counterConn{Conn: conn}, nil
}

// 定义计数器counter和计数方法Increment()
type counter int

func (c *counter) Increment() int {
    *c++
    return int(*c)
}

// 重新定义net.Conn,注入计数器ct
type counterConn struct {
    net.Conn
    ct counter
}

// 重写net.Conn.LocalAddr()，返回本地网络地址的同时返回该连接累计处理过的请求数
func (c *counterConn) LocalAddr() net.Addr {
    return &counterAddr{c.Conn.LocalAddr(), &c.ct}
}

// 定义TCP连接计数器,指向连接累计请求的计数器
type counterAddr struct {
    net.Addr
    *counter
}

func main() {
    r := gin.New()
    r.Use(func(c *gin.Context) {
        localAddr := c.Request.Context().Value(http.LocalAddrContextKey)
        if ct, ok := localAddr.(interface{ Increment() int }); ok {
            if ct.Increment() >= 1000 {
                c.Header("Connection", "close")
            }
        }
        c.Next()
    })
    r.GET("/", func(c *gin.Context) {
        c.String(200, "plain/text", "hello")
    })
    l, err := net.Listen("tcp", ":8080")
    if err != nil {
        panic(err)
    }
    err = http.Serve(&counterListener{l}, r)
    if err != nil {
        panic(err)
    }
}
```
