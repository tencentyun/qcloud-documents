### 1. Overview ###
Tencent Cloud MongoDB Service allows users to create one or more disaster recovery instances for applications with a strong demand for continued services and reliable data or regulatory requirements, helping users enhance their capability to deliver continued services at a low cost and improve data reliability.
### 2. How it works ###
Changes on master instances are synchronized to disaster recovery instances using oplog. Each disaster recovery instance uses a "one master, two slaves" architecture at least. If any failure occurs with the master instance, the disaster recovery instance can be activated in seconds to recover business reading and writing.
### 3. Service limits ###
- Backup and rollback: Backup and rollback are not supported.
- Data migration: Data migration to read-only instances is not supported.
- Database management: Creation and deletion of databases are not supported.
- Account management: Account creation/deletion, password reset and account authorization are not supported.
- A maximum of 3 disaster recovery instances can be created for one master instance. If more disaster recovery instances are needed, submit a ticket.
- Disaster recovery instances can be created only for prepaid master instances.
- The engine of the disaster recovery instance is consistent with that of the master instance.
- Due to network isolation, you cannot create disaster recovery instances in finance zones for master instances in common regions, and vice visa.

### 4. Billing ###
Read-only instances only support prepaid billing. To create a disaster recovery instance, do the followings:<br>
- Step 1. On the instance list, click **More** -> **Management**.
	![](https://main.qcloudimg.com/raw/708eae19f300afe99a69281e9e02a6b6.png)
- Step 2. Click the **Disaster Recovery Instance** tab.
	![](https://main.qcloudimg.com/raw/d189ed8906f9b4130892ad1104444809.png)
- Step 3. Click **New**.
	![](https://main.qcloudimg.com/raw/f3a793223473a283c7f96e1dbf026f4c.png)
