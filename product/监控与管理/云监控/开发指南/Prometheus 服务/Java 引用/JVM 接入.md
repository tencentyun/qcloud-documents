## 操作场景

在使用 Java 作为开发语言的时候，需要监控 JVM 的性能。腾讯云 Prometheus 服务通过采集应用暴露出来的 JVM 监控数据，并提供了开箱即用的 Grafana 监控大盘。

本文以如何在容器服务上部署普通 Java 应用为例，介绍如何通过托管 Prometheus 监控其状态。

>?若已使用 Spring Boot 作为开发框架，请参见 [Spring Boot 接入](https://cloud.tencent.com/document/product/248/49086)。

## 前提条件

- 创建腾讯云容器服务 [托管版集群](https://cloud.tencent.com/document/product/457/32189#TemplateCreation)。
- [使用私有镜像仓库管理应用镜像](https://cloud.tencent.com/document/product/457/9117)。

## 操作步骤

>? Java 作为主流的开发语言其生态较为完善，其中 [micrometer](https://micrometer.io/) 作为指标打点 SDK 已经被广泛运行，本文以 micrometer 为例介绍如何监控 JVM。


### 修改应用的依赖及配置

#### 步骤1：修改 pom 依赖 

在 `pom.xml` 文件中添加相关的 Maven 依赖项，试情况调整相应的版本，示例如下：

```xml
<dependency>
    <groupId>io.prometheus</groupId>
    <artifactId>simpleclient</artifactId>
    <version>0.9.0</version>
</dependency>
<dependency>
    <groupId>io.micrometer</groupId>
    <artifactId>micrometer-registry-prometheus</artifactId>
    <version>1.1.7</version>
</dependency>
```

#### 步骤2：修改代码

在项目启动时，添加相应的监控配置，同时 micrometer 也提供了部分常用的监控数据采集，具体在 `io.micrometer.core.instrument.binder` 包下，可以按实际情况添加。示例如下：

````java
public class Application {
    // 作为全局变量，可以在自定义监控中使用
    public static final PrometheusMeterRegistry registry = new PrometheusMeterRegistry(PrometheusConfig.DEFAULT);
    static {
        // 添加 Prometheus 全局 Label，建议加一上对应的应用名
        registry.config().commonTags("application", "java-demo");
    }

    public static void main(String[] args) throws Exception {
        // 添加 JVM 监控
        new ClassLoaderMetrics().bindTo(registry);
        new JvmMemoryMetrics().bindTo(registry);
        new JvmGcMetrics().bindTo(registry);
        new ProcessorMetrics().bindTo(registry);
        new JvmThreadMetrics().bindTo(registry);
        new UptimeMetrics().bindTo(registry);
        new FileDescriptorMetrics().bindTo(registry);
        System.gc(); // Test GC
        try {
            // 暴露 Prometheus HTTP 服务，如果已经有，可以使用已有的 HTTP Server
            HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);
            server.createContext("/metrics", httpExchange -> {
                String response = registry.scrape();
                httpExchange.sendResponseHeaders(200, response.getBytes().length);
                try (OutputStream os = httpExchange.getResponseBody()) {
                    os.write(response.getBytes());
                }
            });

            new Thread(server::start).start();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
```

>?由于 JVM GC Pause 监控是通过 GarbageCollector Notification 机制实现，因此只有发生 GC 之后才有监控数据。上述示例为了测试更直观，主动调用了 `System.gc()`。

#### 步骤3：本地验证

本地启动之后，可以通过 `http://localhost:8080/metrics` 访问到 Prometheus 协议的指标数据。


### 将应用发布到腾讯云容器服务上

#### 步骤1：本地配置 Docker 镜像环境

如果本地之前未配置过 Docker 镜像环境，可以参见容器镜像服务 [快速入门](https://cloud.tencent.com/document/product/1141/50332) 文档进行配置。若已配置请执行下一步。


#### 步骤2：打包及上传镜像

1. 在项目根目录下添加 `Dockerfile`，请根据实际项目进行修改。示例如下：

  ```
  FROM openjdk:8-jdk
  WORKDIR /java-demo
  ADD target/java-demo-*.jar /java-demo/java-demo.jar
  CMD ["java","-jar","java-demo.jar"]
  ```

2. 打包镜像，在项目根目录下运行如下命令，需要替换对应的 `namespace`/`ImageName`/`镜像版本号`。

  ```bash
  mvn clean package
  docker build . -t ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[镜像版本号]
  docker push ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[镜像版本号]
  ```
  **示例如下：**
  ```bash
  mvn clean package
  docker build . -t ccr.ccs.tencentyun.com/prom_spring_demo/java-demo:latest
  docker push ccr.ccs.tencentyun.com/prom_spring_demo/-demo:latest
  ```

#### 步骤3：应用部署

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/cluster?rid=1)，选择需要部署的容器集群。
2. 通过**工作负载** > **Deployment**进入 `Deployment` 管理页面，选择对应的 `命名空间` 来进行部署服务，通过 YAML 来创建对应的 `Deployment`，YAML 配置如下。
>?如需通过控制台创建，请参见 [Spring Boot 接入](https://cloud.tencent.com/document/product/248/49086)。

``` yaml
apiVersion: apps/v1
kind: Deployment
metadata:
    labels:
      k8s-app: java-demo
    name: java-demo
    namespace: spring-demo
spec:
    replicas: 1
    selector:
      matchLabels:
        k8s-app: java-demo
    template:
      metadata:
        labels:
          k8s-app: java-demo
    spec:
      containers:
      - image: ccr.ccs.tencentyun.com/prom_spring_demo/java-demo
        imagePullPolicy: Always
        name: java-demo
        ports:
        - containerPort: 8080
          name: metric-port
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      dnsPolicy: ClusterFirst
      imagePullSecrets:
      - name: qcloudregistrykey
      restartPolicy: Always
      schedulerName: default-scheduler
      terminationGracePeriodSeconds: 30
```

#### 步骤4：添加采取任务

1. 登录 [云监控 Prometheus 控制台](https://console.cloud.tencent.com/monitor/prometheus)，选择对应 Prometheus 实例进入管理页面。
2. 通过集成容器服务列表单击**集群 ID**进入到容器服务集成管理页面。
3. 通过服务发现添加 `Pod Monitor` 来定义 Prometheus 抓取任务，YAML 配置示例如下：

```yaml
  apiVersion: monitoring.coreos.com/v1
  kind: PodMonitor
  metadata:
    name: java-demo
    namespace: cm-prometheus
  spec:
    namespaceSelector:
      matchNames:
      - java-demo
    podMetricsEndpoints:
    - interval: 30s
      path: /metrics
      port: metric-port
    selector:
      matchLabels:
        k8s-app: java-demo
```

#### 步骤5：查看监控

1. 在对应 Prometheus 实例 >**集成中心**中找到 `JVM` 监控，安装对应的 Grafana Dashboard 即可开启 JVM 监控大盘。
2. 打开 Prometheus 实例对应的 Grafana 地址，在 `Dashboards/Manage/Application` 下查看应用相关的监控大屏。
	- **应用 JVM**：从应用角度出发，查看该应用下所有实例是否有问题，当发现某个实例有问题时可以下钻到对应的实例监控。
	- **实例 JVM**：单实例 JVM 详细的监控数据。
	![](https://main.qcloudimg.com/raw/e440a4b784bb31d02aafb60cbca929f2.png)
	![](https://main.qcloudimg.com/raw/6472032f91fb7f8081eb61a7a935c9d3.png)
