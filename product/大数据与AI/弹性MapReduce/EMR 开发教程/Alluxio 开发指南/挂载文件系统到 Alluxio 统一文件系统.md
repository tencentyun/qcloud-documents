## 背景

Alluxio 提供了统一命名空间机制，允许将其他文件系统挂载到 Alluxio 的文件系统中。
该机制允许上层应用使用统一的命名空间，访问分散在不同系统中的数据。

## 操作

命令`bin/alluxio fs mount <alluxio-path> <source-path>`

示例1：将 COS 某 bucket 挂载到 alluxio 目录中。

```
bin/alluxio fs mount --option fs.cos.access.key=<COS_SECRET_ID> \
    --option fs.cos.secret.key=<COS_SECRET_KEY> \
    --option fs.cos.region=<COS_REGION> \
    --option fs.cos.app.id=<COS_APP_ID> \
    /cos cos://<COS_BUCKET>/<COS_DATA>/
```

其中，--options 中配置 COS 的配置。

| 配置名称          | 解释                                   |
| ----------------- | -------------------------------------- |
| fs.cos.access.key | cos scecret id                         |
| fs.cos.secret.key | cos secret key                         |
| fs.cos.region     | cos region 名称，例如 ```ap-beijing``` |
| fs.cos.app.id     | 用户 APPID                              |
| COS_BUCKET        | COS BUCKET 名称                         |
| COS_DATA          | COS 目录，可以是根目录 ```/```         |

该命令，将 COS 的目录（通过 cos://bucket/xxx 指定）挂载到 alluxio 的 /cos 目录下。 

示例2：将 HDFS 某目录挂载到 alluxio 目录中。

`bin/alluxio fs mount /hdfs hdfs://data`

该命令将 HDFS 的 /data 目录挂载到 alluxio 的 /hdfs 子目录下。

挂载成功后，通过 alluxio fs ls 命令，查看挂载内容。

