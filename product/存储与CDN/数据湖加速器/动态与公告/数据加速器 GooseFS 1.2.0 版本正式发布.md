腾讯云存储团队正式对外发布了数据加速器 GooseFS 1.2.0 版本，该版本总结并收敛了 GooseFS 在过往大规模生产环境实践中遇到的性能、稳定性和安全问题，全面提升产品稳定性。

## 重要更新点一：透明加速热开关

[透明加速能力](https://cloud.tencent.com/document/product/1424/68294) 可以让大数据用户能够使用 CosN scheme 访问 GooseFS，该特性方便用户在不修改已有表定义的前提下，使用 GooseFS 的功能，提升业务访问性能。

透明加速热开关主要用于提升系统的可运维性。在生产环境中使用 GooseFS 集群进行访问加速时，可能出现集群节点故障等各种问题，当集群无法自愈，并且需要尽快恢复现网业务时，需要有手段可以将访问流量在分钟级迅速切换到底层存储服务，然后在不影响计算作业的前提下，运维和管理 GooseFS 集群。

在具体使用过程中，可以通过如下指令启停透明加速热开关：

```
goosefs.user.client.transparent_acceleration.enabled = true | false
```

其中，`false`代表开启透明加速能力，开启后所有访问请求会优先经过 GooseFS；`true`代表关闭透明加速能力，关闭后所有访问请求会直接透传到底层。

## 重要更新点二：集成 CHDFS 认证和 Ranger 鉴权体系

Apache Ranger 是大数据生态系统中用于控制访问权限的一个标准鉴权组件，GooseFS 作为大数据和数据湖场景下的加速存储系统，也已经支持接入 Apache Ranger 的统一鉴权平台中；CHDFS 则是公有云原生的 HDFS 服务，本期重点更新主要集成了 CHDFS 认证和 Ranger 鉴权体系，方便大数据业务尽可能提升业务安全管控能力。


在具体使用过程中，可以通过配置文件方便快捷地将 CHDFS 认证和 Ranger 鉴权体系集成到 GooseFS 中。

步骤如下：
1. 当部署 GooseFS 完成后，在 goosefs-env.sh 中配置 hadoop-ranger-client-for-hadoop-${hadoop.version}-${version}.jar 和 cosn-ranger-interface-${version}.jar 所在的路径：
```
GOOSEFS_CLASSPATH=${GOOSEFS_HOME}/lib/goosefs-underfs-chdfs-${version}.jar:/path/to/cosn-ranger-interface-${version}.jar:/path/to/hadoop-ranger-client-for-hadoop-${hadoop.version}-${version}.jar
```
>? 对于 EMR 的环境，可以查看 `/usr/local/service/hadoop/share/hadoop/common/lib` 这个路径是否存在上述两个依赖包，如果存在的话，将这两个包按照上述方法配置到 GooseFS 即可：
```
GOOSEFS_CLASSPATH=${GOOSEFS_HOME}/lib/goosefs-underfs-chdfs-${version}.jar:/usr/local/service/hadoop/share/hadoop/common/lib/cosn-ranger-interface-${version}.jar:/usr/local/service/hadoop/share/hadoop/common/lib/hadoop-ranger-client-for-hadoop-${hadoop.version}-${version}.jar
```
2. 确保在 core-site.xml 配置文件中，已开启 ranger 相关的配置选项：
```
  <property>
    <name>fs.ofs.ranger.enable.flag</name>
    <value>true</value>
  </property>
```
3. 在 goosefs-site.properties 中需要将 core-site.xml 的配置文件路径指定到 goosefs underfs hdfs 的配置路径中，同时开启 security authorization，这样才能保证身份认证信息能够通过 GooseFS 传递到 UFS 层：
```
goosefs.underfs.hdfs.configuration=/usr/local/service/hadoop/etc/hadoop/hdfs-site.xml:/usr/local/service/hadoop/etc/hadoop/core-site.xml
# Security properties
goosefs.security.authorization.permission.enabled=true
goosefs.security.authentication.type=SIMPLE
```
4. 以上配置至少需要同步到所有的 Master 节点上，然后重启 Master 即可开启 CHDFS 的鉴权。有关 GooseFS Ranger 的详细介绍，可参见 [使用 Apache Ranger 控制 GooseFS 的访问权限](https://cloud.tencent.com/document/product/1424/68312)。

## 其他更新点

除了上述更新之外，我们在本次版本中还优化了 GooseFS 依赖的组件：

- 升级了 RocksDB 的依赖版本到6.15.2（从5.15.10 升级到6.15.2）
- 更新了依赖的 Linux/MacOS libjnifuse 的动态链接库

同时，根据生产环境下大规模使用后的反馈，我们也修复了如下问题：

- 修复 Journal 乱序的问题
- Ratis 死锁导致的 GRPC 问题
- 修复了HDFSUnderFileSystemFactory 加载位置不正确的问题
- 修复了 log4j2 的安全漏洞问题
- 修复了ufsPath 前缀检查错误的问题

如果您想了解数据加速器 GooseFS 的更多信息，或者上手使用 GooseFS ，请参见 [数据加速器 GooseFS](https://cloud.tencent.com/document/product/1424) 产品文档。
