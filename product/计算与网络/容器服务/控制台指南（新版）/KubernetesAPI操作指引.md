## 操作场景
本文介绍如何在腾讯云容器服务集群中使用 Kubernetes API 进行相关操作。例如，查看集群下所有 namespaces、查看指定 namespaces 下所有 Pods 及 Pod 的增加、删除、查询操作。



## 操作步骤

### 获取集群访问凭证 kubeconfig
1. 参考 [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)，登录集群节点。
2. 执行以下命令，获取集群访问凭证（kubeconfig）文件的位置。
```
ps -ef |grep kubelet|grep -v grep
```
返回结果如下图所示，访问凭证位置为：`/etc/kubernetes/kubelet-kubeconfig`。
![](https://main.qcloudimg.com/raw/0dd677da751b8caf8501168c945ed760.png)
3. 执行以下命令，进入目录 kubernetes。
```
cd /etc/kubernetes
```
4. 依次执行以下命令，分别从 kubeconfig 文件中获取 ca、key 和 apiserver 信息。
```
cat  ./kubelet-kubeconfig |grep client-certificate-data | awk -F ' ' '{print $2}' |base64 -d > client-cert.pem
```
```
cat  ./kubelet-kubeconfig |grep client-key-data | awk -F ' ' '{print $2}' |base64 -d > client-key.pem
```
```
APISERVER=`cat  ./kubelet-kubeconfig |grep server | awk -F ' ' '{print $2}'`
```
执行命令 `ls`，可查看在 kubernetes 目录下已生成的 `client-cert.pem`、`client-key.pem` 文件。如下图所示：
![](https://main.qcloudimg.com/raw/8d0741a5db89999eb23a757c6a3dda46.png)


### 使用 CURL 命令操作 Kubernetes API
1. 执行以下命令，查看当前集群中所有 namespaces。
```
curl --cert client-cert.pem --key client-key.pem -k $APISERVER/api/v1/namespaces
```
>?若在执行 `curl` 命令时，出现权限不足的报错，则请参考 [放通集群访问权限](#Authority) 步骤进行解决。
>
2. 执行以下命令，查看 kube-system 命名空间下的所有 Pods。
```
curl --cert client-cert.pem --key client-key.pem -k $APISERVER/api/v1/namespaces/kube-system/pods
```



### Pod 生命周期管理
>?以下步骤中所创建的文件及文件内容均为示例，您可根据实际需要进行自定义创建。
>

#### 使用 JSON 格式创建 Pod
1. 执行以下命令，创建并打开 JSON 文件。
```
vim nginx-pod.json
```
2. 在 JSON 文件中，输入以下内容：
```
     {
         "apiVersion":"v1",
         "kind":"Pod",
         "metadata":{
             "name":"nginx",
             "namespace": "default"
         },
         "spec":{
             "containers":[
                 {
                     "name":"nginx-test",
                     "image":"nginx",
                     "ports":[
                         {
                             "containerPort": 80
                         }
                     ]
                 }
             ]
         }
     }
```
3. 执行以下命令，创建 Pod。
```
curl --cert client-cert.pem --key client-key.pem -k $APISERVER/api/v1/namespaces/default/pods -X POST --header 'content-type: application/json' -d@nginx-pod.json
```

#### 使用 YAML 格式创建 Pod
1. 执行以下命令，创建并打开 YAML 文件。
```
vim nginx-pod.json
```
2. 在 YAML 文件中，输入以下内容：
```
     apiVersion: v1
     kind: Pod
     metadata:
       name: nginx
       namespace: default
     spec:
       containers:
       - name: nginx-test
         image: nginx
         ports:
         - containerPort: 80
```
3. 执行以下命令，创建 Pod。
```
curl --cert client-cert.pem --key client-key.pem -k $APISERVER/api/v1/namespaces/default/pods -X POST --header 'content-type: application/yaml' --data-binary @nginx-pod.yaml
```


  
#### 查询 Pod 状态
您可执行以下命令，查询 Pod 状态。
```
curl --cert client-cert.pem --key client-key.pem -k $APISERVER/api/v1/namespaces/default/pods/nginx
```

#### 查询 Pod logs
您可执行以下命令，查询 Pod logs。
```
curl --cert client-cert.pem --key client-key.pem -k $APISERVER/api/v1/namespaces/default/pods/nginx/log
```

#### 查询 Pod 的 metrics 数据
您可执行以下命令，通过 metric-server api 查询 Pod 的 metrics 数据。
```
curl --cert client-cert.pem --key client-key.pem -k $APISERVER/apis/metrics.k8s.io/v1beta1/namespaces/default/pods/nginx
```

#### 删除 Pod
您可执行以下命令，删除 Pod。
```
curl --cert client-cert.pem --key client-key.pem -k $APISERVER/api/v1/namespaces/default/pods/nginx -X DELETE
```


## 相关操作
### 放通集群访问权限<span id="Authority"></span>
若在执行 `curl` 命令时，出现如下所示错误，则说明需放通集群的 [访问权限](https://kubernetes.io/zh/docs/reference/access-authn-authz/rbac/)。
![](https://main.qcloudimg.com/raw/c50eca5e28b0cdbb4cf00a378a773205.png)
您可通过以下两种方式进行授权操作：
- 方式一（推荐）：参考文档 [使用预设身份授权](https://cloud.tencent.com/document/product/457/46105) 及 [自定义策略授权](https://cloud.tencent.com/document/product/457/46106) 通过容器服务控制台进行 RBAC 授权。
- 方式二：执行以下命令进行授权，但在生产集群中，不建议盲目地将帐户提升为集群管理员权限 cluster-admin。
```
kubectl create clusterrolebinding cluster-system-anonymous --clusterrole=cluster-admin --user=system:anonymous
```

