>!TDMQ 内测版本将于2020年9月17日上午09:00~12:00进行停服升级，升级后需要用户做少量改造重新接入。
升级之后，我们会完整帮您迁移数据，包括您创建的环境和 Topic 以及 VPC 接入点等数据，您无需担心基础数据的丢失。

## 操作场景
**本文档适用于2020年9月17日升级后进行参考和操作**。
本文主要介绍新版 TDMQ SDK 升级后如何快速恢复您原先业务代码的接入。

## 操作步骤
### 步骤1：创建角色并授权
1. 登录 [TDMQ 控制台](https://console.cloud.tencent.com/tdmq)，在左侧导航栏单击【角色管理】，进入角色管理页面。
2. 在角色管理页面，选择地域后，单击【新建】进行新建角色。
![](https://main.qcloudimg.com/raw/030444db462129f54a35ce19f7a92e41.png)
3. 在左侧导航栏单击【环境管理】，在所需环境上单击【配置权限】，配置刚刚创建的角色的权限。
![](https://main.qcloudimg.com/raw/f4fba0c916941ddafe837f5b775c555c.png)

   

### 步骤2：配置角色密钥
#### Java 客户端
当前由于 Pulsar 官方只有 Java 客户端提供了带有 listenerName 参数的最新版本，TDMQ 此次更新需要依赖于 listenerName 参数，所以截止目前只有 Java 客户端可以直接从官网下载。

1. 按照 [Java SDK 下载方式](https://cloud.tencent.com/document/product/1179/44914) 或者[Pulsar 官方文档](https://pulsar.apache.org/docs/zh-CN/2.6.1/client-libraries-java/)更新 Maven 依赖。在此我们仍推荐您按前者的指引使用腾讯云官方提供的SDK。
2. 前往 TDMQ 控制台【角色管理】，找到刚刚创建的角色，单击复制密钥。
3. 在创建 Client 的代码中加入刚刚复制的密钥，并添加  `listenerName` 参数
 ```java
   PulsarClient client = PulsarClient.builder()
			.serviceUrl("pulsar://*.*.*.*:6000/")
			.listenerName(custom:"1300*****0/vpc-******/subnet-********")
			.authentication(AuthenticationFactory.token("eyJh****"))
			.build();
```
>?`listenerName` 即“custom:”拼接原先的路由 ID（NetModel），路由 ID 可以在控制台【环境管理】接入点查看并复制。

#### Go 客户端
Go 客户端 Pulsar 官方目前还未更新最新适配的客户端，在官方适配之前需要下载腾讯云提供的 SDK。
1. 下载 SDK。
   ```sh
   $ go get -u "github.com/TencentCloud/tdmq-go-client/pulsar@v0.2.0-beta.1"
   ```
2. 在代码中重新导入。
   ```go
   import "github.com/TencentCloud/tdmq-go-client/pulsar"
   ```
3. 前往 TDMQ 控制台【角色管理】，找到刚刚创建的角色，单击复制密钥。
4. 在创建 Client 的代码中加入刚刚复制的密钥，并添加 ListenerName 参数
 ```go
   client, err := NewClient(ClientOptions{
			URL:            "pulsar://*.*.*.*:6000",
			ListenerName:	"custom:1300*****0/vpc-******/subnet-********",
			Authentication: NewAuthenticationToken("eyJh****"),
       })
```
 >?`listenerName`即“custom:”拼接原先的路由 ID（NetModel），路由 ID 可以在控制台【环境管理】接入点查看并复制。

### 步骤3：部署客户端
在修改完客户端代码后，您需要重新将客户端部署到原先的环境进行验证和生产。
