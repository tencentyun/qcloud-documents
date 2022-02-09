## 操作场景

开源工具 [Velero](https://velero.io/)（旧版本名称为 Heptio Ark）可以安全地备份和还原、执行灾难恢复以及迁移 Kubernetes 集群资源和持久卷。在容器服务 TKE 集群或自建 Kubenetes 集群中部署 Velero 可以实现以下功能：
- 备份集群资源并在丢失的情况下进行还原。 
- 将集群资源迁移到其他集群。 
- 将生产集群资源复制到开发和测试集群。 

更多关于 Velero 介绍，请参见 [Velero](https://velero.io/) 官网文档。本文将介绍如何使用 Velero 实现 TKE 集群间的无缝迁移复制集群资源。 






## 迁移原理

在需要被迁移的集群和目标集群上都安装 Velero 实例，并且两个集群的 Velero 实例指向相同的腾讯云 [对象存储 COS](https://cloud.tencent.com/document/product/436) 位置，流程如下：
1. 使用 Velero 在需要被迁移的集群执行备份操作，生成备份数据存储到对象存储 COS。 
2. 在目标集群上使用 Velero 执行数据的还原操作实现迁移。 

迁移原理如下图示：
![velero](https://main.qcloudimg.com/raw/61a9cfc9067555df1494fe1f48add278.jpg)



## 前提条件

- 已 [注册腾讯云账号](https://cloud.tencent.com/register)。 
- 已开通腾讯云 [对象存储 COS](https://console.cloud.tencent.com/cos5) 服务。 
- 已有需要被迁移的 TKE 集群（以下称作集群 A），已创建迁移目标的 TKE 集群（以下称作集群 B），创建 TKE 集群请参见 [创建集群](https://cloud.tencent.com/document/product/457/32189)。 
- 集群 A 和 集群 B 都需要安装 Velero 实例（1.5版本以上），并且共用同一个对象存储 COS 存储桶作为 Velero 后端存储，安装步骤请参见 [配置存储和安装 Velero](https://cloud.tencent.com/document/product/457/50122#.E9.85.8D.E7.BD.AE.E5.AF.B9.E8.B1.A1.E5.AD.98.E5.82.A8)。 



## 注意事项

- 从 Velero 1.5版本开始，Velero 可以使用 Restic 备份所有 Pod 卷，无需单独注释每个 Pod。默认情况下，此功能允许用户使用 Restic 备份所有 Pod 卷，但以下卷情况除外：
   - 挂载默认 `Service Account Secret` 的卷
   - 挂载 `hostPath` 的类型卷
   - 挂载 Kubernetes `secrets` 和 `configmaps` 的卷
本示例需要 Velero 1.5以上版本且启用 [Restic](https://velero.io/docs/v1.5/restic/) 来备份持久卷数据，请确保在安装 Velero 阶段开启 `--use-restic` 和 `--default-volumes-to-restic` 参数，安装步骤请参见 [配置存储和安装 Velero](https://cloud.tencent.com/document/product/457/50122#.E9.85.8D.E7.BD.AE.E5.AF.B9.E8.B1.A1.E5.AD.98.E5.82.A8)。 
- 在执行迁移过程中，禁止对两边集群资源进行任何 CRUD 操作，以免在迁移过程中造成数据差异，导致最终迁移后的数据不一致。 
- 尽量保证集群 A 和集群 B 的CPU、内存等规格配置相同或不要相差太大，以免出现迁移后的 Pods 因资源原因无法调度导致 Pending 的情况。 


## 操作步骤

### 在集群 A 创建备份



#### 备份前查看集群 A 资源


在备份集群 A 之前，您可以查看集群 A 资源和服务情况，以便在还原集群之后用于 [迁移结果核验](#.E8.BF.81.E7.A7.BB.E7.BB.93.E6.9E.9C.E6.A0.B8.E9.AA.8C)。 

1. 本文将以 default 、default2 命名空间的资源情况作比较验证。执行以下命令，可以查看集群 A 中两个命名空间下的 Pods 和 PVC 资源情况。如下图所示：
![](https://main.qcloudimg.com/raw/f5c455c011d88bbfeac344d1dc51fbfd.png)
>?您可以在备份期间指定执行一些自定义 Hook 操作。例如，需要在备份之前将运行应用程序的内存中的数据持久化到磁盘。 了解 Hook 更多信息，请参见 [备份 Hook](https://velero.io/docs/v1.5/backup-hooks/)。 
2. 其中，集群 A 中的 MinIO 对象存储服务使用了持久卷，并且已上传一些图片数据，如下图所示：
![](https://main.qcloudimg.com/raw/b1260153686533a1384e2686ffe03fd1.png)

#### 备份集群

1. 执行以下命令，备份集群中不包含 Velero 命名空间（Velero 安装的默认命名空间）资源的其他所有资源，如果需要自定义备份的集群资源范围，可使用命令 `velero create backup -h` 查看支持的资源筛选参数。 
```bash
velero backup create <BACKUP-NAME> --exclude-namespaces <NAMESPACE>
```
	本示例以创建一个 “default-all” 集群备份为例，备份过程如下图所示。若备份任务状态显示 “Completed” 时，说明备份成功。 
	![](https://main.qcloudimg.com/raw/b6294ee314254d5524a9799bdf77112a.png)
>?您还可以为 Velero 设置定期自动备份，设置方法可以使用命令 `velero schedule -h`  查看。 
2. 执行以下命令，检查是否有备份操作发生错误，若命令无任何输出结果，则说明备份过程未发生任何错误。示例如下：
```bash
velero backup logs <BACKUP-NAME> | grep error
```
>!请确保备份过程未发生任何错误，若 Velero 在执行备份过程中发生错误，请排查解决后重新执行备份。 
>
3. 备份完成后执行以下命令，将备份存储位置临时更新为只读模式（非必须，可以防止在还原过程时， Velero 在备份存储位置中创建或删除备份对象）。示例如下：
```bash
kubectl patch backupstoragelocation default --namespace velero \
			--type merge \
			--patch '{"spec":{"accessMode":"ReadOnly"}}'
```

### 在集群 B 执行还原

#### 还原前查看集群 B 资源

在集群 B 执行还原前，您可以查看集群 B 资源和服务情况，以便在还原集群之后用于 [迁移结果核验](#.E8.BF.81.E7.A7.BB.E7.BB.93.E6.9E.9C.E6.A0.B8.E9.AA.8C)。 


在执行还原操作前，集群 B 中 default 、default2 命名空间下无任何工作负载资源。执行以下命令，可以查看集群 B 中两个命名空间下的 Pods 和 PVC 资源情况。如下图所示：
![image-20201118163640448](https://main.qcloudimg.com/raw/69447424d741418a88a85b7579fd124c.png)


#### 还原集群

1. 执行以下命令，将集群 B 中 Velero 备份存储位置临时也更新为只读模式（非必须，可以防止在还原过程时 Velero 在备份存储位置中创建或删除备份对象）。示例如下：
```bash
kubectl patch backupstoragelocation default --namespace velero \
			--type merge \
			--patch '{"spec":{"accessMode":"ReadOnly"}}'
```
>?您可以指定在还原期间或还原资源后执行自定义 Hook 操作。例如，可能需要在数据库应用程序容器启动之前执行自定义数据库还原操作。了解 Hook 更多信息，请参见 [还原 Hook](https://velero.io/docs/v1.5/restore-hooks/)。 
>
2. 在还原操作之前，需确保集群 B 中 的 Velero 资源与对象存储 COS 中的备份文件同步。默认同步间隔是1分钟，可以使用 `--backup-sync-period` 来配置同步间隔。可以执行以下命令，查看集群 A 的备份是否已同步。 
```bash
velero backup get <BACKUP-NAME>
```
3. 获取备份成功检查无误后，执行以下命令还原所有内容到集群 B 中。 
```bash
velero restore create --from-backup <BACKUP-NAME>
```
	还原过程如下图所示：
	![image-20201118175718281](https://main.qcloudimg.com/raw/13b5c653d6f64f800ef242567571408c.png)
4. 等待还原任务完成后查看还原日志，执行以下命令查看还原是否有报错和跳过信息。示例如下：
```bash
# 查看迁移时是否有错误的还原信息
velero restore logs <BACKUP-NAME> | grep error 
# 查看迁移时跳过的还原操作
velero restore logs <BACKUP-NAME> | grep skip
```
	如下图所示，可以查看还原步骤未发生错误，但出现部分 “skipped” 步骤，因为在备份集群资源时备份了不包含 Velero 命名空间的所有集群资源，有一些同类型同名的集群资源已经存在，例如 kube-system下的集群资源。当还原过程中有资源冲突时，Velero 会跳过该还原步骤，实际上该还原过程正常，可以忽略 “skipped” 日志（在特殊情况可以分析该日志）。 
	![](https://main.qcloudimg.com/raw/36f2cc21cdf30d6f4ec0b04e5ecab0f9.png)




### 迁移结果核验

1. 执行以下命令，校验集群 B 执行迁移操作后的集群资源，可以看到 default 、default2 命名空间下的 Pods 和 PVC 资源已按预期迁移成功。如下图所示：
![image-20201118173604915](https://main.qcloudimg.com/raw/57b9724a809ea73a699fc4c437da07b7.png)
2. 登录集群 B 中的 MinIO 服务，可以看到 MinIO 服务中的图片数据未丢失，说明持久卷数据已按预期迁移成功。 
![](https://main.qcloudimg.com/raw/c42a59abebd5049c0f85c564bcbf03f2.png)
3. 至此已完成了 TKE 集群间资源的迁移。 
  迁移操作完成后，执行以下命令，将集群 A 和 集群 B 的备份存储位置恢复为读写模式，以便在下次备份任务可以正常备份。示例如下：
```bash
kubectl patch backupstoragelocation default --namespace velero \
   --type merge \
   --patch '{"spec":{"accessMode":"ReadWrite"}}'
```



## 总结

本文主要介绍了在 TKE 集群间使用 Velero 迁移集群资源的原理、注意事项和操作方法，成功的将集群 A 中的集群资源无缝迁移到集群 B 中，整个迁移过程简单快捷，是一种非常友好的集群资源迁移方案。 

