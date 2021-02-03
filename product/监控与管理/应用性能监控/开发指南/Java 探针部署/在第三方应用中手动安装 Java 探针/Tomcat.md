本文将为您介绍如何在 Tomcat 手动安装 Java 探针。


## 前提条件

- 应用性能监控目前处于内测阶段，如需体验需通过 [应用性能监控内测申请](https://cloud.tencent.com/apply/p/f5yvbf09mka)。
- 在安装探针前，请先安装 Agent Collector。
- 在安装探针前，需要先确保本地浏览器时间与服务器时区、时间一致。若有多个服务器，则要保证本地浏览器、多个服务器的时区、时间都一致。否则，可能会影响数据的准确性，例如拓扑不正确等。
- 前往 TAPM 控制台 [探针下载](https://console.cloud.tencent.com/tapm/addagent) 页面下载 tapm-java-Agent。



##  操作步骤


不同操作系统版本的 Tomcat 安装 Java 探针不同，请参考以下步骤进行安装：


<dx-tabs>
::: Linux
修改 catalina.sh ，配置 JAVA_OPTS。示例如下：
```
export JAVA_OPTS="$JAVA_OPTS -javaagent: /${路径}/tapm-agent-java.jar"
```
:::
::: Windows
大多数 Windows 用户都把 Tomcat 作为服务来运行，Tomcat 提供了一个配置程序来指定该服务的 JVM 参数。

1. 在 Windows 系统中，选择【Start】>【Apache Tomcat (Version)】>【Configure Tomcat】。
2. 在 Configure Tomcat 页面选择【Java】。
3. 在 **Java Options** 文本框中的行末增加，请使用正斜杠作为路径分隔符。示例如下，详细说明可参考 [javaagent](#javaagent)。
```shell
-javaagent:/${路径}/tapm-agent-java.jar
```
4. 单击【Apply】应用配置。
5. 重启 Tomcat 服务。
:::
</dx-tabs>



   



## javaagent 说明[](id:javaagent)

1. 设置 `-javaagent` 参数时，请使用正斜杠作为路径分隔符，示例如下：
```shell
-javaagent:C:/tapm/tapm-agent-java.jar
```
2. 对于 Tomcat 6 版本，在 `-javaagent` 参数之后需要有回车符。并且路径分隔符可以使用正斜杠和反斜杠。
如果您使用 **catalina.bat** 来启动 Tomcat ，请在该批处理文件的顶部增加以下内容：
 ```shell
 SET JAVA_OPTS=%JAVA_OPTS% -javaagent:/${路径}/tapm-agent-java.jar
 ```
3. Tomcat 6 中自带的 Apache Commons Daemon(jsvc) 不支持`-javaagent`参数。关于该问题的描述请参见 [官方文档说明](http://issues.apache.org/jira/browse/DAEMON-84)。
在 Apache Commons 源代码仓库中已经包含了该问题的修复版本。详情请参见：
	- [Apache 源代码仓库](http://commons.apache.org/svninfo.html)
	- [Apache SVN 源代码仓库](http://svn.apache.org/repos/asf/commons/proper/daemon/)

 您也可以直接下载编译好的 [jsvc 版本](http://www.apache.org/dist/commons/daemon/binaries/) 。该版本的 jsvc 支持通过 `-X` 前缀来设置 `-javaagent` 参数。
