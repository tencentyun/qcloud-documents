## 使用腾讯云容器服务构建web应用


本文将介绍在腾讯云容器服务里，如何构建一个最简单的web应用

### 该web应用分为两部分：

1、前端服务，用于处理客户端的查询和写入请求。
2、数据存储服务，使用redis，写入的数据存放到redis-master，读取操作访问的是redis-slave，redis-master和redis-slave通过主从复制来保持数据同步。
该应用是kubernetes项目自带的例子，链接地址为 https://github.com/kubernetes/kubernetes/tree/release-1.6/examples/guestbook 。

### 一、创建容器集群

1、进入创建集群页面，创建[容器集群](https://console.cloud.tencent.com/ccs/cluster)：
2、填写集群名、指定集群的位置(广州、上海、北京等)。
3、指定集群的节点网络，节点网络必须位于某个VPC内，如果您当前没有vpc，请先[创建一个vpc](https://console.cloud.tencent.com/vpc)，并在该vpc下创建一个子网。
4、指定容器网络。
5、为集群节点选择机型(cpu和内存)。
6、为集群节点选择磁盘、带宽等配置，并设置密码和安全组。
7、选择集群节点的数目。
8、稍等几分钟后，集群创建成功。
![](https://mc.qcloudimg.com/static/img/bb4d18120964f61680f504f295418db1/image.png)
![](https://mc.qcloudimg.com/static/img/f5b0e1faaa7458ea145df50e2d387c3f/image.png)
![](https://mc.qcloudimg.com/static/img/503003ab0d98eb9acf0109ee5b10a00e/image.png)

### 二、创建web应用

#### 1、创建redis-master服务

1. 指定服务名称redis-master。
2. 选择集群为我们刚刚创建的集群my-first-cluster。
3. 设置服务的实例信息(实例可以包含多个容器)：
  - 添加一个容器，命名为master。
  - 为master容器指定镜像为ccr.ccs.tencentyun.com/library/redis，版本为latest 。
4. 设置服务运行的实例数，redis-master服务需要运行1个实例，我们选择1。
5. 选择服务的访问方式，因为我们的redis服务是内部服务，只提供给集群内其它服务访问，所以我们选择仅在集群内访问。
6. 最后设置服务的访问端口，我们的服务实例包含1个redis容器，该容器监听了6379端口，所以我们配置端口映射的容器端口为6379，服务端口跟容器端口一样，也设置成6379，这样其它服务可以通过服务名称 redis-master以及端口6379就可以访问到我们的master容器了。

![](https://mc.qcloudimg.com/static/img/0205c172fdcc02921087024c0dfda6fa/image.png)


#### 2、创建redis-slave服务

1. 指定服务名称redis-slave。
2. 选择集群为我们刚刚创建的集群my-first-cluster。
3. 设置服务的实例信息：
  - 添加一个容器，命名为slave。
  - 为slave容器指定镜像为ccr.ccs.tencentyun.com/library/gb-redisslave，版本为latest 。
  - 为容器指定cpu，内存资源的上限(可选)，上面的master容器同样可以指定cpu、内存限制。
  - 运行命令和启动参数我们使用镜像里面默认的命令和参数即可，可以不填。
  - 添加一个环境变量 环境变量名称为：GET_HOSTS_FROM，值为:dns （由于gb-redisslave镜像里的程序需要，这里必填）。
4. 设置服务运行的实例数，redis-slave服务需要运行1个实例，我们选择1。
5. 选择服务的访问方式，因为我们的redis slave服务是内部服务，只提供给集群内其它服务访问，所以我们选择仅在集群内访问。
6. 最后设置服务的访问端口，我们的服务实例包含1个redis slave容器，该容器监听了6379端口，所以我们配置端口映射的容器端口为6379，服务端口跟容器端口一样，也设置成6379，这样其它服务可以通过服务名称 redis-slave以及端口6379就可以访问到我们的slave容器了。

![](https://mc.qcloudimg.com/static/img/c289316bdb27dbf837cd3cba9de3b9da/image.png)


#### 3、创建frontend服务

1. 指定服务名称frontend。
2. 选择集群为我们刚刚创建的集群my-first-cluster。
3. 设置服务的实例信息：
  - 添加一个容器，命名为frontend。
  - 为slave容器指定镜像为ccr.ccs.tencentyun.com/library/gb-frontend，版本为latest 。
  - 添加一个环境变量 环境变量名称为：GET_HOSTS_FROM，值为:dns （由于gb-frontend镜像里的程序需要，这里必填）。
4. 设置服务运行的实例数，frontend服务需要运行1个实例，我们选择1。
5. 选择服务的访问方式，因为我们的frontend需要提供外网浏览器访问，我们选择公网负载均衡访问方式。
6. 最后设置服务的访问端口，我们的服务实例包含1个frontend容器，该容器监听了80端口，所以我们配置端口映射的容器端口为80，服务端口跟容器端口一样，也设置成80，这样，用户通过浏览器访问我们的负载均衡ip就可以访问到我们的frontend容器了。

![](https://mc.qcloudimg.com/static/img/fc06f28b107cae9aed975fddc71bf270/image.png)

#### 4、查看服务

点击左侧栏的服务，即可看到我们刚刚创建的三个服务，其中frontend服务可以公网访问，因为我们指定了公网负载均衡访问方式，而redismaster和redisslave服务只能够在集群内被其它服务访问，因为我们设置了访问方式为集群内访问。
![](https://mc.qcloudimg.com/static/img/f6f97b051b982a79f48972151c2cb9e8/image.png)
我们注意到，frontend服务的属性里面的ip地址有两个： 一个外网ip 211.159.213.194和一个内网ip 10.20.255.125，而redisslave和redismaster服务分别只有一个内网ip，那是因为frontend服务的访问方式为公网负载均衡方式访问，所以我们为该服务分配了一个公网负载均衡，该外网ip就是公网负载均衡的ip，由于frontend服务的访问端口为80，所以我们可以在浏览器直接输入该外网ip 211.159.213.194，可以看到：
![](https://mc.qcloudimg.com/static/img/1d2bee6cf0a05db0e12d409cc83995b7/image.png)
说明我们可以正常访问frontend服务了，现在就试下在输入框中输入任意的字符串吧，输入后可以看到，我们输入的记录被保存起来，并且展示在页面下方，我们可以开启另外一个浏览页，重新打开这个负载均衡的ip地址，看到之前输入的数据都在，说明我们输入的字符串确实已经保存到了redis。

### 三、开发实践

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
这是guestbook app的frontend服务的完整代码，很简短。frontend服务收到一个http请求后，判断是否是set命令，如果是set命令，就取出参数中的key，value，并连接到redis-master服务，将key, value设置到redis master中。如果是不是set命令，就连接到redis-slave服务，从redis slave中获取参数key对应的value，并吐给客户端来展示。
**通过示例的web app，有两点需要注意**：
1、frontend访问redis-master和redis-slave服务时，连接的是**服务名和端口**，我们的集群自带dns服务，会把服务名解析成对应的服务ip，并根据服务ip来做负载均衡，比如redis-slave服务有三个实例，那么我们访问redis-slave服务时，直接连接redis-slave和6379，dns会自动把redis-slave解析成redis-slave的服务ip(实际上是一个浮动ip，类似于负载均衡的ip)，并根据redis-slave的服务ip，会自动做负载均衡，把请求发往某个redis-slave服务的实例中。
2、我们可以为容器设置环境变量。在本例中，frontend容器运行时，会读取GET_HOSTS_FROM环境变量，如果环境变量的值为dns，那么就直接通过服务名来连接(推荐做法)，否则再通过另一个环境变量来获取redis-master或者redis-slave的域名。
