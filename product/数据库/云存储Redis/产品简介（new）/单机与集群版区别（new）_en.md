Tencent Cloud Redis Store (CRS) is available in two editions currently: standalone and cluster. The differences between them are shown as below:

| Edition | Standalone | Cluster |
|:--|:--|:--|
| Capacity | A maximum of 60 GB | No limit |
| Feature | Full compatibility with native Redis protocol | Limits on traverse, transaction and lua script |
| Model | Single thread | Multi-thread |
 | Value adaption | Same with native Redis | Optimum performance within 30 KB|
| Key adaption | Same with native Redis | A maximum of 127 Byte |
| Number of connections | Configurable | Unlimited, non-configurable |
| Timeout | 10 min, configurable | 30 min, non-configurable |
Note: The protocol size of a single request for the cluster instance is less than 1 MB


<br>
Tips on Selection:
1) For developers working with a small single instance (for example, for storing the data on a single server in a single region), standalone instance is recommended.
2) For the scenarios where the business data grows so fast that the upper limit of 60 GB for standalone instance may be exceeded, cluster instance is recommended initially.

Service limits on commands:
1) [Service Limits on Commands for Standalone Instances](https://www.qcloud.com/doc/product/239/%E4%BD%BF%E7%94%A8%E9%99%90%E5%88%B6)
2) [Service Limits on Commands for Cluster Instances](https://www.qcloud.com/doc/product/239/%E4%BD%BF%E7%94%A8%E9%99%90%E5%88%B6)

