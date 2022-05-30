当需要将已有 OLTP 数据库实例中的多个表进行读合并时，可基于 Merge 表引擎合并，将多个表数据实时汇聚到一个 LibraSQL 分析引擎进行分析。

例如：在游戏行业中，各个游戏服采用分库的架构时，各个库中就会有相同的用户表，日志表，道具表等。通过使用 TDSQL-H LibraDB，将数据多源合一到 LibraSQL 分析引擎，既能为各个游戏服产出报表，也能以全局视角聚合分析所有数据或完成全局的审计需要。

## 使用限制
- 添加 CDC 任务通用使用限制、源数据库环境要求请参见 [添加 CDC](https://cloud.tencent.com/document/product/1488/63678)。
- 需保证合并至同一张表的源端表结构相同。

## 注意事项
添加 CDC 任务通用注意事项请参见 [添加 CDC](https://cloud.tencent.com/document/product/1488/63678)。

## 前提条件
[添加 CDC 任务](https://cloud.tencent.com/document/product/1488/63678) 已完成设置数据源步骤并已进入**设置对象**页面。

## 操作步骤
1. 在**设置对象**页面，同步对象选择**指定对象**。
2. **多表归并**开关默认关闭。
3. 在**源库对象**中选择库表。
4. 单击<img src="https://qcloudimg.tencent-cloud.cn/raw/a5a9e29bbdc569bfe45a64837fe87aba.png"  style="zoom:60%;">，**已选对象**中将展示已选择的库表。
5. 使用 Merge 表引擎合并，支持以下两种方式。
>?Merge 表引擎详细说明请参见 [Merge Table Engine](https://clickhouse.com/docs/en/engines/table-engines/special/merge/)。
>
  - **同库多源合一**
     1. （可选）在**已选对象**右侧单击**批量改名**，在弹出的**批量添加已选对象表名后缀**对话框中输入后缀，单击**确定**。
     2. 单击**下一步**，进入 [添加 CDC 任务](https://cloud.tencent.com/document/product/1488/63678) 的高级设置步骤，继续执行其他步骤，启动 CDC 任务后，该配置生效。
     3. 使用 Merge 表引擎，匹配具有相同命名模式和表结构的数据表，构造虚拟表，完成表数据查询合并。
```sql
CREATE TABLE ... Engine=Merge(currentDatabase(), tables_regexp)
```
其中，tables_regexp 是一个正则表达式，用于匹配指定数据库中的表名。
**示例：**
```sql
-- 在当前数据库下，按照普通表 tableA_log 的表结构建立 Merge 表 table_all，其中 table_all 是虚拟表， .*_log 匹配当前数据库中表名的正则表达式
CREATE TABLE table_all on cluster default_cluster as databaseA.tableA_log  Engine=Merge(currentDatabase(), '.*_log') ;
                     
-- 当查询 Merge 表时，LibraSQL 分析引擎会自动查询所有带后缀 _log 的表(例如 tableA_log、tableB_log、tableC_log、tableD_log)，将结果汇聚返回
select * from table_all;
```
   - **跨库多源合一**
     1. （可选）修改库表名映射或批量为表添加后缀请参考 [修改库表名映射](https://cloud.tencent.com/document/product/1488/63694)。
     2. 单击**下一步**，进入 [添加 CDC 任务](https://cloud.tencent.com/document/product/1488/63678) 的高级设置步骤，继续执行其他步骤，启动 CDC 任务后，该配置生效。
     3. 使用 Merge 表引擎，匹配具有相同命名模式的库，且库中有相同命名模式和表结构的数据表，构造虚拟表，完成表数据查询合并。
```sql
CREATE TABLE ... Engine=Merge(REGEXP(expression), tables_regexp)
```
其中，expression 是用于匹配数据库名称的正则表达式。tables_regexp 是一个正则表达式，用于匹配指定数据库中的表名。
**示例：**
```sql
-- 按照普通表 table_1 的表结构建立 Merge 表 table_all，其中 table_all 是虚拟表，A_* 匹配数据库名称的正则表达式，table_1 匹配数据库中表名的正则表达式
CREATE TABLE table_all on cluster default_cluster as A_1.table_1 ENGINE=Merge(REGEXP('A_*'), 'table_1');
                
-- 当查询 Merge 表时，LibraSQL 分析引擎会自动查询所有 A_* 数据库(例如 A_1、A_2)中命名为 table_1 的表，将结果汇聚返回
select * from table_all;
```
 
## 相关操作
最佳实践请参见 [基于 Merge 表引擎数据合并最佳实践](https://cloud.tencent.com/document/product/1488/74333)。

