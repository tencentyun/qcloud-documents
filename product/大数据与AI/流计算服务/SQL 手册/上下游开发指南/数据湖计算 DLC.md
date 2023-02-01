## 版本说明
| Flink 版本 | 说明      |
| ---------- | --------- |
| 1.11       | 不支持    |
| 1.13       | 支持 Sink |
| 1.14       | 不支持    |


## 使用范围
可以作为 Sink 使用。目前支持写入 DLC 托管的原生表。

## DDL 定义
```
CREATE TABLE `eason_internal_test`(
    `name` STRING,
    `age` INT
) WITH (
    'connector' = 'dlc-inlong',
    'catalog-database' = 'test',
    'catalog-table' = 'eason_internal_test',
    'default-database' = 'test',
    'catalog-name' = 'HYBRIS',
    'catalog-impl' = 'org.apache.inlong.sort.iceberg.catalog.hybris.DlcWrappedHybrisCatalog',
    'qcloud.dlc.secret-id' = '12345asdfghASDFGH',
    'qcloud.dlc.secret-key' = '678910asdfghASDFGH',
    'qcloud.dlc.region' = 'ap-guangzhou',
    'qcloud.dlc.jdbc.url' = 'jdbc:dlc:dlc.internal.tencentcloudapi.com?task_type=SparkSQLTask&database_name=test&datasource_connection_name=DataLakeCatalog&region=ap-guangzhou&data_engine_name=dailai_test',
    'qcloud.dlc.managed.account.uid' = '100026378089',
    'request.identity.token' = '100026378089',
    'user.appid' = '1257058945',
    'uri' = 'dlc.internal.tencentcloudapi.com'
);
```

## WITH 参数
### 通用参数

| 参数值                         | 必填 | 默认值 | 描述                                                         |
| ------------------------------ | ---- | ------ | ------------------------------------------------------------ |
| connector                      | 是   | 无     | connector 类型，必须填 dlc-inlong                            |
| catalog-database               | 是   | 无     | DLC 内表所在的数据库名称                                     |
| catalog-table                  | 是   | 无     | DLC 内表名称                                                 |
| default-database               | 是   | 无     | DLC 内表所在的数据库名称                                     |
| catalog-name                   | 是   | 无     | catalog 名称，必须填 HYBRIS                                  |
| catalog-impl                   | 是   | 无     | catalog的 实现类，必须填  org.apache.inlong.sort.iceberg.catalog.hybris.DlcWrappedHybrisCatalog |
| qcloud.dlc.managed.account.uid | 是   | 无     | DLC 管理账号的 uid，此处固定填写 100026378089                |
| qcloud.dlc.secret-id           | 是   | 无     | DLC 用户的 secretId，从 https://console.cloud.tencent.com/cam/capi 中获取 |
| qcloud.dlc.secret-key          | 是   | 无     | DLC 用户的 secretKey，从 https://console.cloud.tencent.com/cam/capi 中获取 |
| qcloud.dlc.region              | 是   | 无     | DLC 所在地域，必须填 ap-地域 格式                            |
| qcloud.dlc.jdbc.url            | 是   | 无     | DLC jdbc 接入 url，格式见 https://cloud.tencent.com/document/product/1342/61547 |
| uri                            | 是   | 无     | DLC 接入 uri，必须填 dlc.internal.tencentcloudapi.com        |
| user.appid                     | 是   | 无     | DLC 用户的 appid                                             |
| request.identity.token         | 是   | 无     | DLC 内表接入的 token，此处固定填写 100026378089              |
| sink.ignore.changelog          | 否   | 是     | 是否忽略 delete 数据，默认为 false，设为 true 则进入 append mode |


## DLC 表配置
```
Upsert 模式
-- DLC 建表语句
CREATE TABLE `bi_sensor`(
    `uuid` string,
    `id` string,
    `type` string,
    `project` string,
    `properties` string,
    `sensors_id` string,
    `time` int,
    `hour` int) PARTITIONED BY (`time`);
-- 将目标表设为 v2 表，允许 upsert
ALTER TABLE `bi_sensor` SET TBLPROPERTIES ('format-version'='2','write.metadata.delete-after-commit.enabled' = 'true', 'write.metadata.previous-versions-max' = '100', 'write.metadata.metrics.default' = 'full', 'write.upsert.enabled'='true', 'write.distribution-mode'='hash');

-- oceanus sink DDL，dlc 的主键和分区字段必须在 flink 定义的主键字段中
create table bi_sensors (
    `uuid` STRING,
    `id` STRING,
    `type` STRING,
    `project` STRING,
    `properties` STRING,
    `sensors_id` STRING,
    `time` int,
    `hour` int,
    PRIMARY KEY (`uuid`, `time`) NOT ENFORCED
) with (...)
```
