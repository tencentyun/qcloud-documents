本文将为您介绍如何在 WebSphere 上安装 Java探针。

## 在 WebSphere 上安装 Java 探针

TAPM Java探针支持 WebSphere 7.0 到 8.5.5 的所有版本，除了有部分 8.5.0 的版本与该探针不兼容。

在 WebSphere 上安装 Java 探针有如下两种方式。

#### 方式一：通过管理控制台配置探针**(推荐)**

1. 登录 [WebSphere管理控制台](https://ip:9043/ibm/consol)。

2. 浏览：**Servers > Application servers > (选择指定的Server)**。

3. 选择：**Configuration > Service Infrastructure > Java and Process Management > Process Definition > Additional Properties**。

4. 在 **Process Definition > Additional Properties**下，选择 **Java Virtual Machine**。

5. 在 **Java Virtual Machine** 页面中，在 **Generic JVM arguments** 选项的文本框中，增加以下内容。

   ```shell
    -javaagent:/${路径}/tapm/tapm-agent-java.jar
   ```

6. 点击 **Apply** 按钮，然后点击 **Save** 按钮。

7. 重启服务。

> **说明**：如果启用了 Java 安全性 (Java 2 Security), 需要授权应用性能监控 TAPM Agent通过JMX获取PMI指标。

### 方式二：修改 server.xml 文件**(不推荐)**

文件路径大致为：WAS_HOME/AppServer/profiles/app_server_name/config/cells/cell_name/nodes/node_name/servers/server_name/server.xml


```xml
   ...
       <jvmEntries ... genericJvmArguments="-javaagent:/${路径}/tapm/tapm-agent-java.jar" ... >
       ...
       </jvmEntries>
   ...
```

#### 安全性（Java 2 Security）配置说明

如果您使用的是 Java 2 Security 或 WebSphere 管理安全性, 需要授予 tapm 目录下所有 jar 文件的执行权限。可以通过修改 **java.policy** 文件启用授予全局安全性，也可以修改某个 Server 的 **server.policy** 文件只授权单个Server 的权限。

##### 授权所有 Server

1. 修改 **java.policy** 文件,文件路径大概为：

   ```shell
   WAS_HOME/java/jre/lib/security/java.policy
   ```

2. 将如下内容添加到java.policy中，`file:`后面的路径必须指定到tapm-agent-java.jar的目录，并确保最后存在`-`。

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

##### 授权单个Server

1. 修改 **server.policy** 文件,文件路径大概为：

   ```shell
   WAS_HOME/AppServer/profiles/APP_SERVER_NAME/properties/server.policy
   ```

2. 将如下内容添加到 java.policy 中，`file:`后面的路径必须指定到 tapm-agent-java.jar 的目录，并确保最后存在`-`。

   ```shell
   grant codeBase "file:/${路径}/tapm/-" {
       permission java.security.AllPermission;
       permission java.net.SocketPermission "*.tencent.com",
       "connect,accept,resolve";
       permission java.lang.RuntimePermission "createClassLoader";
       permission java.lang.RuntimePermission "getClassLoader";
   };
   ```

3. 重启应用 WebSphere。

> ?每个Server最终的安全性都取决于`java.policy`和`server.policy`的并集，切勿在多个文件配置同样的授权。policy文件的配置格式及语法可参考 [Default Policy Implementation and Policy File Syntax](http://docs.oracle.com/javase/8/docs/technotes/guides/security/PolicyFiles.html)。