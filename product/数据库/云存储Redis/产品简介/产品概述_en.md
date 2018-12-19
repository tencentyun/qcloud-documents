## 1 What is Cloud Redis Store Service?

Cloud Redis Store (CRS) is a highly available and reliable Redis service platform built on Tencent Cloud's years of technical expertise in distributed cache. It is designed for Redis business operations. With distributed storage, CRS pushes beyond the performance and capacity constraints of standalone machines to enhance Redis's service capabilities. Thanks to the automatic disaster recovery based on the master/slave hot backup and multiple data copies stored on multiple nodes, both high availability and reliability are ensured for users.

Being available in two specifications, master/slave and cluster, CRS provides master/slave double-node instances. Master/slave instances have a capacity ranging from 1 to 60 GB, and can meet the requirements for capacity and performance from general users. Cluster instances theoretically have no capacity limit to satisfy the requirements for large capacity and high performance. But for a capacity greater than 300 GB, you need to submit a ticket for support.
In practice, CRS is compatible with Redis protocol, and supports data types such as string, chain table, set, sorted set and hash table.

(Note: CRS does not allow the access from public network. You need to purchase a CVM to access CRS.)

## 2 CRS Features

1) Distributed: User's storages are distributed over multiple physical machines to be completely free from the capacity and resource constraints of standalone machines.

2) High availability: Each instance provides master/slave hot backup, automatic monitoring for crash and automatic disaster recovery.

3) High reliability: Persistence of data storage allows daily cold backup and automatic rollback.

4) Elastic expansion of capacity: Unlimited expansion is supported for a single cluster instance, eliminating the worry about resource constraints. During the expansion, service will not be interrupted and therefore no changes are perceived by users.

5) Security: VPC is supported to improve the cache security.

## 3 Release Notes

Master/slave and cluster instances are compatible with v3.0 and v3.0 Redis protocols, respectively. There are some unsupported commands. For more information, please see [Service Limits](/doc/product/239/使用限制).
