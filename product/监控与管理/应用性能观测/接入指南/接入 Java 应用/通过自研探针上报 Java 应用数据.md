
本文将介绍以下两种方式自动安装自研探针：

- [通过修改配置文件安装](#conf)
- [通过添加 JVM 参数安装，无需修改配置文件](#addjvm)

## 前提条件

- 在安装探针前，需要先确保本地浏览器时间与服务器时区、时间都一致。若有多个服务器，则要保证本地浏览器、多个服务器的时区、时间都一致。否则，可能会影响数据的准确性，例如拓扑不正确等。
- 下载  [自研SDK](https://apm-sdk-1258344699.cos.ap-guangzhou.myqcloud.com/tapm-agent-java-3.6.1.5.zip)。

## 操作步骤
### 通过修改配置文件安装[](id:conf)


<dx-tabs>
::: Linux/Mac
1. 执行以下命令，解压 Agent 安装文件包到您的应用服务器的根目录。示例如下：
<dx-codeblock>
:::  plaintext
unzip tapm-agent-java-x.x.x.zip -d /path/to/appserver/
:::
</dx-codeblock><dx-alert infotype="explain" title="">
“`/path/to/appserver`” 为示例路径，请用户根据自身不同的环境修改正确的目录。
例如: 应用服务器的根目录为： /path/to/tomcat，则解压后tapm所处目录为： /path/to/tomcat。
</dx-alert>
2. 修改解压 tapm 目录下的 tapm.properties 文件。
	需修改文件中的 license_key、app_name 和 collector.addresses 两个配置项，否则探针无法进行数据采集也无法启动探针。其他配置项，可根据实际需要进行配置。
	- **license_key**：填写在 [应用性能观测控制台](https://console.cloud.tencent.com/apm) 接入应用时获取的 token。与您的应用性能观测账号关联。探针采集到的数据，会上传到该 LicenseKey 绑定的账号下。
	- **app_name**：自定义应用名称，建议配置为应用的业务名称。
	- **collector.addresses**：填写在 [应用性能观测控制台](https://console.cloud.tencent.com/apm) 接入应用时获取的接入点。例如 tapm.ap-guangzhou.api.tencentyun.com:80。
3. 在 tapm 目录下执行以下命令自动安装探针。
```plaintext
java -javaagent:/data/service/APM/java/tapm/tapm-agent-java-3.6.1.5/tapm/tapm-agent-java.jar -jar watch-0.0.1-SNAPSHOT.jar

```
4. 启动或重启应用服务器。
5. 登录应用性能观测控制台查看性能数据。
重启5分钟后，当您的 Java 应用服务有 HTTP 请求进入，性能数据将发送到应用性能观测系统。

:::
::: Windows

1.  打开 `tapm-agent-java-x.x.x.zip`。
2. 拷贝 tapm 目录到您的应用服务器的根目录。
<dx-alert infotype="explain" title="">
例如: 应用服务器的根目录为： /path/to/tomcat，则解压后tapm所处目录为： /path/to/tomcat。
</dx-alert>
3. 修改放在服务器解压的 tapm 目录下 tapm.properties 文件。
   修改文件中的 license_key、app_name 和 collector.addresses 配置项，否则探针无法进行数据采集也无法启动探针。对于其他配置项，请根据实际需要进行配置。配置说明如下：
   - **license_key**：填写在 [应用性能观测控制台](https://console.cloud.tencent.com/apm) 接入应用时获取的 token。与您的应用性能观测账号关联。探针采集到的数据，会上传到该 LicenseKey 绑定的账号下。
   - **app_name**：自定义应用名称，建议配置为应用的业务名称。
   - **collector.addresses**：填写在 [应用性能观测控制台](https://console.cloud.tencent.com/apm) 接入应用时获取的接入点。例如 tapm.ap-guangzhou.api.tencentyun.com:80。
4. 在命令行窗口执行：(唤起控制台：Windows键+ **R**，然后输入**cmd**)。
<dx-codeblock>
:::  plaintext
java -javaagent:/data/service/APM/java/tapm/tapm-agent-java-3.6.1.5/tapm/tapm-agent-java.jar -jar watch-0.0.1-SNAPSHOT.jar

:::
</dx-codeblock>
5. 启动或重启您的应用服务器。
6. 登录应用性能观测控制台查看性能数据。
7. 重启5分钟后，当您的 Java 应用服务有 HTTP 请求进入，性能数据将发送到应用性能观测系统。
    :::
    </dx-tabs>

>?如果在几分钟之内，无任何应用性能数据，请确保以下信息是否正确：
> - 请按照以上步骤重新查看是否安装正确、目录是否正确、启动脚本是否正确。
> - 请检查 `tapm.properties` 中的 `license_key` 是否与您在应用性能观测控制台的 token 一致。



### 通过添加 JVM 参数安装[](id:addjvm)

配置 JAVA_OPTS，需在 `-javaagent` 后加入以下三个参数，中间以空格分隔：
```
	-Dtapm.app_name=${APP_NAME}
	-Dtapm.license_key=${LICENSE_KEY}
	-Dtapm.collector.addresses=${COLLECTOR_ADDRESSES}
```

参数说明如下：

- **-Dtapm.app_name**：自定义应用名称，建议配置为应用的业务名称。
- **-Dtapm.license_key**：填写在 [应用性能观测控制台](https://console.cloud.tencent.com/apm) 接入应用时获取的 token。与您的应用性能观测账号关联。探针采集到的数据，会上传到该 LicenseKey 绑定的账号下。
- **-Dtapm.collector.addresses**：填写在 [应用性能观测控制台](https://console.cloud.tencent.com/apm) 接入应用时获取的接入点。例如 tapm.ap-guangzhou.api.tencentyun.com:80。Agent Collector 是指服务器的地址和端口号，Agent Collector 在高可用部署模式下，请务必将同一机房内所有的 Agent Collector 服务器地址和端口号都配置进来，以英文逗号分隔。


**使用示例：**

```
java -javaagent:/path/to/appserver/tapm/tapm-agent-java.jar  -Dtapm.app_name={APP_NAME} -Dtapm.collector.addresses={COLLECTOR_ADDRESSES} -Dtapm.license_key={LICENSE_KEY} -jar application.jar
```

>?其中 application.jar 为您所要监控的应用。

上述参数为可选参数，当在启动时配置以上参数，将会替换配置文件中相对应的参数。因此，当启动参数未配置上述参数时，系统将会自动获取配置文件(tapm.properties)中的参数。
