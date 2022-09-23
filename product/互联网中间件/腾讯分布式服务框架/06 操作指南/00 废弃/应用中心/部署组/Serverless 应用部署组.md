Serverless 部署组的操作包括两种：

- 基础操作：部署组的创建和删除。
- 应用生命周期管理相关操作：设置最小实例数和内存规格、部署应用、启动应用、停止应用。

## 基础操作

### 创建部署组

1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf/index)，在左侧导航栏中，单击**部署组**。
2. 在部署组页面顶部选择集群。
3. 单击部署组列表上方的**新建部署组**。
![](https://qcloudimg.tencent-cloud.cn/raw/24131a9e316f7986a92d38f44f974e08.png)
4. 设置部署组相关信息。
	- **部署组名称**：部署组的名称，不超过60个字符。
	- **集群名称**：选择 Serverless 集群名称。
	- **命名空间**：选择命名空间。
	- **关联应用**：关联应用字段决定了后续程序包来源和应用配置来源。
		![](https://main.qcloudimg.com/raw/a0537f82c8f8a57d220acc154042279e.png)

### 删除部署组

> !您需要下线部署组内所有实例，才能执行部署组的删除操作。

1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf/index)，在左侧导航栏中，单击**部署组**。
2. 在部署组列表，单击右侧操作列的**更多** > **删除**。
3. 在弹出的提醒框中，单击**确认**，完成删除。

## 应用生命周期管理

| 功能       | 说明                                            |
| ---------- | ----------------------------------------------- |
| 最小实例数 | Serverless 应用启动时运行的最小实例数。         |
| 内存规格   | Serverless 应用启动时每台实例所运行的内存规格。 |
| 部署应用   | 将应用部署到 Serverless 上，并执行启动命令。    |
| 启动应用   | 当应用处于停止状态时可以启动应用。              |
| 停止应用   | 当应用处于运行中状态时可以停止应用。            |

### 设置内存规格和最小实例数

新建 Serverless 部署组时，单击页面底部的高级设置，即可设置内存规格和最小实例数。
![](https://main.qcloudimg.com/raw/7b58b336541693f3f03fe6d253afeb73.png)

### 部署应用

1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf/index)，在左侧导航栏中，单击**部署组**。
2. 在部署组列表页，单击右侧操作列的**部署应用**，选择程序包。
![](https://qcloudimg.tencent-cloud.cn/raw/579c50ebd919795738f887816c4bf86d.png)
3. 在高级设置中，设置最小实例数（选填），单击**提交**完成部署。
   ![](https://main.qcloudimg.com/raw/082382940ae0a5ac13c144efae346450.png)
4. 应用部署成功后，部署组中的 **运行实例数** 数值发生变化。
![](https://qcloudimg.tencent-cloud.cn/raw/f6aa1768c465cca3908efbe6a408c5f7.png)


### 启动/停止应用

1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf/index)，在左侧导航栏中，单击**[部署组](https://console.cloud.tencent.com/tsf/group)**。
2. 在部署组列表，单击右侧操作列的**更多**，即可设置停止应用,重启应用,启动应用等操作。
![](https://qcloudimg.tencent-cloud.cn/raw/ea649b321b6bf02e6522addf33173c3d.png)
