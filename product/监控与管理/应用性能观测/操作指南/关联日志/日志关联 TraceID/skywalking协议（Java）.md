本文将介绍 Java skywalking 上报方式如何关联 TraceID 。

## 操作步骤

1. 引入依赖。
```
<dependency>
      <groupId>org.apache.skywalking</groupId>
      <artifactId>apm-toolkit-logback-1.x</artifactId>
      <version>8.3.0</version>
</dependency>
```

2. 修改 logback-spring.xml 中的 Appender 的 Pattern 格式。
```
<encoder class="ch.qos.logback.core.encoder.LayoutWrappingEncoder">
    <layout class="org.apache.skywalking.apm.toolkit.log.logback.v1.x.TraceIdPatternLogbackLayout">
        <Pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%tid] [%thread] %-5level %logger{36} -%msg%n</Pattern>
    </layout>
</encoder>
```


3. 启动项目，打印结果如下：
   %tid 会打印 TraceID，默认 TID：N/A，当有请求调用时，会显示 TraceID。
   ![](https://qcloudimg.tencent-cloud.cn/raw/2cd5459ad4e805d6d0d525de6894151d.png)

