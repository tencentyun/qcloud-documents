
数据订阅功能帮助客户实时获取云数据库 MariaDB 以及分布式数据库 TDSQL 中的增量数据，客户能够根据自身业务的需求，自由地对实时增量数据进行处理。

## 功能列表
- 支持公有云云数据库 MariaDB 和分布式数据库 TDSQL 实例的数据订阅。
- 支持专有云云数据库 MariaDB 和分布式数据库 TDSQL 实例的数据订阅。

## 数据源类型
TencentDB for MariaDB、分布式数据库 TDSQL

## 消息格式
数据订阅功能对实例的 Binlog（row 格式）进行解析，并将 Binlog 事件封装成 json 格式的消息上传至 Kafka 集群。消息类型包括 DML 事件、GTID 事件、XID 事件、QUERY 事件。其中 DML 事件包括 insert、update、delete 事件，表征对数据行的更改；GTID 事件表征事务的开始；XID 事件表征事务的提交；QUERY 事件表征 DDL 语句。

**DML 消息格式如下：**
```
{
    "logtype":"mysqlbinlog",          //日志类型，取值唯一，为 mysqlbinlog
    "eventtype":23,                   //事件类型码，对应 mysql 中 binlog 事件类型码
  
    "eventtypestr":"insert",          /*事件类型字符串，包括 insert、update、delete、gtid、xid、query 事件。
		                                其中insert、update、delete 事件对应 DML 语句；tid 事件标识事务开始；
                                        xid 事件标识事务结束；query 事件标识 DDL 语句 */
    "db":"testdb",                    //库名
    "table":"testtable",              //表名
    "localip":"000.00.000.000",       //实例所在机器 IP
    "localport":0000,                 //实例端口
    "begintime":1511350073,           //事务开始时间，当前事件所在的事务的开始时间
    "gtid":"0-2670193178-726233561",  //GTID，当前事件所在事务的 gtid
    "event_index":"4",                //表征该事件在该事务中的序号  
    "where":[                         //where 字段，标识该行变更前的各个字段的值
    
    ],
    "field":[                         //field 字段，标识该行变更后的各个字段的值
        "1",
        "'name1'"
    ]
}
```

**GTID 消息格式如下：**
```
{                                    //GTID 事件表征一个事务的开始
    "logtype":"mysqlbinlog",
    "eventtype":33,
    "eventtypestr":"gtid",
    "db":"sysdb",
    "table":"statustableforhb",
    "localip":"10.231.23.241",
    "localport":8810,
    "begintime":1511419963,
    "gtid":"35be190b-d019-11e7-ab7a-a0423f32c225:469",
    "event_index":"1"
}
```

**XID 消息格式如下：**
```
{                                    //XID 事件表征事务已经提交
    "logtype":"mysqlbinlog",
    "eventtype":16,
    "eventtypestr":"xid",
    "db":"testsummer",
    "table":"test_table1",
    "localip":"10.231.23.241",
    "localport":8810,
    "begintime":1511419963,
    "gtid":"35be190b-d019-11e7-ab7a-a0423f32c225:469",
    "event_index":"5",
    "xid":"11866"
}
```

**QUERY 消息格式如下：**
```
{
    "logtype":"mysqlbinlog",                          
    "eventtype":2,
    "eventtypestr":"query",         //QUERY 事件对应 DDL 语句
    "db":"testsummer",
    "table":"statustableforhb",
    "localip":"10.231.23.241",
    "localport":8810,
    "begintime":1511419941,
    "gtid":"35be190b-d019-11e7-ab7a-a0423f32c225:452",
    "event_index":"2",
    "sql":"create table test_table1 (id int primary key,name varchar(20))"
}
```


## 订阅方式
客户通过获取存储在 Kafka 集群的消息事件来实时获取数据。通过腾讯云提供的数据订阅 API 来实时获取消息并进行处理。
