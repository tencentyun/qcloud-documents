## virtual-kubelet 依赖文件列表

![][1]

 详情请参考 [virtual kubelet 部署模版](https://main.qcloudimg.com/raw/bfb0dcd2aeb8c11295887f19fd0ca8a8/virtual%20kubelet%20node.tar.gz) （该模版支持上传 CCS 节点，解压缩，修改特定参数后直接使用）。

#### 1. virtual-kubelet 启动配置文件：`config.toml`
```
    config.toml:  
    Region = "ap-guangzhou"(创建的cis所在地域)  
    Zone = "ap-guangzhou-4"(创建的cis所在区)  
    Version = "2018-04-08"  
    SecretId = ""(cis用户的secretId)   
    SecretKey = ""（cis用户的secretKey）  
    CPU = "100"  
    Memory = "100Gi"  
    Pods = "50"  
```

 **目前 cis 支持的可选地域和可用区有：  **

|Region|Zone|说明|
|:--|:--|:--|
| "ap-guangzhou" | "ap-guangzhou-2" | 广州可用区2 |
| "ap-guangzhou" | "ap-guangzhou-3" | 广州可用区3 |
| "ap-guangzhou" | "ap-guangzhou-4" | 广州可用区4 |
| "ap-beijing" | "ap-beijing-1" | 北京可用区1 |
| "ap-beijing" | "ap-beijing-2" | 北京可用区2 |
| "ap-beijing" | "ap-beijing-3" | 北京可用区3 |
| "ap-shanghai" | "ap-shanghai-1" | 上海可用区1 |
| "ap-shanghai" | "ap-shanghai-2" | 上海可用区2 |
| "ap-shanghai" | "ap-shanghai-3" | 上海可用区3 |

#### 2. virtual-kubelet 10250 端口认证 certfile 及 keyfile：server.crt 和 server.key  
该端口主要用于 kubectl logs 功能，当我们使用 kubectl logs 获取 pod 容器日志时，kube-apiserver 会访问节点的 10250 端口，获取日志的相关信息，尽管在腾讯云 ccs 服务中，10250 的端口认证我们没有设置，但是 kube-apiserver 需要以 https 方式访问节点的 10250 端口，否则 kube-apiserver 端将报错。因此，这里需要设置假的 server.key 和 server.crt 用于实现 kubectl logs 功能。

#### 3. virtual-kubelet 的部署文件：`qcloud-vkubelet.yaml` 和 `virtual-kubelet.yaml`
    qcloud-vkubelet.yaml (创建 virtual-kubelet 对应的 serviceaccount，可以操作 pod 等资源权限）  
	 
```
    ---  
    apiVersion: rbac.authorization.k8s.io/v1beta1  
    kind: ClusterRoleBinding  
    metadata:  
      name: vkubelet  
    subjects:  
    - kind: ServiceAccount  
      name: vkubelet  
      namespace: default  
    roleRef:  
      kind: ClusterRole  
      name: vkubelet  
      apiGroup: rbac.authorization.k8s.io  
    ---  
    apiVersion: rbac.authorization.k8s.io/v1beta1  
    kind: ClusterRole  
    metadata:  
      name: vkubelet  
      labels:  
    k8s-app: vkubelet  
    rules:  
    - apiGroups: [""] # "" indicates the core API group  
      resources:  
      - namespaces  
      - pods  
      - pods/status  
      - nodes  
      - nodes/status  
      - secrets  
      - configmaps  
      verbs:  
      - create  
      - update  
      - get  
      - watch  
      - list  
      - delete  
    ---  
    apiVersion: v1  
    kind: ServiceAccount  
    metadata:  
      name: vkubelet  
      namespace: default  
      labels:  
    k8s-app: vkubelet  
    ---
```
	
  virtual-kubelet.yaml:(创建 pod 运行 virtual-kubelet 程序)  
		
```
    apiVersion:  v1  
    kind: Pod  
    metadata:  
      name: virtual-kubelet  
      labels:  
    k8s-app: vkubelet  
    spec:  
      serviceAccountName: vkubelet  
      restartPolicy: "Never"  
      imagePullSecrets:  
      - name: qcloudregistrykey  
      containers:  
      - name: virtual-kubelet  
    image: ccr.ccs.tencentyun.com/tencentyun/virtual-kubelet:dev  
    imagePullPolicy: Always  
    env:  
    - name: KUBELET_PORT  
      value: "10250"  
    - name: APISERVER_CERT_LOCATION  
      value: /etc/virtual-kubelet/server.crt  
    - name: APISERVER_KEY_LOCATION  
      value: /etc/virtual-kubelet/server.key  
    - name: VKUBELET_POD_IP  
      valueFrom:  
    fieldRef:  
      fieldPath: status.podIP  
    volumeMounts:  
    - name: credentials  
      mountPath: "/etc/virtual-kubelet"  
    command: ["/usr/bin/virtual-kubelet"]  
    args: ["--provider", "qcloud", "--namespace", "default", "--provider-config", "/etc/virtual-kubelet/  config.toml"]  
      volumes:  
      - name: credentials
    hostPath:
      path: /home/ubuntu/for-show/config (config 文件夹包含 config.toml, server.crt 和 server.key)
```

## 使用步骤
1. 登录安装了 kubectl 并已完成了初始化的 Kubernetes 节点服务器
kubectl 安装和初始化可参考 [使用 kubectl 操作集群](https://cloud.tencent.com/document/product/457/8438)。

2. 执行` kubectl create -f qcloud-vkubelet.yaml`
```
    ubuntu@VM-66-110-ubuntu:~/for-show$ kubectl create -f qcloud-vkubelet.yaml  
    clusterrolebinding "vkubelet" created  
    clusterrole "vkubelet" created  
    serviceaccount "vkubelet" created  
```

3. 执行 `kubectl create -f virtual-kubelet.yaml`
```
    ubuntu@VM-66-110-ubuntu:~/for-show$ kubectl create -f virtual-kubelet.yaml  
    pod "virtual-kubelet" created  
    ubuntu@VM-66-110-ubuntu:~/for-show$ kubectl get po  
    NAME  READY STATUSRESTARTS   AGE  
    virtual-kubelet   1/1   Running   0  3s  
    ubuntu@VM-66-110-ubuntu:~/for-show$ kubectl get no
    NAME           STATUS     ROLES   AGE   VERSION  
    192.168.66.110  Ready      none    3d   v1.8.7-qcloud  
    192.168.66.16   Ready      none    9d   v1.8.7-qcloud  
    virtual-kubelet Ready      agent   5s   v1.8.3  
```

## 示例及注意事项
```
    ubuntu@VM-66-110-ubuntu:~/for-show$ cat busybox-pod-pass.yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: busybox
      annotations:
    kubernetes.io/cis.vpcId: vpc-lpaa5xe3
    kubernetes.io/cis.subnetId: subnet-7z46i306
      labels:
    qcloud-app: busybox
    spec:
      containers:
      - image: busybox
    imagePullPolicy: Always
    name: busybox
    resources:
      requests:
    memory: 1Gi
    cpu: "1"
      limits:
    memory: 1Gi
    cpu: "1"
    command: ["/bin/sh"]
    args: ["-c", "while true; do echo hello world; sleep 2; done"]
      dnsPolicy: ClusterFirst
      nodeName: virtual-kubelet  
```

1. 指定 cis 运行所在的 vpcId 和 subnetId
```
    kubernetes.io/cis.vpcId: vpc-lpaa5xe3
    kubernetes.io/cis.subnetId: subnet-7z46i306  
```

2. 指定 cis 运行的规格，注意 request 和 limit 保持一致
```
    resources:
      requests:
    memory: 1Gi
    cpu: "1"
      limits:
    memory: 1Gi
    cpu: "1"  
```

3. 指定 cis 运行的节点是 virtual-kubelet
```
    nodeName: virtual-kubelet
```  

[1]:https://main.qcloudimg.com/raw/482b5bdebd58cc6940f1374dc790b3c2.png
[1]:https://main.qcloudimg.com/raw/482b5bdebd58cc6940f1374dc790b3c2.png
