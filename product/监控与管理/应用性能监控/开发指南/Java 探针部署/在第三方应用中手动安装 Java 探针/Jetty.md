本文将为您介绍如何在 Jetty 安装 Java 探针。

### 在Jetty上安装Java探针

 Java 探针支持 Jetty [自动安装](self_install.html)，也可以将 `-javaagent `命令行选项添加到 `jetty.sh `文件中完成安装，如下所示：

1. 打开 jetty.sh 启动脚本文件。

2. 编辑`JAVA_OPTIONS`参数，将以下`javaagent`参数添加到`JAVA_OPTIONS`。

   ```shell
   export JAVA_OPTIONS="${JAVA_OPTIONS} -javaagent:/${路径}/tapm/tapm-agent-java.jar"
   ```

3. 保存脚本文件。

4. 重新启动应用服务器 Jetty 。

