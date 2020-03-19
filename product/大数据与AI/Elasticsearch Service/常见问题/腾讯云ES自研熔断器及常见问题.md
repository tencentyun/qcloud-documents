Elasticsearch 提供了多种官方的熔断器（circuit breaker），用于防止内存使用过高导致 ES 集群因为 OutOfMemoryError 而出现问题。Elasticsearch 设置有各种类型的子熔断器，负责特定请求处理的内存限制。此外，还有一个父熔断器，用于限制所有子熔断器上使用的内存总量。

### 腾讯云 ES 自研熔断器的熔断机制是什么？

官方熔断机制的一个不足是仅跟踪那些经常会出问题的请求来预估内存的使用，而无法根据当前节点的实际内存使用状态，来限制请求的内存使用或触发熔断。在腾讯云 ES 中，开发了针对 JVM OLD 区内存使用率的自研熔断器来解决这个问题。

腾讯云 ES 的自研熔断器监控 JVM OLD 区的使用率，当使用率超过`85%`时开始拒绝写入请求，若 GC 仍无法回收 JVM OLD 区中的内存，在使用率到达`90%`时将拒绝查询请求。当请求被拒绝时，客户端将收到如下的响应：
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

上面的错误提示表明当前 JVM OLD 区负载较高，需要清理 JVM 中部分内存后重试。

### 常用清理内存的方法是什么？

* 清理 fielddata cache：在 text 类型的字段上进行聚合和排序时会使用 fileddata 数据结构，可能占用较大内存。可以在 Kibana 界面的【Dev Tools】中使用如下命令查看索引的 fielddata 内存占用：
    ```
    GET /_cat/indices?v&h=index,fielddata.memory_size&s=fielddata.memory_size:desc
    ```
   若 fielddata 占用内存过高，可以在 Kibana 界面的【Dev Tools】中使用如下命令清理 fielddata：
    ```
    POST /${fielddata占用内存较高的索引}/_cache/clear?fielddata=true
    ```
* 清理 segment：每个 segment 的 FST 结构都会被加载到内存中，并且这些内存是不会被 GC 回收的。因此如果索引的 segment 数量过大，也会导致内存使用率较高。可以在 Kibana 界面的【Dev Tools】中使用如下命令查看各节点的 segment 数量和占用内存大小：

    ```
    GET /_cat/nodes?v&h=segments.count,segments.memory&s=segments.memory:desc
    ```
    若 segment 占用内存过高，可以通过删除部分不用的索引，关闭索引，或定期合并不再更新的索引等方式缓解。

* 扩容集群：如果您清理内存后，仍频繁触发熔断，说明您的集群规模已经不匹配于您的业务负载，最好的方式是扩大集群规模，您可以参考 [扩容集群](https://cloud.tencent.com/document/product/845/32096)。
