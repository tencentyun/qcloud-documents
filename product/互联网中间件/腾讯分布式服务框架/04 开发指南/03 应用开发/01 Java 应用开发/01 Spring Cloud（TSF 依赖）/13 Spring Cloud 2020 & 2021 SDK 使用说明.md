
##  使用说明及限制

1. 修改 在`pom.xml`中的 parent 依赖。
   ```xml
   <parent>
       <groupId>com.tencent.tsf</groupId>
       <artifactId>spring-cloud-tsf-dependencies</artifactId>
       <version><!-- 调整为 SDK 长期维护（LTS）版本号 --></version>
   </parent>
   ```
   - 普通微服务：向工程中添加`spring-cloud-tsf-starter`依赖。
   ```xml
   <dependency>
       <groupId>com.tencent.tsf</groupId>
       <artifactId>spring-cloud-tsf-starter</artifactId>
   </dependency>
   ```
   `spring-cloud-tsf-starter`中包含了服务注册发现、服务路由、服务鉴权、服务限流、服务熔断、服务容错、服务监控、分布式配置功能。
   - 网关：向工程中添加`spring-cloud-tsf-msgw-scg`依赖。
   ```xml
   <dependency>
       <groupId>com.tencent.tsf</groupId>
       <artifactId>spring-cloud-tsf-msgw-scg</artifactId>
   </dependency>
   ```
   >!TSF Spring Cloud 2020 开始不再支持 zuul1 网关。
2. 向 Application 类中添加注解`@EnableTsf`。
   ```java
   // 下面省略了无关的代码
   import org.springframework.tsf.annotation.EnableTsf;
   @SpringBootApplication
   @EnableTsf
   public class ProviderApplication {
       public static void main(String[] args) {
           SpringApplication.run(ProviderApplication.class, args);
       }
   }
   ```
>!Spring Cloud Finchley/Greenwich/Hoxton 支持 @EnableTsfAuth 等注解的单独使用，仅开启部分功能，Spring Cloud 2020 不再支持，添加依赖后及支持全部 SDK 功能。
>


3. 配置日志 pattern
Spring Cloud 2020（Spring Boot 2.4）开始，默认的日志格式有所变化。如果需要用日志配置项中的 Spring Boot 格式采集日志，需要对 pattern 进行以下设置

```yaml
logging:
  pattern:
    level: "%-5level [${spring.application.name},%mdc{trace_id},%mdc{span_id},]"
```


4. TSF Spring Cloud 2020 开始，调用链、监控功能通过 OpenTelemetry 的 java agent 支持。
   - 虚拟机：部署时展开高级选项，勾选“Agent 配置”中的“可观测 Agent”。
   - 容器（通过 TSF 控制台制作的镜像）部署时展开高级选项，勾选“Agent 配置”中的“可观测 Agent”。
     ![](https://qcloudimg.tencent-cloud.cn/raw/ea998d8b5e2233e33f87a2332bdc7354.png)
   - 容器（手动制作的镜像）：Dockerfile 中添加  [ot-agent-release.tar ](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/jvm%E7%9B%91%E6%8E%A7/ot-agent-release.tar)，并通过 VM options 配置启动参数：
<dx-codeblock>
:::  bash
-javaagent:ot-agent-release/opentelemetry-javaagent.jar -Dotel.javaagent.extensions=ot-agent-release/femas-trace-opentelemetry.jar
:::
</dx-codeblock>

   
     
