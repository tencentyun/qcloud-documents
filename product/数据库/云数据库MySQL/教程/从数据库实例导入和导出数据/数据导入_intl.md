Online hot migration allows users to migrate CVM self-built MySQL database to CDB with continuous service, providing the migration service from local IDC with public IP/Port or MySQL database on other CVMs to database CDB.

Currently, the migration tool is only available in Guangzhou and Shanghai.

## 1. Preparations

### 1.1 Note

- Self-built migration tool is divided into two operation steps: cold backup data export and incremental data synchronization. Cold backup data export will have a certain impact on the load of source database, so it is recommended to perform database migration during off-peak business period.

- Currently, the public network migration feature only supports CDB instances in basic network.

### 1.2 Checking the Following Items in Advance
1. Check that the target CDB instance must be empty, and cannot have a created database table;
2. Check the version. It currently only supports the same versions including (5.1/5.5/5.6), as well as 5.1-\> 5.5, 5.5-\> 5.6;
3. Check that the capacity of target CDB instance must be larger than that of the source instance;
4. Create a migration account in the source MySQL database (there is no need to create an account if you already have an authorized account for data migration);
```
GRANT ALL PRIVILEGES ON *. * TO "migration account" @ "%" IDENTIFIED BY "migration password";
FLUSH PRIVILEGES;
```
		
5. Confirm the MySQL variables
	  Via `SHOW GLOBAL VARIABLES LIKE 'XXX'`; 
	  Check MySQL global variables to confirm whether the migration can be performed under current status:
```
			server_id > 1
		    log_bin = ON;
		    binlog_format = ROW/MIXED
		    binlog_row_image = FULL
		    innodb_stats_on_metadata = 0
```

6. Modify variables to specified values:

	a. Reboot to modify the MySQL configuration file `my.cnf`:
		        `log-bin=binlog`
	b. Modify the configuration dynamically:
```
		        set global server_id = 99;
		        set global binlog_format=ROW;
		        set global binlog_row_image=FULL;
		        set global innodb_stats_on_metadata = 0;
```

## 2. Steps

2.1. Log in to the console and enter the migration page
![][image-1]

2.2. Create a migration task
	- Click to create a migration task, and enter the task name, source database and information on target CDB for MySQL.
![][image-2]
	- Then, select the database to migrate (You can select to migrate all or part of the database tables), create and check the migration task information.
![][image-3]
![][image-4]
**Data migration**: Export the data in the selected database and import it into CDB for MySQL.
**Incremental synchronization**: After performing data export and import, set CDB for MySQL as the slave database of the source database to realize the incremental synchronization of the master and slave.

2.3. Verify migration task information
 After the creation of a migration task, you need to verify the migration task information. Only after all verification items have passed can the migration task be started. There are three statuses for task verification:

 - Pass: indicates that the verification is fully passed.
 - Warning: indicates that the verification does not pass. That means, during or after the migration, normal operation of database may be affected, but the implementation of the migration task will not be affected.
 - Failed: indicates that the verification does not pass, and the migration cannot be implemented. If the verification fails, check and modify the migration task information according to the error items, and then retry the verification. For reasons of failure, please refer to: "Verification Failure Description".
![][image-5]

2.4. Start migration
If the verification is passed, you can start the migration task. If you set a specified time for the migration task, the migration task will be queued and executed at the specified time. Otherwise, the migration task will be executed immediately.
After the migration is started, you can see the corresponding migration progress information under the migration task.
![][image-6]
> Note: Due to system design constraints, multiple migration tasks submitted or queued at a time will be performed serially based on the queuing time.

2.5. Incremental synchronization
When creating a migration task, the incremental synchronization option is selected by default. When the data migration is completed, target CDB for MySQL will be set as the slave database of the source database, and the new data of the source database during the migration will be synchronized to the target CDB for MySQL via master/slave synchronization. At this point, the modifications in the source database will be synchronized to the target CDB for MySQL. Therefore, you can switch your business to the target CDB for MySQL, and then click "Finish" to complete the migration.
After that, the synchronization relationship of master/slave will be disconnected.

2.6. Terminate the migration
During the migration process, if you need to terminate the migration, click "Terminate" button to terminate.
![][image-7]
> Note:
> 1. The reboot may cause the failure of verification or task. You may need to manually clear the data in the target database to reboot the migration task.
> 2. When migrating a single table, it is necessary to ensure that the tables relied by foreign keys of all tables must be migrated.

[image-1]:	//mccdn.qcloud.com/img56a76ba50e7cb.png
[image-2]:	//mccdn.qcloud.com/img56a7653c6f568.png
[image-3]:	//mccdn.qcloud.com/img56a76670eceb8.png
[image-4]:	//mccdn.qcloud.com/img56a765eb2bb88.png
[image-5]:	//mccdn.qcloud.com/img56a767198f5b7.png
[image-6]:	//mccdn.qcloud.com/img56a767afe0b8c.png
[image-7]:	//mccdn.qcloud.com/img56a76843ea5a9.png

