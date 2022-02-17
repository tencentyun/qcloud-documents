## 操作场景

Netflix 开源的一系列组件（Zuul、Hystrix、Eureka、Ribbon）的配置管理使用的是自家的 [Archaius](https://github.com/Netflix/archaius)，遗憾的是 Netflix 没有开源 Archaius 的服务端，现在可以使用 Apollo 作为 Archaius 的服务端使用。

- Apollo 可以为 Netflix 微服务全家桶提供集中化的配置管理
- Archaius 可以作为 Apollo Client 的另一种选择

## 前提条件

获取 [社区 Demo >>](https://github.com/ctripcorp/apollo-use-cases/tree/master/netflix-archaius)

## 操作步骤
1. 在 Apollo 配置中心创建 AppId 为 `netflix-archaius` 的项目。
2. 在默认的 `application` 下做如下配置（可以通过文本模式直接复制、粘贴下面的内容）：

    ```properties
    hystrix.command.default.circuitBreaker.forceClosed = false
    ```
3. 运行 `com.ctrip.framework.apollo.use.cases.netflix.archaius.Application` 启动 Demo。
4. 程序会在控制台输出 hystrix.command.default.circuitBreaker.forceClosed 参数值的变化。
5. 在 Apollo 配置中心修改配置，把 `hystrix.command.default.circuitBreaker.forceClosed` 的值改为 `true` 并发布配置。
>?Archaius 默认30秒从服务端更新一次配置信息，所以需要等待30秒配置生效。
