> TDSQL内核采用MariaDB 10.0修改，兼容性与MariaDB 10.0基本相同，这里明确如下：

## TDSQL与MySQL兼容性
### 2015年12月31日更新
- 数据文件和表定义文件是二进制兼容的；
- 所有的客户端API和协议都是兼容的；
- 所有的文件名、二进制文件、路径、端口号等都是相同的；
- 所有的连接器，包括PHP、Perl、Python、Java、.NET、Ruby、MySQL的连接器在MariaDB上都可以正常使用的，不需要进行任何改动。
- 可以使用MySQL客户端链接到TDSQL上。

## TDSQL和MySQL5.6的不兼容性
### 2015年12月31日更新
- TDSQL的GTID和MySQL 5.6的GTID不能兼容，也就是说MySQL不能作为TDSQL的从库；
- 如果仅仅给出选项的前缀部分，例如使用--big-table取代--big-tables，MySQL将会给出警告，而TDSQL将会正常工作。也就是说，只要给出的前缀部分能够唯一地标识该选项即可。
- 为了使CREAT TABLE ... SELECT命令在基于行模式复制和基于命令模式复制的情况下都能正常工作，TDSQL中的CREAT TABLE ... SELECT命令在从库上将会被转化为CREAT OR RPLACE命令执行。这样的好处是即使从库在执行CREAT TABLE ... SELECT命令时宕机了，仍然能够正常工作。

### 2016年1月12日更新
- TDSQL的**innodb_page_size**默认设置为*4KB*，MySQL默认设置为16KB，会导致单个索引不能超过768字节

### 2016年1月22日更新
- 在JDBC应用程序下，如果使用**mysql-connector-java.jar**，在执行如下子查询SQL时可能报错：
```
例如：
select * from (select col_a , col_b , from tbl_a where col_b=1) tx where tx.col_a = '01';
错误：Table db.tx' doesn't exist
```

- 使用**mariadb-java-client-1.2.x.jar**时，在执行如下子查询SQL时可能出现异常

```
例如：
select col_a as a from tbl;
查询实际成功，然而在结果集里取结果的时候，只能用原列名，不能用别名查询成功；
例如在获取列数据时如果使用列的别名a，就会遇到失败，而只能使用col_a取值。
```

- 使用**mariadb-java-client-1.3.x.jar**时，会遇到如果设置了autocommit属性（global或者session），那么执行commit方法就会报错。
- 经测试表明，在Hibernate、entityframework框架中，如果设置参数**useAffectedRows=false**，并要求update语句返回**matched rows**时，由于Mariadb忽略了客户端在建立连接阶段推送的**CLIENT_FOUND_ROWS**字段，会导致**useAffectedRows=false**参数的设置不生效，使得update实际返回affected rows。

```
例如：
	执行: update tal_a set col_a = ‘value’;
	如果col_a的值已经是’value’，此时不会执行更新操作。affected rows=0而matched rows=1。
	此时框架需要server返回1，但实际返回0，会导致框架判断异常。
```
