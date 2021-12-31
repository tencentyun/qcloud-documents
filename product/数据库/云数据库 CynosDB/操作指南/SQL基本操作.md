## 查询版本
方法一：
```
MySQL [(none)]> SELECT CYNOS_VERSION();
+------------------------+
| CYNOS_VERSION() |
+------------------------+
| 5.7.mysql_cynos.1.3.10 |
+------------------------+
1 row in set (0.00 sec)
```
方法二：
```
MySQL [(none)]> SELECT @@CYNOS_VERSION;
+------------------------+
| @@CYNOS_VERSION |
+------------------------+
| 5.7.mysql_cynos.1.3.10 |
+------------------------+
1 row in set (0.00 sec)
```
方法三：
```
MySQL [(none)]> SHOW VARIABLES LIKE 'CYNOS_VERSION'; 
+---------------+------------------------+
| Variable_name | Value |
+---------------+------------------------+
| cynos_version | 5.7.mysql_cynos.1.3.10 |
+---------------+------------------------+
1 row in set (0.01 sec)
```
