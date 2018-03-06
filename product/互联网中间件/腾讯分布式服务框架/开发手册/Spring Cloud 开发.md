## 服务注册发现

### 名词解释
Consul : 用于服务注册发现和配置管理。

Feign : 声明式 REST 客户端， 使用Feign可以创建声明式、模板化的HTTP客户端。

### 实现服务注册和发现

#### 1. 服务提供者

**Maven 依赖**
在 pom.xml 中 增加如下依赖：
- spring-boot-starter-parent : 定义了 Spring Boot 版本的基础依赖以及一些默认配置内容。
- spring-boot-starter-web : 全栈 Web 开发模块，包含嵌入式 Tomcat、 Spring MVC。
- spring-boot-starter-test : 通用测试模块，包含 JUnit、Hamcrest、Mockito。
- spring-cloud-starter-consul-discovery：用于服务注册发现的模块。
- spring-cloud-starter-feign：用于实现声明式 REST 客户端。

**application.properties 配置文件**
~~~ xml
#server.address=10.175.133.156
server.port=8002

spring.application.name=demo-provider

spring.cloud.consul.host=127.0.0.1
spring.cloud.consul.port=8500
spring.cloud.consul.discovery.health-check-url=http://${server.address}:${server.port}/health 
spring.cloud.consul.discovery.healthCheckInterval=10s

~~~

**代码**
创建应用主类 TsfDemoProviderApplication 。在主类中通过加入 EnableDiscoveryClient 注解开启服务注册发现功能。
~~~ Java
@SpringBootApplication
@EnableDiscoveryClient
public class TsfDemoProviderApplication {

	public static void main(String[] args) {
		SpringApplication.run(TsfDemoProviderApplication.class, args);
	}
}
~~~

创建请求处理类 DemoController。在 DemoController 类中创建请求处理接口 /provider，在日志中打印出服务的相关内容。

~~~ Java
@RestController
public class DemoController {

    private static final Logger logger = LoggerFactory.getLogger(DemoController.class.getName());

    @RequestMapping(value = "/provider")
    public String provider() {
        logger.info("provider is being called");
        return "resource providing ...\n";
    }
}
~~~



#### 2. 服务消费者
**Maven 依赖**
在 pom.xml 中 增加如下依赖：

- spring-boot-starter-parent：定义了 Spring Boot 版本的基础依赖以及一些默认配置内容。
- spring-boot-starter-web：全栈 Web 开发模块，包含嵌入式 Tomcat、 Spring MVC。
- spring-boot-starter-test：通用测试模块，包含 JUnit、Hamcrest、Mockito。
- spring-cloud-starter-consul-discovery：用于服务注册发现的模块。
- spring-cloud-starter-feign：用于实现声明式 REST 客户端。

**application.properties 配置文件**

~~~ xml
#server.address=10.175.133.156
server.port=8001

spring.application.name=demo-consumer

spring.cloud.consul.host=127.0.0.1
spring.cloud.consul.port=8500
spring.cloud.consul.discovery.health-check-url=http://${server.address}:${server.port}/health
spring.cloud.consul.discovery.healthCheckInterval=10s
~~~

**代码**
创建应用主类 TsfDemoConsumerApplication 。在主类中通过加入 EnableDiscoveryClient 注解开启服务注册发现功能。
~~~ Java
@SpringBootApplication
@EnableDiscoveryClient
@EnableFeignClients
public class TsfDemoConsumerApplication {

	public static void main(String[] args) {
		SpringApplication.run(TsfDemoConsumerApplication.class, args);
	}

}
~~~

定义 DemoService 接口，通过 @FeignClient 注解指定服务名来绑定服务，然后再使用 Spring MVC 的注解来绑定具体该服务提供的 REST 接口。

~~~ Java
@FeignClient("demo-provider")
public interface DemoService {

    @GetMapping("/provider")
    String provider();
}
~~~

创建应用请求处理类 DemoController 来实现对 Feign 客户端的调用。使用 @Autowired 直接注入上面定义的 DemoService 实例并在 consumer 函数中调用这个绑定了 provider 服务接口的客户端来向该服务发起 /provider 接口的调用。

~~~ Java
@RestController
public class DemoController {

    private static final Logger logger = LoggerFactory.getLogger(DemoController.class.getName());

    @Autowired
    DemoService demoService;

    @RequestMapping(value = "/consumer")
    public String consumer() {
        logger.info("consumer is being called");
        return "conumser calling ...\n" + demoService.provider();
    }
}
~~~

## 启动 Spring Boot 应用
启动 Spring Boot 应用的方式有很多种：
- 作为一个 Java 应用程序，可以直接通过运行拥有 main 函数的类来启动。
- 可以使用 spring-boot 插件来启动。执行 mvn spring-boot:run 命令。
- 使用 mvn install 将应用打成 jar 包，通过 java -jar xxx.jar 来启动应用。

通过以上三种方式中的一种方式来启动服务提供者和服务消费者。

## 验证服务间调用功能

启动服务提供者和服务消费者后，向 http://localhost:8001/consumer 发起 GET 请求，成功返回如下信息：
~~~ xml
conumser calling ...
resource providing ...
~~~





