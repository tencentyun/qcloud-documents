 ## 使用准备
#### virtual-kubelet 依赖文件：
- qcloud-vkubelet.yaml
- virtual-kubelet.yaml
- config/config.toml
- config/server.crt
- config/server.key

![][1]

详情请参考 [virtual kubelet 部署模版](https://main.qcloudimg.com/raw/bfb0dcd2aeb8c11295887f19fd0ca8a8/virtual%20kubelet%20node.tar.gz) ，该模版支持上传 TKE 节点，解压缩，修改特定参数后直接使用。

1. virtual-kubelet 启动配置文件 config.toml
```
    config.toml:  
    Region = "ap-guangzhou" #创建的 CIS 所在地域  
    Zone = "ap-guangzhou-4" #创建的 CIS 所在可用区
    Version = "2018-04-08"  
    SecretId = "" #CIS 用户的 SecretId  
    SecretKey = ""#CIS 用户的 SecretKey  
    CPU = "100"  
    Memory = "100Gi"  
    Pods = "50"  
```
其中，Region 和 Zone 的格式分别为`Region = "地域"`、`Zone = "可用区"`，上述代码以广州可用区4为例。
更多可用区信息，参考 [地域和可用区](https://cloud.tencent.com/document/product/858/17806)。

2. virtual-kubelet 10250 端口认证 certfile 及 keyfile：server.crt 和 server.key。  
该 10250 端口主要用于 kubectl logs 功能，当我们使用 kubectl logs 获取 Pod 容器日志时，kube-apiserver 会访问节点的10250端口，获取日志的相关信息。
在腾讯云 TKE 服务中，我们没有设置 10250 的端口认证，但是 kube-apiserver 需要以 HTTPS 方式访问节点的 10250 端口，否则 kube-apiserver 端将报错。因此，这里需要设置假的 server.key 和 server.crt 用于实现 kubectl logs 功能。

3. virtual-kubelet 的部署文件：
qcloud-vkubelet.yaml 创建 virtual-kubelet 对应的 serviceaccount，可以操作 Pod 等资源权限：
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
virtual-kubelet.yaml 创建 Pod 运行 virtual-kubelet 程序：	
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
         path: /home/ubuntu/for-show/config 
```
>?请自行修改为部署模版解压后的 config 文件夹路径，内包含 config.toml、server.crt 和 server.key。
>

## 使用步骤（ubuntu系统）
1. 登录安装了 kubectl 并已完成了初始化的 Kubernetes 节点服务器。
kubectl 安装和初始化可参考 [使用 kubectl 操作集群](https://cloud.tencent.com/document/product/457/8438)。

2. 执行以下命令：
```
kubectl create -f qcloud-vkubelet.yaml
```
执行结果示例：
```
    ubuntu@VM-66-110-ubuntu:~/for-show$ kubectl create -f qcloud-vkubelet.yaml  
    clusterrolebinding "vkubelet" created  
    clusterrole "vkubelet" created  
    serviceaccount "vkubelet" created  
```

3. 请修改virtual-kubelet.yaml最后一行hostPath内path参数为部署模版解压后的config文件夹路径，并执行以下命令：
```
kubectl create -f virtual-kubelet.yaml
```
执行结果示例：
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

## 示例及相关说明
### 示例
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
### 说明
1. 指定 CIS 运行所在的 vpcId 和 subnetId。
```
    kubernetes.io/cis.vpcId: vpc-lpaa5xe3
    kubernetes.io/cis.subnetId: subnet-7z46i306  
```

2. 指定 CIS 运行的规格，注意 request 和 limit 保持一致。
```
    resources:
      requests:
    memory: 1Gi
    cpu: "1"
      limits:
    memory: 1Gi
    cpu: "1"  
```

3. 指定 CIS 运行的节点是 virtual-kubelet。
```
    nodeName: virtual-kubelet
```

[1]:https://main.qcloudimg.com/raw/482b5bdebd58cc6940f1374dc790b3c2.png
