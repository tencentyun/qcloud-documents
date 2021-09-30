## 操作场景
本文介绍如何在 Spring / SpringMVC 项目下，通过 Apollo 配置中心实现动态调整日志的属性值。

## 前提条件

获取 [社区 Demo >>](https://github.com/ctripcorp/apollo-use-cases/tree/master/spring-mvc-logger)

## 操作步骤 
1. 在 Apollo 配置中心创建 AppId 为 `spring-mvc-logger` 的项目。
2. 在默认的 `application` 下做如下配置（可以通过文本模式直接复制、粘贴下面的内容）：

    ```
    apollo.setting.app.name = spring-mvc-logger
    ```
3. 在项目中的 LoggerStartupListener 监听器中设置需要动态更新的值 `appname`，并且在 logback.xml 中引用 `${appname}`。
4. 用 tomcat 启动 `spring-mvc-logger` 项目。
5. 可以看到打印日志：
    ```
    [app_name=spring-mvc-logger][timestamp=2021-03-20 13:34:45.406][level=INFO][msg=the value of the logback field from apollo, apollo.setting.app.name is spring-mvc-logger] 
    ```
5. 在 Apollo 配置中心修改配置，把 `apollo.setting.app.name` 的值改为 `newvalue` 并发布配置。
6. 可以看到打印日志已更新：
    ```
    [app_name=newvalue][timestamp=2021-03-20 13:38:23.928][level=INFO][msg=reload loggerContext , you can see that the log has been updated, new value from apollo is newvalue] 
    ```
   说明 logback.xml 中 app_name 的值随着 apollo 配置的更新而动态更新了。

>?更多信息可请参见 [GitHub 文档](https://github.com/ctripcorp/apollo/issues/2482#issuecomment-801901167)。
