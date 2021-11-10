[Apache Dubbo](http://dubbo.apache.org/) 是一款高性能、轻量级的开源 Java RPC 框架，提供了三大核心能力：面向接口的远程方法调用，智能容错和负载均衡，以及服务自动注册和发现。

## 部署示例

在下面的例子中，我们将部署一套基于 Dubbo 的微服务，包含以下组件：

- 服务提供方（hello-world-provider），使用 CloudBase 云托管部署；
- 服务消费方（hello-world-provider），使用 CloudBase 云托管部署；
- 注册中心（nacos），使用腾讯云 CVM 部署。

## 部署流程
以下所有涉及的 CVM 实例、云托管实例，都处于同一个 VPC 内。您可以在云托管详情内看到您的应用所属的 VPC。

### 步骤1：部署注册中心

在您的 CVM 实例内安装并启动 Nacos，详情请参见 [Nacos 文档](https://nacos.io/zh-cn/docs/quick-start.html)。

### 步骤2：创建服务提供方

1. 创建 Maven 项目，在 `pom.xml` 文件中添加依赖：
<dx-codeblock>
:::  xml
<dependencies>
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter</artifactId>
    <version>1.5.12.RELEASE</version>
  </dependency>
  <dependency>
    <groupId>org.apache.dubbo</groupId>
    <artifactId>dubbo-registry-nacos</artifactId>
    <version>2.7.3</version>
  </dependency>
  <dependency>
    <groupId>org.apache.dubbo</groupId>
    <artifactId>dubbo-spring-boot-starter</artifactId>
    <version>2.7.3</version>
  </dependency>
  <dependency>
    <groupId>com.alibaba.nacos</groupId>
    <artifactId>nacos-client</artifactId>
    <version>1.1.1</version>
  </dependency>
  <dependency>
    <groupId>org.apache.dubbo</groupId>
    <artifactId>dubbo</artifactId>
    <version>2.7.3</version>
  </dependency>
</dependencies>
:::
</dx-codeblock>
2. 在 `src/main/java` 路径下新建 `com.cloudrun.dubbo.inface`，然后创建一个接口 `IHelloService`：
<dx-codeblock>
:::  java
package com.cloudrun.dubbo.inface;

public interface IHelloService {
  String sayHello(String str);
}

:::
</dx-codeblock>
3. 在 `src/main/java` 路径下新建 `com.cloudrun.dubbo.provider`，创建一个类 `IHelloServiceImpl`，实现此接口：
<dx-codeblock>
:::  java
package com.cloudrun.dubbo.provider;

import com.cloudrun.dubbo.inface.IHelloService;

public class HelloServiceImpl implements IHelloService {

  @Override
  public String sayHello(String str) {
    return "hello " + str;
  }
}
:::
</dx-codeblock>
4. 在 `src/main/resources` 路径下创建 `provider.xml` 文件，配置 Dubbo 服务：
<dx-codeblock>
:::  xml
<beans
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:dubbo="http://dubbo.apache.org/schema/dubbo"
  xmlns="http://www.springframework.org/schema/beans"
  xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-4.3.xsd http://dubbo.apache.org/schema/dubbo http://dubbo.apache.org/schema/dubbo/dubbo.xsd"
>

  <dubbo:application name="hello-world-provider" />

  <!-- port 为您的服务端口 -->
  <dubbo:protocol name="dubbo" port="{port}" />

  <dubbo:service interface="com.cloudrun.dubbo.inface.IHelloService" ref="helloService" />

  <bean id="helloService" class="com.cloudrun.dubbo.provider.IHelloServiceImpl" />

  <!-- nacos-ip 为您的nacos地址 -->
  <dubbo:registry address="nacos://{nacos-ip}:8848" />
</beans>
:::
</dx-codeblock>
5. 在 `com.cloudrun.dubbo` 新建 `dubbo` 服务启动类 `ProviderApplication`：
<dx-codeblock>
:::  java
package com.cloudrun.dubbo;

import org.apache.dubbo.config.spring.context.annotation.DubboComponentScan;
import org.apache.dubbo.config.spring.context.annotation.EnableDubbo;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.context.annotation.ImportResource;

@EnableAutoConfiguration
@EnableDubbo
@ImportResource("classpath:provider.xml")
@DubboComponentScan(basePackages = "com.cloudrun")
public class ProviderApplication {

  public static void main(String[] args) {
    SpringApplication.run(ProviderApplication.class, args);
  }
}
:::
</dx-codeblock>
6. 在 `pom.xml` 文件中添加应用编译配置：
<dx-codeblock>
:::  xml
<build>
  <plugins>
    <plugin>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-maven-plugin</artifactId>
      <executions>
        <execution>
          <goals>
            <goal>repackage</goal>
          </goals>
          <configuration>
            <classifier>boot</classifier>
            <mainClass>com.cloudrun.dubbo.ProviderApplication</mainClass>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
:::
</dx-codeblock>
7. 然后运行以下命令，将本地项目构建为可执行的 jar 包：
<dx-codeblock>
:::  sh
mvn clean package
:::
</dx-codeblock>


### 步骤3：部署服务提供方

1. 开通 CloudBase 云托管，创建服务 `hello-world-provider`，然后创建一个版本：
<img src = "https://main.qcloudimg.com/raw/ac4b8d0b851f375ec13c0beeab36e149.png" style="width: 80%"> 
2. 部署成功后，登录 nacos 控制台 `http://${nacos-ip}:8848`，在左侧导航栏中单击服务列表，查看提供者列表。可以看到服务提供者里已经包含了 `com.cloudrun.dubbo.inface.IHelloService`，且可以查询该服务的服务分组和提供者 IP：
![](https://main.qcloudimg.com/raw/fd6ef566091da7d517b8e22937529d23.png)

### 步骤4：创建服务消费方
1. 创建 Maven 项目，在 `pom.xml` 文件中添加依赖：
<dx-codeblock>
:::  xml
<dependencies>
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <version>1.5.12.RELEASE</version>
  </dependency>
  <dependency>
    <groupId>org.apache.dubbo</groupId>
    <artifactId>dubbo-registry-nacos</artifactId>
    <version>2.7.3</version>
  </dependency>
  <dependency>
    <groupId>org.apache.dubbo</groupId>
    <artifactId>dubbo-spring-boot-starter</artifactId>
    <version>2.7.3</version>
  </dependency>
  <dependency>
    <groupId>com.alibaba.nacos</groupId>
    <artifactId>nacos-client</artifactId>
    <version>1.1.1</version>
  </dependency>
  <dependency>
    <groupId>org.apache.dubbo</groupId>
    <artifactId>dubbo</artifactId>
    <version>2.7.3</version>
  </dependency>
</dependencies>
:::
</dx-codeblock>
2. 在 `src/main/java` 路径下新建 `com.cloudrun.dubbo.inface`，然后创建一个接口 `IHelloService`：
<dx-codeblock>
:::  java
package com.cloudrun.dubbo.inface;

public interface IHelloService {
  String sayHello(String str);
}
:::
</dx-codeblock>
3. 在 `src/main/java` 路径下创建 `com.cloudrun.dubbo.controller`，然后创建类 `SayHelloController`：
<dx-codeblock>
:::  java
package com.cloudrun.controller;

import com.cloudrun.dubbo.inface.IHelloService;
import org.apache.dubbo.config.annotation.Reference;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SayHelloController {

  @Reference
  private IHelloService helloService;

  @GetMapping("/")
  public String sayHello(String word) {
    return helloService.sayHello(word);
  }
}

:::
</dx-codeblock>
4. 在 `com.cloudrun` 下创建启动类 `ConsumerApplication`：
<dx-codeblock>
:::  java
package com.cloudrun;

import org.apache.dubbo.config.spring.context.annotation.DubboComponentScan;
import org.apache.dubbo.config.spring.context.annotation.EnableDubbo;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ImportResource;

@SpringBootApplication
@EnableDubbo
@ImportResource("classpath:consumer.xml")
@DubboComponentScan(basePackages = "com.cloudrun")
public class ConsumerApplication {

  public static void main(String[] args) {
    SpringApplication.run(ConsumerApplication.class, args);
  }
}
:::
</dx-codeblock>
5. 在 `src/main/resources` 路径下创建 `consumer.xml` 文件，配置 `dubbo` 服务：
<dx-codeblock>
:::  XML
<beans xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:dubbo="http://dubbo.apache.org/schema/dubbo"
       xmlns="http://www.springframework.org/schema/beans"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-4.3.xsd http://dubbo.apache.org/schema/dubbo http://dubbo.apache.org/schema/dubbo/dubbo.xsd">

  <dubbo:application name="hello-world-consumer"/>

  <!-- port 为您的服务端口 -->
  <dubbo:protocol name="dubbo" port="{port}"/>

  <dubbo:reference id="helloService" interface="com.cloudrun.dubbo.inface.IHelloService"/>

  <!-- nacos-ip 为您的nacos地址 -->
  <dubbo:registry address="nacos://{nacos-ip}:8848" />
</beans>
:::
</dx-codeblock>
6. 在 `src/main/resources` 路径下创建 `application.properties` 文件，配置服务端口：
<dx-codeblock>
:::  properties
server.port=8081
:::
</dx-codeblock>
7. 在 `pom.xml` 文件中添加应用编译配置：
<dx-codeblock>
:::  xml
<build>
  <plugins>
    <plugin>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-maven-plugin</artifactId>
      <executions>
        <execution>
          <goals>
            <goal>repackage</goal>
          </goals>
          <configuration>
            <classifier>boot</classifier>
            <mainClass>com.cloudrun.ConsumerApplication</mainClass>
          </configuration>application.properties
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
:::
</dx-codeblock>
8. 并执行 `mvn clean package` 将本地的程序打成可执行的 `jar` 包。

### 步骤5：部署服务消费方

1. 创建一个新的云托管服务 `hello-world-consumer`，然后创建一个版本：
<img src = "https://main.qcloudimg.com/raw/848a39e405597c4090a3797ee98fc6a8.jpg" style="width: 80%"> 
2. 登录 nacos 控制台 `http://${nacos-ip}:8848`，在左侧导航栏中单击**服务列表**，查看提供者列表。可以看到服务提供者里已经包含了 `com.cloudrun.dubbo.inface.IHelloService` 的消费者，且可以查询该服务的**服务分组**和**提供者 IP**：
![](https://main.qcloudimg.com/raw/aadb6cb0b43a3337fda3ee540ce7d6cd.jpg)
3. 然后设置服务消费者的公网 HTTP 访问路径：
![](https://qcloudimg.tencent-cloud.cn/raw/a2f56b6a7c8ef216d8c52b5142c650ff.jpg)

## 验证服务

浏览器访问上图中的 HTTP 地址：
![](https://qcloudimg.tencent-cloud.cn/raw/83f4c2c0254be5ec1760d27c84278d90.jpg)

