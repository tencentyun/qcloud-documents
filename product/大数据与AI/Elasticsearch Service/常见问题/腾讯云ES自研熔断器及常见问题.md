## 腾讯云ES自研熔断器常见问题

Elasticsearch提供了多种官方的熔断器，用于防止不当的操作导致ES集群因为OutOfMemoryError而出现问题。Elasticsearch设置有各种类型的子熔断器，负责特定请求处理的内存限制。此外，还有一个父熔断器，用于指定可在所有子熔断器上使用的内存总量。

## 腾讯云ES自研熔断器

官方熔断机制的一个不足是仅跟踪那些经常会出问题的请求来预估内存的使用，而无法根据当前节点的实际内存使用状态，来限制请求的内存使用或触发熔断。在腾讯云Elasticsearch Service中，开发了针对JVM OLD区内存使用率的自研熔断器来解决这个问题。

腾讯云Elasticsearch Service的自研熔断器监控JVM OLD区的使用率，当使用率超过`80%`时开始梯度熔断，随机丢弃部分写入及查询请求，若GC仍无法回收JVM OLD区中的内存，至使用率到达`95%`时触发完全熔断，此时将拒绝所有的写入及查询请求。当请求被拒绝时，客户端将收到如下的响应：

```
{
    "status": 403,
    "error": {
        "root_cause": [{
            "reason": "pressure too high, (smooth) bulk request circuit break",
            "type": "status_exception"
        }],
        "type": "status_exception",
        "reason": "pressure too high, (smooth) bulk request circuit break"
    }
}
```

上面的错误提示表明当前JVM OLD区负载较高，需要清理JVM中部分内存后重试。

## 常用清理内存的方法

* 清理fielddata cache：在text类型的字段上进行聚合和排序时会使用fileddata数据结构，可能占用较大内存。可以在Kibana界面的【Dev Tools】中使用如下命令查看索引的fielddata内存占用：

    ```
    GET /_cat/indices?v&h=index,fielddata.memory_size&s=fielddata.memory_size:desc
    ```

    若fielddata占用内存过高，可以在Kibana界面的【Dev Tools】中使用如下命令清理fielddata：

    ```
    POST /${fielddata占用内存较高的索引}/_cache/clear?fielddata=true
    ```

* 清理segment：每个segment的FST结构都会被加载到内存中，并且这些内存是不会被GC回收的。因此如果索引的segment数量过大，也会导致内存使用率较高。可以在Kibana界面的【Dev Tools】中使用如下命令查看各节点的segment数量和占用内存大小：

    ```
    GET /_cat/nodes?v&h=segments.count,segments.memory&s=segments.memory:desc
    ```

    若segment占用内存过高，可以通过删除部分不用的索引，或关闭索引，定期合并不再更新的索引等方式缓解。

* 扩容集群：如果您清理内存后，仍频繁触发熔断，说明您的集群规模已经不匹配于您的业务负载，最好的方式是扩大集群规模，您可以参考[扩容集群](https://cloud.tencent.com/document/product/845/32096)