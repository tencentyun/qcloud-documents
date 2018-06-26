## 一、准备工作

开始实践服务鉴权功能前，请确保已完成了 [准备工作](https://cloud.tencent.com/document/product/649/16619)，并阅读 [服务鉴权概述](https://cloud.tencent.com/document/product/649/18024)。

## 二、管理依赖项

添加 pom.xml 依赖：

```xml
<dependency>
	<groupId>com.tencent.tsf</groupId>
	<artifactId>spring-cloud-tsf-auth</artifactId>
	<version>1.0.3-RELEASE</version>
</dependency>
```



## 三、配置文件

当不配置 `tsf.auth.enable` 时，鉴权功能默认关闭。当希望开启配置功能时，添加配置项：

```yaml
tsf.auth.enable: true
```

-   `tsf.auth.enable: true`，启动鉴权，仅授权的服务可以访问本服务。
-   `tsf.auth.enable: false`，关闭鉴权，任何服务均可访问本服务。

当服务提供者开启了鉴权功能，但是服务消费者未引用 `spring-cloud-tsf-auth` 依赖项时，服务消费者调用服务提供者的接口时，将返回 HTTP 返回码 403（Forbidden）。此时应当在服务消费者的 pom.xml 文件中添加 `spring-cloud-tsf-auth` 依赖项。



## 四、Tag 鉴权开发

使用 tag 鉴权涉及到业务代码和控制台两部分。对于 **服务消费者** 而言，需要在业务代码中设置 tag 的内容；对于 **服务提供者** 而言，需要在控制台上设置 tag 鉴权规则。


### 5.1 使用 TSF SDK 记录 tag

TsfContext 是用于存放 tag 信息的上下文类。设置 Tag 的方法签名如下：

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

其中 TagControlFlag 决定 tag 的使用场景：

```java
public enum ControlFlag {
    TRANSITIVE,     // 表示标签要传递下去，默认不启用
    NOT_IN_AUTH,    // 表示标签不被使用在服务鉴权，默认是被使用的
    NOT_IN_ROUTE,   // 表示标签不被使用在服务路由，默认是被使用的
    NOT_IN_SLEUTH   // 表示标签不被使用在调用链，默认是被使用的
}
```

TSF 提供的 Demo `consumer-demo/src/main/java/com/tsf/demo/consumer/Controller.java` 中设置了键为 user，请求参数作为值的 tag。

```java
@RequestMapping(value = "/echo-rest/{str}", method = RequestMethod.GET)
public String rest(@PathVariable String str, @RequestParam String user) {
    TsfContext.putTag("user", user); 
    return restTemplate.getForObject("http://provider-demo/echo/" + str, String.class);
}
```



### 5.2 控制台配置鉴权规则

控制台上配置鉴权规则，参考 [服务鉴权](https://cloud.tencent.com/document/product/649/15549) 。

