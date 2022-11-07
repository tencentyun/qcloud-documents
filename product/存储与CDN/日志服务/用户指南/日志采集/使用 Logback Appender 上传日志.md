## 简介

日志服务（Cloud Log Service，CLS）目前已支持使用 Logback Appender 上传日志到 CLS。

## 背景信息

Logback 是 Apache 的一个开源项目。通过使用 Logback，我们可以控制日志信息输送的目的地是控制台、文件、GUI 组件，甚至是套接口服务器、NT 的事件记录器、UNIX Syslog 守护进程等。此外，我们还可以通过一个配置文件来灵活地进行配置，而不需要修改应用的代码。

## 功能优势

- 日志不落盘：产生数据通过网络发给服务端。
- 无需改造：对已使用 Logback 应用，只需简单配置即可采集。
- 异步非阻塞：高并发设计，后台异步发送，适合高并发写入。
- 资源可控制：可以通过参数控制 producer 用于缓存待发送数据的内存大小，同时还可以配置用于执行数据发送任务的线程数量。
- 自动重试： 对可重试的异常，支持配置重试次数。
- 优雅关闭： 退出前会将日志全量进行发送。
- 感知日志上报结果："运行过程中产生的异常通过 AddError 输出出来"。


## 工程引入和配置

### maven 工程中引入依赖

```
<dependency>
    <groupId>com.tencentcloudapi.cls</groupId>
    <artifactId>tencentcloud-cls-logback-appender</artifactId>
    <version>1.0.3</version>
</dependency>
```

### 修改 logback 配置文件
```
  <appender name="LoghubAppender" class="com.tencentcloudapi.cls.LoghubAppender">
        <!--必选项-->
        <endpoint><region>.cls.tencentcs.com</endpoint>
        <accessKeyId>${SecretID}</SecretID>
        <accessKeySecret>${SecretKey}</SecretKey>
        <topicId>${topicId}</topicId>

        <!-- 可选项 详见 '参数说明'-->
        <totalSizeInBytes>104857600</totalSizeInBytes>
        <maxBlockMs>0</maxBlockMs>
        <sendThreadCount>8</sendThreadCount>
        <batchSizeThresholdInBytes>524288</batchSizeThresholdInBytes>
        <batchCountThreshold>4096</batchCountThreshold>
        <lingerMs>2000</lingerMs>
        <retries>10</retries>
        <baseRetryBackoffMs>100</baseRetryBackoffMs>
        <maxRetryBackoffMs>50000</maxRetryBackoffMs>

        <!-- 可选项 设置时间格式 -->
        <timeFormat>yyyy-MM-dd'T'HH:mm:ssZ</timeFormat>
        <timeZone>Asia/Shanghai</timeZone>
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger - %msg</pattern>
        </encoder>
        <mdcFields>THREAD_ID,MDC_KEY</mdcFields>
  </appender>
```

## Logback Appender SDK

请使用 [tencentcloud-cls-logback-appender](https://github.com/TencentCloud/tencentcloud-cls-logback-appender)。



