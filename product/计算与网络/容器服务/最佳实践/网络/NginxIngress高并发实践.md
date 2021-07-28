## 概述

Nginx Ingress Controller 基于 Nginx 实现 Kubernetes Ingress API。Nginx 是一款高性能网关，在实际生产环境运行时，需要对参数进行调优，以保证其充分发挥高性能的优势。[在 TKE 上部署 Nginx Ingress](https://cloud.tencent.com/document/product/457/47293) 中的部署 YAML 已经包含 Nginx 部分性能方面的参数优化。
本文将介绍针对 Nginx Ingress 全局配置与内核参数调优的方法及其原理，让 Nginx Ingress 更好的适配高并发业务场景。

## 内核参数调优
您可通过以下方式对 Nginx Ingress 进行内核参数调优，并可使用 initContainers 方式设置内核参数，详情请参见 [配置示例](#.E9.85.8D.E7.BD.AE.E7.A4.BA.E4.BE.8B)。
- [调高连接队列的大小](#.E8.B0.83.E9.AB.98.E8.BF.9E.E6.8E.A5.E9.98.9F.E5.88.97.E7.9A.84.E5.A4.A7.E5.B0.8F)
- [扩大源端口范围](#.E6.89.A9.E5.A4.A7.E6.BA.90.E7.AB.AF.E5.8F.A3.E8.8C.83.E5.9B.B4)
- [TIME_WAIT 复用](#time_wait-.E5.A4.8D.E7.94.A8)
- [调大最大文件句柄数](#.E8.B0.83.E5.A4.A7.E6.9C.80.E5.A4.A7.E6.96.87.E4.BB.B6.E5.8F.A5.E6.9F.84.E6.95.B0)
- [配置示例](#.E9.85.8D.E7.BD.AE.E7.A4.BA.E4.BE.8B)


### 调高连接队列的大小

在高并发环境下，如果连接队列过小，则可能导致队列溢出，使部分连接无法建立。进程监听 socket 的连接队列大小受限于内核参数 `net.core.somaxconn`，调整 somaxconn 内核参数的值即可增加 Nginx Ingress 连接队列。


进程调用 listen 系统监听端口时会传入一个 backlog 参数，该参数决定 socket 连接队列大小，且其值不大于 somaxconn 取值。Go 程序标准库在 listen 时，默认直接读取 somaxconn 作为队列大小，但 Nginx 监听 socket 时并不会读取 somaxconn，而是读取 `nginx.conf` 。在 `nginx.conf` 中的 listen 端口配置项中，可以通过 backlog 参数配置连接队列大小，来决定 Nginx listen 端口的连接队列大小。配置示例如下：
```
server {
    listen  80  backlog=1024;
    ...
```

如果未配置 backlog 值，则该值默认为511。backlog 参数详细说明如下：
```
backlog=number
   sets the backlog parameter in the listen() call that limits the maximum length for the queue of pending connections. By default, backlog is set to -1 on FreeBSD, DragonFly BSD, and macOS, and to 511 on other platforms.
```

在默认配置下，即便 somaxconn 的值配置超过511，但 Nginx 所监听端口的连接队列最大只有511，因此在高并发环境下可能导致连接队列溢出。

而 Nginx Ingress 不同，Nginx Ingress Controller 会自动读取 somaxconn 的值作为 backlog 参数，并写到生成的 [nginx.conf](https://github.com/kubernetes/ingress-nginx/blob/controller-v0.34.1/internal/ingress/controller/nginx.go#L592) 中，因此 Nginx Ingress 的连接队列大小只取决于 somaxconn 的大小，该取值在 TKE 中默认为4096。
在高并发环境下，建议执行以下命令，将 somaxconn 设为65535：
```
sysctl -w net.core.somaxconn=65535
```

### 扩大源端口范围

高并发环境将导致 Nginx Ingress 使用大量源端口与 upstream 建立连接，源端口范围从 `net.ipv4.ip_local_port_range` 内核参数中定义的区间随机选取。在高并发环境下，端口范围小容易导致源端口耗尽，使得部分连接异常。
TKE 环境创建的 Pod 源端口范围默认为32768 - 60999，建议执行以下命令扩大源端口范围，调整为1024 - 65535：
```
sysctl -w net.ipv4.ip_local_port_range="1024 65535"
```

### TIME_WAIT 复用

如果短连接并发量较高，所在 netns 中 TIME_WAIT 状态的连接将同样较多，而 TIME_WAIT 连接默认要等 2MSL 时长才释放，将长时间占用源端口，当这种状态连接数量累积到超过一定量之后可能会导致无法新建连接。

建议执行以下命令，为 Nginx Ingress 开启 TIME_WAIT 复用，即允许将 TIME_WAIT 连接重新用于新的 TCP 连接：
```
sysctl -w net.ipv4.tcp_tw_reuse=1
```

### 调大最大文件句柄数

Nginx 作为反向代理，每个请求将与 client 和 upstream server 分别建立一个连接，即占据两个文件句柄，因此理论上 Nginx 能同时处理的连接数最多是系统最大文件句柄数限制的一半。

系统最大文件句柄数由 `fs.file-max` 内核参数控制，TKE 默认值为838860。建议执行以下命令，将最大文件句柄数设置为1048576：
```
sysctl -w fs.file-max=1048576
```

### 配置示例
给 Nginx Ingress Controller 的 Pod 添加 initContainers 并设置内核参数。可参考以下代码示例：

```
initContainers:
- name: setsysctl
	image: busybox
	securityContext:
		privileged: true
	command:
	- sh
	- -c
	- |
		sysctl -w net.core.somaxconn=65535
		sysctl -w net.ipv4.ip_local_port_range="1024 65535"
		sysctl -w net.ipv4.tcp_tw_reuse=1
		sysctl -w fs.file-max=1048576
```

## 全局配置调优
除了内核参数需要调优，您可以通过以下方式对 Nginx 全局配置进行调优：
- [调高 keepalive 连接最大请求数](#.E8.B0.83.E9.AB.98-keepalive-.E8.BF.9E.E6.8E.A5.E6.9C.80.E5.A4.A7.E8.AF.B7.E6.B1.82.E6.95.B0)
- [调高 keepalive 最大空闲连接数](#.E8.B0.83.E9.AB.98-keepalive-.E6.9C.80.E5.A4.A7.E7.A9.BA.E9.97.B2.E8.BF.9E.E6.8E.A5.E6.95.B0)
- [调高单个 worker 最大连接数](#.E8.B0.83.E9.AB.98.E5.8D.95.E4.B8.AA-worker-.E6.9C.80.E5.A4.A7.E8.BF.9E.E6.8E.A5.E6.95.B0)
- [配置示例](#.E9.85.8D.E7.BD.AE.E7.A4.BA.E4.BE.8B2)

### 调高 keepalive 连接最大请求数

Nginx 针对 client 和 upstream 的 keepalive 连接，具备 keepalive_requests 参数来控制单个 keepalive 连接的最大请求数，默认值均为100。当一个 keepalive 连接中请求次数超过默认值时，将断开并重新建立连接。

如果是内网 Ingress，单个 client 的 QPS 可能较大，例如达到10000QPS，Nginx 将可能频繁断开跟 client 建立的 keepalive 连接，并产生大量 TIME_WAIT 状态连接。为避免产生大量的 TIME_WAIT 连接，建议您在高并发环境中增大 Nginx 与 client 的 keepalive 连接的最大请求数量，在 Nginx Ingress 的配置对应 `keep-alive-requests`，可以设置为10000，详情请参见 [keep-alive-requests](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#keep-alive-requests)。 

同样，Nginx 针对 upstream 的 keepalive 连接的请求数量的配置是 `upstream-keepalive-requests`，配置方法请参见 [upstream-keepalive-requests](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#upstream-keepalive-requests)。 

>! 在非高并发环境，不必配此参数。如果将其调高，可能导致负载不均，因 Nginx 与 upstream 保持的 keepalive 连接过久，导致连接发生调度的次数减少，连接过于“固化”，将使流量负载不均衡。

### 调高 keepalive 最大空闲连接数

Nginx 针对 upstream 可配置参数 keepalive。该参数为最大空闲连接数，默认值为320。在高并发环境下将产生大量请求和连接，而实际生产环境中请求并不是完全均匀，有些建立的连接可能会短暂空闲，在空闲连接数多了之后关闭空闲连接，将可能导致 Nginx 与 upstream 频繁断连和建连，引发 TIME_WAIT 飙升。
在高并发环境下，建议将 keepalive 值配置为1000，详情请参见 [upstream-keepalive-connections](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#upstream-keepalive-connections)。

### 调高单个 worker 最大连接数

`max-worker-connections` 控制每个 worker 进程可以打开的最大连接数，TKE 环境默认为16384。在高并发环境下建议调高该参数值，例如配置为65536，调高该值可以让 Nginx 拥有处理更多连接的能力，详情请参见 [max-worker-connections](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#max-worker-connections)。

### 配置示例

Nginx 全局配置通过 configmap 配置（Nginx Ingress Controller 会读取并自动加载该配置）。可参考以下代码示例：
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-ingress-controller
# nginx ingress 性能优化: https://www.nginx.com/blog/tuning-nginx/
data:
  # nginx 与 client 保持的一个长连接能处理的请求数量，默认100，高并发场景建议调高。
  # 参考: https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#keep-alive-requests
  keep-alive-requests: "10000"
  # nginx 与 upstream 保持长连接的最大空闲连接数 (不是最大连接数)，默认 320，在高并发下场景下调大，避免频繁建联导致 TIME_WAIT 飙升。
  # 参考: https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#upstream-keepalive-connections
  upstream-keepalive-connections: "200"
  # 每个 worker 进程可以打开的最大连接数，默认 16384。
  # 参考: https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#max-worker-connections
  max-worker-connections: "65536"
```




## 相关文档

- [在 TKE 上部署 Nginx Ingress](https://cloud.tencent.com/document/product/457/47293)
- [Nginx Ingress 配置参考](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/)
- [Tuning NGINX for Performance](https://www.nginx.com/blog/tuning-nginx/)
- [ngx_http_upstream_module 官方文档](http://nginx.org/en/docs/http/ngx_http_upstream_module.html)
