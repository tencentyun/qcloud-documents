本文将为您介绍如何在 JBoss 手动安装 Java 探针。

## 前提条件

- 应用性能监控目前处于内测阶段，如需体验需通过 [应用性能监控内测申请](https://cloud.tencent.com/apply/p/f5yvbf09mka)。
- 在安装探针前，请先安装 Agent Collector。
- 在安装探针前，需要先确保本地浏览器时间与服务器时区、时间一致。若有多个服务器，则要保证本地浏览器、多个服务器的时区、时间都一致。否则，可能会影响数据的准确性，例如拓扑不正确等。
- 前往 TAPM 控制台 [探针下载](https://console.cloud.tencent.com/tapm/addagent) 页面下载 tapm-java-Agent。


## 操作步骤

>?8.0以上版本的 JBoss 已改名为 WildFly。关于 WildFly 的探针安装步骤介绍，请参见 [WildFly](https://cloud.tencent.com/document/product/1349/52406)。

### Domain mode

若 Domain mode 使用 JBoss 6.X EAP  或 7.0.X 及更高的版本。 每个服务器组的 JVM 配置信息可以在 **domain/configuration/domain.xml** 文件配置。示例如下：

```xml
<server-group name="main-server-group" profile="full">
  <jvm name="default">
    <jvm-options>
      <option value="-javaagent:/${路径}/tapm-agent-java.jar"/>
    </jvm-options>
  </jvm>
</server-group>
```


>?
>- 请确认 `-javaagent` 指定路径是 tapm-agent-java.jar 的完整路径。
>- 如果您的 JBoss 部署在 Windows，则路径使用的是斜杠 `/`，例如 `d:/tapm/tapm-agent-java.jar`。
>- 参考 [JBoss bug in 7.0.2.Final and 7.1.0.Alpha1](https://issues.jboss.org/browse/AS7-1868)，可发现 JBoss 存在 Bug 不允许在 domain.xml 中配置 jvm-options 。如果您使用的是存在该 Bug 的 JBoss，请升级 JBoss 应用服务器。

### Standalone mode

> ?请确认 `-javaagent` 指定路径是 tapm-agent-java.jar 的完整路径。

| 平台                                              | 用法                                                         |
| ------------------------------------------------- | ------------------------------------------------------------ |
| Unix/Mac OS 使用 6.x EAP 或 7.0.x AS 及更高版本 | 在 `bin/standalone.conf` 文件的底部，添加 `JAVA_OPTS="$JAVA_OPTS -javaagent:/${路径}/tapm-agent-java.jar"` |
| Windows 使用 6.x EAP 或 7.0.x AS 及更高版本       | 在 `bin/standalone.bat` 文件的 `set JBOSS_ENDORSED_DIRS=%JBOSS_HOME%\lib\endorsed` 行之前添加 `set "JAVA_OPTS=-javaagent:C:/${路径}/tapm-agent-java.jar %JAVA_OPTS%"`，使用斜线 `C:/tapm/tapm-agent-java.jar` |
| Unix/Mac OS 使用 6.x 及更低版本                 | 在 `bin/run.conf` 文件的底部，添加 `JAVA_OPTS="$JAVA_OPTS -javaagent:/${路径}/tapm-agent-java.jar"` |
| Windows 使用 6.x 及更低版本                       | 在 `bin/run.bat` 文件中 `set JBOSS_CLASSPATH=%RUN_CLASSPATH%` 行之前添加 `set "JAVA_OPTS=-javaagent:C:/${路径}/tapm-agent-java.jar %JAVA_OPTS%"`，使用斜线 `C:/tapm/tapm-agent-java.jar` |
