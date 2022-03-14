云托管服务可以通过其所在的 VPC（私有网络）访问您在腾讯云上的 CFS 文件存储。

## 使用场景
云托管服务基于容器部署并会弹性水平扩缩容，无法支持数据的持久化存储（若将数据直接存储在容器内存中，则容器缩容被销毁后数据会丢失）。如您有数据持久化需求，建议配合使用文件存储 CFS，将 CFS 挂载到指定的服务版本。

## 背景知识
了解更多文件存储 CFS 的使用方法，请参见 [文件存储CFS](https://cloud.tencent.com/document/product/582/9127)。 

## 前置条件
您的云托管服务和需要使用的 CFS 处于同一 VPC 内。单击云托管服务所在私有网络的名称，可以跳转到私有网络控制台查看该私有网络内您已有哪些文件存储资源，可以与此服务配合使用。若没有满足需要的文件存储资源，您可按以下操作步骤新建 CFS 并挂载使用。
<dx-alert infotype="notice" title="">
目前仅支持通过 API 方式挂载 CFS，控制台挂载操作暂未开放，敬请期待。
</dx-alert>

## 操作步骤
### 步骤1：确认云托管服务所在 VPC[](id:step1)
1. 登录 [云托管控制台](https://console.cloud.tencent.com/tcb/service)，在服务列表中找到您希望挂载CFS的服务；
2. 单击服务名称进入服务详情页，单击**服务配置**进入服务配置选项卡。
3. 在**基本信息**中找到服务的**所在私有网络**，记下服务所在的 VPC 和子网信息。

### 步骤2：检查 VPC 安全组配置[](id:step2)
了解更多什么是安全组及安全组如何使用，请参见 [私有网络安全组文档](https://cloud.tencent.com/document/product/215/20089)。
1. 在云托管控制台上，单击服务所在私有网络名称，跳转到对应的私有网络控制台；
2. 单击左侧菜单进入**安全** > **安全组**。
3. VPC 默认提供了一个 default 安全组，单击进入详情后，检查入站规则与出站规则是否如下图所示使用了默认值。
4. 如果您有其他安全组诉求无法直接使用上述 default 安全组默认值，则至少需保证您的安全组入站规则与出站规则符合以下条件：
	- **来源：**包含挂载 CFS 的服务所在的子网 IP 段。
	- **协议端口：**包含2049（对应 NFS 4.0 协议要求）。
![](https://main.qcloudimg.com/raw/e17c6c78e67ec7f31ed958c620d993de.jpg)
![](https://main.qcloudimg.com/raw/0c0dd045239e457d8fb4435000b6745f.png)


### 步骤3：检查 VPC 网络 ACL 配置[](id:step3)
了解更多什么是 ACL 及 ACL 如何使用，请参见 [私有网络ACL文档](https://cloud.tencent.com/document/product/215/20088)。
1. 在云托管控制台上，单击服务所在私有网络名称，跳转到对应的私有网络控制台。
2. 单击左侧菜单进入**安全** > **网络ACL**。
3. 单击**新建**创建 ACL，确保入站规则与出站规则如下图所示使用默认值。（已有符合条件的 ACL 可不用新建）。
4. 如果您有其他 ACL 诉求无法直接使用上述默认值，则至少需保证您的 ACL 入站规则与出站规则符合以下条件：
	- **来源：**包含挂载 CFS 的服务所在的子网 IP 段。
	- **协议端口：**包含2049（对应 NFS4.0 协议要求）。
![](https://main.qcloudimg.com/raw/be9abc7bf87535830e90d673a8ea58e3.jpg)
![](https://main.qcloudimg.com/raw/998c49084850e7ee45be91ed46be471a.png)

### 步骤4：创建文件存储 CFS[](id:step4)
1. 登录 [文件存储CFS控制台](https://console.cloud.tencent.com/cfs/overview)，单击**创建**，新增文件系统。
![](https://main.qcloudimg.com/raw/45df6a1f8a8504a3a148d3112a70871f.jpg)
2. **选择网络**字段请务必**选择在 [步骤1](#step1) 中查询到的 VPC 和子网**。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/a65f5f297d8db5ec7ee91c17cf85174e.jpg" style="width: 80%"> 


### 步骤5：通过 API 创建云托管服务版本
1. 在文件存储 CFS 控制台，查找所需使用的 CFS 的**挂载点信息**。
![](https://qcloudimg.tencent-cloud.cn/raw/691fbf82760263f5df2f0c73f0eed2d9.jpg)
2. 通过 API 创建服务版本接口，传入文件存储 CFS 信息。创建服务版本接口文档请参见 [接口文档](https://cloud.tencent.com/document/product/876/49627)。CFS 信息参数 MountVolumeInfo 示例如下所示：
```json
{
	"MountVolumeInfo": [{
		"Name": "cfs-test",
		"MountPath": "/cfs",
		"ReadOnly": false,
		"NfsVolumes": [{
			"Server": "10.0.0.16",
			"Path": "/",
			"ReadOnly": false,
			"SecretName": "",
			"EnableEmptyDirVolume": false
		}]
	}]
}
```

### 步骤6：验证 CFS 挂载成功
1. 登录 [云托管控制台](https://console.cloud.tencent.com/tcb/service)，进入**服务** > **版本** > **实例**。
2. 单击 **webshell** 登录容器。
![](https://main.qcloudimg.com/raw/09c460a8879af9fea06d9c8c23004d69.jpg)
3. 查看 CFS 是否挂载成功：
使用cd命令进入通过“MountPath”所设置的挂载目录。如示例中的“/cfs”。能成功打开则证明挂载成功。  
![img](https://main.qcloudimg.com/raw/2c48786f91eb66750baf9b5414e6b085.jpg)

## 说明
- 已有云托管服务不支持修改所在 VPC。若您已部署好了服务，误选了和 CFS 不相同的 VPC，可选择：
  - 重新在正确 VPC 部署服务，删除部署错误的服务。
  - 重新在正确 VPC 创建 CFS。
  - [打通多个 VPC](https://cloud.tencent.com/document/product/215/36698)。
- 云托管暂时仅支持上海、广州、北京地域。若您的 文件存储 CFS 实例不在上述地域则无法复用。更多地域将陆续开放，敬请期待。

