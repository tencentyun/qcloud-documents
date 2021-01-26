

本文将为您介绍如何在 WebLogic 手动安装 Java 探针。

## 在WebLogic上安装Java探针

### 在Linux和Mac下的安装

在 Linux 和 Mac 操作系统下安装 Java 探针的步骤：

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

3. 重启 Weblogic 。

### 在 Windows 下的安装

在 Windows 操作系统下安装 Java 探针的步骤：

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

3. 重启 Weblogic 。

### 管理控制台安装

当使用 Node Manager 来启动和停止被管理的服务器时，采用以下的步骤来安装 Java 探针：

1. 从管理控制台中，浏览：**Environments > Servers > (select your server) > Server Start > Arguments**。

   ![](https://main.qcloudimg.com/raw/2d12377f3d472103f17bec9e5b26b7b7.png)

2. 在 **Arguments** 选项的文本框中增加以下内容。

   ```shell
   -javaagent:"/${路径}/tapm-agent-java.jar"
   ```

### 