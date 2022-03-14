## 简介[](id:Introduction)
Service 定义访问后端 Pod 的访问方式，并提供固定的虚拟访问 IP。您可以在 Service 中通过设置来访问后端的 Pod，不同访问方式的服务可提供不同网络能力。
腾讯云容器服务（TKE）提供以下四种服务访问方式：

<table>
<tr>
<th width="15%">访问方式</th>
<th>说明</th>
</tr>
<tr>
<td>提供公网访问</td>
<td>
<ul class="params">
<li>使用 Service 的 Loadbalance 模式，公网 IP 可直接访问到后端的 Pod，适用于 Web 前台类的服务。</li>
<li>创建完成后的服务在集群外可通过<b>负载均衡域名或 IP + 服务端口</b>访问服务，集群内可通过<b>服务名 + 服务端口</b>访问服务。</li>
</ul>
</td>
</tr>
<tr>
<td>仅在集群内访问</td>
<td>
<ul class="params">
<li>使用 Service 的 ClusterIP 模式，自动分配 Service 网段中的 IP，用于集群内访问。数据库类等服务如 MySQL 可以选择集群内访问，以保证服务网络隔离。</li>
<li>创建完成后的服务可以通过<b>服务名 + 服务端口</b>访问服务。</li>
</ul>
</td>
</tr>
<tr>
<td>VPC  内网访问</td>
<td>
<ul class="params">
<li>使用 Service 的 Loadbalance 模式，指定 <code>annotations:service.kubernetes.io/qcloud-loadbalancer-internal-subnetid: subnet-xxxxxxxx</code>，即可通过内网 IP 直接访问到后端的 Pod。</li>
<li>创建完成后的服务在集群外可通过<b>负载均衡域名或 IP + 服务端口</b>访问服务，集群内可通过<b>服务名 + 服务端口</b>访问服务。</li>
</ul>
</td>
</tr>
<tr>
<td>主机端口访问</td>
<td>
<ul class="params">
<li>提供一个主机端口映射到容器的访问方式，支持 TCP、UDP、Ingress。可用于业务定制上层 LB 转发到 Node。</li>
<li>创建完成后的服务可以通过<b>云服务器 IP+主机端口</b>或<b>服务名 + 服务端口</b>访问服务。</li>
</ul>
</td>
</tr>
</table>

>?集群内进行 Service 访问时，建议不要通过负载均衡 IP 进行访问，以避免出现访问不通的情况。

一般情况下，4层负载均衡（LB）会绑定多台 Node 作为 real server（rs） ，使用时需要限制 client 和 rs 不能存在于同一台云服务器上，否则会有一定概率导致报文回环出不去。
当 Pod 去访问 LB 时，Pod 就是源 IP，当其传输到内网时 LB 也不会做 snat 处理将源 IP 转化成 Node IP，那么 LB 收到报文也就不能判断是从哪个 Node 发送的，LB 的避免回环策略也就不会生效，所有的 rs 都可能被转发。当转发到 client 所在的 Node 上时，LB 就无法收到回包，从而导致访问不通。

## 注意事项[](id:annotations)
- 确保您的容器业务不和 CVM 业务共用一个 CLB。
- 不支持您在 CLB 控制台操作 TKE 管理的 CLB 的监听器和后端绑定的服务器，您的更改会被 TKE 自动覆盖。
- 使用已有的 CLB 时：
  - 只能使用通过 CLB 控制台创建的负载均衡器，不支持复用由 TKE 自动创建的 CLB。
  - 复用 CLB 的 Service 端口不能冲突
  - 不支持跨集群 Service 复用 CLB
  - 删除 Service，复用 CLB 绑定的后端云服务器需要自行解绑，同时会保留一个 tag tke-clusterId: cls-xxxx，需自行清理。


## Service 控制台操作指引



### 创建 Service

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击**集群**，进入集群管理页面。
3. 单击需要创建 Service 的集群 ID，进入待创建 Service 的集群管理页面。
4. 选择 “服务” > “Service”，进入 Service 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/3628305bd167fca1f3e2eaa2a4e1d615.png)
5. 单击**新建**，进入 “新建Service” 页面。如下图所示：
![](https://main.qcloudimg.com/raw/be05e7133d8c205a42dbb03a1b1de3a5.png)
6. 根据实际需求，设置 Service 参数。关键参数信息如下：
   - 服务名称：自定义。
   - 命名空间：根据实际需求进行选择。
   - 访问设置：请参考 [简介](#Introduction) 并根据实际需求进行设置。
7. 单击**创建服务**，完成创建。

### 更新 Service

#### 更新 YAML

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击**集群**，进入集群管理页面。
3. 单击需要更新 YAML 的集群 ID，进入待更新 YAML 的集群管理页面。
4. 选择 “服务” > “Service”，进入 Service 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/77224c6dc76ded174f4188c6e184cc90.png)
5. 在需要更新 YAML 的 Service 行中，单击**编辑YAML**，进入更新 Service 页面。
6. 在 “更新Service” 页面，编辑 YAML，单击**完成**，即可更新 YAML。

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

- kind：标识 Service 资源类型。
- metadata：Service 的名称、Label等基本信息。
- metadata.annotations: Service 的额外说明，可通过该参数设置腾讯云 TKE 的额外增强能力。
- spec.type：标识 Service 的被访问形式
  - ClusterIP：在集群内部公开服务，可用于集群内部访问。
  - NodePort：使用节点的端口映射到后端 Service，集群外可以通过节点 IP:NodePort 访问。
  - LoadBalancer：使用腾讯云提供的负载均衡器公开服务，默认创建公网 CLB， 指定 annotations 可创建内网 CLB。
  - ExternalName：将服务映射到 DNS，仅适用于 kube-dns1.7及更高版本。

#### annotations: 使用已有负载均衡器创建公网/内网访问的 Service

如果您已有的应用型 CLB 为空闲状态，需要提供给 TKE 创建的 Service 使用，或期望在集群内使用相同的CLB，您可以通过以下 annotations 进行设置：
>?请了解 [注意事项](#annotations) 后开始使用。
>
```Yaml
metadata:
  annotations:
    service.kubernetes.io/tke-existed-lbid: lb-6swtxxxx
```

#### annotations: 指定节点绑定 Loadbalancer

如果您的集群规模较大，入口类型的应用需设置亲和性调度到部分节点， 您可以通过配置 Service 的 Loadbalancer，只绑定指定节点， annotations 如下：

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
- 修改存量节点的 Label， 根据匹配规则将动态绑定和解绑 Loadbalancer。

#### 说明事项
如果您使用的是 **IP 带宽包** 账号，在创建公网访问方式的服务时需要指定以下两个 annotations 项：
- `service.kubernetes.io/qcloud-loadbalancer-internet-charge-type` 公网带宽计费方式，可选值有：   
 -  TRAFFIC_POSTPAID_BY_HOUR（按使用流量计费）
 -  BANDWIDTH_POSTPAID_BY_HOUR（按带宽计费）
- `service.kubernetes.io/qcloud-loadbalancer-internet-max-bandwidth-out` 带宽上限，范围：[1,2000] Mbps。
   例如：
```Yaml
  metadata:
  annotations:
  service.kubernetes.io/qcloud-loadbalancer-internet-charge-type: TRAFFIC_POSTPAID_BY_HOUR
  service.kubernetes.io/qcloud-loadbalancer-internet-max-bandwidth-out: "10"
```
关于 **IP 带宽包** 的更多详细信息，欢迎查看文档 [共享带宽包产品类别](https://cloud.tencent.com/document/product/684/15246)。

### 创建 Service

1. 参考 [YAML 示例](#YAMLSample)，准备 Service YAML 文件。
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

<style>
	.params{margin-bottom:0px !important;}
</style>
