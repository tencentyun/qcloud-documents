本文将为您介绍如何在 TongWeb 环境安装 Java 探针。

## 前提条件

- 应用性能监控目前处于内测阶段，如需体验需通过 [应用性能监控内测申请](https://cloud.tencent.com/apply/p/f5yvbf09mka)。
- 在安装探针前，请先安装 Agent Collector。
- 在安装探针前，需要先确保本地浏览器时间与服务器时区、时间一致。若有多个服务器，则要保证本地浏览器、多个服务器的时区、时间都一致。否则，可能会影响数据的准确性，例如拓扑不正确等。
- 前往 TAPM 控制台 [探针下载](https://console.cloud.tencent.com/tapm/addagent) 页面下载 tapm-java-Agent。



## 操作步骤

### 配置启动脚本

嵌入TAPM 探针，请进入 `/${路径}/bin` 目录，编辑 startserver.sh。

```
JAVA_OPTS="${JAVA_OPTS} -javaagent:/${路径}/tapm/tapm-agent-java.jar"
```

### 权限配置

需要保证启动 TongWeb 的用户具有读写 agent_install_path 的权限，保证读写权限由两部分组成：

1. 系统读写权限，可以设置将安装路径 agentPath 的所有者设置为启动 TongWeb 的用户，执行如下命令：
   ```
   chown -R <用户>:<用户组> <agent_install_path>
   chmod u+rw <agentPath>
   ```
2. 如启用 TongWeb 的安全管理配置，需在 /${路径}/conf/tongweb.policy 添加如下代码：
   ```
   grant codeBase "file:/<agent_install_path>/-"{
         permission java.security.AllPermission;
   };      
   ```
3. 完成启动脚本和权限配置后，重启TongWeb服务即可。
> ?
> - 若使用 root 户权限启动 TongWeb 则无需修改系统读写权限部分配置。
> - TongWeb 服务启动方式为：进入 `/${路径}/bin` 目录，执行 `nohup ./startserver.sh &` 命令。




### Spring-boot/独立jar包/其它应用服务器

Java 探针可以运行在任何应用服务器上，只要在启动的参数中配置：

```
java -javaagent:/${路径}/tapm-agent-java.jar -jar ${您的应用}.jar
```

>?-javaagent 必须放置在 -jar 之前。

### 通过添加 JVM 参数安装

配置 JAVA_OPTS，在 `-javaagent` 后加以下三个参数，中间以空格分隔，示例如下：
```
	-Dtapm.app_name=${APP_NAME}
	-Dtapm.license_key=${LICENSE_KEY}
	-Dtapm.collector.addresses=${COLLECTOR_ADDRESSES}
```

- **-Dtapm.app_name**：应用名称，建议配置为应用的业务名称。
- **-Dtapm.license_key**：与您的听云账号关联。探针采集到的数据，会上传到该 LicenseKey 绑定的账号下。
- **-Dtapm.collector.addresses**：Agent Collector 服务器的地址和端口号，例如 ap-guangzhou.tapm.tencentcs.com。Agent Collector 在高可用部署模式下，请务必将同一机房内所有的 Agent Collector 服务器地址和端口号都配入，以英文逗号分隔。
