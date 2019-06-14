## 操作场景

您可以通过控制台管理 Helm 应用的创建、删除、修改等操作，也可以通过本地安装 Helm 客户端连接到集群后，通过 Helm 命令行进行操作。

## 前提条件

- 已有腾讯云 TKE 集群，且拥有0.28核 CPU，180MiB内存的资源。
- 已在集群内开通 Helm 应用管理功能。
- 仅支持 kubernetes 1.8 以上版本的集群。

>? 
> - 若未开通 Helm 应用管理功能，请在 [Helm 应用](https://console.cloud.tencent.com/tke2/helm) 中，申请开通。
> - 开通 Helm 应用管理功能后，将在集群内安装 Helm tiller 相关组件。

 ![](https://main.qcloudimg.com/raw/5a0a28f215950ad6e666de6a855ed741.png)

## 操作步骤

### 创建 Helm 应用

1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，选择【应用中心】，单击【[Helm 应用](https://console.cloud.tencent.com/tke2/helm)】，进入 Helm 应用管理页面。
3. 单击【新建】，进入 “新建 Helm 应用” 页面。
4. 输入应用名，选择 “所在地域”、“运行集群” 以及需要安装的 Helm Chart 和对应的版本。如下图所示：
 ![](https://main.qcloudimg.com/raw/b662048d70667b37e75e2952acdbad0a.png)
 Helm Chart 来源主要分为以下两种：
 - TencentHub：可选择公开和私有两种。详情请参见 [TencentHub Helm Chart 操作指引](https://cloud.tencent.com/document/product/857/31683)。
 - 其他：选择 Helm 官方或自建 Helm Repo 仓库。
>!  当您选择 “其他” 类型来源时，Chart_url 属性必须设置为以 http 开头 tgz 结尾的参数值。
5. 单击【完成】。

### 更新 Helm 应用

1. 前往 [Helm 应用控制台](https://console.cloud.tencent.com/tke2/helm)。
2. 在 “Helm应用” 列表中，选择需要更新的 Helm 应用，单击【更新应用】。
3. 在弹出的 “更新Helm应用” 窗口中，选择需要更新的版本，并根据业务需求填写自定义参数。如下图所示：
![](https://main.qcloudimg.com/raw/19c866d8b2a09f9e2db2618f06bcc007.png)
>?  如果需要更新的应用为其他 Repo 创建的应用，则需要手动填写版本号。
4. 单击【完成】。

### 回滚 Helm 应用

1. 前往 [Helm 应用控制台](https://console.cloud.tencent.com/tke2/helm)。
2. 在 “Helm应用” 列表中，单击需要更新的 Helm 应用的应用名，进入应用详情页面。
3. 选择 “版本历史” 页签，在需要回滚的版本行中，单击【回滚】。

### 删除 Helm 应用

1. 前往 [Helm 应用控制台](https://console.cloud.tencent.com/tke2/helm)。
2. 在 “Helm应用” 列表中，选择需要删除的 Helm 应用，单击【删除】。
3. 在弹出的提示框中，单击【确认】。如下图所示：
![](https://main.qcloudimg.com/raw/10e67636bd07a48a4e9c426157330994.png)

