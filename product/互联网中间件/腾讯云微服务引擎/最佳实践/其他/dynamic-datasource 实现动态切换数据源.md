## 操作场景

本文介绍 [Spring Boot默认的HikariCP DataSource](https://github.com/brettwooldridge/HikariCP) 如何通过 Apollo 配置中心实现动态切换数据源（其它类型的 DataSource 也是类似的，可以参考本文步骤）。

## 前提条件

获取 [社区 Demo >>](https://github.com/ctripcorp/apollo-use-cases/tree/master/dynamic-datasource)

## 操作步骤
1. 创建 test1 数据库，导入 test1.sql。
2. 创建 test2 数据库，导入 test2.sql。
3. 在 Apollo 配置中心创建 AppId 为 `dynamic-datasource` 的项目。
4. 在默认的 `application` 下做如下配置（按照实际的数据库连接信息填写）：

    ```properties
    spring.datasource.url = jdbc:mysql://127.0.0.1:3306/test1?autoReconnect=true&useUnicode=true&characterEncoding=utf-8
    spring.datasource.username = xxx-user
    spring.datasource.password = xxx-password
    # hikari specific settings
    spring.datasource.hikari.maximumPoolSize = 1
    ```
5. 运行 `com.ctrip.framework.apollo.use.cases.dynamic.datasource.Application` 启动 Demo。
6. 程序启动后会持续打印 kl。
7. 在 Apollo 配置中心修改配置，把 `spring.datasource.url` 的值切换到 `test2` 并发布配置。
8. 程序会持续打印 ckl，说明动态切换数据源已生效。


>?更多信息请参见 [Apollo 应用之动态调整线上数据源（DataSource）](http://www.kailing.pub/article/index/arcid/198.html)。
