## 功能介绍
许多用户要求能够使索引不可见，以确定是否可以删除它。通过 invisible index 这种方式，用户可以在做出删除该索引的最终决定之前，来查看是否有任何应用程序或数据库用户实际使用它（是否生成/报告了任何错误），该能力从8.0移植至5.7版本中。

## 支持版本
内核版本 MySQL 5.7 20180918 及以上

## 适用场景
在删除索引前，可以将该索引设置为 invisible，来确认该索引是否有用，这样可以安全地删除该索引。

## 使用说明
可以使用如下语句来创建 invisible 索引和将某个索引改变为 invisible 索引：
```sql
CREATE TABLE t1 (
  i INT,
  j INT,
  k INT,
  INDEX i_idx (i) INVISIBLE
) ENGINE = InnoDB;
CREATE INDEX j_idx ON t1 (j) INVISIBLE;
ALTER TABLE t1 ADD INDEX k_idx (k) INVISIBLE;
```

可以使用如下语句将其改变为可见索引：
```sql
ALTER TABLE t1 ALTER INDEX i_idx INVISIBLE;
ALTER TABLE t1 ALTER INDEX i_idx VISIBLE
```
