# 磁盘readonly问题

Elasticsearch 5.6.4版本没有磁盘容量阈值以防止磁盘被写满，因此，如果您使用Elasticsearch 5.6.4版本请关注磁盘使用量情况，及时删除无用索引或扩容磁盘。

Elasticsearch 6.4.3版本设置了磁盘水位（watermark）阈值，当磁盘使用率到达`99%`时，在该磁盘上有分片的索引将变为readonly状态，此时无法向这些索引写入数据。因此，我们建议当您发现磁盘使用率较高的时候就及时地清理索引或扩容磁盘。

## 问题表现

#### 创建index pattern超时

当您的集群已经出现磁盘状态变为readonly的状态时，您可能会发现在kibana上创建index pattern时卡住了，一直转圈圈，无法创建。这是因为当集群出现过磁盘写满时，ES会自动把索引设置block级别设置为readonly_allow_delete状态。

#### 写入索引出错

当您的集群已经出现磁盘状态变为readonly的状态时，您可能会发现即使清理了索引或者扩容了磁盘仍无法将数据写入索引，错误如下：

```
Elasticsearch exception [type=cluster_block_exception, reason=blocked by: [FORBIDDEN/12/index read-only / allow delete (api)];]
```

## 问题解决

您需要先清理无用索引释放空间或扩容磁盘，然后在Kibana界面的【Dev Tools】中使用如下命令关闭索引的只读状态：

```
PUT _all/_settings
{
  "index.blocks.read_only_allow_delete": null
}
```