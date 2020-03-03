### 出现写入拒绝（Bulk Reject）问题如何解决？

#### 问题现象
集群在某些情况下会出现写入拒绝率增大（bulk reject）的现象，具体表现为，bulk 写入的时候，会有以下类似报错：
```
[2019-03-01 10:09:58][ERROR]rspItemError: {"reason":"rejected execution of org.elasticsearch.transport.TransportService$7@5436e129 on EsThreadPoolExecutor[bulk, queue capacity = 1024, org.elasticsearch.common.util.concurrent.EsThreadPoolExecutor@6bd77359[Running, pool size = 12, active threads = 12, queued tasks = 2390, completed tasks = 20018208656]]","type":"es_rejected_execution_exception"}
```
- 可在云监控看到集群写入拒绝率增大。
![](https://main.qcloudimg.com/raw/998766e0b7117412fb13fd7ca37b2f35.png)
- 也可在 kibana 控制台，通过命令查看正在拒绝或者历史拒绝的个数。
```
GET _cat/thread_pool/bulk?s=queue:desc&v
```
一般默认队列是1024，如果 queue 下有1024，说明这个节点有 reject 的现象。
![](https://main.qcloudimg.com/raw/c31a56cabaa51518be460baa338e5521.png)

#### 问题定位
引起 bulk reject 的大多原因是 shard 容量过大或 shard 分配不均，具体可通过以下方法进行定位分析。
1. 检查分片（shard）数据量是否过大
分片数据量过大，有可能引起 Bulk Reject，建议单个分片大小控制在20GB - 50GB左右。可在 kibana 控制台，通过命令查看索引各个分片的大小。
```
GET _cat/shards?index=index_name&v
```
![](https://main.qcloudimg.com/raw/551e6cb4aaccd8391f619f0ecef0129d.png)
2. 检查分片数是否分布不均匀
集群中的节点分片分布不均匀，有的节点分配的 shard 过多，有的分配的 shard 少。
 - 可在 ES 控制台集群详情页的【集群监控】>【节点状态】查看，具体操作可参见 [查看监控](https://cloud.tencent.com/document/product/845/16995)。
 - 也可通过 curl 客户端，查看集群各个节点的分片个数。
```
curl "$p:$port/_cat/shards?index={index_name}&s=node,store:desc" | awk '{print $8}' | sort | uniq -c | sort
```
结果如下图（第一列为分片个数，第二列为节点 ID），有的节点分片为1，有的为8，分布极不均匀。
![](https://main.qcloudimg.com/raw/62d75ef4823d87934ab64a9eb243a556.png)

#### 解决方案

1. 设置分片大小
分片大小可以通过 index 模版下的 number_of_shards 参数进行配置（模板创建完成后，再次新创建索引时生效，老的索引不能调整）。
2. 调整分片数据不均匀
 - 临时解决方案：
如果发现集群有分片分配不均的现象，可以通过设置 routing.allocation.total_shards_per_node 参数，动态调整某个 index 解决，[参考地址](https://www.elastic.co/guide/en/elasticsearch/reference/6.6/allocation-total-shards.html)。
>!total_shards_per_node 要留有一定的 buffer，防止机器故障导致分片无法分配（例如10台机器，索引有20个分片，则 total_shards_per_node 设置要大于2，可以取3）。
>
参考命令：
```
PUT {index_name}/_settings
 {
    "settings": {
      "index": {
        "routing": {
          "allocation": {
            "total_shards_per_node": "3"
          }
        }
      }
    }
 }
```
 - 索引生产前设置：
通过索引模板，设置其在每个节点上的分片个数。
```
PUT _template/｛template_name｝
{
    "order": 0,
    "template": "｛index_prefix@｝*",  //要调整的index前缀
    "settings": {
      "index": {
        "number_of_shards": "30",   //指定index分配的shard数，可以根据一个shard 30GB左右的空间来分配
        "routing.allocation.total_shards_per_node":3  //指定一个节点最多容纳的shards数
      }
    },
    "aliases": {}
  }
```

