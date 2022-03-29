## 概述
Apache Ranger 是大数据生态系统中用于控制访问权限的一个标准鉴权组件，GooseFS 作为大数据和数据湖场景下的加速存储系统，也支持接入 Apache Ranger 的统一鉴权平台。

此外云 HDFS（Cloud HDFS，CHDFS）作为公有云上的 HDFS 文件存储服务、大数据分布式存储系统，也支持接入 Apache Ranger 的统一鉴权平台。

当您使用 CHDFS 作为 GooseFS 的底层存储系统时，同时您的 CHDFS 已经接入 Apache Ranger， 想要使用这一权限体系，那么您可以参考本文章实施该方案。

实施该方案后，您在计算集群中使用 GooseFS 服务对接公有云 CHDFS 时，如果您使用的 CHDFS 已经对接了 Apache Ranger 鉴权平台，您可以直接复用已经配置完成的权限，无需再进行额外的权限配置。


## 环境准备

您需要提前准备如下环境：

- GooseFS 运行环境：GooseFS-1.2.0 版本以上。
- hadoop-ranger-client-for-hadoop-${hadoop.version}-${version}.jar（ranger client 的实现类），可以由运行环境来提供。
- cosn-ranger-interface-${version}.jar（ranger 的接口类），可以由运行环境来提供。

>!
> - ${hadoop.version} 的版本必须与 GooseFS 依赖的 Hadoop 版本一致，默认 GooseFS 依赖的 Hadoop 版本是 3.3.0，因此一定要注意提供 hadoop-ranger-client-for-hadoop-3.3.0-${version}.jar 和 cosn-ranger-interface-${version}.jar（基于hadoop-common-3.3.0 编译）。
> - 默认 CHDFS 只提供了 2.8.5，因此需要自行基于 hadoop-common-3.3.0 编译 CHDFS ranger 的两个依赖包，或者下载 GooseFS with hadoop-2.8.5 的依赖包来适配 hadoop-2.8.5 环境。
>

## 实践步骤

实施该方案前，您需要提前准备好环境，并且安装部署 GooseFS 集群，同时在 CHDFS 服务上创建好文件系统，最后为文件系统开启 Ranger 服务。

### 安装部署

完成以上环境准备工作后，您可以按照如下操作执行：

1. 在 goosefs-env.sh 中配置 hadoop-ranger-client-for-hadoop-${hadoop.version}-${version}.jar 和 cosn-ranger-interface-${version}.jar 所在的路径：
```
GOOSEFS_CLASSPATH=${GOOSEFS_HOME}/lib/goosefs-underfs-chdfs-${version}.jar:/path/to/cosn-ranger-interface-${version}.jar:/path/to/hadoop-ranger-client-for-hadoop-${hadoop.version}-${version}.jar
```
如果您使用了 EMR 计算服务，可以查阅 `/usr/local/service/hadoop/share/hadoop/common/lib` 这个路径是否存在上述两个依赖包；如果存在上述依赖包，将这两个包按照上述方法配置到 GooseFS 即可：
```
GOOSEFS_CLASSPATH=${GOOSEFS_HOME}/lib/goosefs-underfs-chdfs-${version}.jar:/usr/local/service/hadoop/share/hadoop/common/lib/cosn-ranger-interface-${version}.jar:/usr/local/service/hadoop/share/hadoop/common/lib/hadoop-ranger-client-for-hadoop-${hadoop.version}-${version}.jar
```
>! ${GOOSEFS_HOME}/lib/goosefs-underfs-chdfs-${version}.jar 的依赖需要显式加到 GOOSEFS 的 CLASSPATH 中。其配置的目的是为了保证 GooseFS 的 CHDFS 的类加载器与 CHDFS Ranger 相关依赖的类加载相同，否则会出现类加载器不同，导致的配置对象传递出错。
>
2. 确保在 core-site.xml 配置文件中，开启了 ranger 相关的配置选项：
```
  <property>
    <name>fs.ofs.ranger.enable.flag</name>
    <value>true</value>
  </property>
```
3. 在 goosefs-site.properties 中需要将 core-site.xml 的配置文件路径指定到 goosefs underfs hdfs 的配置路径中，同时开启 security authorization。此操作可以保证身份认证信息能够通过 GooseFS 传递到底层文件存储 CHDFS 服务上：
```
goosefs.underfs.hdfs.configuration=/usr/local/service/hadoop/etc/hadoop/hdfs-site.xml:/usr/local/service/hadoop/etc/hadoop/core-site.xml
#Security properties
goosefs.security.authorization.permission.enabled=true
goosefs.security.authentication.type=SIMPLE
```
4. 上述所有配置必须同步到所有的 Master 节点上。
5. 完成配置同步后，重启 GooseFS 的 Master 节点，即可开启 CHDFS Ranger 的鉴权。有关 CHDFS 的 Ranger 鉴权配置，可参见 [CHDFS Ranger 权限体系解决方案](https://cloud.tencent.com/document/product/1105/53307)。

