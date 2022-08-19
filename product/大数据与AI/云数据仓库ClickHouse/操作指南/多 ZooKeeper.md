## 功能介绍
腾讯云上创建 ClickHouse 高可用集群之后，会默认创建一个 Zookeeper 集群来为 ClickHouse 集群提供服务。但是当 Zookeeper 集群负载过高时，会造成 ClickHouse 集群写入阻塞，严重时会导致集群崩溃。为此 cdwch 支持了多 Zookeeper 方案，用户可以根据集群的负载情况添加多套 Zookeeper 来为 ClickHouse 服务。
## 注意事项
1. 多 Zookeeper 方案只能应用于高可用集群。
2. 最多可以支持7套额外的 Zookeeper 集群。
3. 同一个集群所有的 Zookeeper 规格保持一致，垂直升降配后也会保持同一规格。
4. 多 Zookeeper 使用只是在创建表的时候有区别，其他按照数仓常规操作即可。

## 控制台操作步骤
1. 登录 [CDWCH](https://console.cloud.tencent.com/cdwch) 控制台，在**集群列表**中选择对应的集群，在集群详情页面右下角单击**升级多 ZK** 页面。
![](https://qcloudimg.tencent-cloud.cn/raw/8b19d59bce2146de89f6ed66d0f48411.jpg)
![](https://qcloudimg.tencent-cloud.cn/raw/d9d0136abbe06e1f7caf0bb9e4b2bdb5.jpg)
2. 可在配置文件 config.xml 中查看已经存在的多 Zookeeper 信息。
![](https://qcloudimg.tencent-cloud.cn/raw/86a9750bf4b2d172711401dd5e58fe2f.jpg)
3. 创建多 Zookeeper 之后，也可以对集群中的 Zookeeper 节点进行垂直升降配和扩容磁盘。
![](https://qcloudimg.tencent-cloud.cn/raw/13a02eb94ef53d4a36d1ade3e45b1a11.jpg)

## 多 Zookeeper 使用方法

1. 创建库。
```
CREATE DATABASE IF NOT EXISTS testdb ON CLUSTER default_cluster;
```

2. 创建使用默认Zookeeper 的表。
```
CREATE TABLE testdb.account ON CLUSTER default_cluster(accountid UInt16,name String,address String,year UInt64) ENGINE =ReplicatedMergeTree('/clickhouse/tables/{layer}-{shard}/testdb/account', '{replica}') ORDER BY (accountid);
```

3. 创建使用多 Zookeeper 的表。
```
--创建表时，如果是使用第二套zookeeper就在创建表的zookeeper路径前加：'zookeeper2:'前缀，以此类推，使用第三套zookeeper，则加'zookeeper3'前缀。
CREATE TABLE testdb.account2 ON CLUSTER default_cluster(accountid UInt16,name String,address String,year UInt64) ENGINE =ReplicatedMergeTree('zookeeper2:/clickhouse/tables/{layer}-{shard}/testdb/account2', '{replica}') ORDER BY (accountid);
```
