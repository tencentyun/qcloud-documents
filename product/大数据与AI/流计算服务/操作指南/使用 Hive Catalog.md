## 介绍

您可以在 Oceanus SQL 作业中配置 Hive Catalog、查看 Hive 元数据、使用 Hive Catalog。将元数据信息保存到 Hive Metastore 以后，在作业中无需再显式声明 DDL 语句，直接三段式引用元数据即可。

## 版本说明

| Flink 版本 | 说明                                             |
| ---------- | ------------------------------------------------ |
| 1.11       | 不支持                                           |
| 1.13       | 支持 hive 版本2.2.0、2.3.2、2.3.5、3.1.1 |
| 1.14       | 不支持                                           |

## 前提条件

已在 Hive Metastore 侧开启了 Hive Metastore 服务。
相关命令如下：
- `hive --service metastore`：开启 Hive Metastore 服务。
- `ps -ef|grep metastore`：查询 Hive Metastore 服务是否已开启。

## 操作说明
### 创建 Hive Catalog
切换到 `_dc`，单击**新建 Hive Catalog**。
![](https://qcloudimg.tencent-cloud.cn/raw/c131d8bae1429ff0549207c14f8ff957.png)

### 创建数据库
在 SQL 作业中可以创建数据库。数据库的写法采用两段式：`catalog_name.database_name`。
```sql
CREATE DATABASE IF NOT EXISTS `hiveCatalogName`.`databaseName`;
```

### 创建数据表
在 SQL 作业中可以创建数据表。数据表的写法采用三段式：`catalog_name.database_name.table_name`。
```sql
CREATE TABLE IF NOT EXISTS `hiveCatalogName`.`databaseName`.`tableName` (
  user_id INT,
  item_id INT,
  category_id INT,
  -- ts AS localtimestamp,
  -- WATERMARK FOR ts AS ts,
  behavior VARCHAR
) WITH (
  'connector' = 'datagen',
  'rows-per-second' = '1',  -- 每秒产生的数据条数
  'fields.user_id.kind' = 'sequence',  -- 有界序列（结束后自动停止输出）
  'fields.user_id.start' = '1',  -- 序列的起始值
  'fields.user_id.end' = '10000',  -- 序列的终止值
  'fields.item_id.kind' = 'random',  -- 无界的随机数
  'fields.item_id.min' = '1',  -- 随机数的最小值
  'fields.item_id.max' = '1000',  -- 随机数的最大值
  'fields.category_id.kind' = 'random',  -- 无界的随机数
  'fields.category_id.min' = '1',  -- 随机数的最小值
  'fields.category_id.max' = '1000',  -- 随机数的最大值
  'fields.behavior.length' = '5' -- 随机字符串的长度
);
```

### SQL 作业中引用 Hive Catalog 中的表

在 SQL 作业中，将光标移动到要插入的元表的位置，在左侧导航栏中找到要引用的表，点击菜单中的【引用】。

```sql
INSERT INTO
  `hiveCatalogName`.`databaseName`.`sink_tableName` 
SELECT
  *
FROM
  `hiveCatalogName`.`databaseName`.`source_tableName`;
```
>?
>- 同一个作业中只能引用一个 Hive Catalog。
>- Hive Catalog 不支持 Drop 操作。

### 删除 Hive Metastore
在左侧导航栏，单击 Hive Catalog 对应的**删除**按钮。
![](https://qcloudimg.tencent-cloud.cn/raw/cfe3ae07ba7eeeadf213d38e7a05f809.png)

### 赋权
作业执行过程中，需要有写入 hdfs 文件的权限，目前 Oceanus 使用 Hive Catalog 元数据需要对 flink 用户进行授权。相关操作如下：
- 在 Hive 所在的所有 master 节点执行。
```shell
useradd flink
groupadd supergroup
usermod -a -G supergroup flink
hdfs dfsadmin -refreshUserToGroupsMappings
```

- 建议在 Hive 中开启权限，在 hive-site.xml 文件中添加如下的配置项。
```xml
<property>
<name>hive.metastore.authorization.storage.checks</name>
<value>true</value>
<description>Should the metastore do authorization checks against
the underlying storage for operations like drop-partition (disallow
the drop-partition if the user in question doesn't have permissions
to delete the corresponding directory on the storage).</description>
```

