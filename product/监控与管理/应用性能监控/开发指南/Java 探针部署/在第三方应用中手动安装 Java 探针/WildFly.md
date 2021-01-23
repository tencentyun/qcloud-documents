本文将为您介绍如何在 WildFly 上安装 Java 探针

##  在 WildFly 上安装 Java 探针

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

> ?${路径}需替换成 tapm-agent-java.jar 文件路径，例如： `C:/tapm/tapm-agent-java.jar`。

#### Standalone mode

修改 **bin/standalone.conf** 和 **bin/standalone.bat** 文件，修改说明如下：

| 操作系统          | 描述                                                         |
| ----------------- | ------------------------------------------------------------ |
| **Unix / Mac OS** | 在 **bin/standalone.conf** 文件的底部, 添加: `JAVA_OPTS="$JAVA_OPTS -javaagent:/${路径}/tapm-agent-java.jar"` |
| **Windows**       | 查找 **bin/standalone.bat** 文件中的如下内容：`rem Setup JBoss specific properties`在该行之后添加`set "JAVA_OPTS=-javaagent:C:/tapm/tapm-agent-java.jar %JAVA_OPTS%"` |
