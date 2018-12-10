## 创建仓库
您可以通过如下命令创建仓库：
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
- <1> 腾讯云账号 APPID   
- <2><3> 腾讯云 API 密钥 SecretId、SecretKey
- <4> COS Bucket 名字
- <5> COS Bucket 地域，建议与 ES 集群同地域  
- <6> 备份目录   

## 列出仓库信息
您可通过如下命令获取仓库信息：
```
GET _snapshot
```

也可以使用`GET _snapshot/my_cos_backup`获取指定的仓库信息。


## 创建快照备份

### 备份所有索引
将 ES 集群内所有索引备份到`my_cos_backup`仓库下，并命名为`snapshot_1`。
```
PUT _snapshot/my_cos_backup/snapshot_1
```
这个命令会立刻返回，并在后台异步执行直到结束。   
如果希望创建快照命令阻塞执行，可以添加`wait_for_completion`参数：
```
PUT _snapshot/my_cos_backup/snapshot_1?wait_for_completion=true
```
>**注意：**
>命令执行的时间与索引大小相关。

### 备份指定索引
您可以在创建快照的时候指定要备份的索引：
```
PUT _snapshot/my_cos_backup/snapshot_2
{
    "indices": "index_1,index_2"  <1>
}
```
>**注意：**
>参数 indices 的值为多个索引的时候，需要用`,`隔开且不能有空格。

## 查询快照
查询单个快照信息：
```
GET _snapshot/my_cos_backup/snapshot_1
```
该命令会返回快照的相关信息：
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
>**注意：**
>如果存在还未完成的快照，删除快照命令依旧会执行，并取消未完成快照的创建进程。

## 从快照恢复
将快照中备份的所有索引都恢复到 ES 集群中：
```
POST _snapshot/my_cos_backup/snapshot_1/_restore
```
如果 snapshot_1 包括 5 个索引，则这 5 个索引都会被恢复到 ES 集群中。   
您还可以使用附加的选项对索引进行重命名。该选项允许您通过模式匹配索引名称，并通过恢复进程提供一个新名称。如果您想在不替换现有数据的前提下，恢复旧数据来验证内容或进行其他操作，则可以使用该选项。
从快照里恢复单个索引并提供一个替换的名称：
```
POST /_snapshot/my_cos_backup/snapshot_1/_restore
{
    "indices": "index_1", <1>
    "rename_pattern": "index_(.+)", <2>
    "rename_replacement": "restored_index_$1" <3>
}
```
- <1> 只恢复 index_1 索引，忽略快照中存在的其他索引。
- <2> 查找所提供的模式能匹配上的正在恢复的索引。
- <3> 将匹配的索引重命名成替代的模式。   

## 查询快照恢复状态
您可以通过执行`_recovery`命令，查看快照恢复的状态并监控快照恢复的进度。   
您可以在恢复的指定索引中单独调用下述 API ：
```
GET index_1/_recovery
```
该命令会返回指定索引各分片的恢复状况：
```
{
    "sonested": {
        "shards": [
            {
                "id": 1,
                "type": "SNAPSHOT",     <1>
                "stage": "INDEX",
                "primary": true,
                "start_time_in_millis": 1525766148333,
                "total_time_in_millis": 8718,
                "source": {     <2>
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
                        "percent": "15.2%"      <3>
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
            }
        ]
    }
}
```
- <1> type 字段描述了恢复的本质；该分片是在从一个快照恢复。
- <2> source 哈希描述了作为恢复来源的特定快照和仓库。
- <3> percent 字段描述恢复的状态。该特定分片目前已经恢复了 94% 的文件；它就快完成了。   

输出会列出所有目前正在恢复的索引，以及这些索引里的所有分片。每个分片里会有启动/停止时间、持续时间、恢复百分比、传输字节数等统计值。

## 取消快照恢复
```
DELETE /restored_index_1
```
如果 restored\_index\_1 正在恢复中，则该删除命令会停止恢复，同时删除所有已经恢复到集群里的数据。
