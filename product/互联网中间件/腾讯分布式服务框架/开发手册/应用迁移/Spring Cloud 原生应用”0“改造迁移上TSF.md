## 操作场景

TSF 支持原生 Spring Cloud 应用无侵入接入，无需改造即可直接接入 TSF，享受服务注册与发现、服务治理、应用监控和调用链跟踪等功能。

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

1. 参考环境配置建议 [购买云服务器](https://buy.cloud.tencent.com/cvm)。
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

### 步骤1. 准备应用程序包

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

### 步骤2. 部署应用到 TSF

以部署 mall-search 服务为例，介绍在 TSF 上部署一个应用的流程。

**2.1 新建集群**

1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf/index)，左侧导航栏选择【集群】，单击新建，创建一个名为 mall-demo 的集群。
2. 单击集群操作栏的【导入云主机】，将购买的云服务器全部导入到集群中。

**2.2 新建日志配置项**

在左侧导航栏选择【日志服务】>【日志配置】，单击【新建日志配置项】，创建日志采集规则。

![](https://main.qcloudimg.com/raw/d5d682c4c1b61ef0a68efd212cd66f78.png)

**2.3 创建并部署应用**

1. 在左侧导航栏选择【应用管理】，单击【新建应用】，创建一个名为 mall-search 的应用。

	 ![](https://main.qcloudimg.com/raw/ebc5f4347228e517f5247a13232421a3.png)

2. 单击【提交】后，在提醒弹窗“是否前往倒入程序包，并部署应用”中单击【确认】，前往上传程序包。

3. 在程序包管理页面，单击【上传程序包】，将 mall-search-1.0-SNAPSHOT.jar 程序包上传到TSF平台。

4. 单击【提交】后，在弹窗“已上传完程序包，是否部署应用”中选择【前往部署】，前往创建部署组。

5. 在部署组页面，单击【新建部署组】，填写部署组信息。

   - 集群：选择**2.1步骤**中创建的集群
   - 日志配置项：选择**步骤2.2**中创建的日志配置项

   ![](https://main.qcloudimg.com/raw/a7ef5d0003109f2d33e3e1c9f275c610.png)

6. 单击【保存&下一步】，选择要部署的云主机，单击【部署应用】。

7. 在部署应用页面，选择刚刚上传的程序包版本，健康检查建议勾选“存活检查”和“就绪检查”，因为项目已经集成 actuator，如图填写请求路径即可，端口号根据 application.yml 中定义填写。

   ![](https://main.qcloudimg.com/raw/8f488e92a27488364b5d25d3f51b5711.png)
	健康检查：
   ![](https://main.qcloudimg.com/raw/b43f9211d2bc584c68859f4b60570d2e.png)

8. 单击【完成】，完成应用部署。

**2.4 查看部署结果**

重复本章节**2.3步骤**依次将所有服务部署到TSF上，服务部署顺序建议：**服务网关 mall-gateway -> mall-auth -> mall-admin -> mall-portal -> mall-search -> mall-demon**。

当完成所有的服务部署，部署结果如下。

![](https://main.qcloudimg.com/raw/f58caa863857f5ffd8ae560771552d8c.png)

## 部署结果验证

### 步骤1. 验证服务依赖功能

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

7. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf/index)，在【依赖分析】>【服务依赖拓扑】页面，选择命名空间和时间后，可看到如下图的依赖关系。

   ![](https://main.qcloudimg.com/raw/8a1385e52ec3da92e197368f1771a9a7.png)

   

### 步骤2. 验证服务治理功能

**2.1 验证服务限流功能**

服务限流详细介绍请参考 [服务限流](https://cloud.tencent.com/document/product/649/19046)。

典型业务问题：后端业务被高频恶意访问，导致核心业务链路阻塞，系统瘫痪。

场景：用户频繁访问拉取商品列表接口。

需求：保证核心服务 mall - admin 被每秒中最多被请求20次。

规则配置：在TSF控制台服务治理页面找到 mall-admin 服务，进入服务详情页面，配置服务限流规则。

![](https://main.qcloudimg.com/raw/d491cc4119bcdd37c087ddf9fda3e8dc.png)

效果验证：

![](https://main.qcloudimg.com/raw/b6dccb2c4d676276f3fafb7e017cbeaa.png)

**2.2 验证服务鉴权功能**

服务鉴权详细介绍请参考 [服务鉴权](https://cloud.tencent.com/document/product/649/18024)。

电商典型场景：后端敏感业务需要对访问权限进行控制。

场景：对于后台商品管理模块，仅支持有权限的服务对它进行访问。例如，在这个场景中，我们限制 gateway 微服务可以不访问 mall admin 微服务，所有从 gateway 发起的请求都会被拒绝。

配置方式：在 [TSF 控制台](https://console.cloud.tencent.com/tsf/index) 服务治理页面找到 mall-admin 服务，进入服务详情页面，配置服务鉴权规则。

![](https://main.qcloudimg.com/raw/bdc9e40fc9abd3f51c7e8760128a9aa1.png)

效果验证：

![](https://main.qcloudimg.com/raw/9b912871186b60eb7cd4736df1936762.png)



## 自动化部署

当应用非常多，不希望使用控制台逐个部署怎么办呢？ 或者已经使用了 jenkins、travis 等工具，如何对接到 TSF 平台上呢？我们可以参考下面的操作来进行实践。

[mall-demo 程序包](https://github.com/supergunme/tsf-demo-public) 中的 deploy.py 脚本支持自动上传和部署一个新的应用到现有的集群中，默认选择集群中可用实例中的第一个实例机器部署应用。

1. 在 deploy 目录下的 deploy.py 文件中配置 secret_id、secret_key，clusterId 和 namespace 等参数。


   | 参数                     | 是否必选  | 说明                                                         |
   | ------------------------ |---- | ------------------------------------------------------------ |
   | path  | 必选             | 程序包路径                                                   |
   | applicationName | 必选  | 应用名称                                                     |
   | appId | 必选            | 账号 APPID                                                    |
   | groupName | 可选        | 默认采用和应用名称同名，不可重复                             |
   | microserviceType |可选 | 默认“NATIVE” 云原生应用。否，填写 “N”                        |
   | applicationType | 可选  | 默认“V”表示虚拟机部署                                        |
   | pkgVersion | 可选      | 上传的程序包版本号，默认当前时间戳，时间戳格式：“YYYYmmddHHMMSS”|

2. 在 travis.yml 中添加脚本任务和任务所需的执行参数。依次是：程序包路径、应用名和 APPID。

```yml
- ./scripts/deploy.py mall-demo/target/mall-demo-1.0-SNAPSHOT.jar "test" "1234567890"
```

3. 提交 commit，并且推送到远程分支，自动触发 Travis CI 流程。Travis 流程执行成功。 
 ![](https://main.qcloudimg.com/raw/8b03bb4c06d2d3e74409e90d81388d09.png)   

4. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf/index)，可看到新的应用、部署组和运行实例。
	应用：
	 ![](https://main.qcloudimg.com/raw/6543c26217bd5057bbec86a8969a7d10.png)
	部署组：
	 ![](https://main.qcloudimg.com/raw/d067b31daeabbb9232c9cc2263bb7a47.png)
	运行实例：
	 ![](https://main.qcloudimg.com/raw/57d7a5741f0b959a58edec843f8fffb7.png)

