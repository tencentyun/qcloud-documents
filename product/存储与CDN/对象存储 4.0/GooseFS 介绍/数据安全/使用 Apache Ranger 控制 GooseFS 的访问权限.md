## 概述

Apache Ranger 是大数据生态系统中用于控制访问权限的一个标准鉴权组件，GooseFS 作为大数据和数据湖场景下的加速存储系统，也已经支持接入 Apache Ranger 的统一鉴权平台中，本文将介绍使用 Apache Ranger 控制 GooseFS 的资源访问权限。

## 优势

- GooseFS 作为一款云原生加速存储系统，在 Apache Ranger 支持上已经做到了与 HDFS 近乎一致的访问控制行为。因此，原先使用 HDFS 的大数据用户可以非常轻松地迁移到 GooseFS 上来，并且直接复用 HDFS 的 Ranger 权限策略，即可获得一致的使用体验。
- GooseFS with Ranger 相比 HDFS with Ranger 的鉴权架构，还额外提供了 Ranger + 原生 ACL 的联合鉴权选项，在 Ranger 鉴权失效时，还可选择使用原生 ACL 鉴权，可解决一些 Ranger 鉴权策略配置不完善的问题。

## GooseFS with Ranger 的鉴权架构

![](https://main.qcloudimg.com/raw/2f473b8cb8fc446c8b914101f548219a.png)

为了支持将 GooseFS 集成到 Ranger 鉴权平台中，我们开发了 GooseFS Ranger Plugin，它同时部署在 GooseFS Master 节点和 Ranger Admin 侧。负责完成如下工作：

- GooseFS Master 节点侧：
 - 提供 `Authorizer` 接口，为 GooseFS Master 上的每一次元数据请求提供鉴权结果。
 - 连接 Ranger Admin 获取用户配置的鉴权策略。
- Ranger Admin 侧：
 - 为 Ranger Admin 提供 GooseFS 的资源查找（resource lookup）的能力。
 - 提供配置校验的能力。

## 开始部署

### 准备工作

在开始使用前，需确保环境中已部署并配置了 Ranger 相关的组件（即包括：Ranger Admin 和 Ranger UserSync），并且确保 Ranger 的 WebUI 可以正常打开和使用。

### 部署组件

#### 在 Ranger Admin 侧部署 GooseFS Ranger Plugin 并注册对应服务

>? 单击 [此处](https://cos-data-lake-release-1253960454.cos.ap-guangzhou.myqcloud.com/goosefs/extensions/ranger-plugin/1.0.0/release/ranger-goosefs-plugin-1.0.0.jar) 下载 GooseFS Ranger Plugin。
>

部署步骤如下：

1. 在 Ranger 服务定义目录下新建 GooseFS 的目录（注意，目录权限至少保证 x 与 r 的权限）。
 1. 如果使用的是腾讯云 EMR 集群，则 Ranger 的服务定义目录在：`/usr/local/service/ranger/ews/webapp/WEB-INF/classes/ranger-plugins`。
 2. 如果是自建 Hadoop 集群，则可以通过在 ranger 目录下查找 hdfs 等已经接入到 ranger 服务的组件，查找目录位置。
![ranger 的服务定义目录](https://main.qcloudimg.com/raw/edb3882f1517f7231f2cc0a7f7a750f9.png)
2. 在 GooseFS 的目录下，放入 goosefs-ranger-plugin-${version}.jar 和 ranger-servicedef-goosefs.json，并且具备读权限。
3. 重启 Ranger 服务。
4. 在 Ranger 上，按照如下命令，注册 GooseFS Service。
```bash
# 生成服务，需要传入 Ranger 管理员的账号和密码，以及 Ranger 的服务地址
# 对于腾讯云 EMR 集群，管理员用户是 root，密码是构建 EMR 集群时设置的 root 密码，ranger 服务的 IP 就是 EMR 服务的 Master IP
adminUser=root
adminPasswd=xxxx

rangerServerAddr=10.0.0.1:6080

curl -v -u${adminUser}:${adminPasswd} -X POST -H "Accept:application/json" -H "Content-Type:application/json" -d @./ranger-servicedef-goosefs.json http://${rangerServerAddr}/service/plugins/definitions

# 服务注册成功后，会返回一个服务 ID，请务必记录下这个ID
# 如果要删除 GooseFS 的服务，则传入刚刚返回的服务 ID，执行如下命令即可：
serviceId=104
curl -v -u${adminUser}:${adminPasswd} -X DELETE -H "Accept:application/json" -H "Content-Type:application/json" http://${rangerServerAddr}/service/plugins/definitions/${serviceId}
```
5. 创建成功后，在 Ranger 的 Web 控制台上即可看到 GooseFS 相关的服务：
![ranger 的 web 控制台](https://main.qcloudimg.com/raw/3099cacd0fc907ea83ba418b5c873106.png)
6. 在 GooseFS 服务侧单击【+】，定义 goosefs 服务实例。
![ranger 的 web 控制台上定义 goosefs 服务实例](https://main.qcloudimg.com/raw/8142de87171eb21982c6bfda09e1c3d4.png)
7. 单击新生成的 goosefs 服务实例，即可添加鉴权 policy。
![添加鉴权 policy](https://main.qcloudimg.com/raw/b1ecd8453400c99318b1ee9bcfb608ff.png)

#### 在 GooseFS Master 侧部署 GooseFS Ranger Plugin 并配置启用 Ranger 鉴权

1. 将 goosefs-ranger-plugin-${version}.jar 放入 \${GOOSEFS_HOME}/lib 路径下，并且至少具备读权限。
2. 将 ranger-goosefs-audit.xml、ranger-goosefs-security.xml 以及 ranger-policymgr-ssl.xml 三个文件放入`\${GOOSEFS_HOME}/conf`路径下，并分别填写其必要配置：
 - ranger-goosefs-security.xml：
    ```xml
    <configuration xmlns:xi="http://www.w3.org/2001/XInclude">
      <property>
        <name>ranger.plugin.goosefs.service.name</name>
        <value>goosefs</value>
      </property>
    
      <property>
        <name>ranger.plugin.goosefs.policy.source.impl</name>
        <value>org.apache.ranger.admin.client.RangerAdminRESTClient</value>
      </property>
    
      <property>
        <name>ranger.plugin.goosefs.policy.rest.url</name>
        <value>http://10.0.0.1:6080</value>
      </property>
    
      <property>
        <name>ranger.plugin.goosefs.policy.pollIntervalMs</name>
        <value>30000</value>
      </property>
    
      <property>
        <name>ranger.plugin.goosefs.policy.rest.client.connection.timeoutMs</name>
        <value>1200</value>
      </property>
    
      <property>
        <name>ranger.plugin.goosefs.policy.rest.client.read.timeoutMs</name>
        <value>30000</value>
      </property>
    </configuration>
    ```
 - ranger-goosefs-audit.xml（不开启审计，可不配置）
 - ranger-policymgr-ssl.xml
    ```xml
    <configuration>
      <property>
        <name>xasecure.policymgr.clientssl.keystore</name>
        <value>hadoopdev-clientcert.jks</value>
      </property>
    
      <property>
        <name>xasecure.policymgr.clientssl.truststore</name>
        <value>cacerts-xasecure.jks</value>
      </property>
    
      <property>
        <name>xasecure.policymgr.clientssl.keystore.credential.file</name>
        <value>jceks://file/tmp/keystore-hadoopdev-ssl.jceks</value>
      </property>
    
      <property>
        <name>xasecure.policymgr.clientssl.truststore.credential.file</name>
        <value>jceks://file/tmp/truststore-hadoopdev-ssl.jceks</value>
      </property>
    </configuration>
    ```
3. 在 goosefs-site.xml 文件中，添加如下配置：
```properties
...
goosefs.security.authorization.permission.type=CUSTOM
goosefs.security.authorization.custom.provider.class=org.apache.ranger.authorization.goosefs.RangerGooseFSAuthorizer
...
```
4. 在 \${GOOSEFS_HOME}/libexec/goosefs-config.sh 中，将 goosefs-ranger-plugin-${version}.jar 添加到 GooseFS 的类路径中：
```bash
...
GOOSEFS_RANGER_CLASSPATH="${GOOSEFS_HOME}/lib/ranger-goosefs-plugin-1.0.0-SNAPSHOT.jar"
GOOSEFS_SERVER_CLASSPATH=${GOOSEFS_SERVER_CLASSPATH}:${GOOSEFS_RANGER_CLASSPATH}
...
```

至此，所有配置完成。

## 验证使用

例如，添加一条允许 hadoop 用户对 GooseFS 的根目录具备读取和执行权限，但是不允许写的策略，方法如下：

1. 添加策略，如下所示：
![控制台下发策略](https://main.qcloudimg.com/raw/7f0115000a0baef1089b281d415c095e.png)
2. 策略添加成功后，对策略进行验证，即可看到策略已经生效，如下所示：
![验证使用](https://main.qcloudimg.com/raw/a7c0a21220f8fcd3859e4fd98cc9a819.png)
