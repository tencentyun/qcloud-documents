## 适用场景
该功能主要针对在线业务的超大表 DDL 操作实现秒级变更。
 
## 功能介绍
通过 instant 算法来避免数据拷贝，进而实现大表快速修改列的功能，不拷贝数据，不占用磁盘空间和磁盘 I/O，业务高峰期可以实现秒级变更。

## 使用说明
Instant DDL 支持的操作包括：
- ADD COLUMN
- MODIFY COLUMN

### Instant Add Column 操作说明
1. Instant Add Column 的语法。
Alter Table 新增 algorithm=instant 子句，加列操作可通过如下语句进行：
```
ALTER TABLE t1 ADD COLUMN c INT, ADD COLUMN d INT DEFAULT 1000, ALGORITHM=INSTANT;
```
2. 新增参数 innodb_alter_table_default_algorithm，其可以设置为 inplace，instant。
该参数默认为 inplace，可通过设置该参数来调整 Alter Table 的默认算法，如：
```
SET @@global.innodb_alter_table_default_algorithm=instant;
```
通过该参数指定了缺省算法后，在不指明算法的情况下，将使用默认算法来进行 Alter Table 操作。

#### Instant Add Column 限制
- 一条语句中只有加列操作，不支持有其他的操作在同一条语句的情况。
- 新增列将会放到最后，不支持改变列的顺序。
- 不支持在行格式为 COMPRESSED 的表上快速加列。
- 不支持在已经有全文索引的表上快速加列。
- 不支持在临时表上快速加列。


### Instant Modify Column 操作说明
1. 使用方法同 Instant Add Column 类似，可以通过设置 innodb_alter_table_default_algorithm=instant 或 modify column 时指定 ALGORITHM=instant 关键字进行：
```
ALTER TABLE t1 MODIFY COLUMN c BIGINT, ALGORITHM=INSTANT;
```
2. 同时增加了开关 cdb_instant_modify_column_enabled，当开关开启时以上参数才生效。当开关关闭时 Instant Modify Column 功能将关闭。
>!开关关闭后，已经 instant modify 过的表可以正常使用。

#### Instant Modify Column 限制
- 只支持列类型的修改，不支持修改字段的 nullable、unsigned/signed、charset，但支持修改 default 属性。
- 只支持部分类型的修改，且只能改大长度，目前仅支持以下类型的转换：char 和 varchar 之间、binary 和 varbinary 之间、tinyint/smallint/mediumint/int/bigint 之间互转。
- 单个 column 只能 instant modify 一次，可以同时 instant modify 多个 column。单个 column 第一次 instant add/modify 后，第二次修改此列只能以非 instant 方式进行。
- 支持 instant add columns 和 instant modify columns 的操作需要分开执行，可以先执行 instant add columns 再执行 instant modify columns，或先执行 instant modify columns 再执行 instant add columns。且不能 instant modify 之前 instant add 的列。
- 不能同时修改列名和列类型，可以先修改列名再修改列类型。
- 不支持 import/export，不支持修改索引列。
- 不支持加密与压缩，不支持 redundant 格式。

## 效果对比
对一张5kw的表（12GB）左右，分别进行秒加列和秒改列的操作，可以看到，正常情况下加列需要2分钟、改列需要21分钟左右；而使用秒加列和秒改列，几乎瞬间就能完成。
<img src="https://main.qcloudimg.com/raw/d50bdfe19657d955204ba8fc8331d277.png"  style="zoom:80%;">


 
