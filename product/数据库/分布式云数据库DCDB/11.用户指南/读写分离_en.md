## 1. Background
Cloud Database (TDSQL) supports read-write separation by default. The basic configuration of a standard database node set (SET) is one master and two slaves. Both two slaves support read capability by default.
In order not to affect a cluster's stability, users don't need to directly connect to the slave to perform read operation from TDSQL's slave. The read request is automatically assigned to a low-load slave by gateway cluster (TProxy).
## How to Implement
Add /*slave*/ field before each statement to be read by slave, and add -c parameter after mysql to resolve the annotation `mysql -c -e "/*slave*/sql"`, so as to implement automatic distribution of read request to slave. Example is shown below:

```
//Read by master//
select * from emp order by sal, deptno desc;
//Read by slave//
/*slave*/ select * from emp order by sal, deptno desc;
```


Note:
- 	Only "read by slave" (select) is supported rather than other operations. Non-select statements will fail.
- -c parameter needs to be added after mysql to resolve the annotation.	
- `/*slave*/` must be lowercase, and no space is needed before and after the statement.
- 	If MAR (Strongsync) mechanism is affected due to slave exception, the read operation on slave is automatically switched to that on master.

