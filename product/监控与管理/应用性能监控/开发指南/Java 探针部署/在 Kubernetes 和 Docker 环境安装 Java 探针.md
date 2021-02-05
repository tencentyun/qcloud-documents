本文将为您介绍如何在 Kubernetes 和 Docker 环境安装 Java 探针。

## 前提条件

- 应用性能监控目前处于内测阶段，如需体验需通过 [应用性能监控内测申请](https://cloud.tencent.com/apply/p/f5yvbf09mka)。
- 安装人员熟悉 Java 探针的手动安装。详情请参见手动安装 [概述](https://cloud.tencent.com/document/product/1349/52391)。
- 在安装探针前，需要先确保本地浏览器时间与服务器时区、时间都一致。若有多个服务器，则要保证本地浏览器、多个服务器的时区、时间都一致。否则，可能会影响数据的准确性，例如拓扑不正确等。
- 前往 TAPM 控制台 [探针下载](https://console.cloud.tencent.com/tapm/addagent) 页面下载  tapm-java-Agent。



## 注意事项

- 本文基于 Tomcat 服务开发的一个项目为例介绍 Java 探针的手动安装步骤。
- 使用的镜像依赖关系：
   jdk8（基础镜像）- build > jdk8-tomcat8-demo（服务镜像）- build > tomcat-agent-demo（应用镜像）
- 以下介绍中，基础镜像所在环境系统为 CentOS 。其他操作系统例如 RedHat、Ubuntu、Debian 同样可基于以下步骤作为参考。




## 操作步骤

#### 配置脚本

Kubernetes 和 Docker 环境下服务启动方式为：编写类似 run.sh 脚本，在容器启动后执行。脚本配置完成后，探针会随着容器的创建和运行而自动部署。

镜像内置的服务原始启动脚本 run.sh 内容如下：

```
#!/bin/bash

TOMCAT_SERVER_CONF="/opt/apache-tomcat/conf/server.xml"
sed -i "s#CONNECTOR#$CONNECTOR#"  $TOMCAT_SERVER_CONF
sed -i "s#CONTEXT#$CONTEXT#"    $TOMCAT_SERVER_CONF
sed -i "s#ACCESS_LOG#$ACCESS_LOG#" $TOMCAT_SERVER_CONF
catalina.sh run
```



> ?请勿大范围拷贝以下脚本和 YAML 配置文件内容到 SSH 客户端，否则会引起格式错乱问题。建议直接根据每个配置项的示意按项进行配置。

1. 在服务镜像 jdk8-tomcat8-demo 的 Dockerfile 文件中加入如下代码：
```shell
RUN mkdir -p /script
ADD run.sh /script/run.sh
```
2. 修改 run.sh 文件。包括探针版本、探针下载地址、探针安装目录、应用名称、license_key、collector addresses 等，根据实际情况进行相应替换。注意探针的安装目录不要与其他应用共享。修改示例如下：
<dx-codeblock>
:::  bash
#!/bin/bash
#探针版本
AGENT_VERSION=${AGENT_VERSION}

#探针容器内的安装路径，可将其挂载到容器外，注意此目录严禁与其他共享使用。
TAPM_AGENT_PATH=/opt/tapm_agent

#应用名称
APP_NAME=tomcat-agent-demo

#license_key
LICENSE_KEY=oiHCI********Il4zd

#collector.addresses
COLLECTOR_ADDRESSES=ap-guangzhou.tapm.tencentcs.com

#通过设置 YAML 中的 ENV,修改 Tomcat server.xml 文件
TOMCAT_SERVER_CONF="/opt/apache-tomcat/conf/server.xml"
sed -i "s#CONNECTOR#$CONNECTOR#"  $TOMCAT_SERVER_CONF
sed -i "s#CONTEXT#$CONTEXT#"    $TOMCAT_SERVER_CONF
sed -i "s#ACCESS_LOG#$ACCESS_LOG#" $TOMCAT_SERVER_CONF


#下载探针
function DownLoadAgent() {
 if [ ! -d $TAPM_AGENT_PATH ];then
  mkdir -p $TAPM_AGENT_PATH
  /usr/bin/curl --connect-timeout 10 -m 60 -o $TAPM_AGENT_PATH/tapm-agent-
  java-${AGENT_VERSION}.zip $AGENT_DOWNLOAD_URL
  unzip -d $TAPM_AGENT_PATH $TAPM_AGENT_PATH/tapm-agent-
  java-${AGENT_VERSION}.zip && rm -rf $TAPM_AGENT_PATH/tapm-agent-
  java-${AGENT_VERSION}.zip
 else
  echo "检测发现容器内探针目录已存在，尝试启动探针，如若启动失败，请检查容器内探针目录是否
  完整，可以尝试将整个探针目录删除，重新安装"
 fi
}

#判断是否启用探针
if [ $tapm_agent_ENABLE == "true" ];then
 DownLoadAgent
 if [ $? -eq 0 ];then
  export JAVA_OPTS="$JAVA_OPTS \
           -Dtapm.app_name=${APP_NAME} \
           -Dtapm.license_key=${LICENSE_KEY} \
           -Dtapm.collector.addresses=${COLLECTOR_ADDRESSES} \
           -javaagent:${TAPM_AGENT_PATH}/tapm/tapm-agent-java.jar"
  echo "将探针启动所需的环境变量打入JAVA_OPTS中"
  echo "JAVA_OPTS 更新为：$JAVA_OPTS"
  echo "启动服务及探针"
  catalina.sh run
 else
  echo "Java Agent下载及安装失败,服务未启动，可按以下操作：1.检查错误，直至恢复后启动探针
  及服务。
  2.YAML中AGENT_ENABLE 值设置为false，即关闭探针，启动服务"
 fi
else
 echo "服务启动(未嵌探针)"
 catalina.sh run
fi
:::
</dx-codeblock>
3. 修改应用镜像 tomcat-agent-demo 的 YAML 配置文件，修改示例如下：
<dx-codeblock>
:::  yaml
volumes: 
   #创建configmap目录，目录下放入修改后run.sh脚本(该脚本在原始脚本的基础上进行了探针下载、安装、集成启动的一系列修改) 
   - name: run-config-volume
     configMap: 
     name: tomcat-agent-demo-run-config
:::
</dx-codeblock>
<dx-codeblock>
:::  yaml
 volumeMounts: 
    #新脚本的挂载位置，挂载到容器内原始启动脚本的目录下，替换原始启动脚本
    - name: run-config-volume
      mountPath: /script
:::
</dx-codeblock>
<dx-codeblock>
:::  yaml
containers: 
    - name: tomcat-agent-demo
		image: registry.xxx.com/common/tomcat-agent-demo:15
    #服务启动
		command: ['sh', '/script/run.sh']
        env: 
    #探针安装启动开关，true表示自动安装启动探针，false或其他表示服务不内嵌探针，正常启动
        - name: tapm_agent_ENABLE
          value: "true"
        - name: AGENT_DOWNLOAD_URL
          #Java探针下载地址
          value: "http://xxx.tapm.com/"
:::
</dx-codeblock>
5. 基于应用镜像，创建容器并运行，查看探针日志和报表，观察性能数据上传是否正常。



