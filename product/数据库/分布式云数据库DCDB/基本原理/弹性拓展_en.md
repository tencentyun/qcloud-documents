## Overview
DCDB supports real-time online expansion. There are two capacity expansion methods: adding shards and expanding the existing shards. The entire expansion process is completely transparent to the service without service downtime. Only a fraction of shards become read-only for seconds (or are interrupted) during the expansion, while the entire cluster will not be affected.

## Capacity Expansion Process
DCDB ensures automatic expansion and stability with the self-developed automatic rebalancing technology.

### 1. Add Shards for Expansion
1. After you click on the console to expand capacity, the system will calculate the bottleneck of Node A (maybe multiple nodes are actually affected) based on the load and capacity.
2. According to the configuration of new Node G, some data of Node A will be migrated (from slave) to Node G.
3. After the data is completely synchronized, Nodes A and G will validate the database (read-only for one to tens of seconds), but the entire service is not suspended.
4. Schedule and notify proxy to switch routing.
![](https://mc.qcloudimg.com/static/img/d407c9bf2740c3ceb803392448856cf2/image.png)

### 2. Expand Existing Shards
The expansion based on existing shards is actually replacing the old one with a larger physical shard.
> **Note:**
> The expansion based on existing shards does not add any shard and will not change the logic rules of sharding or number of shards.

1. Assign a new physical shard (hereinafter referred to as "new shard") based on required configuration.
2. Synchronize the data and configuration of the physical shard to be upgraded (hereinafter referred to as "old shard") to the new shard.
3. After the synchronization of data is completed, switch the routing in Tencent Cloud gateway to the new shard for continued use.
![](https://mc.qcloudimg.com/static/img/d30e97c05742feccf7728e6a326e826f/image.png)
