
## 概述

开源工具 Velero（曾用名 Heptio Ark）可以安全地备份和还原集群资源，执行灾难恢复以及迁移 Kubernetes 群集资源和持久卷。在 TKE 集群或自建 Kubenetes 集群中部署 Velero 可以实现以下功能：
- 备份群集资源并在丢失的情况下进行还原。
- 将集群资源迁移到其他群集。
- 将生产集群资源复制到开发和测试集群。

Velero 工作原理图如下图所示（*来源于 Velero 官网*），当用户执行备份命令时，调用自定义资源 API 创建备份对象（1），BackupController 控制器检测到生成的备份对象时（2）执行备份操作（3），备份完成后将备份的集群资源和存储卷快照上传到 Velero 的后端存储（4和5）；类似的，当执行还原操作时，Velero 会将指定备份对象的数据从后端存储同步到 Kubernetes 集群完成还原工作。

![backup-process](https://main.qcloudimg.com/raw/1aea8598f3c0345101e91b586544896d.png)



更多关于 velero 介绍，请参阅 [Velero](https://velero.io/)，本文将介绍使用 [腾讯云COS](https://cloud.tencent.com/document/product/436) 作为 Velero 后端存储实现集群备份和还原的操作步骤。



## 前提条件

- 已 [注册腾讯云账户](https://cloud.tencent.com/register)。
- 已开通腾讯云 COS 服务，以下简称 COS 。
- 已创建 Kubernetes 集群，集群版本 v1.10 或更高版本，集群可正常使用 DNS 和 互联网服务。若需要创建 TKE 集群，请参考 [创建集群](https://cloud.tencent.com/document/product/457/32189)。



## 配置存储

### 创建腾 COS 存储桶

在腾讯云COS 控制台为 Velero 创建一个对象存储桶来存储备份。创建存储桶请参阅腾讯云 COS [创建存储桶 ](https://cloud.tencent.com/document/product/436/13309)使用说明 。

通过对象存储控制台为存储桶 [设置访问权限](https://cloud.tencent.com/document/product/436/13315)。对象存储 COS 支持设置两种权限类型：

- **公共权限**设置：为了安全起见，推荐存储桶权限类别为私有读写，关于公共权限的说明，请参见存储桶概述中的 [权限类别](https://cloud.tencent.com/document/product/436/13312#.E6.9D.83.E9.99.90.E7.B1.BB.E5.88.AB)。
- **用户权限**设置：主账号默认拥有存储桶所有权限（即完全控制）。另外 COS 支持添加子账号有数据读取、数据写入、权限读取、权限写入，甚至**完全控制**的最高权限。

由于需要对存储桶进行读写操作，为示例子账号授予**数据读取、数据写入**权限，如下图所示：

![image-20201113211352787](https://main.qcloudimg.com/raw/cd7a22242a3bf78fbb0bbb536b027efa.png)



### 获取存储桶访问凭证

Velero 使用与 AWS S3 兼容的 API 访问腾讯云 COS 存储， 需要使用一对访问密钥 ID 和密钥创建的签名进行身份验证，在 S3 API 参数中， `access_key_id` 字段为访问密钥ID ，`secret_access_key` 字段为密钥。

在腾讯云 [访问管理控制台](https://console.cloud.tencent.com/cam/capi) 新建和获取 COS 授权的示例子账号的腾讯云密钥 `SecretId` 与 `SecretKey`，如下图。其中  `SecretId` 值对应 `access_key_id` 字段， `SecretKey` 值 对应 `secret_access_key` 字段。

![image-20201113205035229](https://main.qcloudimg.com/raw/1689ca7f35bf291200558094a3905e17.png)

根据上述对应关系在本地目录中创建 Velero 所需的凭证配置文件 `credentials-velero`：

```bash
[default]
aws_access_key_id=<SecretId>
aws_secret_access_key=<SecretKey>
```



## 安装 Velero 

下载 [最新官方发行的 ](https://github.com/vmware-tanzu/velero/releases) Velero 压缩包到集群环境中，本示例以撰写此文档时最新版本 v1.5.2 为例。

```bash
wget https://github.com/vmware-tanzu/velero/releases/download/v1.5.2/velero-v1.5.2-linux-amd64.tar.gz
```

提取压缩包，压缩包中包含 velero 命令行执行文件和一些示例文件。

```bash
tar -xvf velero-v1.5.2-linux-amd64.tar.gz
```

将 `velero` 可执行文件从解压后的目录迁移到系统环境变量目录下直接使用，这里移至 /usr/bin 目录。

```bash
mv velero-v1.5.2-linux-amd64/velero /usr/bin/
```
执行下面 Velero 安装命令，创建 velero 和 restic 工作负载以及其他必要的资源对象。
```bash
velero install  --provider aws --plugins velero/velero-plugin-for-aws:v1.1.0 --bucket  <BucketName> \
--secret-file ./credentials-velero \
--use-restic \
--default-volumes-to-restic \
--backup-location-config \
region=ap-guangzhou,s3ForcePathStyle="true",s3Url=https://cos.ap-guangzhou.myqcloud.com
```

参数说明：

​	--provider：声明使用 `aws` 提供的插件类型。

​	--plugins：使用 AWS S3 兼容 API 插件  “velero-plugin-for-aws ”。

​	--bucket：在腾讯云 COS 创建的存储桶名。

​	--secret-file：访问腾讯云 COS 的访问凭证文件，见上面创建的 “credentials-velero” 凭证文件。

​	--use-restic： 使用开源免费备份工具 [restic](https://github.com/restic/restic) 备份和还原持久卷数据。

​	--default-volumes-to-restic： 启用使用Restic来备份所有Pod卷，前提是需要开启 `--use-restic` 参数。

​	--backup-location-config：备份存储桶访问相关配置。

​		region： 兼容 S3 API 的腾讯云 COS 存储桶地区，例如创建地区是广州的话，`region` 参数值为 “ap-guangzhou”。

​		s3ForcePathStyle： 使用 S3 文件路径格式。

​		s3Url：腾讯云 COS 兼容的 S3 API 访问地址。

Velero 支持使用免费开源备份工具 [restic](https://github.com/restic/restic) 备份和还原 Kubernetes 存储卷数据 (不支持 `hostPath` 卷，详情请参阅 [restic限制](https://velero.io/docs/v1.5/restic/#limitations))，这种集成是 Velero 备份功能的补充，建议开启。

腾讯云 COS 兼容的 S3 API 访问地址，请注意不是创建的 COS 存储桶的公网访问域名，而是要使用格式为 `https://cos.<region>.myqcloud.com` 的 URL，例如地区是广州的话，参数值为 “https://cos.ap-guangzhou.myqcloud.com”。

另外还有其他安装参数可以使用 `velero install --help` 查看，比如不想备份存储卷数据的话可以设置 `--use-volume-snapshots=false` 来关闭存储卷数据快照备份。

执行上面的安装命令后，安装过程如下图所示：

![image-20201113222922584](https://main.qcloudimg.com/raw/9015313121ed7987558c88081b052574.png)

安装命令执行完成后，等待 velero 和 restic 工作负载就绪后，查看配置的存储位置是否可用。

执行 `velero backup-location get` 命令查看存储位置状态，显示 “Avaliable”，则说明访问腾讯云COS正常，如下图所示：

![image-20201113221706250](https://main.qcloudimg.com/raw/69194157ccd5e377d1e7d914fd8c0336.png)

至此，Velero 安装完成，如想了解 Velero 更多安装介绍请参阅官网  [Velero 文档](https://velero.io/docs/ ) 。



## Velero 备份还原测试

在集群中使用 helm 工具创建一个具有持久卷的 minio 测试服务，minio 安装方式请参阅 [minio 安装]( https://github.com/minio/charts)，在此示例中，我已经为 minio 服务绑定了负载均衡器，可以在浏览器中使用公网地址访问管理页面。

![image-20201114222702080](https://main.qcloudimg.com/raw/f0fff5228527edc72d6e71a50d5dc966.png)

登录 minio Web 管理页面，上传一些测试的图片数据， 如下图：

![image-20201114223003538](https://main.qcloudimg.com/raw/e932223585c0b19891cc085ad7f438e1.png)

接下使用 Velero 备份，可以直接备份集群中的所有对象，也可以按类型，名称空间和/或标签过滤对象，本示例我使用下面命令仅备份 default 命名空间下所有资源：

```
velero backup create default-backup --include-namespaces default
```

使用 `velero backup get` 命令查看备份任务是否完成，当备份任务状态是 “Completed” 时，说明备份任务完成且没发生任何错误，备份过程如下图：

![image-20201114223905423](https://main.qcloudimg.com/raw/eb2bbabae48b188748f5278bedf177f1.png)

此时我们删掉 minio 所有资源，包括它的 PVC 持久卷， 如下图：

![image-20201114224920250](https://main.qcloudimg.com/raw/15ccaacf00640a04ae29ceed4c86195b.png)

删掉 minio 资源后，我们就可以测试使用之前的备份来还原被删除的 minio 资源了，先临时将备份存储位置更新为只读模式（这可以防止在还原过程中在备份存储位置中创建或删除备份对象）：

```bash
kubectl patch backupstoragelocation default --namespace velero \
    --type merge \
    --patch '{"spec":{"accessMode":"ReadOnly"}}'
   
```

修改 velero 的存储位置的访问权限为 “ReadOnly”，如下图所示：![image-20201114225639826](https://main.qcloudimg.com/raw/e8c2ab4e5e31d1370c62fad25059a8a8.png)

现在使用刚才 Velero 创建的备份 ”default-backup“ 来创建还原任务：

```bash
velero restore create --from-backup default-backup
```

同样可以使用 `velero restore get` 来查看还原任务的状态，若还原状态是 “Completed”，则说明还原任务完成，还原过程如下图：

![image-20201114230310180](https://main.qcloudimg.com/raw/effe8a0a7ce3aa8e422db00bfdddc375.png)

还原完成后，可以看到之前被删除的 minio 相关资源已经还原成功了，如下图：

![image-20201114230658577](https://main.qcloudimg.com/raw/1d53b0115644d43657c2a5ece805c9b4.png)

在浏览器上登录 minio 的管理页面，可以看到之前上传的图片数据还在，说明持久卷的数据成功还原，如下图：

> 注意：这里我们使用的 restic 来备份、还原的持久卷，但 restic 不支持 `hostPath` 类型卷，详情请参阅 [restic限制](https://velero.io/docs/v1.5/restic/#limitations)。

![image-20201114230426402](https://main.qcloudimg.com/raw/ceaca9ce6bc92bdce987c63d2fe71561.png)

还原完成后，不要忘记把备份存储位置恢复为读写模式，以便下次备份任务成功使用：

```bash
kubectl patch backupstoragelocation default --namespace velero \
   --type merge \
   --patch '{"spec":{"accessMode":"ReadWrite"}}'
```



## Velero 卸载

若想在集群中卸载 velero，使用下面命令即可完成卸载。

```bash
kubectl delete namespace/velero clusterrolebinding/velero

kubectl delete crds -l component=velero
```



## 总结

在本文中，我们简单介绍了 Kubernetes 集群资源备份工具 Velero，展示了如何配置腾讯云 COS 对象存储来作为 Velero 的后端存储，并成功实践了 minio 服务资源和数据的备份和还原操作 。



## 参考

Velero 官网：https://velero.io/

Restic 工具介绍：https://github.com/restic/restic

Minio 安装：https://github.com/minio/charts

restic限制：https://velero.io/docs/v1.5/restic/#limitations
