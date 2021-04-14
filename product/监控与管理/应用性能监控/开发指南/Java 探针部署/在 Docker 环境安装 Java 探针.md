本文将为您介绍如何在 Docker 环境安装 Java 探针。





## 前提条件

- 应用性能监控目前处于内测阶段，如需体验需通过 [应用性能监控内测申请](https://cloud.tencent.com/apply/p/f5yvbf09mka)。
- 安装人员熟悉 Java 探针的手动安装过程。详情请参见手动安装 [概述](https://cloud.tencent.com/document/product/1349/52391)。
- 在安装探针前，需要先确保本地浏览器时间与服务器时区、时间都一致。若有多个服务器，则要保证本地浏览器、多个服务器的时区、时间都一致。否则，可能会影响数据的准确性，例如拓扑不正确等。
- 前往 TAPM 控制台 [探针下载](https://console.cloud.tencent.com/tapm/addagent) 页面下载  tapm-java-Agent。


## 操作步骤

### Docker 容器内部安装 Java 探针

1. 执行以下命令，查看本地镜像。
```plaintext
docker images
```
2. 执行以下命令，查看正在运行的容器。
```plaintext
docker ps
```
3. 执行以下命令，容器id /bin/bash`命令。
```plaintext
docker exec -it
```
 >?其他的步骤请参见手动安装 [概述](https://cloud.tencent.com/document/product/1349/52391) 。

### Dockerfile 形式安装 Java 探针

#### 通过修改配置文件安装 Java 探针

1. 配置 Dockerfile文件，  以 Tomcat 环境为例，Dockerfile 文件中探针嵌码相关的配置，需执行以下命令：
```
#添加探针安装包到 docker 镜像并指定解压目录 /opt/apache-tomcat-8.5.11/ 
ADD tapm-agent-java-x.x.x.zip /opt/apache-tomcat-8.5.11/  
# 修改 tapm.properties 文件 和 catalina.sh 配置文件
# 修改license_key
RUN sed -i 's/<%=license_key%>/oiHC****Z3Il4zd' /opt/apache-tomcat-8.5.11/tapm/tapm.properties
# 增加Agent Collector服务器的地址和端口号
RUN sed -i 's/<%=collector_addresses>/ap-guangzhou.tapm.tencentcs.com' /opt/apache-tomcat-8.5.11/tapm/tapm.properties
# 修改应用名称
RUN set -i 's/Java Application/docker_appname' /opt/apache-tomcat-8.5.11/tapm/tapm.properties
```
 >?部分 Dockerfile 生成的容器不支持 unzip 命令，建议先将探针的zip包解压，再打成 tar.gz 的包再上传。
2. 备份修改的脚本文件，执行如下命令：
```plaintext
RUN cp /opt/apache-tomcat-8.5.11/bin/catalina.sh /opt/apache-tomcat-8.5.11/bin/catalina.sh.bak
``` 
3. 增加探针启动参数，执行如下命令：
```plaintext
RUN sed -i '1a\export CATALINA_OPTS="$CATALINA_OPTS -javaagent:/opt/apache-tomcat-8.5.11/tapm/tapm-agent-java.jar"' /opt/apache-tomcat-8.5.11/bin/catalina.sh
```
4. 执行以下命令，此时创建出来的镜像则包含 Java 探针。
```plaintext
docker build
```
5. 基于镜像，创建容器并运行，查看探针日志和报表，观察性能数据上传是否正常。



#### 通过添加 JVM 参数安装

配置  JAVA_OPTS，在 `-javaagent` 后加以下三个参数，中间以空格分隔。执行命令如下：
```
	-Dtapm.app_name=${APP_NAME}
	-Dtapm.license_key=${LICENSE_KEY}
	-Dtapm.collector.addresses=${COLLECTOR_ADDRESSES}
```
- **-Dtapm.app_name**：应用名称，建议配置为应用的业务名称。
- **-Dtapm.license_key**：与您的应用性能监控 TAPM 账号关联。探针采集到的数据，会上传到该 LicenseKey 绑定的账号下。
- **-Dtapm.collector.addresses**：Agent Collector 服务器的地址和端口号，例如 ap-guangzhou.tapm.tencentcs.com。Agent Collector 在高可用部署模式下，请务必将同一机房内所有的 Agent Collector 服务器地址和端口号都配入，以英文逗号分隔。
