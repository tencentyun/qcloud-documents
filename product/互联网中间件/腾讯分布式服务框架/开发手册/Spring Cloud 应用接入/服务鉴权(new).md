## 一、准备工作

开始实践服务鉴权功能前，请确保已完成了 [准备工作](https://cloud.tencent.com/document/product/649/16619)，并阅读 [服务鉴权概述](https://cloud.tencent.com/document/product/649/18024)。

## 二、快速上手

这里演示如何快速实践服务鉴权功能。假如现在有两个微服务 provider 和 consumer，想实现 consumer 调用 provider 时 provider 对请求做鉴权。

先向 provider 和 consumer 工程都添加依赖。在 `pom.xml` 中添加：

```xml
<dependency>
    <groupId>com.tencent.tsf</groupId>
    <artifactId>spring-cloud-tsf-auth</artifactId>
    <version>1.1.0-RELEASE</version>
</dependency>
```

在 provider 中启用配置项 `tsf.auth.enable`，表示对调用 provider 的请求做鉴权：

```yaml
tsf.auth.enable: true
```

- `tsf.auth.enable: true`，启动鉴权，仅通过鉴权的请求可以访问本服务。
- `tsf.auth.enable: false`，关闭鉴权，任何服务均可访问本服务。

当 provider 开启了鉴权功能，但是 consumer 未引用 `spring-cloud-tsf-auth` 依赖项时，consumer 发起的请求将收到 HTTP 返回码 403（Forbidden）。

使用 tag 鉴权涉及到业务代码和控制台两部分。启用依赖项后，还有两步工作：

* 对于 provider 而言，需要在控制台上设置 tag 鉴权规则
* 对于 consumer 而言，需要在业务代码中设置 tag 的内容

控制台上配置鉴权规则，参考 [服务鉴权](https://cloud.tencent.com/document/product/649/15549) 。

在 consumer 中设置 tag ，使用 `org.springframework.tsf.core` 包中的 `TsfContext` 类。设置 Tag 的方法签名如下：

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

其中 `Tag.ControlFlag` 决定 tag 的使用场景：

```java
public enum ControlFlag {
    TRANSITIVE,     // 表示标签要传递下去，默认不启用
    NOT_IN_AUTH,    // 表示标签不被使用在服务鉴权，默认是被使用的
    NOT_IN_ROUTE,   // 表示标签不被使用在服务路由，默认是被使用的
    NOT_IN_SLEUTH   // 表示标签不被使用在调用链，默认是被使用的
}
```

TSF 提供的 Demo `consumer-demo/src/main/java/com/tsf/demo/consumer/Controller.java` 中提供了一个设置 tag 的例子：

```java
@RequestMapping(value = "/echo-rest/{str}", method = RequestMethod.GET)
public String rest(@PathVariable String str, @RequestParam String user) {
    TsfContext.putTag("user", user); 
    return restTemplate.getForObject("http://provider-demo/echo/" + str, String.class);
}
```
