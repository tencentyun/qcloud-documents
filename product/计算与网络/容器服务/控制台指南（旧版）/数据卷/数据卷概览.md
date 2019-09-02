## 数据卷简介
在 Docker 中，数据卷是磁盘或另一容器中的目录。其生命周期不受管理，且 Docker 现在提供的卷驱动程序功能非常有限。腾讯云容器服务采用的是 Kubernetes 的数据卷的概念，Kubernetes 数据卷具有明确的生命周期管理，支持多种类型的数据卷，同时实例 ( Pod ) 可以使用任意数量的数据卷。
更多 Kubernetes 数据卷信息可见 [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/)。

## 数据卷类型选择
腾讯云容器服务是基于 Kubernetes 编排系统搭建的，创建服务时可以设置以下类型的数据卷：
- **本地硬盘**：将容器所在宿主机的文件目录挂载到容器的指定路径中（对应Kubernetes的HostPath）， 也可以不填写源路径（对应Kubernetes的EmptyDir），不填写时将分配主机的临时目录挂载到容器的挂载点，`指定源路径的本地硬盘数据卷适用于将数据持久化存储到容器所在宿主机，EmptyDir适用于容器的临时存储`，详情请参阅[使用本地硬盘数据卷](https://cloud.tencent.com/document/product/457/12133)。
- **云硬盘**：腾讯云基于CBS扩展的Kubernetes的块存储插件。可以指定一块腾讯云的 CBS 云硬盘挂载到容器的某一路径下，容器的迁移，云硬盘会跟随迁移，`使用云硬盘数据卷适用于数据的持久化保存，可用于Mysql等有状态服务，设置云硬盘数据卷的服务，实例数量最大为 1`，详情请参阅[使用云硬盘数据卷](https://cloud.tencent.com/document/product/457/12131)。
- **NFS盘**：可以使用腾讯云的[文件存储CFS](https://cloud.tencent.com/document/product/582/9127), 也可使用自建的文件存储NFS， 只需要填写NFS路径，`使用NFS数据卷适用于多读多写的持久化存储，适用于大数据分析、媒体处理、内容管理等场景`，详情请参阅[使用NFS数据卷](https://cloud.tencent.com/document/product/457/12130)。
- **配置项**：将配置项中指定 key 映射到容器中（key作为文件名），`使用配置项数据卷主要用于业务配置文件的挂载，可以用于挂载配置文件到指定容器目录`，详情请参阅[使用配置项数据卷](https://cloud.tencent.com/document/product/457/12134)。



## 数据卷的注意事项
1. 创建数据卷后需要设置容器的挂载点。
2. 同一个服务下数据卷的名称和容器设置的挂载点不能重复。
3. 本地硬盘数据卷源路径为空时，系统分配临时目录在`/var/lib/kubelet/pods/pod_name/volumes/kubernetes.io~empty-dir`. 使用临时的数据卷的生命周期与实例的生命周期保持一致。
4. 数据卷挂载未设置权限，默认设置为读写权限。
