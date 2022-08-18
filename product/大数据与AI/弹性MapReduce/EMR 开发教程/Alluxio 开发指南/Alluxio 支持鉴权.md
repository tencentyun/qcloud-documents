Alluxio 用户在对已有的统一命名空间访问 COS、HDFS、CHDFS 上的数据，或者用户使用透明 URL 来访问 Alluxio 中的缓存数据时，会出现无鉴权情况，也就是说任何用户只要拿着对应 URI 就能获取到数据。云上 Alluxio 对此类场景结合 Ranger 和 CosRanger 完善了鉴权场景。

>? 为了设配鉴权特性，请确保集群有以下组件集成：
>- 如果 Alluxio 中只挂载了 HDFS，那么需要集成 Ranger 组件。
>- 如果 Alluxio 中挂载了 COS、CHDFS，那么需要集成 CosRanger 组件。

## 支持版本
- 服务组件支持版本：Alluxio2.8.0版本。
- 产品版本：Hadoop3.x 标准版本 EMR-V3.4.0版本。

## 配置鉴权
### 前置配置
```
#新增hive组件ranger-hive-security.xml配置项
ranger.plugin.hive.urlauth.filesystem.schemes==hdfs:,file:,wasb:,adl:,alluxio:

#新增presto组件hive.properties配置项
hive.hdfs.authentication.type=NONE
hive.metastore.authentication.type=NONE
hive.hdfs.impersonation.enabled=true
hive.metastore.thrift.impersonation.enabled=true
```
>? 以上前置配置需客户根据集群现有组件来配置。

### HDFS 鉴权
软链接 ranger 相关配置文件：
```
[hadoop@172 conf]$ pwd
/usr/local/service/alluxio/conf
[hadoop@172 conf]$ ln -s /usr/local/service/hadoop/etc/hadoop/ranger-hdfs-audit.xml
ranger-hdfs-audit.xml
[hadoop@172 conf]$ ln -s /usr/local/service/hadoop/etc/hadoop/ranger-hdfs-security.xml ranger-hdfs-security.xml
```

**alluxio-site.properties 配置**
建议使用 EMR 控制台进行集群维度配置下发。
```
# 鉴权开关(默认false)
alluxio.security.authorization.plugins.enabled=true
alluxio.security.authorization.plugin.name=ranger
alluxio.security.authorization.plugin.paths=/usr/local/service/alluxio/conf
alluxio.underfs.security.authorization.plugin.name=ranger
alluxio.underfs.security.authorization.plugin.paths=/usr/local/service/alluxio/conf
alluxio.master.security.impersonation.hadoop.users=*
alluxio.security.login.impersonation.username=_HDFS_USER_
```
>? 下发完成后需重启 Alluxio 服务。
>
### COS 及 CHDFS 鉴权

```
#新增core-site.xml配置项
fs.ofs.ranger.enable.flag=true
```

**alluxio-site.properties 配置**
建议使用 EMR 控制台进行集群维度配置下发。
```
# 鉴权开关(默认false)
# 鉴权开关(默认false)
alluxio.security.authorization.plugins.enabled=true
alluxio.security.authorization.plugin.name=ranger
alluxio.security.authorization.plugin.paths=/usr/local/service/alluxio/conf
alluxio.underfs.security.authorization.plugin.name=ranger
alluxio.underfs.security.authorization.plugin.paths=/usr/local/service/alluxio/conf
alluxio.cos.qcloud.object.storage.ranger.service.config.dir=/usr/local/service/cosranger/conf
alluxio.master.security.impersonation.hadoop.users=*
alluxio.security.login.impersonation.username=_HDFS_USER_
# 重试次数默认为5次
alluxio.cos.qcloud.object.storage.permission.check.max.retry=5
```
>? 下发完成后需重启 Alluxio 服务。
