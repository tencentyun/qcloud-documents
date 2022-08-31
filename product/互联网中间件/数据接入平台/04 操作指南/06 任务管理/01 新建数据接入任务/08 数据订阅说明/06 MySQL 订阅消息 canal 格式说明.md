


## 概述

使用数据接入平台订阅 MySQL 的变更操作时，可选多种消息格式，默认采用 debezium 格式，同时提供了兼容开源 canal 等格式的能力。本文介绍兼容 **canal** 的消息格式说明。

## canal 格式说明

| 兼容字段                                          | canal原生字段                            | 是否支持 |
| ------------------------------------------------- | ---------------------------------------- | -------- |
| id（默认值0）                                     | id（canal 生成的消息 ID）                  | 否       |
| database(数据库名)                                | database(数据库名)                       | 是       |
| table（表名）                                     | table（表名）                            | 是       |
| pkNames（默认值null）                             | pkNames（主键字段名）                    | 否       |
| isDdl（变更是否属于DDL）                          | isDdl（变更是否属于 DDL）                 | 是       |
| type（变更类型）                                  | type（变更类型）                         | 是       |
| es（binlog时间戳）                                | es（binlog 时间戳）                       | 是       |
| ts（connector 同步时间，仅 DML 支持，DDL 中与 ts 一致） | ts（connector 同步时间）                  | 是       |
| sql（DDL 执行语句）                                | sql（DDL 执行语句）                       | 是       |
| sqlType（暂不支持，默认值 null）                   | sqlType（与 mysqlType 对应的数据类型编号） | 否       |
| mysqlType（暂不支持，默认值 null）                 | mysqlType（mysql 中的字段类型）           | 否       |
| data（变更后的记录-全字段）                       | data（变更后的记录-全字段）              | 是       |
| old（变更前的记录--全字段）                       | old（变更前的记录--仅变更字段）          | 是       |



## DDL 格式

### create database

```json
{
    "data": null, 
    "database": "dip_test", 
    "es": 1655812326, 
    "id": 0, 
    "isDdl": true, 
    "mysqlType": null, 
    "old": null, 
    "pkNames": null, 
    "sql": "CREATE DATABASE `dip_test` CHARSET utf8mb4 COLLATE utf8mb4_0900_ai_ci", 
    "sqlType": null, 
    "table": "", 
    "ts": 1655812326, 
    "type": "QUERY"
}
```

### drop database

```json
{
    "data": null, 
    "database": "dip_test", 
    "es": 1655812326, 
    "id": 0, 
    "isDdl": true, 
    "mysqlType": null, 
    "old": null, 
    "pkNames": null, 
    "sql": "DROP DATABASE IF EXISTS `dip_test`", 
    "sqlType": null, 
    "table": "", 
    "ts": 1655812326, 
    "type": "QUERY"
}
```

### create table

```json
{
    "data": null, 
    "database": "dip_test", 
    "es": 1655812326, 
    "id": 0, 
    "isDdl": true, 
    "mysqlType": null, 
    "old": null, 
    "pkNames": null, 
    "sql": "CREATE TABLE `customers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `ix_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1041 DEFAULT CHARSET=utf8", 
    "sqlType": null, 
    "table": "customers", 
    "ts": 1655812326, 
    "type": "CREATE"
}
```

### alter table

```json
{
    "data": null, 
    "database": "test", 
    "es": 1655782153, 
    "id": 0, 
    "isDdl": true, 
    "mysqlType": null, 
    "old": null, 
    "pkNames": null, 
    "sql": "ALTER TABLE `user` ADD COLUMN `createtime` datetime NULL DEFAULT CURRENT_TIMESTAMP", 
    "sqlType": null, 
    "table": "user", 
    "ts": 1655782153, 
    "type": "ALTER"
}
```

### drop table

```json
{
    "data": null, 
    "database": "dip_test", 
    "es": 1655812326, 
    "id": 0, 
    "isDdl": true, 
    "mysqlType": null, 
    "old": null, 
    "pkNames": null, 
    "sql": "DROP TABLE IF EXISTS `dip_test`.`customers`", 
    "sqlType": null, 
    "table": "customers", 
    "ts": 1655812326, 
    "type": "ERASE"
}
```

### rename table

```json
{
    "data": null, 
    "database": "testDB", 
    "es": 1656300979748, 
    "id": 0, 
    "isDdl": true, 
    "mysqlType": null, 
    "old": null, 
    "pkNames": null, 
    "sql": "rename table test to t_test", 
    "sqlType": null, 
    "table": "t_test", 
    "ts": 1656300979748, 
    "type": "RENAME"
}
```

## DML 格式

### insert

```json
{
    "data": [
        {
            "last_name": "Kretchmar", 
            "id": 1004, 
            "first_name": "Anne", 
            "email": "annek@noanswer.org"
        }
    ], 
    "database": "inventory", 
    "es": 0, 
    "id": 0, 
    "isDdl": false, 
    "mysqlType": null, 
    "old": null, 
    "pkNames": null, 
    "sql": "", 
    "sqlType": null, 
    "table": "customers", 
    "ts": 1465491411815, 
    "type": "INSERT"
}
```

### update

```json
{
    "data": [
        {
            "last_name": "Kretchmar", 
            "id": 1004, 
            "first_name": "Anne Marie", 
            "email": "annek@noanswer.org"
        }
    ], 
    "database": "inventory", 
    "es": 1465581029100, 
    "id": 0, 
    "isDdl": false, 
    "mysqlType": null, 
    "old": [
        {
            "last_name": "Kretchmar", 
            "id": 1004, 
            "first_name": "Anne", 
            "email": "annek@noanswer.org"
        }
    ], 
    "pkNames": null, 
    "sql": "", 
    "sqlType": null, 
    "table": "customers", 
    "ts": 1465581029523, 
    "type": "UPDATE"
}
```

### delete

```json
{
    "data": null, 
    "database": "inventory", 
    "es": 1465581902300, 
    "id": 0, 
    "isDdl": false, 
    "mysqlType": null, 
    "old": [
        {
            "last_name": "Kretchmar", 
            "id": 1004, 
            "first_name": "Anne Marie", 
            "email": "annek@noanswer.org"
        }
    ], 
    "pkNames": null, 
    "sql": "", 
    "sqlType": null, 
    "table": "customers", 
    "ts": 1465581902461, 
    "type": "DELETE"
}
```



