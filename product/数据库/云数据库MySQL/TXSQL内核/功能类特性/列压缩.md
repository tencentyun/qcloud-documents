## 功能介绍
当前有针对行格式的压缩和针对数据页面的压缩，但是这两种压缩方式在处理一个表中的某些大字段和其他很多小字段，同时对小字段的读写很频繁，对大字段访问不频繁的情形中，它在读写访问时都会造成很多不必要的计算资源的浪费。

列压缩功能可以压缩那些访问不频繁的大字段而不压缩那些访问频繁的小字段，此时不仅能够减少整行字段的存储空间，而且可以提高读写访问的效率。

例如，一张员工表：`create table employee(id int, age int, gender boolean, other varchar(1000) primary key (id))`，当对 `id,age,gender` 小字段访问比较频繁，而对 `other` 大字段的访问频率比较低时，可以将 `other` 列创建为压缩列。一般情况下，只有对 `other` 的读写才会触发对该列的压缩和解压，对其他列的访问并不会触发该列的压缩和解压。由此进一步降低了行数据存储的大小，使得在访问频繁的小字段能够更快，对存储空间比较大而访问频率比较低的字段，使得进一步够降低存储空间。

## 支持版本
内核版本 MySQL 5.7 20210330 及以上

## 适用场景
表中的某些大字段和其他很多小字段，同时对小字段的读写很频繁，对大字段访问不频繁的情形中，可以将大字段设置为压缩列。

## 使用说明
### 支持的数据类型
1. `BLOB`（包含 `TINYBLOB`、`MEDIUMBLOB`、`LONGBLOB`）
2. `TEXT`（包含 `TINYTEXT`、`MEDUUMTEXT`、`LONGTEXT`）
3. `VARCHAR`
4. `VARBINARY`

>!其中 `LONGBLOB` 和 `LONGTEXT` 的长度最大只支持$2^{32}-2$，相比官方 [String Type Storage Requirements](https://dev.mysql.com/doc/refman/5.7/en/storage-requirements.html) 支持的$2^{32}-1$少一个字节。

### 支持的 DDL 语法类型
相对官方的 [建表语法](https://dev.mysql.com/doc/refman/5.7/en/create-table.html)，其中 `column_definition` 的 `COLUMN_FORMAT` 定义有所变动。同时列压缩只支持 Innodb 存储引擎类型的表。
```sql
      column_definition:
        data_type [NOT NULL | NULL] [DEFAULT default_value]
          [AUTO_INCREMENT] [UNIQUE [KEY]] [[PRIMARY] KEY]
          [COMMENT 'string']
          [COLLATE collation_name]
          [COLUMN_FORMAT {FIXED|DYNAMIC|DEFAULT}|COMPRESSED=[zlib]]  # COMPRESSED 压缩列关键字
          [STORAGE {DISK|MEMORY}]
          [reference_definition]
```

一个简单的示例如下：
```javascript
CREATE TABLE t1(
  id INT PRIMARY KEY,
  b BLOB COMPRESSED
);
```

此时省略了压缩算法，默认选择 `zlib` 压缩算法 ，您也可以显示指定压缩算法关键字，目前只支持 `zlib` 压缩算法。
```javascript
CREATE TABLE t1(
  id INT PRIMARY KEY,
  b BLOB COMPRESSED=zlib
);
```

支持的 DDL 语法总结如下：
**create table 方面：**

| DDL                                         | 是否继承压缩属性 |
| ------------------------------------------- | ---------------- |
| `CREATE TABLE t2 LIKE t1;`                  | Y                |
| `CREATE TABLE t2 SELECT * FROM t1;`         | Y                |
| `CREATE TABLE t2(a BLOB) SELECT * FROM t1;` | N                |

**alter table 方面：**

| DDL                                               | 描述                 |
| ------------------------------------------------- | -------------------- |
| `ALTER TABLE t1 MODIFY COLUMN a BLOB;`            | 将压缩列变为非压缩 |
| `ALTER TABLE t1 MODIFY COLUMN a BLOB COMPRESSED;` | 将非压缩列变为压缩 |

 
### 新增变量说明

| 参数名                                  | 动态 | 类型    | 默认 | 参数值范围      | 说明                                                         |
| --------------------------------------- | ---- | ------- | ---- | --------------- | ------------------------------------------------------------ |
| innodb_column_compression_zlib_wrap     | Yes  | bool    | TRUE | true/false   | 如果打开，将生成数据的 zlib 头和 zlib 尾并做 adler32 校验    |
| innodb_column_compression_zlib_strategy | Yes  | Integer | 0    | [0,4]           | 列压缩使用的压缩策略，最小值为：0，最大值为4，0 - 4分别和 zlib 中的压缩策略 Z_DEFAULT_STRATEGY、Z_FILTERED、Z_HUFFMAN_ONLY、Z_RLE、Z_FIXED 一一对应。<br>一般来说，Z_DEFAULT_STRATEGY 对于文本数据常是最佳的，Z_RLE 对于图像数据来说是最佳的 |
| innodb_column_compression_zlib_level    | Yes  | Integer | 6    | [0,9]           | 列压缩使用的压缩级别，最小值：0，最大值：9，0代表不压缩，该值越大代表压缩后的数据越小，但压缩时间也越长 |
| innodb_column_compression_threshold     | Yes  | Integer | 256  | [0, 0xffffffff] | 列压缩使用的压缩阈，最小值为：1，最大值为：0xffffffff，单位：字节。只有长度大于或等于该值数据才会被压缩，否则原数据保持不变，只是添加压缩头 |
| innodb_column_compression_pct           | Yes  | Integer | 100  | [1, 100]        | 列压缩使用的压缩率，最小值：1，最大值：100，单位：百分比。只有**压缩后数据大小 / 压缩前数据大小**低于该值时，数据才会被压缩，否则原数据保持不变，只是添加压缩头 |


### 新增状态说明

| 名称                         | 类型    | 说明                                                |
| ---------------------------- | ------- | ---------------------------------------------------------- |
| `Innodb_column_compressed`   | Integer | 列压缩的压缩次数，包括非压缩格式和压缩格式两种状态的压缩   |
| `Innodb_column_decompressed` | Integer | 列压缩的解压次数，包括非压缩格式和压缩格式两种状态的解压缩 |

### 新增错误说明

| 名称                                                         | 范围                       | 说明                                                  |
| ------------------------------------------------------------ | ------------------------------- | ------------------------------------------------------------ |
| `Compressed column '%-.192s' can't be used in key specification` | 指定压缩的列名                  | 不能对有索引的列指定压缩属性                                 |
| `Unknown compression method: %s"`                            | 在 DDL 语句中指定的压缩算法名 | 在 `create table` 或者 `alter table` 时指定 `zlib` 之外非法的压缩算法 |
| `Compressed column '%-.192s' can't be used in column format specification` | 指定压缩的列名                  | 在同一个列中，已经指定 `COLUMN_FORMAT` 属性就不能再指定压缩属性，其中 `COLUMN_FORMAT` 只在 NDB 中被使用 |
| `Alter table ... discard/import tablespace not support column compression` | \                 | 带有列压缩的表不能执行 `Alter table ... discard/import tablespace` 语句 |

### 性能
整体性能分为 DDL 和 DML 两方面：
DDL 方面，使用 sysbench 进行测试：
- 列压缩对 COPY 算法的 DDL 有较大的性能影响，压缩后性能表现比之前慢7倍 - 8倍。
- 对于 inplace 的影响则取决于压缩后的数据量大小，如果采用压缩后，整体数据大小有降低，那么 DDL 的性能是有提升；反之，性能会有一定的降幅。
- 对于 instant 来说，列压缩对该类型的 DDL 基本没有影响。

DML 方面：考虑最常见的压缩情形（压缩比1:1.8），此时有8个列的表，表中有一个大的 varchar 类型的列，其插入数据长度在1到6000内均匀随机，插入的字符在0 -9 、a - b内随机，其他几个列数据类型为 char(60) 或 int 类型。此时其对非压缩列插入、删除和查询都有10%以内的提升，但对于非压缩列的更新则有10%以内的下降，对于压缩列的更新则有15%以内的性能跌幅。这是因为在更新过程中，MySQL 会先读出该行的值然后在写入该行更新之后的值，整个更新过程会触发一次解压和压缩而插入和查询只会进行一次压缩或者解压。

### 注意事项
1. 逻辑导出方面，逻辑导出时 create table 还是会附有 Compressed 相关的关键字。因此导入时在云数据库 MySQL 内部是支持的。其他 MySQL 分支以及官方版本：
   - 官方版本号小于5.7.18，可以直接导入。
   - 官方版本号大于或等于5.7.18，需要在逻辑导出之后，去掉压缩关键字。
2. DTS 导出其他云或是用户时，在 binlog 同步过程中可能会出现不兼容的问题，可以跳过带压缩关键字的 DDL 语句。

