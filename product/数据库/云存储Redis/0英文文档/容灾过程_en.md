Automatic disaster recovery procedure description

#### Steps
Tencent Cloud Redis implements master-slave hot backup structure. When the master node fails, the service will automatically switch to slave node, without causing service interruption
1. Master node fails, link requests of the interface message processor encounter errors, host failure is detected by the heartbeat mechanism
2. Routing system delivers changes
3. Interface message processor switch requests to the slave machine and completes failover operation
![](https://mc.qcloudimg.com/static/img/7afe117629d4814302377cf46b64d8ee/zidongrognzai.png)
