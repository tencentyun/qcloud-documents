本文将为您介绍如何在 WildFly 上安装 Java 探针。




## 前提条件

- 应用性能监控目前处于内测阶段，如需体验需通过 [应用性能监控内测申请](https://cloud.tencent.com/apply/p/f5yvbf09mka)。
- 在安装探针前，请先安装 Agent Collector。
- 在安装探针前，需要先确保本地浏览器时间与服务器时区、时间一致。若有多个服务器，则要保证本地浏览器、多个服务器的时区、时间都一致。否则，可能会影响数据的准确性，例如拓扑不正确等。
- 前往 TAPM 控制台 [探针下载](https://console.cloud.tencent.com/tapm/addagent) 页面下载 tapm-java-Agent。


##  操作步骤

### Domain mode

修改 domain/configuration/domain.xml 里的 `<jvm-options/>` 增加 `<option/> `，示例如下：

```xml
<server-group name="main-server-group" profile="full">
  <jvm name="default">
    <jvm-options>
      <option value="-javaagent:/${路径}/tapm-agent-java.jar"/>
    </jvm-options>
  </jvm>
```

> ?`${路径}` 需替换成 tapm-agent-java.jar 文件路径，例如  `C:/tapm/tapm-agent-java.jar`。

### Standalone mode

修改 **bin/standalone.conf** 和 **bin/standalone.bat** 文件，修改说明如下：

| 操作系统          | 描述                                                         |
| ----------------- | ------------------------------------------------------------ |
| **Unix/Mac** | 在 **bin/standalone.conf** 文件的底部, 添加: `JAVA_OPTS="$JAVA_OPTS -javaagent:/${路径}/tapm-agent-java.jar"` |
| **Windows**       | 查找 **bin/standalone.bat** 文件中的如下内容：`rem Setup JBoss specific properties`在该行之后添加`set "JAVA_OPTS=-javaagent:C:/tapm/tapm-agent-java.jar %JAVA_OPTS%"` |


