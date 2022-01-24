本文介绍 Java 自研探针上报方式如何关联 TraceID 。

## 操作步骤
1. 修改探针配置文件 tapm.properties。
```
 #日志追溯相关 Plugin，开启后可以在应用的日志中，打印 APM 相关数据，如应用 ID、 TraceID 等。
class_transformer.tapm-log4j-plugin-2.0.0.enabled=true
class_transformer.tapm-log4j-plugin-2.3.enabled=true
class_transformer.tapm-log4j-plugin-1.2.enabled=true
class_transformer.tapm-logback-plugin-1.2.enabled=true
```

2. 修改 logback-spring.xml 中的 Appender 的 Pattern 格式。
```
<encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder">
   <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%R] [%thread] %-5level %logger{50} - %msg%n</pattern>
   <charset>utf8</charset>
</encoder>
```

>? [%R] 负责输出请求的 ` NBS.REQUEST_GUID`，配置后日志会增加 `NBS.REQUEST_GUID ` 信息。在整个请求链路中，入口事务生成的  `NBS.REQUEST_GUID`  将作为整个请求链路的唯一标识，此值将在链路中不断传递直到链路的最后请求（无法实现跨应用追踪的组件的情况除外），以实现全链路追踪。调用链所涉及的各个应用的日志都显示同一个 `NBS.REQUEST_GUID` 。

3. 启动项目，打印结果如下：
   %R 会打印 TraceID，当有请求调用时，会显示 `NBS.REQUEST_GUID:traceID`，即表示 TraceID 注入成功。
   ![](https://qcloudimg.tencent-cloud.cn/raw/31b463a00bbf97d8dfd86b73648223ed.png)
>?上图中，` NBS.REQUEST_GUID` 后的字符串为 TraceID，即 TraceID：ffde4e5b09a36187。
