设置表数据插入时的排序方式。
## 语法
```
ALTER TABLE table_identifier 
WRITE [LOCALLY] ORDERED BY 
{col_name [ASC|DESC] [NULLS FIRST|LAST]}[, ...]
```


## 示例
```
ALTER TABLE dempts WRITE ORDERED BY category, id;
-- use optional ASC/DEC keyword to specify sort order of each field (default ASC)
ALTER TABLE dempts WRITE ORDERED BY category ASC, id DESC;
-- use optional NULLS FIRST/NULLS LAST keyword to specify null order of each field (default FIRST)
ALTER TABLE dempts WRITE ORDERED BY category ASC NULLS LAST, id DESC NULLS FIRST;
-- To order within each task, not across tasks
ALTER TABLE dempts WRITE LOCALLY ORDERED BY category, id;
```



