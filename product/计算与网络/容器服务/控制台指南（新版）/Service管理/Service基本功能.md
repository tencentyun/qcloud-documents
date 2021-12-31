
## Service 控制台操作指引

### 创建 Service

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**集群**。
2. 在“集群管理”页面单击需要创建 Service 的集群 ID，进入待创建 Service 的集群管理页面。
4. 选择**服务与路由** > **Service**，进入 “Service” 管理页面。如下图所示：
![](https://main.qcloudimg.com/raw/c7ac45e1efc03a0cdbd937a35ade9037.png)
5. 单击**新建**，进入 “新建Service” 页面。
根据实际需求，设置 Service 参数。关键参数信息如下：
   - **服务名称**：自定义。
   - **命名空间**：根据实际需求进行选择。
   - **访问设置**：请参考 [概述](https://cloud.tencent.com/document/product/457/45487) 并根据实际需求进行设置。
>?
>- 如需使用已有负载均衡器，请参考 [使用已有 CLB](https://cloud.tencent.com/document/product/457/45491)。
>- 由于4层 CLB 仅限制 **CLB VIP + 监听器协议 + 后端 RS VIP + 后端 RS 端口4元组唯一**，且未包含 CLB 监控端口。因此不支持 CLB 监听端口不同，协议及 RS 相同的场景。容器服务也不支持同一个业务对外开放相同协议的不同端口。
>
7. 单击**创建服务**，完成创建。



### 更新 Service
#### 更新 YAML


1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**集群**。
2. 在“集群管理”页面中，选择需要更新 YAML 的集群 ID，进入待更新 YAML 的集群管理页面。
3. 选择**服务与路由** > **Service**，进入 Service 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/c7ac45e1efc03a0cdbd937a35ade9037.png)
5. 单击需更新 YAML 的 Service 所在行右侧的**编辑YAML**，进入更新 Service 页面。
6. 在 “更新Service” 页面，编辑 YAML 后单击**完成**，即可更新 YAML。

## Kubectl 操作 Service 指引

[](id:YAMLSample)
### YAML 示例
```Yaml
kind: Service
apiVersion: v1
metadata:
  ## annotations:
  ##   service.kubernetes.io/qcloud-loadbalancer-internal-subnetid: subnet-xxxxxxxx ##若是创建内网访问的 Service 需指定该条 annotation
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
  - protocol: TCP
    port: 80
    targetPort: 9376
  type: LoadBalancer
```

- **kind**：标识 Service 资源类型。
- **metadata**：Service 的名称、Label 等基本信息。
- **metadata.annotations**：Service 的额外说明，可通过该参数设置腾讯云容器服务的额外增强能力。
- **spec.type**：标识 Service 的被访问形式。
  - **ClusterIP**：在集群内部公开服务，可用于集群内部访问。
  - **NodePort**：使用节点的端口映射到后端 Service，集群外可以通过节点 `IP:NodePort` 访问。
  - **LoadBalancer**：使用腾讯云提供的负载均衡器公开服务，默认创建公网负载均衡，指定 annotations 可创建内网负载均衡。
  - **ExternalName**：将服务映射到 DNS，仅适用于 kube-dns1.7及更高版本。



### 创建 Service

1. 参考 [YAML 示例](#YAMLSample)，准备 Service YAML 文件。
2. 安装 Kubectl，并连接集群。操作详情请参考 [通过 Kubectl 连接集群](https://cloud.tencent.com/document/product/457/8438)。
3. 执行以下命令，创建 Service YAML 文件。
```shell
kubectl create -f Service YAML 文件名称
```
例如，创建一个文件名为 `my-service.yaml` 的 Service YAML 文件，则执行以下命令：
```shell
kubectl create -f my-service.yaml
```
4. 执行以下命令，验证创建是否成功。
```shell
kubectl get services
```
返回类似以下信息，即表示创建成功。
```
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   172.16.255.1   <none>        443/TCP   38d
```

### 更新 Service

#### 方法1
执行以下命令，更新 Service。
```
kubectl edit service/[name]
```

#### 方法2
1. 手动删除旧的 Service。
2. 执行以下命令，重新创建 Service。
```
kubectl create/apply
```

### 删除 Service
执行以下命令，删除 Service。
```
kubectl delete service [NAME]
```

<style>
	.params{margin-bottom:0px !important;}
</style>
