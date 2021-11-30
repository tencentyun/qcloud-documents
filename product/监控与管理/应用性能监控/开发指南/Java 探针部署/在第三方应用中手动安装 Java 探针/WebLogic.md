本文将为您介绍如何在 WebLogic 手动安装 Java 探针。



## 前提条件

- 应用性能监控目前处于内测阶段，如需体验需通过 [应用性能监控内测申请](https://cloud.tencent.com/apply/p/f5yvbf09mka)。
- 在安装探针前，请先安装 Agent Collector。
- 在安装探针前，需要先确保本地浏览器时间与服务器时区、时间一致。若有多个服务器，则要保证本地浏览器、多个服务器的时区、时间都一致。否则，可能会影响数据的准确性，例如拓扑不正确等。
- 前往 TAPM 控制台 [探针下载](https://console.cloud.tencent.com/tapm/addagent) 页面下载 tapm-java-Agent。


## 操作步骤


<dx-tabs>
::: Linux/Mac
1. 在 domain 的 **bin** 目录下找到 **startWebLogic.sh** 文件。
 ```shell
 WEBLOGIC_HOME/user_projects/domains/domain_name/bin/startWeblogic.sh
 ```
2. 修改文件，在`# START WEBLOGIC`和`echo "starting weblogic with Java version:"`之间增加探针配置。示例如下：
   ```shell
   ...
   # START WEBLOGIC
   
   export JAVA_OPTIONS="$JAVA_OPTIONS -javaagent:/${路径}/tapm/tapm-agent-java.jar"
   
   echo "starting weblogic with Java version:"
   ...
   ```
3. 重启 Weblogic。
:::
::: Windows
1. 在 domain 的 **bin** 目录下找到 **startWebLogic.bat** 文件。
   ```shell
   WEBLOGIC_HOME/user_projects/domains/domain_name/bin/startWeblogic.bat
   ```
2. 修改文件，在`# START WEBLOGIC`和`echo "starting weblogic with Java version:"`之间增加探针配置。
   ```shell
   ...
   # START WEBLOGIC
   
   set JAVA_OPTIONS=%JAVA_OPTIONS% -javaagent:C:\${路径}\tapm\tapm-agent-java.jar
   
   echo "starting weblogic with Java version:"
   ...
   ```
3. 重启 Weblogic。
:::
::: 管理控制台安装
当使用 Node Manager 来启动和停止被管理的服务器时，可采用以下的步骤来安装 Java 探针：

1. 从管理控制台中，浏览：**Environments > Servers > (select your server) > Server Start > Arguments**。
   ![](https://main.qcloudimg.com/raw/2d12377f3d472103f17bec9e5b26b7b7.png)
2. 在 **Arguments** 选项的文本框中增加以下内容。
   ```shell
   -javaagent:"/${路径}/tapm-agent-java.jar"
   ```
:::
</dx-tabs>
