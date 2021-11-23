## 操作场景

本文档指导您将现有 Dubbo 应用迁移至 TSF 平台，并采用虚拟机 Mesh 的部署方式，通过 Service Mesh 的方式实现 Dubbo 应用透明的服务注册发现和无侵入的服务治理，享受 TSF 平台一站式的微服务框架解决方案。

下文以 Dubbo Mesh Demo 为例介绍具体的迁移方式和操作步骤。Dubbo Mesh Demo 提供了 client、greet 和 hello 3个应用，3个应用之间的调用关系是：client -> greet -> hello，client 应用每隔5秒会自动发起请求。

## 迁移价值

- TSF 为您提供**一站式应用生命周期管理服务**。提供从应用部署到应用运行的全流程管理，包括创建、删除、部署、回滚、扩容、下线、启动和停止应用并支持版本回溯能力。
- TSF 为您提供**高效的服务注册发现能力**。支持秒级的服务注册发现并提供本地注册信息缓存、服务实例注册发现异常告警、注册中心跨 AZ 区容灾等完善的高可用保障机制。
- TSF 为您提供**细粒度服务治理能力**。支持服务和 API 多级服务治理能力，通过配置标签形式进行细粒度的流量控制，实现灰度发布、就近路由、熔断限流、服务容错、访问鉴权等功能。
- TSF 为您提供**立体化应用数据运营**。提供完善应用性能指标监控和分布式调用链分析、服务依赖拓扑、日志服务工具，帮助您高效分析应用性能瓶颈及故障问题排查。

## 前提条件

- 已经下载 [Dubbo Mesh Demo](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/mesh-demo/tsf-mesh-dubbo-demo.tar.gz) 的代码程序包。
- 已经创建了集群和命名空间，集群中导入3个云服务器。
- 已经创建了 client、greet 和 hello 应用（虚拟机部署方式）。

## 操作步骤

### 步骤1：修改配置通过直连服务名方式访问服务提供者

配置直连服务提供者的方式，详情请参考 Dubbo 官方文档 [直连提供者](http://dubbo.apache.org/zh/docs/v2.7/user/examples/explicit-target/)。

在 Dubbo Mesh Demo 中，greet 服务需要访问 hello 服务，采用 XML 配置方式，可以配置为：

```xml
<dubbo:reference id="helloService" check="false" interface="org.apache.dubbo.samples.api.HelloService" url="dubbo://org.apache.dubbo.samples.api.HelloService:20880">
```

此处的直连地址为 `dubbo://org.apache.dubbo.samples.api.HelloService:20880`，`org.apache.dubbo.samples.api.HelloService` 为步骤2中 hello 服务注册的服务名。

### 步骤2：按照 TSF Mesh 方式构建程序包

要将 Dubbo 应用以 Mesh 的方式部署到 TSF 平台上，需要遵循 Mesh 的方式构建程序包，主要包含以下几个文件：

#### 1. 编译好的 Dubbo 应用 jar 包

建议使用 FATJAR 包，可直接运行，如 Demo 中 greet 服务的 jar 包为 `dubbo-samples-greetservice-1.0.jar`。

#### 2. spec.yaml 文件

此 yaml 文件用于描述 Dubbo 应用的服务注册信息，至少需要配置服务名、服务监听端口并指定 Dubbo 协议，如下所示：

```yaml
apiVersion: v1
kind: Application
spec:
  services:
    - name: org.apache.dubbo.samples.api.GreetingService
      ports:
        - targetPort: 20881
          protocol: dubbo
      healthCheck:
        path:
```

> !此处的服务名如上面的 `org.apache.dubbo.samples.api.GreetingService` 将被注册到注册中心，其它 Dubbo 应用将通过该服务名进行调用，同时，服务名需要跟该 Dubbo 应用提供的 interface 名保持一致。

#### 3. start.sh 启动脚本

此 shell 脚本用于启动部署的 Dubbo 应用，编写时保证下面两点即可：

- 幂等执行，已经启动的 Dubbo 应用不会因再次执行该脚本而被停止
- 后台执行，将日志输出到本地文件

编写完后可手工执行验证是否启动成功。

以下是 Demo 中 greet 服务的启动脚本：

```bash
#!/bin/bash

already_run=`ps -ef|grep "dubbo-samples-greetservice-1.0.jar"|grep -v grep|wc -l`
if [ ${already_run} -ne 0 ];then
        echo "dubbo-greet already Running!!!! Stop it first"
        exit -1
fi
nohup java -jar dubbo-samples-greetservice-1.0.jar 1>stdout.log 2>&1 &
```

#### 4. stop.sh 停止脚本

此 shell 脚本用于停止部署的 Dubbo 应用，编写完后可手工执行验证是否停止成功，以下是Demo中 greet 服务的停止脚本：

```bash
#!/bin/bash

pid=`ps -ef|grep "dubbo-samples-greetservice-1.0.jar"|grep -v grep|awk '{print $2}'`
kill -SIGTERM $pid
echo "process ${pid} killed"
```

#### 5. cmdline 进程执行命令文件

TSF 平台部署在主机上的 tsf-agent 会通过检查系统运行进程中是否有 cmdline 文件中的执行命令，来验证 Dubbo 应用进程是否存活，一般设置为进程的启动命令即可，如 Demo 中  greet 服务的 cmdline：

```
java -jar dubbo-samples-greetservice-1.0.jar
```

> !这里不需要包括上面启动脚本中的 `nohup` 和 `1>stdout.log 2>&1 &`。

### 步骤3：部署 Dubbo 应用到 TSF 平台

1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf)。
2. 在左侧导航栏中，单击**[应用管理](https://console.cloud.tencent.com/tsf/app)**，进入应用列表页，选择已创建的 Dubbo 应用，进入应用详情页。
3. 单击顶部**程序包管理**，上传步骤2中构建好的程序包。
4. 单击顶部**部署组**，在部署组列表页面创建部署组，选择集群和命名空间，添加实例，选择相应版本的程序包，完成部署，具体操作方式参考 [虚拟机应用部署组](https://cloud.tencent.com/document/product/649/15524)。
5. 部署完成后，在应用的**部署组**页查看对应部署组的状态，如果是 `运行中` 表示部署成功。
6. 在左侧导航栏中，单击 **[服务治理](https://console.cloud.tencent.com/tsf/service)**，进入服务列表页，如果可以看到步骤2中 spec.yaml 文件指定的服务名且是 `在线` 状态, 表示该 Dubbo 服务注册成功，其它 Dubbo 服务可通过此服务名进行调用。

### 步骤4：配置服务治理规则

#### Dubbo 服务路由

1. 在左侧导航栏中，单击* *[服务治理](https://console.cloud.tencent.com/tsf/service)**，进入服务列表页，单击需要设置路由的目的 Dubbo 服务名，进入服务详情页。
2. 单击顶部**服务路由**， 新建路由规则，具体操作方式参考 [服务路由使用方法](https://cloud.tencent.com/document/product/649/18861)，如下图所示：
   ![](https://main.qcloudimg.com/raw/c32c8ff898e62d862a30cfae27af81b2.png)

#### Dubbo 服务监控

1. 在左侧导航栏中，单击 **[服务治理](https://console.cloud.tencent.com/tsf/service)**，进入服务列表页，单击需要监控的Dubbo服务名，进入服务详情页。
2. 单击顶部**服务概览**， 可查看该服务依赖拓扑、请求概览等信息，如下图所示：
   ![](https://main.qcloudimg.com/raw/d8657746ea3ded1c4df324da8d86f801.png)

#### Dubbo 调用链追踪

1. 在左侧导航栏中，单击 **[服务依赖拓扑](https://console.cloud.tencent.com/tsf/topology)**，进入服务依赖拓扑页面。
2. 在顶部选择对应 Dubbo 服务所在的命名空间，再选择对应时间段，页面将自动显示该命名空间下所有服务的调用关系图，如下图所示：
   ![](https://main.qcloudimg.com/raw/6897adbe426b1d6a597ebe5e26156d93.png)
