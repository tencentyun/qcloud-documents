丢弃会话状态。

## 概要

```sql
DISCARD { ALL | PLANS | TEMPORARY | TEMP }
```

## 描述

DISCARD 释放与数据库会话相关联的内部资源。这些资源通常在会话结束时释放。
DISCARD TEMP 删除在当前会话中创建的所有临时表。
DISCARD PLANS 释放所有内部缓存的查询计划。
DISCARD ALL 重置会话到原始状态，丢弃临时资源并重置会话本地配置更改。

## 参数

TEMPORARY, TEMP
删除所有在当前会话中创建的临时表。

PLANS
释放所有缓存的查询计划。

ALL
释放所有和当前会话相关联的临时资源并且重置会话到初始状态。目前，该和执行以下语句序列具有相同的效果。

```sql
SET SESSION AUTHORIZATION DEFAULT;
RESET ALL;
DEALLOCATE ALL;
CLOSE ALL;
UNLISTEN *;
SELECT pg_advisory_unlock_all();
DISCARD PLANS;
DISCARD TEMP;
```

## 注意
DISCARD ALL 不能在事务块中执行。

## 兼容性
DISCARD 是数据库扩展。
