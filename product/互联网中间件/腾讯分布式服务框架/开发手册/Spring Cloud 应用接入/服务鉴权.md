## 准备工作
开始实践服务鉴权功能前，请确保已完成了 [SDK 下载](https://cloud.tencent.com/document/product/649/20231) ，并阅读 [服务鉴权概述](https://cloud.tencent.com/document/product/649/18024)。

## 快速上手
这里演示如何快速实践服务鉴权功能。假如现在有两个微服务 provider 和 consumer，想实现 consumer 调用 provider 时，provider 对请求做鉴权。

1. 向 provider 和 consumer 工程都添加依赖。在`pom.xml`中添加以下代码：
```xml
<dependency>
    <groupId>com.tencent.tsf</groupId>
    <artifactId>spring-cloud-tsf-auth</artifactId>
    <version><!-- 调整为 SDK 最新版本号 --></version>
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

此时您已经对 provider 微服务开启了鉴权功能，任何到达 provider 的请求都会被鉴权，鉴权不通过时会返回 HTTP 403 Forbidden。

TSF 提供了两种类型的鉴权能力，一种根据调用方服务名鉴权，一种根据调用方设置的 tag 鉴权。在控制台上可以配置相应的规则。如果在控制台上对 provider 启用了鉴权功能，并且配置了至少一条规则，那么调用 provider 的微服务（如 comsumer）也需要引入`spring-cloud-tsf-auth`的依赖并且加上`@EnableTsfAuth`注解，否则到 provider 的请求会被返回 HTTP 403 Forbidden。

如果请求双方想使用基本 tag 的鉴权规则，那么：

* 对于 provider 而言，需要在控制台上设置 tag 鉴权规则。
* 对于 consumer 而言，需要在业务代码中设置 tag 的内容。

控制台上配置鉴权规则，参考 [服务鉴权基本操作](https://cloud.tencent.com/document/product/649/15549) 。

在 consumer 中设置 tag ，使用`org.springframework.tsf.core`包中的`TsfContext`类。设置 Tag 的方法签名如下：

```java
/**
 * 设置多个 tag。如果有某个 tag 之前已经被设置过，那么它的值会被覆盖。
 */
public static void putTags(Map<String, String> tagMap, Tag.ControlFlag... flags) {}

/**
 * 设置单个 tag。如果该 key 之前已经被设置过，那么它的值会被覆盖。
 */
public static void putTag(String key, String value, Tag.ControlFlag... flags) {}
```

其中`flags`决定 tag 的使用场景，如果您没有特殊需要，不传即可：

```java
public enum ControlFlag {
    TRANSITIVE,     // 表示标签要传递下去，默认不启用。
    NOT_IN_AUTH,    // 表示标签不被使用在服务鉴权，默认是被使用的。
    NOT_IN_ROUTE,   // 表示标签不被使用在服务路由，默认是被使用的。
    NOT_IN_SLEUTH   // 表示标签不被使用在调用链，默认是被使用的。
}
```

TSF 提供的 Demo`consumer-demo/src/main/java/com/tsf/demo/consumer/Controller.java`中提供了一个设置 tag 的例子：

```java
@RequestMapping(value = "/echo-rest/{str}", method = RequestMethod.GET)
public String rest(@PathVariable String str, @RequestParam String user) {
    TsfContext.putTag("user", user); 
    return restTemplate.getForObject("http://provider-demo/echo/" + str, String.class);
}
```
