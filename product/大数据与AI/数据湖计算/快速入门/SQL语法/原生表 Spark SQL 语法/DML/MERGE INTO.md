行级数据更新操作，可用于替换 INSERT OVERWRITE 操作。
## 语法
```
MERGE INTO target_table_name [target_alias]
   USING source_table_reference [source_alias]
   ON merge_condition
   [ WHEN MATCHED [ AND condition ] THEN matched_action ] [...]
   [ WHEN NOT MATCHED [ AND condition ]  THEN not_matched_action ] [...]

matched_action
 { DELETE |
   UPDATE SET * |
   UPDATE SET { column1 = value1 } [, ...] }

not_matched_action
 { INSERT * |
   INSERT (column1 [, ...] ) VALUES (value1 [, ...])

```



