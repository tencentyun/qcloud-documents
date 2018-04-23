## CDB 导入数据报错：Specified key was too long
### 一、报错原因
	 ERROR 1071 (42000): Specified key was too long; max key length is 767 bytes
客户通过 CVM 的命令行向 CDB 导入XXXX.sql文件时，CDB 返回Specified key was too long的报错。

对于报错信息“ERROR 1071 (42000): Specified key was too long; max key length is 767 bytes”，其实意思就是“索引字段长度太长，超过了767bytes”。

①innodb存储引擎，多列索引的长度限制如下：

  **每个列的长度不能大于767 bytes；所有组成索引列的长度和不能大于3072 bytes**

② myisam存储引擎，多列索引长度限制如下：

  **每个列的长度不能大于1000 bytes，所有组成索引列的长度和不能大于1000 bytes**

	TIPS：768/2=384个双字节 或者767/3=255个三字节的字段（GBK是双字节的，UTF8是三字节的，UTF8MB4是四字节的）

为什么在自建的数据库上是 OK 的，但是把数据导入 CDB 后就报Specified key was too long错误呢？

在 CDB5.6 及其以上版本，所有myisam表都会被自动转换为 innodb，所以在自建数据库上有超过 767 bytes 的组合索引列，但是由于在自建库上 myisam 存储引擎，同样的建表语句在自建库上运行没问题，但是在 CDB5.6 版本以上就会有问题。

## 二、解决方案
### 1、修改备份文件中出错行组合索引列的长度
常见：

**create table test(test varcahr(255) primary key)charset=utf8;**

--成功

**create table test(test varcahr(256) primary key)charset=utf8;**

--失败

--ERROR 1071（42000）:Specified key was too long; max key length is 767 bytes

### 2、控制台调整innodb_large_prefix参数大小
### 3、使用前缀索引

## 报错原因
	 ERROR 1071 (42000): Specified key was too long; max key length is 767 bytes
客户通过 CVM 的命令行向 CDB 导入 XXXX.sql 文件时，CDB 返回 Specified key was too long 的报错。

对于报错信息“ERROR 1071 (42000): Specified key was too long; max key length is 767 bytes”，其实意思就是“索引字段长度太长，超过了 767 bytes”。

① innodb 存储引擎，多列索引的长度限制如下：

  **每个列的长度不能大于 767 bytes；所有组成索引列的长度和不能大于 3072 bytes**

② myisam 存储引擎，多列索引长度限制如下：

  **每个列的长度不能大于 1000 bytes，所有组成索引列的长度和不能大于 1000 bytes**
```
TIPS：768/2=384 个双字节 或者 767/3=255 个三字节的字段（GBK 是双字节的，UTF8 是三字节的，UTF8MB4 是四字节的）
```
为什么在自建的数据库上是 OK 的，但是把数据导入 CDB 后就报 Specified key was too long 错误呢？

在 CDB5.6 及其以上版本，所有 myisam 表都会被自动转换为 innodb，所以在自建数据库上有超过 767 bytes 的组合索引列，但是由于在自建库上 myisam 存储引擎，同样的建表语句在自建库上运行没问题，但是在 CDB5.6 版本以上就会有问题。

## 解决方案
### 1. 修改备份文件中出错行组合索引列的长度
常见：

**create table test(test varcahr(255) primary key)charset=utf8;**

-- 成功

**create table test(test varcahr(256) primary key)charset=utf8;**

-- 失败

-- ERROR 1071（42000）:Specified key was too long; max key length is 767 bytes

### 2. 使用 CDB5.5 版本，myisam 引擎不会被自动转换为 innodb
