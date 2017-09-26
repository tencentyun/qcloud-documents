Tencent Cloud CDB allows for multi-availability zone deployments to provide database instances with support for high availability and failover.
	Note
	Whether the instances in a database cluster are running across multiple availability zones or not, each CDB MySQL has a slave for real-time hot backup to ensure high availability for the database.
In multi-availability zone deployments, the CDB MySQL automatically presets and maintains a sync backup copy in different availability zones. A primary database instance is synchronously replicated to the backup copy across availability zones to provide data redundancy, eliminate I/O freezing, and minimize latency peak during system backup. Multi-availability zone deployments help in securing the database, so as to protect database instances from failure and the availability zones from outage. For more information on availability zones, refer to Regions and Availability Zones.

### Multi-Availability Zone Deployments Using CDB MySQL
1) Log in to [Tencent Cloud Console][1], click "Relational database" in the navigation bar to enter [Cloud Database Console][2], and click "New" button.
2) On the Cloud Database purchase page, select "Yes" on "Multi-availability zone deployments" option.

### Regions Where Multi-Availability Zone Deployments Are Supported
Currently, multi-availability zone deployments are only supported in Shenzhen Finance Zone.

### Failover of MySQL CDB
CDB MySQL can automatically handle failover, so you can recover database operations as soon as possible without any administrator intervention. If any of the following conditions occurs, the primary database instance will automatically switch to the backup copy:
* Availability zone outage
* Primary database instance failure
* Size of the database instance server is changed
* Operating system of the database instance is patching software  


[1]:	https://console.qcloud.com/
[2]:	https://console.qcloud.com/cdb/ "Cloud Database Console"
