## 操作场景
腾讯云容器服务 TKE 支持通过创建 PersistentVolume（PV）/PersistentVolumeClaim（PVC），并为工作负载挂载数据卷的方式使用腾讯云对象存储 COS。本文介绍如何在 TKE 集群中为工作负载挂载对象存储。

## 准备工作
### 安装对象存储扩展组件
>? 若您的集群已安装 COS-CSI 扩展组件，则请跳过此步骤。
>
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 选择左侧导航栏中的**集群**，进入集群管理界面。
3. 选择需新建组件的集群 ID，单击集群详情页左侧栏中的**组件管理**。
4. 在“组件管理”页面，单击**新建**，进入“新建组件”页面。
5. 勾选**COS（腾讯云对象存储）**并单击完成即可。

### 创建访问密钥[](id:CreatAccessKey)
>!
> - 为避免主账号密钥泄露造成您的云上资产损失，建议您参照[ 安全设置策略 ](https://cloud.tencent.com/document/product/598/10592)停止使用主账号登录控制台或者使用主账号密钥访问云 API，并使用已授予相关管理权限的子账号/协作者进行相关资源操作。
> - 本文以已授予访问管理相关权限的子用户创建或查看访问密钥为例，关于如何创建子用户并实现访问管理权限请参考文档[ 自定义创建子用户](https://cloud.tencent.com/document/product/598/13674)。
> 
1. 使用子账号用户登录[ 访问管理控制台 ](https://console.cloud.tencent.com/cam/overview)，单击左侧导航栏中的**访问密钥** > **API密钥管理**，进入 “API密钥管理”管理界面。
2. 单击**新建密钥**等待新建完成即可。
>?
>- 一个子用户最多可以创建两个 API 密钥。
>- API 密钥是构建腾讯云 API 请求的重要凭证，为了您的财产和服务安全，请妥善保存和定期更换密钥。当您更换密钥后，请及时删除旧密钥。


### 创建存储桶[](id:CreatBucket)
>!根据相关法规和政策要求，使用腾讯云对象存储服务前需要完成[ 实名认证](https://console.cloud.tencent.com/developer/auth)。
>
1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)，单击左侧导航中**存储桶列表**，进入“存储桶列表”页面。
2. 单击**创建存储桶**，在弹出的“创建存储桶”窗口，参考以下信息进行创建。如下图所示：
![](https://main.qcloudimg.com/raw/6837245b169037467e1934ff49269dd8.png)
   - **名称**：存储桶名称由 [自定义名称]-[开发商 APPID] 构成。请输入自定义名称，设置后不可修改。命名说明请参见存储桶的 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83)。
   - **所属地域**：请选择本文中目标集群所在地域，设置后不可修改。详情请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224)。
   - **多AZ特性**：开启多 AZ 特性后，可提供同地域多个数据中心的容灾。详情请参见 [多 AZ 特性概述](https://cloud.tencent.com/document/product/436/40548)。
   - **访问权限**：存储桶默认提供**私有读写**、**公有读私有写**和**公有读写**三种访问权限，设置后仍可修改。
      - **私有读写**：仅该存储桶的创建者及有授权的账号具备该存储桶对象的读写权限。存储桶访问权限默认为私有读写，推荐使用。
      - **公有读私有写**：任何人（包括匿名访问者）都具备该存储桶对象的读权限，但仅有存储桶创建者及有授权的账号具备该存储桶对象的写权限。
      - **公有读写**：任何人（包括匿名访问者）都具备该存储桶对象的读权限和写权限，不推荐使用。
   - **存储桶标签**：存储桶标签是一个键值对（key = value），是用于管理存储桶的标识，便于分组管理存储桶。详情请参见 [设置存储桶标签](https://cloud.tencent.com/document/product/436/34830)。
   - **服务端加密**：支持**不加密**和**SSE-COS 加密**（即由对象存储托管密钥的服务端加密）两种方式。
      - **SSE-COS加密**：对象存储托管密钥的服务端加密，由对象存储托管主密钥和管理数据，用户可通过对象存储直接对数据进行管理和加密。详情请参见 [服务端加密概述](https://cloud.tencent.com/document/product/436/18145)。
3. 确认信息无误后单击**确定**即可。创建完成后，即可在存储桶列表中进行查看。


### 获取存储桶子目录[](id:getPath)

1. 在“存储桶列表”页面，选择已创建的存储桶名称，进入该存储桶名称的详情页。
2. 在存储桶详情页面，选择需要挂载的子文件夹，进入该文件夹详情页。在页面右上角获取子目录路径 `/costest`。如下图所示：
![](https://main.qcloudimg.com/raw/40426184568dfe55103d98273ecf5e52.png)





## 操作步骤

### 通过控制台使用对象存储

#### 创建可以访问对象存储的 Secret[](id:StepOne)

1. 单击左侧导航栏中的**集群**，进入集群管理界面。
2. 选择目标集群 ID，进入集群详情页面。
3. 在集群详情页面，选择左侧菜单栏中的**配置管理** > **Secret**，进入 “Secret” 页面。如下图所示：
![](https://main.qcloudimg.com/raw/db1844b634f27d727362f9116f5dc16e.png)
4. 单击**新建**进入“新建Secret” 页面，根据以下信息进行设置。如下图所示：
![](https://main.qcloudimg.com/raw/ae126ccc936ac209fcb33234fd607a28.png)
	- **名称**：自定义，本文以 `cos-secret` 为例。
	- **Secret类型**：选择**Opaque**，该类型适用于保存密钥证书和配置文件，Value 将以 Base64 格式编码。
	- **生效范围**：选择**指定命名空间**，请确保 Secret 创建在 `kube-system` 命名空间下。
	- **内容**：此处用于设置 Secret 访问存储桶（Bucket）所需的访问密钥，需包含变量名 `SecretId` 和 `SecretKey` 及其分别所对应的变量值。
	请参考[ 创建访问密钥 ](#CreatAccessKey) 完成创建，并前往 [API密钥管理](https://console.cloud.tencent.com/cam/capi) 页面获取访问密钥。
5. 单击**创建 Secret**即可。


#### 创建支持 COS-CSI 动态配置的 PV [](id:StepTwo)
>!本步骤需使用存储桶，若当前地域无可用存储桶，则请参考 [创建存储桶](#CreatBucket) 进行创建。
>
1. 在目标集群详情页面，选择左侧菜单栏中的**存储** > **PersistentVolume**，进入 “PersistentVolume” 页面。
2. 单击**新建**进入“新建PersistentVolume” 页面，参考以下信息创建 PV。如下图所示：
![](https://main.qcloudimg.com/raw/b4442141eaf8cc2fbdf96a4bbbf99d8e.png)
主要参数信息如下：
	- **来源设置**：选择**静态创建**。
	- **名称**：自定义，本文以 `cos-pv` 为例。
	- **Provisioner**：选择为**对象存储COS**。
	- **读写权限**：对象存储仅支持多机读写。
	- **Secret**：选择已在[ 步骤1 ](#StepOne)创建的 Secret，本文以 `cos-secret` 为例（请确保 Secret 创建在 `kube-system` 命名空间下）。
	- **存储桶列表**：用于保存对象存储中的对象，按需选择可用存储桶即可。
	- **存储桶子目录**：填写已在[ 获取存储桶子目录 ](#getPath)中获取的存储桶子目录，本文以 `/costest` 为例。若填写的子目录不存在，则系统将为您自动创建。
	- **域名**：展示为默认域名，您可以使用该域名对存储桶进行访问。
	- **挂载选项**：COSFS 工具支持将存储桶挂载到本地，挂载后可直接操作对象存储中的对象，此项用于设置相关限制条件。本例中挂载选项 `-oensure_diskfree=20480` 表示当缓存文件所在磁盘剩余空间不足20480MB时，COSFS 运行将尽量减少使用磁盘空间。
>?不同的挂载项请以空格进行间隔，更多挂载选项请参见[ 常用挂载选项文档 ](https://cloud.tencent.com/document/product/436/6883#.E5.B8.B8.E7.94.A8.E6.8C.82.E8.BD.BD.E9.80.89.E9.A1.B9)。
3. 单击**创建PersistentVolume**即可。


#### 创建 PVC 绑定 PV[](id:StepThree)
>!请勿绑定状态为 Bound 的 PV。
>
1. 在目标集群详情页，选择左侧菜单栏中的**存储** > **PersistentVolumeClaim**，进入 “PersistentVolumeClaim” 页面。
2. 单击**新建**进入“新建PersistentVolumeClaim” 页面，参考以下信息创建 PVC。如下图所示：
![](https://main.qcloudimg.com/raw/8b7e7c5ece9db3104ceddded4a72b5d8.png)
	- **名称**：自定义，本文以 `cos-pvc` 为例。
	- **命名空间**：选择为 `kube-system`。
	- **Provisioner**：选择**对象存储COS**。
	- **读写权限**：对象存储仅支持多机读写。
	- **PersistentVolume**：选择在[ 步骤2 ](#StepTwo)中已创建的 PV，本文以 `cos-pv` 为例。
3. 单击**创建PersistentVolumeClaim**即可。

#### 创建 Pod 使用的 PVC
>?本步骤以创建工作负载 Deployment 为例。
>
1. 在目标集群详情页，选择左侧菜单栏中的**工作负载** > **Deployment**，进入 “Deployment” 页面。
2. 单击**新建**进入“新建Workload” 页面，参考[ 创建 Deployment ](https://cloud.tencent.com/document/product/457/31705#.E5.88.9B.E5.BB.BA-deployment)进行创建，并设置数据卷挂载。如下图所示：
![](https://main.qcloudimg.com/raw/5186f8d947d9593fb726aa95d7e5bd4b.png)
	- **数据卷（选填）**：
      - **挂载方式**：选择**使用已有PVC**。
      - **数据卷名称**：自定义，本文以 `cos-vol` 为例。
      - **选择 PVC**：选择已在[ 步骤3 ](#StepThree)中创建的 PVC，本文以选择 `cos-pvc` 为例。
	- **实例内容器**：单击**添加挂载点**，进行挂载点设置。
      - **数据卷**：选择为该步骤中所添加的数据卷 “cos-vol”。
      - **目标路径**：填写目标路径，本文以 `/cache` 为例。
      - **挂载子路径**：仅挂载选中数据卷中的子路径或单一文件。例如，`./data` 或 `data`。
3. 单击**创建Workload**即可。

### 通过 YAML 文件使用对象存储

#### 创建可以访问对象存储的 Secret[](id:StepOne)

可通过 YAML 创建可以访问对象存储的 Secret，模版如下：
```yaml
apiVersion: v1
kind: Secret
type: Opaque
metadata:
   name: cos-secret
   # Replaced by your secret namespace.
   namespace: kube-system
data:
   # Replaced by your temporary secret file content. You can generate a temporary secret key with these docs:
   # Note: The value must be encoded by base64.
   SecretId: VWVEJxRk5Fb0JGbDA4M...(base64 encode)
   SecretKey: Qa3p4ZTVCMFlQek...(base64 encode)
```

#### 创建支持 COS-CSI 动态配置的 PV[](id:StepTwo)
可通过 YAML 创建 PV 以支持 COS-CSI 动态配置，模版如下：
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
   name: "cos-pv"
spec:
   accessModes:
   - ReadWriteMany
   capacity:
     storage: 1Gi
   csi:
     driver: com.tencent.cloud.csi.cosfs
     # Specify a unique volumeHandle like bucket name.(this value must different from other pv's volumeHandle)
     volumeHandle: xxx
     volumeAttributes:
       # Replaced by the url of your region.
       url: "http://cos.ap-guangzhou.myqcloud.com"
       # Replaced by the bucket name you want to use.
       bucket: "testbucket-1010101010"
       # You can specify sub-directory of bucket in cosfs command in here.
       path: /costest
       # You can specify any other options used by the cosfs command in here.
       #additional_args: "-oallow_other"
     nodePublishSecretRef:
       # Replaced by the name and namespace of your secret.
       name: cos-secret
       namespace: kube-system
```

#### 创建 PVC 绑定 PV

可通过 YAML 创建绑定上述 PV 的 PVC，模版如下：
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
   name: cos-pvc
spec:
   accessModes:
   - ReadWriteMany
   resources:
     requests:
       storage: 1Gi
   # You can specify the pv name manually or just let kubernetes to bind the pv and pvc.
   # volumeName: cos-pv
   # Currently cos only supports static provisioning, the StorageClass name should be empty.
   storageClassName: ""
```

#### 创建 Pod 使用 PVC
可通过 YAML 创建 Pod，模版如下：
```yaml
apiVersion: v1
kind: Pod
metadata:
   name: pod-cos
spec:
   containers:
   - name: pod-cos
     command: ["tail", "-f", "/etc/hosts"]
     image: "centos:latest"
     volumeMounts:
     - mountPath: /data
       name: cos
     resources:
       requests:
         memory: "128Mi"
         cpu: "0.1"
   volumes:
   - name: cos
     persistentVolumeClaim:
       # Replaced by your pvc name.
       claimName: cos-pvc
```

## 相关信息
更多关于如何使用对象存储的信息请参见 [README_COSFS.md](https://github.com/TencentCloud/kubernetes-csi-tencentcloud/blob/master/docs/README_COSFS.md)。


