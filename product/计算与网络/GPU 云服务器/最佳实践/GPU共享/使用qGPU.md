## 操作场景
本文介绍如何通过腾讯云容器服务 TKE 使用 qGPU。


## 使用须知
- TKE 版本限制：需 ≥ v1.14.x。
- 操作系统限制：仅支持特定的 TencentOS 3.1 镜像。
- 机型限制：目前仅支持使用 V100 和 T4 卡的 CVM 机型。
- 目前支持的 NVIDIA Tesla 驱动版本最新至450.102.04，CUDA 版本11.3。为保证兼容性，强烈建议用户使用 node 上自带的 UMD，无需在 POD 内部重复安装 UMD。
- qGPU 粒度：一个 GPU 上最多分配的 qGPU 个数（Pod 个数）= GPU 显存数 / 4。
 例如，32G 显存，最多可以分配8个 qGPU，每个 qGPU 最小分配 1G 显存。
- 开启了 qGPU 能力的节点无法作为常规的 GPU 节点使用，即不能使用整卡的资源。建议通过 TKE 的节点池能力来区分规划资源。
- 如需升级 Kubernetes Master 版本，请注意：
  - 对于托管集群，无需重新设置本插件。
  - 对于独立集群，master 版本升级会重置 master 上所有组件的配置，会影响 qgpu-scheduler 插件作为 Scheduler Extender 的配置，因此 qGPU 插件需要卸载后再重新安装。


## 操作步骤

<dx-alert infotype="explain" title="">
由于使用 qGPU 能力需要使用特定镜像以及设置相关 Label，强烈建议您使用 TKE 的节点池能力来对节点进行分组管理（节点池的节点具备统一的 Label 以及镜像属性），详情请参见 [创建节点池](https://cloud.tencent.com/document/product/457/43735)。
</dx-alert>



### 安装 QGPU 组件
1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)，在左侧导航栏中选择**集群**。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**组件管理**，进入“组件列表”页面。
4. 在“组件列表”页面中选择**新建**，并在“新建组件”页面中勾选 QGPU（GPU 隔离组件）。
5. 单击**参数配置**，可以设置 qgpu-scheduler 的调度策略。
   - **spread**：多个 Pod 会分散在不同节点、不同显卡上，优先选择资源剩余量较多的节点。适用于高可用场景，避免把同一个应用的副本放到同一个设备上。
   - **binpack**：多个 Pod 会优先使用同一个节点，适用于提高 GPU 利用率的场景。
6. 单击**完成**即可创建组件。
安装成功后，需要为集群准备 GPU 资源。

### 准备 GPU 资源
1. 在集群管理页面中，选择左侧工具栏中的**节点管理** > **节点池**。
2. 在“节点池列表”页面中，单击**新建节点池**。
3. 在创建节点池页面中，“镜像提供方”请选择**市场镜像**，“操作系统”请选择 **TencentOS Server 3.1(TK4)**，其余参数配置可参见 [创建节点池](https://cloud.tencent.com/document/product/457/43735)。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/65d9285b9b4d8cc3e93987932ccdae67.png)
<dx-alert infotype="explain" title="">
使用 qGPU 指定的镜像创建节点后，TKE 后台会自动给节点添加 `label qgpu-device-enable:"enable"`，设置了该 label 后，DaemonSet qgpu-manager 会调度到对应节点上，并自动进行 qGPU 相关的设置。
</dx-alert>
4. 在创建节点池页面中展开**更多设置**，通过高级配置设置 Label，指定 qGPU 隔离策略 。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/1adefcd6698d483726ef2dd218f21ec8.png)
 - Label 键：`tke.cloud.tencent.com/qgpu-schedule-policy`。
 - Label 值：`fixed-share`。设置 Label value 时，可填写全称或者缩写，更多取值请参考下表。
 当前 qGPU 支持以下三种隔离策略：
<table>
<thead>
<tr>
<th>Label 值</th>
<th>缩写</th>
<th>英文名</th>
<th>中文名</th>
<th>含义</th>
</tr>
</thead>
<tbody><tr>
<td nowrap="nowrap">best-effort（默认值）</td>
<td>be</td>
<td>Best Effort</td>
<td>争抢模式</td>
<td>默认值。各个 Pods 不限制算力，只要卡上有剩余算力就可使用。 如果一共启动 N 个 Pods，每个 Pod 负载都很重，则最终结果就是 1/N 的算力。</td>
</tr>
<tr>
<td>fixed-share</td>
<td>fs</td>
<td>Fixed Share</td>
<td>固定配额</td>
<td>每个 Pod 有固定的算力配额，无法超过固定配额，即使 GPU 还有空闲算力。</td>
</tr>
<tr>
<td>burst-share</td>
<td>bs</td>
<td>Guaranteed Share with Burst</td>
<td>保证配额加弹性能力</td>
<td>调度器保证每个 Pod 有保底的算力配额，但只要 GPU 还有空闲算力，就可被 Pod 使用。例如，当 GPU 有空闲算力时（没有分配给其他 Pod），Pod 可以使用超过它的配额的算力。注意，当它所占用的这部分空闲算力再次被分配出去时，Pod 会回退到它的算力配额。</td>
</tr>
</tbody></table>
5. 单击**创建节点池**即可。
6. 为应用分配 GPU 资源。
通过给容器设置 qGPU 对应资源允许 Pod 使用 qGPU，您可以通过控制台或者 YAML 方式来设置：
<dx-tabs>
::: 通过控制台设置
在“新建Workload” 页面，填写 “GPU 资源”。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/d3ffe9065299c3e6b5c6be8536aa23d5.png)

:::
::: 通过 YAML 设置
通过 YAML 来设置相关 qGPU 资源：
```yaml
spec:
  containers:
    resources:
      limits:
        tke.cloud.tencent.com/qgpu-memory: "5"
        tke.cloud.tencent.com/qgpu-core: "30"
      requests:
        tke.cloud.tencent.com/qgpu-memory: "5"
        tke.cloud.tencent.com/qgpu-core: "30"
```
- requests 和 limits 中和 qGPU 相关的资源值必须一致（根据 K8S 的规则，可以省略 requests 中对 qGPU 的设置，这种情况下 requests 会被自动设置为和 limits 相同的值）。
- `tke.cloud.tencent.com/qgpu-memory` 表示容器申请的显存（单位G），**整数分配，不支持小数**。
- `tke.cloud.tencent.com/qgpu-core` 代表容器申请的算力，每个 GPU 卡可以提供100%算力，**qgpu-core 的设置应该小于100**，设置值超过剩余算力比例值，则设置失败，设置后容器可以得到一张 GPU 卡 n% 的算力。
:::
</dx-tabs>



## 附录

### 部署在集群内的 Kubernetes 对象

| Kubernetes 对象名称 | 类型 | 请求资源 |Namespace |
|---------|---------|---------|---------|
|qgpu-manager|	DaemonSet|	每 GPU 节点一个 Memory: 300M, CPU:0.2|	kube-system|
|qgpu-manager|	ClusterRole	|-|	-|
|qgpu-manager|	ServiceAccount|-|		kube-system|
|qgpu-manager|	ClusterRoleBinding|-|		kube-system|
|qgpu-scheduler|	Deployment	| 单一副本 Memory: 800M, CPU:1	|kube-system|
|qgpu-scheduler|	ClusterRole|-|		-|
|qgpu-scheduler|	ClusterRoleBinding	|-|	kube-system|
|qgpu-scheduler|	ServiceAccount	|-|	kube-system|
|qgpu-scheduler|	Service|-|		kube-system|

