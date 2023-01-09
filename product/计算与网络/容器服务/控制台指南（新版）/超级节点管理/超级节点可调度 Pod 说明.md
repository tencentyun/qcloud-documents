

## 计费方式

调度到超级节点上的 Pod 支持预付费、后付费（按量计费、竞价）的两种计费模式。

## 支持超级节点的 Kubernetes 版本

- 按量计费超级节点支持 1.16 及以上版本集群。
- 包年包月超级节点当前仅支持 1.22 最高版本集群。

## 超级节点上可调度的 Pod 规格

超级节点支持的 Pod 的规格配置是容器运行时可用资源和使用服务计费的依据，请务必了解超级节点 Pod 的资源规格配置。不同计费模式的超级节点支持的可调度 Pod 规格不同。

### 包年包月模式

- 支持调度 1C～8C 标准规格的 Pod。
- 支持调度 CPU 值大于1/4内存值的 Pod。

节点支持规格列表：
>! 若为非标准规格，则自动向上转换成标准规格。
>

| CPU/核 | 内存区间/GiB | 内存区间粒度/GiB |
| ------ | ------------ | ---------------- |
| 1      | 1 - 4        | 1                |
| 2      | 2 - 8        | 1                |
| 4      | 8 - 16       | 1                |
| 8      | 16 - 32      | 1                |



### 按量计费模式

- 支持调度0.25C～16C标准规格的 Pod（若为非标准规格，则自动向上转换成标准规格）。
- 支持调度 CPU 值大于1/8内存值的 Pod。

节点支持规格列表：
>! 若为非标准规格，则自动向上转换成标准规格。
>

| CPU/核 | 内存区间/GiB | 内存区间粒度/GiB |
| :----- | :----------- | :--------------- |
| 0.25   | 0.5、1、2    | -                |
| 0.5    | 1、2、3、4   | -                |
| 1      | 1 - 8        | 1                |
| 2      | 4 - 16       | 1                |
| 4      | 8 - 32       | 1                |
| 8      | 16 - 32      | 1                |
| 12     | 24 - 48      | 1                |
| 16     | 32 - 64      | 1                |

 

## 超级节点配置说明

### Pod 临时存储

每个调度到超级节点上的 Pod，创建时会分配20GiB的临时镜像存储。

>!
>- 临时镜像存储将于 Pod 生命周期结束时删除，请勿用于存储重要数据。
>- 由于需存储镜像，实际可用空间小于20GiB。
>- 若需要扩容系统盘资源，可通过 Annotation 实现。
>- 重要数据、超大文件等推荐挂载 Volume 持久化存储。

### Pod 网络

调度到超级节点上的 Pod 采用的是与云服务器、云数据库等云产品平级的 VPC 网络，每个 Pod 都会占用一个 VPC 子网 IP。
Pod 与 Pod、Pod 与其他同 VPC 云产品间可直接通过 VPC 网络通信，没有性能损耗。

### Pod 隔离性

调度到超级节点上的 Pod 拥有与云服务器完全一致的安全隔离性。Pod 在腾讯云底层物理服务器上调度创建，创建时会通过虚拟化技术保证 Pod 间的资源隔离。

### 其他 Pod 特殊配置

调度到超级节点上的 Pod 可以通过在 yaml 中定义 `template annotation` 的方式，实现为 Pod 绑定安全组、分配资源、分配 EIP 等能力。配置方法见下表：



>!
>- 如果不指定安全组，则 Pod 会默认绑定节点池指定的安全组。请确保安全组的网络策略不影响该 Pod 正常工作，例如，Pod 启用 80 端口提供服务，请放通入方向80端口的访问。
>- 如需分配 CPU 资源，则必须同时填写 `cpu` 和 `mem` 2个 annotation，且数值必须符合 [资源规格](https://cloud.tencent.com/document/product/457/39808) 中的 CPU 规格。
>- 如需通过 annotation 指定的方式分配 GPU 资源，则必须同时填写`gpu-type` 及 `gpu-count` 2个 annotation，且数值必须符合 [资源规格](https://cloud.tencent.com/document/product/457/39808) 中的 GPU 规格。

| Annotation Key                                    | Annotation Value 及描述                                      | 是否必填                                                     |
| :------------------------------------------------ | :----------------------------------------------------------- | :----------------------------------------------------------- |
| eks.tke.cloud.tencent.com/security-group-id       | 工作负载默认绑定的安全组，请填写 [安全组 ID](https://console.cloud.tencent.com/cvm/securitygroup)：可填写多个，以`,`分割。例如 `sg-id1,sg-id2`。网络策略按安全组顺序生效。 | 否。如不填写，则默认绑定节点池指定的安全组。 如填写，请确保同地域已存在该安全组 ID。 |
| eks.tke.cloud.tencent.com/cpu                     | Pod 所需的 CPU 核数，请参考 [资源规格](https://cloud.tencent.com/document/product/457/39808) 填写。默认单位为核，无需再次注明。 | 否。如填写，请确保为支持的规格，且需完整填写 `cpu` 和 `mem` 两个参数。 |
| eks.tke.cloud.tencent.com/mem                     | Pod 所需的内存数量，请参考 [资源规格](https://cloud.tencent.com/document/product/457/39808) 填写，需注明单位。例如，512Mi、0.5Gi、1Gi。 | 否。如填写，请确保为支持的规格，且需完整填写 `cpu` 和 `mem` 两个参数。 |
| eks.tke.cloud.tencent.com/cpu-type                | Pod 所需的 CPU 资源型号，目前支持型号如下：intelamd 具体型号，如 S4、S3 各型号支持的具体配置请参考 [资源规格](https://cloud.tencent.com/document/product/457/39808)。 | 否。如果不填写则默认不强制指定 CPU 类型，会根据 [指定资源规格方法](https://cloud.tencent.com/document/product/457/44174) 尽量匹配最合适的规格，若匹配到的规格 Intel 和 amd 均支持，则优先选择 Intel。 |
| eks.tke.cloud.tencent.com/gpu-type                | Pod 所需的 GPU 资源型号，目前支持型号如下：V1001/4*T41/2*T4T4 支持优先级顺序写法，如 “T4,V100” 表示优先创建 T4 资源 Pod，如果所选地域可用区 T4 资源不足，则会创建 V100 资源 Pod。各型号支持的具体配置请参考 [资源规格](https://cloud.tencent.com/document/product/457/39808)。 | 如需 GPU，则此项为必填项。填写时，请确保为支持的 GPU 型号，否则会报错。 |
| eks.tke.cloud.tencent.com/gpu-count               | Pod 所需的 GPU 数量，请参考 [资源规格](https://cloud.tencent.com/document/product/457/39808) 填写，默认单位为卡，无需再次注明。 | 否。如填写，请确保为支持的规格。                             |
| eks.tke.cloud.tencent.com/retain-ip               | Pod 固定 IP，value 填写 `"true"` 开启此特性，开启特性的 Pod ，当 Pod 被销毁后，默认会保留这个 Pod 的 IP 24 小时。24 小时内 Pod 重建，还能使用该 IP。24 小时以后，该 IP 有可能被其他 Pod 抢占。**仅对 statefulset、rawpod 生效。** | 否                                                           |
| eks.tke.cloud.tencent.com/retain-ip-hours         | 修改 Pod 固定 IP 的默认时长，value 填写数值，单位是小时。默认是 24 小时，最大可支持保留一年。**仅对 statefulset、rawpod 生效。** | 否                                                           |
| eks.tke.cloud.tencent.com/eip-attributes          | 表明该 Workload 的 Pod 需要关联 EIP，值为 "" 时表明采用 EIP 默认配置创建。"" 内可填写 EIP 云 API 参数 json，实现自定义配置。例如 annotation 的值为 '{"InternetMaxBandwidthOut":2}' 即为使用 2M 的带宽。注意，非带宽上移的账号无法使用。 | 否                                                           |
| eks.tke.cloud.tencent.com/eip-claim-delete-policy | Pod 删除后，EIP 是否自动回收，“Never” 不回收，默认回收。该参数只有在指定 eks.tke.cloud.tencent.com/eip-attributes 时才生效。注意，非带宽上移的账号无法使用。 | 否                                                           |
| eks.tke.cloud.tencent.com/eip-id-list             | 如果工作负载为 StatefulSet，也可以使用指定已有 EIP 的方式，可指定多个，如"eip-xx1,eip-xx2"。请注意，StatefulSet pod 的数量必须小于等于此 annotation 中指定 EIP Id 的数量，否则分配不到 EIP 的 pod 会处于 Pending 状态。注意，非带宽上移的账号无法使用。 | 否                                                           |

示例请参考 [Annotation 说明](https://cloud.tencent.com/document/product/457/44173)。

## 默认配额

购买包年包月的超级节点时，将按照总规格分配默认配额，开通按量计费的超级节点，默认每个集群可将500个 Pod 调度到超级节点上。若您需要超过以上配额的资源，可填写提升配额申请，由腾讯云对您的实际需求进行评估，评估通过之后将为您提升配额。

### 申请提升配额操作指引

1. 请 [提交工单](https://console.cloud.tencent.com/workorder/category) ，选择**人工支持**或者**其他问题** > **立即创建**，进入创建工单信息填写页面。
2. 在问题描述中填写“期望提升集群超级节点 Pod 配额”，注明目标地区及目标配额，并按照页面提示填写您可用的手机号等信息。
3. 填写完成后，单击**在线咨询**即可。

## Pod 限制说明

### Workload 限制

DaemonSet 类型工作负载的 Pod 不会调度到超级节点上。

### Service 限制

采用 [GlobalRouter 网络模式](https://cloud.tencent.com/document/product/457/50354) 的集群 service 如果开启了 externaltrafficpolicy = local，流量不会转发到调度到超级节点上的 Pod。

### Volume 限制

支持 EmptyDir / PVC / Secret / NFS / ConfigMap / Downward API / HostPath 类型的 Volume。
其中针对 PVC 类型的 Volume：
- PV 类型：仅支持 NFS / CephFS / HostPath / 静态 cbs 类型，其他的不支持（csi 不支持）
- Storageclass 类型：仅支持用户自定义 /`cloud.tencent.com/qcloud-cbs` 类型，cfs 不支持

### GPU 限制

必须在 Annotation 中指定 gpu-type 字段，否则不支持调度到超级节点上；不同 type 的 GPU Pod 对应的 cpu、mem 规格是固定的，可不指定 cpu、mem 大小，若需要指定大小，则必须与 GPU Pod 支持的规格完全一致，否则将调度失败。

### 其他限制

- 没有任何服务器节点的空集群暂时无法正常使用超级节点功能。
- 开启了 [固定 IP ](https://cloud.tencent.com/document/product/457/34994) 的 Pod 暂不支持调度到超级节点上。
- 指定了 hostIP 配置的 Pod 默认会把 Pod IP 作为 hostIP。
- 调度到超级节点上的 Pod 是强隔离的，如果开启了硬反亲和性特性，调度到超级节点上不会生效，会存在调度多个同一工作负载的 Pod 在同一个超级节点上的情况。
- tke-eni-ip-webhook 命名空间下的 Pod 不支持调度到超级节点。
- TKE kube-system 下的 Pod 支持调度到包年包月的超级节点，默认不支持调度到按量计费的超级节点。
