**1. Notes on upgrade of a Cloud Database instance**

During the upgrade of a Cloud Database, a flash of interruption lasting for 1-30 seconds will happen to the instance, so it is recommended that you enable automatic reconnection between your applications and the Cloud Database in advance to avoid service unavailable.
The Quick Upgrade feature is under a gray release. Users who are provided with such feature may not be subject to the above limit.

**2. Definition of master/slave in the documentation of Cloud Database**

In the documentation of Cloud Database, slave refers to the hot backup CVM of the Cloud Database under high availability scheme. When the master fails, the slave will be put into use in real time for continuous service.

**3. The architecture of "one master plus two slaves" is recommended if strong synchronization is required**

When you execute strong synchronous replication, the master database will be hanged if it is disconnected from the slave database or the slave database fails. The architecture of "one master plus one slave" cannot provide a high availability scheme, because the failure of both master and slave may result in data loss or disorder.
 
**4. Using weak password on a public network may lead to security risks**

Public network IP has high probability to be detected and scanned by malicious users. If you use weak password (such as 12345678 and 1234abcd) on such network for a long time, your database may suffer great security risks.


**5. Notes on MariaDB (TDSQL) rollback**

- MariaDB (TDSQL) supports data rollback, but we recommend you to back up your key data before rollback.
- Data is rolled back to the temporary instance rather than the master instance to avoid affecting the existing network instance after completion of rollback.
- The temporary instance can be switched to the master instance. To avoid confusion, all backup data from the original master instance are invisible after switchover. If you need such data, submit a ticket for assistance.
- Each master instance has and can generate only one temporary instance.
- The temporary instance can be saved for a maximum of 48 hours. Beyond that, it will be terminated automatically.
- We do not provide full backup for temporary instances. You can use a third-part tool to back up them manually if necessary.


**6. Notes on Cloud Database locking policy**

The Cloud Database provides a locking mechanism through which your instance will be locked as read-only if its storage space exceeds the threshold of 110% according to TDSQL. It is recommended that you check the usage of storage space regularly, and enable SMS alert in the TDSQL console regarding disk space usage. If you fail to upgrade your instance capacity for financial reasons, you can submit a ticket to apply for 1 to 3 working days' access to your instance.


**7. Master/Slave switchover during MariaDB (TDSQL) failure**

MariaDB (TDSQL) features high availability modes including one master plus one slave, and one master plus two slaves. When the master database fails, TDSQL is able to switch to the slave database within 1 second (200 ms average). During master/slave switchover, you may not access your instance in a maximum of 30 seconds because of troubleshooting and data synchronization selection. Therefore, you need to enable automatic reconnection between your applications and TDSQL in advance to avoid service unavailable. The switchover process is independent of your business. The IP port does not change and business intervention is not required. All you need to ensure is that your business has an automatic reconnection mechanism.


**8. What you need to know after purchasing a Cloud Database**

After purchasing a Cloud Database instance, you don't need to do basic operation and maintenance (such as high availability, backup, and security patches) to your database, but the following aspects need to be focused on:

1) CPU, IOPS, space and number of connections of your Cloud Database instance. If they are not sufficient, the instance needs to optimized or upgraded.

2) Performance of your cloud database instance, number of slow SQL statements, optimization of SQL statements, redundant or missing indexes.


**9. You cannot change any data in mysql, information_schema, performance_schema, and sysdb**

**10. SQL statements cannot be used to set permissions for accounts, which can only be done via Console. The following 19 permissions are supported:**

SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, REFERENCES, INDEX, ALTER, 
CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, CREATE VIEW, SHOW VIEW, 
CREATE ROUTINE, ALTER ROUTINE, EVENT, TRIGGER, SHOW DATABASES.

**11. TDSQL does not provide super administrator accounts**

**12. Use InnoDB storage engine, for other storage engine may lead to poor performance**

**13. It is recommended that you use public network address for routine maintenance, rather than connecting the business server**


