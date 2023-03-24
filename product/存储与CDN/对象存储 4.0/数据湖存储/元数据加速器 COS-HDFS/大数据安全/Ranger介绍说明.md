## 背景

COS Ranger Service 是腾讯云存算分离推出的大数据权限管控方案，具有细粒度、兼容 Hadoop Ranger 以及可插拔的优势，便于用户统一管理大数据组件和云端托管存储权限，具体架构方案及说明可查看 [COS Ranger 权限体系解决方案](https://cloud.tencent.com/document/product/436/51125)。

COS Ranger Service 一经推出后便得到广泛使用，然而由于客户业务众多，背景复杂，产生一些问题，现整理相关Ranger 介绍说明、版本细节以及注意事项。

## 版本介绍

### 相关组件

相关组件主要有 Ranger-Plugin、COS Ranger Server、COS Ranger Client（也就是 Hadoop-Ranger-Client）、COSN Ranger Interface。

#### Ranger-Plugin

根据 Ranger 协议（具体可参见 [Apache 官方文档](https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=53741207)）提供 Ranger 服务端的服务定义插件。它们提供了 Ranger 侧的 COS 服务描述，部署了该插件后，用户即可在 Ranger 的控制页面上，填写 COS 的权限策略，例如设置 path、bucket、user、group 等访问策略。  

#### COS Ranger Server

该服务集成了 Ranger 的客户端，周期性从 Ranger 服务端同步权限策略，在收到客户的鉴权请求后，在本地进行权限校验。 同时它提供了 Hadoop 中 DelegationToken 相关的生成、续租等接口。

EMR 环境中默认安装目录在 /usr/local/service/cosranger/lib 下。例如包名 cos-ranger-service-5.1.2-jar-with-dependencies.jar，5.1.2 即为 cos ragner server 的版本号。

#### COS Ranger Client

Hadoop sdk 插件通过 core-site.xml 文件中配置对其进行动态加载，把权限校验的请求转发给 COS Ranger Server。  

EMR 环境中默认安装目录在 /usr/local/service/hadoop/share/hadoop/common/lib 下。例如包名 hadoop-ranger-client-for-hadoop-2.8.5-5.0.jar，2.8.5 是 hadoop 版本号，5.0是该包的版本号。

#### COSN Ranger Interface

该插件由 COS Ranger Server 和 COS Ranger Client 公共数据定义以及接口定义。

EMR 环境中默认安装目录在 /usr/local/service/hadoop/share/hadoop/common/lib 下。例如包名 cosn-ranger-interface-1.0.4.jar，1.0.4即为 COSN Ranger Interface 版本号。

以上 jar 包均可前往 [Github](https://github.com/tencentyun/cos-ranger-service) 获取。其他组件例如 impala、presto 等对应的 COS Ranger Client 包联系 EMR 团队。  

在 EMR 控制台购买 Ranger 和 cosranger 组件时会自动安装以上组件；如果自行安装，可参考 [CHDFS Ranger 权限体系解决方案](https://cloud.tencent.com/document/product/1105/53307)。

### 版本说明 

根据核心架构区分，版本总体上分为两大类：**依赖 zookeeper 服务与发现** 和 **不依赖 zookeeper 服务与发现** 版本。COS Ranger Server 提供服务，供 COS Ranger Client 调用。  
- 如果 COS Ranger Client 通过 zookeeper 去发现 COS Ranger Server 的服务地址，就需要配置 zookeeper 地址，这就是**依赖 zookeeper 版本**的特性。
- 如果 COS Ranger Client 不依赖 zookeeper 去发现 COS Ranger Server 服务，则需要配置 qcloud.object.storage.ranger.service.address 直接指定 COS Ranger Server 服务地址，不必去依赖 zookeeper 去发现 COS Ranger Server 服务；这就是**不依赖 zookeeper 版本**的特性。

### 版本对应关系

| 组件 | 依赖 zookeeper 服务与发现 | 不依赖 zookeeper 服务与发现 | 
| ---- | --- | ---- | 
|COS Ranger Server| v5.0.9 及早期版本| v5.1.1 及以上版本|
|COS Ranger Client |  v3.9 及早期版本| v4.1 及以上版本|
|COSN Ranger Interface | v1.0.3 版本| v1.0.4 版本及以上|

>! 如使用**不依赖 zookeeper 服务与发现**的版本，COS Ranger Server 须 v5.1.1以上（推荐 **v5.1.2**），COS Ranger Client 须 v4.1 以上（推荐 **v5.0**），且 COSN Ranger Interface 须 v1.0.4 版本及以上。
>

### 版本兼容关系

版本对应关系可依照上述两大类去匹配；但由于众多客户，背景复杂，不一定按照上述两大类来区分的，故下表列出各组件间的兼容关系，每一行表示可兼容。

| COS Ranger Client 版本   | COS Ranger Server 版本  | COSN Ranger Interface 版本| 是否依赖 zookeeper 服务与发现  |
|  -----------------------|  ----------------------  | ------------------------ | ------|
|   version ≤ v3.9       |    version ≤ v5.0.9     |       v1.0.3             |  是 |
|   version ≤ v3.9       |    version ≥ v5.1.1     |       v1.0.4             |  是 |
|   version ≥ v4.1       |    version ≥ v5.1.1     |       v1.0.4             |  否 |
|   version ≥ v5.0       |    version ≤ v5.0.9     |       v1.0.4             |  是 |
|   version ≥ v5.0       |    version ≥ v5.1.1     |       v1.0.4             |  否 |


>!
> - COS Ranger Client v5.0 可兼容所有版本 COS Ranger Server 。
> - COS Ranger Client v4.1 只能兼容 v 5.1.1及以上版本的 COS Ranger Server。
> - COS Ranger Client v3.x 虽然也可以兼容所有版本的 COS Ranger Server，但只能依赖 zookeeper 去发现COS Ranger Server 服务（后文会说明依赖 zookeeper 版本的弊病）。
> - COS Ranger Client 和 COSN Ranger Interface 包需要放在同一目录下，供 hadoop sdk 插件动态加载。
> 

### 使用说明

- 元数据加速桶和 CHDFS 文件系统需要在官网控制台打开 Ranger 校验。
- 使用**依赖 zookeeper 服务与发现**版本，core-site.xml 需要配置 qcloud.object.storage.zk.address，value 为 zookeeper 地址（用逗号分隔）。
- 如果 COS Ranger Server 使用 v5.1.1 及 v5.1.2 版本，而 COS Ranger Client 使用 v3.x 版本，此时仍然是依赖 zookeeer 注册与发现，core-site.xml 需要配置 qcloud.object.storage.zk.address，value 为 zookeeper 地址（用逗号分隔，例如10.0.0.8:2181,10.0.0.9:2181,10.0.0.10:2181）。
- 使用**不依赖 zookeeper 服务与发现**版本，core-site.xml 需要配置 qcloud.object.storage.ranger.service.address，value 为 COS Ranger Server 服务地址（用逗号分隔，例如127.0.0.1:9999,128.0.0.1:9999）。
- 使用 ofs 协议访问，core-site.xml 需要配置 fs.ofs.ranger.enable.flag 为 true。
- 使用 cosn 协议访问，core-site.xml 需要配置 fs.cosn.credentials.provider ，设置为：org.apache.hadoop.fs.auth.RangerCredentialsProvider。

### 配置项说明

| 配置项 | 说明 | 示例  |
| --- | --- | --- |
| qcloud.object.storage.zk.address | COS Ranger Server 注册的 zk 地址 | 10.0.0.8:2181,10.0.0.9:2181,10.0.0.10:2181  |
| qcloud.object.storage.ranger.service.address | COS Ranger Server RPC 服务地址 | 127.0.0.1:9999,128.0.0.1:9999 |
| fs.ofs.ranger.enable.flag | 使用 ofs 协议时的 Ranger 开关 | true |
| fs.cosn.credentials.provider | 使用 cosn 协议时的 Ranger 认证类路径 | org.apache.hadoop.fs.auth.RangerCredentialsProvider |
| fs.cosn.posix.bucket.use_ofs_ranger.enabled | 是否走 chdfs ranger 鉴权配置| 默认为 false，即 COSN Ranger 鉴权。<br>配置为 true，则为 chdfs ranger 鉴权<br>说明：该项为 hadoop-cos v8.1.7 及以上版本的新增配置项  |  


### 配置项表

| 组件版本 | 配置项 |
| --- | --- |
| cos ranger verser ≤ v5.0.9<br> cos ranger client ≤ v3.9 OR = v5.0<br> ofs 协议访问| qcloud.object.storage.zk.address<br> fs.ofs.ranger.enable.flag |
| cos ranger verser ≤ v5.0.9<br> cos ranger client ≤ v3.9 OR = v5.0<br> cosn 协议访问| qcloud.object.storage.zk.address<br> fs.cosn.credentials.provider |
| cos ranger verser = v5.1.1 OR = v5.1.2<br> cos ranger client ≥ v4.1<br> ofs 协议访问|qcloud.object.storage.ranger.service.address<br> fs.ofs.ranger.enable.flag|
| cos ranger verser = v5.1.1 OR = v5.1.2<br> cos ranger client ≥ v4.1<br> cosn 协议访问|qcloud.object.storage.ranger.service.address<br> fs.cosn.credentials.provider|

>!
> - 如果使用 cosn 协议访问元数据加速桶，且希望走 chdfs ranger 鉴权，请设置 fs.cosn.posix.bucket.use_ofs_ranger.enabled 为 true；且 hadoop-cos 版本要大于等于 v8.1.7。
> - 新增或调整上述配置，大数据组件如 YARN 中 ResourceManager/NodeManager、Hive 中 HiveMetaStore/HiveServer2、Impala 及 Presto 下应用等都需要重启。
> 

### 推荐版本

| 组件 | 版本号 |
| ---| ---|
| cos-ranger-server| >= v5.1.2 |
| cos-ranger-client| >= v5.0   |
| cosn-ranger-interface| >= v1.0.4|


### 推荐说明

之所以推荐上述版本原因如下：

- zookeeper 只用来选主，不进行服务注册与发现，大大减少大数据作业时 zookeeper 压力；因为每一个大数据作业时，会有大量 task 去访问 zookeeper 来进行 COS Ranger Server 服务发现，对 zookeeper 压力比较大，从而影响其他大数据组件稳定。
- V5.0 版本的 hadoop-ranger-client 包可兼容旧版本 COS Ranger Server 包，可方便老用户升级 COS Ranger Server。
- COS Ranger Server 5.1.2之前的版本，可能会存在获取到的 leader IP 和 leader latch 中的 IP 不一致的情况；而且，后期会简化 COS Ranger Server 注册到 zk 的信息，有利于后续拓展或升级。
- 修复若干 bug。


## 认证和鉴权常见问题

### 报错 IOException: init fs.ofs.ranger.client.impl failed，该如何处理？

- 若 Caused by: java.io.IOException: invalid zk address null，则 core-site.xml 需要配置 qcloud.object.storage.zk.address，value 为 zookeeper 地址（用逗号分隔，例如10.0.0.8:2181,10.0.0.9:2181,10.0.0.10:2181）。
- 若 Caused by: java.io.IOException: ranger client is null, maybe ranger server for qcloud object storage is not deployed! 则参考下一个问题。

### 报错 ranger client is null, maybe ranger server for qcloud object storage is not deployed!，该如何处理？

这种报错主要原因主要有以下几种：
- 如果 hadoop-ranger-client 包是 v3.8 及以下版本，可能是 zookeeper watch 丢失导致的，建议升级到 v5.0。
- 检查配置项 qcloud.object.storage.zk.address 或 qcloud.object.storage.ranger.service.address。
- 检查下 COS Ranger Server 服务和进程是否正常。

### 报错 Expect ranger service addresses: [127.0.0.1:6080,128.0.0.1:6080], but actual ranger service address，该如何处理？

![报错图](https://qcloudimg.tencent-cloud.cn/raw/5cc5ce4451bbe5bfe91835befd1a49db.png)

- 这种报错原因是元数据加速桶或 CHDFS 官网控制台打开 Ranger 校验，然而客户端并没有打开 Ranger 校验。
- 使用 ofs 协议访问，core-site.xml 需要配置 fs.ofs.ranger.enable.flag 为 true。
- 使用 cosn 协议访问，core-site.xml 需要配置 fs.cosn.credentials.provider，设置为：org.apache.hadoop.fs.auth.RangerCredentialsProvider。

### RangerQcloudObjectStorageClient 类未找到，该如何处理？

![报错图](https://qcloudimg.tencent-cloud.cn/raw/6558d81d1269320c53379c44c7f254ca.png)

- 缺少 cosn-ranger-interface 包，可前往 [Github](https://github.com/tencentyun/cos-ranger-service) 的 cosn-ranger-interface 目录下获取。
- 其他相关类未找到，可确认下 cosn-ranger-interface 包和 hadoop-ranger-client 包是否存在、版本是否匹配、以及是否放在正确路径下。
- 其他相关类未找到，还有一种情况是包 shade 路径问题，这个需要联系我们协助排查和处理。

### 报 NoSuchMethodError，该如何处理？

![报错图](https://qcloudimg.tencent-cloud.cn/raw/4b3fdbf027180095ca32292d54a05279.jpg)

这种报错原因是原先有该方法，但是加载到的类中却没有。出现这种情况主要有两种：

- 由于版本迭代，新版本包新增了该方法，而旧版本包中没有。
- 也有可能是加载其他包中的同名类。

在/usr/local/service下执行命令：
```
find . -name "*.jar" -exec grep -Hls "org/apache/hadoop/fs/cosn/ranger/client/RangerQcloudObjectStorageClientImpl" {} \;
```
找到相关包删除即可。如果是其他类，修改上述命令的类路径即可。

### 报错 java.lang.ClassCastException org.apache.hadoop.fs.cosn.ranger.protocol.ClientQCloudObjectStorageProtocolProtos$GetSTSRequest cannot be cast to com.google.protobuf.Message，该如何处理？

类似这种错误，一般是包污染问题，机器上存在旧版本包，因 protobuf 协议不一致导致的，和下面 alluxio 包污染问题基本一样。  

在/usr/local/service下执行命令：
```
find . -name "*.jar" -exec grep -Hls "org/apache/hadoop/fs/cosn/ranger/protocol/ClientQCloudObjectStorageProtocolProtos" {} \;
```
找到相关包删除即可。如果是其他类，修改上述命令的类路径即可。

### 修改 Ranger policy 未生效，该如何处理？

- 如果是 chdfs，修改 COS Ranger Server 配置文件 ranger-chdfs-security.xml 中的配置项：ranger.plugin.chdfs.policy.pollIntervalMs 调小（单位毫秒）。
- 如果是 cosn，修改 COS Ranger Server 配置文件 ranger-cos-security.xml 中的配置项：ranger.plugin.cos.policy.pollIntervalMs 调小（单位毫秒）。

### Ranger policy 策略配置 group 未生效，该如何处理？

如果配置 user 后生效了，需要找 EMR 团队确认 group 同步问题； 其他情况请联系我们。

### Ranger policy 配置存储路径策略规则，该如何处理？

Ranger 对 Path 校验规则其实很简单，主要就是字符串匹配。如果有文件 /a/b/c，配置 policy 的 path 规则为 **/a/**，访问 **/a** 或 **/a/** 都是无法访问的；因为 sdk 会把访问路径末尾 **/** 给去掉，最后到 Ranger 那边路径就变成了 **/a** ，无法匹配上 **/a/** ；如果访问 **/a/b** 或者 **/a/b/c**，这两个 path 的前缀部分是刚好可以匹配上 policy 中的 path 规则 **/a/**。

### Hive 指定 COSN 或 OFS 路径建表报 HiveAccessControlException，该如何处理？

![报错图](https://qcloudimg.tencent-cloud.cn/raw/928c7f08b597170da831dcca0e7edc42.png)

需要 hive 放开对 URL 的校验，需要在 ranger 控制台 hive 里配置允许 url 权限：

![Ranger Admin](https://qcloudimg.tencent-cloud.cn/raw/8db0474e6ec152f92b61c98f6ac5d83c.png)

>! 注意看一下报错日志的格式，这种报错多半是 Ranger 服务报出来的，大多数情况下是 ranger admin 配置权限有误。

### kerberos 下 spark 提交任务报 HiveAccessControlException，该如何处理？

应用程序需要与其他安全 Hadoop 文件系统交互，则需要在启动时将其 URI 显式提供给 Spark，配置参数 spark.kerberos.access.hadoopFileSystems=cosn://bucket-appid,ofs://f4mxxxxxxxx-Xxxx.chdfs.ap-guangzhou.myqcloud.com 可参考 [Spark 官网文档](https://spark.apache.org/docs/latest/security.html)。

### SPARK 删表不会进回收站，该如何处理？

Spark 中 create table 指定 Location 等价于创建外部表，删除外部表无法删除数据，可参考 [Spark 官网文档说明](https://spark.apache.org/docs/latest/sql-migration-guide.html#upgrading-from-spark-sql-16-to-20)。

>? hive on mr 情况下 drop table 可删除。
>

### Hive 执行 INSERT 语句报 AccessControlException，该如何处理？

Hive 默认引擎是 MapReduce，yarn-site.xml 文件新增配置项：
```
<property>
    <name>mapreduce.job.hdfs-servers</name>
    <value>
        ofs://f4mxxxxxxx-XXXX,cosn://bucketname-appid,${fs.defaultFS}
    </value>
</property>
```
如果 hive 引擎是 tez，则在 tez-site.xml 文件中新增配置项 tez.job.fs-servers，value 值同上。

如果是 beeline 连 hive，需要重启 hiveserver2 加载新的 yarn-site 配置。

### 访问 OFS 报错，该如何处理？

![访问 ofs 报错](https://qcloudimg.tencent-cloud.cn/raw/006df64050758fb2e4551d68335b94dd.png)

报错是 ofs 后端返回的，启用 ranger 后，需要关闭 posix。操作如下：

- CHDFS 控制台
![chdfs关闭posix](https://qcloudimg.tencent-cloud.cn/raw/c3949ae42d0e7dcab055960f516b9ea6.png)
- COS bucket 配置
![](https://qcloudimg.tencent-cloud.cn/raw/cca96a97ef5fafcb90f636b0b0a90fb0.png)

### YARN 命令行提交任务 报 renew token failed，该如何处理？

yarn 命令行执行时，需要 -Dmapreduce.job.send-token-conf 参数。

### 如何自建 cosranger？

可参见 [COS Ranger 权限体系解决方案](https://cloud.tencent.com/document/product/436/51125)  、[CHDFS Ranger 权限体系解决方案](https://cloud.tencent.com/document/product/1105/53307)。

### 腾讯云 EMR 中如何启用 Ranger？

在 emr 控制台购买 Ranger 和 cosranger 组件，省去自己部署麻烦。  
- 如果是 chdfs，在 core-site.xml 中新增配置项：fs.ofs.ranger.enable.flag，设置为：true。
- 如果是 cosn，在 core-site.xml 中新增配置项：fs.cosn.credentials.provider，设置为：
org.apache.hadoop.fs.auth.RangerCredentialsProvider。

### NodeCache 空指针异常，该如何处理？

确认 hadoop-ranger-client 版本，如果是 v3.8，建议升级到 v5.0；其他情况请联系我们。
出现这种报错原因是大数据作业时并发程度比较高，zookeeper 压力比较高，zookeeper watch 有丢失导致的。

### 启用 cosranger 后 hadoop fs 命令报 java.lang.IllegalArgumentException: Failed to specify server's Kerberos principal name，该如何处理？

- core-site.xml 新增配置项：qcloud.object.storage.kerberos.principal。
- 如果是 hdfs 集群报该错，core-site.xml 新增配置项：dfs.namenode.kerberos.principal。
