## 简介

Service 定义访问后端 Pod 的访问策略，提供固定的虚拟访问 IP。您可以通过 Service 负载均衡地访问到后端的 Pod。
Service 支持以下类型：

- 公网访问： 使用 Service 的 Loadbalance 模式，自动创建公网 CLB。 公网 IP 可直接访问到后端的 Pod。
- VPC内网访问：使用 Service 的 Loadbalance 模式，自动创建内网 CLB。指定 `annotations:service.kubernetes.io/qcloud-loadbalancer-internal-subnetid: subnet-xxxxxxxx`，VPC 内网即可通过内网 IP 直接访问到后端的 Pod。
- 集群内访问：使用 Service 的 ClusterIP 模式，自动分配 Service 网段中的 IP，用于集群内访问。

## Service 控制台操作指引

### 注意事项

- 建议您的容器业务不要和 CVM 业务共用一个 CLB。
- 建议您不要在 CLB 控制台直接操作 TKE 自动管理的 CLB。
- 使用已有的 CLB 时:
  - 只能使用通过CLB控制台创建的负载均衡器，不支持复用由TKE自动创建的CLB。
  - 复用CLB的Service端口不能冲突
  - 不支持跨集群Service复用CLB
  - 复用CLB的Service不支持开启local访问。
  - 删除Service, 复用CLB绑定的后端云主机需要自行解绑，同时会保留一个tag tke-clusterId: cls-xxxx 需自行清理
- TKE 会自动覆盖和更新名称为 TKE_Dedicated_Listener 的监听器，其他监听器不覆盖。

### 创建 Service

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击【集群】，进入集群管理页面。
3. 单击需要创建 Service 的集群 ID，进入待创建 Service 的集群管理页面。
4. 选择 “服务” > “Service”，进入 Service 信息页面。如下图所示：
   
   ![Service](https://main.qcloudimg.com/raw/d42865b5fc802688b365cb2c8409e811.png)
5. 单击【新建】，进入 “新建Service” 页面。如下图所示：
   
   ![新建Service](https://main.qcloudimg.com/raw/beb261a208c44327e4d5381f29ac0724.png)
6. 根据实际需求，设置 Service 参数。关键参数信息如下：
   - 服务名称：自定义。
   - 命名空间：根据实际需求进行选择。
   - 服务访问方式：根据实际需求，选择对应的访问方式。
   - 端口映射：根据实际需求进行设置。
7. 单击【创建服务】，完成创建。

### 更新 Service

#### 更新 YAML

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击【集群】，进入集群管理页面。
3. 单击需要更新 YAML 的集群 ID，进入待更新 YAML 的集群管理页面。
4. 选择 “服务” > “Service”，进入 Service 信息页面。如下图所示：
   
   ![Service](https://main.qcloudimg.com/raw/d42865b5fc802688b365cb2c8409e811.png)
5. 在需要更新 YAML 的 Service 行中，单击【编辑YAML】，进入更新 Service 页面。
6. 在 “更新Service” 页面，编辑 YAML，单击【完成】，即可更新 YAML。

## Kubectl 操作 Service 指引

<span id="YAMLSample"></span>

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

- kind：标识 Service 资源类型。
- metadata：Service 的名称、Label等基本信息。
- metadata.annotations: Service 的额外说明，可通过该参数设置腾讯云 TKE 的额外增强能力。
- spec.type：标识 Service 的被访问形式
  - ClusterIP：在集群内部公开服务，可用于集群内部访问。
  - NodePort：使用节点的端口映射到后端 Service，集群外可以通过节点 IP:NodePort 访问。
  - LoadBalancer：使用腾讯云提供的负载均衡器公开服务，默认创建公网 CLB， 指定 annotations 可创建内网 CLB。
  - ExternalName：将服务映射到 DNS，仅适用于 kube-dns1.7及更高版本。

#### annotations: 使用已有负载均衡器创建公网/内网访问的 Service

如果您已有的传统型 CLB 为空闲状态，需要提供给 TKE 创建的 Service 使用，或期望在集群内使用相同的CLB，您可以通过以下 annotations 进行设置：

> 注意：
> 
> - 只能使用通过CLB控制台创建的负载均衡器，不支持复用由TKE自动创建的CLB。
> 
> - 复用CLB的Service端口不能冲突
> 
> - 不支持跨集群Service复用CLB
> 
> - 复用CLB的Service不支持开启local访问。
> 
> - 删除Service, 复用CLB绑定的后端云主机需要自行解绑，同时会保留一个tag tke-clusterId: cls-xxxx 需自行清理

```Yaml
metadata:
  annotations:
    service.kubernetes.io/tke-existed-lbid: lb-6swtxxxx
```

#### annotations: 指定节点绑定 Loadbalances

如果您的集群规模较大，入口类型的应用需设置亲和性调度到部分节点， 您可以通过配置 Service 的 Loadbalance，只绑定指定节点， annotations 如下：

```yaml
metadata:
  annotations:
    service.kubernetes.io/qcloud-loadbalancer-backends-label: `key in (value1, value2) ` ## LabelSelector格式
```

- 建议配合工作负载的亲和性调度使用。
- 前提条件是 Node 已根据业务需求设置 Label。
- 采用原生 LabelSelector 格式如：
  - service.kubernetes.io/qcloud-loadbalancer-backends-label: key1=values1, key2=values2
  - service.kubernetes.io/qcloud-loadbalancer-backends-label: key1 in (value1),key2 in (value2)
  - service.kubernetes.io/qcloud-loadbalancer-backends-label: key in (value1, value2)
  - service.kubernetes.io/qcloud-loadbalancer-backends-label: key1, key2 notin (value2)
- 增量的节点若匹配，将自动绑定到该 Loadbalance。
- 修改存量节点的 Label， 根据匹配规则将动态绑定和解绑 Loadbalance。

> ? 如果您使用的是带宽上移账号，在创建公网访问方式的服务时需要指定以下两个 annotations 项：
> 
> - `service.kubernetes.io/qcloud-loadbalancer-internet-charge-type` 公网带宽计费方式，可选值有：TRAFFIC_POSTPAID_BY_HOUR（按使用流量计费），BANDWIDTH_POSTPAID_BY_HOUR（按带宽计费）
> - `service.kubernetes.io/qcloud-loadbalancer-internet-max-bandwidth-out` 带宽上限，范围：[1,2000] Mbps。
>   
>   例如：
>   
>   ```Yaml
>   metadata:
>   annotations:
>     service.kubernetes.io/qcloud-loadbalancer-internet-charge-type: TRAFFIC_POSTPAID_BY_HOUR
>     service.kubernetes.io/qcloud-loadbalancer-internet-max-bandwidth-out: "10"
>   ```

### 创建 Service

1. 参考 [YAML 示例](#YAMLSample)，准备 StatefulSet YAML 文件。
2. 安装 Kubectl，并连接集群。操作详情请参考 [通过 Kubectl 连接集群](https://cloud.tencent.com/document/product/457/8438)。
3. 执行以下命令，创建 Service YAML 文件。
   
   ```shell
   kubectl create -f Service YAML 文件名称
   ```
   
   例如，创建一个文件名为 my-service.yaml 的 Service YAML 文件，则执行以下命令：
   
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

#### 方法一

执行以下命令，更新 Service。

```
kubectl edit service/[name]
```

#### 方法二

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
