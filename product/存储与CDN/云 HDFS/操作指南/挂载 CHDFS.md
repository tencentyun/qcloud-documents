
创建 CHDFS 及挂载点后，可以通过挂载点挂载 CHDFS，本文为您详细介绍如何挂载 CHDFS。

## 前提条件
- 确保挂载的机器或者容器内安装了 Java 1.8。
- 确保挂载的 CVM、CPM 2.0或者容器其 VPC ，与挂载点指定 VPC 相同。
- 确保挂载的 CVM、CPM 2.0或者容器其 VPC IP，与挂载点指定权限组中有一条权限规则授权地址匹配。

## 操作步骤
1.  下载 [CHDFS-Hadoop](https://github.com/tencentyun/chdfs-hadoop-plugin) JAR 包。
2.	将 JAR 包放置对应的目录下，对于 emr 集群，可同步到所有节点的`/usr/local/service/hadoop/share/hadoop/common/lib/`目录下。
3.	编辑 core-site.xml 文件，新增以下配置：
```
<!--chdfs的实现类-->
<property>
		 <name>fs.AbstractFileSystem.chdfs.impl</name>
		 <value>com.qcloud.chdfs.fs.CHDFSDelegateFSAdapter</value>
</property>
<property>
		 <name>fs.chdfs.impl</name>
		 <value>com.qcloud.chdfs.fs.CHDFSHadoopFileSystemAdapter</value>
</property>
<!--本地cache的临时目录, 对于读写数据, 当内存cache不足时会写入本地硬盘, 这个路径若不存在会自动创建-->
<property>
		 <name>fs.chdfs.tmp.cache.dir</name>
		 <value>/data/chdfs_tmp_cache</value>
</property>
<!—appId-->      
<property>
		 <name>fs.chdfs.user.appid</name>
		 <value>125000001</value>
</property>
```
4.	将 core-site.xml 同步到所有 hadoop 节点上。
>?对于 EMR 集群，以上步骤3、4可在 EMR 控制台的组件管理中，修改 HDFS 配置即可。
5.	使用 hadoop fs 命令行工具，运行`hadoop fs –ls chdfs://${mountpoint}/`命令，这里 mountpoint 为挂载地址。如果正常列出文件列表，则说明已经成功挂载 CHDFS。
6.	可以使用 hadoop 其他命令，或者 mr 任务在 CHDFS 上运行数据任务。
对于 mr 任务，可以通过`-Dfs.defaultFS=chdfs://${mountPoint}/`将本次任务的默认输入输出 FS 改为 CHDFS。
