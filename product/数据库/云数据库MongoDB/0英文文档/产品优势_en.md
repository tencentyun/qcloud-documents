Tencent Cloud Database MongoDB provides the capabilities of NoSQL Database as a service, making it easier to be deployed, managed, and expanded compared with self-built MongoDB databases;
At the same time, it has the same feature with the public cloud in terms of "Request on Demand and Pay by Usage" which improves cost efficiency as is shown in the following table:

| Dimension | Cloud Database MongoDB | Self-built MongoDB |
|:--|:--|:--|
| Cost | No need to invest in hardware and software and multiple options are available (high IO, large capacity); pay on demand | Hardware: a single storage server is costly (if a highly available master-slave instance (replica set) is required, you need to buy 2 units, causing resource redundancy)<br> Software: you need to recruit professional DBA personnel which means high labor costs |
| Service availability | 99.95%, high industry standard, professional team on a 7/24 basis, one-to-one instruction, QQ remote assistance | Deal with failures, build master/slave and RAID by yourself |
| Data reliability | 99.9996%, perfect auto data backup and non-destructive recovery mechanism, real-time hot backup, recover data to any time within 5 days (Note: If the data operated between the two backups exceeds the oplog size, you cannot roll it back to the time between the two backups) | Self-protection, reliability depends on hardware failure rate and on the database management skills of technical personnel |
| System security | Anti-DDoS attacks; repair various database and host security vulnerabilities in time | Self-deployed with high costs; you need to repair database security vulnerabilities on your own |
| Real-time monitoring | Multi-dimensional monitoring, failure warning for ease of use | Need to develop your own monitoring system, and require the operation and maintenance personnel to repair failures over night |
| Business expansion | One-click expansion on demand, fast deployment, early on-line for ease of use | Need to procure hardwares, host data center, redeploy application and complete other work on your own with longer cycle |
| Resource utilization | Request on demand and 100% resource utilization to save your budget | Peak period will cause low average load and low resource utilization rate |

Tencent cloud CDB for MongoDB have implanted special optimizations to resolve issues which often occur during the operations of traditional self-built MongoDB, including performance bottleneck, operation and maintenance difficulties, data reliability and availability problems:
1) Performance bottleneck breakthrough: adopt brand-new PCI-E SSD storage media and new generation storage engine; provide customizable performance enhancing features to help users enhance the performance of specified components.
2) Solve operational and maintenance difficulties: automatic monitor alarm for over 20 monitoring metrics; provide bulk data import and export feature, templated parameter modification to make business deployment easy and fast.
3) Highly available service: master-slave or even more hot backups, automatic disaster recovery, failover transparent to users; support the same "read slave first" feature as the native MongoDB to ensure high concurrent read capability.
4) Highly reliable data: combined with cold backup and oplog to provide data rollback capability which is able to restore data to at any time point within 5 days, supports data dump of cold backup data within 5 days. Also supports private network firewall and public network DDoS protection.







