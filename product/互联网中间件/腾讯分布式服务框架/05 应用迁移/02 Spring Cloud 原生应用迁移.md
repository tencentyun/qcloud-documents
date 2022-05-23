## 迁移价值

Spring Cloud 提供了微服务系统架构的一站式解决方案，并利用 Spring Boot 的开发便利性巧妙地简化了分布式系统基础设施的开发，如服务发现注册、配置中心、消息总线、负载均衡、断路器、数据监控、分布式调用链等，通过 Spring Cloud 提供的一套简易的编程模型，我们可以在 Spring Boot 的基础上轻松地实现微服务项目的构建。

然而，这仅仅是帮助开发者开发微服务应用带来了便利，最终开发出的应用需要在生产环境运行起来，因此，我们还需要：

1. **稳定的运行环境**，如虚机环境或者容器环境，并能对微服务应用进行生命周期管理
2. **高可用的注册中心**，Spring Cloud虽然支持使用 Eureka、 Zookeeper或 Consul实现服务注册发现，但需要我们自行搭建并保证其高可用
3. **统一的控制平面对服务进行治理**，Spring Cloud整合了大量的服务治理组件，但没有一个统一的控制平面进行管理，这对大规模的微服务治理带来了不少的压力
4. **可视化的数据运营服务**，如日志服务、监控服务、分布式调用链服务，如Spring Cloud通过引入Sleuth实现分布式调用链，并和Zipkin、HTrace、ELK兼容，但这些后端服务需要我们自行搭建并保证其稳定性

也就是说，我们开发者开发完应用、构建好Jar包也只是第一步，要让应用稳定运行和持续运营，还需要一个微服务平台来满足上面的要求，这正是TSF——腾讯微服务平台 （Tencent Service Framework）的价值所在：

1. TSF 提供了**一站式应用生命周期管理服务**。提供从应用部署到应用运行的全流程管理，包括创建、删除、部署、回滚、扩容、下线、启动和停止应用并支持版本回溯能力。
2. TSF 提供了**高效的服务注册发现能力**。支持秒级的服务注册发现并提供本地注册信息缓存、服务实例注册发现异常告警、注册中心跨 AZ 区容灾等完善的高可用保障机制。
3. TSF 提供了**细粒度服务治理能力**。支持服务和 API 多级服务治理能力，通过配置标签形式进行细粒度的流量控制，实现灰度发布、就近路由、熔断限流、服务容错、访问鉴权等功能。
4. TSF 提供了**立体化应用数据运营**。提供完善应用性能指标监控和分布式调用链分析、服务依赖拓扑、日志服务工具，帮助您高效分析应用性能瓶颈及故障问题排查。

**目前TSF 支持原生 Spring Cloud 应用无侵入接入，无需改造即可直接接入 TSF，享受服务注册与发现、服务治理、应用监控和调用链跟踪等功能。**



## 操作步骤

本文档以一个 [开源商城系统](https://github.com/macrozheng/mall-swarm) 为示例，为您介绍将原生 Spring Cloud 应用迁移到 TSF 的方法。

该系统由以下几部分组成：

| 模块         | 说明                                                |
| ------------ | --------------------------------------------------- |
| mall-admin   | 后台管理系统                                        |
| mall-auth    | 角色认证模块                                        |
| mall-gateway | 网关模块，请求入口                                  |
| mall-portal  | 前台商城系统                                        |
| mall-search  | 商品检索模块                                        |
| mall-demo    | 用来测试 API 的样例工程                               |
| mall-monitor | Spring 自带的监控模块，TSF 自带监控能力，因此可以略过 |

## 环境准备

### 环境配置建议

>?以下配置仅做建议，具体以您的实际业务需求为主。

- 开发环境：指含有 mall demo 程序源码的计算环境。
- 部署环境：指购买的腾讯云主机，并且运用 TSF 服务部署商城系统的环境。



<table>
<tr>
<th>环境</th>
<th>环境分类</th>
<th>配置</th>
</tr>
<tr>
<td>开发环境</td>
<td>-</td>
<td>CPU: 4核<br> 内存：8GB <br>网络：50Mbps</td>
</tr>
<tr>
<td rowspan="2">部署环境</td>
<td>中间件部署服务器</td>
<td>配置：1台云主机<br> CPU：4核<br> 内存：8GB<br> 网络：50Mbps</td>
</tr>
<tr>
<td>微服务部署服务器</td>
<td>配置：每个服务1台云主机<br> CPU：1核<br> 内存：2GB<br> 网络：20Mbps，按量计费<br> 磁盘：50GB</td>
</tr>
</table>



### 中间件部署服务器准备

1. 参见环境配置建议 [购买云服务器](https://buy.cloud.tencent.com/cvm)。
2. 安装 [Docker](https://docs.docker.com/engine/install/) 和 [Docker Compose](https://docs.docker.com/compose/install/)。
3. 下载 [mall-demo程序包](https://github.com/supergunme/tsf-demo-public)，并将其上传到云服务器中。
4. 进入 `tsf-demo-public/document/docker` 目录，执行如下命令，等待下载和容器拉起完成。
   ```
   docker-compose -f docker-compose-env.yml up -d
   ```
	<dx-alert infotype="explain" title="">
	下载时间根据实际网络带宽可能需等待几分钟到几十分钟不等。
	</dx-alert>
5. 执行下面的命令创建 RabbitMQ 的 virtual_host、用户和权限，需要等 RabbitMQ 启动完成，如果下面的命令报错，再次执行。
   ```
   docker exec -it rabbitmq /init.sh
   正常情况下屏幕会显示如下：
   Adding user "mall" ...
   Setting tags for user "mall" to [administrator] ...
   Adding vhost "/mall" ...
   Setting permissions for user "mall" in vhost "/mall" ...
   ```


## 迁移上云

### 步骤1：准备应用程序包

**前提条件**

[安装 Maven](https://maven.apache.org/install.html)

**操作步骤**
1. 下载 [mall-demo程序包](https://github.com/supergunme/tsf-demo-public) 到本地。
2. 在 `tsf-demo-public` 根目录下执行如下命令，进行依赖初始化，耗时根据网速可能不同。
   ```
   mvn clean
   ```
3. 进入每个项目的 `src/main/resource` 目录，根据已经部署的容器所有的云服务器地址，修改 application.yml 文件中的连接信息。
	<dx-alert infotype="explain" title="">
	若在本地安装调试可以忽略本步骤，即在本地安装 docker 和所有基础组件，在本地启动 Spring Cloud 调试。
	</dx-alert>
   ```yml
   # mysql中替换localhost为内网IP
   url: jdbc:mysql://localhost:3306/mall?useUnicode=true&characterEncoding=utf-8&serverTimezone=Asia/Shanghai
   # redis中替换localhost为内网IP
   host: localhost
   # rabbitmq中替换localhost为内网IP
   host: localhost
   # mongo中替换localhost为内网IP
   host: localhost
   # ES中替换127.0.0.1为内网IP
   uris: 127.0.0.1:9200
   ```
4. 进入 mall-mbg 项目的 `src/main/resource` 目录，修改 generator.properties 文件中 MySQL 的连接信息，修改localhost为指定主机名/IP。
5. 在 `tsf-demo-public` 根目录下，执行如下命令将项目进行打包。
   ```
   mvn clean package -DskipTests
   ```
6. 在 target 目录下，可看到生成的 jar 程序包。
   ```
   需上传jar包本地路径
   mall-admin/target/mall-admin-1.0-SNAPSHOT           # 后台管理系统
   mall-auth/target/mall-auth-1.0-SNAPSHOT             # 角色认证模块
   mall-gateway/target/mall-gateway-1.0-SNAPSHOT       # 网关模块，请求入口
   mall-portal/target/mall-portal-1.0-SNAPSHOT         # 前台商城系统
   mall-search/target/mall-search-1.0-SNAPSHOT         # 商品检索模块
   两个可选部署的服务
   mall-demo/target/mall-demo-1.0-SNAPSHOT       # 用来测试API的样例工程
   mall-monitor/target/mall-monitor-1.0-SNAPSHOT   # Spring自带的监控模块，TSF自带监控能力，故可以略过
   ```

### 步骤2：部署应用到 TSF

以部署 mall-search 服务为例，介绍在 TSF 上部署一个应用的流程。

**新建集群**

1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf/index)，左侧导航栏选择**集群**，单击新建，创建一个名为 mall-demo 的集群。
2. 单击集群操作栏的**导入云主机**，将购买的云服务器全部导入到集群中。

**新建日志配置项**

在左侧导航栏选择**日志服务** > **日志配置**，单击**新建日志配置项**，创建日志采集规则。

![](https://main.qcloudimg.com/raw/d5d682c4c1b61ef0a68efd212cd66f78.png)

**创建并部署应用**

1. 在左侧导航栏选择**应用管理**，单击**新建应用**，创建一个名为 mall-search 的应用。
	 ![](https://main.qcloudimg.com/raw/ebc5f4347228e517f5247a13232421a3.png)
2. 单击**提交**后，在提醒弹窗“是否前往倒入程序包，并部署应用”中单击**确认**，前往上传程序包。
3. [](id:step2_3)在程序包管理页面，单击**上传程序包**，将 mall-search-1.0-SNAPSHOT.jar 程序包上传到 TSF 平台。
4. 单击**提交**后，在弹窗“已上传完程序包，是否部署应用”中选择**前往部署**，前往创建部署组。
5. 在部署组页面，单击**新建部署组**，填写部署组信息。
   - 集群：选择**2.1步骤**中创建的集群
   - 日志配置项：选择**步骤2.2**中创建的日志配置项
![](https://qcloudimg.tencent-cloud.cn/raw/a3ed956784646fa6c3833cc74c26f2e9.png)
6. 单击**保存&下一步**，选择要部署的云主机，单击**部署应用**。
7. 在部署应用页面，选择刚刚上传的程序包版本，健康检查建议勾选“存活检查”和“就绪检查”，因为项目已经集成 actuator，如图填写请求路径即可，端口号根据 application.yml 中定义填写。
![](https://qcloudimg.tencent-cloud.cn/raw/1f62097af40dc146eddf0444ed7066bc.png)
	健康检查：
   ![](https://main.qcloudimg.com/raw/b43f9211d2bc584c68859f4b60570d2e.png)
8. 单击**完成**，完成应用部署。

**查看部署结果**

重复本章节 [**步骤3**](#step2_3) 依次将所有服务部署到 TSF 上，服务部署顺序建议：**服务网关 mall-gateway -> mall-auth -> mall-admin -> mall-portal -> mall-search -> mall-demon**。

当完成所有的服务部署，部署结果如下。

![](https://qcloudimg.tencent-cloud.cn/raw/2715b0b31002fc901ef8a2d7edf0a2ae.png)

## 部署结果验证

### 步骤1：验证服务依赖功能

通过部署前端页面，验证服务依赖功能

1. 登录中间件部署服务器，在服务器上安装 [node.js](https://nodejs.org/dist/v8.9.4/node-v8.9.4-x64.msi)。
2. 下载前端代码，地址 [mall-admin-web](https://github.com/macrozheng/mall-admin-web)。
3. 在项目根目录下执行如下命令，安装前端项目所需的第三方依赖。
   ```
   npm install
   ```
4. 修改 dev.env.js 文件中的 BASE_API 配置为网关服务的端口，示例如下：IP 为gateway 服务机器内网 IP，port 为服务的端口号。
   ```
   http://IP:PORT/mall-admin
   ```
5. 执行如下命令运行前端项目。
   ```
   npm run dev
   
   ```
6. 访问前端页面，地址：`http://中间件服务器的外网 IP: 8090`，体验服务。
7. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf/index)，在**依赖分析** > **服务依赖拓扑**页面，选择命名空间和时间后，可看到如下图的依赖关系。
   ![](https://main.qcloudimg.com/raw/8a1385e52ec3da92e197368f1771a9a7.png)

   

### 步骤2：验证服务治理功能

**验证服务限流功能**

服务限流详细介绍请参见 [服务限流](https://cloud.tencent.com/document/product/649/19046)。

典型业务问题：后端业务被高频恶意访问，导致核心业务链路阻塞，系统瘫痪。

场景：用户频繁访问拉取商品列表接口。

需求：保证核心服务 mall - admin 被每秒中最多被请求20次。

规则配置：在TSF控制台服务治理页面找到 mall-admin 服务，进入服务详情页面，配置服务限流规则。

![](https://main.qcloudimg.com/raw/d491cc4119bcdd37c087ddf9fda3e8dc.png)

效果验证：

![](https://main.qcloudimg.com/raw/b6dccb2c4d676276f3fafb7e017cbeaa.png)

**验证服务鉴权功能**

服务鉴权详细介绍请参见 [服务鉴权](https://cloud.tencent.com/document/product/649/18024)。

电商典型场景：后端敏感业务需要对访问权限进行控制。

场景：对于后台商品管理模块，仅支持有权限的服务对它进行访问。例如，在这个场景中，我们限制 gateway 微服务可以不访问 mall admin 微服务，所有从 gateway 发起的请求都会被拒绝。

配置方式：在 [TSF 控制台](https://console.cloud.tencent.com/tsf/index) 服务治理页面找到 mall-admin 服务，进入服务详情页面，配置服务鉴权规则。

![](https://main.qcloudimg.com/raw/bdc9e40fc9abd3f51c7e8760128a9aa1.png)

效果验证：

![](https://qcloudimg.tencent-cloud.cn/raw/52f255467e3425fb759230c57ab01960.png)



## 自动化部署

当应用非常多，不希望使用控制台逐个部署怎么办呢？ 或者已经使用了 jenkins、travis 等工具，如何对接到 TSF 平台上呢？我们可以参见下面的操作来进行实践。

[mall-demo 程序包](https://github.com/supergunme/tsf-demo-public) 中的 deploy.py 脚本支持自动上传和部署一个新的应用到现有的集群中，默认选择集群中可用实例中的第一个实例机器部署应用。

1. 在 deploy 目录下的 deploy.py 文件中配置 secret_id、secret_key，clusterId 和 namespace 等参数。
<table>
<thead>
<tr>
<th>参数</th>
<th>是否必选</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>path</td>
<td>必选</td>
<td>程序包路径</td>
</tr>
<tr>
<td>applicationName</td>
<td>必选</td>
<td>应用名称</td>
</tr>
<tr>
<td>appId</td>
<td>必选</td>
<td>账号 APPID</td>
</tr>
<tr>
<td>groupName</td>
<td>可选</td>
<td>默认采用和应用名称同名，不可重复</td>
</tr>
<tr>
<td>microserviceType</td>
<td>可选</td>
<td>默认“NATIVE” 云原生应用。否，填写 “N”</td>
</tr>
<tr>
<td>applicationType</td>
<td>可选</td>
<td>默认“V”表示虚拟机部署</td>
</tr>
<tr>
<td>pkgVersion</td>
<td>可选</td>
<td>上传的程序包版本号，默认当前时间戳，时间戳格式：“YYYYmmddHHMMSS”</td>
</tr>
</tbody></table>
2. 在 travis.yml 中添加脚本任务和任务所需的执行参数。依次是：程序包路径、应用名和 APPID。
```yml
- ./scripts/deploy.py mall-demo/target/mall-demo-1.0-SNAPSHOT.jar "test" "1234567890"
```
3. 提交 commit，并且推送到远程分支，自动触发 Travis CI 流程。Travis 流程执行成功。 
 ![](https://main.qcloudimg.com/raw/8b03bb4c06d2d3e74409e90d81388d09.png)   
4. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf/index)，可看到新的应用、部署组和运行实例。
	应用：
![](https://qcloudimg.tencent-cloud.cn/raw/1da32aec9fa7a8b46e449c29f40b85d7.png)
	部署组：
![](https://qcloudimg.tencent-cloud.cn/raw/093a4c38bbf3519b3d560513110dad1e.png)
	运行实例：
![](https://qcloudimg.tencent-cloud.cn/raw/42567628e6f692bfd0f512dc6e0e0ea1.png)

