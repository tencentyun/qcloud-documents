本文将为您介绍如何在 Apusic 上安装 Java 探针。

### 在  Apusic 上安装 Java 探针

探针安装步骤如下：

1. 嵌入TAPM 探针。

   进入 /${路径}/domains/mydomain/bin 目录，编辑 startapusic 文件。示例如下：

   ```
   JVM_OPTS="$OTHERS_JVMOPTS $MEMORY_JVMOPTS $GC_JVMOPTS -javaagent:/${路径}/ting
   
   yun-agent-java.jar "
   ```

2. 重启 Apusic  服务。

   Apusic服务启动方式为：

1. 进入 /${路径}/domains/mydomain/bin 目录。
2. 执行 `nohup ./startapusic &`命令。

