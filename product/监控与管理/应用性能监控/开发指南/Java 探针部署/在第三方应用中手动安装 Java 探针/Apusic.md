本文将为您介绍如何在 Apusic 上安装 Java 探针。

## 操作步骤
1. 嵌入TAPM 探针。
   进入 `/${路径}/domains/mydomain/bin` 目录，编辑 startapusic 文件。示例如下：
   ```
   JVM_OPTS="$OTHERS_JVMOPTS $MEMORY_JVMOPTS $GC_JVMOPTS -javaagent:/${路径}/ting
   yun-agent-java.jar "
   ```
2. 重启 Apusic 服务。
	1. 进入 `/${路径}/domains/mydomain/bin` 目录。
	2. 执行以下命令，重启 Apusic 服务。
	```
	nohup ./startapusic &
	```
