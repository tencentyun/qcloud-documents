
## 背景
腾讯云数据库 MySQL 默认支持 InnoDB 存储引擎，并在 5.6 及以上的版本中，不再支持 MyISAM 引擎和 Memory 引擎，不支持 MyISAM 引擎的主要原因，详见 [数据库存储引擎](https://cloud.tencent.com/document/product/236/9535)。
当数据库迁移或升级到云数据库 MySQL 5.6 及以上版本时，系统会自动将 MyISAM 引擎转换为 InnoDB 引擎。

由于 MyISAM 引擎会支持复合主键包含自增列，而引擎 InnoDB 引擎不支持，因此 MyISAM 引擎转换为 InnoDB 引擎后，创建表时会报错，报错信息为`ERROR 1075 (42000):Incorrect table definition;there can be only one auto column and it must be defined as a key`。


建议您通过为自增列创建索引的方式，实现 InnoDB 引擎的复合主键包含自增列语法。

## 复合主键包括自增列改写案例
- **原创建表的 SQL 语句：**
```
 create table t_complexkey
 ( 
 id int(8) AUTO_INCREMENT, 
 name varchar(19), 
 value varchar(10), 
 primary key (name,id)
 ) ENGINE=MyISAM DEFAULT CHARSET=utf8;
```
![](https://main.qcloudimg.com/raw/4ff00d33bc2d14b0a229dae99ab40b5d.png)
- **改写后的 SQL 语句：**
```
 create table t_complexkey
 ( 
 id int(8) AUTO_INCREMENT, 
 name varchar(19), 
 value varchar(10), 
 primary key (name,id),
 key key_id (id)
 ) ENGINE=MyISAM DEFAULT CHARSET=utf8;
```
![](https://main.qcloudimg.com/raw/34925406c1d5c36a7357f1735342907b.png)
- **查看表结构：**
```
show create table t_complexkey;
```
![](https://main.qcloudimg.com/raw/8509780314f54ecebe54283c579b49f8.png)

