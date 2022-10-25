支持 Skywalking 探针（目前只支持 Java 的 Log4j/ Logback/ Log4j2 ）进行日志接入、接入成功后您将可以日志检索及分析。您将可以本文将为您介绍如何接入日志服务。



## 前提条件
已接入应用，若未接入可参见 [接入指南](https://cloud.tencent.com/document/product/1463/57860)。

## 操作步骤

### 步骤1：日志上报配置
1. 进入 [应用性能观测控制台](https://console.cloud.tencent.com/apm) **日志分析** > **日志概览**页面，单击**日志接入**。
2. 在接入流程中，进行下列配置：
 - 选择您的上报地域和业务系统。公测期上报地域仅支持广州。
 - 根据您的日志内容，选择适合的日志类型。并选择 skywalking 作为接入方式。

### 步骤2：选择任意一种方式接入日志
>?**Logback、Log4j、Log4j2：**都是 Apache 的开源项目，常用的日志框架，通过使用这些日志框架，我们可以控制日志信息输送的目的地，还可以通过一个配置文件来灵活地进行配置，而不需要修改应用的代码。
- Logback
[Logback](http://logback.qos.ch/) 是一个开源日志组件，是 Slf4j 的原生实现框架，相比 Log4j，Logback 执行速度更快，占用内存更少，是 spring boot 默认集成的日志框。
- **Log4j & Log4j2**
  [Log4j](http://logging.apache.org/log4j/1.2/) 和 [Log4j2](https://logging.apache.org/log4j/2.x/) 也都是 Apache 的开源日志框架， Log4j2 是Log4j 1.x 和 Logback 的改进版，采用无锁异步等，使日志吞吐量、性能比 log4j 1.x提高10倍，并解决了一些老版本的 bug，且配置更加简单灵活。

####  方式一：Logback
1. 在 pom 文件中添加相关依赖。
 ```
  <dependency>
    <groupId>org.apache.skywalking</groupId>
    <artifactId>apm-toolkit-logback-1.x</artifactId>
    <version>8.5.0</version>
  </dependency>
```
2. 在 resources 中新建 logback-spring.xml 文件。
 ```
  <configuration>
    <include resource="org/springframework/boot/logging/logback/defaults.xml"></include>

    <appender name="console" class="ch.qos.logback.core.ConsoleAppender">
      <encoder class="ch.qos.logback.core.encoder.LayoutWrappingEncoder">
        <layout class="org.apache.skywalking.apm.toolkit.log.logback.v1.x.TraceIdPatternLogbackLayout">
          <Pattern>-%clr(%d{${LOG_DATEFORMAT_PATTERN:-yyyy-MM-dd HH:mm:ss.SSS}}){faint} %clr(${LOG_LEVEL_PATTERN:-%5p}) %clr(${PID:- }){magenta}%clr(---){faint} %clr([%15.15t]){faint} %clr(%-40.40logger{39}){cyan} %clr(:){faint} %m%n${LOG_EXCEPTION_CONVERSION_WORD:-%wEx}}</Pattern>
        </layout>
      </encoder>
    </appender>
    <appender name="grpc-log" class="org.apache.skywalking.apm.toolkit.log.logback.v1.x.log.GRPCLogClientAppender">
      <encoder class="ch.qos.logback.core.encoder.LayoutWrappingEncoder">
        <layout class="org.apache.skywalking.apm.toolkit.log.logback.v1.x.mdc.TraceIdMDCPatternLogbackLayout">
          <Pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%X{tid}] [%thread] %-5level %logger{36} %msg%n</Pattern>
        </layout>
      </encoder>
    </appender>
  </configuration>
```
3. 在 agent.config 中添加 以下内容。
```
  plugin.toolkit.log.grpc.reporter.server_host=${SW_GRPC_LOG_SERVER_HOST:pl.ap-guangzhou.apm.tencentcs.com}
  plugin.toolkit.log.grpc.reporter.server_port=${SW_GRPC_LOG_SERVER_PORT:}
  plugin.toolkit.log.grpc.reporter.max_message_size=${SW_GRPC_LOG_MAX_MESSAGE_SIZE:10485760}
  plugin.toolkit.log.grpc.reporter.upstream_timeout=${SW_GRPC_LOG_GRPC_UPSTREAM_TIMEOUT:30}
```

#### 方式二：Log4j2
1. 在 pom 文件中添加相关依赖。
 ```
   <dependency>
    <groupId>org.apache.skywalking</groupId>
    <artifactId>apm-toolkit-log4j-2.x</artifactId>
    <version>{project.release.version}</version>
  </dependency>


```
2. 在 log4j2.xml 中增加如下内容支持日志中打印 TraceId。
 ```
 <Appenders>
    <Console name="Console" target="SYSTEM_OUT">
      <PatternLayout pattern="%d [%traceId] %-5p %c{1}:%L - %m%n"></PatternLayout>
    </Console>
  </Appenders>
```
3. 在 log4j2.xml 中添加 GRPCLogClientAppender。
 ```
   <GRPCLogClientAppender name="grpc-log">
    <PatternLayout pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} - %msg%n"></PatternLayout>
  </GRPCLogClientAppender>
```
4. 在 agent.config 中添加 以下内容：
```
  plugin.toolkit.log.grpc.reporter.server_host=${SW_GRPC_LOG_SERVER_HOST:pl.ap-guangzhou.apm.tencentcs.com}
  plugin.toolkit.log.grpc.reporter.server_port=${SW_GRPC_LOG_SERVER_PORT:}
  plugin.toolkit.log.grpc.reporter.max_message_size=${SW_GRPC_LOG_MAX_MESSAGE_SIZE:10485760}
  plugin.toolkit.log.grpc.reporter.upstream_timeout=${SW_GRPC_LOG_GRPC_UPSTREAM_TIMEOUT:30}
 
```

#### 方式三：Log4j
1. 在 pom 文件中添加相关依赖。
```
    <dependency>
    <groupId>org.apache.skywalking</groupId>
    <artifactId>apm-toolkit-log4j-1.x</artifactId>
    <version>{project.release.version}</version>
  </dependency>
```
2. 在 log4j.properties 中添加 GRPCLogClientAppender。
 ```
  <configuration>
    <include resource="org/springframework/boot/logging/logback/defaults.xml"></include>

    <appender name="console" class="ch.qos.logback.core.ConsoleAppender">
      <encoder class="ch.qos.logback.core.encoder.LayoutWrappingEncoder">
        <layout class="org.apache.skywalking.apm.toolkit.log.logback.v1.x.TraceIdPatternLogbackLayout">
          <Pattern>-%clr(%d{${LOG_DATEFORMAT_PATTERN:-yyyy-MM-dd HH:mm:ss.SSS}}){faint} %clr(${LOG_LEVEL_PATTERN:-%5p}) %clr(${PID:- }){magenta}%clr(---){faint} %clr([%15.15t]){faint} %clr(%-40.40logger{39}){cyan} %clr(:){faint} %m%n${LOG_EXCEPTION_CONVERSION_WORD:-%wEx}}</Pattern>
        </layout>
      </encoder>
    </appender>
    <appender name="grpc-log" class="org.apache.skywalking.apm.toolkit.log.logback.v1.x.log.GRPCLogClientAppender">
      <encoder class="ch.qos.logback.core.encoder.LayoutWrappingEncoder">
        <layout class="org.apache.skywalking.apm.toolkit.log.logback.v1.x.mdc.TraceIdMDCPatternLogbackLayout">
          <Pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%X{tid}] [%thread] %-5level %logger{36} %msg%n</Pattern>
        </layout>
      </encoder>
    </appender>
  </configuration>
 
```
3. 在 agent.config 中添加 以下内容。
 ```
  plugin.toolkit.log.grpc.reporter.server_host=${SW_GRPC_LOG_SERVER_HOST:pl.ap-guangzhou.apm.tencentcs.com}
  plugin.toolkit.log.grpc.reporter.server_port=${SW_GRPC_LOG_SERVER_PORT:}
  plugin.toolkit.log.grpc.reporter.max_message_size=${SW_GRPC_LOG_MAX_MESSAGE_SIZE:10485760}
  plugin.toolkit.log.grpc.reporter.upstream_timeout=${SW_GRPC_LOG_GRPC_UPSTREAM_TIMEOUT:30}
 ```

### 步骤3：验证是否上报成功
上述步骤配置完成后，等待1~2分钟，若在 [日志检索](https://console.cloud.tencent.com/apm/explorer/log/query) 所看到上报的日志，则说明上报成功。
