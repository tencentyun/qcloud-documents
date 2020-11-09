本文档介绍可能导致 Pod 一直处于 ImagePullBackOff 状态的几种情形，以及如何通过排查步骤定位异常原因。请按照以下步骤依次进行排查，定位问题后恢复正确配置即可。

## 可能原因
- HTTP 类型 Registry 地址未加入 insecure-registry
- HTTPS 自签发类型 Registry CA 证书未添加至节点
- 私有镜像仓库认证失败
- 镜像文件损坏
- 镜像拉取超时
- 镜像不存在

## 排查方法
### 检查 HTTP 类型 Registry 地址是否加入 insecure-registry

Dockerd 默认从 HTTPS 类型的 Registry 拉取镜像。当您使用 HTTP 类型的 Registry 时，请确保已将其地址添加到 insecure-registry 参数中，并重启或 reload Dockerd 使其生效。

### 检查 HTTPS 自签发类型 Registry CA 证书是否未添加至节点

当您使用 HTTPS 类型 Registry 且其证书属于自签发证书时，Dockerd 将会校验该证书，只有校验成功才可以正常使用镜像仓库。

为确保校验成功，需要将 Registry 的 CA 证书放置到以下位置： 
```
/etc/docker/certs.d/<Registry:port>/ca.crt
```

### 检查私有镜像仓库配置
若 Pod 未配置 imagePullSecret、配置的 Secret 不存在或者有误都会造成 Registry 认证失败，使 Pod 一直处于 ImagePullBackOff 状态。

### 检查镜像文件是否损坏
若 Push 的镜像文件损坏，下载成功后也不能正常使用，则需要重新 push 镜像文件。

### 检查镜像是否拉取超时
#### 现象描述
当节点上同时启动大量 Pod 时，可能会导致容器镜像下载需要排队。假设下载队列靠前位置已有许多大容量镜像且需较长的下载时间，则会导致排在队列靠后的 Pod 拉取超时。

默认情况下，kubelet 支持串行下载镜像。如下所示：
``` txt
--serialize-image-pulls   Pull images one at a time. We recommend *not* changing the default value on nodes that run docker daemon with version < 1.9 or an Aufs storage backend. Issue #10959 has more details. (default true)
```

#### 解决思路
必要情况下，为避免 Pod 拉取超时，可开启并行下载及控制并发。示例如下：
``` txt
--Registry-qps int32   If > 0, limit Registry pull QPS to this value.  If 0, unlimited. (default 5)
--Registry-burst int32   Maximum size of a bursty pulls, temporarily allows pulls to burst to this number, while still not exceeding Registry-qps. Only used if --Registry-qps > 0 (default 10)
```

### 检查镜像是否存在
镜像本身不存在也会导致 Pod 一直处于 ImagePullBackOff 状态，可以通过 kubelet 日志进行确认。如下所示：
``` bash
PullImage "imroc/test:v0.2" from image service failed: rpc error: code = Unknown desc = Error response from daemon: manifest for imroc/test:v0.2 not found
```
