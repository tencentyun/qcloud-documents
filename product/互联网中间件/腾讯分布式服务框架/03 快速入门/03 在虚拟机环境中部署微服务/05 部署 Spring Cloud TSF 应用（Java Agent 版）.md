
## 操作场景
Spring Cloud 普通应用使用 Java Agent 接入 TSF 平台，支持 TSF 服务注册发现、服务治理、应用配置管理和应用性能监控能力。

Java Agent 是 Java 1.5 版本之后引⼊的特性，可以被理解为 JVM 虚拟机级别的 AOP，使用该技术可以做到无需对原有应用做任何修改，就可以对原有应用的实现类进行动态修改和增强。利用 Java Agent 技术来做无侵入埋点，可以使得业务无需做任何改造就可以接入 TSF 平台并使用 TSF 一系列配套的能力。 

本文主要介绍开源 Spring Cloud 应用如何 0 改造就可以将应用部署接入到 TSF 平台。

## Agent 插件功能说明
- 以下表格是目前支持的 Agent 插件以及其对应功能的详细说明
<table>
<thead>
<tr>
<th align="left">Agent 插件名称</th>
<th>插件说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">服务 Agent</td>
<td>支持 TSF 服务注册发现、服务治理以及应用配置管理能力</td>
</tr>
<tr>
<td align="left">可观测 Agent</td>
<td>支持 TSF 应用性能监控能力，包括调用链、数据指标监控等</td>
</tr>
</tbody></table>
- 以下表格是 Spring Cloud 版本以及对应支持 Agent 插件的详细说明
<table>
<thead>
<tr>
<th align="left">开源 Spring Cloud 版本</th>
<th>服务 Agent</th>
<th>可观测 Agent</th>
</tr>
</thead>
<tbody><tr>
<td align="left">Spring Cloud 2020</td>
<td>支持</td>
<td>支持</td>
</tr>
</tbody></table>

> ? 目前仅支持 **Spring Cloud 2020** 使用 Java Agent 接入 TSF 平台。

## 前提条件

1. 已创建好集群并导入云主机，虚拟机场景请参见 [虚拟机集群管理](https://cloud.tencent.com/document/product/649/73964)。
2. 下载 [官方开源 Spring Cloud 2020 Demo](https://github.com/polarismesh/femas/tree/develop/femas-agent/femas-agent-example)，在pom.xml文件所在目录下执行`mvn clean package`将应用程序打包，在`femas-agent-example-springcloud-provider/target/`目录下可以看到打包好的 jar 程序包。

## 操作步骤
1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf)。
2. 这里跳过 **新建应用** 步骤，直接到 **部署应用配置 Agent 插件**，如果需要了解 **新建应用** 和其他 **部署应用** 相关操作可以参见 [虚拟机应用管理](https://cloud.tencent.com/document/product/649/55494)。
3. **部署应用配置 Agent 插件**：在部署虚拟机应用的时候单击**展开高级设置**，勾选相应的 Agent 插件进行部署（建议服务 Agent 和可观测 Agent 都选上）。
   ![](https://qcloudimg.tencent-cloud.cn/raw/4f661b546fd5af73e31d4fe751397299.png)
4. 其他部署配置都选择好以后，单击 **完成** 进行部署。
5. 完成部署以后的服务调用和拓扑图展示等验证操作继续参考文档上述虚拟机应用管理文档。
