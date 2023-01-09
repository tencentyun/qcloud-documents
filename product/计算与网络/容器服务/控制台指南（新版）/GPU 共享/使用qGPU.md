## 使用须知

- **版本支持：**TKE 版本 ≥ v1.14.x
- **节点支持：**支持原生节点以及普通节点，推荐 [原生节点](https://cloud.tencent.com/document/product/457/78197)，原生节点搭载 FinOps 理念，配合 qGPU 使用可全面提升 GPU/CPU 资源利用率。
- **OS 支持**：推荐使用 TencentOS Server 3.1 (TK4) ，稳定高效。不推荐使用市场镜像，公共镜像更稳定、高效、更易维护。
<table>
<thead>
  <tr>
    <th>镜像 ID</th>
    <th>Os Name</th>
    <th>控制台操作系统展示名</th>
    <th>OS 类型</th>
    <th>发布状态</th>
    <th>备注</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href="https://console.cloud.tencent.com/cvm/image/detail?rid=16&id=img-eb30mz89">img-eb30mz89</a></td>
    <td>tlinux3.1x86_64</td>
    <td>TencentOS Server 3.1(TK4)</td>
    <td>Tencent OS Server</td>
    <td>全量发布</td>
    <td>推荐使用 Tencent OS Server 最新发行版<br>内核版本：5.4.119</td>
  </tr>
      <tr>
    <td><a href="https://console.cloud.tencent.com/cvm/image/detail?rid=1&id=img-9axl1k53">img-9axl1k53</a></td>
    <td>tlinux2.4(tkernel4)x86_64</td>
    <td>TencentOS Server 2.4(TK4)</td>
    <td>Tencent OS Server</td>
    <td>全量发布</td>
    <td>内核版本：5.4.119</td>
  </tr>
  <tr>
    <td><a href="https://console.cloud.tencent.com/cvm/image/detail/8/PUBLIC_IMAGE/img-22trbn9x">img-22trbn9x</a></td>
    <td>ubuntu20.04x86_64</td>
    <td>Ubuntu Server 20.04.1 LTS 64bit</td>
    <td>Ubuntu</td>
    <td>内测中，请 <a href="https://console.cloud.tencent.com/workorder/category">提交工单</a> 进行申请</td>
    <td>Ubuntu 20.04.1 公版内核</td>
  </tr>
  <tr>
    <td><a href="https://console.cloud.tencent.com/cvm/image/detail?rid=1&id=img-pi0ii46r">img-pi0ii46r</a></td>
    <td>ubuntu18.04.1x86_64</td>
    <td>Ubuntu 18.04 LTS 64bit</td>
    <td>Ubuntu</td>
    <td>全量发布</td>
    <td>Ubuntu 18.04.1 公版内核</td>
  </tr>
  <tr>
    <td><a href="https://console.cloud.tencent.com/cvm/image/detail/8/PUBLIC_IMAGE/img-25szkc8t">img-25szkc8t</a></td>
    <td>centos8.0x86_64</td>
    <td>CentOS 8.0</td>
    <td>CentOS</td>
    <td>内测中，请 <a href="https://console.cloud.tencent.com/workorder/category">提交工单</a> 进行申请</td>
    <td>Centos 8.0 公版内核</td>
  </tr>
  <tr>
    <td><a href="https://console.cloud.tencent.com/cvm/image/detail?rid=1&id=img-9qabwvbn">img-9qabwvbn</a></td>
    <td>centos7.6.0_x64</td>
    <td>CentOS 7.6</td>
    <td>CentOS</td>
    <td>全量发布</td>
    <td>Centos 7.6 公版内核</td>
  </tr>
</tbody>
</table>
- **GPU 卡架构：**支持 Volta（如 **V100**）、Turing（如 **T4**）、Ampere（如 **A100、A10**）。
- **驱动版本：**支持驱动版本由镜像和机型所共同决定，具体可参考 [步骤3](#step3)。
>? 为保证兼容性，我们推荐您在节点上安装 NVIDIA 驱动，无需在 POD 内部重复安装。
>
- **共享粒度：**每个 qGPU 最小分配1G显存，精度单位是1G。算力最小分配5（代表一张卡的5%），最大100（代表一张卡），精度单位是5（即5、10、15、20 ... 100）。
- **整卡分配：**开启了 qGPU 能力的节点可按照 `tke.cloud.tencent.com/qgpu-core: 100 | 200 | ...`（N * 100，N 是整卡个数）的方式分配整卡。建议通过 TKE 的节点池能力来区分 NVIDIA 分配方式或转换到 qGPU 使用方式。
- **个数限制：**一个 GPU 上最多可创建16个 qGPU 设备。建议按照容器申请的显存大小确定单个 GPU 卡可共享部署的 qGPU 个数。
- **升级需知：**如需升级 Kubernetes Master 版本，请注意：
  - 对于托管集群，无需重新设置本插件。
  - 对于独立集群，master 版本升级会重置 master 上所有组件的配置，从而影响到 qgpu-scheduler 插件作为 Scheduler Extender 的配置，因此 qGPU 插件需要卸载后再重新安装。

## 操作步骤

>? 由于使用 qGPU 能力需要使用特定镜像以及设置相关 Label，因此推荐您使用 TKE 的 [节点池](https://cloud.tencent.com/document/product/457/43719) 能力来对节点进行分组管理（节点池的节点具备统一的 Label 以及镜像属性），详情请参见 [新建节点池](https://cloud.tencent.com/document/product/457/43735)。

### 步骤1：安装 qGPU 调度组件
1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)，在左侧导航栏中选择**集群**。
2. 在“集群管理”页面选择地域，单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**组件管理**，在组件管理页面中单击**新建**。
4. 在“新建组件”页面中勾选 QGPU（GPU隔离组件）。
5. 单击**参数配置**，设置 qgpu-scheduler 的调度策略。
   - **spread**：多个 Pod 会分散在不同节点、不同显卡上，优先选择资源剩余量较多的节点，适用于高可用场景，避免把同一个应用的副本放到同一个设备上。
   - **binpack**：多个 Pod 会优先使用同一个节点，适用于提高 GPU 利用率的场景。
6. 单击**完成**即可创建组件。安装成功后，需要为集群准备 GPU 资源。

### 步骤2：开启集群 qGPU 共享
1. 单击目标集群 ID，进入集群详情页。
2. 单击 **qGPU 共享**右侧的![](https://qcloudimg.tencent-cloud.cn/raw/ac424dc18407ca5df9d26132588673d5.png)，开启 qGPU 共享。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/1f86d47db6a4df577cdb5ffc4eddbd8a.png)
开启后，**集群中所有新增 GPU 节点**默认开启 GPU 共享能力。您可以在 [步骤3](#step3) 中通过 Label 控制是否开启隔离能力。


[](id:step3)
### 步骤3：准备 GPU 资源
1. 在**节点管理 > 节点池**中，单击**新建节点池**。
2. 在“新建节点池”中，选中支持镜像，例如 **TencentOS Server 3.1 (TK4)** 并设置相关驱动。
设置镜像并选择机型后, 可以根据需求选择 GPU 驱动的版本、CUDA 版本、cuDNN 版本。
![](https://main.qcloudimg.com/raw/1869ca364f14446013570f9398bf1315.jpg)
<dx-alert infotype="explain" title="">
- 勾选“后台自动安装 GPU 驱动”，将在系统启动时进行自动安装，预计耗时15-25分钟。支持的驱动版本由 OS 以及 GPU 机型共同决定，详情可参见 [GPU 后装驱动版本列表](https://cloud.tencent.com/document/product/560/30211#gpu-.E9.A9.B1.E5.8A.A8.E9.A2.84.E8.A3.85.E4.BF.A1.E6.81.AF.3Cspan-id.3D.22preloadgpudrive.22.3E.3C.2Fspan.3E)。
- 如果您未勾选“后台自动安装 GPU 驱动”，为了保证 GPU 机型的正常使用，针对某些低版本 OS，将会为您默认安装 GPU 驱动，完整的默认驱动版本信息可参考下表：
<table>
<thead>
<tr>
<th>OS名称</th>
<th>默认安装驱动版本</th>
</tr>
</thead>
<tbody><tr>
<td>CentOS 7.6、Ubuntu 18、Tencent Linux2.4</td>
<td>450</td>
</tr>
<tr>
<td>Centos 7.2 (不推荐)</td>
<td>384.111</td>
</tr>
<tr>
<td>Ubuntu 16 (不推荐）</td>
<td>410.79</td>
</tr>
</tbody></table>
</dx-alert>
3. 在**更多设置 > Labels** 中，通过节点池的高级配置来设置 Label，指定 qGPU 隔离策略：
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
4. 单击**创建节点池**即可。


### 步骤4：给应用分配共享 GPU 资源
通过给容器设置 qGPU 对应资源可以允许 Pod 使用 qGPU，您可以通过控制台或者 YAML 方式为应用分配 GPU 资源。
>?
> - 如果应用需要使用整数卡资源，只需填写卡数，无需填写显存（自动使用分配的 GPU 卡上全部显存）。
> - 如果应用需要使用小数卡资源（即和其他应用共享同一张卡），需要同时填写卡数和显存。
>
<dx-tabs>
::: 通过控制台设置
在“新建 Workload 页面”，填写 GPU 相关资源，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/122b5487e234952701ff798a8e78c4a8.png)
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
