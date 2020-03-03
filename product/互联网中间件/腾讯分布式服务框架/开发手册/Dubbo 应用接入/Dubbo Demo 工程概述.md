## 获取 Demo
- 基于 Alibaba Dubbo 版本 SDK 的 [Demo 下载](https://main.qcloudimg.com/raw/abe7f56420e98dd58cf0ef60705d7e19/tsf-dubbo-alibaba-demo.zip)
- 基于 Apache Dubbo 版本 SDK 的 [Demo 下载](https://main.qcloudimg.com/raw/2bc8fac2528b0faf58e5a614bbf73d8f/tsf-dubbo-apache-demo.zip)

## 工程目录
`tsf-dubbo-xxx-demo`的工程目录如下：
```
|- consumer-demo
|- provider-demo
|- pom.xml
```
其中 consumer-demo 表示服务消费者， provider-demo 表示服务提供者，pom.xml 中定义了工程需要的依赖包（以下以基于 Alibaba Dubbo 版本 SDK 举例说明）：
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.3.RELEASE</version>
    </parent>

    <artifactId>provider-demo</artifactId>
    <version>1.1.6-alibaba-RELEASE</version>
    <packaging>jar</packaging>
    <name>provider-demo</name>

    <properties>
        <start-class>com.tsf.demo.provider.ProviderApplication</start-class>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.6</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>com.tencent.tsf</groupId>
            <artifactId>tsf-dubbo</artifactId>
            <!-- 调整为 SDK 最新版本号 -->
            <version>1.1.6-alibaba-RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
    </dependencies>

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
关于 Maven 环境安装，请参考 Spring Cloud [SDK 下载](https://cloud.tencent.com/document/product/649/20231) 时的 Maven 配置。
