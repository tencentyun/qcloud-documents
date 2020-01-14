Serverless部署组的操作包括两种：
- 基础操作：部署组的创建和删除。
- 应用生命周期管理相关操作：最小实例数、内存规格、部署应用、启动应用、停止应用。

## 基础操作
### 创建部署组
1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf/index)。
2. 在左侧导航栏中，单击【[部署组](https://console.cloud.tencent.com/tsf/group)】。
3. 在页面顶部选择集群。
4. 单击部署组列表上方的【新建部署组】。
![](https://main.qcloudimg.com/raw/7c0625ee021772a0630fd5a1ae63df56.png)
5. 设置部署组相关信息。
 - **部署组名称**：部署组的名称，不超过60个字符。
 - **集群名称**：选择Serverless集群名称。
 - **命名空间**：选择命名空间。
 - **关联应用**：关联应用字段决定了后续程序包来源和应用配置来源。
![](https://main.qcloudimg.com/raw/a0537f82c8f8a57d220acc154042279e.png)

### 删除部署组
1. 下线部署组内所有实例，才能执行部署组的删除操作。
2. 单击部署组列表页右侧的【删除】。



## 应用生命周期管理相关

|功能|说明|
|---|---|
|最小实例数 | Serverless 应用启动时运行的最小实例数|
|内存规格| Serverless 应用启动时每台实例所运行的内存规格|
|部署应用|将应用部署到Serverless上，并执行启动命令。|
|启动应用|当应用处于停止状态时可以启动应用。|
|停止应用|当应用处于运行中状态时可以停止应用。|

### 最小实例,内存规格

新建Serverless部署组，在<高级设置>下即可设置内存规格，最小实例数
![](https://main.qcloudimg.com/raw/a90cf7705e677d5347d50c6c5346c6da.png)

### 部署应用
1. 单击部署组列表页右侧的【部署应用】。
![](https://main.qcloudimg.com/raw/7fff167a22c7fdf6765d70c165f9e2f7.png)
2. 选择程序包后，在高级设置中，可设置最小实例数	（选填），单击【提交】。
![](https://main.qcloudimg.com/raw/ce1efcf26cd02ac6fbef2d86b6aa8fd0.png)
3. 应用部署成功后，部署组中的 **运行实例数** 数值发生变化。
![](https://main.qcloudimg.com/raw/2b545be372923f537f95d110e622e5e1.png)

### 启动/停止应用
单击部署组列表页右侧的【更多】,即可设置停止应用,重启应用,启动应用等操作。
![](https://main.qcloudimg.com/raw/2ff9b9c523f799ddf922ac9ae234472c.png)