## 本地Helm客户端连接集群
### 下载Helm客户端
```
curl -O https://storage.googleapis.com/kubernetes-helm/helm-v2.10.0-linux-amd64.tar.gz
tar xzvf helm-v2.10.0-linux-amd64.tar.gz
sudo cp linux-amd64/helm /usr/local/bin/helm
```
### 配置Helm为Client-only
```
helm init --client-only
```

### 内网通过Helm客户端连接集群

####目标集群节点
可直接使用
####非目标集群节点
1. 修改目标集群Tiller服务的type为内网Loadbalancer模式,注意替换以下需要生产CLB的子网ID。
```
kubectl patch svc $(kubectl get svc -l app=helm,name=tiller -n kube-system -o=jsonpath={.items[0].metadata.name}) -n kube-system -p '{"metadata":{"annotations":{"service.kubernetes.io/qcloud-loadbalancer-internal-subnetid":"subnet-88888888"}},"spec":{"type":"LoadBalancer"}}'
```

2. 在目标集群节点上获取 $EXTERNALIP
```
  kubectl get svc -l app=helm,name=tiller -n kube-system -o=jsonpath={.items[0].status.loadBalancer.ingress[0].ip}
```
3. 在目标集群节点上获取 $PORT
```
kubectl get svc -l app=helm,name=tiller -n kube-system -o=jsonpath={.items[0].spec.ports[0].port}
```
4. 在Helm客户端节点上导如环境变量
```
export HELM_HOST=$EXTERNALIP:$PORT
```
5. helm ls命令验证

```
[centos ~]# helm ls
NAME     	REVISION	UPDATED                 	STATUS  	CHART          	APP VERSION	NAMESPACE
wordpress	1       	Mon Jan 21 14:22:30 2019	DEPLOYED	wordpress-5.0.1	5.0.1      	default
```

### 外网通过Helm客户端连接集群（不推荐使用）
