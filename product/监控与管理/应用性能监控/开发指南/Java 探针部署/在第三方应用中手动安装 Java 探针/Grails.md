本文将为您介绍如何在 Grails 上安装 Java 探针。


## 前提条件

- 应用性能监控目前处于内测阶段，如需体验需通过 [应用性能监控内测申请](https://cloud.tencent.com/apply/p/f5yvbf09mka)。
- 在安装探针前，请先安装 Agent Collector。
- 在安装探针前，需要先确保本地浏览器时间与服务器时区、时间一致。若有多个服务器，则要保证本地浏览器、多个服务器的时区、时间都一致。否则，可能会影响数据的准确性，例如拓扑不正确等。
- 前往 TAPM 控制台 [探针下载](https://console.cloud.tencent.com/tapm/addagent) 页面下载 tapm-java-Agent。



## 操作步骤



### 使用 run-app 启动 Grails

当使用 `grails run-app` 启动服务时，需要在 run-app 之前增加 `-javaagent` 参数，示例如下：

```bash
grails -noreloading -javaagent:/${路径}/tapm-agent-java.jar run-app
```

> ?`-noreloading` 参数只需在 Grails 2.x 版本添加。

### 使用 run-war 启动 Grails

修改 `{your-grails-app}/conf/BuildConfig.groovy ` 文件，在 `grails.tomcat.jvmArgs` 属性里添加 `-javaagent` 参数，示例如下：

```bash
grails.tomcat.jvmArgs = ["-javaagent:/${路径}/tapm-agent-java.jar"]
```

