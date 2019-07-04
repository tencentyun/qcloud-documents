## 操作场景

本文档指导您通过本地 Helm 客户端连接集群。

## 操作步骤

### 下载 Helm 客户端

执行以下命令，下载 Helm 客户端。
```
curl -O https://storage.googleapis.com/kubernetes-helm/helm-v2.10.0-linux-amd64.tar.gz
tar xzvf helm-v2.10.0-linux-amd64.tar.gz
sudo cp linux-amd64/helm /usr/local/bin/helm
```

### 配置 Helm 为 Client-only

执行以下命令，将 Helm 配置为 Client-only。
```
helm init --client-only
```

### 内网通过 Helm 客户端连接集群

#### 目标集群节点

您可以直接使用。

#### 非目标集群节点

1. 执行以下命令，将目标集群 Tiller 服务的 type 修改为内网 Loadbalancer 模式。
>! 请将以下命令中 “service.kubernetes.io/qcloud-loadbalancer-internal-subnetid” 的值替换为需要生产 CLB 的子网 ID。
 
 ```
kubectl patch svc $(kubectl get svc -l app=helm,name=tiller -n kube-system -o=jsonpath={.items[0].metadata.name}) -n kube-system -p '{"metadata":{"annotations":{"service.kubernetes.io/qcloud-loadbalancer-internal-subnetid":"subnet-88888888"}},"spec":{"type":"LoadBalancer"}}'
```
2. 执行以下命令，在目标集群节点上获取 $EXTERNALIP。
```
  kubectl get svc -l app=helm,name=tiller -n kube-system -o=jsonpath={.items[0].status.loadBalancer.ingress[0].ip}
```
3. 执行以下命令，在目标集群节点上获取 $PORT。
```
kubectl get svc -l app=helm,name=tiller -n kube-system -o=jsonpath={.items[0].spec.ports[0].port}
```
4. 执行以下命令，在 Helm 客户端节点上导入环境变量。
```
export HELM_HOST=$EXTERNALIP:$PORT
```
5. 执行以下命令，命令验证 Helm 客户端。
```
[centos ~]# helm ls
NAME     	REVISION	UPDATED                 	STATUS  	CHART          	APP VERSION	NAMESPACE
wordpress	1       	Mon Jan 21 14:22:30 2019	DEPLOYED	wordpress-5.0.1	5.0.1      	default
```



