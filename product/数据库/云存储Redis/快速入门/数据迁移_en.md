## How to Use Redis Migration Tool
## 1. Overview of Self-built Instance Migration
Currently, Tencent CRS supports two types of migration: self-built CVM instance migration and public network instance migration.
#### 1.1 Glossary

| Term | Description | 
|---------|---------|
| Source instance | Source instance of the migration | 
| Destination instance | Destination instance of the migration, i.e. Tencent CRS instance purchased by the user | 
| Self-built CVM instance migration | Migrate the Redis service deployed on Tencent CVM to Tencent CRS | 
| Public network instance migration | Migrate the Redis service deployed in public network environment to Tencent CRS | 

#### 1.2 Notes on Migration
1.	Currently you can only migrate instances to Tencent CRS master/slave editions;
2.	To ensure migration efficiency, you cannot migrate self-built CVM instance to other regions;
3.	Due to restrictions of rdb protocol, currently it is not supported to migrate self-built instance of Redis 3.2 version;
4.	When migrating public network instance, please ensure that the source instance service is accessible via public network environment;
5.	When the migration succeeds, you can disconnect from the source instance and switch the connection to destination instance after the data is verified at business side.

## 2. Migration Procedure
#### 2.1 Creating a Migration Task
Enter the "Migration Task List" and create a migration task by following the steps below:
1.	Select the region to which the destination instance belongs;
2.	Select migration task type ("self-built CVM instance migration" or "public network instance migration");
3.	Click "New Instance Migration Task" to go to the "New Migration Task" page.
![](https://mc.qcloudimg.com/static/img/fdb19a7ff4ba6b8f8f66566910927213/1.png)

#### 2.2 Entering Basic Information
The following description is based on Redis instance on CVM. The same is applicable to the public network instance migration.

| Field | Description | Use | Required | 
|---------|---------|---------|---------|
| Task Name | Name of the migration task | Used by users for their management of tasks | Yes |
| CVM Instance ID | ID of the Tencent CVM in which the source Redis instance resides | The migration task will check the operation status of the CVM with this ID | Yes |
| CVM Private IP | Private IP of the Tencent CVM in which the source Redis instance resides | The migration task will check the private IP of CVM | Yes |
| Port | Port number of source instance | The migration task will access the source instance service | Yes |
| Password | Source instance password | Used for authentication when accessing the source instance service | Yes |
| Instance ID | Destination instance ID | Data is synchronized to the destination instance | Yes |
Note: If your source instance doesn't have a password, please [Contact Us](https://console.qcloud.com/workorder/category/create?level1_id=10&level2_id=103&level1_name=%E6%95%B0%E6%8D%AE%E5%BA%93&level2_name=%E4%BA%91%E5%AD%98%E5%82%A8Redis%20CRS) to configure password-free access
![](https://mc.qcloudimg.com/static/img/e237dfb8238ed627026185359cccf781/2.png)

#### 2.3 Parameter Configuration
![](https://mc.qcloudimg.com/static/img/539c11f2e7b3cc222f8b171792d17aa5/3.png)
The system will configure these parameters at the start of the migration task. The parameters will return to their original values when the migration is finished. (It is recommended to use default values to ensure migration efficiency)

![](https://mc.qcloudimg.com/static/img/731eb2d6562dfd1429c52eef94d4e084/4.png)
Click "Check" to verify the parameters

![](https://mc.qcloudimg.com/static/img/0ce244608ba76dbc00843af62afbf9be/5.png)
If verification is successful, click "Confirm New Task"
Note:
1. You can continue with the data migration even if there are warnings. However, you need to check if the warnings may affect your data
2. Special note: If the network is inaccessible, please check the security group of the service to which the source instance belongs. All ports for the security group should be allowed.

#### 2.4 Starting the Migration Task
When parameter verification is successful, you can start the task by checking it, then click "Start" in the navigation bar or in the Action section. The task will verify parameters again when it starts. In this case, you can only cancel/view the task or check the status of verification process.
![](https://mc.qcloudimg.com/static/img/51ee9697fd1524cf0d260d9723237ad1/7.png)

When the task starts and begins to verify parameters, the task status will be "Verifying Parameters"
![](https://mc.qcloudimg.com/static/img/7f020d28b70c1282cb95c26d4f4b4037/8.png)

Data migration will begin once the parameters have been successfully verified
![](https://mc.qcloudimg.com/static/img/99ea6dc76bba850aae5915969d1e56eb/9.png)
During data synchronization, data offset and the changes in the keys of source/destination instances will be displayed


#### 2.5 Stop Synchronization
When the keys of source/destination instances are consistent with each other, click "Stop Synchronization" and then "OK" to complete the data synchronization.
You can verify the data on the destination instance. If the verification is passed, the synchronization can be stopped.
![](https://mc.qcloudimg.com/static/img/9fd273f97043cd9c219455112775393c/10.png)

The migration task is completed after you stop the synchronization operation
![](https://mc.qcloudimg.com/static/img/5df72d6d546388f8055c64ddabaeac2b/11.png)
