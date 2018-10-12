### About Redis 4.0
 Redis 4.0 is a new version developed by the Tencent Cloud Redis team based on Redis Community 4.0. With a distributed architecture, Redis 4.0 maximizes the flexibility, availability, and high performance with up to 10 million QPS. It supports Standalone, Master/Slave, Cluster and multi-replica sets, as well as vertical and horizontal capacity expansion and reduction, thus maximizing its flexibility. Redis 4.0 supports horizontal extension of 1-128 shards and vertical extension of 0-5 replica sets. The capacity expansion/reduction and the migration process almost do not affect the business, thus maximizing the flexibility.<br><br>
 ![](https://main.qcloudimg.com/raw/28b67a0b4de50e751fd2119876019ffd.svg)

 ### Specifications for Redis 4.0
 - Shard specifications: 0.25, 1, 2, 4, 8, 12, 16, 20, 24, 28, and 32 (GB) 
 - Number of shards: 1, 3, 5, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96, and 128 
 - Number of replicas: 0, 1, 2, 3, 4, and 5 

 ### Cluster mode
 - When the number of shards is greater than 1, Redis automatically enables the cluster mode. Then, data sharding is automatically started, and the system provides data balance and data migration features.
 - The cluster mode supports the shard specifications of 4-32 GB, while the minimum specification for non-cluster mode is 4 GB.
 - The cluster mode is compatible with some commands in the non-cluster mode. For more information, see **Limits on the Cluster Mode** below.
 - Redis 4.0 supports upgrading from non-cluster mode to cluster mode, or vice versa. The migration process does not affect the business.

 ### Replica notes
 - If number of replicas = 0, Redis does not guarantee high reliability of data. Once the HA system detects a node failure, it will immediately enable a new node to provide services (**there is no data on this node**). This is not suitable for scenarios requiring high reliability of data.
 - If number of replicas = 1, Redis provides real-time master/slave hot backup of data to guarantee the high reliability and availability of data. Once the HA system detects a node failure, it will switch the request to the slave node and add another slave node to the system.
 - If number of replicas > 1, Redis provides real-time master/slave hot backup of data and enables the read-only slave node feature.


 ### Features of Redis 4.0

 **High flexibility** 
 Redis Community 4.0 supports horizontal capacity expansion and reduction in the range of 1-128 nodes, as well as vertical capacity expansion and reduction in the range of 0-5 replica sets. It supports various application scenarios through the adjustment of one instance.

 **Ultra-high system availability** 
 Redis Community 4.0 supports horizontal (shard-based) and vertical (replica-based) capacity expansion and reduction without affecting the business to maximize the system availability. The Cloud Redis Storage has optimized the original version to support a minimum of one shard, and the system supports capacity expansion and reduction in the range of 1-128 shards.
  
  **High compatibility**
 As to application scenarios, Redis Community 4.0 supports native Cluster scenarios in Redis Community, and is compatible with Codis, Jedis and other intelligent client scenarios.
  
  **OPS-friendliness**
 By maximizing the system capabilities, Redis Community 4.0 provides shard-based monitoring and management, sharding data migration and balance, and advanced features of big Key and hot Key, so as to ensure the complete management and OPS of the system.

 ### Scenarios

 **Caching-only scenarios** 
 Redis 4.0 provides a standalone version of Redis services when you configure 0 replica set. The single-replica version has only one database node, and when the node fails, the system will start another Redis process (**there is no data**). When the auto failover is completed for the failed node, the application needs to preheat the data again to prevent the access pressure on the backend databases.

 >Note: Since single-replica version cannot ensure data reliability and the service needs to be preheated after a node failure, it is recommended to use the dual-replica high-availability version instead of the single-replica version for sensitive services that require high reliability of data.

 **Master/slave high-availability scenarios**
 Selects a single node and select a single replica set for this node to ensure the master/slave high availability and provides the master/slave hot backup and auto failover capabilities, thus ensuring the high availability of Redis services.

  **Scenarios of read/write separation**  
 If the number of configured node replicas is greater than 1, Cloud Redis Storage provides the read/write separation capability automatically to improve the read performance of a single node vertically. It supports a maximum of 5 replica sets, and the configuration of read access weights of the master node and each replica node.
  
 **High-performance scenarios for multiple shards**
  When the number of configured nodes is greater than 1 (more than 1 shard), Cloud Redis Storage automatically enables the assignment mode to assign different Keys to multiple nodes to improve the system performance horizontally.
  


 ### Limits on the cluster mode
 When the number of shards selected is greater than 1, the system enables the cluster mode by default, and the data will be automatically Hashed to multiple shards. The cluster mode does not provide specifications less than 4 GB.
 In the cluster mode of Redis Community 4.0, there are **supported commands**, **commands with limited support**, **custom commands** and **unsupported commands**. The following error may be returned for unsupported command systems:
   ```
   select 1
   (error) ERR unknown command 'select'
   ```

 - **Unsupported commands**:
 Redis 4.0 does not support multiple databases, which might have a negative impact on performance. We recommend using a dedicated database. The following commands are blocked and errors are generated during the execution:
     - MOVE
     - SELECT
     - SWAPDB
     
  Data persistence and backup are managed through the console, so the following commands are not supported:
  - BGREWRITEAOF
  - BGSAVE
  - LASTSAVE
     
  The replication and high availability of the system are centrally managed in the background of CRS. Related operation on it may affect the stability, so the following commands are not supported:
     - REPLCONF
     - SLAVEOF
     - SYNC / PSYNC

  The transactional commands are not supported, but will be available in the Redis version released in August, 2018:
      - MULTI
      - EXEC
      - DISCARD
      - UNWATCH

  Other unsupported commands:
     -   CONFIG
     -   DEBUG 
     -   PFDEBUG
     -   OBJECT
     -   SHUTDOWN
     -   CLIENT
     -   MONITOR
     -   COMMAND
     -   SCRIPT-DEBUG
     -   LATENCY
     -  READONLy
 	- TIME
 	- WAIT
 	- MODULE
 	- DBSIZE
 - **Commands with limited support**:
  To be compatible with the Jedis cluster scenarios, CRS modifies the IP list returned by the supported Cluster commands. The IP of each node in the returned information is the VIP of the instance.
     - CLUSTER NODES
     - CLUSTER SLOT 

  Cross-slot commands are not supported in the first phase, but will be available later. In case of unsupported commands, the system returns the following error:
  `(error) CROSSSLOT Keys in request don't hash to the same slot`

  Related commands are as follows:
     - DEL
     - UNLINK
     - EXISTS
     - MGET
     - BRPOP
     - BLPOP
     - SINTER
     - STNTERSTORE
     - SUNION
     - SDIFF
     - SDIFFSTORE
     - MSET
     - MSETNX
     - PFCOUNT
     - PFMERGE
      
 **Custom commands**
 Redis 4.0 provides a standalone version in the cluster mode through VIP encapsulation, which facilitates the business greatly but brings certain opacity to OPS. In this case, custom commands can help address this issue. Custom commands support the access to each node in the cluster by adding a parameter [Node ID], COMMAND arg1 arg2 ... [Node ID] to the right most of the original parameter list. The node ID is obtained through the "cluster nodes" command or via the console:
   ```
 	1.1.1.1:2000> cluster nodes
 	25b21f1836026bd49c52b2d10e09fbf8c6aa1fdc 10.0.0.15:6379@11896 slave 36034e645951464098f40d339386e9d51a9d7e77 0 1531471918205 1 connected
 	da6041781b5d7fe21404811d430cdffea2bf84de 10.0.0.15:6379@11170 master - 0 1531471916000 2 connected 10923-16383
 	36034e645951464098f40d339386e9d51a9d7e77 10.0.0.15:6379@11541 myself,master - 0 1531471915000 1 connected 0-5460
 	53f552fd8e43112ae68b10dada69d3af77c33649 10.0.0.15:6379@11681 slave da6041781b5d7fe21404811d430cdffea2bf84de 0 1531471917204 3 connected
 	18090a0e57cf359f9f8c8c516aa62a811c0f0f0a 10.0.0.15:6379@11428 slave ef3cf5e20e1a7cf5f9cc259ed488c82c4aa17171 0 1531471917000 2 connected
 	ef3cf5e20e1a7cf5f9cc259ed488c82c4aa17171 10.0.0.15:6379@11324 master - 0 1531471916204 0 connected 5461-10922

 	Native command:
 	info server
 	Custom command:
 	info server ef3cf5e20e1a7cf5f9cc259ed488c82c4aa17171
   ```
   
  List of custom commands:
 - INFO	 
 - MEMORY
 - SLOWLOG
 - KEYS (hashtag supported and preferred)
 - SCAN (hashtag supported and preferred)

 **Supported commands**
   Redis Community 4.0 supports all commands except the above.


