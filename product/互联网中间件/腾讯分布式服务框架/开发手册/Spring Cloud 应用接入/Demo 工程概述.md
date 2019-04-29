## 获取 Demo

- 基于 Spring Cloud Edgware 版本 SDK 的 [Demo 下载 >> ](https://main.qcloudimg.com/raw/a3e2ddbf8bea79631d64986f72a7f083/tsf-demo-simple-1.12.2-Edware.zip) 
- 基于 Spring Cloud Finchley 版本 SDK 的 [Demo 下载 >> ](https://main.qcloudimg.com/raw/d26190f5a5a2f6e7f9c57ef47142c6b9/tsf-demo-simple-develop_1.12.2-finchley.zip) 

## 工程目录

`tsf-simple-demo`的工程目录如下：

```
|- consumer-demo
|- provider-demo
|- pom.xml
```

其中 consumer-demo 表示服务消费者， provider-demo 表示服务提供者。
pom.xml 中定义了工程需要的依赖包（以下以基于 Spring Cloud Finchley 版本 SDK 举例说明）：

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.tencent.tsf</groupId>
        <artifactId>spring-cloud-tsf-dependencies</artifactId>
        <version><!-- 调整为 SDK 最新版本号 --></version>
    </parent>

	<groupId>com.tsf.demo</groupId>
	<artifactId>tsf-demo</artifactId>
	<version>1.12.0-Finchley-RELEASE</version>
	<packaging>pom</packaging>

	<modules>
		<module>provider-demo</module>
		<module>consumer-demo</module>
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

其中 parent 描述了`provider-demo`和`consumer-demo`共同的 TSF 依赖。

```xml
<parent>
        <groupId>com.tencent.tsf</groupId>
        <artifactId>spring-cloud-tsf-dependencies</artifactId>
        <version><!-- 调整为 SDK 最新版本号 --></version>
</parent>
```

关于 Maven 环境安装以及 TSF SDK 下载，请参考 [SDK 下载](https://cloud.tencent.com/document/product/649/20231) 和 [SDK 更新日志](https://cloud.tencent.com/document/product/649/20230) 。

## Demo 功能

- [服务注册与发现]( https://cloud.tencent.com/document/product/649/16617)
- [分布式配置](https://cloud.tencent.com/document/product/649/16620)
- [服务鉴权](https://cloud.tencent.com/document/product/649/16621)
- [服务限流](https://cloud.tencent.com/document/product/649/19019)
- [参数传递](https://cloud.tencent.com/document/product/649/18511)
- [调用链](https://cloud.tencent.com/document/product/649/16622)
