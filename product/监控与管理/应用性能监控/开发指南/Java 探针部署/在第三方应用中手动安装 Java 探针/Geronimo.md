本文将为您介绍如何在 Geronimo 上安装 Java 探针。

## 前提条件

- 应用性能监控目前处于内测阶段，如需体验需通过 [应用性能监控内测申请](https://cloud.tencent.com/apply/p/f5yvbf09mka)。
- 在安装探针前，请先安装 Agent Collector。
- 在安装探针前，需要先确保本地浏览器时间与服务器时区、时间一致。若有多个服务器，则要保证本地浏览器、多个服务器的时区、时间都一致。否则，可能会影响数据的准确性，例如拓扑不正确等。
- 前往 TAPM 控制台 [探针下载](https://console.cloud.tencent.com/tapm/addagent) 页面下载 tapm-java-Agent。


## 操作步骤

使用 Geronimo run 启动时，将 tapm-agent-java.jar 添加到 `JAVA_OPTS` 变量里，示例如下：

```shell
export JAVA_OPTS="$JAVA_OPTS -javaagent:/${路径}/tapm-agent-

java.jar" && geronimo run
```
