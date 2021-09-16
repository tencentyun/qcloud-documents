
## MySQL/TDSQL-C 检查详情
- 检查要求：在导出视图结构时，DTS 会检查源库中 `DEFINER` 对应的 user1（ [DEFINER = user1]）和迁移目标的 user2 是否一致。
   - 如果一致则迁移后不做改动。
   - 如果不一致，则迁移后修改 user1 在目标库中的 `SQL SECURITY` 属性，由 `DEFINER` 转换为 `INVOKER`（ [INVOKER = user1]），同时设置目标库中 `DEFINER` 为迁移目标的 user2（[DEFINER = 迁移目标user2]）。

- 检查说明：`SQL SECURITY` 参数用来表示用户访问指定视图时，系统按照谁的权限来执行。 
  - `DEFINER`：表示只有定义者才能执行。
  - `INVOKER`：表示拥有权限的调用者可以执行。
默认情况下，系统指定为 `DEFINER`。

## TDSQL MySQL 检查详情
只允许和迁移目标 user@host 相同的 definer，即在导出视图结构时，DTS 检查源库中 definer 对应的 user1（ [DEFINER = user1]）和迁移目标的 user2（user@host）是否一致，一致则支持迁移视图，否则不支持。

对于和迁移目标 user@host 不同的 definer，如果需要迁移，则要修改源数据库视图的 definer（修改为迁移目标用户），或者在迁移/同步任务中不勾选，等任务结束后手动同步视图。

