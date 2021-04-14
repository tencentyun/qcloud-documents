本文将为您介绍如何在 WebSphere 上安装 Java探针。





## 前提条件

- 应用性能监控目前处于内测阶段，如需体验需通过 [应用性能监控内测申请](https://cloud.tencent.com/apply/p/f5yvbf09mka)。
- 在安装探针前，请先安装 Agent Collector。
- 在安装探针前，需要先确保本地浏览器时间与服务器时区、时间一致。若有多个服务器，则要保证本地浏览器、多个服务器的时区、时间都一致。否则，可能会影响数据的准确性，例如拓扑不正确等。
- 前往 TAPM 控制台 [探针下载](https://console.cloud.tencent.com/tapm/addagent) 页面下载 tapm-java-Agent。




## 操作步骤

TAPM Java探针支持 WebSphere 7.0 到 8.5.5 的所有版本，除了有部分 8.5.0 的版本与该探针不兼容。

在 WebSphere 上安装 Java 探针有如下两种方式。



### 方式1：通过管理控制台配置探针（推荐）

1. 登录 [WebSphere 管理控制台](https://ip:9043/ibm/consol)。
2. 选择【Servers】>【Application servers】>【选择指定的 Server】。
3. 选择 【Configuration】>【Service Infrastructure】>【Java and Process Management】>【Process Definition】>【Additional Properties】，进入 Additional Properties 页面。
4. 选择【Process Definition】>【Additional Properties】>【Java Virtual Machine】。
5. 在 **Java Virtual Machine** 页面中，打开 **Generic JVM arguments** 选项配置框，增加以下内容：
<dx-codeblock>
:::  plaintext
-javaagent:/${路径}/tapm/tapm-agent-java.jar
:::
</dx-codeblock>
6. 选择【Apply】>【Save】，保存配置。
7. 重启 WebSphere 服务。
>?如果已启用 Java 安全性 (Java 2 Security)，需要授权应用性能监控 TAPM Agent 通过 JMX 获取 PMI 指标。







### 方式2：修改 server.xml 文件（不推荐）

修改 server.xml，文件路径为：`WAS_HOME/AppServer/profiles/app_server_name/config/cells/cell_name/nodes/node_name/servers/server_name/server.xml`。添加如下：
```xml
 ...
		 <jvmEntries ... genericJvmArguments="-javaagent:/${路径}/tapm/tapm-agent-java.jar" ... >
		 ...
		 </jvmEntries>
 ...
```



#### 安全性（Java 2 Security）配置说明

如果您使用的是 Java 2 Security 或 WebSphere 管理安全性, 需要授予 tapm 目录下所有 jar 文件的执行权限。可以通过修改 **java.policy** 文件启用授予全局安全性，也可以修改某个 Server 的 **server.policy** 文件只授权单个Server 的权限。

#### 授权所有 Server

1. 修改 **java.policy** 文件，文件路径如下：
   ```shell
   WAS_HOME/java/jre/lib/security/java.policy
   ```
2. 将如下内容添加到 java.policy 中，`file:` 后面的路径必须指定到 tapm-agent-java.jar 的目录，并确保最后存在 `-`。
   ```java
   grant codeBase "file:/${路径}/tapm/-" {
       permission java.security.AllPermission;
       permission java.net.SocketPermission "*.tencent.com",
       "connect,accept,resolve";
       permission java.lang.RuntimePermission "createClassLoader";
       permission java.lang.RuntimePermission "getClassLoader";
   };
   ```
3. 重启应用 WebSphere。

#### 授权单个Server

1. 修改 **server.policy** 文件，文件路径如下：
   ```shell
   WAS_HOME/AppServer/profiles/APP_SERVER_NAME/properties/server.policy
   ```
2. 将如下内容添加到 java.policy 中，`file:` 后面的路径必须指定到 tapm-agent-java.jar 的目录，并确保最后存在 `-`。
   ```shell
   grant codeBase "file:/${路径}/tapm/-" {
       permission java.security.AllPermission;
       permission java.net.SocketPermission "*.tencent.com",
       "connect,accept,resolve";
       permission java.lang.RuntimePermission "createClassLoader";
       permission java.lang.RuntimePermission "getClassLoader";
   };
   ```
3. 重启 WebSphere 服务。
> ?每个 Server 最终的安全性都取决于 `java.policy` 和 `server.policy` 的并集，切勿在多个文件配置同样的授权。policy 文件的配置格式及语法可参考 [Default Policy Implementation and Policy File Syntax](http://docs.oracle.com/javase/8/docs/technotes/guides/security/PolicyFiles.html)。
