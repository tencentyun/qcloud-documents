## 1. Region-related APIs
| API | Action Name | Description |
|---------|---------|---------|
| [Query Supported Availability Zones](http://cloud.tencent.com/doc/api/260/4951) | DescribeRedisZones | Query the list of availability zones where the Redis is available |
| [Query Supported Specifications](http://cloud.tencent.com/doc/api/260/4974) | DescribeRedisProduct | Query the specifications of purchasable instances, such as maximum capacity, number of instances allowed to be purchased |


## 2. Instance-related APIs

| API | Action Name | Description |
|---------|---------|---------|
| [Query Instance Price (Annual or Monthly Plan)](http://cloud.tencent.com/doc/api/260/5324) | InquiryRedisPrice | Query the fees charged for creation and renewal of instance |
| [Create Instance (Annual or Monthly Plan)](http://cloud.tencent.com/doc/api/260/5325) | CreateRedis | Create a Redis instance based on configurations such as specified specification and network and deduct the fee returned by API [Query Instance Price](http://cloud.tencent.com/doc/api/260/5324) from the account balance |
| [Renew Instance (Annual or Monthly Plan)](http://cloud.tencent.com/doc/api/260/5326)  | RenewRedis| Renew a specified instance and deduct the fee returned by API [Query Instance Price](http://cloud.tencent.com/doc/api/260/5324) from the account balance |
| [Query Price for Instance Upgrade (Annual or Monthly Plan)](http://cloud.tencent.com/doc/api/260/5327) | UpgradeRedisInquiryPrice | Query the fee charged for upgrade of an instance to specified specification |
| [Upgrade Instance (Annual or Monthly Plan)](http://cloud.tencent.com/doc/api/260/5328)| UpgradeRedis | Upgrade an instance to specified specification and deduct the fee returned by API [Query Price for Instance Upgrade](http://cloud.tencent.com/doc/api/260/5327) from the account balance |
| [Query Order Details](http://cloud.tencent.com/doc/api/260/5329) | DescribeRedisDealDetail | Query the details of an order |
| [Set Auto Renewal](http://cloud.tencent.com/doc/api/260/5330)  | SetRedisAutoRenew| Set or cancel auto renewal. When auto renewal is set, the system will renew the instance automatically upon its expiration |
| [Query CRS Instances and Instance List](http://cloud.tencent.com/doc/api/260/1384) | DescribeRedis | Query the list of instance details based on conditions | 
| [Modify CRS Instance Password](http://cloud.tencent.com/doc/api/260/1390) | ModfiyRedisPassword | Modify the password for an instance |
| [Reset CRS Instance Password](/document/product/239/1390) | ResetMongoDBPassword | Reset the password for an instance |
| [Modify Project of Redis Instance](http://cloud.tencent.com/doc/api/260/1385) | ModifyRedisProject | Modify the project to which an instance belongs |
| [Clear CRS Instance](http://cloud.tencent.com/doc/api/260/1386) | ClearRedis | Clear the instance data | 
| [Query CRS Task Result](http://cloud.tencent.com/doc/api/260/1387) | DescribeTaskInfo | Query the task execution result |
| [Manually Back Up CRS Instance](/document/product/239/8402) | ManualBackupInstance | Back up a CRS instance manually |
| [Query CRS Instance Backup List](/document/product/239/8403) | GetRedisBackupList | Query the list of CRS instance backups |  
| [Restore CRS Instance](/document/product/239/8401) | RestoreInstance | Restore a CRS instance |
| [Export Backup of CRS Instance](/document/product/239/8430) | ExportRedisBackup | Export the backup of a CRS instance |  
| [Query Task List of CRS Instance](/document/product/239/8404) | GetRedisTaskList | Query the task list of a CRS instance |

