## 简介

### 组件介绍
该组件是基于游戏进程重启后保持共享内存的特性，自研的一种容器原地更新的 Kubernetes 工作负载（GameApp）控制器。

### 组件功能

- 支持原地更新，并保持共享内存（目前支持 image 更新）。
- 支持 GameApp Scale（HPA）特性。
- 支持 operator 高可用部署。
- 给重启的容器注入一次性元数据，可实现容器重启时控制是否清空共享内存的功能。


### 部署在集群内的 Kubernetes 对象

在集群内部署 GameApp Add-on，将在集群内部署以下 Kubernetes 对象：

| Kubernetes 对象名称             | 类型                       | 默认占用资源 | 所属 Namespaces |
| -------------------------- | ------------------------ | ------ | ------------ |
| gameapps.game.scr.ied.com  | CustomResourceDefinition | \      | \            |
| gameapp-operator           | ClusterRoleBinding       | \      | \            |
| gameapp-operator           | ClusterRole              | \      | \            |
| gameapp-operator           | ServiceAccount           | \      | default      |
| gameapp-controller-manager | StatefulSet              | 1C2G   | default      |


## 限制条件
- 支持 Kubernetes 1.10 以上版本的集群。
- 需设置 kube-apiserver 的启动参数为：` --feature-gates=CustomResourceSubresources=true`。

>?推荐您在 [腾讯云容器服务](https://cloud.tencent.com/product/tke2) 中购买 1.12.4 版本集群，无需修改任何参数，开箱可用。

## 使用方法

### 组件安装
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的【扩展组件】。
2. 在“扩展组件”管理页面上方，选择地域及需安装 GameApp 的集群，并单击【新建】。如下图所示：
![](https://main.qcloudimg.com/raw/887d95fb6d298edbb4e9a329440c22c1.png)
3. 在“新建扩展组件”页面，选择【GameApp 组件】后，单击【完成】即可安装成功。



### Yaml 创建并使用 GameApp 工作负载
#### 创建
1. 创建  `GameApp`  资源时，指定需注入的 env，并指定更新策略为原地更新。yaml 文件内容如下所示：
```
apiVersion: game.scr.ied.com/v1
kind: GameApp
metadata:
  name: "test-gameapp"
spec:
  replicas: $replicas
  selector:
    matchLabels:
      app: nginx
  serviceName: "test-gameapp"
  template:
    metadata:
      annotations:
        test: test
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx
        name: c1
        ports:
        - containerPort: 80
          name: web
        resources: {}
        volumeMounts:
        - mountPath: /dev/shm
          name: shm
        env:
        - name: clearSHM
          valueFrom:
            fieldRef:
              # 指定需要注入的 env
              fieldPath: metadata.annotations['oneshot.cloud.tencent.com/clearSHM'] 
      terminationGracePeriodSeconds: 10
      volumes:
      - emptyDir:
          medium: Memory
          sizeLimit: 1Gi
        name: shm
  updateStrategy:
    type: StableUpdate # 指定策略为原地更新
```

#### 使用
1. <span id="step1"></span>执行以下命令，设置升级镜像和一次性参数。
```
$ cat example/patch.yaml
template:
  metadata:
    annotations:
      oneshot.cloud.tencent.com/clearSHM: "true"
  spec:
    containers:
    - image: nginx:1.14        
      name: c1
$ kubectl patch gameapp test-gameapp --patch "$(cat patch.yaml)"
```
2. 执行以下命令，验证 env 是否注入成功。
```
kubectl exec test-gameapp-1 printenv clearSHM
true
```
执行结果返回 [步骤1](#step1) 中所设置的参数，则说明 env 注入成功。
4. 执行以下命令，仅设置升级镜像。
```
kubectl patch gameapp test-gameapp --type=json -p'[{"op":"replace","path":"/spec/template/spec/containers/0/image","value":"nginx:1.14"}]'
```
5. 再次执行以下命令，查看是否无 env 注入。
```
kubectl exec test-gameapp-1 printenv clearSHM
```
无返回值，则说明无 env 注入。
