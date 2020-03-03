>**Note:**
It is expected to support self-application at the end of August. If you need the service in advance, you may submit a ticket.

## 1. Overview
### 1.1 Features
When there is high pressure and demand of "read requests" in the case of large data volume, read-write separation function can be used to distribute read traffic to slave nodes.
DCDB developed by Tencent supports read-write separation by default. Each slave in architecture supports read-only capability. If multiple slaves are configured, gateway cluster (TProxy) automatically assigns traffic to low-load slaves to support read traffic of large applications.

### 1.2 Basic Principle
**Read-write separation** is designed to allow a master node to perform transactional operations like addition, modification and deletion (INSERT, UPDATE, DELETE), and allow slave nodes to perform query operation (SELECT).

## 2. Use Read-write Separation
### 2.1 Read-write separation based on read-only account
A read-only account is a type of account only with read permission to read data from a slave (or read-only instance) in a database cluster by default.
![](https://mc.qcloudimg.com/static/img/b3d0c86496bc308807a5c2136edd9fb4/image.png)
A read-only account is used to implement automatic distribution of read request to slave and return the result.
![](https://mc.qcloudimg.com/static/img/e302e114b8de2b6db5883d927893a6e3/image.png)
2.1.1 Read-write Separation Policy
In the setting options of read-only account, you can set "Read-only Request Allocation Policy" to define the "Read" policy when the slave fails (or experiences a long delay).
 - Select "Master" to read from the master when the delay of slave exceeds the limit.
 - Select "Report Errors" to report errors when the delay of slave exceeds the limit.
 - Select "Read from Slave Only" to ignore delay parameters and always read from slave (it's generally used to pull binlog sync).
 - Define "Read-only Slave Delay Parameter" to define the data synchronization delay time. It is used in combination with "Master" and "Report Errors" under "Read-only Request Allocation Policy".
![](https://mc.qcloudimg.com/static/img/138f7ac5797c9ca72189d35f694b15e5/image.png)

### 2.2 Read-write separation based on annotation
Add **```/*slave*/```** field before each SQL to be "read" by slave, and add -c parameter after mysql to resolve the annotation ```mysql -c -e "/*slave*/sql"``` to automatically distribute the read request to slave. Code examples are shown below:
```
//Read by master//
select * from emp order by sal,deptno desc;
//Read by slave//
/*slave*/ select * from emp order by sal,deptno desc;
```
> **Note:**
>1\. Only "read by slave" (select) is supported rather than other operations. Non-select statements will fail.
>2\. -c parameter needs to be added after mysql to resolve the annotation.
>3\. ```/*slave*/``` must be lowercase, and no spaces are needed before and after the statement.
>4\.  If MAR (Strongsync) mechanism is affected due to slave exception, the read operation on slave is automatically switched to that on master.
