## 使用须知

- **版本支持：**TKE 版本 ≥ v1.14.x
- **OS 支持：**仅支持特定的 Tencent OS 3.1 镜像。
- **GPU 卡架构：**支持 Volta（如 **V100**）、Turing（如 **T4**）、Ampere（如 **A100、A10**)。
- **驱动版本：**默认预装 NVIDIA 驱动 450.102.04 / 470.82.01；支持 CUDA 11.4 及以下。为保证兼容性，强烈建议用户使用节点预安装 NVIDIA 驱动，无需在 POD 内部重复安装。
- **共享粒度：**每个 qGPU 最小分配 1G 显存，精度单位是 1G。算力最小分配 5（代表一张卡的 5%），最大 100（代表一张卡），精度单位是 5（即 5、10、15、20 ... 100）。
- **整卡分配：**开启了 qGPU 能力的节点可按照 `tke.cloud.tencent.com/qgpu-core: 100 | 200 | ...`（N * 100，N 是整卡个数）的方式分配整卡。建议通过 TKE 的节点池能力来区分 nvidia 分配方式或转换到 qGPU 使用方式。
- **个数限制：**一个 GPU 上最多可创建 16 个 qGPU 设备。建议按照容器申请的显存大小确定单个 GPU 卡可共享部署的 qGPU 个数。
- **升级需知：**如需升级 Kubernetes Master 版本，请注意：
  - 对于托管集群，无需重新设置本插件。
  - 对于独立集群，master 版本升级会重置 master 上所有组件的配置，从而影响到 qgpu-scheduler 插件作为 Scheduler Extender 的配置，因此 qGPU 插件需要卸载后再重新安装。

## 操作步骤

>? 由于使用 qGPU 能力需要使用特定镜像以及设置相关 Label，因此强烈建议您使用 TKE 的 [节点池](https://cloud.tencent.com/document/product/457/43719) 能力来对节点进行分组管理（节点池的节点具备统一的 Label 以及镜像属性），详情请参见 [新建节点池](https://cloud.tencent.com/document/product/457/43735)。

### 安装 qGPU 
1. 登录 [容器服务控制台 ](https://console.qcloud.com/tke2)，在左侧导航栏中选择**集群**。
2. 在“集群管理”页面选择地域，单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**组件管理**，在组件管理页面中单击**新建**。
4. 在“新建组件”页面中勾选 QGPU（GPU隔离组件）。
5. 单击**参数配置**，设置 qgpu-scheduler 的调度策略。
   - **spread**：多个 Pod 会分散在不同节点、不同显卡上，优先选择资源剩余量较多的节点，适用于高可用场景，避免把同一个应用的副本放到同一个设备上。
   - **binpack**：多个 Pod 会优先使用同一个节点，适用于提高 GPU 利用率的场景。
6. 单击**完成**即可创建组件。安装成功后，需要为集群准备 GPU 资源。


### 准备 GPU 资源
1. 单击**新建节点池**，选中**qGPU 专用市场镜像**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/f7e20abd820ef098d8ebf2d4e79b160f.png)
>? 通过 qGPU 指定的镜像创建节点，TKE 后台会自动给节点添加 `label qgpu-device-enable:"enable"`。设置了该 Label 后，DaemonSet qgpu-manager 会调度到对应节点上，并自动进行 qGPU 相关的设置。
>
2. 在**更多设置 > Labels**中，通过节点池的高级配置来设置 Label，指定 qGPU 隔离策略：
      - Label 键：`tke.cloud.tencent.com/qgpu-schedule-policy`
      - Label 值：`fixed-share`（Label value 可填写全称或者缩写，更多取值可参考下方 [隔离策略说明](#table)）
![](https://qcloudimg.tencent-cloud.cn/raw/ffb8cf8b972e8a7a792e6c1f8c538eb9.png)
    当前 qGPU 支持以下隔离策略：[](id:table)
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
<td>默认值。各个 Pods 不限制算力，只要卡上有剩余算力就可使用。  如果一共启动 N 个 Pods，每个 Pod 负载都很重，则最终结果就是 1/N 的算力。</td>
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
3. 单击**创建节点池**即可。


### 分配 GPU 资源
通过给容器设置 qGPU 对应资源可以允许 Pod 使用 qGPU，您可以通过控制台或者 YAML 方式为应用分配 GPU 资源。
>?
> - 如果应用需要使用整数卡资源，只需填写卡数，无需填写显存（自动使用分配的 GPU 卡上全部显存）。
> - 如果应用需要使用小数卡资源（即和其他应用共享同一张卡），需要同时填写卡数和显存。
>
<dx-tabs>
::: 通过控制台设置
在“新建 Workload 页面”，填写 GPU 相关资源，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/9539ca990e24c089842113e25e6961fc.png)
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

其中：

- requests 和 limits 中和 qGPU 相关的资源值必须一致（根据 K8S 的规则，可以省略掉 requests 中对 qGPU 的设置，这种情况下 requests 会被自动设置为和 limits 相同的值）。
- tke.cloud.tencent.com/qgpu-memory 表示容器申请的显存（单位G），**整数分配，不支持小数**。
- tke.cloud.tencent.com/qgpu-core 代表容器申请的算力，每个 GPU 卡可以提供100%算力，**qgpu-core 的设置应该小于100**，设置值超过剩余算力比例值，则设置失败，设置后容器可以得到一张 GPU 卡 n% 的算力。
:::
</dx-tabs>




## 部署在集群内的 Kubernetes 对象

| Kubernetes 对象名称 | 类型               | 请求资源                              | Namespace   |
| ------------------- | ------------------ | ------------------------------------- | ----------- |
| qgpu-manager        | DaemonSet          | 每 GPU 节点一个 Memory: 300M, CPU:0.2 | kube-system |
| qgpu-manager        | ClusterRole        | -                                     | -           |
| qgpu-manager        | ServiceAccount     | -                                     | kube-system |
| qgpu-manager        | ClusterRoleBinding | -                                     | kube-system |
| qgpu-scheduler      | Deployment         | 单一副本 Memory: 800M, CPU:1          | kube-system |
| qgpu-scheduler      | ClusterRole        | -                                     | -           |
| qgpu-scheduler      | ClusterRoleBinding | -                                     | kube-system |
| qgpu-scheduler      | ServiceAccount     | -                                     | kube-system |
| qgpu-scheduler      | Service            | -                                     | kube-system |

