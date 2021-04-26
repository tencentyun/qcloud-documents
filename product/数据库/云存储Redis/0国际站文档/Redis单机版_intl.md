### About Redis Standalone
 Redis Standalone is a scenario-specific version using a single database node deployment architecture. It is compatible with protocols and commands in Redis 2.8, and will be compatible with Redis 4.0 soon. Unlike Redis Master/Slave, Redis Standalone only contains one node and one copy of data, and **does not provide data persistence and backup**. It is suitable for caching-only business scenarios that do not require high data reliability.<br><br>
 ![](https://main.qcloudimg.com/raw/dba336b5ffa8b277bc2c36f3a8cd030d.svg)

 ### Features of Redis Standalone

  - **Low cost**
  The Redis Standard single-replica architecture uses single node deployment. The HA system regularly detects the health condition of the node, and will start another Redis process to continue the Redis service within 30 seconds upon detecting that the service is unavailable. This ensures high service availability comparable to the dual-replica version. In addition, you can save great cost by only deploying one database node. The price is about half that of the dual-replica high-availability version.
  - **High performance**
 Since the slave database in the standard dual-replica architecture is only used for failover and does not provide services, and database replication also consumes performance of the master database, the performance of the single-replica version will be no lower than and even higher than that of the dual-replica high availability version.

 ### Scenarios


  - **Caching-only scenarios** 
 The single-replica version has only one database node, and when the node fails, the system will start another Redis process (**there is no data**). When the auto failover is completed for the failed node, the application needs to preheat the data again to prevent the access pressure on the backend databases.
 >Note: Since single-replica version cannot ensure data reliability and the service needs to be preheated after a node failure, it is recommended to use the dual-replica high-availability version instead of the single-replica version for sensitive services that require high reliability of data.

  - **Early business stages** 
 You can use the Standalone version at the business development and testing stages when you do not require high data reliability and hope to lower the cost. You can use the Master/Slave version instead when the business is officially launched.

 ### Use limits

  1. Redis Standalone does not support high reliability of data. When the Redis node fails, the system will provide another service node within 1 minute. The original data cannot be recovered and the business needs to preheat the data again.
  2. Redis Standalone does not provide data backup and data recovery features. If these two features are required, select Redis Master/Slave.
