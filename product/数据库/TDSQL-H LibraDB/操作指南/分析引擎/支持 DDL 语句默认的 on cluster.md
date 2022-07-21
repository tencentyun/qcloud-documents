## 特性描述
默认情况下，原生 ClickHouse 的 DDL 操作只在链接所在的节点上生效。如果需要 DDL 变更在整个集群维度生效，需要显式在 DDL 语句中添加 `ON CLUSTER default cluster` 语句。

LibraSQL 提供了默认 DDL 集群配置：`ddl_default_oncluster`。打开该配置后，DDL 操作会默认在 `default_cluster` 上执行，效果相当于在 DDL 语句中添加 `ON CLUSTER default_cluster`。该配置默认关闭。 

LibraSQL 支持会话级别打开配置。打开前，执行 DDL 操作仅在当前节点执行。打开后，执行 DDL 操作将在集群中各节点执行。

## 使用限制
暂不支持在 TDSQL-H LibraDB 控制台修改该参数，如需全局开启该配置，请 [提交工单](https://console.cloud.tencent.com/workorder/category)。

## 使用说明
### 打开 DDL 集群配置
```sql
set ddl_default_oncluster = 'default_cluster';
```
打开 DDL 集群配置 `ddl_default_oncluster`，执行 DDL 操作将在集群各节点执行。

示例：
![](https://qcloudimg.tencent-cloud.cn/raw/7d681489e08d969a298f3e30e9be62c1.png)

### 关闭 DDL 集群配置
```sql
set ddl_default_oncluster = '';
```
关闭 DDL 集群配置 `ddl_default_oncluster`，执行 DDL 操作仅在当前节点执行。

示例：
![](https://qcloudimg.tencent-cloud.cn/raw/f0a785ee574df8cbec463a8a9b3df08d.png)

