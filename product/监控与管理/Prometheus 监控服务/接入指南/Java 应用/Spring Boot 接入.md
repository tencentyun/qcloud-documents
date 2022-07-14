## 操作场景

在使用 Spring Boot 作为开发框架时，需要监控应用的状态，例如 JVM/Spring MVC 等。 Prometheus 监控服务基于 Spring Actuator 机制采集 JVM 等数据，结合配套提供的 Grafana Dashboard 可以方便的监控 Spring Boot 应用的状态。

本文档以在容器服务上部署 Spring Boot 应用为例，介绍如何通过 Prometheus监控服务监控其状态。

## 前提条件

- 创建 [腾讯云容器服务—托管版集群](https://cloud.tencent.com/document/product/457/32189#TemplateCreation)：在腾讯云容器服务中创建 Kubernetes 集群。
- [使用私有镜像仓库管理应用镜像](https://cloud.tencent.com/document/product/457/9117)。
- 应用基于 Spring Boot 框架进行开发。

## 操作步骤

> !Spring Boot 已提供 actuator 组件来对应用进行监控，简化了开发的使用成本，所以这里直接使用 actuator 为 Spring Boot 应用进行监控埋点，基于 Spring Boot 2.0 及以上的版本，低版本会有配置上的差别需要注意。
>**若您使用spring boot 1.5 接入，接入时和2.0会有一定区别，需要注意如下几点：**
1. 访问 `prometheus metrics` 的地址和2.0不一样，1.5默认的是`/prometheus`，即`http://localhost:8080/prometheus`。
2. 若报401错误则表示没有权限(Whitelabel Error Page)，1.5默认对 `management` 接口加了安全控制，需要修改 `management.security.enabled=false`。
3. 若项目中用 `bootstrap.yml` 来配置参数，在 `bootstrap.yml` 中修改 `management` 不起作用，需要在 `application.yml` 中修改，原因： spring boot 启动加载顺序有关。
4. `metric common tag` 不能通过 `yml` 来添加，只有通过代码加一个 `bean` 的方式添加，详细信息可参见 [spring boot 1.5 接入](https://micrometer.io/docs/ref/spring/1.5)。

### 修改应用的依赖及配置

#### 步骤1：修改 pom 依赖 

项目中已经引用 `spring-boot-starter-web` 的基础上，在 `pom.xml` 文件中添加 `actuator/prometheus` Maven 依赖项。

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
<dependency>
  <groupId>io.micrometer</groupId>
  <artifactId>micrometer-registry-prometheus</artifactId>
</dependency>
```

#### 步骤2：修改配置

编辑 `resources` 目录下的 `application.yml` 文件，修改 `actuator` 相关的配置来暴露 Prometheus 协议的指标数据。

```
management:
  endpoints:
    web:
      exposure:
        include: prometheus  # 打开 Prometheus 的 Web 访问 Path
  metrics:
    # 下面选项建议打开，以监控 http 请求的 P99/P95 等，具体的时间分布可以根据实际情况设置
    distribution:
      sla:
        http:
          server:
            requests: 1ms,5ms,10ms,50ms,100ms,200ms,500ms,1s,5s
    # 在 Prometheus 中添加特别的 Labels
    tags:
      # 必须加上对应的应用名，因为需要以应用的维度来查看对应的监控
      application: spring-boot-mvc-demo
```

#### 步骤3：本地验证

在项目当前目录下，运行 `mvn spring-boot:run` 之后，可以通过 `http://localhost:8080/actuator/prometheus` 访问到 Prometheus 协议的指标数据，说明相关的依赖配置已经正确。

> ?例子中配置默认配置，对应的端口和路径以实际项目为准。

### 将应用发布到腾讯云容器服务上

#### 步骤1：本地配置 Docker 镜像环境

如果本地之前未配置过 Docker 镜像环境，可以参考 [镜像仓库基本教程](https://cloud.tencent.com/document/product/457/9117) 进行配置，如果已经配置可以直接执行下一步。

#### 步骤2：打包及上传镜像

1. 在项目根目录下添加 `Dockerfile` ，您可以参考如下示例进行添加，在实际项目中需要修改 `Dockerfile` 。
```plaintext
FROM openjdk:8-jdk
WORKDIR /spring-boot-demo
ADD target/spring-boot-demo-*.jar /spring-boot-demo/spring-boot-demo.jar
CMD ["java","-jar","spring-boot-demo.jar"]
```
2. 打包镜像，在项目根目录下运行如下命令，在实际项目中需要替换对应的 `namespace`、`ImageName`、`镜像版本号`。
```plaintext
mvn clean package
docker build . -t ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[镜像版本号]
docker push ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[镜像版本号]
```
例如：
```plaintext
mvn clean package
docker build . -t ccr.ccs.tencentyun.com/prom_spring_demo/spring-boot-demo:latest
docker push ccr.ccs.tencentyun.com/prom_spring_demo/spring-boot-demo:latest
```

#### 步骤3：应用部署

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/cluster?rid=1)，选择需要部署的容器集群。
2. 单击**工作负载** > **Deployment**，进入 Deployment 管理页面，选择对应的命名空间来进行部署服务，这里选择通过控制台的方式创建，同时打开 Service 访问方式，您也可以选择通过命令行的方式创建。
![](https://main.qcloudimg.com/raw/396a36fccd6f9c5568bcdac692626114.png)
![](https://main.qcloudimg.com/raw/22e6bb4a200f2664a8005f54f977a72b.png)
3. 为对应的 Service 添加 K8S Labels，如果使用命令方式新建，可以将 Labels 直接加上。这里介绍在容器控制台调整配置，选择需要调整的容器集群。
单击**服务与路由** > **Service**，进入 Service 管理页面，选择对应的命名空间来调整 Service Yaml 配置，如下图：
![](https://main.qcloudimg.com/raw/fab7f044fdc658a7608214d86eed740e.png)
配置示例如下：

```yaml
  apiVersion: v1
  kind: Service
  metadata:
     labels: # 可以根据实际情况添加对应的 labels
       k8sapp: spring-mvc-demo
     name: spring-mvc-demo
     namespace: spring-demo
  spec:
     ports:
     - name: 8080-8080-tcp  # ServiceMonitor 抓取任务中 port 对应的值
       port: 8080
       protocol: TCP
       targetPort: 8080
     selector:
       k8s-app: spring-mvc-demo
       qcloud-app: spring-mvc-demo
     sessionAffinity: None
     type: ClusterIP
   status:
     loadBalancer: {}
```

#### 步骤4：添加采取任务

1. 登录 [ Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)，选择对应 Prometheus 实例进入管理页面。
2. 单击集成容器服务列表中的**集群 ID**，进入到容器服务集成管理页面。
3. 通过服务发现添加 Service Monitor，目前支持基于 Labels 发现对应的目标实例地址，所以可以对一些服务添加特定的 K8S Labels，配置之后在 Labels 下的服务都将被 Prometheus 服务自动识别出来，不需要再为每个服务一一添加采取任务。以该例子介绍，配置信息如下：
> ?这里需要注意的是 `port` 的取值为 `service yaml` 配置文件里的 `spec/ports/name` 对应的值。

```yaml
  apiVersion: monitoring.coreos.com/v1
  kind: ServiceMonitor
  metadata:
    name: spring-mvc-demo # 填写一个唯一名称
    namespace: cm-prometheus # namespace固定，不要修改
  spec:
    endpoints:
    - interval: 30s
      port: 8080-8080-tcp # 填写service yaml中Prometheus Exporter对应的Port的Name
      path: /actuator/prometheus  # 填写Prometheus Exporter对应的Path的值，不填默认/metrics
    namespaceSelector:  # 选择要监控service所在的namespace
      matchNames:
      - spring-demo 
    selector: # 填写要监控service的Label值，以定位目标service
      matchLabels:
        k8sapp: spring-mvc-demo 
```

#### 步骤5：查看监控

打开 Prometheus 实例对应的 Grafana 地址，在 `Dashboards/Manage/Application` 下查看应用相关的监控大屏。

- Spring MVC 应用：监控 MVC 的状态，例如请求耗时/请求量/成功率/异常分布等。
- Spring MVC 接口：接口级监控，可以对应多个接口，方便定位是哪个接口出问题。
- Tomcat：Tomcat 内部状态的监控大屏，例如线程使用情况等。
- 应用 JVM：从应用角度出发，查看该应用下所有实例是否有问题，当发现某个实例有问题时可以下钻到对应的实例监控。
- 实例 JVM：单实例 JVM 详细的监控数据。

![](https://main.qcloudimg.com/raw/64fe9d893ea8ee2451d4a724fd8578fe.png)
![](https://main.qcloudimg.com/raw/bd5a682f94502b534bb57d602969f2b3.png)
![](https://main.qcloudimg.com/raw/6472032f91fb7f8081eb61a7a935c9d3.png)
