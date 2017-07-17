Procedure for Automatic Disaster Recovery on Cloud Memcached
1. The data of each Cloud Memcached's instance is stored on multiple sets of machines with each using the master/slave hot backup architecture. If a node fails, the faulty node will be replaced with a new one.
2. When a master node fails, the access machine will send the read/write requests to the original slave node. At the same time, a new slave node is added to copy data from the new master machine, to complete the data synchronization between master and slave.
3. When a slave node fails, a new slave node is added directly.
4. Any nodes can be replaced by the system automatically, and manual operation is also supported.
![](https://mc.qcloudimg.com/static/img/da620dfc691b0150fc92148f25c530b3/mem_HA.png)
