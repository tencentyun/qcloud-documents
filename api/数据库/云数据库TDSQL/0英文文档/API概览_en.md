## 1. Instance-related APIs
| Feature | Action ID | Description | 
|---------|---------|---------|
| View Instance List | [CdbTdsqlGetInstanceList](/doc/api/309/5447) | View the list and details of instances |
| Modify Instance Name | [CdbTdsqlRenameInstance](/doc/api/309/5449) | Modify instance name |
| Expand Instance Capacity | [CdbTdsqlExpandInstance](/doc/api/309/5533) | Expand the instance capacity |
| Change Instance Project | [ CdbTdsqlAssignToProject](/doc/api/309/5534) | Change the project to which the instance belongs |
| Open Internet Address | [CdbTdsqlOpenWanIP](/doc/api/309/5535) | Open Internet address |
| Close Internet Address | [CdbTdsqlCloseWanIP](/doc/api/309/5536) | Close Internet address |
| Query Instance Specifications | [CdbTdsqlGetSpecList](/doc/api/309/5537) | Query instance specifications |
| Query Price |[CdbTdsqlGetPrice](/doc/api/309/5538)| Query price |
| Create Instance |[CdbTdsqlCreateInstance](/doc/api/309/5539)| Create an instance (prepaid) |
| Initialize Instance |[CdbTdsqlInitInstance](/doc/api/309/5540)| Initialize an instance |
| Renew Instance |[CdbTdsqlRenewInstance](/doc/api/309/5541)| Renew an instance |
| Query Project List |[CdbTdsqlGetProjectList](/doc/api/309/5604)| Query project list |
| Query Flow Status |[CdbTdsqlGetFlowInfo](/doc/api/309/5605)| Query flow status |
| Query Order Information |[CdbTdsqlGetOrderInfo](/doc/api/309/5690)| Query order information |
| Acquire Custom Backup Time |[CdbTdsqlGetBackupTime](/doc/api/309/5970)| Acquire custom backup time |
| Configure Custom Backup Time |[CdbTdsqlSetBackupTime](/doc/api/309/5969)| Configure custom backup time |

## 2. Account-related APIs

| Feature | Action ID | Description | 
|---------|---------|---------|
| Create Account | [CdbTdsqlAddUser](/doc/api/309/5394) | Create a Cloud Database account |
| View Account List | [CdbTdsqlGetUserList](/doc/api/309/5395) | Obtain the list of accounts for the instance |
| Delete Account | [CdbTdsqlDeleteUser](/doc/api/309/5396) | Delete an account for the instance |
| Configure Permissions | [ CdbTdsqlSetRight](/doc/api/309/5397) | Configure permissions for an account for accessing database object |
| Acquire Permission List | [CdbTdsqlGetRightList](/doc/api/309/5398) | Acquire the list of permissions for an account |
| Copy Permissions | [CdbTdsqlCopyRight](/doc/api/309/5399) | Copy the permissions of an account to another one |
| Modify Account Remarks | [CdbTdsqlChangeUserDesc](/doc/api/309/5400) | Modify the description of an account |
| Reset Account Password |[CdbTdsqlResetCdbInstancesPassword](/doc/api/309/5401)| Reset the password of database account |

## 3. Backup/Recovery-related APIs
| Feature | Action ID | Description | 
|---------|---------|---------|
| Acquire Log List |[CdbTdsqlGetLog](/doc/api/309/5402)| Acquire the list of full cold backup log, binlog and errlog as well as their download addresses |

## 4. Parameter Management APIs

| Feature | Action ID | Description | 
|---------|---------|---------|
| View Database Parameters |[CdbTdsqlGetConfigList](/doc/api/309/5403)| View the parameters of current database |
| Modify Database Parameters | [CdbTdsqlModifyConfig](/doc/api/309/5405) | Modify database parameters |
| View Backup Log Configuration | [CdbTdsqlQueryLogConfig](/doc/api/309/5406) | View the backup log configuration. Currently, only the number of days a log is kept is available |
| Modify Backup Log Configuration | [CdbTdsqlModifyLogConfig](/doc/api/309/5407) | Modify the backup log configuration. Currently, you can only modify the number of days a log is kept |

## 5. Monitor Management APIs

| Feature | Action ID | Description | 
|---------|---------|---------|
| View Instance Resource Usage | [CdbTdsqlGetResourceUsageInfo](/doc/api/309/5408) | View the information on instance resource usage, such as available disk space, CPU utilization |
| View Instance Performance Data |[CdbTdsqlGetPerformanceInfo](/doc/api/309/5409)| View instance performance data, such as number of active connections, I/O count per second for the disk |
| View Instance Resource Usage Details |[CdbTdsqlGetResourceUsageInfoDetail](/doc/api/309/5968)| View the details of instance resource usage |
| View Detailed Performance Data |[CdbTdsqlGetPerformanceInfoDetail](/doc/api/309/5967)| View detailed performance data of instance |
| Acquire Details of Slow Logs |[CdbTdsqlGetSlowLogAnalysis](/doc/api/309/5972)| Acquire the details of slow logs |
| Acquire Slow Log List |[CdbTdsqlGetSlowLogList](/doc/api/309/5973)| Acquire the list of slow logs |
