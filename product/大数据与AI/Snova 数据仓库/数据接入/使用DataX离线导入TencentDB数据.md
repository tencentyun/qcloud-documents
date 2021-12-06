DataX 是一个开源的命令行工具，支持将 TencentDB 中全量或增量数据导入到云数据仓库 PostgreSQL 中。工具采用 Java 开发，用 JDBC 连接源数据库与目标数据库，可在 Windows 与 Linux 下运行，使用前需安装 Java 运行环境。

**DataX 工具安装：**
1. 在 [DataX 官网](https://github.com/HashDataInc/DataX) 下载源码进行编译。
2. 直接使用已编译好的版本，[datax-v1.0.4-hashdata.tar.gz](https://packagedown-online-1256722404.cos.ap-guangzhou.myqcloud.com/datax/datax-v1.0.4-hashdata.tar.gz)。

下文主要介绍由 HashData 公司修改过的 [DataX](https://github.com/HashDataInc/DataX)，其导入云数据仓库 PostgreSQL 效率更高，经测试可达到每秒10W条以上。以 MySQL 导入到云数据仓库 PostgreSQL 为例，配置文件如下：
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
                                    "jdbc:mysql://***:***/db1?serverTimezone=Asia/Shanghai"
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

**参数说明：**
1. writer 需选择 gpdbwriter。使用 postgresqlwriter 也可写入云数据仓库 PostgreSQL，但插入效率会很低。
2. 参数具体含义和调优可以参考 [DataX](https://github.com/HashDataInc/DataX)。
3. `mysqlreader` 的 jdbc url 建议加上 `serverTimezone=Asia/Shanghai` 参数，避免时区问题导致的数据不一致。


