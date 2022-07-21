
## 操作场景
Spring Cloud 普通应用使用 Java Agent 接入，支持 TSF 全栈服务治理、应用性能监控、应用配置管理能力。Java Agent 是 Java 1.5 版本之后引⼊的特性，可以被理解为 JVM 虚拟机级别的 AOP，使用该技术可以做到无需对原有应用做任何修改，就可以对原有应用的实现类进行动态修改和增强。利用 Java Agent 技术来做无侵入埋点，可以使得业务无需做任何改造就可以接入 TSF 平台并使用 TSF 一系列配套的能力。 
本文主要介绍开源 Spring Cloud 应用如何 0 改造就可以将应用部署到 TSF 平台，目前支持服务发现、服务治理、配置中心和应用监控能力。

## 前提条件
请确保您已经参见 [下载 Maven](https://cloud.tencent.com/document/product/649/20231) 下载安装了 Java 和 Maven，并且配置了 TSF 私服地址。

> ? 目前 同时请确保 SDK 版本高于**2020**。
## 操作步骤
>?[步骤1](#step1) 和 [步骤2](#step2) 与其他模块一样，已经使用过其他模块的可直接跳至 [步骤3](#step3)。
[](id:step1)
**1. 向工程中添加依赖。**
在 `pom.xml` 中添加以下代码：
```xml
<dependency>
    <groupId>com.tencent.tsf</groupId>
    <artifactId>spring-cloud-tsf-starter</artifactId>
    <version><!-- 调整为 SDK 最新版本号 --></version> 
</dependency>
