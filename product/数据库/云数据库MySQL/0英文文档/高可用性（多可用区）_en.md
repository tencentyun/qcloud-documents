Tencent Cloud CDB provides high availability and failover support for database instances using multi-availability zone deployments. A multi-availability zone is a physical zone consisting of multiple single availability zones within the same region. Multi-availability zone deployments help protect your database against database instance failure and availability zone disruption. For more information on availability zones, please see [Regions and Availability Zones](https://cloud.tencent.com/document/product/236/8458).
>**Note:**
- Whether the instances in a database cluster are running across multiple availability zones or not, each CDB for MySQL has a slave for real-time hot backup to ensure high availability for the database.
- In a multi-availability zone deployment, CDB for MySQL automatically presets and maintains a sync standby replica in a different availability zone.
- The master database instance is synchronously replicated across availability zones to a standby replica to provide data redundancy, eliminate I/O freezes, and minimize latency spikes during system backups.

### Supported Regions
Tencent Cloud CDB multi-availability zone deployments are only supported in Shenzhen Finance Zone.
### Multi-availability Zone Deployments
1. Log in to [Tencent Cloud Console][1], click "Relational Database" in the navigation bar to enter [Cloud Database Console][2], and then click the "New" button.
2. On the cloud database purchase page, select "Yes" on the "Multi-availability Zone Deployments" option.

### Failover
CDB for MySQL handles failovers automatically so you can resume database operations as quickly as possible without administrative intervention. The master database instance switches over automatically to the standby replica if any of the following conditions occur: 
- Availability zone outage
- Master database instance failure

[1]:	https://console.cloud.tencent.com/
[2]:	https://console.cloud.tencent.com/cdb/

