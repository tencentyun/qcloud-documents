本文档仅适用于使用 `1.15.0-Edgware-RELEASE` / `1.15.0-Finchley-RELEASE` 和之前版本的 SDK。参考使用 `1.14.2-Finchley-RELEASE` 的 [Demo](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/demo/tsf-demo-simple-_1.14.2-finchley.zip) 了解全部依赖项及注解使用方法。

### 服务鉴权
1. 向 provider 和 consumer 工程都添加依赖。在`pom.xml`中添加以下代码：
```xml
<dependency>
    <groupId>com.tencent.tsf</groupId>
    <artifactId>spring-cloud-tsf-auth</artifactId>
    <version><!-- 调整为历史版本 SDK 版本号 --></version>
</dependency>
```

2. 向 Application 类中添加注解`@EnableTsfAuth`：
```java
// 下面省略了无关的代码
import org.springframework.tsf.auth.annotation.EnableTsfAuth;
@SpringBootApplication
@EnableTsfAuth
public class ProviderApplication {
	public static void main(String[] args) {
		SpringApplication.run(ProviderApplication.class, args);
  }
}
```

### 服务限流
如果用户要对某个服务开启限流的能力，即对调用它的请求做限流，可以按下面的步骤打开限流开关。

1. 向工程中添加依赖。在`pom.xml`中添加以下代码：
```xml
<dependency>
    <groupId>com.tencent.tsf</groupId>
    <artifactId>spring-cloud-tsf-ratelimit</artifactId>
    <version><!-- 调整为历史版本 SDK 版本号 --></version>
</dependency>
```

2. 向 Application 类中添加注解`@EnableTsfRateLimit`：
```java
// 下面省略了无关的代码
import org.springframework.tsf.ratelimit.annotation.EnableTsfRateLimit;
@SpringBootApplication
@EnableTsfRateLimit
public class ProviderApplication {
	public static void main(String[] args) {
		SpringApplication.run(ProviderApplication.class, args);
	}
}
```

### 服务路由

1. 向工程中添加依赖。在 `pom.xml` 中添加以下代码：
```xml
<dependency>
    <groupId>com.tencent.tsf</groupId>
    <artifactId>spring-cloud-tsf-route</artifactId>
    <version><!-- 调整为历史版本 SDK 版本号 --></version> 
</dependency>
```
2. 向 Application 类中添加注解 `@EnableTsfRoute`：
```java
// 下面省略了无关的代码
import org.springframework.cloud.tsf.route.annotation.EnableTsfRoute;
@SpringBootApplication
@EnableTsfRoute
public class ProviderApplication {
	public static void main(String[] args) {
		SpringApplication.run(ProviderApplication.class, args);
	}
}
```

### 分布式配置

添加 pom.xml 依赖：
```xml
<dependency>
  <groupId>com.tencent.tsf</groupId>
  <artifactId>spring-cloud-tsf-consul-config</artifactId>
  <version><!-- 调整为历史版本 SDK 版本号 --></version>
</dependency>
 <!-- 1.12.0之前（不包含1.12.0）版本 SDK，使用分布式配置自动刷新功能时，要添加 actuator 的依赖包
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
-->
```

### 调用链

添加 pom.xml 依赖：
```xml
<dependency>
	<groupId>com.tencent.tsf</groupId>
	<artifactId>spring-cloud-tsf-sleuth</artifactId>
	<version><!-- 调整为历史版本 SDK 版本号 --></version>
</dependency>
```

### 服务监控

#### Edgware 版本 SDK 相关设置
向工程中添加依赖。在`pom.xml`中添加以下代码：
```xml
<dependency>
    <groupId>com.tencent.tsf</groupId>
    <artifactId>spring-cloud-tsf-monitor</artifactId>
    <version><!-- 调整为历史版本 SDK 版本号 --></version>
</dependency>
```

#### Finchley 版本 SDK 相关设置
1. 向工程中添加依赖。在`pom.xml`中添加以下代码，**依赖的是`spring-cloud-tsf-sleuth`**而不是`spring-cloud-tsf-monitor`。
   ```xml
   <dependency>
       <groupId>com.tencent.tsf</groupId>
       <artifactId>spring-cloud-tsf-sleuth</artifactId>
       <version><!-- 调整为历史版本 SDK 版本号 --></version>
   </dependency>
   ```

2. 向 Application 类中添加注解`@EnableTsfMonitor`：
   ```java
   // 下面省略了无关的代码
   import com.tencent.tsf.monitor.annotation.EnableTsfMonitor;
   @SpringBootApplication
   @EnableTsfMonitor
   public class ProviderApplication {
   	public static void main(String[] args) {
   		SpringApplication.run(ProviderApplication.class, args);
   	}
   }
   ```

### API 注册

在 pom.xml 中添加以下代码：
```xml
<dependency>
    <groupId>com.tencent.tsf</groupId>
    <artifactId>spring-cloud-tsf-swagger</artifactId> 
    <version><!-- 调整为历史版本 SDK 版本号 --></version>
    <scope>compile</scope>
</dependency>
```
添加依赖包后，TSF API 注册功能即生效。

