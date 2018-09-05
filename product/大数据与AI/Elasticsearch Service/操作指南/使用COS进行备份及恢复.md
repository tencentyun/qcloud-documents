## 创建仓库

```
PUT _snapshot/my_cos_backup
{
    "type": "cos",
    "settings": {
        "app_id": "xxxxxxx", <1>
        "access_key_id": "xxxxxx", <2>
        "access_key_secret": "xxxxxxx", <3>
        "bucket": "xxxxxx",  <4>
        "region": "ap-guangzhou", <5>
        "compress": true,
        "chunk_size": "500mb",
        "base_path": "/", <6>
    }
}
```
* <1> 腾讯云账号 APPID   
* <2><3> 腾讯云 API 密钥 SecretId，SecretKey
* <4> COS Bucket 名字
* <5> COS Bucket 地域，建议与 ES 集群同地域  
* <6> 备份目录   

## 列出仓库信息
您可通过以下两种方式获取仓库信息：
- 使用`GET _snapshot`获取仓库信息。

- 使用`GET _snapshot/my_cos_backup`获取指定的仓库信息。


## 创建快照备份

### 备份所有索引

```
PUT _snapshot/my_cos_backup/snapshot_1
```
这个命令会将ES集群内所有索引备份到```my_cos_backup```仓库下，并命名为```snapshot_1```。这个命令会立刻返回，并在后台异步执行直到结束。   
如果希望创建快照命令阻塞执行，可以添加```wait_for_completion```参数：
```
PUT _snapshot/my_cos_backup/snapshot_1?wait_for_completion=true
```
>**注意：**命令执行的时间与索引大小相关。

### 备份指定索引
可以在创建快照的时候指定要备份哪些索引：
```
PUT _snapshot/my_cos_backup/snapshot_2
{
    "indices": "index_1,index_2"  <1>
}
```
>**注意：**参数 indices 的值为多个索引的时候，需要用逗号`,`隔开且不能有空格。

## 查询快照

查询单个快照信息：
```
GET _snapshot/my_cos_backup/snapshot_1
```
这个命令会返回快照的相关信息：
```
{
    "snapshots": [
        {
            "snapshot": "snapshot_1",
            "uuid": "zUSugNiGR-OzH0CCcgcLmQ",
            "version_id": 5060499,
            "version": "5.6.4",
            "indices": [
                "index_1",
                "index_2"
            ],
            "state": "SUCCESS",
            "start_time": "2018-05-04T11:44:15.975Z",
            "start_time_in_millis": 1525434255975,
            "end_time": "2018-05-04T11:45:29.395Z",
            "end_time_in_millis": 1525434329395,
            "duration_in_millis": 73420,
            "failures": [],
            "shards": {
                "total": 3,
                "failed": 0,
                "successful": 3
            }
        }
    ]
}
```

## 删除快照
删除指定的快照：
```
DELETE _snapshot/my_cos_backup/snapshot_1
```
如果有还未完成的快照，删除快照命令依旧会执行，并取消快照创建进程。

## 从快照恢复
```
POST _snapshot/my_cos_backup/snapshot_1/_restore
```

执行快照恢复命令会把把这个快照里的备份的所有索引都恢复到ES集群中。如果 snapshot_1 包括五个索引，这五个都会被恢复到我们集群里。   
还有附加的选项用来重命名索引。这个选项允许您通过模式匹配索引名称，然后通过恢复进程提供一个新名称。如果您想在不替换现有数据的前提下，恢复老数据来验证内容，或者做其他处理，这个选项很有用。让我们从快照里恢复单个索引并提供一个替换的名称：
```
POST /_snapshot/my_cos_backup/snapshot_1/_restore
{
    "indices": "index_1", <1>
    "rename_pattern": "index_(.+)", <2>
    "rename_replacement": "restored_index_1" <3>
}
```
* <1> 只恢复 index_1 索引，忽略快照中存在的其余索引。
* <2> 查找所提供的模式能匹配上的正在恢复的索引。
* <3> 然后把它们重命名成替代的模式。   

## 查询快照恢复状态
通过执行`_recovery`命令，可以查看快照恢复的状态，监控快照恢复的进度。   
这个 API 可以为您在恢复的指定索引单独调用：
```
GET index_1/_recovery
```
这个命令会返回指定索引各分片的恢复状况：
```
{
    "sonested": {
        "shards": [
            {
                "id": 1,
                "type": "SNAPSHOT",
                "stage": "INDEX",
                "primary": true,
                "start_time_in_millis": 1525766148333,
                "total_time_in_millis": 8718,
                "source": {
                    "repository": "my_cos_backup",
                    "snapshot": "snapshot",
                    "version": "5.6.4",
                    "index": "index_1"
                },
                "target": {
                    "id": "TlzmxJHwSqyv4rhyQfRkow",
                    "host": "10.0.0.6",
                    "transport_address": "10.0.0.6:9300",
                    "ip": "10.0.0.6",
                    "name": "node-1"
                },
                "index": {
                    "size": {
                        "total_in_bytes": 1374967573,
                        "reused_in_bytes": 0,
                        "recovered_in_bytes": 160467084,
                        "percent": "11.7%"
                    },
                    "files": {
                        "total": 132,
                        "reused": 0,
                        "recovered": 20,
                        "percent": "15.2%"
                    },
                    "total_time_in_millis": 8716,
                    "source_throttle_time_in_millis": 0,
                    "target_throttle_time_in_millis": 0
                },
                "translog": {
                    "recovered": 0,
                    "total": 0,
                    "percent": "100.0%",
                    "total_on_start": 0,
                    "total_time_in_millis": 0
                },
                "verify_index": {
                    "check_index_time_in_millis": 0,
                    "total_time_in_millis": 0
                }
            },
            {
                "id": 0,
                "type": "SNAPSHOT",
                "stage": "INDEX",
                "primary": true,
                "start_time_in_millis": 1525766148296,
                "total_time_in_millis": 8748,
                "source": {
                    "repository": "my_cos_backup",
                    "snapshot": "snapshot",
                    "version": "5.6.4",
                    "index": "index_1"
                },
                "target": {
                    "id": "rOupcFi7Rn-kc2PzEoRMMQ",
                    "host": "10.0.0.15",
                    "transport_address": "10.0.0.15:9300",
                    "ip": "10.0.0.15",
                    "name": "node-3"
                },
                "index": {
                    "size": {
                        "total_in_bytes": 1362775831,
                        "reused_in_bytes": 0,
                        "recovered_in_bytes": 155162131,
                        "percent": "11.4%"
                    },
                    "files": {
                        "total": 125,
                        "reused": 0,
                        "recovered": 27,
                        "percent": "21.6%"
                    },
                    "total_time_in_millis": 8736,
                    "source_throttle_time_in_millis": 0,
                    "target_throttle_time_in_millis": 0
                },
                "translog": {
                    "recovered": 0,
                    "total": 0,
                    "percent": "100.0%",
                    "total_on_start": 0,
                    "total_time_in_millis": 0
                },
                "verify_index": {
                    "check_index_time_in_millis": 0,
                    "total_time_in_millis": 0
                }
            }
        ]
    }
}
```
* <1> type 字段告诉您恢复的本质；这个分片是在从一个快照恢复。
* <2> source 哈希描述了作为恢复来源的特定快照和仓库。
* <3> percent 字段让您对恢复的状态有个概念。这个特定分片目前已经恢复了 94% 的文件；它就快完成了。   

输出会列出所有目前正在经历恢复的索引，然后列出这些索引里的所有分片。每个分片里会有启动/停止时间、持续时间、恢复百分比、传输字节数等统计值。

## 取消快照恢复
```
DELETE /restored_index_1
```
如果 restored\_index\_1 正在恢复中，这个删除命令会停止恢复，同时删除所有已经恢复到集群里的数据。
