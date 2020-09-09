## 问题背景
早期容器服务 TKE 产品上线时为了方便用户在节点上操作集群，在节点上下发了带有 admin token 的 Kubeconfig 文件。使用此文件可以方便地对 Kubernetes 集群进行读写操作，但同时也存在越权风险。我们已停止下发节点上的 Kubeconfig 文件，目前新增节点和集群将无法获取 Kubeconfig 文件，存量节点不受影响。

考虑到存量集群可能会在用户自定义脚本中使用 Kubeconfig 文件对集群进行一些初始化的操作，我们将临时下发一个权限相同但有效期仅为12小时的客户端证书，供用户初始化节点使用。

## 问题影响及处理措施



#### 问题现象
如用户习惯使用如下命令进行 TKE 集群登录节点进行 kubectl 操作，命令及报错信息如下：
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
获取 Kubeconfig 文件后，可以选择开启内网访问，也可直接使用 Kubernetes 的 service IP。
 在集群详情页面中，选择左侧的【服务与路由】>【Service】获取 default 命名空间下 Kubeconfig 的 service IP。将 Kubeconfig 文件中 clusters.cluster.server 字段替换为 https://\<`IP`\>:443 即可。
4. 拷贝 Kubeconfig 文件内容到新节点上的 `$HOME/.kube/config` 下。
5. 访问 Kubeconfig 集群，使用 `kubectl get nodes` 测试是否连通。

## 特殊场景处理
#### 特殊场景
workload 已挂载 host 的 `/root/.kube/config` 或者 `/home/ubuntu/.kube/config` 文件进行使用。
#### 处理措施
正确使用 Kubernetes 的 serviceaccount 进行 incluster 方式访问集群，请参见 [Kubernetes官方文档](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)。

>! 如果您出于某些特殊场景考虑，仍需要节点下发 admin token 的 Kubeconfig 文件，或者遇到其他任何问题，您可通过 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们。

