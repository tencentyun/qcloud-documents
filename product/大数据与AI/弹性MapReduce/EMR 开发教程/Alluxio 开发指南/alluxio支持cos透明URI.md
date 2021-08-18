Alluxio 用户通常具有通过现有应用程序访问其底层存储系统（Under-FileSystem），将 Alluxio 添加到现有的生态系统中需求，但现有应用程序必须更改是需要在应用程序使用 Alluxio 的 URI。透明 URI 功能允许用户访问现有存储系统，且无需在应用程序级别更改 URI。

## 支持版本与配置 URI
1. 服务组件支持版本：Alluxio2.5.0 及以上版本。
2. 产品版本：Hadoop2.x 标准版本 EMR-V2.5.1 及以上版本和 Hadoop3.x 标准版本 EMR-V3.2.0 及以上版本。
3. 配置支持透明 URI。使用 Alluxio 透明 URI，需要配置新的 Hadoop 兼容文件系统客户端实现。只要将客户端配置为接收外部 URI，此新的 ShimFileSystem 就会替换现有的 FileSystem。Hadoop 兼容的计算框架--Hadoop FileSystem 接口定义了从 FileSystem 方案到 FileSystem 实现的映射。为了配置 ShimFileSystem，请确保 core-site 其配置了以下配置项：

| 配置项                          | 配置项值                                  |
| ------------------------------- | ----------------------------------------- |
| fs.cosn.impl                    | com.qcloud.emr.CosNShimFileSystem         |
| fs.AbstractFileSystem.cosn.impl | com.qcloud.emr.CosNShimAbstractFileSystem |
| fs.cosn.userinfo.appid          | $appId                                    |

>?
>- 一旦配置了 ShimFileSystem，master 将需要将外部存储系统本地的 URI 路由到 Alluxio 名称空间。这要求 cosn 已 mount 在 Alluxio 名称空间中。
>- 关闭透明 URI 功能：只需 EMR-Alluxio 的使用 EMR 配置下发功能即可。

## mount
mount 命令可以说是 Alluxio 最有特色的命令之一。它类似于 Linux 里的 mount 命令---Linux 用户可以通过 Linux mount 把硬盘，SSD 等存储设备加载到这台 Linux 系统的本地文件系统中。而在 Alluxio 系统当中，mount 的概念进一步被扩展到了分布式系统一层：用户可以通过 Alluxio mount 把一个或多个其他的存储系统/云存储服务（例如 HDFS、COS 等）, 挂载到 Alluxio 这个分布式文件系统当中去。从而运行在 Alluxio 上的分布式应用，例如 Spark、Presto 或者 MapReduce 等，不需要去适配甚至了解具体的数据访问协议和路径，而只需要知道数据对应在 Alluxio 文件系统的路径就已足够，从而极大的方便了应用的开发和维护。
![](https://main.qcloudimg.com/raw/b5d3e96ce6c17866480a36e231c52517.png)

#### EMR-Alluxio 默认使用 hdfs 作为根目录挂载点
在 EMR-Alluxio2.5.1+后，Alluxio 的 UFS 开始支持 COSN 协议，COS UFS 存在读写性能较差以及不稳定的问题，为了解决此类问题，社区贡献了 COSN UFS 底层文件系统。COS 和 COSN UFS 都是用于访问腾讯云对象存储，COSN 相对于 COS 做了深度优化，其读写性能较COS 成倍提升，同时带来了更好的稳定性，所以强烈推荐使用 COSN。COS UFS 将于 EMR-Alluxio2.6.0 版本后停止维护。

Mount COSN 示例：
```
  alluxio fs mount --option fs.cosn.userinfo.secretId=xx \ 
        --option fs.cosn.userinfo.secretKey=xx \ 
        --option fs.cosn.bucket.region=ap-xx \ 
        --option fs.cosn.impl=org.apache.hadoop.fs.CosFileSystem \ 
        --option fs.AbstractFileSystem.cosn.impl=org.apache.hadoop.fs.CosN \ 
        --option fs.cosn.userinfo.appid=xx \ 
        /cosn cosn://COS_BUCKET/path
```
其中，--options 中配置 COS 的配置。

| 配置项名称                       | 解释                                      |
| -------------------------------- | ----------------------------------------- |
| fs.cosn.userinfo.secretId        | cos  scecret id                           |
| fs.cosn.userinfo.secretKey       | cos  secret key                           |
| fs.cosn.impl                     | 固定值：`org.apache.hadoop.fs.CosFileSystem` |
| fs.AbstractFileSystem.cosn.impl  | 固定值：`org.apache.hadoop.fs.CosN`          |
| fs.cosn.bucket.region cos region | 名称，例如 ap-beijing                      |
| fs.cosn.userinfo.appid           | 用户主账号 AppID                          |
| COS_BUCKET COS BUCKET            | 名称。只要名称，不要带 AppID 后缀         |

 
