## Overview
The horizontal split is actually the basic principle of distributed database. Each node is involved in computing and data storage, but only for a part of the data. Therefore, no matter how the business grows, we simply need to keep adding devices to the distributed cluster to handle the growing computing and storage needs.

## Horizontal Split
 **Horizontal split (table split)**: According to certain rules, the data of a table is split across multiple physically independent database servers to form a "separate" database "shard". Multiple shards together form a logically complete database instance.

- In a conventional stand-alone database, read and write of a complete table will be done on only one physical storage device.
![](https://mc.qcloudimg.com/static/img/6c5dca25ea4df9d72e10143c9defe13a/image.png)
- For distributed database, according to the shard keys set when creating the table, the system will automatically distribute data to different physical shards, but the table is still a logically complete table.
![](https://mc.qcloudimg.com/static/img/fd0bd977b8ecc7ec9858b8f463090d6d/image.png)

- In DCDB, the data sharding is usually required to find a shardkey to determine the split dimension, and then use a field modulo operation (HASH) program for table split, and the field for calculating HASH is shardkey. HASH algorithm can basically guarantee the data is relatively evenly distributed in different physical devices.

### Data writing (shardkey included in SQL statement)
1. Write a line of data by the business.
2. Perform hash of shardkey by gateway.
3. Different hash value ranges correspond to different shards (decided by pre-sharding algorithm of scheduling system).
4. Data is stored in the actual corresponding shard according to the sharding algorithm.

![](https://mc.qcloudimg.com/static/img/5dd0a9883398f72c82a7e7c6b0b0b0e9/image.png)

## Data Aggregation
 **Data aggregation**: If the data of a query SQL statement involve multiple split tables, SQL will be routed to multiple split tables for execution. DCDB will merge the data returned by each split table based on the original SQL semantics, and the final result is returned to the user.
> **Note:**
> For the execution of SELECT statement, it is recommended to include the shardkey field, and otherwise the gateway may aggregate the execution results after a full table scan. Full table scan is slow, which will cause a great impact on performance.

### Data reading (specific shardkey included):
1. When the business sends a Select request including shardkey, the gateway performs a hash of the shardkey.
2. Different hash value ranges correspond to different shards.
3. Data is obtained from the corresponding shard according to the sharding algorithm.

### Data reading (specific shardkey not included):
1. A Select request without shardkey sent by the business will be sent to all of the shards.
2. Shards send back data to Proxy after querying their own content.
3. Proxy aggregates the data according to SQL rules, and then responds to the gateway.
![](https://mc.qcloudimg.com/static/img/89b6fdca310ab3a51b2a573ba0b63373/image.png)
