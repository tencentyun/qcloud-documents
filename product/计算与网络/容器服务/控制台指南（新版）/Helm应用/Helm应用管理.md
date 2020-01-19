## 操作场景

您可以通过控制台进行 Helm 应用的创建、删除、修改等操作，也可以通过本地安装 Helm 客户端并连接到集群后，通过 Helm 命令行进行操作。

## 前提条件
- 已有腾讯云 TKE 集群，且至少拥有0.28核 CPU，180MiB内存的资源。
- 已在集群内开通 Helm 应用管理功能。
- 仅支持 kubernetes 1.8 以上版本的集群。

## 说明事项
- 若未开通 Helm 应用管理功能，请在 [Helm 应用](https://console.cloud.tencent.com/tke2/helm) 中申请开通。
- 开通 Helm 应用管理功能后，将在集群内安装 Helm tiller 相关组件。

## 操作步骤

### 创建 Helm 应用
1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的【Helm 应用】。
2. 在 “Helm应用” 页面上方，选择**所在地域**及**运行集群**，并单击【新建】。
4. 在 “新建 Helm 应用” 页面，根据实际需求填写以下参数。如下图所示：
![](https://main.qcloudimg.com/raw/b806bcd27f12261d2662e35c9992e8c6.png)
	- **应用名**：自定义。
	- **来源**：主要提供 TencentHub 和第三方仓库两种来源，请根据实际情况进行选择：
   - **TencentHub**：可选择公开和私有两种。详情请参见 [TencentHub Helm Chart](https://cloud.tencent.com/document/product/857/31683) 操作指引。
   >?TencentHub 预计将于2020年3月正式下线，目前仅存量用户可使用此功能，同时已不支持新用户开通使用。建议所有用户再次新建 Helm 应用时请选择第三方仓库来源进行创建。
     - **第三方仓库**：可以是 Helm 官方或自建 Helm Repo 仓库。
		- **下载地址**：根据实际需求填写具体 Chart 的下载地址，注意必须设置为以 `http` 开头 `tgz` 结尾的参数值。
	- **类型**：提供公有和私有两种类型，请根据实际情况进行选择。
	- **Key-Value**：可通过设置自定义参数替换 Chart 包的默认配置，如 `image.repository = nginx`。
5. 单击【完成】，即可新建成功。

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

