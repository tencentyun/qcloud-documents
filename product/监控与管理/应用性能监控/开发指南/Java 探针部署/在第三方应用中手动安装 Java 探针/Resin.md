本文将为您介绍如何在 Resin 安装 Java 探针。

## 在Resin上安装Java探针

### Resin pro 3.1+ production mode

找到 conf 目录下的 resin.conf 文件，增加配置 ：

```xml
<jvm-arg>-javaagent:/${路径}/tapm-agent-java.jar</jvm-arg>
```

多个 serve 和单个 server 配置示例如下：

- 针对集群所有 server 增加探针：

```xml
<cluster id="cluster_id">
      ........
    <server-default>
      ...........
        <jvm-arg> -javaagent:/${路径}/tapm-agent-java.jar</jvm-arg>
      ..........
   </server-default>
      ..........
</cluster>
```

- 针对集群某台 server 增加探针：

```xml
<cluster id="cluster_id">
      ........
    <server id="" address="x.x.xxx.x.x.xxx" port="xxxx">
      ...........
        <jvm-arg> -javaagent:/${路径}/tapm-agent-java.jar</jvm-arg>
      ..........
   </server>
      ..........
</cluster>
```

#### Resin pro 4.0+ production mode

Resin pro 4.0+ 有两种安装方式。

方式一：找到 conf 目录下的 resin.properties 文件，将 JVM 的配置打开，并增加 `-javaagent:/${路径}/tapm-agent-java.jar`，示例如下：

```properties
# Arg passed directly to the JVM
jvm_args: -javaagent:/${路径}/tapm-agent-java.jar
# jvm_mode: -server
```

方式二：增加如下配置：

```xml
<jvm-arg>-javaagent:/${路径}/tapm-agent-java.jar</jvm-arg>
```

多个 serve 和单个 server 配置示例如下：

- 针对集群所有 server 增加探针：

```xml
<cluster id="cluster_id">
      ........
    <server-default>
      ...........
        <jvm-arg> -javaagent:/${路径}/tapm-agent-java.jar</jvm-arg>
      ..........
   </server-default>
      ..........
</cluster>
```

- 针对集群某台 server 增加探针：

```xml
<cluster id="cluster_id">
      ........
    <server id="" address="x.x.xxx.x.x.xxx" port="xxxx">
      ...........
        <jvm-arg> -javaagent:/${路径}/tapm-agent-java.jar</jvm-arg>
      ..........
   </server>
      ..........
</cluster>
```

