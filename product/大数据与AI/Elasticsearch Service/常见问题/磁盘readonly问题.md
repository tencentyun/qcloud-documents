
Elasticsearch设置了磁盘水位（watermark）阈值，当磁盘使用率到达`99%`时，在该磁盘上有分片的索引将变为readonly状态，此时无法向这些索引写入数据。因此，我们建议当您发现磁盘使用率较高的时候就及时地清理索引或扩容磁盘。

当您的集群已经出现磁盘状态变为readonly的状态时，您可能会发现即使清理了索引或者扩容了磁盘仍无法将数据写入索引，错误如下：

```
Elasticsearch exception [type=cluster_block_exception, reason=blocked by: [FORBIDDEN/12/index read-only / allow delete (api)];]
```

此时，需要您在Kibana界面的【Dev Tools】中使用如下命令关闭索引的只读状态：

```
PUT _all/_settings
{
  "index.blocks.read_only_allow_delete": null
}
```