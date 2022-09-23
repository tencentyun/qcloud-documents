本文将介绍 Java skywalking 上报方式如何关联 TraceID 。

## 操作步骤

### 配置 Logback 输出 TraceID 

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

### 配置 log4j-1x 输出 TraceID 
1. 通过 maven 或 gradle 引入 toolkit 依赖。
```
<dependency>
<groupId>org.apache.skywalking</groupId>
<artifactId>apm-toolkit-log4j-1.x</artifactId>
<version>{project.release.version}</version>
</dependency>
```
2. 修改 log4j1.properties 配置 layout。
```
log4j.appender.CONSOLE.layout=org.apache.skywalking.apm.toolkit.log.log4j.v1.x.TraceIdPatternLayout
```
在 `layout.ConversionPattern` 中设置 `%T` （在2.0-2016中，您应该使用%x，[为什么做了修改?](https://github.com/wu-sheng/sky-walking/issues/77) ）。
```
log4j.appender.CONSOLE.layout.ConversionPattern=%d [%T] %-5p %c{1}:%L - %m%n
```
3. 启动项目，打印结果如下：
假设 TraceID 存在，当您使用 `-javaagent` 激活 skywalking tracer 后，log4j 将会输出 **TraceID**。如果 tracer 未激活，输出将是 `TID: N/A`。
![](https://qcloudimg.tencent-cloud.cn/raw/36c762433447c7625f44d0b7b1cd560a.png)

### 配置 log4j-2x 输出 TraceID 
1. 使用 maven 或 gradle 引入 toolkit 依赖。
```
<dependency>
<groupId>org.apache.skywalking</groupId>
<artifactId>apm-toolkit-log4j-2.x</artifactId>
<version>{project.release.version}</version>
</dependency>
```
2. 在 log4j2.xml 的 pattern 中配置`[%traceId]`。
 - 支持在 log4j2.xml 的 pattern 中配置 [%traceId]。
```
<Appenders>
      <Console name="Console" target="SYSTEM_OUT">
         <PatternLayout pattern="%d [%traceId] %-5p %c{1}:%L - %m%n"/>
      </Console>
</Appenders>
```
 - 支持 log4j2 AsyncRoot，无需其他配置。请参阅下文的 log4j2.xml 演示。有关详细信息：[Log4j2异步记录器](https://logging.apache.org/log4j/2.x/manual/async.html)。
```
    <Configuration>
        <Appenders>
            <Console name="Console" target="SYSTEM_OUT">
                <PatternLayout pattern="%d [%traceId] %-5p %c{1}:%L - %m%n"/>
            </Console>
        </Appenders>
        <Loggers>
            <AsyncRoot level="INFO">
                <AppenderRef ref="Console"/>
            </AsyncRoot>
        </Loggers>
    </Configuration>
```
  - 支持 log4j2 AsyncAppender，不需要其他配置。请参阅下文的 log4j2.xml 演示。
有关详细信息： [All Loggers Async](https://logging.apache.org/log4j/2.x/manual/async.html#AllAsync)
<dx-alert infotype="explain" title="">
Log4j-2.9 和更高版本要求在类路径上使用 disruptor-3.3.4.jar 或更高版本。在 Log4j-2.9 之前，需要使用 interrupter-3.0.0.jar 或更高版本。 这是最简单的配置，并提供最佳性能。要使所有记录器异步，请将 disruptor jar 添加到类路径中并且 设置系统属性 `log4j2.contextSelector`为 `org.apache.logging.log4j.core.async.AsyncLoggerContextSelector`。
</dx-alert>
  ```
  <Configuration status="WARN">
    <Appenders>
      <!-- Async Loggers will auto-flush in batches, so switch off immediateFlush. -->
      <RandomAccessFile name="RandomAccessFile" fileName="async.log" immediateFlush="false" append="false">
        <PatternLayout>
          <Pattern>%d %p %c{1.} [%t] [%traceId] %m %ex%n</Pattern>
        </PatternLayout>
      </RandomAccessFile>
    </Appenders>
    <Loggers>
      <Root level="info" includeLocation="false">
        <AppenderRef ref="RandomAccessFile"/>
      </Root>
    </Loggers>
  </Configuration>
  ```

     详细可参见： [Mixed Sync & Async](https://logging.apache.org/log4j/2.x/manual/async.html#MixedSync-Async)
<dx-alert infotype="explain" title="">
Log4j-2.9 及更高版本需要类路径上使用  disruptor-3.3.4.jar 或更高版本。在 Log4j-2.9 之前，需要 disruptor-3.0.0.jar 或更高版本。不需要将系统属性 “Log4jContextSelector” 设置为任何值。
</dx-alert>
  ```
  <Configuration status="WARN">
    <Appenders>
      <!-- Async Loggers will auto-flush in batches, so switch off immediateFlush. -->
      <RandomAccessFile name="RandomAccessFile" fileName="asyncWithLocation.log"
                immediateFlush="false" append="false">
        <PatternLayout>
          <Pattern>%d %p %class{1.} [%t] [%traceId] %location %m %ex%n</Pattern>
        </PatternLayout>
      </RandomAccessFile>
    </Appenders>
    <Loggers>
      <!-- pattern layout actually uses location, so we need to include it -->
      <AsyncLogger name="com.foo.Bar" level="trace" includeLocation="true">
        <AppenderRef ref="RandomAccessFile"/>
      </AsyncLogger>
      <Root level="info" includeLocation="true">
        <AppenderRef ref="RandomAccessFile"/>
      </Root>
    </Loggers>
  </Configuration>
  ```
 - 支持 log4j2 AsyncAppender，详细信息请参见： [Log4j2 AsyncAppender](https://logging.apache.org/log4j/2.x/manual/appenders.html)
```
    <Configuration>
        <Appenders>
            <Console name="Console" target="SYSTEM_OUT">
                <PatternLayout pattern="%d [%traceId] %-5p %c{1}:%L - %m%n"/>
            </Console>
            <Async name="Async">
                <AppenderRef ref="Console"/>
            </Async>
        </Appenders>
        <Loggers>
            <Root level="INFO">
                <AppenderRef ref="Async"/>
            </Root>
        </Loggers>
    </Configuration>
```
3. 启动项目，打印结果如下
假设 TraceID 存在，当您使用 `-javaagent` 激活 skywalking tracer 后，log4j 将会输出 **TraceID** 。如果 tracer 未激活，输出将是`TID: N/A`。
![](https://qcloudimg.tencent-cloud.cn/raw/36c762433447c7625f44d0b7b1cd560a.png)

