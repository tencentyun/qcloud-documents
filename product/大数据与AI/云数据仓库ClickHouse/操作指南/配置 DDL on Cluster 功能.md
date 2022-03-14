默认情况下，ClickHouse 在进行集群纬度执行建表等 DDL 操作时需要手动添加 ON CLUSTER XXX 语法。云数据仓库 ClickHouse 21.8.8.12版本添加 DDL On Cluster 新功能，在执行 DDL 操作时可以自动添加 Cluster，默认状态为不开启。

ClickHouse 新增参数：
```xml
<!--default_on_cluster为默认添加的Cluster，默认为""-->
<default_on_cluster>default_cluster</default_on_cluster>
<!--enable_default_on_cluster为是否开启DDL On Cluster功能，默认为0-->
<enable_default_on_cluster>1</enable_default_on_cluster>
```
## 使用方式
### 1. 配置文件永久配置
修改 users.xml 添加参数，配置后不需要重启：
```xml
<yandex>
	<!-- Profiles of settings. -->
	<profiles>
		<default_on_cluster>default_cluster</default_on_cluster>
		<enable_default_on_cluster>1</enable_default_on_cluster>
	</profiles>
</yandex>
```
### 2. 用户 session 级别临时修改
```sql
set default_on_cluster='default_cluster';
set enable_default_on_cluster=1;
```
