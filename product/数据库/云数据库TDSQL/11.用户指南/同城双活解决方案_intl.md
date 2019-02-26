Tencent Cloud MariaDB supports intra-city dual-active 2-DC capacity. The main features are as follows:
- Intra-city 2-DC deployment
- 2-DC writable: If your servers are deployed on different subnets of 2-DC, you can write data by connecting databases from each server of 2-DC.
- Automatic failover/recovering
- Unique access IP of 2-DC

However, intra-city dual-active 2-DC databases alone cannot achieve disaster recovery at the business system level. Actually, it is easy to switch a single system/module to a disaster recovery center in the same city. However, the complicated correlation among enterprise-level system businesses and their configurations are challenges for 2-DC.

Therefore, **to build a dual-active business system, businesses must be based on 2-DC in the design, use, management, and upgrade of the system at all times. Real-time use of 2-DC and interoperability of configuration are the basic elements**. In this way, businesses can be quickly resumed without modification or with minor modification in case of failures. This is also the goal of designing Tencent Cloud MariaDB intra-city dual-active 2-DC. It allows business systems of both centers to fully read and write database systems via the local network, ensuring strong database consistency.

## Design Standard
Tencent Cloud MariaDB dual-active feature is designed based on "GB/T 20988-2007 Information Security Technology - Disaster Recovery Specifications for Information System". For single database module:
- RTO ≤ 60s
- RPO ≤ 5s
- Failover time ≤ 5s
- Failure detection time ≤ 30s

It means that it takes about 40 seconds to complete the switch since the occurrence of failure (including failure detection time).

- Risk warning: To perform test in the real environment, ensure that the business system has an automatic database reconnection mechanism. However, the business system always has multiple modules, and each module may be related to multiple data sources. Therefore, the more complex the system, the longer the recovery time.


## Support
### Supported
Instance version:
- Standard: 1 master, 1 slave (two nodes)/1 master, 2 slaves (three nodes)
- Financially Customized : 1 master, 1 slave (two nodes)/1 master, 2 slaves (three nodes)

Network requirement: VPC only
Supported regions:
- Beijing (Beijing Zone 1, Beijing Zone 3)
- Shanghai Finance Zone (Finance Zone 1, Finance Zone 2)
- Shenzhen Finance Zone (Finance Zone 1, Finance Zone 2)

### Price
The same price is offered for dual availability zone and single availability zone. For more information, please see [Price](https://cloud.tencent.com/document/product/237/2034).

- Risk warning: The cost of Direct Connect for 2-DC data synchronization will be exempted before June 30, 2019. If the operating policy changes in the future, the price will not be higher than the price of intra-city Direct Connect published by Tencent Cloud. If you do not want to continue using the intra-city 2-DC solution, you can migrate the data to intra-city 1-DC for free.

### Purchase and Use
Go to [Cloud Database MariaDB purchase page](https://buy.cloud.tencent.com/tdsql), and click to purchase.
- When the master and slave availability zones are the same, a single availability zone is deployed.
- When the master and slave availability zones are different, an intra-city 2-DC is deployed.
![](https://main.qcloudimg.com/raw/fe800ff0f6a63b9e6bd64a0f27007f89.png)

>**Note:**
>- The master availability zone is the zone where your master server is located. The database should be assigned on the same VPC subnet of the master server to reduce access delay. Slave availability zone is the zone where the slave nodes of the database are located. For 1 master and 2 slaves (3 nodes), 2 nodes are deployed in the master availability zone. For 1 master and 1 slave (2 nodes), 1 node is deployed in the master availability zone.
- If intra-city 2-DC policy is required for the finance cloud cage solution, an intra-city 2-DC cage solution needs to be built first. For more information, please contact your business manager and architect.


### Initializing Instance
Initialize your instance by referring to [Instance Initialization](https://cloud.tencent.com/document/product/237/7055).


### Viewing Details of the Availability Zone of Instance
You can view it on the instance details page.
![](https://main.qcloudimg.com/raw/53e48b1dcdeee28d97d790b94f56d0dc.png)

### Master/Slave Switch
To switch the master node from one available zone to another, you can simply click master/slave switch. Since this operation is high risky, the IP address of the login account must be verified. The switch process may cause flash disconnection of database (≤1s). Please ensure that the business has a database reconnection mechanism. Frequent switch may result in service system exception or even data exception.
![](https://main.qcloudimg.com/raw/82e6ef75b950949b3a1fb36f44cfd4b1.png)

## Technical Principle
By integrating highly available master-slave architecture of MariaDB with virtual IP drifting of VPC availability zone, simultaneous read and write of 2-DC is achieved. Here are the architecture features:
- Proxy modules are deployed in a mixed way at the frontend of each DB node for MariaDB. Proxy module is responsible for routing data requests to corresponding DB nodes.
- Deploy cross-region VPC gateway before the Proxy module is deployed, and virtual IP drifting is supported.
![](https://main.qcloudimg.com/raw/a714b045d40ad44223f03e5d5fede0fd.png)

As shown above, taking data write as an example. If the business server is deployed in the availability zone A, PC gateway forwards the data request to the Proxy gateway in the availability zone A, and then Proxy transparently forwards it to the Master node. If the business server is deployed in the availability zone B, the VPC gateway forwards the data request to Proxy gateway in the availability zone B, and then Proxy transparently forwards it to the Master node via the Tencent Cloud BGP private network.
Whether it is a read or write request, the entire process is transparent to the business. In case of database exception, the database cluster is processed as follows:
1. If both Master and Proxy fail, the cluster automatically selects the optimal Slave as the new Master. The system notifies VPC to modify the association between the virtual IP and the physical IP. The business only perceives that part of the requests are disconnected.
2. If Master fails but Proxy is normal, the cluster automatically selects the optimal Slave as the new Master. Proxy will block requests until the master/slave switch is completed. In this case, the business only perceives that part of the requests have timed out.
3. If Slave fails (regardless of whether Proxy fails or not), when read-write separation is enabled, the operation is performed according to **read-only policy** (3 types) of pre-configured read-only account.
4. If the availability zone A completely fails, while VPC and the database are still alive in the available zone B, the Slave 2 node is automatically selected as Master. **The read/write policy of the node is adjusted according to the strongsync policy**, and VPC network IP drifts to the availability zone B. In this case, the cluster tries to recover the node in the availability zone A. If the node cannot be recovered within 30 minutes, at least 1 Slave node is automatically rebuilt on the node B. Due to the IP drifting policy, no database configuration modification is required for the business.
5. If the data center B completely fails, it is equivalent to the failed Slave node of MariaDB cluster. The processing method is the same as that in Step 3.

## FAQ
#### 1. Compared to intra-city 1-DC, will the intra-city 2-DC cause a decrease in performance?
Considering the strongsync replication solution, since the cross-center delay is slightly greater than that of the device in the same data center, the speed of SQL response will drop by about 5% in theory.

#### 2. Is it possible for a Master node to switch from the master availability zone to the slave availability zone?
Yes, neglect it if it does not affect the use of your business. If you are concerned about the impact, you can switch back by using the master/slave switch feature on the console when business volume is low.

#### 3. How do I know that master/slave switch is applied to the database cluster?
Log in to the console, and go to **Cloud Monitoring** -> **Alarm Policy** -> **Cloud Database MariaDB** to configure an alarm on master/slave switch.

#### 4. If part of the read/write requests are read from/written to the slave availability zone, the network delay will cause a decrease in performance, but I really want to reserve the intra-city 2-DC feature. What should I do?
You can submit a ticket indicating the instance ID, deployment solution of your server in the availability zone, and the ratio of read and write requests. Tencent Cloud DBA can help you adjust the loading mechanism of dual availability zone to minimize the number of read and write requests in the availability zone.

#### 5. If I want to change from 1-DC to intra-city 2-DC architecture, what should I do?
First, confirm whether intra-city 2-DC solution is supported in your region. It is now available in three regions including Beijing, Shanghai Finance Zone, and Shenzhen Finance Zone. Second, submit a ticket indicating the information of the account to be adjusted, the instance ID, two availability zones, and recommended OPS time. Finally, Tencent Cloud service personnel will conduct an audit. If you pass the audit (dual availability zone is supported), you can change solution as needed, otherwise your request will be rejected.

