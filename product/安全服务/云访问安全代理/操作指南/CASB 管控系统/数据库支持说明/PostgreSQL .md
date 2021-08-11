## 对数据库字段类型的支持
目前 PostgreSQL 支持的数据库版本为 **postgre 9.3.5**，支持的字段类型如下：

| 字段类型                                | 支持情况                                                     | 可选算法 |
| --------------------------------------- | ------------------------------------------------------------ | -------- |
| character varying(n), varchar(n)        | <li>支持</li><li>加密结果大于当前Char长度限制，直接存明文</li> | AES/SM4  |
| character(n), char(n)                   | 支持                                                         | AES/SM4  |
| bytea                                   | 支持                                                         | AES/SM4  |
| text                                    | 支持                                                         | AES/SM4  |
| smallint                                | 不支持                                                       |          |
| integer                                 | 不支持                                                       |          |
| bigint                                  | 不支持                                                       |          |
| decimal                                 | 不支持                                                       |          |
| numeric                                 | 不支持                                                       |          |
| real                                    | 不支持                                                       |          |
| double precision                        | 不支持                                                       |          |
| smallserial                             | 不支持                                                       |          |
| serial                                  | 不支持                                                       |          |
| bigserial                               | 不支持                                                       |          |
| money8                                  | 不支持                                                       |          |
| timestamp [ (p) ] [ without time zone ] | 不支持                                                       |          |
| timestamp [ (p) ] with time zone        | 不支持                                                       |          |
| date                                    | 不支持                                                       |          |
| time [ (p) ] [ without time zone ]      | 不支持                                                       |          |
| time [ (p) ] with time zone             | 不支持                                                       |          |
| interval [ fields ] [ (p) ]             | 不支持                                                       |          |
| boolean                                 | 不支持                                                       |          |
| enum                                    | 不支持                                                       |          |
| point                                   | 不支持                                                       |          |
| line                                    | 不支持                                                       |          |
| lseg                                    | 不支持                                                       |          |
| box                                     | 不支持                                                       |          |
| path                                    | 不支持                                                       |          |
| path                                    | 不支持                                                       |          |
| polygon                                 | 不支持                                                       |          |
| circle                                  | 不支持                                                       |          |
| cidr                                    | 不支持                                                       |          |
| inet                                    | 不支持                                                       |          |
| macaddr                                 | 不支持                                                       |          |
| bit(n)                                  | 不支持                                                       |          |
| varying(n)                              | 不支持                                                       |          |
| tsvector                                | 不支持                                                       |          |
| tsquery                                 | 不支持                                                       |          |
| json                                    | 不支持                                                       |          |
| jsonb                                   | 不支持                                                       |          |
| jsonpath                                | 不支持                                                       |          |
| int4range                               | 不支持                                                       |          |
| int8range                               | 不支持                                                       |          |
| numrange                                | 不支持                                                       |          |
| tsrange                                 | 不支持                                                       |          |
| tstzrange                               | 不支持                                                       |          |
| daterange                               | 不支持                                                       |          |
| oid                                     | 不支持                                                       |          |
| regproc                                 | 不支持                                                       |          |
| regprocedure                            | 不支持                                                       |          |
| regoper                                 | 不支持                                                       |          |
| regoperator                             | 不支持                                                       |          |
| regclass                                | 不支持                                                       |          |
| regtype                                 | 不支持                                                       |          |
| regconfig                               | 不支持                                                       |          |
| regdictionary                           | 不支持                                                       |          |

## 对 SQL 语句的支持

对数据库查询语句的支持情况如下：

- **插入语句**：

| 类型           | 支持情况 | SQL 样例                                                     |
| -------------- | -------- | ------------------------------------------------------------ |
| 不指定列插入   | 支持     | INSERT INTO public.table_a VALUES (1,1,'n1','a1'), (2,1, 'n1','a1'); |
| 指定列插入     | 支持     | INSERT INTO public.table_a  VALUES (2,1 ,'n2','a2');         |
| 指定列写入     | 支持     | INSERT INTO public.table_a (id, col1, col2,col3) VALUES (1, 1,'n1','a1'); |
| 指定列批量写入 | 支持     | INSERT INTO public.table_a (id,col1, col2,col3) VALUES (1,1,'n1','a1'), (2,1,'n1','a1'); |

- **删除语句**：

| 类型                                       | 支持情况 | SQL 样例                                                     |
| ------------------------------------------ | -------- | ------------------------------------------------------------ |
| 等值匹配删除，策略配置在其中某个条件字段上 | 支持     | delete from public.table_a where col2 != 'n2' and id != 2;   |
| 带 in 的删除，策略配置在 in 字段上         | 支持     | delete from public.table_a where id in (1,2);                  |
| 带子查询的删除，策略在子查询的条件字段上   | 支持     | select * from table_a t1 where t1.col2 in (select col2 from table_b) and t1.id = 1; |


- **更新语句**：


| 类型                 | 支持情况 | SQL 样例                                                 |
| -------------------- | -------- | -------------------------------------------------------- |
| 策略配置在查询条件上 | 支持     | UPDATE public.table_a SET id=1, col1='c11' where col2='c; |
| 策略配置在更新字段上 | 支持     | UPDATE public.table_a SET id=1, col1='c11' where id=1;   |

- **查询语句**：

| 类型                                                   | 支持情况                 | SQL 样例                                                     |
| ------------------------------------------------------ | ------------------------ | ------------------------------------------------------------ |
| 对 select * 语法的支持                                 | 支持                     | select * from public.table_a;                                |
| 条件字段等值匹配                                       | 支持                     | select * from public.table_a where col2 != 'n2' and id != 2; |
| 条件字段模糊匹配                                       | 支持                     | select * from public.table_a where col2 like 'n%';           |
| 条件字段范围查询                                       | 不支持                   | select * from public.table_a where col2 > 'n0'               |
| 条件字段带函数                                         | 不支持                   | select col1 from  table_a where substr(col1,0,2) = 'aa';     |
| 条件字段带 in 操作                                     | 支持                     | select * from public.table_a where id in (1,2)               |
| 条件字段为函数参数                                     | 不支持                   | select id, lower(col2) from public.table_a ta ;              |
| 目标字段函数参数为加策略字段                           | 不支持                   | select  concat(tft.col2 , 2, NULL, 22) from public.table_a tft ; |
| SQL 语句中的表使用别名，选择字段及查询条件通过别名指定 | 支持                     | select tft.id, tft.col1, tft.col2, tft.col3 from public.table_a tft  where tft.id=1; |
| 关联查询时使用 select  *                               | 支持                     | select * from table_a t1 inner join table_b t2 on t1.id = t2.id and t1.col2 = t2.col2 where t1.id = 1; |
| 子查询-简单语法子查询，策略在子查询条件语句上          | 支持                     | select * from table_a t1 where t1.col2 in (select col2 from table_a) and t1.id = 1; |
| 子查询-子查询中策略字段作为关联条件或条件字段          | 支持                     | select t1.id, t1.col1, t1.col2, t1.col3 from table_a t1 inner join table_b t2 on t1.id = t2.id and t1.col2 = t2.col2 where t1.id = 1 and t2.col2 = 'n1'; |
| 子查询-结果集带有子查询字段并是策略字段                | 支持                     | select t1.id, t1.col1, t1.col2, t2.col3 from table_a t1 inner join table_b t2 on t1.id = t2.id and t1.col2 = t2.col2 where t1.id = 1 and t2.col2 = 'n1'; |
| 对 exist 关键字的支持                                  | 支持                     | select * from table_a tft  where exists (select 1 from table_b tft2 where tft2.id = tft.id and tft2.col2='n1'); |
| 对 group by 语法的支持                                 | 支持                     | select col2, count(1) from table_a tft group by col2;        |
| 对 Union 关键字的支持                                  | 支持 策略字段 按照基础表 | select id, col1 from public.table_a ta  union select id, col1 from public.table_b tb ; |
| 对 order by 的支持                                     | 支持非加解密字段         | select id, col2 from table_a tft order by id desc limit 1;<br>select id, col2 from table_a tft order by lower(col2); |
| 常量查询                                               | 支持                     | select version();                                            |
| 临时表                                                 | 不支持                   |                                                              |

## 其他注意事项

### 数据库连接

目前不支持 SSL 连接，客户端字符集支持 UTF-8。客户端建立连接时必须指定如下参数 client_encoding='utf8'，sslmode=disable。

```
## python
conn=psycopg2.connect("dbname='foo' user='dbuser' password='mypass' client_encoding='utf8' sslmode='disable' ")
```
