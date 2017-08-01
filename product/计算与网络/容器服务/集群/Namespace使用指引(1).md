命名空间(Namespace)是对一组资源和对象的抽象集合。例如可以将开发环境，联调环境，测试环境的服务分别放到不同的namespace中。

## Namespace类别

### 集群默认创建的Namespace 
Kubernetes 集群在启动时会默认创建 `default` 和 `kube-system` 这两个命名空间，这两个命令空间不可以删除。

 - 在不指定命名空间时，默认使用 `default namespace`
 - 系统服务一般建议创建在 `kube-system namespace`
 
### 用户创建的Namespace
用户可以在集群中按照需要创建 namespace 。可以按照不同的环境创建对应的 namespace ，例如开发环境，联调环境和测试环境分别创建对应的 namespace 。或者按照不同的应用创建对应的 namespace ，例如应用 APP1 和应用 APP2 分别创建对应的 namespace。

>**注意**：用户创建的 namespace 可以进行删除，但删除 namespace 操作会依次删除 namespace 下的所有服务。

## Namespace 操作指引

### 创建Namespace

1. 在集群列表中单击集群的 **ID/名称**。
2. 点击 **Namespace列表** ，单击【新建Namespace】。
 ![Alt text](https://mc.qcloudimg.com/static/img/56c29533e95348e62e1129ebf1c310d0/r.png)
3. 填写信息并点击【提交】。
 - **名称**：输入 Namespace 的名称。
 - **描述**：创建 Namespace 的相关信息。该信息将显示在 **Namespace列表** 页面。
![](https://mc.qcloudimg.com/static/img/4abaa7a0be188a3832c6878d1a86c043/t.png)

### 查看Namespace列表
1. 在集群列表中单击集群的 **ID/名称**。
2. 单击要查看集群的 **Namespace列表**。
![](https://mc.qcloudimg.com/static/img/159bed0588cd1f637dacdda982f98d99/r.png)

### 使用Namespace
1. 创建服务时，选择对应的 Namespace。
![](https://mc.qcloudimg.com/static/img/fea0440bb18409eab93de60f3710e76c/q.png)

2. 查询服务时，选择对应的 Namespace ，查看对应 Namespace 下的所有服务。
![](https://mc.qcloudimg.com/static/img/2fb68ed8a2920a250507ae8da8bce4b1/w.png)

### 删除集群Namespace

1. 在集群列表页中选择某集群的 **ID/名称**。
2. 点击 **Namespace列表** ，选择需删除的 Namespace，单击右侧【删除】。
![](https://mc.qcloudimg.com/static/img/0517d764ef15dfabd53443438f6421b1/a.png)
3. 单击【确定】。
![](https://mc.qcloudimg.com/static/img/cbba287cfc54d6390d7a02406d0ec661/s.png)
>**注意**： 删除 Namespace 将销毁 Namespace下 的所有资源，销毁后所有数据将被清除且不可恢复，清除前将请提前备份数据。

## Namespace使用实践
### 按照不同环境划分Namespace

一般情况下，服务的发布过程中会经过开发环境、联调环境、测试环境到生产环境的过程。这个过程中不同环境部署的服务相同，只是在逻辑上进行了定义。分为两种做法：
1. 分别创建不同的集群。但这样在不同环境中资源不能进行共享。同时，不同环境中的服务互访也需要通过服务配置的 LB 才能够实现。
2. 对于不同环境创建对应的 Namespace 。同一 Namespace 下可以通过服务名称 (service-name) 直接访问，跨 Namespace 可以通过 service-name.namespace-name 访问。具体的方案如下图所示：

![不同环境使用不同的namespace](https://mc.qcloudimg.com/static/img/045ec0b79b88de1e4891c55904bc73bb/image.png)

如上图所示，开发环境，联调环境和测试环境分别创建 Namespace Dev ，Namespace Intergrated 和 Namespace Test 。

### 按照应用划分Namespace

对于同一个环境中，服务数量比较多的情况，建议可以进一步按照应用划分 Namespace 。例如下图中，按照 APP1 和 APP2 划分了不同的Namespace，这样将不同应用的服务在逻辑上当做一个服务组进行管理。
![不同应用划分namespace](https://mc.qcloudimg.com/static/img/351a4eeeb0235692227093b6802aeaea/image.png)

同样的，在同一个应用(同一个Namespace)内的服务通过服务名称(service-name)直接访问，不同的应用(不同的Namespace)通过service-name.namespace-name访问。
