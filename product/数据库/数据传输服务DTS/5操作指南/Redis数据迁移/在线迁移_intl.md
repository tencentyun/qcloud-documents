## How to Use Redis Migration Tool
## Overview of Self-built Instance Migration
The online migration tool does not support migration between Master/Slave, Cluster, and new-generation CRS instances.
#### Glossary

| Term | Description |
|---------|---------|
| Source Instance | Source instance of the migration |
| Destination Instance | Destination instance of the migration, i.e. Tencent CRS instance purchased by the user |
| Self-built CVM instance migration | Migrate the Redis service deployed on Tencent CVM to Tencent CRS |
| Public network instance migration | Migrate the Redis service deployed in public network environment to Tencent CRS |

#### Notes on migration
1. You can only migrate instances to Tencent CRS master/slave edition.
2. To ensure efficient migration, cross-region migration is not supported for self-built CVM instances.
3. Migration of self-built CRS 3.2 instances is not allowed by the RDB protocol.
4. For the migration of public network instances, make sure the source instance service is accessible in public network environments.
5. Only migrate instances that are running normally. Instances with an uninitialized password or another task going on cannot be migrated.
6. The destination instance must be an empty instance without any data. Instances in migration will be locked, so no data can be written into them.
7. When the migration succeeds, you can disconnect from the source instance and switch the connection to the destination instance after the data is verified at the business side.

## Migration Process
#### Create a migration task
Enter the migration task list page and click **New Task** to enter the migration task creation page.
![](https://mc.qcloudimg.com/static/img/bcf597d496292b67635a5f84d5ca1583/image.png)

#### Migration task configuration
Task name: Specify a name for the task.
Execution schedule: Specify a start time for your migration task.
![](https://mc.qcloudimg.com/static/img/6d45bf22f31923704b6055f3f94f1781/image.png)

>Note:
> 1. To start a scheduled task that has been modified, you need to click **Scheduled Start** again after the verification passes.
>2. If the start time is set at a time earlier than the current time, the scheduled start is converted to an immediate start. Click **Start Now** to start the task immediately.

#### Enter basic information
The following description is based on Redis instance on CVM. The same is applicable to the public network instance migration.

| Field | Description | Use | Required |
|---------|---------|---------|---------|
| Task name | Name of the migration task | Used by users for their management of tasks | Yes |
| CVM instance ID | ID of the Tencent CVM in which the source Redis instance resides | The migration task will check the operation status of the CVM with this ID | Yes |
| CVM private network IP | Private IP of the Tencent CVM in which the source Redis instance resides | The migration task will check the private IP of CVM | Yes |
| Port | Port number of source instance | The migration task will access the source instance service. | Yes |
| Password | Source instance password | The password is used for the authentication for accessing the source instance | No |
| Instance ID | Destination instance ID | Data is synchronized to the destination instance | Yes |

>Note: Currently, the migration of a source instance without the password is supported.

![](https://mc.qcloudimg.com/static/img/a42a402f82cf1bb2d3086e3e41265ec6/image.png)


#### Parameter settings
The system sets the parameters when the migration starts and recovers them to the history values after migration. Click **Next Step: Verification Task** to verify the parameters (Use default value for migration efficiency).
![](https://main.qcloudimg.com/raw/af8381c236e912ae4798b296c5cdbe0a.png)

Then, the parameters are under verification. Click **Start** after the verification passes.
 ![](https://main.qcloudimg.com/raw/7bd1e80ac17d3a0c6250ebcd15852c75.png)
>Note:
1. A migration can be executed even if an alarm occurs. But you need to check whether the alarm may affect the data.
2. Special note: If the network is inaccessible, please check the security group of the service to which the source instance belongs. All ports for the security group should be allowed.

#### Start the migration task
The migration task is still in "Not Started" status after the parameter verification passes. Click **Start Now** on the right. Another parameter verification is launched after the task is started. In this case, you can only cancel the task, view the task and view verification details.
![](https://main.qcloudimg.com/raw/935db808f97440ed4f6067e95d18a7ff.png)

Another parameter verification is launched after the task is started. The task status is "Verifying".
![](https://main.qcloudimg.com/raw/861ed166a2e473c491c79a92a2fd2fb4.png)

The data migration starts after the parameter verification passes.
![](https://main.qcloudimg.com/raw/e7b074825acfa8abae2260deb9afcc7d.png)

During data synchronization, data offset and the changes in the keys of source/destination instances will be displayed.


#### Complete the migration task 
When the keys of source/destination instances are consistent with each other, click **Finish** on the right and then **OK** to complete the data synchronization.
You can verify the data on the destination instance. If the verification is passed, the synchronization can be finished.
![](https://main.qcloudimg.com/raw/b4b428f3d5cb801488aa25864730edcf.png)

 
 
