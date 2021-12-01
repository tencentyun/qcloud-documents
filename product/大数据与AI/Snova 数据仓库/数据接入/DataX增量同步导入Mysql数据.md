本文主要介绍使用 HashData 公司修改过的 [DataX](https://github.com/HashDataInc/DataX)，将其 MySQL 中的数据增量同步到云数据仓库 PostgreSQL。

使用 DataX 将 MySQL 中的数据增量同步到云数据仓库 PostgreSQL 中，具体步骤如下：
1. 从本地文件读取上次同步成功之后的最大时间 MaxTime（初始同步时，可以结合业务选取指定一个初始时间值）。
2. 将 MaxTime 作为本次同步时间 LastTime（增量同步的下限），将当前时间 CurTime 作为同步增量的上限。
3. 修改 datax.json 配置，指定同步表的时间区间（SQL 的 where 条件）为：`[LastTime, CurTime)`。
4. 执行 datax 同步，同步成功后，将 CurTime 写入本地文件供下次同步使用。
5. 循环执行1 - 4实现多次增量同步。

datax.json 配置文件实例如下：
```
{
    "job": {
        "setting": {
            "speed": {
                "channel": 3, 
                "byte": 1048576, 
                "record": 1000
            }, 
            "errorLimit": {
                "record": 2, 
                "percentage": 0.02
            }
        }, 
        "content": [
            {
                "reader": {
                    "name": "mysqlreader", 
                    "parameter": {
                        "username": "******", 
                        "password": "******", 
                        "connection": [
                            {
                                "jdbcUrl": [
                                    "jdbc:mysql://***:***/test?serverTimezone=Asia/Shanghai"
                                ],
                                "querySql": [
                                    "select * from cdw_test_table where updateTime >= '${lastTime}' and updateTime < '${currentTime}'"
                                ]
                            }
                        ]
                    }
                }, 
                "writer": {
                    "name": "gpdbwriter", 
                    "parameter": {
                        "username": "******", 
                        "password": "******", 
                        "column": [
                                 "*"
                        ],
                        "segment_reject_limit": 0, 
                        "copy_queue_size": 2000, 
                        "num_copy_processor": 1, 
                        "num_copy_writer": 1, 
                        "connection": [
                            {
                                "jdbcUrl": "jdbc:postgresql://***:***/***", 
                                "table": [
                                    "ods_cdw_test_table"
                                ]
                            }
                        ]
                    }
                }
            }
        ]
    }
}
```

