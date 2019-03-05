## 1. Instance-related APIs
| API Function | Action Name | Description | 
|---------|---------|---------|
| [Query Instance List](/document/api/236/1266) | DescribeCdbInstances | Query the list of cloud database instances. It can use IDs, access addresses and status, and the likes of cloud database instances as filtering conditions to query the list of instances. |
| [Query Read-only Instance List](/document/api/236/6417) | GetCdbReadOnlyInstances | Query the list of read-only instances. You can input one or more master instance IDs to query the list of read-only instances associated with the master instance(s) |
| [Create Instance (Pay-by-usage)](/document/api/236/5175)| CreateCdbHour | Create cloud database instances, with the billing model of Pay-by-usage |
| [Query Price (Pay-by-usage)](/document/api/236/5176)| InquiryCdbPriceHour | Query the pay-by-usage price of a certain type of Cloud Database instance |
| [Query Supported Specifications(supporting custom availability zones and configurations)](/document/api/236/6109) | DescribeCdbProductListNew | Query supported specifications of cloud database instances, and support the creation of instances according to availability zones and custom specifications. Recommended to use |
| [Query Supported Specifications](/document/api/236/1333) DescribeCdbProductList | Query supported specifications of cloud database instances |
| [Initialize Instance](/document/api/236/5335) | CdbMysqlInit | Initialize a cloud database instance, and meanwhile can set the character set, port, root account password and table name case sensitivity of the instance during initialization.  |
| [Query Details on Initialization Task](/document/api/236/5334) | GetCdbInitInfo | Query details on the progress of the asynchronous task about initializing a cloud database instance through the initialization task ID |
| [Upgrade Instance](/document/api/236/7164) | UpgradeCdb | Upgrade cloud database instances. Instance types include master instance, disaster recovery instance and read-only instance.
| [Query Upgrade Price](/document/api/236/7193) | InquiryCdbUpgradePrice | Query the upgrade price of a cloud database instance. Instance types include master instance, disaster recovery instance and read-only instance. |
| [Upgrade Database Engine Version](/document/api/236/8371) | UpgradeCdbEngineVersion | Upgrade the engine version of a cloud database instance |
| [Query Details on Instance Upgrade Task](/document/api/236/8373) | GetCdbUpgradeJobInfo | Query details on instance upgrade task. The query of upgrade details on master instances, disaster recovery instances and read-only instances are supported. |
| [Terminate Instance (Pay-by-usage)](/document/api/236/6415) | CloseCdbHour | Instances in pay-by-usage mode can be terminated in real time |
| [Recover Instance (Pay-by-usage)](/document/api/236/6416) | OpenCdbHour | Instances in pay-by-usage mode, if terminated, can be recovered in real time through this API |
| [Set Automatic Renewal](/document/api/236/4112) | SetCdbAutoRenew| Set cloud database instances to be automatically renewed |
| [Modify Parent Project](/document/api/236/6541) | ModifyCdbInstanceProject | Modify the project a cloud database instance belongs to |
| [Reset Password](/document/api/236/1271) | ResetCdbInstancesPassword | Reset the password of the root account of a cloud database instance |
| [Modify Name](/document/api/236/1270) | ModifyCdbInstanceName | Modify the name of a cloud database instance |
| [Modify Port](/document/api/236/6543) | ModifyCdbInstanceVport | Modify the port of a cloud database instance, with supported port value range of 1024-65535 |
| [Modify Character Set](/document/api/236/4113) | ModifyCdbCharset | Modify the character set of a cloud database instance |
| [Enable Public Network Access](/document/api/236/7165) | OpenCdbExtranetAccess | Enable the public network access to a cloud database instance. After public network access is enabled, you can access an instance through the domain and port of a public network |
| [Disable Public Network Access](/document/api/236/7166) | CloseCdbExtranetAccess | Disable the public network access to a cloud database instance. After public network access is disabled, public network addresses will be inaccessible |
| [Switch Disaster Recovery Instance to Master Instance](/document/api/236/7460) | SwitchCdbDrToMaster | Switch a disaster recovery instance to a master instance in the cloud database. The region in the common parameters is the region where the disater recovery instance resides in |
| [Enable GTID](/document/api/236/8372) | OpenCdbGtid | Enable the GTID of a cloud database instance |
| [Query GTID Details on Instance](/document/api/236/8374) | GetCdbGtidInfo | Query details on instance's GTID |
| [Query Number of Instances in Subnet of VPC](/document/api/236/5440)  | GetCdbInstanceNumByVpcSubnetId | Query the number of cloud database instances under the subnet of a VPC |


## 2. Account-Related APIs
| API Function | Action Name | Description | 
|---------|---------|---------|
| [Query Account List](/document/api/236/8010) | GetCdbInstanceAccountList | Query the account list of a database |
| [Create Account](/document/api/236/8011) | CreateCdbInstanceAccount | Create the account of a database |
| [Query Permissions Settable for Account](/document/api/236/8063) | GetCdbInstanceAccountAvailablePrivileges | Query permissions that can be set for the account of a cloud data instance |
| [Query Account Permissions](/document/api/236/8062) | GetCdbInstanceAccountPrivileges | Query account permissions for a cloud data instance |
| [Modify Account Permission](/document/api/236/8060) | ModifyCdbInstanceAccountPrivileges | Modify access permission of the account for a cloud data instance |
| [Delete Account](/document/api/236/8012) | DelCdbInstanceAccount | Delete a database account |
| [Modify Account Notes](/document/api/236/8013) | ModifyCdbInstanceAccountRemarks | Modify the notes of a database account |
| [Modify Account Password](/document/api/236/8061) | ModifyCdbInstanceAccountPassword | Modify the account password for a cloud database instance|


## 3. Database-Related APIs
| API Function | Action Name | Description | 
|---------|---------|---------|
| [Query Database Schema](http://intl.cloud.tencent.com/document/product/236/8923) | GetCdbInstanceSchema | Query details on a database schema |
| [Query Database](/document/api/236/7167) | QueryCdbDatabases | Query database information of a cloud database instance |
| [Query Database Table](/document/api/236/7176) | QueryCdbDatabaseTables | Query database table information of a cloud database instance |


## 4. Parameter-Related APIs
| API Function | Action Name | Description | 
|---------|---------|---------|
| [Query Details on Default Parameter Template](/document/api/236/7190) | GetCdbDefaultParamInfo | Query details on the default template for database parameters |
| [Query List of Parameter Templates](/document/api/236/7185) | GetCdbParamTemplateList | Query the list of templates for database parameters |
| [Add Parameter Template](/document/api/236/7186) | AddCdbParamTemplate | Add a template for database parameters |
| [Delete Parameter Template](/document/api/236/7187) | DelCdbParamTemplate | It deletes a template for database parameters |
| [Query Details on Parameter Template](/document/api/236/7189) | GetCdbParamTemplateInfo | Query details on the template for cloud database parameters |
| [Modify Parameter Template](/document/api/236/7188) | ModifyCdbParamTemplate | Modify contents of the template for database parameters |
| [Query List of Parameters](/document/api/236/6369) | GetCdbParams | Query the list of database parameters using instance IDs|
| [Modify Parameter](/document/api/236/6368) | ModifyCdbParams | Modify database parameters, and return task ID of parameter modification after successful submission |
| [Query Modification Record of Parameters](/document/api/236/6367) | GetCdbParamsModifyHistory | Query the modification record of database parameters |
| [Query Details on Parameter Modification Task](/document/api/236/6428) | GetCdbModifyParamsJobTask | Query details on parameter modification task through task ID of parameter modification |


## 5. Monitoring-Related APIs
| API Function | Action Name | Description | 
|---------|---------|---------|
| [Query Monitoring Information of Physical Machine](/document/api/236/4687) | GetCdbDeviceMonitorInfo | Query monitoring information of a physical machine, temporarily only supporting the query of instances with highest configuration |
| [Query Statistics](/document/api/236/4688) | QueryCdbStatisticsInfo | Query statistics of a cloud database; query only statistics within last minute |


## 6. Import-Related APIs
| API Function | Action Name | Description | 
|---------|---------|---------|
| [Upload Imported File](/document/api/236/8595) | UploadCdbImportSQLFile | Used to upload imported file |
| [Start File Import Task](/document/api/236/8376) | StartCdbImportJob | Used to start a file import task |
| [Terminate File Import Task](/document/api/236/8379) | StopCdbImportJob | Used to terminate a file import task |
| [Query List of Imported Files](/document/api/236/8377) | GetCdbImportSQLFileList | Used to query the list of imported files |
| [Query Record of Recently Imported Files](/document/api/236/8378) | GetCdbImportSQLFileHistory | Used to query the record of recently imported files |


## 7. Rollback-Related APIs
| API Function | Action Name | Description | 
|---------|---------|---------|
| [Query Details on Rollback Task](/document/api/236/4114) | GetCdbRollbackJobTask | Query details on the rollback task performed on a cloud database instance |
| [Query List of Rollback Tasks](/document/api/236/4115) | GetCdbRollbackJob | Query the list of rollback tasks performed on a cloud database instance |
| [Query Rollback Time](/document/api/236/7168) | QueryCdbRollbackRangeTime | Query the time span during which a cloud database instance can be rolled back |
| [Run Database Table Rollback](/document/api/236/7169) | RollbackCdbDatabaseTables | Roll back database tables of a cloud database instance in batch |


## 8. Backup-Related APIs
| API Function | Action Name | Description | 
|---------|---------|---------|
| [Query Backups and Logs](/document/api/236/4691) | GetCdbExportLogUrl | Query cold backup data, binary logs and slow query logs of an instance |
| [Query Database Table for Backup Data](/document/api/236/5105) | GetBackupDatabaseTableList | Query database tables for backup data |
| [Query Backup Address (Query by Table is Supported)](/document/api/236/5125) | GetExportBackupUrl | Query addresses of backup data, and support query by database table |
| [Modify Backup Information](/document/api/236/7397) | ModifyCdbBackupInfo | Modify backup information, for example, the backup name |


## 9. Task-Related APIs
| API Function | Action Name | Description | 
|---------|---------|---------|
| [Query Task List](/document/api/236/7464) | GetCdbJobList | Query the list of tasks performed on a cloud database |
