## 操作场景

本文档指导您使用腾讯云容器服务构建一个简单的 Web 应用。

Web 应用分为以下两部分：
- 前端服务，用于处理客户端的查询和写入请求。
- 数据存储服务，使用 redis，将写入的数据存放到 redis-master。通过访问 redis-slave 进行读取操作，redis-master 和 redis-slave 通过主从复制来保持数据同步。
该应用是 kubernetes 项目自带的例子，链接地址为 <a href="https://github.com/kubernetes/kubernetes/tree/release-1.6/examples/guestbook">https://github.com/kubernetes/kubernetes/tree/release-1.6/examples/guestbook</a>。


## 操作步骤

### 创建容器集群

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke)。
2. 在左侧导航栏中，单击【[集群](https://console.cloud.tencent.com/tke/cluster?rid=1)】，进入集群管理页面。
3. 单击【[新建](https://console.cloud.tencent.com/tke/cluster/create?rid=1)】，进入 “创建集群” 页面。如下图所示：
![](https://main.qcloudimg.com/raw/26d6ea41c2d1300c67a24b9e9049dbcc.png)
4. 根据实际需求，填写以下参数。
 - 集群名称：自定义。
 - 新增资源所属项目：指定项目，集群内新增的云服务器、负载均衡器等资源将会自动分配到该项目下。
 - Kubernetes版本：指定 Kubernetes 版本。
 - 所在地域：指定集群的位置。
 - 集群网络：指定集群的节点网络，节点网络必须位于某个 VPC 内，如果您当前没有 VPC，请先 [创建一个 VPC](https://console.cloud.tencent.com/vpc)，并在该 VPC 下创建一个子网。
 - 容器网络：指定容器网络，集群内容器的 IP将从该网络分配。
5. 单击【下一步】。
6. 根据实际需求，为集群节点选择 Master 方式、计费模式，选择机型，配置机型、系统盘、公网带宽	
等。如下图所示：
![选择机型](https://main.qcloudimg.com/raw/ee04b24871660e87344df18ed223c6c7.png)
7. 单击【下一步】。
8. 根据实际需求，选择操作系统、安全组，并选择登录方式和设置密码等。如下图所示：
![云主机配置](https://main.qcloudimg.com/raw/8f58c57764ccf3898036f059d85a885f.png)
9. 单击【下一步】。
10. 确认信息，单击【完成】。稍等几分钟即可创建成功。

### 创建 Web 应用

#### 创建 redis-master 服务

1. 在左侧导航栏中，单击【[服务](https://console.cloud.tencent.com/tke/service)】，进入服务管理页面。
2. 单击【[新建](https://console.cloud.tencent.com/tke/service/create)】，进入 “新建服务” 页面。
3. 根据实际需求，填写以下参数。如下图所示：
![新建服务](https://main.qcloudimg.com/raw/4214e8141c8d0dad79f12c924db12d27.png)
 - 服务名称：命名为 redis-master。
 - 所在地域：选择集群所在地域。
 - 运行集群：选择新创建的集群。
 - 运行容器
    - 名称：命名为 master。
    - 镜像：指定 master 容器的镜像为 `ccr.ccs.tencentyun.com/library/redis`。
    - 镜像版本：latest。
    - CPU/内存限制：（可选）设置 CPU 和内存资源的上限。
 - 实例数量：选择 “手动调节”，设置为1个。
 - 服务访问方式：选择 “仅在集群内访问”。
 - 端口映射：选择 TCP 协议，并将服务端口和容器端口都设置为6379。其它服务可以通过服务名称 redis-master 以及端口6379访问到 master 容器。
4. 单击【创建服务】。

#### 创建 redis-slave 服务

1. 单击【[新建](https://console.cloud.tencent.com/tke/service/create)】，进入 “新建服务” 页面。
2. 根据实际需求，填写以下参数。如下图所示：
![新建服务](https://main.qcloudimg.com/raw/3050a6ea76a368745caa70bdcf8845f4.png)
 - 服务名称：命名为 redis-slave。
 - 所在地域：选择集群所在地域。
 - 运行集群：选择新创建的集群。
 - 运行容器
    - 名称：命名为 slave。
    - 镜像：指定 master 容器的镜像为 `ccr.ccs.tencentyun.com/library/gb-redisslave`。
    - 镜像版本：latest。
    - CPU/内存限制：（可选）设置 CPU 和内存资源的上限。
    - 环境变量：添加一个名称为：GET_HOSTS_FROM，值为：dns 的环境变量。
 - 实例数量：选择 “手动调节”，设置为1个。
 - 服务访问方式：选择 “仅在集群内访问”。
 - 端口映射：选择 TCP 协议，并将服务端口和容器端口都设置为6379。其它服务可以通过服务名称 redis-slave 以及端口6379访问到 slave 容器。
3. 单击【创建服务】。

#### 创建 frontend 服务

1. 单击【[新建](https://console.cloud.tencent.com/tke/service/create)】，进入 “新建服务” 页面。
2. 根据实际需求，填写以下参数。如下图所示：
![新建服务](https://main.qcloudimg.com/raw/f394092f104b00b91b3520846441152f.png)
 - 服务名称：命名为 frontend。
 - 所在地域：选择集群所在地域。
 - 运行集群：选择新创建的集群。
 - 运行容器
    - 名称：命名为 frontend。
    - 镜像：指定 master 容器的镜像为 `ccr.ccs.tencentyun.com/library/gb-frontend`。
    - 镜像版本：latest。
    - CPU/内存限制：（可选）设置 CPU 和内存资源的上限。
    - 环境变量：添加一个名称为：GET_HOSTS_FROM，值为：dns 的环境变量。
 - 实例数量：选择 “手动调节”，设置为1个。
 - 服务访问方式：选择 “提供公网访问”。
 - 端口映射：选择 TCP 协议，并将服务端口和容器端口都设置为80。用户通过浏览器访问负载均衡 IP 即可访问到 frontend 容器。
3. 单击【创建服务】。

#### 查看服务

在左侧导航栏中，单击【[服务](https://console.cloud.tencent.com/tke/service)】，即可查看新建的三个服务。如下图所示：
![](https://main.qcloudimg.com/raw/5e2bdd2ec19bc4224b93e71778ecbad2.png)
- 在创建 redis-master 和 redis-slave 服务时，因设置了 “仅在集群内访问” 的访问方式，这两个服务的 IP 地址只有一个内网 IP，且只能在集群内被其它服务访问。
- 在创建 frontend 服务时，因设置了 “提供公网访问” 的访问方式，该服务的 IP 地址有两个，分别为外网 IP（即公网负载均衡的 IP）和内网 IP，可以进行公网访问。由于 frontend 服务的访问端口为80，您可以在浏览器直接输入该外网 IP 即可访问页面。
返回如下图所示页面，即表示可以正常访问 frontend 服务。
![](https://mc.qcloudimg.com/static/img/1d2bee6cf0a05db0e12d409cc83995b7/image.png)
在输入框中输入任意的字符串，即可发现输入的记录已被保存，并且展示在页面下方。关闭并重新打开浏览器，重新访问该外网 IP 地址，原输入的数据依然存在，即表示输入的字符串已经保存到 redis 中。

### 开发实践

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
该实例是 Guestbook App 的 frontend 服务的完整代码。frontend 服务收到一个 HTTP 请求后，判断是否是 set 命令。
- 如果是 set 命令，则取出参数中的 key，value，连接到 redis-master 服务，并将 key, value 设置到 redis-master 中。
- 如果不是 set 命令，则连接到 redis-slave 服务，获取参数 key 对应的 value 值，并返回到客户端进行展示。

**通过示例的 Web App，需要注意以下两点**：
1. frontend 访问 redis-master 和 redis-slave 服务时，连接**服务名和端口**，集群自带 dns 服务将服务名解析成对应的服务 IP，并根据服务 IP 进行负载均衡。例如，redis-slave 服务有三个实例，在访问 redis-slave 服务时，直接连接 redis-slave 和6379，dns 会自动将 redis-slave 解析成 redis-slave 的服务 IP（即一个浮动 IP，类似于负载均衡的 IP），并根据 redis-slave 的服务 IP 自动进行负载均衡，将请求发往某个 redis-slave 服务的实例中。
2. 您可以为容器设置环境变量。在本例中，frontend 容器运行时，会读取 GET_HOSTS_FROM 环境变量，如果环境变量的值为 dns，则直接通过服务名来连接（推荐做法），否则需通过另一个环境变量来获取 redis-master 或者 redis-slave 的域名。
