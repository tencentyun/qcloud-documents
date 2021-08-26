## 操作场景

本文档指导您使用腾讯云容器服务构建一个简单的 Web 应用。

Web 应用分为以下两部分：
- 前端服务，用于处理客户端的查询和写入请求。
- 数据存储服务，使用 redis。将写入的数据存放到 redis-master，访问 redis-slave 进行读取操作。redis-master 和 redis-slave 通过主从复制来保持数据同步。

该应用是 kubernetes 项目自带的示例，详情请参见 <a href="https://github.com/kubernetes/kubernetes/tree/release-1.6/examples/guestbook">Guestbook App</a>。

## 前提条件
- 已 [注册腾讯云账户](https://cloud.tencent.com/register)。
- 已创建集群。如未创建，请参见 [创建集群](https://cloud.tencent.com/document/product/457/32189)。

## 操作步骤
### 创建 redis-master 服务
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 单击需要创建应用的集群 ID，进入工作负载 Deployment 详情页，选择**新建**。如下图所示：
![](https://main.qcloudimg.com/raw/43b6b4dde7a18b9721c1f1ccd57b1cf2.png)
3. 在“新建Workload”页面，根据以下提示，设置工作负载基本信息。如下图所示：
![](https://main.qcloudimg.com/raw/24f730c631c381ffcf5fca4fe1d2e691.png)
 - **工作负载名**：要创建的工作负载的名称，本文以 redis-master 为例。
 - **描述**：填写工作负载的相关信息。
 - **标签**：key = value 键值对，本例中标签默认值为 k8s-app = **redis-master**。
 - **命名空间**：根据实际需求进行选择。
 - **类型**：根据实际需求进行选择。
 - **数据卷**：根据实需求设置工作负载的挂载卷，详情请参见 [Volume 管理](https://cloud.tencent.com/document/product/457/31713)。
4. 根据以下提示，设置**实例内容器**。如下图所示：
![](https://main.qcloudimg.com/raw/a4a3c9725ff0004efa08202228c0bd89.png)
主要参数信息如下，其余选项保持默认设置：
 - **名称**：输入实例内容器名称，本文以 master 为例。
 - **镜像**：输入 `ccr.ccs.tencentyun.com/library/redis`。
 - **镜像版本（Tag）**：输入 latest。
 - **镜像拉取策略**：提供以下3种策略，请按需选择，本文以不进行设置使用默认策略为例。
若不设置镜像拉取策略，当镜像版本为空或 latest 时，使用 Always 策略，否则使用 IfNotPresent 策略。
    - **Always**：总是从远程拉取该镜像。
    - **IfNotPresent**：默认使用本地镜像，若本地无该镜像则远程拉取该镜像。
    - **Never**：只使用本地镜像，若本地没有该镜像将报异常。
6. 设置实例数量，如下图所示：
![](https://main.qcloudimg.com/raw/ef60609106114af8ec7ddf4a3d25480d.png)
 - **手动调节**：设定实例数量，本文实例数量设置为1。可单击“+”或“-”控制实例数量。
 - **自动调节**：满足任一设定条件，则自动调节实例（pod）数目。详情请参见 [服务自动扩缩容](https://cloud.tencent.com/document/product/457/14209)。
7. 根据以下提示，进行工作负载的访问设置。如下图所示：   
![](https://main.qcloudimg.com/raw/e94209f0c1cc66961e1bd1a165e1e8ef.png)
 - **Service**：勾选“启用”。
 - **服务访问方式**：选择“仅在集群内访问”。
 - **负载均衡器**：根据实际需求进行选择。
 - **端口映射**：选择 TCP 协议，并将服务端口和容器端口都设置为6379。 其它服务可以通过服务名称 redis-master 以及端口6379访问到 master 容器。
8. 单击**创建Workload**，完成 redis-master 服务的创建。

### 创建 redis-slave 服务
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 单击需要创建服务的集群 ID，进入工作负载 Deployment 详情页，选择**新建**。如下图所示：
![](https://main.qcloudimg.com/raw/e7e626eab53919b49fa7afbf0f79dd85.png)
3. 在“新建Workload”页面，根据以下提示，设置工作负载基本信息。如下图所示：
![](https://main.qcloudimg.com/raw/0841b89642e2d94f7939c583241f0a60.png)
 - **工作负载名**：要创建的工作负载的名称，本文以 redis-slave 为例。
 - **描述**：填写工作负载的相关信息。
 - **标签**：key = value 键值对，本例中标签默认值为 k8s-app = **redis-slave**。
 - **命名空间**：根据实际需求进行选择。
 - **类型**：根据实际需求进行选择。
 - **数据卷**：根据实需求设置工作负载的挂载卷，详情请参见 [Volume 管理](https://cloud.tencent.com/document/product/457/31713)。
4. 根据以下提示，设置**实例内容器**。如下图所示：
![](https://main.qcloudimg.com/raw/49aefd663923bbd4fed3af1bdbbf04d9.png)
主要参数信息如下，其余选项保持默认设置：
 - **名称**：输入实例内容器名称，本文以 slave 为例。
 - **镜像**：输入 `ccr.ccs.tencentyun.com/library/gb-redisslave`。
 - **镜像版本（Tag）**：输入 latest。
 - **镜像拉取策略**：请按需选择，本文以不进行设置使用默认策略为例。
 - **环境变量**：输入以下配置信息：
GET_HOSTS_FROM = dns
5. 设置实例数量。如下图所示：
![](https://main.qcloudimg.com/raw/42df721d539fccb0e23e5b61d6b429ab.png)
 - **手动调节**：设定实例数量，本文实例数量设置为1。可单击“+”或“-”控制实例数量。
 - **自动调节**：满足任一设定条件，则自动调节实例（pod）数目。详情请参见 [服务自动扩缩容](https://cloud.tencent.com/document/product/457/14209)。
6. 根据以下提示，进行工作负载的访问设置。如下图所示：   
![](https://main.qcloudimg.com/raw/a8db4feb02f1423182d5a69044708365.png)
 - **Service**：勾选“启用”。
 - **服务访问方式**：选择“仅在集群内访问”。
 - **负载均衡器**：根据实际需求进行选择。
 - **端口映射**：选择 TCP 协议，并将服务端口和容器端口都设置为6379。 其它服务可以通过服务名称 redis-master 以及端口6379访问到 master 容器。
7. 单击**创建Workload**，完成 redis-slave 服务的创建。

### 创建 frontend 服务
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 单击需要创建应用的集群 ID，进入工作负载 Deployment 详情页，选择**新建**。如下图所示：
![](https://main.qcloudimg.com/raw/eb39a8ddb8768270901d0f821e5b915d.png)
3. 在“新建 Workload”页面，根据以下提示，设置工作负载基本信息。如下图所示：
![](https://main.qcloudimg.com/raw/b4621c3a833517e41f641fddc402fade.png)
 - **工作负载名**：要创建的工作负载的名称，本文以 frontend 为例。
 - **描述**：填写工作负载的相关信息。
 - **标签**：key = value 键值对，本例中标签默认值为 k8s-app = **frontend**。
 - **命名空间**：根据实际需求进行选择。
 - **类型**：根据实际需求进行选择。
 - **数据卷**：根据实需求设置工作负载的挂载卷，详情请参见 [Volume 管理](https://cloud.tencent.com/document/product/457/31713)。
5. 根据以下提示，设置**实例内容器**，如下图所示：
![](https://main.qcloudimg.com/raw/f33bc92285e4c537022ee81d189c9aa7.png)
主要参数信息如下，其余选项保持默认设置：
 - **名称**：输入实例内容器名称，本文以 frontend 为例。
 - **镜像**：输入 `ccr.ccs.tencentyun.com/library/gb-frontend`。
 - **镜像版本（Tag）**：输入 latest。
 - **镜像拉取策略**：请按需选择，本文以不进行设置使用默认策略为例。
 - **环境变量**：输入以下配置信息：
GET_HOSTS_FROM = dns
6. 设置实例数量，如下图所示：
![](https://main.qcloudimg.com/raw/f9aa502568533e4b9fc01ba3395e7e9c.png)
 - **手动调节**：设定实例数量，本文实例数量设置为1。可单击“+”或“-”控制实例数量。
 - **自动调节**：满足任一设定条件，则自动调节实例（pod）数目。详情请参见 [服务自动扩缩容](https://cloud.tencent.com/document/product/457/14209)。
7. 根据以下提示，进行工作负载的访问设置。如下图所示：   
![](https://main.qcloudimg.com/raw/d371c33adde156247329a531c95a7f19.png)
 - **Service**：勾选“启用”。
 - **服务访问方式**：选择“提供公网访问”。
 - **负载均衡器**：根据实际需求进行选择。
 - **端口映射**：选择 TCP 协议，并将服务端口和容器端口都设置为80。用户通过浏览器访问负载均衡 IP 即可访问到 frontend 容器。
8. 单击**创建Workload**，完成 frontend 服务的创建。


### 验证 Web 应用
1. 单击左侧导航栏中 **[集群](https://console.cloud.tencent.com/tke2/cluster)**，进入“集群管理”页面。
2. 单击已创建服务所在的集群 ID，选择**服务** > **Service**。如下图所示：
3. 进入服务管理页面，复制 frontend 服务的负载均衡 IP。如下图所示：
![](https://main.qcloudimg.com/raw/70f977306648e811b82c124492657ce1.png)
>?
>- 在创建 redis-master 和 redis-slave 服务时，因设置了**仅在集群内访问**的访问方式，服务只具备一个内网 IP，且只能在集群内被其它服务访问。
>- 在创建 frontend 服务时，因设置了**提供公网访问**的访问方式，服务具备负载均衡  IP（即公网 IP）和内网 IP，可在集群内被其它服务访问，也可通过公网访问。
>
4. 使用浏览器访问 frontend 服务的负载均衡 IP，返回如下图所示页面，即表示可以正常访问 frontend 服务。
![](https://main.qcloudimg.com/raw/d168ffa008a9c91e8b0e0c2051abd5a3.png)
5. 在输入框中输入任意的字符串后单击**Submit**，发现输入的记录已被保存，并且展示在页面下方。
刷新浏览器页面，重新访问该服务 IP 地址。原输入的数据依然存在，即表示输入的字符串已经保存到 redis 中。

### 开发实践
以下示例代码是 Guestbook App 的 frontend 服务的完整代码，当 frontend 服务收到一个 HTTP 请求后，会进行判断是否为 set 命令：
- 如果是 set 命令，则取出参数中的 key 和 value，连接到 redis-master 服务。并将 key 和 value 设置到 redis-master 中。
- 如果不是 set 命令，则连接到 redis-slave 服务，获取参数 key 对应的 value 值，并返回到客户端进行展示。

```php
<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
require 'Predis/Autoloader.php';
Predis\Autoloader::register();
if (isset($_GET['cmd']) === true) {
  $host = 'redis-master';
  if (getenv('GET_HOSTS_FROM') == 'env') {
    $host = getenv('REDIS_MASTER_SERVICE_HOST');
  }
  header('Content-Type: application/json');
  if ($_GET['cmd'] == 'set') {
    $client = new Predis\Client([
      'scheme' => 'tcp',
      'host'   => $host,
      'port'   => 6379,
    ]);
    $client->set($_GET['key'], $_GET['value']);
    print('{"message": "Updated"}');
  } else {
    $host = 'redis-slave';
    if (getenv('GET_HOSTS_FROM') == 'env') {
      $host = getenv('REDIS_SLAVE_SERVICE_HOST');
    }
    $client = new Predis\Client([
      'scheme' => 'tcp',
      'host'   => $host,
      'port'   => 6379,
    ]);
    $value = $client->get($_GET['key']);
    print('{"data": "' . $value . '"}');
  }
} else {
  phpinfo();
} ?>

```


### 说明事项

- 当 frontend 服务访问 redis-master 和 redis-slave 服务时，连接**服务名和端口**。集群自带 dns 服务将服务名解析成对应的服务 IP，并根据服务 IP 进行负载均衡。
例如，redis-slave 服务有三个实例。在访问 redis-slave 服务时，直接连接 redis-slave 和6379，dns 会自动将 redis-slave 解析成 redis-slave 的服务 IP（即一个浮动 IP，类似于负载均衡的 IP），并根据 redis-slave 的服务 IP 自动进行负载均衡，将请求发往某个 redis-slave 服务的实例中。
- 容器环境变量设置：
 - **使用默认设置（推荐设置）**：frontend 容器运行时，会读取已设置的 GET_HOSTS_FROM 环境变量值 dns，则直接通过服务名来连接。
 - **其他设置**：需通过另一个环境变量来获取 redis-master 或者 redis-slave 的域名。

