## 背景

大数据用户使用存算分离后，将数据托管在云 HDFS（Cloud HDFS，CHDFS）上。CHDFS 提供了类似 HDFS 的权限体系管控。Hadoop Ranger 在 HDFS 权限基础上，提供了更精细的权限管控，包括用户组权限设置，针对某个前缀的权限设置。同时 Hadoop Ranger 作为一站式的权限体系解决方案， 不仅支持存储端权限管控，还支持 YARN，Hive 等组件权限管控。因此，为了维持方便客户的使用习惯，我们提供了 CHDFS 的 Ranger 接入解决方案，方便客户使用 Ranger 来进行 CHDFS 的权限管控。


## 优势

- 细粒度的权限控制，兼容 Hadoop 权限习惯。
- 用户统一管理大数据组件与云端托管存储的权限。

## 解决方案架构

![](https://main.qcloudimg.com/raw/31d674511bcc4d75caf24312801818d2.png)

Hadoop 权限体系中，认证由 Kerberos 提供，授权鉴权由 Ranger 负责。在此基础上，我们提供以下组件，来支持 CHDFS 的 Ranger 权限方案。

- CHDFS-Ranger-Plugin：提供 Ranger 服务端的服务定义插件。它们提供了 Ranger 侧的 CHDFS 服务描述，部署了该插件后，用户即可在 Ranger 的控制页面上，填写相应的权限策略。
- COSRangerService：该服务集成了 Ranger 的客户端，周期性从 Ranger 服务端同步权限策略，在收到客户的鉴权请求后，在本地进行权限校验。 同时它提供了 Hadoop 中 DelegationToken 相关的生成，续租等接口，所有的接口都是通过 Hadoop IPC 定义。
- CosRangerClient：COSN 插件对其进行动态加载，把权限校验的请求转发给 CosRangerService。

## 部署环境

- Hadoop 环境。
- ZooKeeper、Ranger、Kerberos 服务（如果有认证需求，则部署）。

>? 以上服务由于是成熟的开源组件，因此客户可自行安装。
>

## 部署组件

<dx-tabs>
::: 部署CHDFS-Ranger-Plugin
CHDFS-Ranger-Plugin 拓展了 Ranger Admin 控制台上的服务种类， 用户可在 Ranger 控制台上，设置和 CHDFS 相关的操作权限。

#### 代码地址

可前往 [Github](https://github.com/tencentyun/cos-ranger-service) 的 ranger-plugin 目录下获取。

#### 版本

V1.2版本及以上。

#### 部署步骤

1. 在 Ranger 的服务定义目录下新建 COS 目录（注意：目录权限需要保证至少有 x 与 r 权限）。
 1. 腾讯云的 EMR 环境，路径是 ranger/ews/webapp/WEB-INF/classes/ranger-plugins。
 2. 自建的 hadoop 环境，可以通过在ranger目录下 find hdfs 等方式找到已经接入到 ranger 服务的组件，查找 ranger-plugins 目录位置。
![](https://main.qcloudimg.com/raw/679f61339b8c3864a84b3b757dd84815.png)
2. 在 CHDFS 目录下，放入 cos-chdfs-ranger-plugin-xxx.jar（注意： jar 包至少有 r 权限）。
3. 重启 Ranger 服务。
4. 在 Ranger 上注册 CHDFS Service。可参考如下命令：
<dx-codeblock>
::: plaintext
##生成服务，需传入 Ranger 管理员账号密码，以及 Ranger 服务的地址。
##对于腾讯云 EMR 集群，管理员用户是 root，密码是构建 emr 集群时设置的 root 密码，ranger 服务的 IP 换成 EMR 的 master 节点 IP。
adminUser=root
adminPasswd=xxxxxx
rangerServerAddr=10.0.0.1:6080
curl -v -u${adminUser}:${adminPasswd} -X POST -H "Accept:application/json" -H "Content-Type:application/json" -d @./chdfs-ranger.json http://${rangerServerAddr}/service/plugins/definitions
##如果要删除刚定义的服务，则传入刚刚创建服务时，返回的服务 ID
serviceId=102
curl -v -u${adminUser}:${adminPasswd} -X DELETE -H "Accept:application/json" -H "Content-Type:application/json" http://${rangerServerAddr}/service/plugins/definitions/${serviceId}
:::
</dx-codeblock>
5. 创建服务成功后，可在 Ranger 控制台看到 CHDFS 服务。如下所示：
![](https://main.qcloudimg.com/raw/163aac38c68931f51ab34c221ea3cef1.png)
6. 在 CHDFS 服务侧单击【+】，定义新服务实例，服务实例名可自定义，例如`chdfs`或者`chdfs_test`。服务的配置如下所示：
![](https://main.qcloudimg.com/raw/255869b8c485a93427585d21476ec001.png)
其中 policy.grantrevoke.auth.users 需设置后续启动 COSRangerService 服务的用户名。通常建议设置成 hadoop，后续 COSRangerService 可使用此用户名进行启动。
7. 单击新生成的 CHDFS 服务实例，添加 policy。如下所示：
![](https://main.qcloudimg.com/raw/f0d76ecf787eec3340f7d923e65b9b48.png)
8. 在跳转界面中，配置以下参数。具体说明如下：
![](https://main.qcloudimg.com/raw/317e1b5cb39abae6904552cb1ebade58.png)
 - **MountPoint**:  挂载点的名称，格式为 f4mxxxxxx-yyyy 等样式，可登录 [CHDFS 控制台](https://console.cloud.tencent.com/chdfs/filesystem) 查看。
 - **path**: CHDFS 路径。注意 CHDFS 路径必须以`/`开始。
    - include：表示设置的权限适用于 path 本身，还是除了 path 以外的其他路径。
    - recursive：表示权限不仅适用于 path，还适用于 path 路径下的子成员（即递归子成员）。通常用于 path 设置为目录的情况。
 - **user/group**：用户名和用户组。这里是或的关系，即用户名或者用户组满足其中一个，即可拥有对应的操作权限。
 - **Permissions**：
    -  Read：读操作。对应于对象存储里面的 GET、HEAD 类操作，包括下载对象、查询对象元数据等。
    -  Write：写操作。对应于对象存储里面的 PUT 类等修改操作，例如上传对象。
    -  Delete：删除操作。 对应于对象存储里删除 Object。对于 Hadoop 的 Rename 操作，需要有对原路径的删除操作权限，对新路径的写入操作权限。
    -  List：遍历权限。对应于对象存储里面的 List Object。

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
 -  qcloud.object.storage.enable.chdfs.ranger
 -  qcloud.object.storage.zk.address
3. 修改 ranger-chdfs-security.xml 文件中的相关配置。其中必须修改的配置项有如下所示。配置项说明请参见文件中的注释说明。
 -  ranger.plugin.chdfs.policy.cache.dir
 -  ranger.plugin.chdfs.policy.rest.url
 -  ranger.plugin.chdfs.service.name
4. 修改 start_rpc_server.sh 中 hadoop_conf_path 和 java.library.path 的配置。这两个配置分别指向 hadoop 配置文件所在的目录（例如 core-site.xml、hdfs-site.xml）以及 hadoop native lib 路径。
5. 执行如下命令启动服务。
```
chmod +x start_rpc_server.sh
nohup ./start_rpc_server.sh &> nohup.txt &
```
6. 如果启动失败，查看 log 下 error 日志是否有错误信息。
7. cos-ranger-service 支持展示 HTTP 端口状态（端口名为 qcloud.object.storage.status.port，默认值为9998）。用户可通过以下命令获取状态信息（例如是否包含 leader、鉴权数量统计等)。
```
# 请将下面的10.xx.xx.xxx替换为部署 ranger service 的机器 IP
# port 9998 设置为 qcloud.object.storage.status.port 配置值
curl -v http://10.xx.xx.xxx:9998/status
```

:::
::: 部署COS-Ranger-Client
COS-Ranger-Client 由 hadoop chdfs 插件动态加载，并代理访问 COS-Ranger-Service 的相关请求。例如获取 token、鉴权操作等。

#### 代码地址

可前往 [Github](https://github.com/tencentyun/cos-ranger-service) 的 cos-ranger-client 目录下获取。

#### 版本

V3.4版本及以上。

#### 部署方式
1. 将 cos-ranger-client jar 包和cosn-ranger-interface jar 包拷贝到与 CHDFS 插件 同一目录下（请选择拷贝与自身 hadoop 大版本一致的  jar 包）。
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
::: 部署CHDFS

#### 版本

V2.1版本及以上。

#### 部署方式

部署 CHDFS 插件的方法请参考 [挂载 CHDFS](https://cloud.tencent.com/document/product/1105/36368) 文档，开启 ranger 通过添加以下方式进行：


<dx-codeblock>
::: plaintext 
```
    <property>
        <name>fs.ofs.ranger.enable.flag</name> 
        <value>true</value>
    </property>
```
:::
</dx-codeblock>
:::
</dx-tabs>


## 验证

1. 使用 hadoop cmd 执行访问 chdfs 的相关操作。 如下范例所示：
```plaintext
# 将挂载点，路径等替换为自己的实际信息。
hadoop fs -ls ofs://f4mxxxxyyyy-zzzz.chdfs.ap-guangzhou.myqcloud.com/doc
hadoop fs -put ./xxx.txt ofs://f4mxxxxyyyy-zzzz.chdfs.ap-guangzhou.myqcloud.com/doc/
hadoop fs -get ofs://f4mxxxxyyyy-zzzz.chdfs.ap-guangzhou.myqcloud.com/exampleobject.txt
hadoop fs -rm ofs://f4mxxxxyyyy-zzzz.chdfs.ap-guangzhou.myqcloud.com/exampleobject.txt
```
2. 使用 MR Job 进行验证，验证前需重启相关的服务，例如 Yarn、Hive 等。


## 常见问题

#### kerberos 是否必须安装？

如果所在的集群，用户都是可信的，例如仅内部使用的集群，可安装 Kerberos 满足认证的需求。如果用户仅进行鉴权操作，为了避免无权限的客户误操作，那么可以不安装 Kerberos，只使用 ranger 进行鉴权。
安装 Kerberos 会引入一些性能损耗，请用户综合自己的安全需求与性能需求进行考量。如果需要认证，开启 Kerberos 后，需要设置 COS Ranger Service 和 COS Ranger Client 相关的配置项。

#### 如果开启了 Ranger，但未配置任何 Policy，或者未匹配到任何 Policy，会如何操作？

如果未匹配上任何 policy，会默认拒绝该操作。

#### 开启了 ranger 后，CHDFS 端是否还会进行 POSIX 鉴权？

Ranger 鉴权是在客户端环境进行的，经过 ranger 鉴权的请求，会发给 CHDFS 服务端，服务端默认会进行 POSIX 鉴权。因此如果权限都在 Ranger 端进行控制，请在 CHDFS 控制台关闭 POSIX 权限。
