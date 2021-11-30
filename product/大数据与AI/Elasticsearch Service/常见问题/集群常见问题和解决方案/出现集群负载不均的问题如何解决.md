## 问题现象
集群在某些情况下会个别节点 CPU 使用率远高于其他节点的现象，具体表现为 ES 集群控制台节点监控上可以明显看到某些节点 CPU 使用率很高。

## 问题原因
- 索引分片设计不合理
- Segment 大小不均
- 存在典型的冷热数据需求场景

## 原因分析及解决方案
### Shard 设置不合理
1. 登录 Kibana 控制台，在开发工具中执行以下命令，查看索引的 shard 信息，确认索引的 shard 在负载高的节点上呈现的数量较多，说明 shard 分配不均。
```
GET _cat/shards?v
```
2. 登录 Kibana 控制台，在开发工具中执行以下命令，查看索引信息。结合集群配置，确认存在节点 shard 分配不均的现象。
```
GET _cat/indices?v
```
3. 重新分配分片，合理规划 shard，确保主 shard 数与副 shard 数之和是集群数据节点的整数倍。
>!Elasticsearch 在检索过程中也会检索 `.del` 文件，然后过滤标记有 `.del` 的文档，这会降低检索效率，耗费规格资源，建议在业务低峰期进行强制合并操作，具体请参见 [force merge](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/indices-forcemerge.html)。

#### shard 规划建议
Shard 大小和数量是影响 Elasticsearch 集群稳定性和性能的重要因素之一。Elasticsearch 集群中任何一个索引都需要有一个合理的 shard 规划。合理的 shard 规划能够防止因业务不明确，导致分片庞大消耗 Elasticsearch 本身性能的问题。以下是 shard 规划时的几个建议：
- 尽量遵循索引单分片20g - 50g的设计原则。
2. 索引尽量增加时间后缀，按时间滚动，方便管理。
3. 在遵循单分片设计原则的前提下，预测出索引最终大小，并根据集群节点数设计索引分片数量，使分片尽量平均分布在各个节点。

>!主分片不是越多越好，因为主分片越多，Elasticsearch 性能开销也会越大。建议单节点 shard 总数按照单节点内存×30进行评估，如果 shard 数量太多，极易引起文件句柄耗尽，导致集群故障。

### Segment 大小不均
1. 在查询 body 中添加 `"profile": true`，检查 test 索引是否存在某个 shard 查询时间比其他 shard 长。
2. 查询中分别指定 `preference=_primary` 和 `preference=_replica`，在 body 中添加 `"profile": true`，分别查看主副 shard 查询消耗的时间。检查较耗时的 shard 主要体现在主 shard 上还是副 shard 上。
3. 登录 Kibana 控制台，在开发工具中执行以下命令，查看 shard，并根据其中 segment 信息分析问题所在，确认负载不均与 segment 大小不均有关。
```
GET _cat/segments/index?v&amp;h=shard,segment,size,size.momery,ip
GET _cat/shards?v
```
4. 参考以下两种方法其中一种解决问题：
 - 在业务低峰期进行强制合并操作，具体请参见 [force merge](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/indices-forcemerge.html)，将缓存中的 delete.doc 彻底删除，将小 segment 合并成大 segment。
 - 重启主 shard 所在节点，触发副 shard 升级为主 shard。并且重新生成副 shard，副 shard 复制新的主 shard 中的数据，保持主副 shard 的 segment 一致。

### 存在典型的冷热数据需求场景
如果查询中添加了 routing 或查询频率较高的热点数据，则必然导致数据出现负载不均。
