## 1. Background
Cloud Database MariaDB (TDSQL) supports read-write separation in default. Each slave in the architecture supports read-only capability. If multiple slaves are configured, they can be allocated to low-load slave automatically by a gateway cluster (TProxy).

## 2. Read-write separation based on read-only account
Read-only account has only read permission. It reads data from a slave (or a read-only instance) of database cluster in default. TDSQL can set read-only account and read policy in "Account Management", as shown below:

![](https://mc.qcloudimg.com/static/img/667143c40f947d2f7cb4f3af8c814d2c/image.png)

In the settings of read-only account, you can set "Read-only request distribution policy", to define the read policy in case of a failure of slave (or high delay). "Read-only slave delay parameter" is used to define the delay of data synchronization, and is used in combination with "Read-only request distribution policy", as shown below:

![](https://mc.qcloudimg.com/static/img/5a5a3df53530feb4232826bd19020216/image.png)

>Suggestion on configurations:
>If you design a transaction system
> 
> - Core transaction module: Set a regular account which is both readable and writable.
> - Balance query module: Set a read-only account which reads data from slave in default. Request distribution policy: Read from master in case of a failure of slave, and set the delay parameter to no more than 10 seconds, to ensure the master-slave performance is consistent with the data queried by users.
> - Batch query module: Set a read-only account which reads data from slave in default. Request distribution policy: Error occurs in case of a failure of slave, and set the delay parameter to more than 30 seconds, to protect the master performance from being affected.
> 
> In addition, since the strongsync mechanism is to send a response after the data has been written in the transaction log of slave, the database table of slave may not be updated, therefore, delay occurs.


## 3. Read-write separation based on annotation
Add /*slave*/ field before each SQL to be read by slave, and add -c parameter after mysql to resolve the annotation `mysql  -c -e  "/*slave*/sql"`, to automatically distribute the read request to slave. Examples are shown below:

```
//Read by master//
select * from emp order by sal, deptno desc;
//Read by slave//
/*slave*/ select * from emp order by sal, deptno desc;
```


>Note:
>
>- This feature only supports the read operation of slave (select). Non-select statements will fail;
>
>- -c parameter requires to be added after mysql to resolve the annotation	
>
>- `/*slave*/` must be lowercase, and no spaces are needed before and after the statement;
>
>- If MAR (Strongsync) mechanism is affected due to slave exception, the read operation on slave is automatically switched to that on master.

