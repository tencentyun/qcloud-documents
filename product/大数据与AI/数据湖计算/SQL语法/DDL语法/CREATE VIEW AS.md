## 说明
- 支持内核：Presto、SparkSQL。
- 用途：创建视图。

## 标准语法
```
CREATE [ OR REPLACE ] VIEW [IF NOT EXISTS] view_name
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
