本文将为您介绍如何在 Glassfish 手动安装 Java 探针。

## 前提条件

- 应用性能监控目前处于内测阶段，如需体验需通过 [应用性能监控内测申请](https://cloud.tencent.com/apply/p/f5yvbf09mka)。
- 在安装探针前，请先安装 Agent Collector。
- 在安装探针前，需要先确保本地浏览器时间与服务器时区、时间一致。若有多个服务器，则要保证本地浏览器、多个服务器的时区、时间都一致。否则，可能会影响数据的准确性，例如拓扑不正确等。
- 前往 TAPM 控制台 [探针下载](https://console.cloud.tencent.com/tapm/addagent) 页面下载 tapm-java-Agent。


## 操作步骤




1. 访问 Glassfish 配置界面。
2. 从左侧菜单依次选择【Configurations】>【server-config】>【JVM Settings】>【JVM Options】。
3. 在 JVM Options 页面，选择【Add JVM Option】。
4. 添加以下条目，配置 `-javaagent` 参数。
<dx-codeblock>
:::  bash
-javaagent:/${路径}/tapm-agent-java.jar
:::
</dx-codeblock>
5. 保存设置。
6. 重启应用服务器。
> ?若 Glassfish 不能够正常启动，可能是 -javaagent 参数配置错误。可以通过编辑 **domain.xml** 正确配置 -javaagent 参数。（domain.xml 参考路径 `GLASSFISH_HOME/glassfish/domains/{domain}/config/domain.xml`）。


