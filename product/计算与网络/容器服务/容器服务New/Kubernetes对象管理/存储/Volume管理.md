## Volume 管理
### Volume 简介
#### 数据卷类型

- **使用主机路径**：将容器所在宿主机的文件目录挂载到容器的指定路径中（对应Kubernetes的HostPath）， 也可以不填写源路径（对应Kubernetes的EmptyDir），不填写时将分配主机的临时目录挂载到容器的挂载点，`指定源路径的本地硬盘数据卷适用于将数据持久化存储到容器所在宿主机，EmptyDir适用于容器的临时存储`.
- **使用NFS盘**：可以使用腾讯云的[文件存储CFS](https://cloud.tencent.com/document/product/582/9127), 也可使用自建的文件存储NFS， 只需要填写NFS路径，`使用NFS数据卷适用于多读多写的持久化存储，适用于大数据分析、媒体处理、内容管理等场景`.
- **使用已有PersistentVolumeClaim**:使用已有PersistentVolumeClaim来声明工作负载的存储，自动分配或新建PersistentVolume挂载到对应的Pod下，主要适用于StatefulSet创建有状态应用。更多请查阅[Persistent Volumes管理]().
- **使用新的PersistentVolumeClaim**:新建一个PersistentVolumeClaim来声明工作负载的存储，自动分配或新建PersistentVolume挂载到对应的Pod下，主要适用于StatefulSet创建有状态应用。更多请查阅[Persistent Volumes管理]().
- **使用腾讯云硬盘**：腾讯云基于CBS扩展的Kubernetes的块存储插件。可以指定一块腾讯云的 CBS 云硬盘挂载到容器的某一路径下，容器的迁移，云硬盘会跟随迁移，`使用云硬盘数据卷适用于数据的持久化保存，可用于Mysql等有状态服务，设置云硬盘数据卷的服务，实例数量最大为 1`.
- **使用ConfigMap**: 将ConfigMap已文件系统的形式挂载到Pod上，支持自定义ConfigMap的条目挂载到特定的路径。更多请查阅[ConfigMap管理]().
- **使用Secret**:将Secret已文件系统的形式挂载到Pod上，支持自定义Secret的条目挂载到特定的路径。更多请查阅[Secret管理]().


#### 数据卷的注意事项

1. 创建数据卷后需要设置容器的挂载点。
2. 同一个服务下数据卷的名称和容器设置的挂载点不能重复。
3. 本地硬盘数据卷源路径为空时，系统分配临时目录在`/var/lib/kubelet/pods/pod_name/volumes/kubernetes.io~empty-dir`. 使用临时的数据卷的生命周期与实例的生命周期保持一致。
4. 数据卷挂载未设置权限，默认设置为读写权限。


### Volume 控制台操作指引
#### 创建工作负载挂载数据卷
1. 点击需要部署 workloads 的集群ID，进入集群详情页面。
2. 点击 任意workloads类型 ，选择新建。
3. 根据指引设置数据卷参数，配置挂载点，完成创建。
![][createVolume]

### kubectl 操作 Volume 指引
以下仅提供示例文件，可直接通过Kubectl 进行创建操作。
#### Pod挂载Volume Yaml示例
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
- spec.volumes：此处设置数据卷名称，类型，数据卷的参数
  - spec.volumes.emptyDir：使用临时路径
  - spec.volumes.hostPath：使用主机路径
  - spec.volumes.nfs：使用NFS盘
  - spec.volumes.persistentVolumeClaim：使用已有PersistentVolumeClaim
- spec.volumeClaimTemplates: 若使用该声明，则根据内容自动创建PersistentVolumeClaim，进而自动创建PersistentVolume。
- spec.containers.volumeMounts：此次填写数据卷的挂载点
