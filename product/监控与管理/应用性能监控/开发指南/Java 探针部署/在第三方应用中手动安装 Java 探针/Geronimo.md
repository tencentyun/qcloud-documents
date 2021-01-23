本文将为您介绍如何在 Geronimo 上安装 Java 探针

### 在 Geronimo 上安装 Java 探针

使用 geronimo run 启动时，将 tapm-agent-java.jar 添加到 `JAVA_OPTS`变量里，示例如下：

```shell
export JAVA_OPTS="$JAVA_OPTS -javaagent:/${路径}/tapm-agent-

java.jar" && geronimo run
```

