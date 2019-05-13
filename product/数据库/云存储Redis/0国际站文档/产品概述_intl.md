## TencentDB for Redis

 TencentDB for Redis is a highly available, highly reliable Redis service platform built on Tencent's years of technical expertise in distributed cache. TencentDB for Redis has two storage engines: Redis Community and Tencent Cloud's proprietary CKV. TencentDB for Redis is now available in three versions: Standalone, Master/Slave, and Cluster, allowing flexible deployment in different business scenarios.

 ### Cloud Redis Storage engine

  - **Standalone**: Suitable for caching-only scenarios, supports flexible configuration changes for single-node clusters in scenarios with high QPS, and provides a capacity ranging from 1 to 60 GB and ultra-high cost performance.
  - **Master/Slave**: When the system works, the data on the Master and Slave nodes is synchronized in real time. When the Master node fails, the system automatically switches the service to the Slave node in seconds, without causing any impact on the service. The Master/Slave architecture ensures the high availability of the system service. 0.25-60 GB of specifications are available.
  - **Cluster**: Cluster instances adopt the distributed architecture, so you can flexibly select the number of shards, the capacity of a shard and the number of replicas, to realize flexible capacity expansion and reduction without affecting the service. This version is available with a capacity ranging from 16 GB to 2 TB and provides the ability to handle up to 10 million queries per second.

 ### Database CKV engine:

  - **Master/Slave**: When the system works, the data on the Master and Slave nodes is synchronized in real time. This version is available with a capacity ranging from 4 to 384 GB.
  - **Cluster**: Cluster instances adopt the distributed architecture, so you can flexibly select the number of shards, the capacity of a shard and the number of replicas, to realize flexible capacity expansion and reduction without affecting the service. This version is available with a capacity ranging from 16 GB-2 TB and provides the ability to handle up to 10 million queries per second.



 ## Cloud Redis Storage Features

 1. High availability: Provides master/slave hot backup, automatic monitoring for crashes and automatic disaster recovery.
 2. High reliability: The Master/Slave and Cluster versions can ensure persistent data storage, allowing daily cold backups and automatic rollbacks.
 3. High flexibility: Freely expanding or reducing the capacity of instances. The Cluster version supports expanding and reducing the capacity of nodes and replicas.
 4. Security: VPC support is available for improved cache security.
 5. Distributed: User's storages are distributed over multiple physical machines to be completely free from the capacity and resource constraints of standalone machines.

 ## Release Notes

 The Redis Community engine is compatible with Redis 2.8 protocols and commands. Redis Community 4.0 will be available soon. Tencent Cloud's proprietary CKV engine is compatible with Redis 3.2 protocols and commands.

