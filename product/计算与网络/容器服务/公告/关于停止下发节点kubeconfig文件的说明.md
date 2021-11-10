>? 计划于北京时间2020年9月21日（周一）23:00 - 9月22日（周二）06:00进行操作停止下发 kubeconfig 文件。

## 问题背景
当前容器服务 TKE 在节点默认会放置带有 admin token 的 Kubeconfig 文件，用户可以通过此 Kubeconfig 文件方便的操作 Kubernetes 集群，但是当用户节点登录权限管理不慎，可能会导致集群面临安全风险，所以我们将停止下发 Kubeconfig 文件。

考虑到存量集群可能会在用户自定义脚本中使用 Kubeconfig 文件对集群进行一些初始化的操作，我们将下发一个权限相同但有效期仅为12小时的客户端证书，供用户初始化节点使用，证书过期之后，此 Kubeconfig 文件也相应作废。如仍需使用，请参考 [问题影响及处理措施](#QA) 进行操作。

>! 如果您出于某些特殊场景考虑，仍需要在节点安装之后默认带有长期 admin 权限而非12小时有效的 Kubeconfig 文件，或者遇到其他任何问题，您可通过 [在线咨询](https://cloud.tencent.com/online-service?from=doc_457) 联系我们。






## 问题影响及处理措施[](id:QA)

#### 问题现象
如用户习惯使用如下命令进行 TKE 集群登录节点进行 Kubectl 操作，命令及报错信息如下：
```bash
$ kubectl get node
The connection to the server localhost:8080 was refused - did you specify the right host or port?
```

```bash
$ kubectl get node
error: You must be logged in to the server (Unauthorized)
```

#### 处理措施
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 获取当前使用账号的凭证信息 Kubeconfig 文件，请参见 [获取凭证](https://cloud.tencent.com/document/product/457/46105#.E8.8E.B7.E5.8F.96.E5.87.AD.E8.AF.81)。
3. 获取 Kubeconfig 文件后，可以选择开启内网访问，也可直接使用 Kubernetes 的 service IP。
 - 开启内网访问：在集群详情页面中，选择左侧的**基本信息**，在“集群APIServer信息”中开启内网访问，并根据提示信息进行操作。
 - 使用 Kubernetes 的 service IP：在集群详情页面中，选择左侧的**服务与路由** > **Service**获取 default 命名空间下 Kubernetes 的 service IP。将 Kubeconfig 文件中 clusters.cluster.server 字段替换为 https://\<`IP`\>:443 即可。
4. 拷贝 Kubeconfig 文件内容到新节点上的 `$HOME/.kube/config` 下。
5. 访问 Kubeconfig 集群，使用 `kubectl get nodes` 测试是否连通。

## 特殊场景处理
#### 特殊场景
workload 已挂载 host 的 `/root/.kube/config` 或者 `/home/ubuntu/.kube/config` 文件进行使用。
#### 处理措施
正确使用 Kubernetes 的 serviceaccount 进行 incluster 方式访问集群，请参见 [Kubernetes官方文档](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)。
