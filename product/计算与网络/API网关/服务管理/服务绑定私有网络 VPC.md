## 操作场景
为服务绑定 [私有网络 VPC](https://console.cloud.tencent.com/vpc) 属性后，即可在服务中创建对接该 VPC 下后端资源的 API。

## 共享实例下服务绑定 VPC
### 创建服务绑定 VPC
1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/service) 。
2. 在左侧导航栏，单击**服务**，进入服务列表页。
3. 在当前地域下，单击页面左上角的**新建**，新建一个服务。在**基本信息配置**中，实例选择“共享型”；在**网络和可选配置**中即可为本次创建的服务绑定同地域下的 VPC。
![](https://qcloudimg.tencent-cloud.cn/raw/fa3a7a2ae4e267e1322eefd61d126a4a.png)

### 服务详情页绑定 VPC
当您在创建服务时未绑定 VPC 时，可在服务详情页为服务绑定 VPC，以实现对接 VPC 内资源。
1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/service)。
2. 在左侧导航栏，单击**服务**，进入服务列表页。
3. 选择需要绑定 VPC 的服务，单击**服务名称**，进入服务详情页。
4. 在服务详情页选择**基础配置**，进入基础配置页。
5. 在**基础配置**页找到**网络信息** > **所属 VPC** 字段，单击该字段后的**编辑图标**，即可在弹出框中为服务绑定 VPC。
![](https://qcloudimg.tencent-cloud.cn/raw/a9dba3794910ea2b9a86e3a1fa4e225b.png)


## 专享实例下服务绑定 VPC
由于专享实例本身具备 VPC 属性中，因此不需要用户操作绑定 VPC。创建专享实例下服务时，所属 VPC 字段会自动选择专享实例所在的 VPC。
![](https://qcloudimg.tencent-cloud.cn/raw/44b6ec02dfe85fe93297c52ff2c674e9.png)
