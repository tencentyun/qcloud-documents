

## 操作场景
边缘容器服务 TKE Edge 提供 ServiceGroup 特性，只需两个 yaml 文件即可轻松实现上百地域的服务部署，且无需进行应用适配或改造。本文以在边缘部署 nginx 为例。若您希望在多个节点组内分别部署 nginx 服务，请参考本文依次执行以下步骤。

## 操作步骤


### 确定 ServiceGroup 唯一标识

该步骤进行逻辑规划，无需任何实际操作。边缘容器将目前要创建的 ServiceGroup 逻辑标记使用的 UniqKey 设置为 zone。

### 通过 Label 将边缘节点分组[](id:Step2)

该步骤需要通过 TKE Edge 控制台或者 kubectl 对边缘节点打 Label。TKE Edge 控制台操作步骤如下：

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**边缘集群**。
2. 选择需要编辑标签的节点所在的集群 ID，进入该集群管理页面。
3. 选择**节点管理** > **节点**，进入节点列表页，如下图所示：
   ![](https://main.qcloudimg.com/raw/712450952968557eefd23e4833deaa5f.png)
4. 选择需要编辑标签的节点所在行右侧的**更多** > **编辑标签**。
5. 在弹出的“编辑标签”窗口，参考以下信息新增 Label。如下图所示：
   ![](https://main.qcloudimg.com/raw/28596c7e60903b064df642f3a823427e.png)   
   - 参考 [整体架构](https://cloud.tencent.com/document/product/457/46923#OverallStructure) 章节，选择 Node12及 Node14编辑 Label：`zone=nodeunit1`。Node21及 Node23编辑 Label：`zone=nodeunit2`。
   - Label 的 key 需与 ServiceGroup 的 UniqKey 一致，value 是 NodeUnit 的唯一key。value 相同的节点表示属于同一个 NodeUnit。
   - 如果同一个集群中有多个 ServiceGroup，请为每一个 ServiceGroup 分配不同的 Uniqkey。
6. 单击**确定**即可。

### 部署 DeploymentGrid

```
apiVersion: superedge.io/v1
kind: DeploymentGrid
metadata:
    name: deploymentgrid-demo
    namespace: default
spec:
    gridUniqKey: zone
    template:
      selector:
        matchLabels:
          appGrid: nginx
      replicas: 2
      template:
        metadata:
          labels:
            appGrid: nginx
        spec:
          containers:
          - name: nginx
            image: nginx:1.7.9
            ports:
            - containerPort: 80
              protocol: TCP
```

### 部署 ServiceGrid

```
apiVersion: superedge.io/v1
kind: ServiceGrid
metadata:
    name: servicegrid-demo
    namespace: default
spec:
    gridUniqKey: zone
    template:
      selector:
        appGrid: nginx
      ports:
      - protocol: TCP
        port: 80
        targetPort: 80
```
>?可查看此处 gridUniqKey 字段设置为 zone，因此对应 [通过 Label 将边缘节点分组](#Step2) 步骤中对节点进行分组时 Label 的 key 也应设置为 zone。如果有三组节点，则分别添加 `zone: zone-0`，`zone: zone-1 `，`zone: zone-2 `的 Label 即可。

这时，每组节点内都有了 nginx 的 Deployment 和对应的 Pod，在节点内访问统一的 service-name 也只会将请求发向本组的节点。验证方式如下：

```
[root@VM_1_34_centos ~]# kubectl get deploy
NAME                         READY   UP-TO-DATE   AVAILABLE   AGE
deploymentgrid-demo-zone-0   2/2     2            2           85s
deploymentgrid-demo-zone-1   2/2     2            2           85s
deploymentgrid-demo-zone-2   2/2     2            2           85s
 
[root@VM_1_34_centos ~]# kubectl get svc
NAME                   TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
kubernetes             ClusterIP   172.19.0.1     <none>        443/TCP   87m
servicegrid-demo-svc   ClusterIP   172.19.0.177   <none>        80/TCP    80s
```

另外，对于部署了 DeploymentGrid 和 ServiceGrid 后才添加进集群的节点组，该功能会在新的节点组内自动创建指定的 Deployment 和 Service。

