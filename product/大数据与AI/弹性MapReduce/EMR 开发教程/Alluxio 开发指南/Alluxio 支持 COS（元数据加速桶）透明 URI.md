元数据加速桶与普通 COS 存储桶不同的是，其在文件系统上提供了高性能的能力。具体可参见 [元数据加速](https://cloud.tencent.com/document/product/436/56971) 文档。

Alluxio 支持元数据加速桶在透明 URL 使用和配置上有以下异同点：
## 使用层面
### 普通存储桶+Alluxio 透明 URL
```
hdfs dfs -ls cosn://COS_BUCKET/PATH/
```
### 元数据加速桶+Alluxio 透明 URL
```
hdfs dfs -ls ofs://MOUNT_POINT-APPID/
```
其中，MOUNT_POINT-APPID 例图如下：
![](https://qcloudimg.tencent-cloud.cn/raw/5732a7c6f13828e12a711dcf1ace6d25.png)

## 配置层面
### 相同点
使用 Alluxio 对元数据加速桶加速的场景，core-site.xml 及 alluxio-site.properties 的配置与 [Alluxio 支持 COS 透明 URI ](https://cloud.tencent.com/document/product/589/55234) 中的**支持版本与配置 URI** 一致

### 不同点
#### Mount
```
alluxio fs mount --option fs.AbstractFileSystem.ofs.impl=com.qcloud.chdfs.fs.CHDFSDelegateFSAdapter \
	--option fs.ofs.user.appid=xx \
	--option fs.ofs.tmp.cache.dir=xx \
	--option fs.ofs.impl=com.qcloud.chdfs.fs.CHDFSHadoopFileSystemAdapter \
	--option fs.ofs.bucket.region=xx 
	/meta-accelarate ofs://MOUNT_POINT-APPID/
```
其中，--options 中配置 CHDFS 的配置。

|配置项名称 |解释 |
|------|------|
|fs.AbstractFileSystem.ofs.impl |固定值：`com.qcloud.chdfs.fs.CHDFSDelegateFSAdapter`|
|fs.ofs.user.appid|用户主账号 AppID |
|fs.ofs.tmp.cache.dir |存放 chdfs 插件目录 |
|fs.ofs.impl |固定值：  `com.qcloud.chdfs.fs.CHDFSHadoopFileSystemAdapter` |
|fs.ofs.bucket.region |名称，例如 ap-beijing |
|MOUNT_POINT-APPID |携带 AppID 的挂载点名称 |



