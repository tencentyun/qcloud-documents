### Overview
Multi-Thread Asynchronous Replication (MAR) is a self-developed MySQL-based multi-thread strongsync replication program by Tencent. Only when the slave data is completely synchronized (with log) can master respond to the application transaction, to prevent data loss and errors.
As the core of system data storage and service, the database should be highly available. In production systems, high availability solutions are often required to ensure uninterrupted system operation, with data synchronization technology as the foundation of a highly available database solution. MAR strongsync technology can well meet the requirements of database availability.

### Traditional Data Replication Methods
For now, there are three methods to replicate data:
- Async replication: An application initiates an update request. After completing the operation, the Master responds to the application immediately to replicate the data to a Slave asynchronously.
- Strongsyn replication: An application initiates an update request. After completing the operation, the Master replicates the data to a Slave immediately. After receiving the data, the Slave returns success message to the Master. Only after receiving the message from the Slave the Master can return a response to the application. The data is replicated synchronously from the Master to the Slave.
- Semisync replication: Generally, strongsync replication is employed. Only when an exception occurs with the data replication from the Master to the Slave (a Slave node becomes unavailable or an exception occurs with the network of the two nodes), the replication will be downgraded to async replication. When the replication returns to a normal state, strongsync replication will be restored from async replication.

When the Master or Slave is not available, there is a chance of data inconsistency for the above three methods.

### MAR Strongsync Replication Program
MAR strongsync replication program can prevent data loss and errors. Here is the technical diagram:
![](https://mc.qcloudimg.com/static/img/d8a36cbf57eff5c0de84e46d2591970f/image.png)
Features:
  1\. Consistent sync replication ensures strong consistency of data between nodes.
	2\. Complete transparency to the service. Read and write separation or sync enhancement is not required for the service.
	3\. Asynchronization of serial sync threads and introduction of thread pool result in a substantial increase in performance.
	4\. Cluster architecture is supported.
	5\. Automatic member control is supported and faulty nodes are automatically removed from the cluster.
	6\. Automatic node join is supported without human intervention.
	7\. Each node contains a complete replica of the data and you can switch at any time.
	8\. Shared storage devices are not required.
MAR strongsync program is superior to other mainstream sync programs in performance. For more information, refer to [Strongsync Performance Comparison Data](https://cloud.tencent.com/document/product/557/10105).
