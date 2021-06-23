本文将为您介绍如何在 Resin 安装 Java 探针。



## 前提条件

- 应用性能监控目前处于内测阶段，如需体验需通过 [应用性能监控内测申请](https://cloud.tencent.com/apply/p/f5yvbf09mka)。
- 在安装探针前，请先安装 Agent Collector。
- 在安装探针前，需要先确保本地浏览器时间与服务器时区、时间一致。若有多个服务器，则要保证本地浏览器、多个服务器的时区、时间都一致。否则，可能会影响数据的准确性，例如拓扑不正确等。
- 前往 TAPM 控制台 [探针下载](https://console.cloud.tencent.com/tapm/addagent) 页面下载 tapm-java-Agent。



## 操作步骤

### Resin pro 3.1+ production mode


找到 conf 目录下的 resin.conf 文件，增加如下配置 ：

```xml
<jvm-arg>-javaagent:/${路径}/tapm-agent-java.jar</jvm-arg>
```

多个 server 和单个 server 配置示例如下：

<dx-tabs>
:::  针对集群所有\sserver\s增加探针：
<dx-codeblock>
:::  xml
```
<cluster id="cluster_id">
      ...
    <server-default>
      ...
        <jvm-arg> -javaagent:/${路径}/tapm-agent-java.jar</jvm-arg>
      ...
   </server-default>
      ...
</cluster>
```
:::
</dx-codeblock>
:::
::: 针对集群某台\sserver\s增加探针：
<dx-codeblock>
:::  xml
```
<cluster id="cluster_id">
      ...
    <server id="" address="x.x.xxx.x.x.xxx" port="xxxx">
      ...
        <jvm-arg> -javaagent:/${路径}/tapm-agent-java.jar</jvm-arg>
      ...
   </server>
      ...
</cluster>
```
:::
</dx-codeblock>
:::
</dx-tabs>






### Resin pro 4.0+ production mode

Resin pro 4.0+ 有两种安装方式。

#### 方式1


找到 conf 目录下的 resin.properties 文件，将 JVM 的配置打开，并增加 `-javaagent:/${路径}/tapm-agent-java.jar`，示例如下：
```properties
# Arg passed directly to the JVM
jvm_args: -javaagent:/${路径}/tapm-agent-java.jar
# jvm_mode: -server
```




#### 方式2

增加如下配置：
```xml
<jvm-arg>-javaagent:/${路径}/tapm-agent-java.jar</jvm-arg>
```

多个 server 和单个 server 配置示例如下：

<dx-tabs>
::: 针对集群所有\sserver\s增加探针：
<dx-codeblock>
:::  xml
```
<cluster id="cluster_id">
      ...
    <server-default>
      ...
        <jvm-arg> -javaagent:/${路径}/tapm-agent-java.jar</jvm-arg>
      ...
   </server-default>
      ...
</cluster>
```
:::
</dx-codeblock>
:::
::: 针对集群某台\sserver\s增加探针：
<dx-codeblock>
:::  xml
```
<cluster id="cluster_id">
      ...
    <server id="" address="x.x.xxx.x.x.xxx" port="xxxx">
      ...
        <jvm-arg> -javaagent:/${路径}/tapm-agent-java.jar</jvm-arg>
      ...
   </server>
      ... 
</cluster>
```
:::
</dx-codeblock>
:::
</dx-tabs>

