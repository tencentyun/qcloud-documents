## 操作场景

本文介绍如何通过 Java Agent 技术无缝集成 Apollo 配置中心，典型使用场景如：

- 有些配置已经打到 jar 包里了，而源码不方便修改
- 不想改动项目代码直接集成 Apollo

>?通过 Java Agent 的偷懒方式有缺陷，很难使用到配置变更动态生效功能，本文仅提供场景实例思路，建议您按照官方 wiki 的方式正确接入。


## 前提条件
获取 [社区 Demo >>](https://github.com/ctripcorp/apollo-use-cases/tree/master/spring-boot-agent)

## 操作步骤

1. 在 Apollo 配置中心创建 AppId为 `spring-boot-agent` 的项目。
2. 在默认的 `application` 下做如下配置（可以通过文本模式直接复制、粘贴下面的内容）：
    ```properties
    test.input = 666
    ```
3. 运行 `com.ctrip.framework.apollo.use.cases.agent.Application` 启动 Demo，程序会打印 application.properties 配置的 `888`。
4. 编译 apollo-agent 模块，得到 apollo-agent-1.0-SNAPSHOT.jar，然后在 VM options 中，添加如下 javaagent 配置：
   ```plaintext
   -javaagent:xxx\apollo-agent-1.0-SNAPSHOT.jar
   -Ddev_meta=http://127.0.0.1:8801
   -Denv=DEV
   -Dapp.id=spring-boot-agent
   ```
   javaagent 需要自行替换 apollo-agent-1.0-SNAPSHOT.jar 的决定路径。
5. 重新运行 `com.ctrip.framework.apollo.use.cases.agent.Application` 启动 Demo，即可输出 Apollo 中配置的 `666`。
