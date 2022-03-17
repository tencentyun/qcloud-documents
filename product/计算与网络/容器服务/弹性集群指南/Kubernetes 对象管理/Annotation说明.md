## 工作负载 pod template annotation 说明
您可以通过在 yaml 中定义 `spec.template.metadata.annotations` 的方式，实现为 Pod 绑定安全组、分配资源等能力。配置方法见下表：

<dx-alert infotype="notice" title="">
- 如果不指定安全组，则 Pod 会默认绑定同地域的 `default` 安全组。请确保 `default` 安全组的网络策略不影响该 Pod 正常工作。
- 如需通过 annotation 指定的方式分配 CPU 资源，则必须同时填写 `cpu` 和 `mem` 2个 annotation，且数值必须符合 [资源规格](https://cloud.tencent.com/document/product/457/39808) 中的 CPU 规格。另外，可以通过 `cpu-type` 指定分配 intel 或 amd CPU，其中 amd 具备更高的性价比，详情请参考 [产品定价](https://cloud.tencent.com/document/product/457/39806)。 
- 如需通过 annotation 指定的方式分配 GPU 资源，则必须同时填写`gpu-type` 及 `gpu-count` 2个 annotation，且数值必须符合 [资源规格](https://cloud.tencent.com/document/product/457/39808) 中的 GPU 规格。
</dx-alert>


<table>
<thead>
<tr>
<th width="20%">Annotation Key</th>
<th width="40%">Annotation Value 及描述</th>
<th width="40%">是否必填</th>
</tr>
</thead>
<tbody>
<tr>
<td>eks.tke.cloud.tencent.com/security-group-id</td>
<td>工作负载默认绑定的安全组，请填写 <a href="https://console.cloud.tencent.com/cvm/securitygroup" target="_blank">安全组 ID</a>：
	<ul class="params">
	<li>可填写多个，以<code>,</code>分割。例如 <code>sg-id1,sg-id2</code>。</li>
	<li>网络策略按安全组顺序生效。</li>
	<li>请注意单个安全组默认只能关联 2000 个计算实例，如云服务器 CVM 或 弹性容器 Pod，详细请参考 <a href="https://cloud.tencent.com/document/product/213/15379#.E5.AE.89.E5.85.A8.E7.BB.84.E7.9B.B8.E5.85.B3.E9.99.90.E5.88.B6" target="_blank">安全组限制</a>。</li>
	</ul>
</td>
<td> 否。如不填写，则默认关联工作负载绑定同地域的 <code>default</code> 安全组。<br>如填写，请确保同地域已存在该安全组 ID。</td></tr>
<tr>
<td>eks.tke.cloud.tencent.com/cpu</td>
<td>Pod 所需的 CPU 核数，请参考 <a href="https://cloud.tencent.com/document/product/457/39808" target="_blank">资源规格</a> 填写。默认单位为核，无需再次注明。</td>
<td>否。如填写，请确保为支持的规格，且需完整填写 <code>cpu</code> 和 <code>mem</code> 两个参数。</td>
</tr>
<tr>
<td>eks.tke.cloud.tencent.com/mem</td>
<td>Pod 所需的内存数量，请参考 <a href="https://cloud.tencent.com/document/product/457/39808" target="_blank">资源规格</a> 填写，需注明单位。例如，512Mi、0.5Gi、1Gi。</td>
<td>否。如填写，请确保为支持的规格，且需完整填写 <code>cpu</code> 和 <code>mem</code> 两个参数。</td>
</tr>
<tr>
<td>eks.tke.cloud.tencent.com/cpu-type</td>
<td>Pod 所需的 CPU 资源类型及机型，格式如下：
<ul  class="params">
<li>intel</li>
<li>amd</li>
<li>S5,S4</li>
<li>支持优先级顺序写法，如 “amd,intel” 表示优先创建 amd 资源 Pod，如果所选地域可用区 amd 资源不足，则会创建 intel 资源 Pod。</li>
</ul>
各型号支持的具体配置请参考 <a href="https://cloud.tencent.com/document/product/457/39808" target="_blank">资源规格</a>。</td>
<td>否。如果不填写则默认不强制指定 CPU 类型，会根据 <a href="https://cloud.tencent.com/document/product/457/44174" target="_blank">指定资源规格方法</a> 尽量匹配最合适的规格，若匹配到的规格 Intel 和 amd 均支持，则优先选择 Intel。</td>
</tr>
<tr>
<td>eks.tke.cloud.tencent.com/gpu-type</td>
<td>Pod 所需的 GPU 资源型号，目前支持型号如下：
<ul  class="params">
<li>V100</li>
<li>1/4*T4</li>
<li>1/2*T4</li>
<li>T4</li>
<li>支持优先级顺序写法，如 “T4,V100” 表示优先创建 T4 资源 Pod，如果所选地域可用区 T4 资源不足，则会创建 V100 资源 Pod。</li>
</ul>
各型号支持的具体配置请参考 <a href="https://cloud.tencent.com/document/product/457/39808">资源规格</a>。</td>
<td>如需 GPU，则此项为必填项。填写时，请确保为支持的 GPU 型号，否则会报错。</td>
</tr>
<tr>
<td>eks.tke.cloud.tencent.com/gpu-count</td>
<td>Pod 所需的 GPU 数量，请参考 <a href="https://cloud.tencent.com/document/product/457/39808" target="_blank">资源规格</a> 填写，默认单位为卡，无需再次注明。</td>
<td>否。如填写，请确保为支持的规格。</td>
</tr>
<tr>
<td>eks.tke.cloud.tencent.com/retain-ip</td>
<td>Pod 固定 IP，value 填写 <code>"true"</code> 开启此特性，开启特性的 Pod ，当 Pod 被销毁后，默认会保留这个 Pod 的 IP 24小时。24小时内 Pod 重建，仍可使用该 IP。24小时以后，该 IP 有可能被其他 Pod 抢占。<b>仅对 statefulset、rawpod 生效。</b></td>
<td>否</td>
</tr>
<tr>
<td>eks.tke.cloud.tencent.com/retain-ip-hours</td>
<td>修改 Pod 固定 IP 的默认时长，value 填写数值，单位是小时。默认是24小时，最大可支持保留一年。<b>仅对 statefulset、rawpod 生效。</td>
<td>否</td>
</tr>
<tr>
<td>eks.tke.cloud.tencent.com/role-name</td>
<td>为 Pod 关联 CAM 角色，value 填写 <a href="https://console.cloud.tencent.com/cam/role" target="_blank">CAM 角色名称</a>，Pod 可获取该 CAM 角色包含的权限策略，方便 Pod 内的程序进行如购买资源、读写存储等云资源操作。</td>
<td>否。如填写，请确保填写的 CAM 角色名存在。</td>
</tr>
<tr>
<td>eks.tke.cloud.tencent.com/custom-metrics-url</td>
<td>为 Pod 设置自定义监控指标拉取地址，通过该地址暴露的监控数据会自动被监控组件读取并上报。</td>
<td>否。如填写，请确保暴露的数据协议可被监控系统识别，如 Prometheus 协议、云监控数据协议。</td>
</tr>
<tr>
<td>eks.tke.cloud.tencent.com/eip-attributes</td>
<td>表明该 Workload 的 Pod 需要关联 EIP，值为 "" 时表明采用 EIP 默认配置创建。"" 内可填写 EIP 云 API 参数 json，实现自定义配置。例如 annotation 的值为 '{"InternetMaxBandwidthOut":2}' 即为使用2M的带宽。注意，非带宽上移的账号无法使用。</td>
<td>否 </td>
</tr>
<tr>
<td>eks.tke.cloud.tencent.com/eip-claim-delete-policy</td>
<td> Pod 删除后，EIP 是否自动回收，“Never” 不回收，默认回收。该参数只有在指定 eks.tke.cloud.tencent.com/eip-attributes 时才生效。注意，非带宽上移的账号无法使用。</td>
<td>否 </td>
</tr>
<tr>
<td>eks.tke.cloud.tencent.com/eip-id-list</td>
<td>如果工作负载为 StatefulSet，也可以使用指定已有 EIP 的方式，可指定多个，如 "eip-xx1,eip-xx2"。请注意，StatefulSet pod 的数量必须小于等于此 annotation 中指定 EIP Id 的数量，否则分配不到 EIP 的 Pod 会处于 Pending 状态。注意，非带宽上移的账号无法使用。</td>
<td>否 </td>
</tr>
<tr>
<td>eks.tke.cloud.tencent.com/registry-insecure-skip-verify</td>
<td>镜像仓库地址（多个用“,”隔开，或者填写 all）。在弹性集群使用自建 HTTPS 自签名镜像仓库的镜像创建工作负载时，可能会遇到 “ErrImagePull” 报错，拉取镜像失败，可添加该 Annotation 来解决。详情见 <a href="https://cloud.tencent.com/document/product/457/54755#.E5.BC.B9.E6.80.A7.E9.9B.86.E7.BE.A4.E5.A6.82.E4.BD.95.E4.BD.BF.E7.94.A8.E8.87.AA.E5.BB.BA.E7.9A.84.E8.87.AA.E7.AD.BE.E5.90.8D.E9.95.9C.E5.83.8F.E4.BB.93.E5.BA.93.E6.88.96-http-.E5.8D.8F.E8.AE.AE.E9.95.9C.E5.83.8F.E4.BB.93.E5.BA.93.EF.BC.9F">弹性集群如何使用自建的自签名镜像仓库或 HTTP 协议镜像仓库？</a></td>
<td>否 </td>
</tr>
<tr>
<td>eks.tke.cloud.tencent.com/registry-http-endpoint</td>
<td>镜像仓库地址（多个用“,”隔开，或者填写 all）。在弹性集群使用自建 HTTP 协议镜像仓库的镜像创建工作负载时，可能会遇到 “ErrImagePull” 报错，拉取镜像失败，可添加该 Annotation 来解决。详情见 <a href="https://cloud.tencent.com/document/product/457/54755#.E5.BC.B9.E6.80.A7.E9.9B.86.E7.BE.A4.E5.A6.82.E4.BD.95.E4.BD.BF.E7.94.A8.E8.87.AA.E5.BB.BA.E7.9A.84.E8.87.AA.E7.AD.BE.E5.90.8D.E9.95.9C.E5.83.8F.E4.BB.93.E5.BA.93.E6.88.96-http-.E5.8D.8F.E8.AE.AE.E9.95.9C.E5.83.8F.E4.BB.93.E5.BA.93.EF.BC.9F">弹性集群如何使用自建的自签名镜像仓库或 HTTP 协议镜像仓库？</a></td>
<td>否 </td>
</tr>
</tbody></table>

### 示例
以下为 Pod 绑定安全组的 GPU 规格完整示例：
```
apiVersion: apps/v1
kind: StatefulSet
metadata:
  generation: 1
  labels:
    k8s-app: nginx
    qcloud-app: nginx
  name: nginx
  namespace: default
spec:
  progressDeadlineSeconds: 600
  replicas: 1
  revisionHistoryLimit: 10
  selector:
    matchLabels:
      k8s-app: nginx
      qcloud-app: nginx
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
    type: RollingUpdate
  template:
    metadata:
      annotations:
        eks.tke.cloud.tencent.com/cpu: "4"
        eks.tke.cloud.tencent.com/gpu-count: "1"
        eks.tke.cloud.tencent.com/gpu-type: 1/4*T4
        eks.tke.cloud.tencent.com/mem: 10Gi
        eks.tke.cloud.tencent.com/security-group-id: "sg-dxxxxxx5,sg-zxxxxxxu"
        eks.tke.cloud.tencent.com/role-name: "cam-role-name"
        eks.tke.cloud.tencent.com/monitor-port: "9123"
        eks.tke.cloud.tencent.com/custom-metrics-url: "http://localhost:8080/metrics"
      creationTimestamp: null
      labels:
        k8s-app: nginx
        qcloud-app: nginx
    spec:
      containers:
      - image: nginx:latest
        imagePullPolicy: Always
        name: nginx
        resources:
          limits:
            cpu: "1"
            memory: 2Gi
            nvidia.com/gpu: "1"
          requests:
            cpu: "1"
            memory: 2Gi
            nvidia.com/gpu: "1"
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      dnsPolicy: ClusterFirst
      imagePullSecrets:
      - name: qcloudregistrykey
      restartPolicy: Always
      schedulerName: default-scheduler
      securityContext: {}
      terminationGracePeriodSeconds: 30
```



## 虚拟节点 annotation 说明
弹性容器服务 EKS 支持虚拟节点特性，您可通过在 yaml 中定义 annotation 的方式，实现自定义 DNS 等能力，具体如下：

<table>
<thead>
<tr>
<th width="20%">Annotation Key</th>
<th width="40%">Annotation Value 及描述</th>
<th width="40%">是否必填</th>
</tr>
</thead>
<tbody>
<tr>
<td>eks.tke.cloud.tencent.com/resolv-conf</td>
<td> 容器解析域名时查询 DNS 服务器的 IP 地址列表。例如 <code>nameserver 8.8.8.8</code>。
<br> 可通过 <code>kubectl edit node eklet-subnet-xxxx</code> 添加该 annotation。
<br> 修改后调度到该虚拟节点的 Pod 默认全部采用该 DNS 配置。</td>
<td>否。</td>
</tr>
</tr>
</tbody></table>

### 示例
以下为虚拟节点自定义 DNS 配置的示例：

```
apiVersion: v1
kind: Node
metadata:
  annotations:
    eks.tke.cloud.tencent.com/resolv-conf：|
	  nameserver 4.4.4.4
      nameserver 8.8.8.8
```



## 服务 annotation 说明

弹性容器服务支持使用已有负载均衡器创建公网/内网访问的 Service。如果您具备空闲的应用型负载均衡，需要提供给即将创建的 Service 使用，或需要在集群内使用相同的负载均衡时，您可以通过添加 annotations 的方法指定。

<table>
<thead>
<tr>
<th width="20%">Annotation Key</th>
<th width="40%">Annotation Value 及描述</th>
<th width="40%">是否必填</th>
</tr>
</thead>
<tbody>
<tr>
<td>service.kubernetes.io/tke-existed-lbid</td>
<td> Service 使用已有 <a href="https://cloud.tencent.com/document/product/214/524" target="_blank">负载均衡CLB</a> 创建，value 填写希望使用的 CLB 实例 ID。</td>
<td>否。如填写，请确保填写的 CLB 实例 ID 存在。</td>
</tr>
<tr>
<td>service.kubernetes.io/qcloud-share-existed-lb</td>
<td> 默认多个 Service 不可共用同一个 CLB 实例，如果希望 Service 复用其他 Service 占用的 CLB，请添加此 annotation 并将 value 填写为 <code>"true"</code>。</td>
<td>否。不填写默认不可复用。</td>
</tr>
</tr>
</tbody></table>

此外，弹性集群也支持和 TKE 普通集群一致的扩展协议，详情可参见 [Service 扩展协议](https://cloud.tencent.com/document/product/457/51259)。

>!
>- 请确保您的弹性容器服务业务不与云服务器业务共用一个负载均衡。
>- 使用已有负载均衡时：
>   - 只能使用通过负载均衡控制台创建的负载均衡器，不支持复用由容器服务自动创建的负载均衡器。
>   - 复用负载均衡的 Service 端口不能冲突。
>   - 不支持跨集群 Service 复用负载均衡。


### 示例
```
apiVersion: v1
kind: Service
metadata:
  annotations:
    service.kubernetes.io/tke-existed-lbid: lb-pxxxxxxq
    service.kubernetes.io/qcloud-share-existed-lb: true
  name: servicename
  namespace: default
spec:
  externalTrafficPolicy: Cluster
  ports:
  - name: tcp-80-80
    nodePort: 31728
    port: 80
    protocol: TCP
    targetPort: 80
  sessionAffinity: None
  type: LoadBalancer
```

<style>
	.params{margin:0px !important}
</style>
