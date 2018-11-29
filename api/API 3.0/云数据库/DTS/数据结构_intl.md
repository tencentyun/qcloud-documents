## ConsistencyParams

Sampling parameters in a sampling test

Referenced by the following APIs: CreateMigrateJob, DescribeMigrateJobs, and ModifyMigrateJob.

| Name | Type | Required | Description |
|------|------|----------|------|
| SelectRowsPerTable | Integer | Yes | An integer between 1 and 100. The proportion of sampling rows per table in select(*) comparison. |
| TablesSelectAll | Integer | Yes | An integer between 1 and 100. The proportion of tables in select(*) comparison. |
| TablesSelectCount | Integer | Yes | An integer between 1 and 100. The proportion of tables in select count(*) comparison. |

## DstInfo

Destination instance information depending on the migration task type

Referenced by the following APIs: CreateMigrateJob, DescribeMigrateJobs, and ModifyMigrateJob.

| Name | Type | Required | Description |
|------|------|----------|------|
| InstanceId | String | Yes | Destination instance ID |
| Ip | String | No | Destination instance VIP |
| Port | Integer | No | Destination instance vport |
| Region | String | No | Destination instance ID |
| ReadOnly | Integer | No | Enables/Disables read-only mode |

## MigrateDetailInfo

Detailed migration process

Referenced by the following APIs: DescribeMigrateJobs.

| Name | Type | Description |
|------|------|-------|
| StepAll | Integer | Total number of steps |
| StepNow | Integer | The current step |
| Progress | String | The overall progress |
| CurrentStepProgress | String | The progress of the current step |
| MasterSlaveDistance | Integer | Distance between the master and slave (in MB) |
| SecondsBehindMaster | Integer | Time between master and slave (in sec) |
| StepInfo | Array of [MigrateStepDetailInfo](#MigrateStepDetailInfo) | Step information |

## MigrateJobInfo

Details of a migration task

Referenced by the following APIs: DescribeMigrateJobs.

| Name | Type | Description |
|------|------|-------|
| JobId | String | ID of a data migration task |
| JobName | String | Name of a data migration task |
| MigrateOption | [MigrateOption](#MigrateOption) | Migration task configuration options |
| SrcDatabaseType | String | Database type of the source instance: mysql, redis, percona, mongodb, postgresql, sqlserver, or mariadb |
| SrcAccessType | String | Connection type of the source instance: extranet (a public network instance), cvm (a self-built CVM instance), dcg (an instance connected via Direct Connect), vpncloud (an instance connected via Tencent Cloud VPN), vpnselfbuild (an instance connected via self-built VPN), or cdb (a CDB instance) |
| SrcInfo | [SrcInfo](#SrcInfo) | Source instance information depending on the migration task type |
| DstDatabaseType | String | Database type of the destination instance: mysql, redis, percona, mongodb, postgresql, sqlserver, or mariadb |
| DstAccessType | String | Connection type of the destination instance: extranet (a public network instance), cvm (a self-built CVM instance), dcg (an instance connected via Direct Connect), vpncloud (an instance connected via Tencent Cloud VPN), vpnselfbuild (an instance connected via self-built VPN), or cdb (a CDB instance) |
| DstInfo | [DstInfo](#DstInfo) | Information on the destination instance |
| DatabaseInfo | String | Information on the source database table to be migrated. If you need to migrate the entire instance, this field should be []. |
| CreateTime | Timestamp | Time when a task is created (submitted) |
| StartTime | Timestamp | Start time of a task |
| EndTime | Timestamp | End time of a task |
| Status | Integer | Task status: 1 - Creating (Creating); 2 - Created (Created); 3 - Verifying (Checking); 4 - Verification successful (CheckPass); 5 - Verification failed (CheckNotPass); 6 - Prepare for running (ReadyRun); 7 - Running (Running); 8 - Ready (ReadyComplete); 9 - Successful (Success); 10 - Failed (Failed); 11 - Stopping (Stopping); 12 - Completing (Completing) |
| Detail | [MigrateDetailInfo](#MigrateDetailInfo) | Task details |

## MigrateOption

Migration task configuration options

Referenced by the following APIs: CreateMigrateJob, DescribeMigrateJobs, and ModifyMigrateJob.

| Name | Type | Required | Description |
|------|------|----------|------|
| RunMode | Integer | Yes | Run mode of a task. Available values: 1 - Immediate execution; 2 - Timed execution |
| ExpectTime | Timestamp | No | Expected execution time. When the runMode = 2, the field is required. Format: yyyy-mm-dd hh: mm: ss |
| MigrateType | Integer | Yes | Data migration type. Available values: 1 - Structural migration; 2 - Full migration; 3 - Full + Incremental migration |
| MigrateObject | Integer | No | The object to be migrated: 1 - Entire instance; 2 - Specified database table |
| ConsistencyType | Integer | No | Data comparison type: 1 - Not configured; 2 - Full test; 3 - Sample test; 4 - Verify inconsistent tables only; 5 - No test |
| IsOverrideRoot | Integer | No | Indicates whether to overwrite the Root account of destination database with that of source database. Available values: 0 - Do not overwrite; 1 - Overwrite. Default is 0 when the database table or structural migration is selected. |
| ExternParams | String | No | Additional parameters used by different databases, which are described in JSON format. <br/>The following parameters can be defined for Redis: <br/>{ <br/>	"ClientOutputBufferHardLimit":512, 	Hard capacity limit of slave buffer (in MB) <br/>	"ClientOutputBufferSoftLimit":512, 	Soft capacity limit of slave buffer (in MB) <br/>	"ClientOutputBufferPersistTime":60, Duration of soft limit on the slave buffer (in sec) <br/>	"ReplBacklogSize":512, 	Capacity limit of circular buffer (MB) <br/>	"ReplTimeout":120，		Replication timeout (in sec) <br/>}<br/>The following parameters can be defined for MongoDB: <br/>{<br/>	'SrcAuthDatabase':'admin', <br/>	'SrcAuthFlag': "1", <br/>	'SrcAuthMechanism':"SCRAM-SHA-1"<br/>} |
| ConsistencyParams | [ConsistencyParams](#ConsistencyParams) | No | Sampling parameters in a sampling test |

## MigrateStepDetailInfo

Step information of a migration task

Referenced by the following APIs: DescribeMigrateJobs.

| Name | Type | Description |
|------|------|-------|
| StepNo | Integer | Step sequence |
| StepName | String | Step name |
| StepId | String | Step ID |
| Status | Integer | Step status: 0 - Default value; 1 - Successful; 2 - Failed; 3 - Executing; 4 - Not executed |

## SrcInfo

Information on the source instance

Referenced by the following APIs: CreateMigrateJob, DescribeMigrateJobs, and ModifyMigrateJob.

| Name | Type | Required | Description |
|------|------|----------|------|
| AccessKey | String | No | Alibaba Cloud AccessKey |
| Ip | String | No | IP address of the instance |
| Port | Integer | No | Port of the instance |
| User | String | No | User name of the instance |
| Password | String | No | Password of the instance |
| RdsInstanceId | String | No | Alibaba Cloud RDS instance ID |
| CvmInstanceId | String | No | Short ID of a CVM instance, such as: ins-olgl89y8. It is identical to the instance ID displayed in the CVM console page. This field is required for self-built CVMs or public network instances connected via self-built VPN. |
| UniqDcgId | String | No | Direct Connect gateway ID |
| VpcId | String | No | VPC ID, which corresponds to the original numeral vpcId. It should be converted by calling the VPC API. |
| SubnetId | String | No | Subnet ID under the VPC, which corresponds to the original numeral subnet ID. It should be converted by calling the VPC API. |
| UniqVpnGwId | String | No | VPN gateway ID assigned by the system |
| InstanceId | String | No | Short ID of an instance |
| Region | String | No | Region name, for example: ap-guangzhou |
| Supplier | String | No | Service provider, such as: Alibaba Cloud |


