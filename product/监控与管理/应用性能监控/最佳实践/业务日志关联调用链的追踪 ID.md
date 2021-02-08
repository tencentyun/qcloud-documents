一个事务往往会跨越很多个应用，事务的日志都分散在各个应用下，查找单次请求的所有日志较为困难。 TAPM 的日志溯源功能可以很好的解决这个问题。TAPM 探针可以自动在用户的日志内容中输出 TAPM.APPID 和 TAPM.REQUEST_GUID 属性，通过 TAPM.REQUEST_GUID 属性可以关联不同应用和实例上单次请求的日志。
>?TAPM.REQUEST_GUID 即 TAPM 控制台页面中的追踪 ID 。

## 前提条件
如果应用初次使用该功能，需要在探针配置文件 tapm.properties 中开启以下设置：
```
# 日志追溯相关 Plugin，开启后可以在应用的日志中，打印 TAPM 相关数据，如应用 ID、追踪 ID 等。
class_transformer.tapm-log4j-plugin-2.0.0.enabled=true
class_transformer.tapm-log4j-plugin-2.3.enabled=true
class_transformer.tapm-log4j-plugin-1.2.enabled=true
class_transformer.tapm-logback-plugin-1.2.enabled=true
```

## 背景信息
TAPM 日志溯源功能支持主流的 Log4j 和 Logback 日志框架。

## 操作步骤
1. 登录 [应用性能监控控制台](https://console.cloud.tencent.com/tapm)。
2. 在左侧导航栏中选择【配置】，然后在页面左上角的【业务系统】下拉菜单中选择应用所属的业务系统。
3. 单击【系统配置】页签，然后单击【日志溯源】子页签。
4. 在【日志溯源】区域，选择【单独配置】，然后打开开关。
5. 配置被监控应用的日志配置文件。
   - Log4j 配置
   ```
   log4j.appender.order-file-appender.layout.ConversionPattern=[%d] [%-5p] [%t]
   [%c] [%R][%A]%m%n
   ```
   -   Log4j2 配置
   ```
   <Console name="Console" target="SYSTEM_OUT"\>
    <PatternLayout pattern="%d{HH:mm:ss.SSS} [log4j2] %-5level %logger{36} -
    %msg%n[%A][%R]"/\>
   </Console\>
   ```
   -   Logback 配置
   ```
   <encoder\>
        <pattern\>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} -
     %msg%n[%A][%R]\</pattern\>
   </encoder\>
   ```
   例如，Log4j 日志输出格式如下：
   ```
   [2020-10-29T16:30:27,730-07:00][DEBUG][com.tapm.Log-0][com.tapm.Test][TAPM.REQUEST_GUID:167d328d-b82a-4b8c-8049-7a3a13af158f][TAPM.APPID:0017]
   
   Test Log Message
   ```
   其中：
	 - `[%R]`负责输出请求的 TAPM.REQUEST_GUID，配置后日志会增加 TAPM.REQUEST_GUID 信息。在整个请求链路中，入口事务生成的 NBS.REQUEST_GUID 将作为整个请求链路的唯一标识，此值将在链路中不断传递直到链路的最后请求（如果遇到无法实现跨应用追踪的组件的情况除外），以实现全链路追踪。调用链所涉及的各个应用的日志都显示同一个 NBS.REQUEST_GUID 。
	 - `[%A]`负责输出应用的 TAPM.APPID ，是 TAPM 为每一个监控的应用生成的唯一 ID，配置后日志会增加 TAPM.APPID 信息。如果日志溯源功能是关闭的，即使用户配置了`[%R]`，TAPM.REQUEST_GUID 也不会被嵌入。
6. 重启应用，然后查看应用业务日志。
   在应用的业务日志中成功打印出追踪 ID 信息，则说明业务日志跟调用链的追踪 ID 关联成功。
![](https://main.qcloudimg.com/raw/e0e6bee7614f66b9afac0c766462dadb.png)
