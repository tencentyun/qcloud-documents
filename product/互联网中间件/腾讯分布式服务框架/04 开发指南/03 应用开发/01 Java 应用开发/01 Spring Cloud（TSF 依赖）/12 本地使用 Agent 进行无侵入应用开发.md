## 操作场景
本文主要介绍 Spring Cloud 开源项目如何在本地使用 Agent 进行无侵入应用开发。

## 前提条件
请确保您已经参见 [下载 Maven](https://cloud.tencent.com/document/product/649/20231) 下载安装了 Java 和 Maven，并且配置了 TSF 私服地址。

> ? 同时请确保 SDK 版本高于**2020**。

## 操作步骤
如果对 Agent 有疑问，可以先参见 [Agent 插件功能说明](https://cloud.tencent.com/document/product/649/79177)。

>?[步骤1](#step1) 和 [步骤2](#step2) 与其他模块一样，已经使用过其他模块的可直接跳至 [步骤3](#step3)。

[](id:step1)
**1. 在本地确保依赖了 2020 相关的 SDK 依赖。**
在 `pom.xml` 中添加以下代码：
```xml
<dependency>
    <groupId>com.tencent.tsf</groupId>
    <artifactId>femas-adaptor-tsf-springcloud-2020</artifactId>
    <version><!-- 调整为 SDK 最新版本号 --></version> 
</dependency>

<dependency>
    <groupId>com.tencent.tsf</groupId>
    <artifactId>femas-adaptor-tsf-springfox-2.10</artifactId>
    <version><!-- 调整为 SDK 最新版本号 --></version> 
</dependency>
```
**[](id:step2)2. 向 Application 类中添加注解 `@EnableTsf`：**

<dx-codeblock>
:::  java
// 下面省略了无关的代码
@SpringBootApplication
@EnableTsf
public class ProviderApplication {
    public static void main(String[] args) {
        SpringApplication.run(ProviderApplication.class, args);
    }
}
:::
</dx-codeblock>

**[](id:step3)3. 在启动应用时使用服务 Agent：**

下载 [service-agent-release.tar](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/jvm%E7%9B%91%E6%8E%A7/service-agent-release.tar)，并解压。在 IDE 中启动，通过 VM options 配置启动参数`-javaagent:service-agent-release/femas-agent/femas-agent.jar`，通过 main 方法直接启动。

**[](id:step4)4. 在启动应用时使用可观测 Agent：**

下载 [ot-agent-release.tar](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/jvm%E7%9B%91%E6%8E%A7/ot-agent-release.tar)，并解压。在 IDE 中启动，通过 VM options 配置启动参数`-javaagent:ot-agent-release/opentelemetry-javaagent.jar -Dotel.javaagent.extensions=ot-agent-release/femas-trace-opentelemetry.jar`，通过 main 方法直接启动。

>!如果想要多个 Agent 一起使用，可以使用命令如：`-javaagent:service-agent-release/femas-agent/femas-agent.jar -javaagent:ot-agent-release/opentelemetry-javaagent.jar -Dotel.javaagent.extensions=ot-agent-release/femas-trace-opentelemetry.jar`

