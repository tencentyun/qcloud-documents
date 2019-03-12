Tencent Cloud MongoDB implements a master-slave hot backup structure. When the master node fails, the service will be automatically switched to slave node, without causing interruption in service.
The procedure for automatic disaster recovery is as follows:
1. When the master node is exceptionally inaccessible, a new one will be automatically elected within the cluster.
2. If the master node fails, it will become a slave node after a successful recovery. Otherwise, a new node will be supplemented into the cluster to meet the user-selected cluster scale.
3. Likewise, if any one slave node is inaccessible, the system will try to recover it or supplement it with a new node.
![](https://mc.qcloudimg.com/static/img/5cdada2069c890c3ba44486641413d20/zidongrongzai.png)
