## 工作负载 template annotation 说明
您可以通过在 yaml 中定义 `template annotation` 的方式，实现为 Pod 绑定安全组、分配资源等能力。配置方法见下表：

>!
>- 如果不指定安全组，则 Pod 会默认绑定同地域的 `default` 安全组。请确保 `default` 安全组的网络策略不影响该 Pod 正常工作。
>- 如需分配 GPU 资源，则必须填写 `eks.tke.cloud.tencent.com/gpu-type`。
>- 下表中除 `eks.tke.cloud.tencent.com/gpu-type` 外，其余4个资源分配相关的 annotation 均为非必填，如填写则请确保正确性。
> - 如需分配 CPU 资源，则必须同时填写 `cpu` 和 `mem` 2个 annotation，且数值必须符合 [资源规格](https://cloud.tencent.com/document/product/457/39808) 中的 CPU 规格。另外，可以通过 `cpu-type` 指定分配 intel 或 amd CPU，其中 amd 具备更高的性价比，详情请参考 [产品定价](https://cloud.tencent.com/document/product/457/39806)。 
> - 如需分配 GPU 资源，则必须同时填写 `cpu`、`mem`、`gpu-type` 及 `gpu-count` 4个 annotation，且数值必须符合 [资源规格](https://cloud.tencent.com/document/product/457/39808) 中的 GPU 规格。


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
<td>Pod 所需的 CPU 资源型号，目前支持型号如下：
<ul  class="params">
<li>intel</li>
<li>amd</li>
</ul>
各型号支持的具体配置请参考 <a href="https://console.cloud.tencent.com/cvm/securitygroup" target="_blank">资源规格</a>。</td>
<td>否。如果不填写则默认不强制指定 CPU 类型，会根据 <a href="https://cloud.tencent.com/document/product/457/44174" target="_blank">指定资源规格方法</a> 尽量匹配最合适的规格，若匹配到的规格 Intel 和 amd 均支持，则优先选择 Intel。</td>
</tr>
<tr>
<td>eks.tke.cloud.tencent.com/gpu-type</td>
<td>Pod 所需的 GPU 资源型号，目前支持型号如下：
<ul  class="params">
<li>1/4*V100</li>
<li>1/2*V100</li>
<li>V100</li>
<li>1/4*T4</li>
<li>1/2*T4</li>
<li>T4</li>
</ul>
各型号支持的具体配置请参考 <a href="https://console.cloud.tencent.com/cvm/securitygroup" target="_blank">资源规格</a>。</td>
<td>如需 GPU，则此项为必填项。填写时，请确保为支持的 GPU 型号，否则会报错。</td>
</tr>
<tr>
<td>eks.tke.cloud.tencent.com/gpu-count</td>
<td>Pod 所需的 GPU 数量，请参考 <a href="https://cloud.tencent.com/document/product/457/39808" target="_blank">资源规格</a> 填写，默认单位为卡，无需再次注明。</td>
<td>否。如填写，请确保为支持的规格。</td>
</tr>
<tr>
<td>eks.tke.cloud.tencent.com/static-ip</td>
<td>Pod 固定 IP，value 填写 <code>"true"</code> 开启此特性，开启特性的 StatefulSet 和 Bare Pod 在 Pod 发生更新/重启后 IP 不会变化。</td>
<td>否。但仅对 StatefulSet、Pod 类型工作负载生效。</td>
</tr>
<tr>
<td>eks.tke.cloud.tencent.com/role-name</td>
<td>为 Pod 关联 CAM 角色，value 填写 <a href="https://console.cloud.tencent.com/cam/role" target="_blank">CAM 角色名称</a>，Pod 可获取该 CAM 角色包含的权限策略，方便 Pod 内的程序进行如购买资源、读写存储等云资源操作。</td>
<td>否。如填写，请确保填写的 CAM 角色名存在。</td>
</tr>
<tr>
<td>eks.tke.cloud.tencent.com/monitor_port</td>
<td>为 Pod 设置监控数据暴露端口，以便被 Prometheus 等组件采集。</td>
<td>否。不填写默认为 9100。</td>
</tr>
<tr>
<td>eks.tke.cloud.tencent.com/custom_metrics_url</td>
<td>为 Pod 设置自定义监控指标拉取地址，通过该地址暴露的监控数据会自动被监控组件读取并上报。</td>
<td>否。如填写，请确保暴露的数据协议可被监控系统识别，如 Prometheus 协议、云监控数据协议。</td>
</tr>
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
        eks.tke.cloud.tencent.com/cpu: "2"
        eks.tke.cloud.tencent.com/gpu-count: "1"
        eks.tke.cloud.tencent.com/gpu-type: 1/4*V100
        eks.tke.cloud.tencent.com/mem: 10Gi
        eks.tke.cloud.tencent.com/security-group-id: "sg-dxxxxxx5,sg-zxxxxxxu"
        eks.tke.cloud.tencent.com/static-ip: "true"
        eks.tke.cloud.tencent.com/role-name: "cam-role-name"
        eks.tke.cloud.tencent.com/monitor_port: "9123"
        eks.tke.cloud.tencent.com/custom_metrics_url: "http://localhost:8080/metrics"
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


## 服务 annotation 说明

弹性容器服务支持使用已有负载均衡器创建公网/内网访问的 Service。如果您具备空闲的应用型负载均衡，需要提供给即将创建的 Service 使用，或需要在集群内使用相同的负载均衡时，您可以通过添加 annotations 的方法指定。

>!
>- 请确保您的弹性容器服务业务不与云服务器业务共用一个负载均衡。
> - 使用已有负载均衡时：
>  - 只能使用通过负载均衡控制台创建的负载均衡器，不支持复用由容器服务自动创建的负载均衡器。
>  - 复用负载均衡的 Service 端口不能冲突。
>  - 不支持跨集群 Service 复用负载均衡。


### 示例
```
apiVersion: v1
kind: Service
metadata:
  annotations:
    service.kubernetes.io/tke-existed-lbid: lb-pxxxxxxq
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
