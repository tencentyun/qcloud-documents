


通过 Dubbo 的扩展机制，将 TSF 的大部分能力适配至 Dubbo 上，允许用户只修改几行依赖和配置即可体验完整的服务治理和监控体验。

> ?Apache Dubbo3 接入 TSF 需要平台组件支持，私有云 TSF 支持的版本请提交工单咨询



## 功能支持

- 服务注册与发现：  支持 Dubbo3 的接口级注册发现和应用级注册发现
  - 应用级的服务名为 dubbo.application.name。但如果与 Spring Cloud 结合使用，并且与 spring.application.name 相同，为了区分服务，Dubbo 应用级服务名自动加下 `-dubbo`后缀。Dubbo3 机制下，当程序有暴露 Dubbo 接口时，才会进行应用级的服务注册。
  - 接口级的服务名为 `providers:<接口全限定名>:<Version信息>:<Group信息>`。
- 配置管理：如需使用，建议结合 spring-cloud-tsf-starter 一起使用。如果是纯 Dubbo3 应用，仅支持通过内部接口获取配置及监听。
- 服务治理：支持服务鉴权、服务路由、服务限流、服务熔断。
  - TSF 服务熔断需要配置在主调方，由于仅 dubbo client 时可以不注册服务。可以结合  spring-cloud-tsf-starter 使用并配置在 Spring Cloud 对应的服务上。或者在控制台上手动创建 dubbo.application.name 对应的服务，并在上面配置熔断规则。
  - Dubbo 第一跳没有对应的服务，因此第一跳时，治理规则自定义标签中无法使用上游服务名进行限制。第二跳时，上游服务名为上一跳的目标 Dubbo 服务。
  - Dubbo3 治理规则系统标签不支持 API 以及 HTTP method。
  - Dubbo3 默认优先选择应用级服务发现，此时服务鉴权、服务路由、服务限流规则需要配置在应用级对应的服务上。
- 服务容错：不单独支持 Dubbo3 服务容错，如果需要使用可结合 spring-cloud-tsf-starter。
- 参数传递
  - 与 Spring Cloud 结合使用时，可以参考 [Spring Cloud TSF 参数传递的用法](https://cloud.tencent.com/document/product/649/18511)。
  - Dubbo3 单独使用时，可使用`com.tencent.tsf.util.TsfTagUtils`的对应方法。
- 全链路灰度发布：支持。并且支持全链路中包含 Dubbo3 服务也有 Spring Cloud 服务（仅支持 Spring Cloud 2020 及以上的版本）。
- 调用链、服务监控：通过可观测 Agent（opentelemetry）支持大部分功能，但调用链中的 API 信息不支持跳转，不支持 API 级别的监控信息。
- API 注册：Dubbo3 不支持。
- 与 Spring Cloud 框架结合：仅支持 Spring Cloud 2020 及以上的版本一起使用 。

  



## 接入操作步骤

### 步骤1：安装 Maven 环境

参见 [下载 Maven](https://cloud.tencent.com/document/product/649/20231)下载安装 Java 和 Maven。

### 步骤2：配置注册中心

- Dubbo 官网 Demo：
```xml
<dubbo:registry address="multicast://224.5.6.7:1234"/>
```

- TSF Demo（**注册中心地址使用注册中心 IP 和端口替换**）：[下载地址->>](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/dubbo/dubbo3-demo.zip)

xml 格式：
```xml
<dubbo:registry address="tsf://127.0.0.1:8500">
</dubbo:registry>
```
yaml 格式：
```yaml
dubbo:
  registry:
    address: tsf://127.0.0.1:8500
```
- 注册中心协议名为 tsf。
> ?新接入客户推荐使用注册中心协议 tsf，接口级注册时，服务名附带完整的信息。存量使用 TSF Atom Dubbo 接入的客户，如果使用的协议是 tsfconsul，升级到 TSF Dubbo3 时也需要保持，否则服务发现不兼容。
> 
- "注册中心地址:端口" 可以填写 127.0.0.1:8500，在 TSF 控制台部署时，SDK 会替换为正确的地址。
- 默认的 register-mode 为 all，即双注册（既包括应用级，也包括接口级），如果都是 Dubbo3 的应用，建议 register-mode 改为 instance，仅注册应用级服务。这样服务列表的服务数比较少，比较干净，也可以降低注册中心的压力。如果有存量的 TSF Atom Dubbo2.7 的，可以全部迁到 TSF Dubbo3 后建议将  register-mode 改为 instance。
xml 格式：
```xml
<dubbo:application name="provider-demo-dubbo" logger="slf4j" register-mode="instance"/>
```
yaml 格式：
```yaml
dubbo:
  application:
    name: provider-demo-dubbo
    logger: slf4j
    register-mode: instance
```



### 步骤3：添加依赖

根据 Dubbo3 单独使用还是和 Spring Cloud 一起使用，所用的依赖及其版本有一定区别。
- 单独使用 Dubbo（可能与 Spring Boot 一起使用），在 pom .xml 文件中增加插件依赖：
   ```xml
   <dependency>
       <groupId>com.tencent.tsf</groupId>
       <artifactId>femas-adaptor-tsf-apache-dubbo3</artifactId>
     	<!-- 调整为 tsf dubbo3 最新版本号，1.0.6-RELEASE 为支持 dubbo3 的第一版 -->
       <version>1.0.7-RELEASE</version>
   </dependency>
   ```
- Dubbo3 与 Spring Cloud 一起使用（Spring Cloud 只支持 2020 及以上版本）
  - 父依赖：父依赖使用 spring-cloud-tsf-dependencies。
    ```xml
    <parent>
        <groupId>com.tencent.tsf</groupId>
        <artifactId>spring-cloud-tsf-dependencies</artifactId>
      	<!-- 调整为 spring cloud 2020 tsf 最新版本号，1.40.6-SpringCloud2020-RELEASE 为支持 dubbo3 的第一版 -->
        <version>1.40.7-SpringCloud2020-RELEASE</version>
    </parent>
    ```
    如果必须要用业务的父依赖，则可以在子项目的 dependencyManagement 里添加。
    ```xml
    <dependencyManagement>
      <dependencies>
        <dependency>
          <groupId>com.tencent.tsf</groupId>
          <artifactId>spring-cloud-tsf-dependencies</artifactId>
          <!-- 调整为 spring cloud 2020 tsf 最新版本号，1.40.6-SpringCloud2020-RELEASE 为支持 dubbo3 的第一版 -->
        	<version>1.40.7-SpringCloud2020-RELEASE</version>
          <type>pom</type>
          <scope>import</scope>
        </dependency>
      </dependencies>
    </dependencyManagement>
    ```
  - tsf dubbo3 依赖：不需要指定版本号，如果手动指定了，可能与 spring cloud tsf 的产生冲突，造成异常。
    ```xml
    <dependency>
        <groupId>com.tencent.tsf</groupId>
        <artifactId>femas-adaptor-tsf-apache-dubbo3</artifactId>
    </dependency>
    ```

### 步骤4：配置日志格式
Spring Cloud 2020（Spring Boot 2.4）开始，默认的日志格式有所变化。如果需要用日志配置项中的 Spring Boot 格式采集日志，需要对 pattern 进行以下设置

```yaml
logging:
  pattern:
    level: "%-5level [${spring.application.name},%mdc{trace_id},%mdc{span_id},]"
```

### 步骤5：打包 FatJar

和 Spring Boot 或 Spring Cloud 结合的时候，您可以通过 **spring-boot-maven-plugin** 构建一个包含所有依赖的 jar 包（FatJar）， 在 pom.xml 所在目录下执行命令`mvn clean package`。

>?如果是单纯的 Dubbo 应用，可以使用 Maven 的 FatJar 插件。

### 步骤6：使用可观测 Agent

可观测 Agent 在云上部署时才需要使用。本地使用也无法采集数据。

使用方法：下载 [ot-agent-release.tar](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/jvm%E7%9B%91%E6%8E%A7/ot-agent-release.tar)，并解压。容器部署时需要手动将 Agent 物料放到镜像内。启动 jar 时附带 -javaagent:ot-agent-release/opentelemetry-javaagent.jar -Dotel.traces.exporter=none -Dotel.javaagent.extensions=ot-agent-release/femas-trace-opentelemetry.jar`，通过 main 方法直接启动。其中 ot-agent-release/opentelemetry-javaagent.jar  和 ot-agent-release/femas-trace-opentelemetry.jar 是对应的具体路径。例如：

```shell
java ${JAVA_OPTS} -Xshare:off -javaagent:/opt/ot-agent-release/opentelemetry-javaagent.jar -Dotel.traces.exporter=none -Dotel.javaagent.extensions=/opt/ot-agent-release/femas-trace-opentelemetry.jar -jar provider-demo.jar
```



如果使用的是 jdk17，还需要额外加以下参数 `--add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/java.lang.reflect=ALL-UNNAMED --add-opens java.base/java.math=ALL-UNNAMED --add-opens java.base/sun.net.util=ALL-UNNAMED`

```shell
java ${JAVA_OPTS} -Xshare:off -javaagent:/opt/ot-agent-release/opentelemetry-javaagent.jar -Dotel.traces.exporter=none -Dotel.javaagent.extensions=/opt/ot-agent-release/femas-trace-opentelemetry.jar --add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/java.lang.reflect=ALL-UNNAMED --add-opens java.base/java.math=ALL-UNNAMED --add-opens java.base/sun.net.util=ALL-UNNAMED -jar provider-demo.jar
```



## 与 TSF Atom Dubbo 2.7 的兼容性

- 适用于 consumer 为 TSF Atom Dubbo 2.7 、provider 为 TSF Dubbo3 或 consumer 为 TSF Dubbo3、provider 为 TSF Atom Dubbo 2.7 的场景
- 注册中心协议需要保持一致，否则服务发现会失败
- 混用场景仅兼容服务注册与发现。治理能力需要 consumer 和 provider 都升级到 TSF Dubbo3 才能完整支持



## Dubbo reference 配置建议

Dubbo 客户端需要使用 reference 对象调用 Dubbo 服务端，reference 的 check 属性默认为 true。即启动时会检查服务端的实例状态，如果不存在在线实例，则会启动失败。建议设置为 false，避免对服务启动顺序的依赖。timeout 属性默认为 1000 （单位ms），初始化建立连接，可观测 Agent 对相关 class 的增强，都是在第一次调用的时候进行。如果业务程序也有一些初始化而导致慢些，较容易超时，建议根据实际情况调整，最好 5000ms 以上。

- xml 格式示例：
```xml
<dubbo:reference id="echoDubboService" interface="com.tsf.demo.dubbo.EchoDubboService" check="false"  timeout="5000"/>
```
- Java 注解示例：
```java
@DubboReference(timeout = 5000, check = false)
EchoDubboService echoDubboService;
```







