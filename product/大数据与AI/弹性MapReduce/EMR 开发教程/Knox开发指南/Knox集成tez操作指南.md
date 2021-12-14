本文主要介绍 Knox 集成 tez 的具体操作步骤，主要有安装 tomcat 和 tez-ui、新建 role、配置 timelineserver、配置 tez和启动服务。其中，`172.**.**.9` 为主节点内网 IP，`159.**.**.70` 为主节点外网 IP，tez 版本为0.9.2版本。

## 安装 Tomcat 和 tez-ui 
```
cd  /usr/local/service
wget https://jaydihu-package-1258469122.cos.ap-guangzhou.myqcloud.com/apache-tomcat-9.0.46.tar.gz
tar -zxvf apache-tomcat-9.0.46.tar.gz
mv /usr/local/service/apache-tomcat-9.0.46 /usr/local/service/tomcat
```
修改 tomcat 端口号：
```
vim /usr/local/service/tomcat/conf/server.xml
```
第一处：由8005修改为2020
![](https://main.qcloudimg.com/raw/f2671aa74d382897c4a373d8a994802a.png)                      
第二处：端口由8080改为2000
![](https://main.qcloudimg.com/raw/40176a1db40180919d47924b7544a901.png)

```
mkdir -p /usr/local/service/tomcat/webapps/tez-ui
cp /usr/local/service/tez/tez-ui-0.9.2.war /usr/local/service/tomcat/webapps/tez-ui/
cd /usr/local/service/tomcat/webapps/tez-ui
unzip tez-ui-0.9.2.war
vim ./config/configs.env
```
将 localhost 修改为当前服务器的内网 IP。
![](https://main.qcloudimg.com/raw/c62c7ad792096c3033d1e38ba94a3cbe.png)

## 新建 role
```
vim /usr/local/service/knox/conf/topologies/emr.xml 
```
**修改 emr.xml 配置文件**
第一处：添加内容如下
![](https://main.qcloudimg.com/raw/81c51a74c086002a9089ae2ca676865b.png)
```
<param>
    <name>TEZUI</name>
<value>maxFailoverAttempts=3;failoverSleep=1000;enabled=true</value>
</param>
 <param>
     <name>APPLICATIONHISTORY</name>
<value>maxFailoverAttempts=3;failoverSleep=1000;enabled=true</value>
</param>
```

第二处：修改内容如下
![](https://main.qcloudimg.com/raw/f97bacdc69f9b28a34f4789dbf715991.png)
```
<service>
		<role>TEZUI</role>
		<url>http://172.**.**.9:2000/tez-ui</url>
		<version>0.9.2</version>
</service>
<service>
		<role>APPLICATIONHISTORY</role>
		<url>http://172.**.**.9:8188</url>
		<version>2.7.3</version>
</service>
```

## yarn 的 timelineserver 配置
在配置管理中修改 yarn-site.xml 配置文件，保存配置修改，重启配置发生变化组件。

| 参数                                                      | 值                |
| --------------------------------------------------------- | ----------------- |
| yarn.timeline-service.enabled                             | true              |
| yarn.timeline-service.hostname                            | `172.**.**.9`（需替换为自己的 IP）       |：
| yarn.timeline-service.http-cross-origin.enabled           | true              |
| yarn.resourcemanager.system-metrics-publisher.enabled     | true              |
| yarn.timeline-service.address                             | `172.**.**.9:10201`（需替换为自己的 IP） |
| yarn.timeline-service.webapp.address                      |`172.**.**.9:8188`  （需替换为自己的 IP）|
| yarn.timeline-service.webapp.https.address                | `172.**.**.9:2191` （需替换为自己的 IP） |
| yarn.timeline-service.generic-application-history.enabled | true              |
| yarn.timeline-service.handler-thread-count                | 24                |

   
## tez 配置修改
在配置管理中的 tez-site.xml 配置文件中新增配置项，保存配置修改，重启配置发生变化组件。

| 参数                              | 值                                                           |
| --------------------------------- | ------------------------------------------------------------ |
| tez.tez-ui.history-url.base       | `http://172.**.**.9:2000/tez-ui/`（需替换为自己的 IP）                              |
| tez.history.logging.service.class | org.apache.tez.dag.history.logging.ats.ATSHistoryLoggingService |
 

## 服务启动
1. 启动 timelineserver
```
/usr/local/service/hadoop/sbin/yarn-daemon.sh  start timelineserver  
```
2. 启动 tomcat
```
/usr/local/service/tomcat/bin/startup.sh  
```
3. 重启 tez 服务
```
su hadoop
rm -rf  /usr/local/service/knox/data/deployments/*
/usr/local/service/knox/bin/ldap.sh stop
/usr/local/service/knox/bin/ldap.sh start
/usr/local/service/knox/bin/gateway.sh stop
/usr/local/service/knox/bin/gateway.sh start
```
4. tezui 访问地址
>?账号密码与服务器登录账号密码相同。
>
```
https://{集群公网ip}:30002/gateway/emr/tez/  
```
