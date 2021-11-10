## 操作场景

本文介绍 [Dubbo](https://github.com/apache/incubator-dubbo) 如何通过 Apollo 配置中心实现中心化配置。


## 前提条件
获取 [社区 Demo >>](https://github.com/ctripcorp/apollo-use-cases/tree/master/dubbo)

## 操作步骤
1. 在 Apollo 配置中心创建 AppId 为 `dubbo` 的项目。
2. 在默认的 `application` 下配置 zookeeper 的地址。
	key为 `zookeeper.address`，例如：zookeeper.address = 127.0.0.1:2181。
3. 启动 zookeeper。
4. 运行 `com.ctrip.framework.apollo.use.cases.dubbo.service.Server` 启动 Demo 服务端。
5. 运行 `com.ctrip.framework.apollo.use.cases.dubbo.client.Consumer` 启动 Demo 调用端。

6. 在调用端输入任意字符后按回车，即可发起一次 Dubbo 服务请求并输出服务端的响应。
	例如：输入 `dubbo`，服务端会响应 `Hello dubbo`。
