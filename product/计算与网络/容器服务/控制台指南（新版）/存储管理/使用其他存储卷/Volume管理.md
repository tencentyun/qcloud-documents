

## 简介

### 数据卷类型

<table>
	<tr>
	<th>数据卷类型</th>	<th>描述</th>
	</tr>
	<tr>
	<td>使用临时路径</td>
	<td>/</td>
	</tr>
	<tr>
	<td>使用主机路径</td>
	<td>将容器所在宿主机的文件目录挂载到容器的指定路径中（即对应 Kubernetes 的 HostPath）。您可以根据业务需求，不设置源路径（即对应 Kubernetes 的 EmptyDir）。如果不设置源路径，系统将分配主机的临时目录挂载到容器的挂载点。<b>指定源路径的本地硬盘数据卷适用于将数据持久化存储到容器所在宿主机，EmptyDir 适用于容器的临时存储。</b></td>
	</tr>
	<tr>
	<td>使用 NFS 盘</td>
	<td>只需填写 NFS 路径，您可以使用腾讯云的 <a href="https://cloud.tencent.com/document/product/582/9127">文件存储 CFS</a>，也可使用自建的文件存储 NFS。<b>使用 NFS 数据卷适用于多读多写的持久化存储，也适用于大数据分析、媒体处理、内容管理等场景。</b></td>
	</tr>
	<tr>
	<td>使用已有 PersistentVolumeClaim</td>
	<td>使用已有 PersistentVolumeClaim 声明工作负载的存储，自动分配或新建 PersistentVolume 挂载到对应的 Pod 下。主要适用于 StatefulSet 创建的有状态应用。</td>
	</tr>
	<tr>
	<td>使用腾讯云硬盘</td>
	<td>腾讯云基于 CBS 扩展的 Kubernetes 的块存储插件。您可以指定一块腾讯云的 CBS 云硬盘挂载到容器的某一路径下，当容器迁移时，云硬盘会随之迁移。<b>使用云硬盘数据卷适用于数据的持久化保存，可用于 Mysql 等有状态服务。设置云硬盘数据卷的服务，实例数量最大为1。</b></td>
	</tr>
	<tr>
	<td>使用 ConfigMap</td>
	<td>ConfigMap 以文件系统的形式挂载到 Pod 上，支持自定义 ConfigMap 条目挂载到特定的路径。更多详情请参见 <a href="https://cloud.tencent.com/document/product/457/31717">ConfigMap 管理</a>。</td>
	</tr>
	<tr>
	<td>使用 Secret</td>
	<td>Secret 以文件系统的形式挂载到 Pod 上，支持自定义 Secret 条目挂载到特定的路径。更多详情请参见 <a href="https://cloud.tencent.com/document/product/457/31718">Secret 管理</a>。</td>
	</tr>
</table>




### 数据卷的注意事项

- **创建数据卷后，需在**实例内容器**模块设置容器的挂载点。**
- 同一个服务下，数据卷的名称和容器设置的挂载点不能重复。
- 本地硬盘数据卷源路径为空时，系统将分配 `/var/lib/kubelet/pods/pod_name/volumes/kubernetes.io~empty-dir` 临时目录，且使用临时的数据卷生命周期与实例的生命周期保持一致。
- 数据卷挂载未设置权限，默认设置为读写权限。

## Volume 控制台操作指引
### 创建工作负载挂载数据卷

1. 登录容器服务控制台，并选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 在“集群管理”页面，单击需要部署 Workload 的集群 ID，进入待部署 Workload 的集群管理页面。
3. 在**工作负载**下，任意选择 Workload 类型，进入对应的信息页面。
例如，选择**工作负载** > **DaemonSet**，进入 DaemonSet 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/0098359fed5ce7eb42658604962f3165.png)
4. 单击**新建**，进入 “新建Workload” 页面。
5. [](id:Step5)根据页面信息，设置工作负载名、命名空间等信息。并在“数据卷”中，单击**添加数据卷**添加数据卷。
6. 根据实际需求，选择数据卷的存储方式，本文以**使用腾讯云硬盘**为例。
7. 在“实例内容器”的**挂载点**配置挂载点。如下图所示：
在 [步骤5](#Step5) 中选择**添加数据卷**后，才可进行挂载点配置。
![](https://main.qcloudimg.com/raw/ba8a35b82a905daa9823add9299b12d1.png)
8. 其余选项请按需设置，并单击**创建Workload**即可完成创建。


### 各类数据卷挂载配置
该表展示了不同数据卷的使用细节，**当您在创建工作负载时，并选择“添加数据卷”后**，可参照以下内容进行数据卷的添加以及挂载点的设置：

<table>
<thead>
        <tr>
            <th colspan="3" class="text-center salesInfoStyle">
                数据卷
            </th>
            <th colspan="3" class="text-center dispositionStyle">
                挂载点
            </th>
        </tr>
      <tr>
        <!-- <th style="position: relative;" [style.top]="columnTop"><span></span></th> -->
        <th style="position: relative;" class="salesInfoStyle" [style.top]="columnTop"><span rtsort="del_order">类型</span></th>
        <th style="position: relative;" class="salesInfoStyle" [style.top]="columnTop"><span rtsort="type">名称</span></th>
        <th style="position: relative;" class="salesInfoStyle" [style.top]="columnTop"><span>其他</span></th>
        <th style="position: relative;" class="salesInfoStyle" [style.top]="columnTop"><span rtsort="plant">目标路径</span></th>
        <th style="position: relative;" class="salesInfoStyle" [style.top]="columnTop"><span rtsort="customer">挂载子路径</span></th>
        <th style="position: relative;" class="salesInfoStyle" [style.top]="columnTop"><span rtsort="shipto">读写权限</span></th>
      </tr>
    </thead>
    <tbody><tr>
        <td>临时路径</td><td rowspan="8">自定义</td><td>/</td><td rowspan="8">请根据实际需求进行填写，示例如 <code>/cache</code>。</td><td rowspan="8">仅挂载选中数据卷中的子路径或单一文件，示例如 <code>/data</code> 或 <code>/test.txt</code>。</td><td rowspan="8">请根据实际需求进行选择。<li>只读：只允许读取该容器路径数据卷，数据修改只允许在宿主机上操作。</li><li>读写：允许读取以及将修改保存到该容器路径数据卷。</li></td>
    </tr>
    <tr>
        <td>主机路径</td><td>设置主机路径。<li>主机路径：该路径不能为空，例如当该容器需要访问 Docker 时主机路径可设置为<code>/var/lib/docker</code>。</li><li>检查类型：TKE 为您提供 NoChecks、DirectoryOrCreate 等多种检查类型，请仔细查阅控制台上每种类型介绍，并根据实际需求进行选择。</li></td>
    </tr>
    <tr>
        <td> NFS 盘</td><td> NFS 路径：填写文件系统 CFS 或自建 NFS 地址。<li>如需创建文件系统，请参看<a herf="https://cloud.tencent.com/document/product/582/9132">创建文件系统及挂载点。</a></li><li> NFS 路径示例如<code>10.0.0.161:/</code>。该路径可登录 <a href="https://console.cloud.tencent.com/cfs" target="_blank">文件系统控制台</a>，单击目标文件系统 ID ，在**挂载点信息**页签的 “Linux 下挂载目录”中获取。</li></td>
    </tr>
    <tr>
        <td>已有 PVC</td><td>请选择 PVC：根据实际需求进行选择。</td>
    </tr>
    <tr>
        <td>腾讯云硬盘</td><td>选择云硬盘：请根据实际需求进行选择。</td>
    </tr>
    <tr>
        <td>ConfigMap</td><td rowspan="2"><li>选择 ConfigMap：根据实际需求进行。</li><li>选项：提供“全部”和“指定部分Key”两种选择。</li><li>Items：当选择“指定部分Key” 选项时，可以通过添加 item 向特定路径挂载，如挂载点是 <code>/data/config</code>，子路径是 <code>dev</code>，最终会存储在 <code>/data/config/dev</code> 下。</li></td>
    </tr>
    <tr>
        <td>Secret</td>
</tr></tbody></table>



## Kubectl 操作 Volume 指引

仅提供示例文件，您可直接通过 Kubectl 进行创建操作。

### Pod 挂载 Volume YAML 示例
```Yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: k8s.gcr.io/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /cache
      name: cache-volume
  volumes:
  - name: cache-volume
    emptyDir: {}
```
- **spec.volumes**：设置数据卷名称、类型、数据卷的参数。
  - **spec.volumes.emptyDir**：设置临时路径。
  - **spec.volumes.hostPath**：设置主机路径。
  - **spec.volumes.nfs**：设置 NFS 盘。
  - **spec.volumes.persistentVolumeClaim**：设置已有 PersistentVolumeClaim
- **spec.volumeClaimTemplates**：若使用该声明，将根据内容自动创建 PersistentVolumeClaim 和 PersistentVolume。
- **spec.containers.volumeMounts**：填写数据卷的挂载点。
