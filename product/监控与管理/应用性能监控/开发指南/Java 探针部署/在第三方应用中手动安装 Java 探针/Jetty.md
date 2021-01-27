本文将为您介绍如何在 Jetty 安装 Java 探针。


## 前提条件


- 在安装探针前，请先安装 Agent Collector。
- 在安装探针前，需要先确保本地浏览器时间与服务器时区、时间一致。若有多个服务器，则要保证本地浏览器、多个服务器的时区、时间都一致。否则，可能会影响数据的准确性，例如拓扑不正确等。
- 前往 TAPM 控制台 [探针下载](https://console.cloud.tencent.com/monitor/tapm/addagent) 页面下载 tapm-java-Agent。



## 操作步骤

 Java 探针支持 Jetty [自动安装](self_install.html)，也可以将 `-javaagent `命令行选项添加到 jetty.sh 文件中完成安装，详细步骤如下：

1. 编辑 jetty.sh 启动脚本文件，修改 `JAVA_OPTIONS` 参数，将以下 `javaagent` 参数添加到 `JAVA_OPTIONS`。
<dx-codeblock>
:::  bash
 export JAVA_OPTIONS="${JAVA_OPTIONS} -javaagent:/${路径}/tapm/tapm-agent-java.jar"
:::
</dx-codeblock>
2. 保存 jetty.sh 脚本文件。
4. 重启 Jetty。






