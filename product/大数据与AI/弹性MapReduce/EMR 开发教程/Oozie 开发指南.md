Apache Oozie 是一个开源的工作流引擎，被设计将 hadoop 生态组件的任务编排成 Workflow，然后对其进行调度、执行、监控。本文简单介绍如何在 EMR 上使用 Oozie，详细的使用文档请参考官网,另外这里建议用户通过 Hue 的图像化界面来使用 Oozie，使用文档请移步 Hue 开发文档。
## 前提条件
已创建弹性 MapReduce（简称EMR）的 Hadoop 集群，并选择了 Oozie 服务，详情请参见 [创建 EMR 集群](https://cloud.tencent.com/document/product/589/10981)。

## 访问 Oozie WebUI
- 如果您在购买集群时勾选了开启集群节点外网，就可以在 EMR 控制台上通过单击 WebUI 链接来访问。
- 对于国内用户，建议将 WebUI 时区设置为 GMT+08:00。
![](https://qcloudimg.tencent-cloud.cn/raw/205fb90fb72f9f7befae72668e755b75.png)

### sharelib 的更新
在 EMR 集群中，已安装了 sharelib，所以您使用 Oozie 提交 Workflow 作业时，不需要再安装 sharelib。当然您也可以对 sharelib 进行编辑与更新，操作步骤如下：
```
cd /usr/local/service/oozie
tar -xf oozie-sharelib.tar.gz添加jar包到解压出的share目录下要支持的action对应的目录下bin/oozie-setup.sh sharelib create -fs hdfs://active-namenode-ip:4007 -locallib shareoozie admin --oozie http://oozie-server-ip:12000/oozie -sharelibupdate
```

## 在非 Kerberos 环境下提交 Workflow
在 oozie 的安装目录/usr/local/service/oozie，对文件 oozie-examples.tar.gz 进行解压，里面有 Oozie 支持的组件的 Workflow 示例：
```
tar -xf oozie-examples.tar.gz
```
这里以 action hive2来进行举例：
- su hadoop。
- cd examples/apps/hive2/。
- 修改 job.properties。
	- namenode 设置为 core-site.xml 下`fs.defaultFS`的值。
	-** resourceManager** 的值在 HA 模式下设置为 yarn-site.xml 下`yarn.resourcemanager.ha.rm-ids`的值，非 HA 模式下为`yarn.resourcemanager.address`的值。
	- **jdbcURL** 的值为`jdbc:hive2://hive2-server:7001/default`。
- hadoop fs -put examples。
- oozie job -debug -oozie http://oozie-server-ip:12000/oozie -config examples/apps/hive2/job.properties -run。
- oozie job -info 上一步返回的Job ID（或者通过WebUI查看） 。

## 在 Kerberos 环境下提交 Workflow
仍然以 action hive2 来进行举例，其它的注意事项请查看 hive2目录下的 README，此处不再赘述。
- kinit -kt /var/krb5kdc/emr.keytab hadoop 的 principal && su hadoop。
- cd examples/apps/hive2/。
- mv job.properties.security job.properties && mv workflow.xml.security workflow.xml。
- 修改 job.properties：
	- namenode 设置为 core-site.xml 下`fs.defaultFS`的值。
	- resourceManager 的值在 HA 模式下设置为 yarn-site.xml 下`yarn.resourcemanager.ha.rm-ids`的值，非 HA 模式下为`yarn.resourcemanager.address`的值。
	- jdbcURL 的值为`jdbc:hive2://hive2-server:7001/default`。
	- jdbcPrincipal 的值为`hive.server2.authentication.kerberos.principal`的值。
- hadoop fs -put examples。
- oozie job -debug -oozie http://oozie-server-ip:12000/oozie -config examples/apps/hive2/job.properties -run。
- oozie job -info 上一步返回的 Job ID（或者通过 WebUI 查看）。
