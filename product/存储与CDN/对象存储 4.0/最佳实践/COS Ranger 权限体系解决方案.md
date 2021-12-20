
## 背景

Hadoop Ranger 权限体系是大数据场景下的权限解决方案。用户使用存算分离后，将数据托管在 COS 上。COS 使用的是腾讯云 CAM 权限体系，无论是用户身份，权限策略等，都与本地 Hadoop Ranger 体系不同。为维持客户的使用习惯，我们提供 COS 的 Ranger 接入解决方案。


## 优势

- 细粒度的权限控制，兼容 Hadoop 权限逻辑，用户统一管理大数据组件与云端托管存储的权限。
- 插件侧无需在 core-site 中设置密钥，密钥统一在 COSRangerService 中设置，避免明文密钥的泄露。


## 解决方案架构

![](https://main.qcloudimg.com/raw/221e3a3e8fd6d31590fc8ca2562d7489.png)

Hadoop 权限体系中, 认证由 Kerberos 提供，授权鉴权由 Ranger 负责。在此基础上，我们提供以下组件，来支持 COS 的 Ranger 权限方案。

 
1. cos-ranger-plugin：提供 Ranger 服务端的服务定义插件。它们提供了 Ranger 侧的 COS 服务描述，包括权限种类，必要参数定义（例如 COS 的 bucket 参数和 region 参数）。部署了该插件后，用户即可在 Ranger 的控制页面上，填写相应的权限策略。
2. COSRangerService：该服务集成了 Ranger 的客户端，周期性从 Ranger 服务端同步权限策略，在收到客户的鉴权请求后，在本地进行权限校验。 同时它提供了 Hadoop 中 DelegationToken 相关的生成，续租等接口，所有的接口都是通过 Hadoop IPC 定义。
3. CosRangerClient：COSN 插件对其进行动态加载，把权限校验的请求转发给 CosRangerService。

## 部署环境

- Hadoop 环境。
- ZooKeeper、Ranger、Kerberos 服务（如果有认证需求，则部署）。
>?以上服务由于是成熟的开源组件，因此客户可自行安装。

## 部署组件

<dx-tabs>
::: 部署COS-Ranger-Plugin
COS-Ranger-Plugin 拓展了 Ranger Admin 控制台上的服务种类，用户可在 Ranger 控制台上，设置和 COS 相关的操作权限。


#### 代码地址
可前往 [Github](https://github.com/tencentyun/cos-ranger-service) 的 ranger-plugin 目录下获取。
#### 版本
V1.1版本及以上。
#### 部署步骤
1. 在 Ranger 的服务定义目录下新建 COS 目录（注意，目录权限需要保证至少有 x 与 r 权限）。
a. 腾讯云的 EMR 环境，路径是 ranger/ews/webapp/WEB-INF/classes/ranger-plugins。
b. 自建的 hadoop 环境，可以通过在 ranger 目录下查找 hdfs 等已经接入到 ranger 服务的组件，查找目录位置。
![](https://main.qcloudimg.com/raw/793f47a53343657a000b34b7ac66b074.png)
2. 在 COS 目录下，放入 cos-chdfs-ranger-plugin-xxx.jar。（注意 jar 包至少有 r 权限）。
3. 重启 Ranger 服务。
4. 在 Ranger 上注册 COS Service。可参考如下命令：
<dx-codeblock>
::: plaintext
##生成服务，需传入 Ranger 管理员账号密码，以及 Ranger 服务的地址。
##对于腾讯云 EMR 集群，管理员用户是 root，密码是构建 emr 集群时设置的 root 密码，ranger 服务的 IP 换成 EMR 的 master 节点 IP。
adminUser=root
adminPasswd=xxxxxx
rangerServerAddr=10.0.0.1:6080
curl -v -u${adminUser}:${adminPasswd} -X POST -H "Accept:application/json" -H "Content-Type:application/json" -d @./cos-ranger.json http://${rangerServerAddr}/service/plugins/definitions
##如果要删除刚定义的服务，则传入刚刚创建服务时，返回的服务 ID
serviceId=102
curl -v -u${adminUser}:${adminPasswd} -X DELETE -H "Accept:application/json" -H "Content-Type:application/json" http://${rangerServerAddr}/service/plugins/definitions/${serviceId}
:::
</dx-codeblock>
5. 创建服务成功后，可在 Ranger 控制台看到 COS 服务。如下所示：
![](https://main.qcloudimg.com/raw/d1a6e2722d11f7177636a5e2c54226e3.png)
6. 在 COS 服务侧单击【+】，定义新服务实例，服务实例名可自定义，例如`cos`或者`cos_test`，服务的配置如下所示。
![](https://main.qcloudimg.com/raw/2be86fb2b8232b16679b29e908f82d3a.png)
其中 policy.grantrevoke.auth.users 需设置后续启动 COSRangerService 服务的用户名（即允许拉取权限策略的用户）。通常建议设置成 hadoop，后续 COSRangerService 可使用此用户名进行启动。
7. 单击新生成的 COS 服务实例，添加 policy。如下所示：
![](https://main.qcloudimg.com/raw/58ded7125d5c5d161ca6e2f5a98d8e7b.png)
8. 在跳转界面中，配置以下参数，说明如下：
 - **bucket**：存储桶名称，例如 examplebucket-1250000000，可登录 [COS 控制台](https://console.cloud.tencent.com/cos5/bucket) 查看。
 - **path**：COS 对象路径。注意 COS 的对象路径不以/开始。
    - include：表示设置的权限适用于 path 本身，还是除了 path 以外的其他路径。
    - recursive：表示权限不仅适用于 path，还适用于 path 路径下的子成员（即递归子成员）。通常用于 path 设置为目录的情况。
 - **user/group**：用户名和用户组。这里是或的关系，即用户名或者用户组满足其中一个，即可拥有对应的操作权限。
 - **Permissions**：
    -  Read：读操作。对应于对象存储里面的 GET、HEAD 类操作，包括下载对象、查询对象元数据等。
    -  Write：写操作,。对应于对象存储里面的 PUT 类等修改操作，例如上传对象。
    -  Delete：删除操作。 对应于对象存储里删除 Object。对于 Hadoop 的 Rename 操作，需要有对原路径的删除操作权限，对新路径的写入操作权限。
    -  List：遍历权限。对应于对象存储里面的 List Object。
![](https://main.qcloudimg.com/raw/00a619b4b963a9acf766411fad722fe4.png)
:::
::: 部署COS-Ranger-Service
COS-Ranger-Service 是整个权限体系的核心，负责集成 ranger 的客户端，接收 ranger client 的鉴权请求，token 生成续租请求和临时密钥生成请求。同时也是敏感信息（腾讯云密钥信息）所在的区域，通常部署在堡垒机器上，只允许集群管理员操作，查看配置等。

COS-Ranger-Service 支持一主多备的 HA 部署，DelegationToken 状态持久化到 HDFS。通过 ZK 抢锁决定 Leader 身份。获取 Leader 身份的服务会把地址写入 ZK，以便 COS Ranger Client 进行路由寻址。

#### 代码地址
可前往 [Github](https://github.com/tencentyun/cos-ranger-service) 的 cos-ranger-server 目录下获取。

#### 版本
V5.0.4版本及以上。

#### 部署步骤
1. 将 COS Ranger Service 服务代码拷贝到集群的几台机器上，生产环境建议至少两台机器（一主一备）。因为涉及到敏感信息，建议是堡垒机或者权限严格管控的机器。
2. 修改 cos-ranger.xml 文件中的相关配置，其中必须修改的配置项如下所示。配置项说明请参见文件中的注释说明。
 -  qcloud.object.storage.rpc.address
 -  qcloud.object.storage.status.port
 -  qcloud.object.storage.enable.cos.ranger
 -  qcloud.object.storage.zk.address
 -  qcloud.object.storage.cos.secret.id
 -  qcloud.object.storage.cos.secret.key
3. 修改 ranger-cos-security.xml 文件中的相关配置。其中必须修改的配置项有如下所示。配置项说明请参见文件中的注释说明。
 -  ranger.plugin.cos.policy.cache.dir
 -  ranger.plugin.cos.policy.rest.url
 -  ranger.plugin.cos.service.name
4. 修改 start_rpc_server.sh 中 hadoop_conf_path 和 java.library.path 的配置。这两个配置分别指向 hadoop 配置文件所在的目录（例如 core-site.xml、hdfs-site.xml）以及 hadoop native lib 路径。
5. 执行如下命令启动服务。
```
chmod +x start_rpc_server.sh
nohup ./start_rpc_server.sh &> nohup.txt &
```
6. 如果启动失败，查看 log 下 error 日志是否有错误信息。
7. cos-ranger-service 支持展示 HTTP 端口状态（端口名为 qcloud.object.storage.status.port，默认值为9998）。用户可通过以下命令获取状态信息（例如是否包含 leader、鉴权数量统计等)
```
# 请将下面的10.xx.xx.xxx替换为部署 ranger service 的机器 IP
# port 9998 设置为 qcloud.object.storage.status.port 配置值
curl -v http://10.xx.xx.xxx:9998/status
```

:::
::: 部署COS-Ranger-Client
COS-Ranger-Client 由 hadoop cosn 插件动态加载，并代理访问 COS-Ranger-Service 的相关请求。例如获取临时密钥、获取 token、鉴权操作等。

#### 代码地址
可前往 [Github](https://github.com/tencentyun/cos-ranger-service) 的 cos-ranger-client 目录下获取。

#### 版本
V3.4版本及以上。

#### 部署方式
1. 将 cos-ranger-client jar 包和cosn-ranger-interface jar 包拷贝到与 COSN 同一目录下（请选择拷贝与自身 hadoop 大版本一致的  jar 包）。
2. 在 core-site.xml 添加如下配置项：
<dx-codeblock>
::: xml
```
<configuration>
           <!--*****必须配置********-->
           <!-- zk 的地址，客户端从 zk 上查询得知 ranger-service 的服务地址 -->
           <property>
               <name>qcloud.object.storage.zk.address</name>
               <value>10.0.0.8:2121</value>
           </property>

           <!--***可选配置****-->           
           <!-- 设置 cos ranger service 端用的 kerberos 凭据，参考 cos ranger service 端的配置，须保持一致，如果没有认证的需求，不需要配置 -->
           <property>                
					 <name>qcloud.object.storage.kerberos.principal</name>
					 <value>hadoop/_HOST@EMR-XXXX</value>
           </property>

         <!--***可选配置****-->  
         <!-- zk 上记录的 ranger server 的 ip 地址路径, 这里使用了默认值, 配置必须与 cos-ranger-service 的配置一致 -->
          <property>              
					<name>qcloud.object.storage.zk.leader.ip.path</name> 
					<value>/ranger_qcloud_object_storage_leader_ip</value>
          </property>
         <!-- zk 上记录的 cos ranger service follower的ip地址路径,这里使用了默认值 必须与 cos-ranger-service 的配置一致,主备节点同时提供服务 -->
          <property>
                    <name>qcloud.object.storage.zk.follower.ip.path</name>
                    <value>/ranger_qcloud_object_storage_follower_ip</value>
          </property>
</configuration>
```
:::
</dx-codeblock>
:::
::: 部署COSN
#### 版本
V7.0.5版本及以上。

####  部署方式
部署 COSN 插件方法请参考 [Hadoop 工具](https://cloud.tencent.com/document/product/436/6884) 文档，但需注意以下几点：

1. 使用 ranger 后，fs.cosn.userinfo.secretId 和 fs.cosn.userinfo.secretKey 密钥信息不需要配置。COSN 插件后续通过 COSRangerService 获取临时密钥。
2. fs.cosn.credentials.provider 需设置为 org.apache.hadoop.fs.auth.RangerCredentialsProvider 才可通过 Ranger 进行认证鉴权。如下所示：
<dx-codeblock>
::: plaintext 
```
<property>
         <name>fs.cosn.credentials.provider</name>
         <value>org.apache.hadoop.fs.auth.RangerCredentialsProvider</value>
</property>
```
:::
</dx-codeblock>
:::
</dx-tabs>


## 验证

1. 使用 hadoop cmd 执行访问 COSN 的相关操作。查看当前用户执行的操作是否符合主账号的权限设置预期，示例如下所示：
```plaintext
#将bucket，路径等替换为主账号的实际信息。
hadoop fs -ls cosn://examplebucket-1250000000/doc
hadoop fs -put ./xxx.txt cosn://examplebucket-1250000000/doc/
hadoop fs -get cosn://examplebucket-1250000000/doc/exampleobject.txt
hadoop fs -rm cosn://examplebucket-1250000000/doc/exampleobject.txt
```
2. 使用 MR Job 进行验证，验证前需重启相关的服务，例如 Yarn、Hive 等。


## 常见问题

#### kerberos 是否必须安装？
Kerberos 满足认证的需求，如果所在的集群，用户都是可信的，例如仅内部使用的集群。若用户仅进行鉴权操作，为了避免无权限的客户误操作，那么可以不安装 Kerberos，只使用 ranger 进行鉴权。同时 Kerberos 会引入一些性能损耗。请客户综合自己的安全需求与性能需求进行考量。如果需要认证，开启 Kerberos 后，需要设置 COS Ranger Service 和 COS Ranger Client 相关的配置项。
#### 如果开启了 Ranger，但未配置任何 Policy，或者未匹配到任何 Policy，会如何操作？
如果未匹配上任何 policy，会默认拒绝该操作。
#### 配置 COS Ranger Service 侧的密钥可以是子账号？
可以是子账号，但是必须拥有被操作 bucket 的相应权限，才能生成临时密钥给到 COSN 插件，进行相应的操作。通常建议这里设置的密钥拥有对该 bucket 的所有权限。
#### 临时密钥需如何更新，每次访问 COS 前都需要从 COS Ranger Service 侧获取?
临时密钥是 cache 在 COSN 插件侧，并周期性进行异步更新。
