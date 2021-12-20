命名空间 ( Namespace ) 是对一组资源和对象的抽象集合。例如可以将开发环境，联调环境，测试环境的服务分别放到不同的 Namespace 中。
## Namespace 类别
Namespace 按创建类型分为两大类：集群默认创建的 Namespace 的和用户创建的 Namespace 。
### 集群默认创建的 Namespace 
Kubernetes 集群在启动时会默认创建 `default` 和 `kube-system` 这两个命名空间，这两个命令空间不可以删除。
 - 在不指定命名空间时，默认使用 `default namespace` 。
 - 系统服务一般建议创建在 `kube-system namespace` 。
 
### 用户创建的 Namespace
用户可以在集群中按照需要创建 Namespace 。可以按照不同的环境创建对应的 Namespace ，例如开发环境，联调环境和测试环境分别创建对应的 Namespace 。或者按照不同的应用创建对应的 Namespace ，例如应用 App1 和应用 App2 分别创建对应的 Namespace。
>**注意：**
>用户创建的 Namespace 可以进行删除，但删除 Namespace 操作会依次删除 Namespace 下的所有服务。

## Namespace 操作指引
### 创建 Namespace
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/ccs) 。
2. 单击左侧导航栏中的 **集群** 。
3. 在集群列表中单击集群的 **ID/名称**。
![](//mc.qcloudimg.com/static/img/61849c3dd8141879ca64e52a7348a065/image.png)
4. 单击 **Namespace 列表** ，单击**新建 Namespace **。
![](//mc.qcloudimg.com/static/img/605f218bba56eacb1f6d21ed507ea8eb/image.png)
5. 填写信息并单击**提交**。
 - **名称**：输入 Namespace 的名称。
 - **描述**：创建 Namespace 的相关信息。该信息将显示在 **Namespace 列表** 页面。
![](//mc.qcloudimg.com/static/img/2eff6302e4e127f7d4c01f1fa552f52a/image.png)

### 查看 Namespace 列表
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/ccs) 。
2. 单击左侧导航栏中的 **集群** 。
3. 在集群列表中单击集群的 **ID/名称**。
![](//mc.qcloudimg.com/static/img/61849c3dd8141879ca64e52a7348a065/image.png)
4. 单击要查看集群的 ** Namespace 列表**。
![](//mc.qcloudimg.com/static/img/198a4f5c8bb8680093e89a9491d5b389/image.png)

### 使用 Namespace
1. 创建服务时，选择对应的 Namespace。
![](//mc.qcloudimg.com/static/img/0c7959a293de17fe5ceb3c34f3be8597/image.png)

2. 查询服务时，选择对应的 Namespace ，查看对应 Namespace 下的所有服务。
![](//mc.qcloudimg.com/static/img/a2874127fc88b6deffe23710fe3b471b/image.png)

### 删除集群 Namespace
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/ccs) 。
2. 单击左侧导航栏中的 **集群** 。
3. 在集群列表中单击集群的 **ID/名称**。
![](//mc.qcloudimg.com/static/img/61849c3dd8141879ca64e52a7348a065/image.png)
4. 单击 **Namespace 列表** ，选择需删除的 Namespace，单击右侧**删除**。
![](//mc.qcloudimg.com/static/img/8c3af52aa236daf6c9768a095d421623/image.png)
5. 弹出提示页面，显示要删除的 Namespace 信息，单击**确定**删除。
![](//mc.qcloudimg.com/static/img/1d5fa45b089ce4c4120fe3050622f283/image.png)
>**注意：**
> 删除 Namespace 将销毁 Namespace下 的所有资源，销毁后所有数据将被清除且不可恢复，清除前将请提前备份数据。

## Namespace 使用实践
### 按照不同环境划分 Namespace
一般情况下，服务的发布过程中会经过开发环境、联调环境、测试环境到生产环境的过程。这个过程中不同环境部署的服务相同，只是在逻辑上进行了定义。分为两种做法：
1. 分别创建不同的集群。但这样在不同环境中资源不能进行共享。同时，不同环境中的服务互访也需要通过服务配置的 Load Balance(负载均衡) 才能够实现。
2. 对于不同环境创建对应的 Namespace。同一 Namespace 下可以通过服务名称 （service-name） 直接访问，跨 Namespace 可以通过 service-name.namespace-name 访问。
例如下图，开发环境、联调环境和测试环境分别创建 Namespace Dev、 Namespace Intergrated 和 Namespace Test。
![不同环境使用不同的namespace](https://mc.qcloudimg.com/static/img/045ec0b79b88de1e4891c55904bc73bb/image.png)

### 按照应用划分 Namespace
对于同一个环境中，服务数量比较多的情况，建议进一步按照应用划分 Namespace 。例如下图中，按照 App1 和 App2 划分了不同的 Namespace ，将不同应用的服务在逻辑上当做一个服务组进行管理。
![不同应用划分namespace](https://mc.qcloudimg.com/static/img/351a4eeeb0235692227093b6802aeaea/image.png)

同样的，在同一个应用（同一个 Namespace）内的服务通过服务名称 （service-name ） 直接访问，不同的应用（不同的 Namespace）通过 service-name.namespace-name 访问。
