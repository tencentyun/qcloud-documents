## 介绍
Flink connector mongodb 目前支持通过 Flink 将数据批量写入到 mongodb 中，目前仅支持 append 流。

## 版本说明
| Flink 版本 | 说明 |
| :-------- | :--- |
| 1.11      | 不支持 |
| 1.13      | 支持 |

## DDL定义
```sql
CREATE TABLE mongodb (
  user_id INT,
  item_id INT,
  category_id INT,
  behavior VARCHAR
) WITH (
  'connector' = 'mongodb', -- 固定值 'mongodb'
  'database' = 'test', --数据库名
  'collection' = 'table1',--数据集合
  'uri' = 'mongodb://$username:$password@$IP:$PORT,$IP:$PORT,$IP:$PORT/test?authSource=admin', -- MongoDB连接串
  'batchSize' = '1024' -- 每次批量写入的条数
);
```

## 使用范围

Flink connector mongodb 目前仅支持 mongodb sink。支持将腾讯云数据库 MongoDB 作为结果表使用。

## WITH参数

| 参数                  | 说明               | 是否必填 | 备注                      |
| --------------------- | ------------------ | -------- | ------------------------- |
| connector             | 结果表类型         | 是       | 固定值 `mongodb`          |
| database              | 数据库名称         | 是       | -                         |
| collection            | 数据集合           | 是       | -                         |
| uri                   | MongoDB连接串      | 是       | -                         |
| batchSize             | 每次批量写入的条数 | 否       | 默认 1024                 |
| maxConnectionIdleTime | 连接超时时长       | 否       | 默认值为60000，单位为毫秒 |

## 代码示例

```sql
CREATE TABLE random_source (
  user_id INT,
  item_id INT,
  category_id INT,
  behavior VARCHAR
) WITH (
  'connector' = 'datagen',
  'rows-per-second' = '100',  -- 每秒产生的数据条数
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

CREATE TABLE mongodb (
  user_id INT,
  item_id INT,
  category_id INT,
  behavior VARCHAR
) WITH (
  'connector' = 'mongodb', -- 固定值 'mongodb'
  'database' = 'test', --数据库名
  'collection' = 'table1',--数据集合
  'uri' = 'mongodb://$username:$password@$IP:$PORT,$IP:$PORT,$IP:$PORT/test?authSource=admin', -- MongoDB连接串
  'batchSize' = '1024' -- 每次批量写入的条数
);

insert into mongodb select * from random_source;
```

## 注意事项
### Upsert
MongoDB sink 暂不支持 upsert。

### 用户权限
MongoDB的User 必须拥有 database 的写权限。
