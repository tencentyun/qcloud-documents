### Redis Community

 TencentDB for Redis is a highly available, highly reliable Redis service platform built on Tencent's years of technical expertise in distributed cache. Redis Community engine is developed based on Redis Community 2.8, and a new version for Redis Community 4.0 will be available soon. The Community version provides native Redis experience and supports various scenarios. Redis Community is now available in three versions: Standalone, Master/Slave, and Cluster, allowing flexible deployment in different business scenarios.

 **Redis Community engine supports the following versions:**

  - **Standalone**: Suitable for caching-only scenarios, supports flexible configuration changes for single-node clusters in scenarios with high QPS, and provides a capacity ranging from 1 to 60 GB and ultra-high cost performance.
  - **Master/Slave**: When the system works, the data on the Master and Slave nodes is synchronized in real time. When the Master node fails, the system automatically switches the service to the Slave node in seconds, without causing any impact on the service. The Master/Slave architecture ensures the high availability of the system service. 0.25-60 GB of specifications are available.
  - **Cluster**: Cluster instances adopt the distributed architecture, so you can flexibly select the number of shards, the capacity of a shard and the number of replicas, to realize capacity expansion and reduction without affecting the service. This version is available with a capacity ranging from 16 GB to 2 TB and provides the ability to handle up to 10 million queries per second.
