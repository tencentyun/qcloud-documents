Hadoop 默认将 YARN 的作业日志存储在 hdfs 上，腾讯云 EMR 还提供了将 YARN 作业日志存储在外部存储 COS 上。

## 前提条件
EMR 集群需要支持 COS，详情可参考 [使用 API 分析 HDFS/COS 上的数据](https://cloud.tencent.com/document/product/589/19013)。

## 操作步骤
1. 在 `yarn-site.xml` 修改配置，并配置下发所有节点。
```
yarn.nodemanager.remote-app-log-dir=cosn://[bucket_name]/[logs_dirs]
```
2. 在`core-site.xml`新增配置，并配置下发所有节点。
```
fs.AbstractFileSystem.cosn.impl=org.apache.hadoop.fs.cosnative.COS
```
3. 重启集群所有 `nodemanager/datanode` 服务。
4. 运行 `hive/spark` 作业，查看存储在 COS 上的作业日志。
```
hdfs dfs -ls cosn://[bucket_name]/[logs_dirs] 
```
