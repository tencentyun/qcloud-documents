### 磁盘 readonly 的产生原因和解决办法是什么？
Elasticsearch 5.6.4版本没有磁盘容量阈值以防止磁盘被写满，因此，如果您使用 Elasticsearch 5.6.4版本请关注磁盘使用量情况，及时删除无用索引或扩容磁盘。

Elasticsearch 6.4.3版本设置了磁盘水位（watermark）阈值，当磁盘使用率到达`99%`时，在该磁盘上有分片的索引将变为 readonly 状态，此时无法向这些索引写入数据。因此，我们建议当您发现磁盘使用率较高的时候就及时地清理索引或扩容磁盘。

#### 产生原因

1. **创建 index pattern 超时**
当您的集群磁盘状态变为 readonly 时，将无法在 kibana 上创建 index pattern。这是因为当集群磁盘写满时，ES 会自动把索引设置的 block 级别设为 readonly_allow_delete 状态。
2. **写入索引出错**
当您的集群磁盘状态变为 readonly 时，清理索引或扩容磁盘仍无法将数据写入索引，错误如下：
 - 索引只读错误：
```
Elasticsearch exception [
    type=cluster_block_exception, 
    reason=blocked by: [FORBIDDEN/12/index read-only / allow delete (api)];
]
```
 - 集群只读错误：
```
Elasticsearch exception [
    type=cluster_block_exception, 
    reason=blocked by: [FORBIDDEN/13/cluster read-only / allow delete (api)];
]
```

#### 解决办法

您需要先清理无用索引释放空间或扩容磁盘，然后在 Kibana 界面的【Dev Tools】中使用如下命令：
* 关闭索引只读状态：
```
PUT _all/_settings
{
  "index.blocks.read_only_allow_delete": null
}
```
* 关闭集群只读状态：
```
PUT _cluster/settings
{
  "persistent": {
    "cluster.blocks.read_only_allow_delete": null
  }
}
```
