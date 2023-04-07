## 准备工作

在开始开发前，请确保您已经参见 [下载 Maven](https://cloud.tencent.com/document/product/649/20231) 下载安装了 Java 和 Maven，并且配置了 TSF 私服地址。


## 下载 Demo

[Demo 下载地址](https://github.com/tencentyun/tsf-simple-demo)。

- release/<版本号>：对应 Spring Cloud Edgware 系列的 Demo
- release/<版本号>-finchley：对应 Spring Cloud Finchley 系列的 Demo
- release/<版本号>-greenwich：对应 Spring Cloud Greenwich 系列的 Demo
- release/<版本号>-hoxton-higher：对应 Spring Cloud Hoxton Higher 系列的 Demo
- release/<版本号>-springcloud2020：对应 Spring Cloud 2020 系列的 Demo
- release/<版本号>-springcloud2021：对应 Spring Cloud 2021 系列的 Demo

![](https://main.qcloudimg.com/raw/3ceb421e4fc1ead076ff0686558ef865.png)

### Demo 目录介绍

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
<dx-codeblock>
:::  xml
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

:::
</dx-codeblock>
其中 parent 描述了不同微服务 demo 共同的 TSF 依赖。
<dx-codeblock>
:::  xml
<parent>
        <groupId>com.tencent.tsf</groupId>
        <artifactId>spring-cloud-tsf-dependencies</artifactId>
        <version><!-- 调整为 SDK 长期维护（LTS）版本号 --></version>
</parent>
:::
</dx-codeblock>
<dx-alert infotype="explain" title="">
SDK 长期维护（LTS）版本号请参见 [Spring Cloud 概述 > SDK 版本说明](https://cloud.tencent.com/document/product/649/36285#SDKexplain)。
</dx-alert>





## 依赖构建及注解使用

> !如果您使用的是 1.15.0-Edgware-RELEASE/1.15.0-Finchley-RELEASE 及之前的版本，使用方法参见 [Spring Cloud SDK 历史版本使用方法](https://cloud.tencent.com/document/product/649/45864)。

1. 向工程中添加依赖。在`pom.xml`中添加以下代码：
<dx-codeblock>
:::  xml
<dependency>
    <groupId>com.tencent.tsf</groupId>
    <artifactId>spring-cloud-tsf-starter</artifactId>
    <version><!-- 调整为 SDK 长期维护（LTS）版本号 --></version>
</dependency>
:::
</dx-codeblock>
`spring-cloud-tsf-starter` 中包含了服务注册发现、服务路由、服务鉴权、服务限流、服务熔断、服务容错、服务监控、分布式配置、调用链功能。
2. 向 Application 类中添加注解 `@EnableTsf`：
<dx-codeblock>
:::  java
// 下面省略了无关的代码
import org.springframework.tsf.annotation.EnableTsf;
@SpringBootApplication
@EnableTsf
public class ProviderApplication {
    public static void main(String[] args) {
        SpringApplication.run(ProviderApplication.class, args);
    }
}
:::
</dx-codeblock>

>!
>
>TSF 各部分功能对应的注解如下，不推荐只单独用部分的注解，建议添加 @EnableTsf 注解可以开启 TSF 全部功能，
>
>- @EnableTsfUnit // 单元化
>- @EnableTsfAuth // 服务鉴权
>- @EnableTsfRoute // 服务路由
>- @EnableTsfRateLimit // 服务限流
>- @EnableTsfSleuth // 调用链
>- @EnableTsfMonitor // 服务监控
>- @EnableTsfCircuitBreaker // 服务熔断
>- @EnableTsfFaultTolerance // 服务容错
>- @EnableTsfLane //泳道



