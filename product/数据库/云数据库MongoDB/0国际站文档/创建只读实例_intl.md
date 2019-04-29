### 1. Overview ###
Tencent Cloud MongoDB Service allows users to create one or more read-only instances to support read-write separation application scenario, thus releasing the request stress on master instances and improving the read load capacity of users' business.
### 2. Basic Architecture ###
Changes on master instances are synchronized to read-only instances using oplog. Each read-only instance uses a "one master, two slaves" architecture at least. The architecture is shown as below:
![](https://main.qcloudimg.com/raw/dd4316c0d814aabfb1f05bf337976c1c.svg)
### 3. Service limits ###
- Backup and rollback: Backup and rollback are not supported.
- Data migration: Data migration to read-only instances is not supported.
- Database management: Creation and deletion of databases are not supported.
- Account management: Account creation/deletion, password reset and account authorization are not supported.
- A maximum of 3 read-only instances can be created for one master instance. If more read-only instances are needed, submit a ticket.
- Read-only instances can be created only for prepaid master instances.
- The engine of the read-only instance is consistent with that of the master instance.

### 4. Billing ###
Read-only instances only support prepaid billing. To create a disaster recovery instance, do the followings:<br>
- Step 1. On the instance list, click **More** -> **Management**.
	![](https://main.qcloudimg.com/raw/708eae19f300afe99a69281e9e02a6b6.png)
- Step 2. Click the **Read-only Instance** tab.
	![](https://main.qcloudimg.com/raw/beb2aa1493bbcc1f25ce8a21846f7fbc.png)
- Step 3. Click **New**.
	![](https://main.qcloudimg.com/raw/ebf55c6f6de21886f570c820c6baa8e5.png)
