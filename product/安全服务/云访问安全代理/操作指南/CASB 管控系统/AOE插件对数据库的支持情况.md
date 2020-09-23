本文档将为您介绍云访问安全代理（CASB）对数据库的支持情况。

## 支持的数据库类型及版本
目前云访问安全代理仅支持 Mysql 5.6及5.7版本，暂不支持其他类型及其他版本数据库。


## 对数据库字段类型的支持

目前支持的数据库类型为 Mysql，支持的字段类型如下：

| 字段类型    | 支持情况 | 可选算法 |
| ----------- | -------- | -------- |
| char        | <li>支持51个及以内汉字</li><li>支持155个及以内字母</li>   |   AES/SM4    |
| varchar     | 支持     | AES/SM4  |
| tinytext    | <li>支持51个及以内汉字</li><li>支持155个及以内字母</li>    | AES/SM4  |
| text        | 支持     | AES/SM4  |
| longtext    | 支持     | AES/SM4  |
| tinyblob    | 支持     | AES/SM4  |
| blob        | 支持     | AES/SM4  |
| longblob    | 支持     | AES/SM4  |
| tinyint     | 不支持   |      -    |
| smallint    | 不支持   |     -     |
| mediumint   | 不支持   |   -       |
| int/integer | 不支持   |   -       |
| bigint      | 不支持   |     -     |
| float       | 不支持   |     -     |
| double      | 不支持   |    -      |
| decimal     | 不支持   |    -      |
| date        | 不支持   |   -       |
| time        | 不支持   |    -      |
| year        | 不支持   |    -      |
| datetime    | 不支持   |    -      |
| timestamp   | 不支持   |     -     |

## 对 SQL 语句的支持
对数据库查询语句的支持情况如下：

- **插入语句**：

| 类型         | 支持情况 | SQL 样例                                                      |
| ------------ | -------- | ------------------------------------------------------------ |
| 不指定列插入 | 支持     | insert into table_a  values ('a',1,'bbb','ccc','ddd',3.74, sysdate); |
| 指定列插入   | 支持     | insert into  table_a(col1, col3, col4) values('a','bbb','ccc'); |

- **删除语句**：

| 类型                                       | 支持情况 | SQL 样例                                                      |
| ------------------------------------------ | -------- | ------------------------------------------------------------ |
| 等值匹配删除，策略配置在其中某个条件字段上 | 支持     | delete from table_a  where col1='aaa' and col3='bbb';        |
| 带 in 的删除，策略配置在 in 字段上             | 支持     | delete from table_a  where col1 in ('a','b','c');            |
| 带子查询的删除，策略在子查询的条件字段上    | 支持     | delete from table_a  where col1 in (select col2 from table_b where col3 = 1); |

- **更新语句**：


| 类型                 | 支持情况 | SQL 样例                                      |
| -------------------- | -------- | -------------------------------------------- |
| 策略配置在查询条件上   | 支持     | update table_a set  col1='aaa' where col2=1; |
| 策略配置在更新字段上 | 支持     | update table_a set  col1='aaa' where col2=1; |

- **查询语句**：

| 类型                                                | 支持情况                             | SQL 样例                                                      |
| --------------------------------------------------- | ------------------------------------ | ------------------------------------------------------------ |
| 对 select * 语法的支持                                | 支持                                 | select * from  table_a;                                      |
| 条件字段等值匹配                                    | 支持                                 | select col1 from  table_a where col2=1;                      |
| 条件字段模糊匹配                                    | 只支持完全匹配及从左边完全匹配的情况 | select col1 from  table_a where col3 like 'bbb%';           |
| 条件字段范围查询                                    | 不支持                               | select col1 from  table_a where col1 > 'aaa' and col2 < 3;   |
| 条件字段带函数                                      | 不支持                               | select col1 from  table_a where substr(col1,0,2) = 'aa';     |
| 条件字段带 in                                        | 支持                                 | select col1 from  table_a where col1 in ('a',b','c');        |
| SQL 语句中的表使用别名，选择字段及查询条件通过别名指定 | 支持                                 | select t.col1 from  table_a t where t.col2=1                 |
| 关联查询，策略在条件字段中                           | 支持                                 | select table_a.col2,  table_b.col2 from table_a join table_b on table_a.col1 = table_b.col3 where  table_a.col4='ccc' |
| 关联查询，策略在选择字段中                           | 支持                                 | select table_a.col2,  table_b.col2 from table_a join table_b on table_a.col1 = table_b.col3 where  table_a.col4='ccc' |
| 关联查询时使用 select  *                             | 支持                                 | select * from table_a  join table_b on table_a.col1 = table_b.col3 where table_b.col4='fff'; |
| 选择字段带别名                                      | 支持                                 | select col1 a, col2 b  from table_a                          |
| 子查询-简单语法子查询，策略在子查询条件语句上       | 支持                                 | select col1 from  table_a where col1 in (select col2 from table_b where col3 = 1) |
| 子查询-子查询中字段作为关联条件                     | 支持                                 | select a.col1 from table_a a  join (select col2,col3,col4 from table_b) t on a.col1=t.col3 where  t.col2='ddd' |
| 子查询-策略配置在子查询条件字段上                   | 支持                                 | select t.col4 from  table_a a join (select col2,col3,col4 from table_b) t on a.col1=t.col3 where  t.col2='ddd' |
| 子查询-结果集中带有子查询字段，且配置了策略         | 支持                                 | select t.col4 from  table_a a join (select col2,col3,col4 from table_b) t on a.col1=t.col3 where  t.col2='ddd' |
| 对 exist 关键字的支持                                 | 不支持                               | select col1,col2,col3  from table_a where exists (select 1 from table_b where col3 = table_a.col1) |
| 对 group by 语法的支持                                | 支持                                 | select col1, col2  from table_a group by col1,col2 where col3 = 'bbb' |
| 对 union 的支持                                       | 不支持                               | select a.col1,a.col2  from table_a union (select c.col3,c.col5 from table_c) |
| 对数字类型的分组函数                                | 不支持                               | select  sum(col2),avg(col2),min(col2),max(col2) from table_a where col1='aaa' |
|对 order by 的支持|只支持非加密字段的排序|select * from table_a order by id desc|
|临时表|不支持|select * from (select table1.col1,table1.col2,table1.col3,table2.id,table2.col4 from table1,table2 where table1.col1 = table2.col1 ) tmp|

## 对 JDBC 接口的支持
对 Java 数据库访问接口的支持情况如下：

| 类                | 方法                | 支持情况     |
| ----------------- | ------------------- | ------------ |
| DataSource        |        -             | 不支持       |
| Driver            |        -             | 支持         |
| Connection        |       -              | 支持         |
| PreparedStatement | setArray            | 不支持       |
| PreparedStatement | setAsciiStream      | 不支持       |
| PreparedStatement | setBigDecimal       | 支持         |
| PreparedStatement | setBinaryStream     | 支持         |
| PreparedStatement | setBlob             | 支持         |
| PreparedStatement | setBoolean          | 支持，不处理 |
| PreparedStatement | setByte             | 支持，不处理 |
| PreparedStatement | setBytes            | 支持         |
| PreparedStatement | setCharacterStream  | 支持         |
| PreparedStatement | setClob             | 支持         |
| PreparedStatement | setDate             | 支持，不处理 |
| PreparedStatement | setDouble           | 支持         |
| PreparedStatement | setFloat            | 支持         |
| PreparedStatement | setInt              | 支持         |
| PreparedStatement | setLong             | 支持         |
| PreparedStatement | setNCharacterStream | 支持         |
| PreparedStatement | setNClob            | 支持         |
| PreparedStatement | setNString          | 支持         |
| PreparedStatement | setNull             | 支持         |
| PreparedStatement | setObject           | 支持         |
| PreparedStatement | setRef              | 支持，不处理 |
| PreparedStatement | setRowId            | 支持         |
| PreparedStatement | setShort            | 支持，不处理 |
| PreparedStatement | setSQLXML           | 支持，不处理 |
| PreparedStatement | setString           | 支持         |
| PreparedStatement | setTime             | 支持，不处理 |
| PreparedStatement | setTimestamp        | 支持，不处理 |
| PreparedStatement | setUnicodeStream    | 支持，不处理 |
| PreparedStatement | setURL              | 支持，不处理 |
| Statement         |               -      | 支持         |
| ResultSet         | getArray            | 支持，不处理 |
| ResultSet         | getAsciiStream      | 支持，不处理 |
| ResultSet         | getBigDecimal       | 支持         |
| ResultSet         | getBinaryStream     | 支持         |
| ResultSet         | getBlob             | 支持         |
| ResultSet         | getBoolean          | 支持，不处理 |
| ResultSet         | getByte             | 支持，不处理 |
| ResultSet         | getBytes            | 支持         |
| ResultSet         | getCharacterStream  | 支持         |
| ResultSet         | getClob             | 支持         |
| ResultSet         | getCursorName       | 支持         |
| ResultSet         | getDate             | 支持，不处理 |
| ResultSet         | getDouble           | 支持         |
| ResultSet         | getFloat            | 支持         |
| ResultSet         | getInt              | 支持         |
| ResultSet         | getLong             | 支持         |
| ResultSet         | getNCharacterStream | 支持         |
| ResultSet         | getNClob            | 支持         |
| ResultSet         | getNString          | 支持         |
| ResultSet         | getObject           | 支持         |
| ResultSet         | getRef              | 支持，不处理 |
| ResultSet         | getShort            | 支持，不处理 |
| ResultSet         | getSQLXML           | 支持，不处理 |
| ResultSet         | getString           | 支持         |
| ResultSet         | getTime             | 支持，不处理 |
| ResultSet         | getTimestamp        | 支持，不处理 |
| ResultSet         | getUnicodeStream    | 支持，不处理 |
| ResultSet         | getURL              | 支持，不处理 |
| ResultSet         | udpate*             | 支持，不处理 |
