
## 背景

早期容器服务 TKE 产品上线时考虑安全不足，为了方便用户在节点上操作集群，在节点上下发了带有 admin token 的 kubeconfig 文件。使用此文件可以方便地对 Kubernetes 集群进行读写操作，但同时也存在越权风险，如用户节点被黑客攻破，黑客即可通过 admin token 的 kubeconfig 文件随意操作整个集群。由此我们将停止下发节点上的 kubeconfig 文件，目前仅涉及增量节点和集群，存量节点不受影响。

考虑到存量集群可能会在用户自定义脚本中使用此 kubeconfig 文件对集群进行一些初始化的操作，我们将临时下发一个权限相同但有效期仅为12小时的客户端证书，供用户初始化节点使用。

## 影响及处理措施

### 问题1：用户习惯，可能您使用TKE集群习惯登录节点进行kubectl操作，后续将无法直接在节点上使用。

#### 现象

```bash
$ kubectl get node
The connection to the server localhost:8080 was refused - did you specify the right host or port?
# 或者
$ kubectl get node
error: You must be logged in to the server (Unauthorized)
```

#### 处理措施

建议您从控制台-集群详情页-集群APIServer信息-Kubeconfig（或者通过云API调用DescribeClusterKubeconfig）中获取到kubeconfig文件之后拷贝到节点使用。

1. 打开集群详情页获取kubeconfig文件（或者通过云API调用DescribeClusterKubeconfig），可以选择开启内网访问，也可直接使用kubernetes的service ip。

   ![](https://main.qcloudimg.com/raw/62ca44dcbb1093a1a14d1b626c694da9.png)

2. 也可获取到default命名空间下的kubernetes的serviceIP，替换掉kubeconfig文件中clusters.cluster.server字段为下图中的https://\<IP\>:443即可。

   ![](https://main.qcloudimg.com/raw/48af13c18a50cf5b9ce4108f3f9543b7.png)

3. 拷贝内容到新节点上的$HOME/.kube/config下

4. 访问kubernetes集群，使用kubectl get nodes 测试是否连通

## 特殊场景处理

1. workload有挂载host的/root/.kube/config（或者/home/ubuntu/.kube/config）文件进行使用

   **处理措施**：正确使用kubernetes的serviceaccount进行incluster方式访问集群，参考[这里](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)。

2. 如果您处于某些特殊场景考虑，需要节点仍然下发admin token的kubeconfig文件，或者其他任何问题，可以提交工单，联系我们。

