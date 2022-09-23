从指定的 SELECT 查询创建新视图。视图是一个逻辑表，将来的查询可以引用它。视图不包含任何数据，也不写入数据。相反，每次您通过另一个查询引用视图时，视图指定的查询都会运行。
## 语法
```
CREATE VIEW [IF NOT EXISTS] view_name
    [(column_name [COMMENT 'column_comment'][, ...])]
    [COMMENT 'view_comment']
  AS select_statement
```
## 参数
- `[IF NOT EXISTS]`：不存在则创建。
- `view_name`：视图名。
- `[(column_name [COMMENT 'column_comment'][, ...])]`：列的名字，同时后面可以带上列的注释。
- `[COMMENT 'view_comment']`：视图的注释。
- `select_statement`：查询语句。

## 示例
```
create or replace view db1.v1 as select x,y from tbl;
create view test_view (id comment 'test c1', name_length comment 'test name c2') as  select id, length(name) from test;
```
