## 使用 kettle 导入 TencentDB 的数据
Kettle 是一款开源的 ETL 工具，纯 Java 编写，可以在 Window、Linux、Unix 上运行，数据抽取高效稳定。

## 使用 DataX 工具导入 TencentDB 的数据
DataX 是一个开源的命令行工具，支持将 TencentDB 中全量或增量数据导入到 Snova 中。工具采用 Java 开发，用 JDBC 连接源数据库与目标数据库，可在 Windows 与 Linux 下运行，使用前需要安装 Java 运行环境。本文介绍的是由HashData公司修改过的[DataX](https://github.com/HashDataInc/DataX)，导入Snova效率更高，经测试可以达到每秒10W条以上。

以Mysql导入到Snova为例，配置文件如下：
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
                        "username": "****", 
                        "password": "****", 
                        "column": [
                            "*"
                        ], 
                        "splitPk": "id", 
                        "connection": [
                            {
                                "table": [
                                    "test1"
                                ], 
                                "jdbcUrl": [
                                    "jdbc:mysql://***:***/db1"
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
                        "preSql": [
                            "truncate table test1"
                        ], 
                        "postSql": [
                            "select count(*) from test2"
                        ], 
                        "segment_reject_limit": 0, 
                        "copy_queue_size": 2000, 
                        "num_copy_processor": 1, 
                        "num_copy_writer": 1, 
                        "connection": [
                            {
                                "jdbcUrl": "jdbc:postgresql://****:**/db1", 
                                "table": [
                                    "test1"
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

参数说明
1. writer需要选择gpdbwriter，尽管使用postgresqlwriter也能写入Snova，但是插入的效率很低
2. 参数具体含义和调优可以参考[DataX](https://github.com/HashDataInc/DataX)
