## 操作场景


开源工具 [Velero](https://velero.io/)（旧版本名称为 Heptio Ark）可以安全地备份和还原、执行灾难恢复以及迁移 Kubernetes 集群资源和持久卷。在容器服务 TKE 集群或自建 Kubenetes 集群中部署 Velero 可以实现以下功能：
- 备份集群资源并在丢失的情况下进行还原。 
- 将集群资源迁移到其他集群。 
- 将生产集群资源复制到开发和测试集群。 

Velero 工作原理图如下图所示（来源于 [Velero](https://velero.io/) 官网），当用户执行备份命令时，备份过程说明如下：
1. 调用自定义资源 API 创建备份对象（1）。 
2. BackupController 控制器检测到生成的备份对象时（2）执行备份操作（3）。 
3. 将备份的集群资源和存储卷快照上传到 Velero 的后端存储（4）和（5）。 
![backup-process](https://main.qcloudimg.com/raw/1aea8598f3c0345101e91b586544896d.png)

另外当执行还原操作时，Velero 会将指定备份对象的数据从后端存储同步到 Kubernetes 集群完成还原工作。 
更多关于 Velero 介绍，请参见 [Velero](https://velero.io/) 官网文档。本文将介绍如何使用腾讯云 [对象存储 COS](https://cloud.tencent.com/document/product/436) 作为 Velero 后端存储实现集群备份和还原。 




## 前提条件

- 已 [注册腾讯云账号](https://cloud.tencent.com/register)。 
- 已开通腾讯云 [对象存储 COS](https://console.cloud.tencent.com/cos5) 服务。 
- 已创建 v1.10 或以上版本的 Kubernetes 集群，集群可正常使用 DNS 和 互联网服务，详情请参见 [创建集群](https://cloud.tencent.com/document/product/457/32189)。 


## 操作步骤
### 配置对象存储

#### 创建存储桶

1. 在 [对象存储控制台](https://console.cloud.tencent.com/cos5) 为 Velero 创建一个对象存储桶用于存储备份，详情请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309)。 
2. 为存储桶 [设置访问权限](https://cloud.tencent.com/document/product/436/13315)。对象存储 COS 支持设置两种权限类型：
	- **公共权限**：为了安全起见，推荐存储桶权限类别为私有读写，关于公共权限的说明，请参见存储桶概述中的 [权限类别](https://cloud.tencent.com/document/product/436/13312#.E6.9D.83.E9.99.90.E7.B1.BB.E5.88.AB)。 
	- **用户权限**：主账号默认拥有存储桶所有权限（即完全控制）。另外 COS 支持添加子账号有数据读取、数据写入、权限读取、权限写入，甚至**完全控制**的最高权限。 
	由于需要对存储桶进行读写操作，为示例子账号授予**数据读取、数据写入**权限，如下图所示：
	![](https://main.qcloudimg.com/raw/3f23d6cfeca3c3b01bed6577bc173eb0.jpg)



#### 获取存储桶访问凭证

Velero 使用与 AWS S3 兼容的 API 访问 COS ，需要使用一对访问密钥 ID 和密钥创建的签名进行身份验证，在 S3 API 参数中：
- `access_key_id` ：访问密钥 ID 
- `secret_access_key`：密钥


1. 在腾讯云 [访问管理控制台](https://console.cloud.tencent.com/cam/capi) 新建和获取 COS 授权子账号的腾讯云密钥 `SecretId` 与 `SecretKey`。其中：
 -  `SecretId` 值对应 `access_key_id` 字段
 -  `SecretKey` 值对应 `secret_access_key` 字段
2. [](id:credentials)根据上述对应关系，在本地目录创建 Velero 所需的凭证配置文件 `credentials-velero`，内容如下：
```bash
[default]
aws_access_key_id=<SecretId>
aws_secret_access_key=<SecretKey>
```



### 安装 Velero 

1. 下载 [Velero](https://github.com/vmware-tanzu/velero/releases) 最新版本安装包到集群环境中，本文以 v1.5.2 版本为例。示例如下：
```bash
wget https://github.com/vmware-tanzu/velero/releases/download/v1.5.2/velero-v1.5.2-linux-amd64.tar.gz
```
2. 执行以下命令解压安装包，安装包提供 Velero 命令行执行文件和一些示例文件。示例如下：
```bash
tar -xvf velero-v1.5.2-linux-amd64.tar.gz
```
3. 执行以下命令，将 Velero 可执行文件从解压后的目录迁移到系统环境变量目录下直接使用，本文以迁移至 `/usr/bin` 目录为例。示例如下：
```bash
mv velero-v1.5.2-linux-amd64/velero /usr/bin/
```
4. 执行以下命令安装 Velero ，创建 Velero 和 Restic 工作负载以及其他必要的资源对象（安装参数说明请见 [下表](#velero)）。示例如下：
```plaintext
velero install  --provider aws --plugins velero/velero-plugin-for-aws:v1.1.0 --bucket  <BucketName> \
--secret-file ./credentials-velero \
--use-restic \
--default-volumes-to-restic \
--backup-location-config \
region=ap-guangzhou,s3ForcePathStyle="true",s3Url=https://cos.ap-guangzhou.myqcloud.com
```
[](id:velero)安装参数说明：
<table>
<thead>
<tr>
<th  nowrap="nowrap">安装参数</th>
<th>参数说明</th>
</tr>
</thead>
<tbody><tr>
<td>--provider</td>
<td>声明使用 <code>aws</code> 提供的插件类型。</td>
</tr>
<tr>
<td>--plugins</td>
<td>使用 AWS S3 兼容 API 插件  “velero-plugin-for-aws”。</td>
</tr>
<tr>
<td>--bucket</td>
<td>在对象存储 COS 创建的存储桶名。</td>
</tr>
<tr>
<td>--secret-file</td>
<td>访问对象存储 COS 的访问凭证文件，详情参见上述创建的 “<a href="#credentials">credentials-velero</a>” 凭证文件。</td>
</tr>
<tr>
<td>--use-restic</td>
<td>Velero 支持使用免费开源备份工具 <a href="https://github.com/restic/restic">Restic</a> 备份和还原 Kubernetes 存储卷数据 （不支持 <code>hostPath</code> 卷，详情请参见 <a href="https://velero.io/docs/v1.5/restic/#limitations">Restic 限制</a>），该集成是 Velero 备份功能的补充，建议开启。</td>
</tr>
<tr>
<td  nowrap="nowrap">--default-volumes-to-restic</td>
<td>启用使用 Restic 来备份所有 Pod 卷，前提是需要开启 <code>--use-restic</code> 参数。</td>
</tr>
<tr>
<td  nowrap="nowrap">--backup-location-config</td>
<td>备份存储桶访问相关配置，包括 region、s3ForcePathStyle、s3Url 等。</td>
</tr>
<tr>
<td>region</td>
<td>兼容 S3 API 的对象存储 COS 存储桶地域，例如创建地域为广州，region 参数值为 “ap-guangzhou”</td>
</tr>
<tr>
<td>s3ForcePathStyle</td>
<td>使用 S3 文件路径格式。</td>
</tr>
<tr>
<td>s3Url</td>
<td>对象存储 COS 兼容的 S3 API 访问地址。请注意该访问地址中的域名不是上述创建 COS 存储桶的公网访问域名，须使用格式为 https://cos.&lt;region&gt;.myqcloud.com 的 URL，例如地域为广州，则参数值为 <code>https://cos.ap-guangzhou.myqcloud.com。</code></td>
</tr>
</tbody></table>

其他安装参数可以使用命令 `velero install --help` 查看。例如，不备份存储卷数据，可以设置 `--use-volume-snapshots=false` 来关闭存储卷快照备份。 
执行安装命令之后查看安装过程，如下图所示：
![](https://main.qcloudimg.com/raw/817541d26a0d167de0a20a0f8127c8d1.png)

5. 安装完成后，等待 Velero 和 Restic 工作负载就绪。执行以下命令，查看配置的存储位置是否可用，若显示 “Avaliable”，则说明集群可正常访问对象存储 COS，如下图所示：
![](https://main.qcloudimg.com/raw/a1cf8fc3d5bd53daa09be30edac332fa.png)
至此，Velero 安装完成。了解 Velero 更多安装介绍，请参见 [Velero](https://velero.io/docs/) 官网文档。 



### Velero 备份还原测试

1. 在集群中使用 Helm 工具，创建一个具有持久卷的 MinIO 测试服务，MinIO 安装方式请参见 [MinIO 安装]( https://github.com/minio/charts)。在此示例中，已经为 MinIO 服务绑定了负载均衡器，可以在浏览器中使用公网地址访问管理页面。 
![](https://main.qcloudimg.com/raw/9352391a728698fe72ca414fb55d03d1.png)
2. 登录 MinIO Web 管理页面，上传用于测试的图片， 如下图所示：
![](https://main.qcloudimg.com/raw/9dd7e1f08709292e5c58f5744ffb5f10.png)
3. [](id:velerostep3)使用 Velero 备份，可以直接备份集群中的所有对象，也可以按类型，名称空间和/或标签过滤对象。您可以执行以下命令仅备份 default 命名空间下所有资源。示例如下：
```bash
velero backup create default-backup --include-namespaces default
```
4. 执行以下命令查看备份任务是否完成，当备份任务状态是 “Completed” 且 “ERRORS” 为0时，说明备份任务完成且未发生任何错误。 
```bash
velero backup get
```
	备份过程如下图所示：
	![](https://main.qcloudimg.com/raw/fff36d963fb9b600e3c34c0556c5a2bf.png)
5. 执行以下命令，删除 MinIO 下所有资源，包括 PVC 持久卷。如下图所示：
![](https://main.qcloudimg.com/raw/23a84feb0f24b45484175278c97c01b9.png)
6. 删除 MinIO 资源后，使用之前的备份测试是否可以成功还原被删除的 MinIO 资源。执行以下命令，将备份存储位置临时更新为只读模式（可以防止在还原过程中，Velero 在备份存储位置中创建或删除备份对象）。 
```bash
kubectl patch backupstoragelocation default --namespace velero \
			--type merge \
			--patch '{"spec":{"accessMode":"ReadOnly"}}'
```
	执行过程如下图所示：
	![](https://main.qcloudimg.com/raw/8abb88e5ce2586dc6f3c0d268883e4cd.png)
7. 执行以下命令，使用上述 [步骤3](#velerostep3) Velero 创建的备份 “default-backup” 来创建还原任务。示例如下：
```bash
velero restore create --from-backup default-backup
```
	通过命令 `velero restore get` 查看还原任务的状态，若还原状态是 “Completed” 且 “ERRORS” 为0时，则说明还原任务完成，如下图所示：
	![](https://main.qcloudimg.com/raw/ed52f0465d7bc59ce871678448961bd7.png)
8. 还原完成后，执行以下命令，可以查看到之前被删除的 MinIO 相关资源已经还原成功。如下图所示：
![](https://main.qcloudimg.com/raw/fc58c6f4325913d01cd7bb131a920d78.png)
9. 在浏览器上登录 MinIO 的管理页面，可以查看到之前上传的图片，说明持久卷的数据还原成功。如下图所示：
>!本文使用 Restic 来备份和还原持久卷，但 Restic 不支持 `hostPath` 类型卷，详情请参见 [Restic 限制](https://velero.io/docs/v1.5/restic/#limitations)。 
>
![](https://main.qcloudimg.com/raw/1ed0a87a01ece26311c41a026cc8013a.png)
10. 另外在还原完成后，可以执行以下命令，将备份存储位置恢复为读写模式，以便在下次可以正常备份。示例如下：
```bash
kubectl patch backupstoragelocation default --namespace velero \
			--type merge \
			--patch '{"spec":{"accessMode":"ReadWrite"}}'
```



### Velero 卸载

执行以下命令，可以在集群中卸载 Velero。示例如下：
```bash
kubectl delete namespace/velero clusterrolebinding/velero
kubectl delete crds -l component=velero
```



## 总结

本文主要介绍 Kubernetes 集群资源备份工具 Velero，展示了如何配置腾讯云 COS 对象存储来作为 Velero 的后端存储，并成功实践 MinIO 服务资源和数据的备份和还原操作。 



## 参考文档

- [Velero 官网](https://velero.io/)
- [Restic 工具介绍](https://github.com/restic/restic)
- [Minio 安装](https://github.com/minio/charts)
- [restic 限制](https://velero.io/docs/v1.5/restic/#limitations)
