本文将为您介绍如何使用 Skywalking 协议上报 Java 应用数据。

## 前提条件[](id:before)

- 打开 [SkyWalking](https://archive.apache.org/dist/skywalking/8.5.0/) 下载页面，下载 SkyWalking8.5.0 以上的（包含8.5.0）版本，并将解压后的 Agent 文件夹放至 Java 进程有访问权限的目录。
- 插件均放置在/plugins 目录中。在启动阶段将新的插件放进该目录，即可令插件生效。将插件从该目录删除，即可令其失效。另外，日志文件默认输出到/logs 目录中。

## 接入步骤

### 步骤1：获取接入点和 Token
进入 [应用性能观测控制台](https://console.cloud.tencent.com/apm) **应用监控** > **应用列表**页面，单击**接入应用**，在接入应用时选择 Java 语言与 SkyWalking 的数据采集方式。
在选择接入方式步骤获取您的接入点和 Token，如下图所示：
![](https://main.qcloudimg.com/raw/d7d94913947d31edf70e85c6462c6bac.png)


### 步骤2：下载 Skywalking
- 若您已经使用了 SkyWalking，可跳过本步骤。
- 若您还未使用 SkyWalking，建议 [下载最新版本](http://skywalking.apache.org/downloads/?spm=a2c4g.11186623.2.12.65355968AbUoDc)，下载方式参见 [前提条件](#before)。

### 步骤3：配置相应参数及名称

Skywalking Agent 支持多种方式完成参数配置，不同配置方式之间可以彼此组合，下面给出配置方式及其示例。

#### 方法1：使用 agent.config 文件配置

打开 agent/config/agent.config 文件，配置接入点、 Token 和自定义服务名称。

```ini
collector.backend_service=<接入点>
agent.authentication=<Token>
agent.service_name=<上报的服务名称>
```

>?修改完 `agent.config` 需要把配置项前反注释符号`#`去掉。否则更改的信息将无法生效。

#### 方法2：Java VM Options

启动 Java 应用程序时，在命令行中添加相应以 -DSkywalking 开头的参数,以下给出方法一的等效范例。

```
java -javaagent:<步骤一目录绝对路径>/skywalking-agent.jar 
-Dskywalking.collector.backend_service==<接入点>
-Dskywalking.agent.authentication=<Token>
-Dskywalking.agent.service_name=<上报的服务名称> 要启动的程序
```

#### 方法3：设置相应环境变量

可以在系统中设置相应环境变量来完成 skywalking 客户端的配置，以下为 Linux 命令的示例。

```
export SW_AGENT_AUTHENTICATION=<Token> (等效于agent.authentication=Token)
export SW_AGENT_NAME=<上报的服务名称> (等效于agent.service_name=<上报的服务名称>)
export SW_AGENT_COLLECTOR_BACKEND_SERVICES=<接入点>(等效于collector.backend_service=接入点)
```

>? 以上三种方式读取优先级关系为：服务器配置->环境变量->配置文件。优先级高的配置会将优先级的低的配置覆盖。

### 步骤4：选择相应方法指定插件路径

根据应用的运行环境，选择相应的方法来指定 SkyWalking Agent 的路径。
- Linux Tomcat 7/Tomcat 8 
  在 `tomcat/bin/catalina.sh` 第一行添加以下内容：
 ```routeros
CATALINA_OPTS="$CATALINA_OPTS -javaagent:<skywalking-agent-path>"; export CATALINA_OPTS
```
- Jetty
```routeros
在{JETTY_HOME}/start.ini配置文件中添加以下内容：
--exec # 去掉前面的井号取消注释。 
-javaagent:<步骤一目录绝对路径>
```

- JAR File 或 Spring Boot 
  在应用程序的启动命令行中添加 `-javaagent` 参数（-javaagent 参数一定要放在 -jar 参数之前），参数内容如下：
```
java -javaagent:<skywalking-agent-path> -jar yourApp.jar
```
- IDEA
  在 IDEA 中运行时，可在 Configuration 中配置应用程序的 VM option,添加 -javaagent 参数，参数配置如上一致。
	
### 步骤5：重新启动应用
完成上述部署步骤后，参见 [Skywalking 官网指导](https://github.com/apache/skywalking/blob/v8.2.0/docs/en/setup/service-agent/java-agent/README.md#install-javaagent-faqs) 重新启动应用即可。


