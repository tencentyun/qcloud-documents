

## 概述

使用数据接入平台订阅 MySQL 的变更操作时，可选多种消息格式，默认采用 debezium 格式，同时提供了兼容其他消息格式的能力。本文介绍兼容 **官方自定义格式** 的消息格式说明。

## 官方格式一说明

官方格式一目前仅支持 DML 消息，DDL 消息格式与 canal 格式一致。

| 字段名称        | 字段说明                                                     |
| --------------- | ------------------------------------------------------------ |
| BINLOG_NAME     | binlog 日志文件名称                                           |
| BINLOG_POS      | binlog 日志的 pos 位置                                          |
| DATABASE        | 数据库名称                                                   |
| EVENT_SERVER_ID | 暂时默认为 null                                               |
| GLOBAL_ID       | 如果开启 GTID，则为 GTID 信息                                   |
| GROUP_ID        | 暂时默认为 null                                               |
| NEW_VALUES      | type=U，则为更新后的行信息，格式为 json<br/>type=D，则为null<br/>type=I，则为新插入的行信息，格式为 json |
| OLD_VALUES      | type=U，则为更新前的行信息，格式为 json<br/>type=D，则为删除的行信息，格式为 json<br/>type =I, 则为 null |
| TABLE           | 表名                                                         |
| TIME            | 日志生成时间                                                 |
| TYPE            | 日志类型。U:update，D:delete，l:insert                       |

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

## drop database

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
    "BINLOG_NAME": "mysql-bin.000003", 
    "BINLOG_POS": 154, 
    "DATABASE": "inventory", 
    "EVENT_SERVER_ID": null, 
    "GLOBAL_ID": null, 
    "GROUP_ID": null, 
    "NEW_VALUES": {
        "last_name": "Kretchmar", 
        "id": "1004", 
        "first_name": "Anne", 
        "email": "annek@noanswer.org"
    }, 
    "OLD_VALUES": null, 
    "TABLE": "customers", 
    "TIME": "19700101080000", 
    "TYPE": "I"
}
```

### update

```json
{
    "BINLOG_NAME": "mysql-bin.000003", 
    "BINLOG_POS": 484, 
    "DATABASE": "inventory", 
    "EVENT_SERVER_ID": null, 
    "GLOBAL_ID": null, 
    "GROUP_ID": null, 
    "NEW_VALUES": {
        "last_name": "Kretchmar", 
        "id": "1004", 
        "first_name": "Anne Marie", 
        "email": "annek@noanswer.org"
    }, 
    "OLD_VALUES": {
        "last_name": "Kretchmar", 
        "id": "1004", 
        "first_name": "Anne", 
        "email": "annek@noanswer.org"
    }, 
    "TABLE": "customers", 
    "TIME": "20160611015029", 
    "TYPE": "U"
}
```

### delete

```json
{
    "BINLOG_NAME": "mysql-bin.000003", 
    "BINLOG_POS": 805, 
    "DATABASE": "inventory", 
    "EVENT_SERVER_ID": null, 
    "GLOBAL_ID": null, 
    "GROUP_ID": null, 
    "NEW_VALUES": null, 
    "OLD_VALUES": {
        "last_name": "Kretchmar", 
        "id": "1004", 
        "first_name": "Anne Marie", 
        "email": "annek@noanswer.org"
    }, 
    "TABLE": "customers", 
    "TIME": "20160611020502", 
    "TYPE": "D"
}
```

