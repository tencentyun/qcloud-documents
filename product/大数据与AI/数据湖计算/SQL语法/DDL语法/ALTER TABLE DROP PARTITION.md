从表中删除一个或者多个分区。
## 语法
```
ALTER TABLE table_name DROP [IF EXISTS] PARTITION (partition_spec) [, PARTITION (partition_spec)];
```
## 参数
- IF EXISTS：如果指定的分区不存在，则取消显示错误消息。
- `PARTITION (partition_spec)`：指定分区。

## 示例
```
ALTER TABLE tbl DROP IF EXISTS PARTITION (P = 1);
```
```
alter table tbl drop 
    partition (p1='a',p2=1), partition(p1='b',p2=2), 
    partition(p1='c',p2=3);
```
