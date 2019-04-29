## The 9th Release

Release time: 2018-08-02 15:48:57

The following changes are contained in this release:

The existing documents were improved.

APIs added:

* [DescribeRollbackRangeTime](/document/api/236/#)
* [DescribeTables](/document/api/236/#)
* [StartBatchRollback](/document/api/236/#)

Data structures added:

* [InstanceRollbackRangeTime](/document/api/236/##InstanceRollbackRangeTime)
* [RollbackDBName](/document/api/236/##RollbackDBName)
* [RollbackInstancesInfo](/document/api/236/##RollbackInstancesInfo)
* [RollbackTableName](/document/api/236/##RollbackTableName)
* [RollbackTables](/document/api/236/##RollbackTables)
* [RollbackTimeRange](/document/api/236/##RollbackTimeRange)

## The 8th Release

Release time: 2018-07-26 12:22:36

The following changes are contained in this release:

The existing documents were improved.

APIs added:

* [DescribeDBPrice](/document/api/236/#)

## The 7th Release

Release time: 2018-07-12 16:12:26

The following changes are contained in this release:

The existing documents were improved.

**API deleted:**

* DescribeBackupDownloadDbTableCode

**Data structure deleted:**

* DatabaseTableList

## The 6th Release

Release time: 2018-07-05 14:15:06

The following changes are contained in this release:

The existing documents were improved.

Data structures added:

* [RoInstanceInfo](/document/api/236/##RoInstanceInfo)

Data structure modified:

* [InstanceInfo](/document/api/236/##InstanceInfo)
	* **Modified member:** RoVipInfo
* [RoGroup](/document/api/236/##RoGroup)
	* New members: RoInstances, Vip, Vport

## The 5th Release

Release time: 2018-06-14 12:15:42

The following changes are contained in this release:

The existing documents were improved.

API modified:

* [CreateBackup](/document/api/236/#)
	* New output parameter: BackupId
* [CreateDBInstance](/document/api/236/#)
	* **Modified output parameter:** DealIds
* [CreateDBInstanceHour](/document/api/236/#)
	* **Modified output parameter:** DealIds
* [DescribeBackupTables](/document/api/236/#)
	* **Modified input parameter:** SearchTable
* [UpgradeDBInstance](/document/api/236/#)
	* **Deleted output parameter:** DealNames

Data structure modified:

* [RoGroup](/document/api/236/##RoGroup)
	* **Modified member:** RoGroupMode

## The 4th Release

Release time: 2018-05-31 14:45:35

The following changes are contained in this release:

The existing documents were improved.

APIs added:

* [CreateAccounts](/document/api/236/#)
* [DeleteAccounts](/document/api/236/#)
* [DescribeAccountPrivileges](/document/api/236/#)
* [DescribeAccounts](/document/api/236/#)
* [DescribeDBInstanceConfig](/document/api/236/#)
* [DescribeDBSwitchRecords](/document/api/236/#)
* [DescribeDatabases](/document/api/236/#)
* [ModifyAccountDescription](/document/api/236/#)
* [ModifyAccountPassword](/document/api/236/#)
* [ModifyAccountPrivileges](/document/api/236/#)
* [OpenDBInstanceGTID](/document/api/236/#)
* [RestartDBInstances](/document/api/236/#)
* [VerifyRootAccount](/document/api/236/#)

Data structures added:

* [Account](/document/api/236/##Account)
* [AccountInfo](/document/api/236/##AccountInfo)
* [BackupConfig](/document/api/236/##BackupConfig)
* [ColumnPrivilege](/document/api/236/##ColumnPrivilege)
* [DBSwitchInfo](/document/api/236/##DBSwitchInfo)
* [DatabasePrivilege](/document/api/236/##DatabasePrivilege)
* [SlaveConfig](/document/api/236/##SlaveConfig)
* [TablePrivilege](/document/api/236/##TablePrivilege)

## The 3rd Release

Release time: 2018-05-17 15:58:40

The following changes are contained in this release:

The existing documents were improved.

APIs added:

* [DescribeDBZoneConfig](/document/api/236/#)

Data structures added:

* [RegionSellConf](/document/api/236/##RegionSellConf)
* [SellConfig](/document/api/236/##SellConfig)
* [SellType](/document/api/236/##SellType)
* [ZoneConf](/document/api/236/##ZoneConf)
* [ZoneSellConf](/document/api/236/##ZoneSellConf)

Data structure modified:

* [InstanceInfo](/document/api/236/##InstanceInfo)
	* New members: UniqVpcId, UniqSubnetId

## The 2nd Release

Release time: 2018-05-11 10:47:37

The following changes are contained in this release:

The existing documents were improved.

Data structure modified:

* [InstanceInfo](/document/api/236/##InstanceInfo)
	* **Modified member:** RoVipInfo

## The 1st Release

Release time: 2018-04-24

The following changes are contained in this release:

The existing documents were improved.

APIs added:

* [AssociateSecurityGroups](/document/api/236/#)
* [CloseWanService](/document/api/236/#)
* [CreateBackup](/document/api/236/#)
* [CreateDBImportJob](/document/api/236/#)
* [CreateDBInstance](/document/api/236/#)
* [CreateDBInstanceHour](/document/api/236/#)
* [DeleteBackup](/document/api/236/#)
* [DescribeBackupConfig](/document/api/236/#)
* [DescribeBackupDatabases](/document/api/236/#)
* [DescribeBackupDownloadDbTableCode](/document/api/236/#)
* [DescribeBackupTables](/document/api/236/#)
* [DescribeBackups](/document/api/236/#)
* [DescribeBinlogs](/document/api/236/#)
* [DescribeDBImportRecords](/document/api/236/#)
* [DescribeDBInstanceCharset](/document/api/236/#)
* [DescribeDBInstanceGTID](/document/api/236/#)
* [DescribeDBInstanceRebootTime](/document/api/236/#)
* [DescribeDBInstances](/document/api/236/#)
* [DescribeDBSecurityGroups](/document/api/236/#)
* [DescribeProjectSecurityGroups](/document/api/236/#)
* [DescribeSlowLogs](/document/api/236/#)
* [DescribeTasks](/document/api/236/#)
* [DisassociateSecurityGroups](/document/api/236/#)
* [InitDBInstances](/document/api/236/#)
* [IsolateDBInstance](/document/api/236/#)
* [ModifyBackupConfig](/document/api/236/#)
* [ModifyDBInstanceName](/document/api/236/#)
* [ModifyDBInstanceProject](/document/api/236/#)
* [ModifyDBInstanceSecurityGroups](/document/api/236/#)
* [ModifyDBInstanceVipVport](/document/api/236/#)
* [ModifyInstanceParam](/document/api/236/#)
* [OpenWanService](/document/api/236/#)
* [StopDBImportJob](/document/api/236/#)
* [SwitchForUpgrade](/document/api/236/#)
* [UpgradeDBInstance](/document/api/236/#)
* [UpgradeDBInstanceEngineVersion](/document/api/236/#)

Data structures added:

* [BackupInfo](/document/api/236/##BackupInfo)
* [BinlogInfo](/document/api/236/##BinlogInfo)
* [DatabaseName](/document/api/236/##DatabaseName)
* [DatabaseTableList](/document/api/236/##DatabaseTableList)
* [DrInfo](/document/api/236/##DrInfo)
* [First](/document/api/236/##First)
* [ImportRecord](/document/api/236/##ImportRecord)
* [Inbound](/document/api/236/##Inbound)
* [InstanceInfo](/document/api/236/##InstanceInfo)
* [InstanceRebootTime](/document/api/236/##InstanceRebootTime)
* [MasterInfo](/document/api/236/##MasterInfo)
* [Outbound](/document/api/236/##Outbound)
* [ParamInfo](/document/api/236/##ParamInfo)
* [Parameter](/document/api/236/##Parameter)
* [RoGroup](/document/api/236/##RoGroup)
* [RoVipInfo](/document/api/236/##RoVipInfo)
* [SecurityGroup](/document/api/236/##SecurityGroup)
* [SlaveInfo](/document/api/236/##SlaveInfo)
* [SlowLogInfo](/document/api/236/##SlowLogInfo)
* [TableName](/document/api/236/##TableName)


