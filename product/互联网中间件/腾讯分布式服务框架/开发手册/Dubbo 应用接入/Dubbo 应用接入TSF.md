## 操作场景
TSF 为其他应用提供服务注册中心，Dubbo 应用可通过依赖 jar 包的方式接入该项服务。本文档介绍 Dubbo 应用从接入TSF 到部署应用的操作方法及相关注意事项。

## 操作步骤
#### 1. Maven 环境安装
详细操作请参考 [Maven 安装](https://cloud.tencent.com/document/product/649/20231#2.-.E5.AE.89.E8.A3.85-maven)。

#### 2. 注册中心配置
Dubbo 官网 Demo：
```xml
<dubbo:registry address="multicast://224.5.6.7:1234"/>
```

TSF Demo（**注册中心地址使用注册中心IP和端口替换**）：
```xml
<dubbo:registry address="tsfconsul://注册中心地址:端口"/>
```
> ?协议名为 tsfconsul。

#### 3. 添加依赖
根据业务使用的对应的 TSF Dubbo 版本 SDK 如下： 
- TSF Alibaba Dubbo 版本的 SDK： 
```xml
<dependency>
  <groupId>com.tencent.tsf</groupId>
  <artifactId>tsf-dubbo</artifactId>
  <!-- 修改为对应的版本号 -->
  <version>1.1.6-alibaba-RELEASE</version>
</dependency>
```

- TSF Apache Dubbo 版本的 SDK：
```xml
<dependency>
  <groupId>com.tencent.tsf</groupId>
  <artifactId>tsf-dubbo</artifactId>
  <!-- 修改为对应的版本号 -->
  <version>1.1.6-apache-RELEASE</version>
</dependency>
```
> ?当当网的 Dubbox 的部分功能可能不支持。

#### 4. 打包 FATJAR
和 Spring Boot 结合的时候，您可以通过 **spring-boot-maven-plugin** 构建一个包含所有依赖的 jar 包（FatJar），执行命令`mvn clean package`。
详情请参考 [Dubbo Demo 工程概述](https://cloud.tencent.com/document/product/649/35577)。

## Dubbo 兼容说明
- TSF 提供服务注册中心，Dubbo 应用通过依赖 jar 包的方式使用。
- TSF 支持 Dubbo 应用的 Dubbo 服务注册、Dubbo 服务调用、调用链、监控。
- Dubbo 应用的其他能力（如 filter 机制），可以继续使用。
- TSF 平台提供的服务限流、鉴权、路由功能目前只支持基于 Spring Cloud 和 Service Mesh 框架开发的应用。

## 常见错误
部分包对版本有要求，如果发生**包冲突**，请尝试主动依赖以下版本：
 ```xml
 <dependency>
  <groupId>com.ecwid.consul</groupId>
  <artifactId>consul-api</artifactId>
  <version>1.4.2</version>
</dependency>
  
<dependency>
  <groupId>io.zipkin.brave</groupId>
  <artifactId>brave</artifactId>
  <version>5.4.3</version>
</dependency>s
```
