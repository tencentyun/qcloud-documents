## 背景
Alluxio 提供了统一命名空间机制，允许将其他文件系统挂载到 Alluxio 的文件系统中。该机制允许上层应用使用统一的命名空间，访问分散在不同系统中的数据。

## 操作
```
bin/alluxio fs mount <alluxio-path> <source-path>
```

**示例1：将 COS 中某个 bucket 挂载到 alluxio 目录中。**
```
bin/alluxio fs mount --option fs.cos.access.key=<COS_SECRET_ID> \
    --option fs.cos.secret.key=<COS_SECRET_KEY> \
    --option fs.cos.region=<COS_REGION> \
    --option fs.cos.app.id=<COS_APP_ID> \
    /cos cos://<COS_BUCKET>/
```

其中，--options 中配置 COS 的配置。

| 配置名称          | 解释                                   |
| ----------------- | -------------------------------------- |
| fs.cos.access.key | cos scecret id                         |
| fs.cos.secret.key | cos secret key                         |
| fs.cos.region     | cos region 名称，例如 `ap-beijing` |
| fs.cos.app.id     | 用户 AppID                              |
| COS_BUCKET        | COS BUCKET 名称。**只要名称，不要带 AppID 后缀**                         |

该命令，将 COS 的目录（通过 `cos://bucket/xxx` 指定）挂载到 alluxio 的 `/cos` 目录下。 

**示例2：将 HDFS 某目录挂载到 alluxio 目录中。**
```
bin/alluxio fs mount /hdfs hdfs://data
```
该命令将 HDFS 的 `/data` 目录挂载到 alluxio 的 `/hdfs` 子目录下。

挂载成功后，通过 `alluxio fs ls` 命令，查看挂载内容。

**示例3：将 CHDFS 通过 mount 挂载到 Alluxio**
>?只有 EMR2.5.0 + alluxio2.3.0+ 以上才支持。
>
```
alluxio fs mount   \ 
 --option alluxio.underfs.hdfs.configuration=/usr/local/service/hadoop/etc/hadoop/core-site.xml  \
/chdfs ofs://f4modr7kmvw-wMqw.chdfs.ap-chongqing.myqcloud.com
```
