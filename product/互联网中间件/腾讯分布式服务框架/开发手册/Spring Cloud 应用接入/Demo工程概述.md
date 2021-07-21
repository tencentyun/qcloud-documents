## 开发前准备
开发前，请确保：
1. 已下载安装了 Java 和 Maven
2. 已配置了 TSF 私服地址（参考 [SDK 下载](https://cloud.tencent.com/document/product/649/20231)）

## 获取 Demo

[Demo 下载地址 >>](https://github.com/tencentyun/tsf-simple-demo)
- release/<版本号>：对应 Spring Cloud Edgware 系列的 Demo
- release/<版本号>-finchley：对应 Spring Cloud Finchley 系列的 Demo
- release/<版本号>-greenwich：对应 Spring Cloud Greenwich 系列的 Demo

![](https://main.qcloudimg.com/raw/3ceb421e4fc1ead076ff0686558ef865.png)

## Demo 工程目录

`tsf-simple-demo`的工程目录如下：

| 工程名称	   |  工程说明   |
| ----------    |  ----------  |
| consumer-demo	            | TSF 微服务治理服务消费者 | 
| provider-demo	              | TSF 微服务治理服务提供者 | 
| msgw-demo	                  | 基于 TSF Spring Cloud MS Gateway 网关示例 | 
| opensource-zuul-demo	 | 基于开源 Zuul 的微服务网关示例 | 
| opensource-scg-demo	    | 基于开源 Spring Cloud Gateway 的微服务网关示例 | 
| rocketmq-producer	         | 支持 RocketMQ 消息队列调用链的消息生产者示例 | 
| rocketmq-consumer	        | 支持 RocketMQ 消息队列调用链的消息消费者示例 | 
| kafka-demo	                   | 支持 Kafka 调用链的示例，包含了消息消费者和生产者 |
| mongodb-demo	             | 支持 MongoDB 调用链的微服务示例 | 
| mysql-demo                  	| 支持 MySQL 调用链的微服务示例 |
| redis-demo	                   |支持 Redis 调用链的微服务示例 |
| task-schedule-demo       	| TCT 分布式任务调度示例 |

pom.xml 中定义了工程需要的依赖包（以下以基于 Spring Cloud Finchley 版本 SDK 举例说明）：

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
			xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
			<modelVersion>4.0.0</modelVersion>



			<parent>
				<groupId>com.tencent.tsf</groupId>
				<artifactId>spring-cloud-tsf-dependencies</artifactId>
				<version><!-- 调整为 SDK 长期维护（LTS）版本号 --></version>
			</parent>



			<groupId>com.tencent.tsf</groupId>
			<artifactId>tsf-demo</artifactId>
			<version><!-- 调整为 SDK 长期维护（LTS）版本号 --></version>
			<packaging>pom</packaging>



			<modules>
				<module>provider-demo</module>
				<module>consumer-demo</module>
				<module>opensource-zuul-demo</module>
				<module>rocketmq-demo</module>
				<module>mysql-demo</module>
				<module>redis-demo</module>
				<module>mongodb-demo</module>
				<module>kafka-demo</module>
				<module>msgw-demo</module>
				<module>opensource-scg-demo</module>
			</modules>



			<properties>
				<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
				<project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
				<java.version>1.8</java.version>
			</properties>



			<build>
				<plugins>
					<plugin>
						<groupId>org.springframework.boot</groupId>
						<artifactId>spring-boot-maven-plugin</artifactId>
					</plugin>
				</plugins>
			</build>
</project>


```



其中 parent 描述了不同微服务 demo 共同的 TSF 依赖。

```xml
<parent>
        <groupId>com.tencent.tsf</groupId>
        <artifactId>spring-cloud-tsf-dependencies</artifactId>
        <version><!-- 调整为 SDK 长期维护（LTS）版本号 --></version>
</parent>
```

关于 Maven 环境安装以及 TSF SDK 下载，请参考 [SDK 下载](https://cloud.tencent.com/document/product/649/20231) 和 [SDK 更新日志](https://cloud.tencent.com/document/product/649/38983) 。


## 依赖项及注解使用

1. 向工程中添加依赖。在`pom.xml`中添加以下代码：

```xml
<dependency>
    <groupId>com.tencent.tsf</groupId>
    <artifactId>spring-cloud-tsf-starter</artifactId>
    <version><!-- 调整为 SDK 长期维护（LTS）版本号 --></version>
</dependency>
```
`spring-cloud-tsf-starter` 中包含了服务注册发现、服务路由、服务鉴权、服务限流、服务熔断、服务容错、服务监控、分布式配置、调用链功能。

2. 向 Application 类中添加注解 `@EnableTsf`：

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
>!如果您使用的是 1.15.0-Edgware-RELEASE/1.15.0-Finchley-RELEASE 及之前的版本，使用方法参考 [Spring Cloud SDK 历史版本使用方法](https://cloud.tencent.com/document/product/649/45864)。
