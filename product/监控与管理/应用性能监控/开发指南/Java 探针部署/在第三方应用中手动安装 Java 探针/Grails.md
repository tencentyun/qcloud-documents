本文将为您介绍如何在 Grails 上安装 Java 探针。

## 在 Grails 上安装 Java 探针

### 使用 run-app 启动 Grails

当使用 `grails run-app` 启动服务时，需要在 run-app 之前增加 `-javaagent` 参数,示例如下：

```shell
grails -noreloading -javaagent:/${路径}/tapm-agent-java.jar run-app
```

> ?`-noreloading` 参数只在 Grails 2.x 版本需要。

### 使用 run-war 启动 Grails

修改 {**your-grails-app}/conf/BuildConfig.groovy ** 文件，在 `grails.tomcat.jvmArgs` 属性里添加`-javaagent`参数，示例如下：

```properties
grails.tomcat.jvmArgs = ["-javaagent:/${路径}/tapm-agent-java.jar"]
```

### 