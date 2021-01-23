本文将为您介绍如何在 Glassfish 手动安装 Java 探针。

### 在 Glassfish 上安装 Java 探针

在 Glassfish 上安装 Java 探针的步骤如下：


1. 访问 Glassfish 配置界面。
2. 从左侧菜单依次选择： **Configurations -> server-config -> JVM Settings -> JVM Options**。
3. 在 JVM Options 页面，选择 **Add JVM Option**。
4. 添加一个条目，配置`-javaagent`参数。
   ```shell
   -javaagent:/${路径}/tapm-agent-java.jar
   ```
5. 保存设置。
6. 重启应用服务器。

> ?如果 Glassfish 不能够正常启动，可能是 -javaagent 参数配置错误。可以通过编辑 **domain.xml** 正确配置-javaagent 参数。
>
> domain.xml 参考地址：GLASSFISH_HOME/glassfish/domains/{domain}/config/domain.xml。

