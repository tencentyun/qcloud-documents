## CDB导入数据报错：Specified key was too long
## 一、报错原因
	 ERROR 1071 (42000): Specified key was too long; max key length is 767 bytes
客户通过CVM的命令行向CDB导入XXXX.sql文件时，CDB返回Specified key was too long的报错。

对于报错信息“ERROR 1071 (42000): Specified key was too long; max key length is 767 bytes”，其实意思就是“索引字段长度太长，超过了767bytes”。

① innodb存储引擎，多列索引的长度限制如下：

  **每个列的长度不能大于767 bytes；所有组成索引列的长度和不能大于3072 bytes**

② myisam存储引擎，多列索引长度限制如下：

  **每个列的长度不能大于1000 bytes，所有组成索引列的长度和不能大于1000 bytes**

	TIPS：768/2=384个双字节 或者767/3=255个三字节的字段（GBK是双字节的，UTF8是三字节的，UTF8MB4是四字节的）

为什么在自建的数据库上是OK的，但是把数据导入CDB后就报Specified key was too long错误呢？

在CDB5.6及其以上版本，所有myisam表都会被自动转换为innodb，所以在自建数据库上有超过767 bytes的组合索引列，但是由于在自建库上myisam存储引擎，同样的建表语句在自建库上运行没问题，但是在CDB5.6版本以上就会有问题。

## 二、解决方案
### 1、修改备份文件中出错行组合索引列的长度
常见：

**create table test(test varcahr(255) primary key)charset=utf8;**

-- 成功

**create table test(test varcahr(256) primary key)charset=utf8;**

-- 失败

-- ERROR 1071（42000）:Specified key was too long; max key length is 767 bytes

###2、使用CDB5.5版本，myisam引擎不会被自动转换为innodb
