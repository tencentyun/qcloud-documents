## 操作场景
本文介绍 [Spring Boot Logging](https://docs.spring.io/spring-boot/docs/current/reference/html/howto-logging.html) 如何通过 Apollo 配置中心实现动态调整 Logging Level。

## 前提条件

获取 [社区 Demo >>](https://github.com/ctripcorp/apollo-use-cases/tree/master/spring-boot-logger)


## 操作步骤
1. 在 Apollo 配置中心创建 AppId 为 `spring-boot-logger` 的项目。
2. 在默认的 `application` 下做如下配置（可以通过文本模式直接复制、粘贴下面的内容）：

    ```properties
    logging.level.com.ctrip.framework.apollo.use.cases.spring.boot.logger = warn
    ```
3. 运行 `com.ctrip.framework.apollo.use.cases.spring.boot.logger.Application` 启动 Demo。
4. 程序只会持续打印 error 级别日志。
5. 在 Apollo 配置中心修改配置，把 `logging.level.com.ctrip.framework.apollo.use.cases.spring.boot.logger` 的值改为 `debug` 并发布配置。
6. 程序输出 debug、info、warn、error 等级别日志，说明动态调整 Logging Level 生效了。

>?更多信息请参见 [spring boot动态调整线上日志级别](http://www.kailing.pub/article/index/arcid/189.html)。
