## 1. 接口描述

接口：GetMonitorData

获取云产品的监控数据。传入产品的命名空间、对象维度描述和监控指标即可获得相应的监控数据。 

接口调用频率限制为：50次/秒，500次/分钟。 单请求最多可支持批量拉取10个实例的监控数据，单请求的数据点数限制为1440个。

若您需要调用的指标、对象较多，可能存在因限频出现拉取失败的情况，建议尽量将请求按时间维度均摊。

查询云数据库（MySQL）产品监控数据，入参取值如下：
Namespace：qce/cdb
Dimensions.N.uInstanceId：cdb实例id

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为GetMonitorData。

### 2.1输入参数

| 参数名称         | 是否必选 | 类型              | 描述                                       |
| ------------ | ---- | --------------- | ---------------------------------------- |
| Namespace    | 是    | String          | 命名空间，每个云产品会有一个命名空间                       |
| MetricName   | 是    | String          | 指标名称，具体名称见2.2                            |
| Period       | 否    | Integer         | 监控统计周期。默认为取值为300，单位为s                    |
| StartTime    | 否    | Timestamp       | 起始时间，如"2016-01-01 10:25:00"。 默认时间为当天的”00:00:00” |
| EndTime      | 否    | Timestamp       | 结束时间，默认为当前时间。 endTime不能小于startTime       |
| Dimensions.N | 是    | Array of String | 实例对象的维度组合                                |

### 2.2 指标名称

每个指标的统计粒度（Period）可取值不一定相同，可通过[DescribeBaseMetrics](https://cloud.tencent.com/document/api/248/15679)接口获取每个接口支持的统计粒度。

| 指标名称                             | 含义             | 单位     |
| -------------------------------- | -------------- | ------ |
| slow_queries                     | 慢查询数           | 次/分    |
| max_connections                  | 最大连接数          | 个      |
| select_scan                      | 全表扫描数          | 次/秒    |
| select_count                     | 查询数            | 次/秒    |
| com_update                       | 更新数            | 次/秒    |
| com_delete                       | 删除数            | 次/秒    |
| com_insert                       | 插入数            | 次/秒    |
| com_replace                      | 覆盖数            | 次/秒    |
| queries                          | 总请求数           | 次/秒    |
| threads_connected                | 当前打开连接数        | 个      |
| real_capacity                    | 磁盘使用空间         | MB     |
| capacity                         | 磁盘占用空间         | MB     |
| bytes_sent                       | 内网出流量          | Byte/秒 |
| bytes_received                   | 内网入流量          | Byte/秒 |
| qcache_use_rate                  | 缓存使用率          | %      |
| qcache_hit_rate                  | 缓存命中率          | %      |
| table_locks_waited               | 等待表锁次数         | 次/秒    |
| created_tmp_tables               | 临时表数量          | 次/秒    |
| innodb_cache_use_rate            | innodb缓存使用率    | %      |
| innodb_cache_hit_rate            | innodb缓存命中率    | %      |
| innodb_os_file_reads             | innodb读磁盘数量    | 次/秒    |
| innodb_os_file_writes            | innodb写磁盘数量    | 次/秒    |
| innodb_os_fsyncs                 | innodb fsync数量 | 次/秒    |
| key_cache_use_rate               | myisam缓存使用率    | %      |
| key_cache_hit_rate               | myisam缓存命中率    | %      |
| volume_rate                      | 容量使用率          | %      |
| query_rate                       | 查询使用率          | %      |
| qps                              | 每秒执行操作数        | 次/秒    |
| tps                              | 每秒执行事务数        | 次/秒    |
| cpu_use_rate                     | CPU占比          | %      |
| memory_use                       | 内存占用           | MB     |
| key_write_requests               | 数据块写入键缓冲次数     | 次/秒    |
| key_writes                       | 数据块写入磁盘次数      | 次/秒    |
| com_commit                       | 提交数            | 次/秒    |
| handler_commit                   | 内部提交数          | 次/秒    |
| innodb_rows_read                 | InnoDB行读取量     | 次/秒    |
| innodb_row_lock_time_avg         | InnoDB平均获取行锁时间 | 毫秒     |
| threads_created                  | 已创建的线程数        | 个      |
| opened_tables                    | 已经打开的表数        | 个      |
| threads_running                  | 运行的线程数         | 个      |
| innodb_data_reads                | InnoDB总读取量     | 次/秒    |
| com_rollback                     | 回滚数            | 次/秒    |
| key_blocks_unused                | 键缓存内未使用的块数量    | 个      |
| innodb_data_writes               | InnoDB总写入量     | 次/秒    |
| innodb_buffer_pool_pages_free    | InnoDB空页数      | 个      |
| innodb_rows_inserted             | InnoDB行插入量     | 次/秒    |
| created_tmp_files                | 临时文件数量         | 次/秒    |
| innodb_data_read                 | InnoDB读取量      | Byte/秒 |
| innodb_row_lock_waits            | InnoDB等待行锁次数   | 次/秒    |
| innodb_buffer_pool_read_requests | InnoDB逻辑读      | 次/秒    |
| handler_rollback                 | 内部回滚数          | 次/秒    |
| master_slave_sync_distance       | 主从不同步距离        | MB     |
| handler_read_rnd_next            | 读下一行请求数        | 次/秒    |
| innodb_rows_updated              | InnoDB行更新量     | 次/秒    |
| innodb_rows_deleted              | InnoDB行删除量     | 次/秒    |
| innodb_buffer_pool_pages_total   | InnoDB空页数      | 个      |
| key_blocks_used                  | 键缓存内使用的块数量     | 个      |
| innodb_data_written              | InnoDB写入量      | Byte/秒 |
| key_read_requests                | 键缓存读取数据块次数     | 次/秒    |
| innodb_buffer_pool_reads         | InnoDB物理读      | 次/秒    |
| created_tmp_disk_tables          | 磁盘临时表数量        | 次/秒    |
| key_reads                        | 硬盘读取数据块次数      | 次/秒    |


## 3. 输出参数

| 参数名称       | 类型             | 描述                                       |
| ---------- | -------------- | ---------------------------------------- |
| MetricName | String         | 监控指标                                     |
| StartTime  | Timestamp      | 数据点起始时间                                  |
| EndTime    | Timestamp      | 数据点结束时间                                  |
| Period     | Integer        | 数据统计周期                                   |
| DataPoints | Array of Float | 监控数据列表                                   |
| RequestId  | String         | 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。 |

## 4. 错误码表

| 错误代码             | 描述                 |
| ---------------- | ------------------ |
| InternalError    | 内部错误               |
| InvalidParameter | 参数错误（包括参数格式、类型等错误） |

## 5. 示例

## 示例1 拉取单个实例监控数据示例

### 场景描述

拉取某个云数据库MySQL某段时间内统计周期为5分钟的慢查询数监控数据

### 请求参数

```
https://monitor.tencentcloudapi.com/?Action=GetMonitorData
&Namespace=qce/cdb
&MetricName=slow_queries
&Period=300
&StartTime=2018-04-16 20:00:00
&EndTime=2018-04-16 20:05:00
&Dimensions.0.uInstanceId=cdb-e242adzf
&<公共请求参数>
```

### 返回参数

```
{
  "Response": {
    "DataPoints": [
      {
        "Dimensions": {
          "uInstanceId": "cdb-e242adzf"
        },
        "Points": [
          0,
          0
        ]
      }
    ],
    "EndTime": "2018-04-16 20:05:00",
    "MetricName": "slow_queries",
    "Period": 300,
    "RequestId": "c9df44f6-953d-4a19-a240-c1262511abe7",
    "StartTime": "2018-04-16 20:00:00"
  }
}
```

## 示例2 拉取多个实例监控数据示例

### 场景描述

拉取三个云数据库MySQL某段时间内统计周期为5分钟的慢查询数监控数据

### 请求参数

```
https://monitor.tencentcloudapi.com/?Action=GetMonitorData
&Namespace=qce/cdb
&MetricName=slow_queries
&Period=300
&StartTime=2018-04-16 20:00:00
&EndTime=2018-04-16 20:05:00
&Dimensions.0.uInstanceId=cdb-aaaaaa
&Dimensions.1.uInstanceId=cdb-bbbbb
&Dimensions.2.uInstanceId=cdb-ccccc
&<公共请求参数>
```

### 返回参数

```
{
  "Response": {
    "DataPoints": [
      {
        "Dimensions": {
          "uInstanceId": "cdb-aaaaaa"
        },
        "Points": [
          0,
          0
        ]
      },
      {
        "Dimensions": {
          "uInstanceId": "cdb-bbbbb"
        },
        "Points": [
          0,
          0
        ]
      },
      {
        "Dimensions": {
          "uInstanceId": "cdb-ccccc"
        },
        "Points": [
          0,
          0
        ]
      }
    ],
    "EndTime": "2018-04-16 20:05:00",
    "MetricName": "slow_queries",
    "Period": 300,
    "RequestId": "c9df44f6-953d-4a19-a240-c1262511abe7",
    "StartTime": "2018-04-16 20:00:00"
  }
}
```