## 操作场景

本文介绍 [Spring Cloud Gateway](https://cloud.spring.io/spring-cloud-static/spring-cloud-gateway/2.0.3.RELEASE/single/spring-cloud-gateway.html) 如何通过 Apollo 配置中心实现动态路由。

## 前提条件

获取 [社区 Demo >>](https://github.com/ctripcorp/apollo-use-cases/tree/master/spring-cloud-gateway)

## 操作步骤
1. 在 Apollo 配置中心创建 AppId 为 `spring-cloud-Gateway` 的项目。
2. 在默认的 `application` 下做如下配置（可以通过文本模式直接复制、粘贴下面的内容）：

    ```properties
    server.port = 9090
    spring.cloud.gateway.routes[0].id = github_route
    spring.cloud.gateway.routes[0].uri = https://github.com/
    #spring.cloud.gateway.routes[0].uri = https://github.com/ctripcorp/apollo
    spring.cloud.gateway.routes[0].predicates[0] = Path=/**
    ```
3. 运行 `com.ctrip.framework.apollo.use.cases.spring.cloud.gateway.SpringCloudGatewayApplication` 启动 Demo。
4. 打开 `http://localhost:9090`，显式内容为 GitHub 首页。 
5. 在 Apollo 配置中心修改配置，把 `spring.cloud.gateway.routes[0].uri` 的值改为 `https://github.com/ctripcorp/apollo` 并发布配置。
  例如：可以以文本模式在原来生效的 `spring.cloud.gateway.routes[0].uri` 前面加上 `#` 注释掉，同时把原来注释掉的指向 `https://github.com/ctripcorp/apollo` 的配置反注释掉来快速修改。
6. 刷新 `http://localhost:9090` 页面，显式的内容会变成 Apollo 配置中心的 GitHub 首页，说明动态路由已生效。
7. 如果浏览器缓存影响测试，可以配置 `actuator` 使用 `org.springframework.cloud.gateway.actuate.GatewayControllerEndpoint` 提供的端点查看路由配置。
