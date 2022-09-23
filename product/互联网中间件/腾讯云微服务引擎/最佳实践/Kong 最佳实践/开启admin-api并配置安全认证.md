
## 操作场景

本文介绍 **Kong** 如何开启 **admin-api** 并为 **admin-api** 配置 **Basic Auth** 安全认证插件。

## 前置条件

已购买 Kong 网关实例，详情请参见 [操作文档](https://cloud.tencent.com/document/product/1364/72495)。

## 操作步骤

### 步骤1：在 Kong 的管理控制台上配置 admin api 的服务和路由

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse/kong)，进入需要配置限流插件的 Kong 网关实例详情页，在**配置管理**页查看管理控制台登录方式。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/296cd720bc50aba0da782189d28d0073.jpg">
2. 单击**访问链接**进入**管理控制台**页面，在左侧导航栏单击 **SERVICES**，进入服务列表。
3. 单击 **ADD NEW SERVICE**，在弹出的对话框中填写内容，URL 的内容填写为`http://127.0.0.1:8001/`，创建一个服务。
![](https://qcloudimg.tencent-cloud.cn/raw/acfbf91328042db2be86dda7af4c019c.png)
4. 创建成功后，在服务列表中单击已创建好的服务，进入负服务详情页面，在左侧导航栏单击 **Routes**，进入路由列表。
5. 单击 **ADD ROUTE**，在弹出的对话框中填写内容，**Path** 的内容填写为`/admin-api`，创建一个路由。
![](https://qcloudimg.tencent-cloud.cn/raw/95810088a197f2c55d21b19486dcbed0.png)
6. 打开浏览器通过公网地址访问`admin api`，`uri`的内容填写为`/admin-api`。
![](https://qcloudimg.tencent-cloud.cn/raw/99cb32eeaeebbd6595f84141c1fb84f3.png)

### 步骤2：为 admin api 配置 basic-auth 安全认证插件

1. 打开 Kong 的管理控制台, 在左侧导航栏单击 **CONSUMERS**，进入消费者列表。
2. 单击 **CREATE CONSUMER**，在弹出的对话框中填写内容。
![](https://qcloudimg.tencent-cloud.cn/raw/3202618ae55fbf08fb06e1b427cc751d.png)
3. 单击 **Credentials** 左侧的选项选择 BASIC，并单击 **CREATE CREDENTIALS**。
![](https://qcloudimg.tencent-cloud.cn/raw/82db60d5aad5a53d0977c8f89576e19d.png)
在弹出的对话框中填写内容，创建一个消费者。
![](https://qcloudimg.tencent-cloud.cn/raw/39e45a441b422278a4539c618c27cbcd.png)
4. 在左侧导航栏中依次单击 **SERVICES** > **admin-api** > **Plugins** > **ADD Plugin**，选择 **Basic Auth** 插件并完成添加。
![](https://qcloudimg.tencent-cloud.cn/raw/203484765fe355c48b216b4533f457c1.png)
![](https://qcloudimg.tencent-cloud.cn/raw/f96f1237bd5f93d2e8e5059a25a5d78d.png)
![](https://qcloudimg.tencent-cloud.cn/raw/d04c8c1f3bc4f87e3ff71320dc1a62af.png)
5. 打开浏览器通过公网地址访问 **admin api**，`uri` 的内容填写为`/admin-api`，输入之前配置好的用户名和密码即可访问。
![](https://qcloudimg.tencent-cloud.cn/raw/8f901928e48af88e59e49cbc4d5d473c.png)

## 参考

更多相关说明请参见 [Kong API Lookback](https://docs.konghq.com/gateway-oss/2.5.x/secure-admin-api/)。

