
在 Java 应用程序的用户日志中配置 TraceID 和 SpanID 数据注入非常简单。 一般来说，将日志包的 OpenTelemetry-Java-Instrumentation 检测版本添加到项目依赖项中即可。从 OpenTelemetry-Java-Instrumentation 版本 0.10.1 开始支持 Log4j2 和 logback 注入 TraceID。

### Log4j instrumentation 注入 TraceID
1. 添加 **Log4j2** 与 **OpenTelemetry-api** 库到依赖库 dependencies 中：
 - Maven projects：
```
<dependencies>
  <dependency>
    <groupId>io.opentelemetry.instrumentation</groupId>
    <artifactId>opentelemetry-log4j-2.13.2</artifactId>
    <version>1.9.2-alpha</version>
    <scope>runtime</scope>
  </dependency>
  <dependency>
    <groupId>io.opentelemetry</groupId>
    <artifactId>opentelemetry-api</artifactId>
    <version>1.11.0</version>
  </dependency>

<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-api</artifactId>
  </dependency>
</dependencies>
```
 - Gradle projects：
```
dependencies {
  runtimeOnly("io.opentelemetry.instrumentation:opentelemetry-log4j-2.13.2:1.9.2-alpha")
  implementation("io.opentelemetry:opentelemetry-api:1.11.0"

  implementation("org.slf4j:slf4j-api")
}
```
2. 更新 log4j2.properties 配置文件，示例配置如下：
```
status=info
name=properties_configuration
property.basePath=/Users/tcenent/java/opentelemetry-logger-tracer/logs/

appender.rolling.type=RollingFile
[appender.rolling.name](http://appender.rolling.name/)=fileLogger
appender.rolling.fileName=${basePath}/opentelemetry-tracer.log
appender.rolling.filePattern=${basePath}app_%d{yyyyMMdd}.log.gz
appender.rolling.layout.type=PatternLayout
appender.rolling.layout.pattern=%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} traceId: %X{trace_id} spanId: %X{span_id} - %msg%n
appender.rolling.policies.type=Policies

appender.rolling.policies.time.type=TimeBasedTriggeringPolicy
appender.rolling.policies.time.interval=1
appender.rolling.policies.time.modulate=true
appender.rolling.strategy.type=DefaultRolloverStrategy
appender.rolling.strategy.delete.type=Delete
appender.rolling.strategy.delete.basePath=${basePath}
appender.rolling.strategy.delete.maxDepth=1
appender.rolling.strategy.delete.ifLastModified.type=IfLastModified
appender.rolling.strategy.delete.ifLastModified.age=30d

rootLogger.level=info
rootLogger.additivity=false
rootLogger.appenderRef.rolling.ref=fileLogger
```
3. 配置完后，可在 logger 日志文件中查看到 TraceID 与 SpanID，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/542cf0fda03907e7487baa9131bb478e.png)

### Logback instrumentation 注入 TraceID
1. 添加 logback 工程依赖库到 dependencies 中：
 - Maven projects
```
<dependencies>
  <dependency>
    <groupId>io.opentelemetry.instrumentation</groupId>
    <artifactId>opentelemetry-logback-1.0</artifactId>
    <version>1.9.2-alpha</version>
    <scope>runtime</scope>
  </dependency>

    <dependency>
       <groupId>ch.qos.logback</groupId>
      <artifactId>logback-core</artifactId>
      <scope>provided</scope>
   </dependency>
   <dependency>
       <groupId>ch.qos.logback</groupId>
      <artifactId>logback-classic</artifactId>
   </dependency>
  <dependency>
      <groupId>ch.qos.logback</groupId>
     <artifactId>logback-access</artifactId>
     <scope>provided</scope>
  </dependency>
</dependencies>
```
 - Gradle projects：
```
dependencies {
  runtimeOnly("io.opentelemetry.instrumentation:opentelemetry-logback-1.0:1.9.2-alpha")

  implementation("ch.qos.logback:logback-core:1.11.0"

  implementation("ch.qos.logback:logback-classic"

  implementation("ch.qos.logback:logback-access"
  }
```
2. 更新 logback.xml 配置文件，下面是一个示例配置：
```
<?xml version="1.0" encoding="UTF-8" ?>
<configuration scan="true" scanPeriod="3 seconds">
    <appender name="FILE" class="ch.qos.logback.core.FileAppender">
        <encoder>
            <pattern><![CDATA[%date{HH:mm:ss.SSS} [%thread] %-5level %logger{15}#%line %X{req.requestURI} traceId: %X{trace_id} spanId: %X{span_id} %msg\n]]></pattern>
        </encoder>
        <File>/Users/tencent/java/opentelemetry-logger-tracer/logs/logFile.log</File>
        <append>true</append>
    </appender>
    <appender name="OTEL" class="io.opentelemetry.instrumentation.logback.v1_0.OpenTelemetryAppender">
        <appender-ref ref="FILE" />
    </appender>
    <root>
        <level value="INFO" />
        <appender-ref ref="FILE" />
    </root>
</configuration>
```
3. 配置完后，可在 logger 日志文件中查看到 TraceID 与 SpanID，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/d5e3299b75c4fe83a7f87fb7f66c7e25.png)


### 注意事项
因为 spring-boot 会自带 logger 的配置，所以要我们配置的文件生效，需要在引入 spring-boot 依赖示去掉默认的 loger 库：
```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <exclusions>
        <exclusion>
            <artifactId>org.springframework.boot</artifactId>
            <groupId>spring-boot-starter-logging</groupId>
        </exclusion>
        <exclusion>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-log4j12</artifactId>
        </exclusion>
    </exclusions>
</dependency>

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter</artifactId>
    <exclusions>
        <exclusion>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-logging</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

>!如上 exclusions 的配置很重要。

