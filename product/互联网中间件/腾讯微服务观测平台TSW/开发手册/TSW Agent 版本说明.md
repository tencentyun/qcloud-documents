TSW Agent 是一款基于字节码增强技术研发的 Java 应用探针，支持自动埋点完成请求上报。TSW Agent 采集的数据遵循 [Opentracing 规范](https://github.com/opentracing-contrib/opentracing-specification-zh/blob/master/semantic_conventions.md)，在 Agent 设计上，一定程度参考了开源 Skywalking 的探针设计。

>?[SkyWalking](https://github.com/apache/skywalking) 是 Apache 基金会的顶级项目，其核心是一个分布式追踪系统。Skywalking 社区活跃，技术更迭迅速，广泛兼容主流编程语言、组件与框架，为云原生微服务以及容器架构的链路追踪能力广受欢迎。

### 版本说明
| Agent版本	| 更新时间	| 更新说明 |
| ----- | ----- | ----- |
| 0.2.0	 | 2020-12-30 | 	<li>支持主流 HTTP/RPC 框架；</li><li>支持采集主流 JDBC、NoSQL 调用；</li><li>支持无侵入采集。</li>|
