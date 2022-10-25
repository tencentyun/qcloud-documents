## 对数据库字段类型的支持
目前支持的字段类型如下：

| 字段类型    | 支持情况                                                | 可选算法 |
| ----------- | ------------------------------------------------------- | -------- |
| char        | <li>支持51个及以内汉字</li><li>支持155个及以内字母</li> | AES/SM4  |
| varchar     | 支持                                                    | AES/SM4  |
| tinytext    | <li>支持51个及以内汉字</li><li>支持155个及以内字母</li> | AES/SM4  |
| text        | 支持                                                    | AES/SM4  |
| mediumtext  | 支持                                                    | AES/SM4  |
| longtext    | 支持                                                    | AES/SM4  |
| tinyblob    | 支持                                                    | AES/SM4  |
| blob        | 支持                                                    | AES/SM4  |
| longblob    | 支持                                                    | AES/SM4  |
| tinyint     | 不支持                                                  | -        |
| smallint    | 不支持                                                  | -        |
| mediumint   | 不支持                                                  | -        |
| int/integer | 不支持                                                  | -        |
| bigint      | 不支持                                                  | -        |
| float       | 不支持                                                  | -        |
| double      | 不支持                                                  | -        |
| decimal     | 不支持                                                  | -        |
| date        | 不支持                                                  | -        |
| time        | 不支持                                                  | -        |
| year        | 不支持                                                  | -        |
| datetime    | 不支持                                                  | -        |
| timestamp   | 不支持                                                  | -        |

## 对 SQL 语句的支持
对数据库查询语句的支持情况如下：
- **插入语句**：

| 类型         | 支持情况 | SQL 样例                                                     |
| ------------ | -------- | ------------------------------------------------------------ |
| 不指定列插入 | 支持     | insert into table_a  values ('a',1,'bbb','ccc','ddd',3.74, sysdate); |
| 指定列插入   | 支持     | insert into  table_a(col1, col3, col4) values('a','bbb','ccc'); |

- **删除语句**：

| 类型                                       | 支持情况 | SQL 样例                                                     |
| ------------------------------------------ | -------- | ------------------------------------------------------------ |
| 等值匹配删除，策略配置在其中某个条件字段上 | 支持     | delete from table_a  where col1='aaa' and col3='bbb';        |
| 带 in 的删除，策略配置在 in 字段上         | 支持     | delete from table_a  where col1 in ('a','b','c');            |
| 带子查询的删除，策略在子查询的条件字段上   | 支持     | delete from table_a  where col1 in (select col2 from table_b where col3 = 1); |

- **更新语句**：


| 类型                 | 支持情况 | SQL 样例                                     |
| -------------------- | -------- | -------------------------------------------- |
| 策略配置在查询条件上 | 支持     | update table_a set  col1='aaa' where col2=1; |
| 策略配置在更新字段上 | 支持     | update table_a set  col1='aaa' where col2=1; |

- **查询语句**：

| 类型                                                   | 支持情况                             | SQL 样例                                                     |
| ------------------------------------------------------ | ------------------------------------ | ------------------------------------------------------------ |
| 对 select * 语法的支持                                 | 支持                                 | select * from  table_a;                                      |
| 条件字段等值匹配                                       | 支持                                 | select col1 from  table_a where col2=1;                      |
| 条件字段范围查询                                       | 不支持                               | select col1 from  table_a where col1 > 'aaa' and col2 < 3;   |
| 条件字段带函数                                         | 不支持                               | select col1 from  table_a where substr(col1,0,2) = 'aa';     |
| 条件字段带 in                                          | 支持                                 | select col1 from  table_a where col1 in ('a',b','c');        |
| SQL 语句中的表使用别名，选择字段及查询条件通过别名指定 | 支持                                 | select t.col1 from  table_a t where t.col2=1                 |
| 关联查询，策略在条件字段中                             | 支持                                 | select table_a.col2,  table_b.col2 from table_a join table_b on table_a.col1 = table_b.col3 where  table_a.col4='ccc' |
| 关联查询，策略在选择字段中                             | 支持                                 | select table_a.col2,  table_b.col2 from table_a join table_b on table_a.col1 = table_b.col3 where  table_a.col4='ccc' |
| 关联查询时使用 select  *                               | 支持                                 | select * from table_a  join table_b on table_a.col1 = table_b.col3 where table_b.col4='fff'; |
| 选择字段带别名                                         | 支持                                 | select col1 a, col2 b  from table_a                          |
| 子查询-简单语法子查询，策略在子查询条件语句上          | 支持                                 | select col1 from  table_a where col1 in (select col2 from table_b where col3 = 1) |
| 子查询-子查询中字段作为关联条件                        | 支持                                 | select a.col1 from table_a a  join (select col2,col3,col4 from table_b) t on a.col1=t.col3 where  t.col2='ddd' |
| 子查询-策略配置在子查询条件字段上                      | 支持                                 | select t.col4 from  table_a a join (select col2,col3,col4 from table_b) t on a.col1=t.col3 where  t.col2='ddd' |
| 子查询-结果集中带有子查询字段，且配置了策略            | 支持                                 | select t.col4 from  table_a a join (select col2,col3,col4 from table_b) t on a.col1=t.col3 where  t.col2='ddd' |
| 对 exists 关键字的支持                                  | 支持                                 | select col1,col2,col3  from table_a where exists (select 1 from table_b where col3 = table_a.col1) |
| 对 group by 语法的支持                                 | 支持                                 | select col1, col2 from table_a where col3 = 'bbb' group by col1,col2 |
| 对数字类型的分组函数                                   | 不支持                               | select  sum(col2),avg(col2),min(col2),max(col2) from table_a where col1='aaa' |
| 对 order by 的支持                                     | 只支持非加密字段的排序               | select * from table_a order by id desc                       |
| 临时表                                                 | 支持                                 | select * from (select table1.col1,table1.col2,table1.col3,table2.id,table2.col4 from table1,table2 where table1.col1 = table2.col1 ) tmp |

## 功能支持和使用限制

### 数据库
- 支持**5.7及以上**版本的 MySQL 数据库和兼容 MySQL 协议的数据库（如 TDSQL、MariaDB）。
- 支持**8.0及以上版本**的数据库, 但不支持此系列版本新增的 SQL 语法。
- 仅只支持 `utf8` 和 `utf8mb4` 字符集。
- 数据库、表和字段名不区分大小写。
- 加密字段长度需预先扩容以支持更长长度的密文。
- 加密字段需使用区分大小写的 collation，如 `utf8_general_bin`。
- `information_schema`，`sys`，`mysql` 等内置数据库 CASB 会自动忽略。

### 连接
- 连接内不允许切换登录用户。
- 不支持 SSL 连接, CASB 账号认证方式为 `mysql_native_password`。
- CASB 连接后端 DB 的认证方式仅支持 `mysql_native_password` 和 `caching_sha2_password`。

### 加解密和脱敏
- 加解密算法支持 `AES` 和 `SM4` 算法。
- 仅支持 `string` 和 `blob` 类型的数据加解密。
- 支持数值和字符串类型字段数据的动态脱敏。
- 加密后密文超过字段长度时会保存**明文**。
- 支持 `SELECT`, `INSERT`, `REPLACE`, `UPDATE`, `DELETE` 语句中  `WHERE、ON、IN、INSERT VALUE、SET` 等各字段中非表达式的值加解密。
- 支持 `ROW` 条件中非表达式的值加解密，如支持 ` where (id, 'n2' , addr)=(2, name,'a2')` 中的字段加解密。
- 支持 `table references` 和 `where condition` 中的子查询字段中非表达式的值加解密。
- `UNION` 语句使用第一个 `SELECT 子句` 的加解密策略。 
- 不支持存储过程的加解密。
- 不支持 `INSERT INTO ... SELECT ...` 等不经过 CASB 处理的数据的加解密。
- 连接查询时，JOIN 字段需选择同样的密钥，否则密文不一致，无法正确进行连接查询。

### 协议
- 支持 `COM_QUERY`,`COM_STMT_PREPARE` 和 `COM_STMT_EXECUTE` 协议中字段加解密。
- 不支持 `COM_STMT_SEND_LONG_DATA`，`COM_STMT_RESET` 协议。
- 不支持 `COM_QUERY Protocol::LOCAL_INFILE_Data` 协议。

### 语句
- DML 执行前，需先切换到或指定相应的库。
- 加密字段不支持函数操作。
- 加密字段不支持数学运算。
- 加密字段不支持 `ORDER BY`。
- 加密字段不支持 `LIKE` 查询和正则查询。
- 不支持包含自定义变量的语句。
- 不支持视图相关语句。
- 不支持 `SELECT INTO` 语句。
- 不支持 `mysqldump` 中使用 CASB 不支持的特性和条件。
- 不支持 `CREATE TABLE xx AS SELECT`、`CHECK TABLE`、`CHECKSUM TABLE` 语法。
- 不支持 TDSQL 自定义的管理语法, 如 `help`, `repair` 等。
- 不支持 **COM_QUERY 协议**的  `Prepare`、`Execute` 语句的加解密。
- 除了 TDSQL 增删改查语句的行首注释外，SQL 语句中的其余注释不会生效。
- TDSQL 的 ShardKey 字段不能配置加密。

### 其他
- 所有表结构必须预先在策略控制台定义，账号必须和相应数据源绑定后才能通过 proxy 操作相应的数据源。
- 数据源删除后重新添加时，需断开存量连接，建立新的 MySQL 连接查询。
- 单次查询处理的数据大小需小于2^24字节。
