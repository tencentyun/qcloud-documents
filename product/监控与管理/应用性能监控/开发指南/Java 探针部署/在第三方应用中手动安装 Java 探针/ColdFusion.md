本文将为您介绍如何在 ColdFusion 上安装 Java 探针。

## 前提条件

- 应用性能监控目前处于内测阶段，如需体验需通过 [应用性能监控内测申请](https://cloud.tencent.com/apply/p/f5yvbf09mka)。
- 在安装探针前，请先安装 Agent Collector。
- 在安装探针前，需要先确保本地浏览器时间与服务器时区、时间一致。若有多个服务器，则要保证本地浏览器、多个服务器的时区、时间都一致。否则，可能会影响数据的准确性，例如拓扑不正确等。
- 前往 TAPM 控制台 [探针下载](https://console.cloud.tencent.com/tapm/addagent) 页面下载 tapm-java-Agent。

## 操作步骤

1. 访问 **ColdFusion Administrator Console**。
2. 从左侧菜单依次选择【SERVER SETTINGS】>【Java and JVM】。
3. 在  **JVM Arguments**  输入框里，配置 `-javaagent` 参数。
<dx-codeblock>
:::  bash
 -javaagent:/${路径}/tapm-agent-java.jar
:::
</dx-codeblock>
4. 单击【Submit Changes】。
5. 重启 ColdFusion。
>?探针暂时不支持 ColdFusion Version 9 on IIS。
