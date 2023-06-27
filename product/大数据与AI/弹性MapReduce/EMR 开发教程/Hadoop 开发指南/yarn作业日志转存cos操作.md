Hadoop 默认将 YARN 的作业日志存储在 hdfs 上，腾讯云 EMR 还提供了将 YARN 作业日志存储在外部存储 COS 上。

## 前提条件
EMR 集群需要支持 COS，详情可参考 [使用 API 分析 HDFS/COS 上的数据](https://cloud.tencent.com/document/product/589/19013)。

## 操作步骤
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在集群列表中选择对应的集群，单击**集群服务**进入集群服务列表。
2. 通过 YARN 服务面板右上角**操作 > 配置管理**，找到  `yarn-site.xml` 配置文件并修改以下配置，下发所有节点。
```
yarn.nodemanager.remote-app-log-dir=cosn://$bucketname/$logs_dirs
```
其中，$bucketname 为您的存储桶名，$logs_dirs 为您希望将 yarn 作业日志转存的文件目录。
3. 通过 HDFS 服务面板右上角**操作 > 配置管理**，找到 `core-site.xml` 并新增以下配置项，下发所有节点。
```
fs.AbstractFileSystem.cosn.impl=org.apache.hadoop.fs.cosnative.COS
```
4. 在**集群服务 > HDFS  >  角色管理**中重启集群所有 `nodemanager/datanode` 服务。
5.运行 `hive/spark` 作业后，可通过以下命令查看存储在 COS 上的作业日志。
```
hdfs dfs -ls cosn://$bucketname/$logs_dirs
```
