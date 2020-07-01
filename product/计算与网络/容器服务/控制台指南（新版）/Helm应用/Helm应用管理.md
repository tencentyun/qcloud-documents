## 操作场景

您可以通过控制台进行 Helm 应用的创建、删除、修改等操作，也可以通过本地安装 Helm 客户端并连接到集群后，通过 Helm 命令行进行操作。

## 前提条件
- 已有腾讯云容器服务 TKE 集群，且至少为 Helm tiller 组件的安装预留0.28核 CPU 及180MiB内存的资源。
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
![](https://main.qcloudimg.com/raw/19e3da62e87d6f067e8c1d5563c9afa3.png)
	- **应用名**：自定义。
	- **来源**：支持使用第三方仓库来源，可以是 Helm 官方或自建 Helm Repo 仓库。
   - **下载地址**：根据实际需求填写具体 Chart 的下载地址，注意必须设置为以 `http` 开头 `.tgz` 结尾的参数值。本文示例为：`http://139.199.162.50/test/nginx-0.1.0.tgz`。
   - **类型**：提供公有和私有两种类型，请根据实际情况进行选择。
	- **Key-Value**：可通过设置自定义参数替换 Chart 包的默认配置，如 `image.repository = nginx`。
5. 单击【完成】，即可新建成功。

### 更新 Helm 应用

1. 前往 [Helm 应用控制台](https://console.cloud.tencent.com/tke2/helm)，进入 “Helm列表”页面。
2. 在 “Helm应用” 列表中，选择需更新的 Helm 应用所在行右侧的【更新应用】。
3. 在弹出的 “更新Helm应用” 窗口中，重新输入 “Chart_Url”，并根据业务需求填写自定义参数。如下图所示：
![](https://main.qcloudimg.com/raw/3c26cea1635755c096170676d0b43fe8.png)
4. 单击【确认】即可完成更新。

### 回滚 Helm 应用

1. 前往 [Helm 应用控制台](https://console.cloud.tencent.com/tke2/helm)，进入 “Helm列表”页面。
2. 在 “Helm应用” 列表中，单击需要更新的 Helm 应用名，进入应用详情页面。
3. 选择【版本历史】页签，单击需要回滚的版本所在行右侧的【回滚】。
>!仅支持更新过的 Helm 应用进行回滚操作。


### 删除 Helm 应用

1. 前往 [Helm 应用控制台](https://console.cloud.tencent.com/tke2/helm)，进入 “Helm列表”页面。
2. 在 “Helm应用” 列表中，选择需要删除的 Helm 应用所在行右侧的【删除】。
3. 在弹出的提示框中，单击【确认】即可。如下图所示：
![](https://main.qcloudimg.com/raw/0ddd2a8730af43235c3429dd2371f41c.png)

