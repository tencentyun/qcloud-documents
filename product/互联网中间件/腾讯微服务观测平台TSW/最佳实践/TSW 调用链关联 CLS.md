## 操作场景

本文档指导您将腾讯微服务观测平台 TSW 的调用链与腾讯云日志服务 CLS 进行关联。
您可以将自身微服务应用的日志采集上报到 CLS，然后在 CLS 的控制台查看微服务应用的日志信息。与此同时，您可以在微服务应用输出的日志中加入 TraceID（调用链 ID），然后根据该 TraceID 在 TSW 中直接查询到该 TraceID 对应的调用链详细信息，提高用户在出现异常日志时的排查效率。

## 前提条件

在开始本文的实践前，您需要先了解以下产品：

- [TSW 服务观测](https://cloud.tencent.com/document/product/1311/51690)
- [CLS 产品概述](https://cloud.tencent.com/document/product/614/11254) 

## 操作步骤

以使用 Apache SkyWalking 上报的 Java 应用数据为例。

### 步骤1：配置 logback 以输出 TraceID

1. 在 pom.xml 中引入相关依赖。
```xml
<dependency>
	<groupId>org.apache.skywalking</groupId>
	<artifactId>apm-toolkit-logback-1.x</artifactId>
</dependency>
```


2. 修改 logback.xml 文件。
   在 appender 中添加如下日志配置：
```xml
<encoder class="ch.qos.logback.core.encoder.LayoutWrappingEncoder">
	<layout class="org.apache.skywalking.apm.toolkit.log.logback.v1.x.TraceIdPatternLogbackLayout">
		<pattern>%d{HH:mm:ss.SSS} [%thread] %-5level logger_name:%logger{36} - [%tid] - message:%msg%n</pattern>
	</layout>
</encoder>
```

 输出的日志将如下所示：
```xml
16:39:12.134 [http-nio-19200-exec-1] ERROR logger_name:c.t.c.t.d.b.o.c.OrderController - [TID:0524******2672.30.16143287521281125] - message:Order of orderId [172651] is finished failed.
```
	无 TraceID 时打印 [TID:N/A]。

### 步骤2：在 TSW 上接入服务

参考 [通过 SkyWalking 上报 Java 应用数据](https://cloud.tencent.com/document/product/1311/51606) 部署好一套使用 SkyWalking Agent 上报的 Java 的 Demo。

### 步骤3：在 CLS 上接入服务

参考 [五分钟入门指南](https://cloud.tencent.com/document/product/614/34340) 将一整套 Demo 接入 CLS。

### 步骤4：联动使用

在 [CLS 控制台](https://console.cloud.tencent.com/cls) 成功创建日志主题，并成功写入 TraceID 后，您就可以在 TSW 控制台的服务列表中，配置服务关联的日志主题。
1. 单击【日志配置】，打开关联日志的开关，并正确配置日志集与日志主题。
	 ![](https://main.qcloudimg.com/raw/1efab147a3d9008e6b0aa3e63bcdaa58.png)
日志配置界面如下：
![](https://main.qcloudimg.com/raw/a722931c37d21f250db8984e43acd3e0.png)
2. 在 TSW 控制台的【链路追踪】>【[调用链查询](https://console.cloud.tencent.com/tsw/trace)】中，展开任意 Trace，即可通过日志 icon 跳转到对应的业务日志。在各请求列表中，您也可以直接跳转到对应 Trace 的日志。
![](https://main.qcloudimg.com/raw/079ed56b5a99c03e218eadb11aad1e2e.png)
