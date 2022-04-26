

## 前提条件
- 已有容器服务 TKE 托管集群（以下称作集群 A ），且集群版本需 >= 1.18 及以上。
- 已创建迁移目标的弹性容器服务 EKS 集群（以下称作集群 B），集群版本需 >= 1.20 及以上，创建 EKS 集群请参见 [创建集群](https://cloud.tencent.com/document/product/457/39813)。
- 集群 A 和 集群 B 需要共用同一个腾讯云 COS 存储桶作为 Velero 后端存储，配置 COS 存储桶请参见 [配置对象存储](https://cloud.tencent.com/document/product/457/50122#.E9.85.8D.E7.BD.AE.E5.AF.B9.E8.B1.A1.E5.AD.98.E5.82.A8)。
- 集群 A 和 集群 B 建议在同一 VPC 下（如果需要备份 PVC 中的数据，必须在同一 VPC 下）。
- 确保镜像资源在迁移后可以正常拉取，在 EKS 集群中配置镜像仓库请参见 [镜像仓库相关](https://cloud.tencent.com/document/product/457/54755#.E5.BC.B9.E6.80.A7.E9.9B.86.E7.BE.A4.E5.A6.82.E4.BD.95.E4.BD.BF.E7.94.A8.E8.87.AA.E5.BB.BA.E7.9A.84.E8.87.AA.E7.AD.BE.E5.90.8D.E9.95.9C.E5.83.8F.E4.BB.93.E5.BA.93.E6.88.96-http-.E5.8D.8F.E8.AE.AE.E9.95.9C.E5.83.8F.E4.BB.93.E5.BA.93.EF.BC.9F)。
- 确保两个集群的 Kubernetes 版本的 API 兼容，建议使用相同版本。若集群 A 的集群版本较低，建议先升级集群 A 集群版本后，再进行迁移操作。

## 迁移限制

- 在 TKE 集群中启用固定 ip 特性的工作负载，在迁移到 EKS 集群后，ip 会发生改变。
- EKS 集群使用 containerd v1.4.3 作为运行时，与 docker 不一致，不兼容 Docker registry v2.5 以下版本、harbor v1.10 以下的版本的镜像。
- EKS 集群中，每个 Pod 默认分配 20GiB 的免费临时磁盘空间，用于镜像存储，该盘随 Pod 的生命周期创建和销毁。
- EKS 不支持 RDMA。
- EKS 不支持自定义 net 前缀的内核参数。
- EKS 不支持部署 DaemonSet 类型的工作负载。
- EKS 不支持部署 NodePort 类型的服务。
- EKS Pod 不支持监听 9100 端口及 62000 以上端口。
- 除以上限制外，务必阅读 <a href="https://cloud.tencent.com/document/product/457/39815#.E5.85.B6.E4.BB.96.E8.AF.B4.E6.98.8E"> EKS 集群其他说明</a>。

## 迁移步骤
以下将介绍 TKE 集群 A 中的资源迁移到 EKS 集群 B 中的详细操作步骤。

### 配置对象存储
操作步骤请参见 [创建存储桶](https://cloud.tencent.com/document/product/457/50122#.E9.85.8D.E7.BD.AE.E5.AF.B9.E8.B1.A1.E5.AD.98.E5.82.A8)。

### 下载 velero
1. 下载 [Velero](https://github.com/vmware-tanzu/velero/releases) 最新版本安装包到集群环境中，本文以 v1.8.1 版本为例。  
```bash
wget https://github.com/vmware-tanzu/velero/releases/download/v1.8.1/velero-v1.8.1-linux-amd64.tar.gz
```
2. 执行以下命令解压安装包，安装包提供 Velero 命令行执行文件和一些示例文件。  
```bash
tar -xvf velero-v1.8.1-linux-amd64.tar.gz
```
3. 执行以下命令，将 Velero 可执行文件从解压后的目录迁移到系统环境变量目录下直接使用，本文以迁移至 `/usr/bin` 目录为例。示例如下：
```bash
cp velero-v1.8.1-linux-amd64/velero /usr/bin/
```

### 在集群 A 和集群 B 中安装 velero

1. 配置 velero 客户端，开启 CSI 特性。
```bash
velero client config set features=EnableCSI
```
2. 执行以下命令在集群 A 和集群 B 中安装 Velero ，创建 Velero 工作负载以及其他必要的资源对象。
	- 使用 CSI 备份 PVC 的示例如下：
```plaintext
velero install  --provider aws  \
--plugins velero/velero-plugin-for-aws:v1.1.0,velero/velero-plugin-for-csi:v0.2.0 \
--features=EnableCSI \
--features=EnableAPIGroupVersions \
--bucket <BucketName> \
--secret-file ./credentials-velero \
--use-volume-snapshots=false \
--backup-location-config region=ap-guangzhou,s3ForcePathStyle="true",s3Url=https://cos.ap-guangzhou.myqcloud.com
```
>! EKS 不支持部署 Daemonset，因此本文示例都不支持使用 restic 插件。
>
	- 如不需要备份 PVC，安装示例如下：
```plaintext
./velero install  --provider aws --use-volume-snapshots=false --bucket gtest-1251707795  --plugins velero/velero-plugin-for-aws:v1.1.0   --secret-file ./credentials-velero  --backup-location-config region=ap-guangzhou,s3ForcePathStyle="true",s3Url=https://cos.ap-guangzhou.myqcloud.com
```
安装参数说明详情见 [velero 安装参数](https://cloud.tencent.com/document/product/457/50122#velero)，您也可以使用命令 `velero install --help` 查看。
[](id:velero) 其他安装参数说明：
<table>
<thead>
<tr>
<th  nowrap="nowrap">安装参数</th>
<th>参数说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>--plugins</td>
<td>使用 AWS S3 兼容 API 插件  “velero-plugin-for-aws”；使用 CSI 插件 <a href="https://github.com/vmware-tanzu/velero-plugin-for-csi/">velero-plugin-for-csi</a> 对 csi-pv 进行备份，建议开启。</td>
</tr>
<tr>
<td>--features</td>
<td>启用可选功能：<a href="https://velero.io/docs/v1.8/enable-api-group-versions-feature/">启用 API 组版本功能</a> 该功能用于兼容不同 API 组版本，建议开启；<a href="https://velero.io/docs/v1.8/csi/">启用 CSI 快照功能</a> 该功能用于备份 CSI 支持的 PVC，建议开启。</td>
</tr>
<tr>
<td>--use-restic</td>
<td>Velero 支持使用免费开源备份工具 <a href="https://github.com/restic/restic">Restic</a> 备份和还原 Kubernetes 存储卷数据 （不支持 <code>hostPath</code> 卷，详情请参见 <a href="https://velero.io/docs/v1.5/restic/#limitations">Restic 限制</a>），该集成是 Velero 备份功能的补充，在迁移 EKS 集群的场景下，开启该参数会导致备份失败。</td>
</tr>
<tr>
<td>--use-volume-snapshots=false</td>
<td>关闭默认存储卷快照备份</td>
</tr>
</tbody></table>
3. 安装完成后，等待 Velero 工作负载就绪。执行以下命令，查看配置的存储位置是否可用，若显示 “Avaliable”，则说明集群可正常访问对象存储 COS。
```bash
velero backup-location get
NAME      PROVIDER   BUCKET/PREFIX      PHASE       LAST VALIDATED                  ACCESS MODE   DEFAULT
default   aws        <BucketName>   Available     2022-03-24 21:00:05 +0800 CST      ReadWrite     true
```
至此，Velero 安装完成。了解 Velero 更多安装介绍，请参见 [Velero](https://velero.io/docs/) 官网文档。

### （可选） 在集群 A 和集群 B 中安装 VolumeSnapshotClass 对象
>? 
>- 如不需要备份 PVC，可跳过该步骤。
>- 更多存储快照相关功能，请参见 [使用 CBS CSI 插件对 PVC 进行备份与恢复](https://cloud.tencent.com/document/product/457/50867)。

1. 确认已安装 [CBS-CSI 插件](https://github.com/TencentCloud/kubernetes-csi-tencentcloud/blob/master/docs/README_CBS.md)。
2. 在 [访问管理](https://console.cloud.tencent.com/cam/role) 控制台完成对 `TKE_QCSRole` 角色授予 CBS 快照操作的相关权限，详情请参考 [快照授权](https://cloud.tencent.com/document/product/457/51099#authorize)。
3. 使用以下 YAML，创建 VolumeSnapshotClass 对象。示例如下：
```yaml
apiVersion: snapshot.storage.k8s.io/v1beta1
kind: VolumeSnapshotClass
metadata:
  labels:
    velero.io/csi-volumesnapshot-class: "true"
  name: cbs-snapclass
driver: com.tencent.cloud.csi.cbs
deletionPolicy: Delete
```
4. 执行以下命令，检查 VolumeSnapshotClass 是否创建成功。示例如下：
```bash
$ kubectl get volumesnapshotclass
NAME            DRIVER                      DELETIONPOLICY   AGE
cbs-snapclass   com.tencent.cloud.csi.cbs   Delete           17m
```



### （可选） 创建集群 A 示例资源

>? 如不需要备份 PVC，可跳过该步骤。

在集群 A 中部署 Velero 实例中含有 PVC 的 minio 工作负载，这里使用 cbs-csi 动态存储类来创建 PVC 和 PV。
1. 使用集群中 provisioner 为 `com.tencent.cloud.csi.cbs` 的存储类来动态创建 pv。pvc 示例如下：
```bash
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  annotations:
    volume.beta.kubernetes.io/storage-provisioner: com.tencent.cloud.csi.cbs
  name: minio
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
  storageClassName: cbs-csi
  volumeMode: Filesystem
```
2. 使用 Helm 工具，创建一个引用上述 pvc 的 MinIO 测试服务，MinIO 安装方式请参见 [MinIO 安装](https://github.com/minio/charts)。在此示例中，已经为 MinIO 服务绑定了负载均衡器，可以在浏览器中使用公网地址访问管理页面。
![](https://qcloudimg.tencent-cloud.cn/raw/dec9aa32caf4ffb390bbb54b484aa3b5.png)
3. 登录 MinIO Web 管理页面，上传用于测试的图片。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/2d75a57b25205ca427e62f9ce50f42a8.png)

### 备份与还原
1. 在集群 A 创建备份，请参见**集群迁移**操作步骤中的 [集群 A 创建备份](https://cloud.tencent.com/document/product/457/50550#.E5.9C.A8.E9.9B.86.E7.BE.A4-a-.E5.88.9B.E5.BB.BA.E5.A4.87.E4.BB.BD)。
2. 在集群 B 还原备份，请参见**集群迁移**操作步骤中的 [集群 B 执行还原](https://cloud.tencent.com/document/product/457/50550#.E5.9C.A8.E9.9B.86.E7.BE.A4-b-.E6.89.A7.E8.A1.8C.E8.BF.98.E5.8E.9F)。
3. 迁移结果核验：
	- 如不需要备份 PVC，请参见**集群迁移**操作步骤中的 [迁移结果核验](https://cloud.tencent.com/document/product/457/50550#.E8.BF.81.E7.A7.BB.E7.BB.93.E6.9E.9C.E6.A0.B8.E9.AA.8C)。
	- 如需要备份 PVC，参照以下步骤进行核验：
  1. 执行以下命令，校验集群 B 执行迁移操作后的集群资源，可以看到 Pods、PVC、Service 资源已按预期迁移成功。如下图所示：
  ![](https://qcloudimg.tencent-cloud.cn/raw/3bafcbd38e9a9c63ba7804a4773e9a9c.png)
  2. 登录集群 B 中的 MinIO 服务，可以看到 MinIO 服务中的图片数据未丢失，说明持久卷数据已按预期迁移成功。
  ![](https://qcloudimg.tencent-cloud.cn/raw/f709be2542e9830116eaf03c77027e1c.png)
4. 至此已完成了 TKE 集群与 EKS 集群间资源的迁移。
  迁移操作完成后，执行以下命令，将集群 A 和 集群 B 的备份存储位置恢复为读写模式，以便在下次备份任务可以正常备份。示例如下：
  ```bash
  kubectl patch backupstoragelocation default --namespace velero \
     --type merge \
     --patch '{"spec":{"accessMode":"ReadWrite"}}'
  ```

## 使用 EKS 常见问题
- 拉取镜像失败：请参见 [镜像仓库](https://cloud.tencent.com/document/product/457/54755)。
- 域名解析失败：常见于 Pod 镜像拉取失败、投递日志到自建 kafka 失败，请参见 [弹性集群自定义 DNS 服务](https://cloud.tencent.com/document/product/457/63735)。
- 日志投递到 CLS 失败：首次使用 EKS 集群投递日志到 CLS，需要为服务授权，请参见 [首次授权](https://cloud.tencent.com/document/product/457/56751#.E9.A6.96.E6.AC.A1.E6.8E.88.E6.9D.83.3Ca-id.3D.22role.22.3E.3C.2Fa.3E)。
- 每个集群默认仅可创建 100 个 Pod，若需要创建超过配额的资源，请参见 [默认配额](https://cloud.tencent.com/document/product/457/53030#.E9.BB.98.E8.AE.A4.E9.85.8D.E9.A2.9D)。
- Pod 频繁被销毁重建，报错 `Timeout to ensure pod sandbox`：EKS Pod 内的组件会与管控面通讯以保持健康检测，当 Pod 创建完后，Pod 持续 6 分钟网络不通，则会被管控面发起销毁重建。此时需检查 Pod 关联的安全组是否放通了 169.254 路由的访问。
- Pod 端口访问不通 / not ready：
  - 业务容器端口是否与 EKS 管控面端口有冲突，请参见 [端口限制](https://cloud.tencent.com/document/product/457/39815#.E7.AB.AF.E5.8F.A3.E9.99.90.E5.88.B6)
  - Pod 可以 ping 成功，但是 telnet 失败，检查安全组。
- 创建实例时，可以使用如下特性加快拉取镜像速度：请参见 [镜像缓存](https://cloud.tencent.com/document/product/457/65908) 与 [镜像复用](https://cloud.tencent.com/document/product/457/54980#FAQ8)。
- 业务日志转存：EKS job 类型的业务在退出后，底层资源就被回收，此时 Kubectl logs 无法查看容器日志，对于需要 debug 的场景不友好。可通过延迟销毁或者设置 terminationMessage 字段将业务日志转存，请参见 [设置容器终止消息](https://cloud.tencent.com/document/product/457/54980#FAQ5)。
- Pod 频繁重启，报错 `ImageGCFailed`：EKS Pod 默认磁盘大小为 20GiB, 如果磁盘使用空间达到 80%，EKS 管控面就会触发容器镜像的回收流程，尝试回收未使用的容器镜像来释放磁盘空间。如果未能释放任何空间，则会有一条事件提醒：`ImageGCFailed: failed to garbage collect required amount of images`，提醒用户磁盘空间不足。常见磁盘空间不足的原因有：
  - 业务有大量临时输出。
  - 业务持有已删除的文件描述符，导致磁盘空间未释放。

## 参考文档
- [在 Velero 中使用 csi](https://velero.io/docs/v1.8/csi/)
- [在 Velero 中启用 API 组版本功能](https://velero.io/docs/v1.8/enable-api-group-versions-feature/)
- [使用应用市场安装 Minio](https://cloud.tencent.com/document/product/457/46432)
