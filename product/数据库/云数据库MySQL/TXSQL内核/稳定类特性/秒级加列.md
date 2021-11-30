## 功能介绍
快速加列功能是通过只修改数据字典的方法来实现大表快速加列，避免之前加列操作必须做的数据拷贝，从而大幅缩小大表加列所需的时间，减少对系统的影响。

## 支持版本
- 内核版本 MySQL 5.7 20190830 及以上
- 内核版本 MySQL 8.0 20200630 及以上

## 适用场景
适用于需要对数据量大的表进行增加列操作的场景。

## 性能数据
通过对5GB数据量的表进行测试，增加一列操作从40秒降到1秒以内。

## 使用说明
- Instant Add Column 语法
Alter Table 新增 algorithm=instant 子句，加列操作可通过如下语句进行：
```
ALTER TABLE t1 ADD COLUMN c INT, ADD COLUMN d INT DEFAULT 1000, ALGORITHM=INSTANT;
```

- 新增参数 innodb_alter_table_default_algorithm，可以设置为 inplace、instant。
该参数默认为 inplace，可通过设置该参数来调整 Alter Table 的默认算法，如：
```
SET @@global.innodb_alter_table_default_algorithm=instant;
```
通过该参数指定了缺省算法后，在不指明算法的情况下，将使用默认算法来进行 Alter Table 操作。
