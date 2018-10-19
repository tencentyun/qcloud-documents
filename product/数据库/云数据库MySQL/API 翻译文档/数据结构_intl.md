## Account

The information of the database account

Referenced by the following APIs: CreateAccounts, DeleteAccounts, ModifyAccountDescription, ModifyAccountPassword, and ModifyAccountPrivileges.

| Name | Type | Required | Description |
|------|------|----------|------|
| User | String | Yes | New name of the account |
| Host | String | Yes | New domain name of the account |

## AccountInfo

Account details

Referenced by the following API: DescribeAccounts.

| Name | Type | Description |
|------|------|-------|
| Notes | String | Remarks of the account |
| Host | String | Domain name of the account |
| User | String | Account name |
| ModifyTime | Timestamp | Time when the account information is modified |
| ModifyPasswordTime | Timestamp | Time when the password is modified |
| CreateTime | Timestamp | Creation time of the account |

## BackupConfig

The configuration information of the second slave database of ECDB. This field is only applicable to ECDB instances.

Referenced by the following API: DescribeDBInstanceConfig.

| Name | Type | Description |
|------|------|-------|
| ReplicationMode | String | Indicates how to copy the second slave database. Possible return values: async and semisync |
| Zone | String | Formal name of the availability zone of the second slave database, such as ap-shanghai-1 |
| Vip | String | Private IP of the second slave database |
| Vport | String | Access port of the second slave database |

## BackupInfo

Details of backup

Referenced by the following API: DescribeBackups.

| Name | Type | Description |
|------|------|-------|
| Name | String | Name of the backup file |
| Size | Integer | Size of the backup file (in bytes) |
| Date | String | Backup time of the snapshot, such as 2016-03-17 02:10:37 |
| IntranetUrl | String | Download URL in private network |
| InternetUrl | String | Download URL in public network |
| Type | String | Specific log type. Available values: logic - Logical cold backup; physical - Physical cold backup |
| BackupId | Integer | ID of the backup subtask, which is used when the backup file is deleted |
| Status | String | Status of the backup task |
| FinishTime | String | The completion time of the backup task |
| Creator | String | The creator of the backup. Available values: SYSTEM - Created by the system; Uin - Initiator's Uin value |

## BinlogInfo

Binary log information

Referenced by the following API: DescribeBinlogs.

| Name | Type | Description |
|------|------|-------|
| Name | String | Name of the backup file |
| Size | Integer | Size of the backup file (in bytes) |
| Date | Timestamp | Backup time of the snapshot, such as 2016-03-17 02:10:37 |
| IntranetUrl | String | Download URL in private network |
| InternetUrl | String | Download URL in public network |
| Type | String | Specific log type. Available values: binlog - Binary log |

## ColumnPrivilege

Column permission information

Referenced by the following API: DescribeAccountPrivileges, and ModifyAccountPrivileges.

| Name | Type | Required | Description |
|------|------|----------|------|
| Database | String | Yes | Name of the database |
| Table | String | Yes | Name of the database table |
| Column | String | Yes | Name of the database column |
| Privileges | Array of String | Yes | Permission information |

## DBSwitchInfo

Records of database switch

Referenced by the following API: DescribeDBSwitchRecords.

| Name | Type | Description |
|------|------|-------|
| SwitchTime | Timestamp | Switch time, such as 2017-09-03 01:34:31 |
| SwitchType | String | Switch type. Possible return values: TRANSFER - Data migration; MASTER2SLAVE - Master/Slave switch; RECOVERY - Master/Slave recovery |

## DatabaseName

Database table name

Referenced by the following API: DescribeBackupDatabases.

| Name | Type | Description |
|------|------|-------|
| DatabaseName | String | Name of the database table |

## DatabasePrivilege

Permissions of the database

Referenced by the following API: DescribeAccountPrivileges, and ModifyAccountPrivileges.

| Name | Type | Required | Description |
|------|------|----------|------|
| Privileges | Array of String | Yes | Permission information |
| Database | String | Yes | Name of the database |

## DrInfo

Information on disaster recovery instance

Referenced by the following API: DescribeDBInstances.

| Name | Type | Description |
|------|------|-------|
| Status | Integer | Status of the disaster recovery instance |
| Zone | String | Information on the availability zone |
| InstanceId | String | Instance ID |
| Region | String | Region information |
| SyncStatus | Integer | Synchronization status of the instance |
| InstanceName | String | Instance name |
| InstanceType | Integer | Instance type |

## First

Information on the first slave instance

Referenced by the following API: DescribeDBInstances.

| Name | Type | Description |
|------|------|-------|
| Vport | Integer | Port number |
| Region | String | Region information |
| Vip | String | Virtual IP information |
| Zone | String | Information on the availability zone |

## ImportRecord

Record of import task

Referenced by the following API: DescribeDBImportRecords.

| Name | Type | Description |
|------|------|-------|
| Status | Integer | Status value |
| Code | Integer | Status value |
| CostTime | Integer | Execution time |
| InstanceId | String | Instance ID |
| WorkId | String | Backend task ID |
| FileName | String | Name of the imported file |
| Process | Integer | Execution progress |
| CreateTime | Timestamp | Creation time of the task |
| FileSize | String | File size |
| Message | String | Task execution information |
| JobId | Integer | Task ID |
| DbName | String | Name of the imported database table |
| AsyncRequestId | String | ID of async task request |

## Inbound

Inbound rules of security group

Referenced by the following API: DescribeDBSecurityGroups, and DescribeProjectSecurityGroups.

| Name | Type | Description |
|------|------|-------|
| Action | String | Policy, ACCEPT or DROP |
| CidrIp | String | Source IP or IP address range, such as 192.168.0.0/16 |
| PortRange | String | Port |
| IpProtocol | String | Network protocol, such as UDP and TCP |
| Dir | String | Direction limited on the rules, which is INPUT for inbound rules |

## InstanceInfo

Instance details

Referenced by the following API: DescribeDBInstances.

| Name | Type | Description |
|------|------|-------|
| WanStatus | Integer | Status of public network |
| Zone | String | Information on the availability zone |
| InitFlag | Integer | Initialization flag |
| RoVipInfo | [RoVipInfo](#RoVipInfo) | Read-only VIP information |
| Memory | Integer | Memory capacity |
| Status | Integer | Instance status |
| VpcId | Integer | VPC ID |
| SlaveInfo | [SlaveInfo](#SlaveInfo) | Information on the slave instance |
| InstanceId | String | Instance ID |
| Volume | Integer | Disk capacity |
| AutoRenew | Integer | Auto renewal flag |
| ProtectMode | Integer | Database replication mode |
| RoGroups | Array of [RoGroup](#RoGroup) | RO group information |
| SubnetId | Integer | Subnet ID |
| InstanceType | Integer | Instance type |
| ProjectId | Integer | Project ID |
| Region | String | Region information |
| DeadlineTime | Timestamp | Expiration time |
| DeployMode | Integer | Indicates how to deploy an availability zone |
| TaskStatus | Integer | Instance task status |
| MasterInfo | [MasterInfo](#MasterInfo) | Information on the master instance |
| DeviceType | String | Supported instance model |
| EngineVersion | String | Kernel version |
| InstanceName | String | Instance name |
| DrInfo | Array of [DrInfo](#DrInfo) | Information on the disaster recovery instance |
| WanDomain | String | Public network domain name |
| WanPort | Integer | Public network port |
| PayType | Integer | Billing method |
| CreateTime | String | Creation time |
| Vip | String | Instance IP |
| Vport | Integer | Port number |
| CdbError | Integer | Instance status |
| UniqVpcId | String | VPC descriptor |
| UniqSubnetId | String | Subnet descriptor |

## InstanceRebootTime

Restart time of instance

Referenced by the following API: DescribeDBInstanceRebootTime.

| Name | Type | Description |
|------|------|-------|
| InstanceId | String | Instance ID, such as cdb-c1nl9rpv. It is identical to the instance ID displayed in the database console page |
| TimeInSeconds | Integer | Indicates how long it takes for the instance to restart |

## InstanceRollbackRangeTime

Time range available for the rollback of instance

Referenced by the following API: DescribeRollbackRangeTime.

| Name | Type | Description |
|------|------|-------|
| Code | Integer | Queries database error code |
| Message | String | Queries database error message |
| InstanceId | String | Instance ID list. ID of an instance should look like this: cdb-c1nl9rpv. It is identical to the instance ID displayed in the database console page |
| Times | Array of [RollbackTimeRange](#RollbackTimeRange) | Time range available for rollback |

## MasterInfo

Information on master instance

Referenced by the following API: DescribeDBInstances.

| Name | Type | Description |
|------|------|-------|
| Region | String | Region information |
| RegionId | Integer | Region ID |
| ZoneId | Integer | Availability zone ID |
| Zone | String | Information on the availability zone |
| InstanceId | String | Instance ID |
| ResourceId | String | Instance resource ID |
| Status | Integer | Instance status |
| InstanceName | String | Instance name |
| InstanceType | Integer | Instance type |
| TaskStatus | Integer | Task status |
| Memory | Integer | Memory capacity |
| Volume | Integer | Disk capacity |
| DeviceType | String | Instance model |
| Qps | Integer | Queries per second |
| VpcId | Integer | VPC ID |
| SubnetId | Integer | Subnet ID |
| ExClusterId | String | Exclusive cluster ID |
| ExClusterName | String | Exclusive cluster name |

## Outbound

Outbound rules of security group

Referenced by the following API: DescribeDBSecurityGroups, and DescribeProjectSecurityGroups.

| Name | Type | Description |
|------|------|-------|
| Action | String | Policy, ACCEPT or DROP |
| CidrIp | String | Destination IP or IP address range, such as 172.16.0.0/12 |
| PortRange | String | Port or port range |
| IpProtocol | String | Network protocol, such as UDP and TCP |
| Dir | String | Direction limited on the rules, which is OUTPUT for outbound rules |

## ParamInfo

Instance parameter information

Referenced by the following API: CreateDBInstance, CreateDBInstanceHour, and InitDBInstances.

| Name | Type | Required | Description |
|------|------|----------|------|
| Name | String | Yes | Parameter name |
| Value | String | Yes | Parameter value |

## Parameter

Database instance parameter

Referenced by the following API: ModifyInstanceParam.

| Name | Type | Required | Description |
|------|------|----------|------|
| Name | String | Yes | Parameter name |
| CurrentValue | String | Yes | Parameter value |

## RegionSellConf

Supported configuration of region

Referenced by the following API: DescribeDBZoneConfig.

| Name | Type | Description |
|------|------|-------|
| RegionName | String | Region name |
| Area | String | Area |
| IsDefaultRegion | Integer | Indicates whether it is the default region |
| Region | String | Region |
| ZonesConf | Array of [ZoneSellConf](#ZoneSellConf) | Supported configuration of availability zone |

## RoGroup

RO group parameter

Referenced by the following API: CreateDBInstance, CreateDBInstanceHour, and DescribeDBInstances.

| Name | Type | Required | Description |
|------|------|----------|------|
| RoGroupMode | String | Yes | RO group mode. Available values: alone - RO group is automatically assigned by the system; allinone - Create a RO group; join - Use an existing RO group |
| RoGroupId | String | No | RO group ID |
| RoGroupName | String | No | RO group name |
| RoOfflineDelay | Integer | No | Indicates whether to enable "Elimination of instance with a delay exceeding limit". If it is enabled, a RO instance is isolated if delay between the RO instance and the master instance exceeds the threshold. Available values: 1 - Enable; 0 - Disable |
| RoMaxDelayTime | Integer | No | Delay threshold |
| MinRoInGroup | Integer | No | Minimum retained instances. When the number of purchased RO instances is below the set number, no instance is eliminated. |
| WeightMode | String | No | Read-write weight assignment mode. Available values: system - Automatically assigned by the system; custom - Custom |
| Weight | Integer | No | Weight value |
| RoInstances | Array of [RoInstanceInfo](#RoInstanceInfo) | No | Details of RO instances in the RO group |
| Vip | String | No | Private IP in the RO group |
| Vport | Integer | No | Private network port in the RO group |

## RoInstanceInfo

Details of RO instance

Referenced by the following API: CreateDBInstance, CreateDBInstanceHour, and DescribeDBInstances.

| Name | Type | Description |
|------|------|-------|
| MasterInstanceId | String | ID of the master instance corresponding to the RO group |
| RoStatus | String | Status of the RO instance in the RO group. Available values: online - Online; offline - Offline |
| OfflineTime | String | Time when the RO instance last went offline in the RO group |
| Weight | Integer | The weight of the RO instance in the RO group |
| Region | String | Name of the region in which the RO instance resides, such as ap-shanghai |
| Zone | String | The formal name of the RO availability zone, such as ap-shanghai-1 |
| InstanceId | String | RO instance ID, such as cdbro-c1nl9rpv |
| Status | Integer | RO instance status. Possible return values: 0 - Creating; 1 - Running; 4 - Deleting |
| InstanceType | Integer | Instance type. Possible return values: 1 - Master instance; 2 - Disaster recovery instance; 3 - RO instance |
| InstanceName | String | RO instance name |
| HourFeeStatus | Integer | Postpaid billing status. Possible values: 1 - Normal; 2 - In arrears |
| TaskStatus | Integer | RO instance task status. Possible return values:<br>0 - No task<br>1 - Upgrading<br>2 - Importing data<br>3 - Opening slave<br>4 - Enabling access over public network<br>5 - Performing batch operation<br>6 - Rolling back<br>7 - Disabling access over public network<br>8 - Modifying password<br>9 - Modifying instance name<br>10 - Restarting<br>12 - Under self-built migration<br>13 - Deleting database table<br>14 - Creating disaster recovery instance synchronization |
| Memory | Integer | RO instance memory size (in MB) |
| Volume | Integer | RO instance memory disk size (in GB) |
| Qps | Integer | Queries per second |
| Vip | String | Private IP of the RO instance |
| Vport | Integer | Access port of the RO instance |
| VpcId | Integer | ID of the VPC in which the RO instance resides |
| SubnetId | Integer | ID of the VPC subnet in which the RO instance resides |
| DeviceType | String | RO instance specification description. Available value: CUSTOM |
| EngineVersion | String | Version of RO instance database engine. Possible return values: 5.1, 5.5, 5.6 and 5.7 |
| DeadlineTime | String | Expiration time of the RO instance. Format: yyyy-mm-dd hh:mm:ss. If the instance is billed on a postpaid basis, the field value is 0000-00-00 00:00:00. |
| PayType | Integer | Billing method of RO instance. Possible return values: 0 - Prepaid; 1 - Postpaid; 2 - Monthly postpaid |

## RoVipInfo

Read-only VIP information

Referenced by the following API: DescribeDBInstances.

| Name | Type | Description |
|------|------|-------|
| RoVipStatus | Integer | Status of the read-only VIP |
| RoSubnetId | Integer | Subnet of the read-only VIP |
| RoVpcId | Integer | VPC of the read-only VIP |
| RoVport | Integer | Port of the read-only VIP |
| RoVip | String | Read-only VIP |

## RollbackDBName

Name of the database for rollback

Referenced by the following API: StartBatchRollback.

| Name | Type | Required | Description |
|------|------|----------|------|
| DatabaseName | String | Yes | Name of the original database before rollback |
| NewDatabaseName | String | Yes | Name of the new database after rollback |

## RollbackInstancesInfo

Details of the instance for rollback

Referenced by the following API: StartBatchRollback.

| Name | Type | Required | Description |
|------|------|----------|------|
| InstanceId | String | Yes | Database instance ID |
| Strategy | String | Yes | Rollback policy. Available values: table, db, and full. Default is full. Table - Swift mode. Only import backups and binlogs at the dimension of selected table. If there is join operation and the corresponding table is not selected, callback will fail; db - Quick mode. Only import backups and binlogs at the dimension of selected database. If there is join operation and the corresponding table is not selected, callback will fail; full - Normal mode. Import the backups and binlogs of the entire instance, which may take a long time. |
| RollbackTime | String | Yes | Database rollback time. Format: yyyy-mm-dd hh:mm:ss |
| Databases | Array of [RollbackDBName](#RollbackDBName) | No | Information of the database to be rolled back, which indicates rollback of the entire database |
| Tables | Array of [RollbackTables](#RollbackTables) | No | Information of the database table to be rolled back, which indicates rollback by table |

## RollbackTableName

Name of the database table for rollback

Referenced by the following API: StartBatchRollback.

| Name | Type | Required | Description |
|------|------|----------|------|
| TableName | String | Yes | Name of the original database table before rollback |
| NewTableName | String | Yes | Name of the new database table after rollback |

## RollbackTables

Details of the database table for rollback

Referenced by the following API: StartBatchRollback.

| Name | Type | Required | Description |
|------|------|----------|------|
| Database | String | Yes | Name of the database |
| Table | Array of [RollbackTableName](#RollbackTableName) | Yes | Details of the database table |

## RollbackTimeRange

Time range available for rollback

Referenced by the following API: DescribeRollbackRangeTime.

| Name | Type | Description |
|------|------|-------|
| Begin | String | Start time of instance rollback, such as 2016-10-29 01:06:04 |
| End | String | End time of instance rollback, such as 2016-11-02 11:44:47 |

## SecurityGroup

Details of security group

Referenced by the following API: DescribeDBSecurityGroups, and DescribeProjectSecurityGroups.

| Name | Type | Description |
|------|------|-------|
| ProjectId | Integer | Project ID |
| CreateTime | String | Creation time. Format: yyyy-mm-dd hh:mm:ss |
| Inbound | Array of [Inbound](#Inbound) | Inbound rules |
| Outbound | Array of [Outbound](#Outbound) | Outbound rules |
| SecurityGroupId | String | Security group ID |
| SecurityGroupName | String | Security group name |
| SecurityGroupRemark | String | Remarks for the security group |

## SellConfig

Details of supported configuration

Referenced by the following API: DescribeDBZoneConfig.

| Name | Type | Description |
|------|------|-------|
| Device | String | Device type |
| Type | String | Description of supported specifications |
| CdbType | String | Instance type |
| Memory | Integer | Memory size (in MB) |
| Cpu | Integer | Number of CPU cores |
| VolumeMin | Integer | Minimum disk size (in GB) |
| VolumeMax | Integer | Maximum disk size (in GB) |
| VolumeStep | Integer | Disk increment (in GB) |
| Connection | Integer | Number of connections |
| Qps | Integer | Queries per second |
| Iops | Integer | Input/output operations per second |
| Info | String | Description of application scenarios |
| Status | Integer | Status value |

## SellType

Type of supported instance

Referenced by the following API: DescribeDBZoneConfig.

| Name | Type | Description |
|------|------|-------|
| TypeName | String | Name of supported instance |
| EngineVersion | Array of String | Kernel version number |
| Configs | Array of [SellConfig](#SellConfig) | Detailed configuration of supported specifications |

## SlaveConfig

The configuration information of slave database

Referenced by the following API: DescribeDBInstanceConfig.

| Name | Type | Description |
|------|------|-------|
| ReplicationMode | String | Indicates how to copy the slave database. Possible return values: async and semisync |
| Zone | String | Formal name of the availability zone of the slave database, such as ap-shanghai-1 |

## SlaveInfo

Information on slave instance

Referenced by the following API: DescribeDBInstances.

| Name | Type | Description |
|------|------|-------|
| First | [First](#First) | Information on the first slave instance |
| Second | [First](#First) | Information on the second slave instance |

## SlowLogInfo

Details of slow logs

Referenced by the following API: DescribeSlowLogs.

| Name | Type | Description |
|------|------|-------|
| Name | String | Name of the backup file |
| Size | Integer | Size of the backup file (in bytes) |
| Date | Timestamp | Backup time of the snapshot, such as 2016-03-17 02:10:37 |
| IntranetUrl | String | Download URL in private network |
| InternetUrl | String | Download URL in public network |
| Type | String | Specific log type. Available value: slowlog - Slow log |

## TableName

Table name

Referenced by the following API: DescribeBackupTables.

| Name | Type | Description |
|------|------|-------|
| TableName | String | Table name |

## TablePrivilege

Permissions of database table

Referenced by the following API: DescribeAccountPrivileges, and ModifyAccountPrivileges.

| Name | Type | Required | Description |
|------|------|----------|------|
| Database | String | Yes | Name of the database |
| Table | String | Yes | Name of the database table |
| Privileges | Array of String | Yes | Permission information |

## ZoneConf

Information on multiple availability zones

Referenced by the following API: DescribeDBZoneConfig.

| Name | Type | Required | Description |
|------|------|----------|------|
| DeployMode | Array of Integer | Yes | Availability zone deployment method. Available values: 0 - Single availability zone; 1 - Multiple availability zones |
| MasterZone | Array of String | Yes | Availability zone in which the master instance resides |
| SlaveZone | Array of String | Yes | The availability zone in which the slave database 1 resides in case of multi-availability zone deployment |
| BackupZone | Array of String | Yes | The availability zone in which the slave database 2 resides in case of multi-availability zone deployment |

## ZoneSellConf

Supported configuration of availability zone

Referenced by the following API: DescribeDBZoneConfig.

| Name | Type | Description |
|------|------|-------|
| Status | Integer | Availability zone status. Possible return values: 0 - Unavailable; 1 - Available; 2 - Open; 3 - Stop selling; 4 - Disable display |
| ZoneName | String | Availability zone name |
| IsCustom | Boolean | Indicates whether the instance type is custom |
| IsSupportDr | Boolean | Indicates whether the disaster recovery is supported |
| IsSupportVpc | Boolean | Indicates whether VPC is supported |
| HourInstanceSaleMaxNum | Integer | Maximum supported number of instances billed by hour |
| IsDefaultZone | Boolean | Indicates whether it is the default availability zone |
| IsBm | Boolean | Indicates whether it is BM zone |
| PayType | Array of String | Supported billing method. Possible return values: 0 - Prepaid; 1 - Bill by hour; 2 - Postpaid |
| ProtectMode | Array of String | Data replication mode. 0 - Async replication; 1 - Semisync replication; 2 - Strongsync replication |
| Zone | String | Availability zone name |
| SellType | Array of [SellType](#SellType) | Array of supported instance types |
| ZoneConf | [ZoneConf](#ZoneConf) | Information on multiple availability zones |


