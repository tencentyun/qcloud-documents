## 简介

### 数据卷类型

- **使用主机路径**：将容器所在宿主机的文件目录挂载到容器的指定路径中（即对应 Kubernetes 的 HostPath）。您可以根据业务需求，不设置源路径（即对应 Kubernetes 的 EmptyDir）。如果不设置源路径，系统将分配主机的临时目录挂载到容器的挂载点。**指定源路径的本地硬盘数据卷适用于将数据持久化存储到容器所在宿主机，EmptyDir 适用于容器的临时存储。**
- **使用 NFS 盘**：只需填写 NFS 路径，您可以使用腾讯云的 [文件存储 CFS](https://cloud.tencent.com/document/product/582/9127)，也可使用自建的文件存储 NFS。**使用 NFS 数据卷适用于多读多写的持久化存储，也适用于大数据分析、媒体处理、内容管理等场景。**
- **使用已有 PersistentVolumeClaim**：使用已有 PersistentVolumeClaim 声明工作负载的存储，自动分配或新建 PersistentVolume 挂载到对应的 Pod 下。主要适用于 StatefulSet 创建的有状态应用。更多详情请参见 [PV 和 PVC 管理](https://cloud.tencent.com/document/product/457/31712)。
- **使用新的 PersistentVolumeClaim**：新建一个 PersistentVolumeClaim 声明工作负载的存储，自动分配或新建 PersistentVolume 挂载到对应的 Pod 下。主要适用于 StatefulSet 创建的有状态应用。更多详情请参见 [PV 和 PVC 管理](https://cloud.tencent.com/document/product/457/31712)。
- **使用腾讯云硬盘**：腾讯云基于 CBS 扩展的 Kubernetes 的块存储插件。您可以指定一块腾讯云的 CBS 云硬盘挂载到容器的某一路径下，当容器迁移时，云硬盘会随之迁移。**使用云硬盘数据卷适用于数据的持久化保存，可用于 Mysql 等有状态服务。设置云硬盘数据卷的服务，实例数量最大为 1。**
- **使用 ConfigMap**：ConfigMap 以文件系统的形式挂载到 Pod 上，支持自定义 ConfigMap 条目挂载到特定的路径。更多详情请参见 [ConfigMap 管理](https://cloud.tencent.com/document/product/457/31717)。
- **使用 Secret**：Secret 以文件系统的形式挂载到 Pod 上，支持自定义 Secret 条目挂载到特定的路径。更多详情请参见 [Secret 管理](https://cloud.tencent.com/document/product/457/31718)。


### 数据卷的注意事项

- 创建数据卷后，需设置容器的挂载点。
- 同一个服务下，数据卷的名称和容器设置的挂载点不能重复。
- 本地硬盘数据卷源路径为空时，系统将分配 `/var/lib/kubelet/pods/pod_name/volumes/kubernetes.io~empty-dir` 临时目录，且使用临时的数据卷生命周期与实例的生命周期保持一致。
- 数据卷挂载未设置权限，默认设置为读写权限。

## Volume 控制台操作指引

### 创建工作负载挂载数据卷

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击【集群】，进入集群管理页面。
3. 单击需要部署 Workload 的集群 ID，进入待部署 Workload 的集群管理页面。
4. 在 “工作负载” 下，任意选择 Workload 类型，进入对应的信息页面。例如，选择 “工作负载” > “DaemonSet”，进入 DaemonSet 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/73b214fcb0cf26e569310894dd44c512.png)
5. 单击【新建】，进入 “新建Workload” 页面。
6. 根据页面信息，设置工作负载名、命名空间等信息。并在 “数据卷” 中，单击【添加数据卷】，添加数据卷。如下图所示：
![添加数据卷](https://main.qcloudimg.com/raw/2e036dc898bd3fecfc59edd8742ff18a.png)
7. 根据实际需求，选择数据卷的存储方式，配置挂载点。
9. 单击【创建Workload】，完成创建。

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
- spec.volumes：设置数据卷名称、类型、数据卷的参数。
  - spec.volumes.emptyDir：设置临时路径。
  - spec.volumes.hostPath：设置主机路径。
  - spec.volumes.nfs：设置 NFS 盘。
  - spec.volumes.persistentVolumeClaim：设置已有 PersistentVolumeClaim
- spec.volumeClaimTemplates：若使用该声明，将根据内容自动创建 PersistentVolumeClaim 和 PersistentVolume。
- spec.containers.volumeMounts：填写数据卷的挂载点。
