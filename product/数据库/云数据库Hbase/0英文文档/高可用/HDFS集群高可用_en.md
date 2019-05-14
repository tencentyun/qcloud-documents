Storage layer HDFS high availability HA. HA means High Availability, which is used to solve the single-point failure of NameNode.

This feature provides a backup for the master NameNode through hot backup method. Once the master NameNode fails, it can be quickly switched to the slave NameNode, thereby achieving the uninterrupted services. In this solution, the namenode of HA is usually composed of two NameNodes, one is in active state, and the other is in standby state. The active NameNode provides services externally, such as handling the RPC requests from clients, while Standby NameNode does not provide services externally, and it only synchronizes the state of active namenode, so that it can be quickly switched when the master fails.


The metadata information is synchronized through a group of JournalNodes between the master NameNode and the slave NameNode. As long as a data is successfully written into the majority of JournalNodes, it is considered to be successfully written. We usually configure (2N+1) JournalNodes, so that as long as N+1 nodes are successfully written, the data is considered to be successfully written. At this time, a maximum of N-1 failed JournalNodes are tolerable, for example, if there are three JournalNodes, at most one JournalNode is allowed to fail, and if there are five JournalNodes, at most two JounralNodes are allowed to fail.

![](https://mc.qcloudimg.com/static/img/2d6e738edcabe791089188918c254ab9/HDFS_HA.png)
