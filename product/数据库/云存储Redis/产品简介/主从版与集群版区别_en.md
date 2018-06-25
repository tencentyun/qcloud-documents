Tencent Cloud Redis Store (CRS) is available in two editions currently: master/salve and cluster. The differences between them are shown as below:

| Features | Master/Slave | Cluster |
|:--|:--|:--|
| Capacity | A maximum of 60 GB | No limit |
| Feature | Full compatibility with native Redis protocol | Limits on traverse, transaction and lua script |
| Model | Single thread | Multi-thread |
| Value adaption | Same with native Redis | Optimum performance within 30 KB|
| Key adaption | Same with native Redis | A maximum of 127 Byte |
| Number of connections | Configurable | Unlimited, non-configurable |
| Timeout | 10 min, configurable | 30 min, non-configurable |
Note 1: The protocol size of a single request for the cluster instance is less than 10 MB
Note 2: The maximum number of connections for master/salve instances is 9000


<br>
Tips on Selection:
1) For developers working with a small single instance (for example, for storing the data on a single server in a single region), master/salve instance is recommended.
2) For the scenarios where the business data grows so fast that the upper limit of 60 GB for standalone instance may be exceeded, cluster instance is recommended initially.

Service limits on commands:
1) [Service Limits on Commands for Master/Slave Instances](https://cloud.tencent.com/doc/product/239/%E4%BD%BF%E7%94%A8%E9%99%90%E5%88%B6)
2) [Service Limits on Commands for Cluster Instances](https://cloud.tencent.com/doc/product/239/%E4%BD%BF%E7%94%A8%E9%99%90%E5%88%B6)
