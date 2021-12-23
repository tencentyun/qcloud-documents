## select语句

### 访问函数

```
postgres=# select md5(random()::text);
        md5         
----------------------------------
 3eb6c0c8f8355f0b0f0cad7a8f0f7491
```



### 数据排序

- **按某一列排序**

 ```
postgres=# INSERT into tdsql_pg (nickname) VALUES('tdsql_pg好');               
INSERT 0 1
postgres=# INSERT into tdsql_pg (id,nickname) VALUES(1,' TDSQL PG版分布式数据库的时代来了');        
INSERT 0 1
postgres=# select * from tdsql_pg order by id;
 id |      nickname      
----+-----------------------------
 1 | hello tdsql_pg
 1 | tdsql_pg分布式数据库的时代来了
 2 | tdsql_pg好
(3 rows)
 ```



- **按第一列排序**

 ```
postgres=# select * from tdsql_pg order by 1;
 id |      nickname      
----+-----------------------------
 1 | hello tdsql_pg
 1 | tdsql_pg分布式数据库的时代来了
 2 | tdsql_pg好
(3 rows)
 ```



- **按id升级排序，再按nickname降序排序**

```
postgres=# select * from tdsql_pg order by id,nickname desc;
 id |      nickname      
----+-----------------------------
 1 | tdsql_pg分布式数据库的时代来了
 1 | hello tdsql_pg
 2 | tdsql_pg好
(3 rows)
```

 效果与上面的语句一样

```
postgres=# select * from tdsql_pg order by 1,2 desc;
 id |      nickname      
----+-----------------------------
 1 | tdsql_pg分布式数据库的时代来了
 1 | hello tdsql_pg
 2 | tdsql_pg好
(3 rows)
```



- **随机排序**

 ```
postgres=# select * from tdsql_pg order by random();
 id |      nickname      
----+-----------------------------
 1 | tdsql_pg分布式数据库的时代来了
 2 | tdsql_pg好
 1 | hello tdsql_pg
(3 rows)
 ```



- **计算排序**

```
postgres=# select * from tdsql_pg order by md5(nickname);
 id |      nickname      
----+-----------------------------
 2 | tdsql_pg好
 1 | tdsql_pg分布式数据库的时代来了
 1 | hello tdsql_pg
(3 rows)
 
```

排序都能用子查询，牛

```
postgres=# select * from tdsql_pg order by (select id from tdsql_pg order by random() limit 1);
 id |      nickname      
----+-----------------------------
 1 | hello tdsql_pg
 2 | tdsql_pg好
 1 | tdsql_pg分布式数据库的时代来了
(3 rows)
```



- **null值排序结果处理**

```
postgres=# insert into tdsql_pg values(4,null);
INSERT 0 1
```

null值记录排在最前面

```
postgres=#  select * from tdsql_pg order by nickname nulls first;
 id |      nickname      
----+-----------------------------
 4 | 
 1 | hello tdsql_pg
 1 | tdsql_pg分布式数据库的时代来了
 2 | tdsql_pg好
(4 rows)

```

null值记录排在最后

```
postgres=#  select * from tdsql_pg order by nickname nulls last; 
 id |      nickname      
----+-----------------------------
 1 | hello tdsql_pg
 1 | tdsql_pg分布式数据库的时代来了
 2 | tdsql_pg好
 4 | 
(4 rows)
```

- **按拼音排序**

```
postgres=# select * from (values ('张三'), ('李四'),('陈五')) t(myname) order by myname;                
 myname 
--------
 张三
 李四
 陈五
(3 rows)

```

 如果不加处理，则按汉字的utf8编码进行排序，不符合中国人使用习惯

```
postgres=# select * from (values ('张三'), ('李四'),('陈五')) t(myname) order by convert(myname::bytea,'UTF-8','GBK');
 myname 
--------
 陈五
 李四
 张三
(3 rows)
 
```

使用convert函数实现汉字按拼音进行排序

```
postgres=# select * from (values ('张三'), ('李四'),('陈五')) t(myname) order by convert_to(myname,'GBK');     
 myname 
--------
 陈五
 李四
 张三
(3 rows)

```

使用convert_to函数实现汉字按拼音进行排序

```
postgres=# select * from (values ('张三'), ('李四'),('陈五')) t(myname) order by myname  collate "zh_CN.utf8";
 myname 
\--------
 陈五
 李四
 张三
(3 rows)
```

通过指定排序规则collact来实现汉字按拼音进行排序

 

### where条件使用

- **单条件查询**

```
postgres=# select * from tdsql_pg where id=1;
 id |      nickname      
----+-----------------------------
 1 | hello tdsql_pg
 1 | tdsql_pg分布式数据库的时代来了
```

- **多条件and**

```
postgres=# select * from tdsql_pg where id=1 and nickname like '%h%';
 id |  nickname  
----+-------------
 1 | hello tdsql_pg
(1 row)
```

- **多条件or**

```
postgres=# select * from tdsql_pg where id=2 or nickname like '%h%';   
 id |  nickname  
----+-------------
 1 | hello tdsql_pg
 2 | tdsql_pg好
(2 rows)
```

- **ilike不区分大小写匹配**

```
postgres=# create table t_ilike(id int,mc text);
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# insert into t_ilike values(1,'tdsql_pg'),(2,'tdsql_pg');
INSERT 0 2
postgres=# select * from t_ilike where mc ilike '%tb%';
 id |  mc  
----+-------
 1 | tdsql_pg
 2 | tdsql_pg
(2 rows)
```

- **where条件也能支持子查询**

 ```
postgres=# select * from tdsql_pg where id=(select (random()*2)::integer from tdsql_pg order by random() limit 1);    
 id | nickname 
----+----------
(0 rows)
 
postgres=# select * from tdsql_pg where id=(select (random()*2)::integer from tdsql_pg order by random() limit 1);    
 id |      nickname      
----+-----------------------------
 1 | hello tdsql_pg
 1 | tdsql_pg分布式数据库的时代来了
(2 rows)
 ```

- **null值查询方法**

```
postgres=# select * from tdsql_pg where nickname is null;
 id | nickname 
----+----------
 4 | 
(1 row)
 
postgres=# select * from tdsql_pg where nickname is not null;
 id |      nickname      
----+-----------------------------
 1 | hello tdsql_pg
 2 | tdsql_pg好
 1 | tdsql_pg分布式数据库的时代来了
(3 rows)
```

- **exists，只要有记录返回就为真**

```
postgres=#  create table t_exists1(id int,mc text);
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
 
postgres=# insert into t_exists1 values(1,'tdsql_pg'),(2,'tdsql_pg');  
INSERT 0 2
 
postgres=# create table t_exists2(id int,mc text); 
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
 
postgres=# insert into t_exists2 values(1,'tdsql_pg'),(1,'tdsql_pg');
INSERT 0 2
 
postgres=# select * from  t_exists1 where  exists(select 1 from t_exists2 where t_exists1.id=t_exists2.id) ;
 id |  mc  
----+-------
 1 | tdsql_pg
(1 row)
```

- **exists等价写法**

```
postgres=# select t_exists1.* from t_exists1,(select distinct id from  t_exists2) as t where t_exists1.id=t.id;;
 id |  mc  
----+-------
 1 | tdsql_pg
(1 row)
```

 

### 分页查询

默认从第一条开始，返回一条记录

```
postgres=# select * from tdsql_pg limit 1;
 id |  nickname  
----+-------------
 1 | hello tdsql_pg
(1 row)
```

使用offset指定从第几条开始，0表示第一条开如，返回1条记录

```
postgres=# select * from tdsql_pg limit 1 offset 0;  
 id |  nickname  
----+-------------
 1 | hello tdsql_pg
(1 row)
```

从第3条开始，返回二条记录

```
postgres=# select * from tdsql_pg limit 1 offset 2;
 id |      nickname      
----+-----------------------------
 1 | tdsql_pg分布式数据库的时代来了
(1 row)
```

上面的语句没有使用排序，返回结果不可预知，使用order by可以获得一个有序的结果

 ```
postgres=# select * from tdsql_pg order by id limit 1 offset 2;
 id | nickname  
----+-----------
 2 | tdsql_pg好
(1 row)
 ```



### 合并多个查询结果

不过虑重复的记录

 ```
postgres=# select * from tdsql_pg union all select * from t_appoint_col;
 id |      nickname      
----+-----------------------------
 1 | hello tdsql_pg
 2 | tdsql_pg好
 1 | tdsql_pg分布式数据库的时代来了
 1 | hello tdsql_pg
(4 rows)
 
 ```

过虑重复的记录

```
postgres=# select * from tdsql_pg union select * from t_appoint_col;   
 id |      nickname      
----+-----------------------------
 1 | tdsql_pg分布式数据库的时代来了
 1 | hello tdsql_pg
 2 | tdsql_pg好
(3 rows)
```

每个子查询分布在合并结果中的使用

```
postgres=# select * from ( select * from tdsql_pg limit 1) as t union all select * from (select * from t_appoint_col limit 1) as t ;
 id |  nickname  
----+-------------
 1 | hello tdsql_pg
 1 | hello tdsql_pg
(2 rows)
```





### 返回两个结果的交集

```
postgres=# create table t_intersect1(id int,mc text);
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
 
postgres=# insert into t_intersect1 values(1,'tdsql_pg'),(2,'tdsql_pg');
INSERT 0 2
 
postgres=# create table t_intersect2(id int,mc text);
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
 
postgres=# insert into t_intersect2 values(1,'tdsql_pg'),(3,'tdsql_pg');
INSERT 0 2
 
postgres=# select * from t_intersect1 INTERSECT select * from t_intersect2;
 id |  mc  
----+-------
 1 | tdsql_pg
(1 row)
```

### 返回两个结果的差集

```
postgres=# create table t_except1(id int,mc text);
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
 
postgres=# insert into t_except1 values(1,'tdsql_pg'),(2,'tdsql_pg');
INSERT 0 2
 
postgres=# create table t_except2(id int,mc text);
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
 
postgres=# insert into t_except2 values(1,'tdsql_pg'),(3,'tdsql_pg');
INSERT 0 2
 
postgres=# select * from t_except1 except select * from t_except2;
 id |  mc  
----+-------
 2 | tdsql_pg
(1 row)
```

### any用法

```
postgres=# create table t_any(id int,mc text);
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
 
postgres=# insert into t_any values(1,'tdsql_pg'),(2,'tdsql_pg');  
INSERT 0 2
 
postgres=# select * from t_any where id>any (select 1 union select 3);
 id |  mc  
----+-------
 2 | tdsql_pg
(1 row)
```

只需要大于其中一个值即为真

### all用法

```
postgres=# create table t_all(id int,mc text);
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# insert into t_all values(2,'tdsql_pg'),(3,'tdsql_pg'); 
INSERT 0 2
 
postgres=# select * from t_all where id>all (select 1 union select 2);   
 id |  mc  
----+-------
 3 | tdsql_pg
(1 row)
 
```

需要大于所有值才为真

### 聚集查询

统计记录数

```
postgres=# select count(1) from tdsql_pg;
 count 
-------
   3
(1 row)
```

统计不重复值的记录表

```
postgres=# select count(distinct id) from tdsql_pg;
 count 
-------
   2
(1 row)
```

求和

```
postgres=# select sum(id) from tdsql_pg;
 sum 
-----
  4
(1 row)
```

求最大值

```
postgres=# select max(id) from tdsql_pg;
 max 
-----
  2
(1 row)
```

求最小值

```
postgres=# select min(id) from tdsql_pg;   
 min 
-----
  1
(1 row)
```

求平均值

```
postgres=# select avg(id) from tdsql_pg;    
    avg     
--------------------
 1.3333333333333333
(1 row)
```





### 多表关联

- **内连接**

```
postgres=# select * from tdsql_pg inner join t_appoint_col on tdsql_pg.id=t_appoint_col.id;  
 id |      nickname      | id |  nickname  
----+-----------------------------+----+-------------
 1 | hello tdsql_pg         |  1 | hello tdsql_pg
 1 | tdsql_pg分布式数据库的时代来了 |  1 | hello tdsql_pg
(2 rows)
 
```

- **左外连接**

```
 postgres=# select * from tdsql_pg left join t_appoint_col on tdsql_pg.id=t_appoint_col.id;     
 id |      nickname      | id |  nickname  
----+-----------------------------+----+-------------
 1 | hello tdsql_pg         |  1 | hello tdsql_pg
 2 | tdsql_pg好          |   | 
 1 | tdsql_pg分布式数据库的时代来了 |  1 | hello tdsql_pg
(3 rows)
```

- **右外连接**

 ```
postgres=# select * from tdsql_pg right join t_appoint_col on tdsql_pg.id=t_appoint_col.id;    
 id |      nickname      | id |  nickname  
----+-----------------------------+----+-------------
 1 | tdsql_pg分布式数据库的时代来了 |  1 | hello tdsql_pg
 1 | hello tdsql_pg         |  1 | hello tdsql_pg
  |               |  5 | Power tdsql_pg
(3 rows)
 ```

- **全连接**

 ```
postgres=# select * from tdsql_pg full join t_appoint_col on tdsql_pg.id=t_appoint_col.id;     
 id |      nickname      | id |  nickname  
----+-----------------------------+----+-------------
 1 | hello tdsql_pg         |  1 | hello tdsql_pg
 2 | tdsql_pg好          |   | 
 1 | tdsql_pg分布式数据库的时代来了 |  1 | hello tdsql_pg
  |               |  5 | Power tdsql_pg
(4 rows)
 ```

### 聚合函数并发计算

- **单核计算**

 ```
postgres=# \timing 
Timing is on.
postgres=# set max_parallel_workers_per_gather to 0;
SET
Time: 0.633 ms
postgres=# select count(1) from t_count;
 count  
----------
 20000000
(1 row)
 
Time: 3777.518 ms (00:03.778)
 ```



- **二核并行**

```
postgres=# set max_parallel_workers_per_gather to 2;
SET
Time: 0.478 ms
postgres=# select count(1) from t_count;       
 count  
----------
 20000000
(1 row)
 
Time: 2166.481 ms (00:02.166)
```

- **四核并行**

 ```
postgres=# set max_parallel_workers_per_gather to 4;
SET
Time: 0.315 ms
postgres=# select count(1) from t_count;       
 count  
----------
 20000000
(1 row)
 
Time: 1162.433 ms (00:01.162)
postgres=# 
 ```

### not in中包含了null，结果全为真

```
postgres=# create table t_not_in(id int,mc text);
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# insert into t_not_in values(1,'tdsql_pg'),(2,'pgxz');
INSERT 0 2
postgres=# select * from t_not_in where id not in (3,5);
 id |  mc  
----+-------
 1 | tdsql_pg
 2 | pgxz
(2 rows)
 
postgres=# select * from t_not_in where id not in (3,5,null);
 id | mc 
----+----
(0 rows)
```

### 只查某个dn的数据

```
postgres=# create table t_direct(id int,mc text);
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# insert into t_direct values(1,'tdsql_pg'),(3,'pgxz');
INSERT 0 2
postgres=# EXECUTE DIRECT ON (dn001) 'select * from t_direct';
 id |  mc  
----+-------
 1 | tdsql_pg
(1 row)
 
postgres=# EXECUTE DIRECT ON (dn002) 'select * from t_direct'; 
 id |  mc  
----+------
 3 | pgxz
(1 row)
 
postgres=# select * from t_direct ;
 id |  mc  
----+-------
 1 | tdsql_pg
 3 | pgxz
(2 rows)
 
postgres=# 
```

### 特殊应用

- **多行变成单行**

 ```
postgres=# create table t_mulcol_tosimplecol(id int,mc text);
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
 
postgres=# insert into t_mulcol_tosimplecol values(1,'tdsql_pg'),(2,'tdsql_pg');  
INSERT 0 2
 
postgres=# select array_to_string(array(select mc from t_mulcol_tosimplecol),',');
 array_to_string 
-----------------
 tdsql_pg,tdsql_pg
(1 row)
 
 ```

- **一列变成多行**

 ```
postgres=# create table t_col_to_mulrow(id int,mc text);
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
 
postgres=# insert into t_col_to_mulrow values(1,'tdsql_pg,tdsql_pg');  
INSERT 0 1
 
postgres=# select regexp_split_to_table((select mc from t_col_to_mulrow where id=1 limit 1), ',');
 
 regexp_split_to_table 
-----------------------
 tdsql_pg
 tdsql_pg
(2 rows)
 ```

### 查询记录所在dn

```
postgres=# select xc_node_id,* from t1;
 xc_node_id | f1 | f2 
------------+----+----
 2142761564 |  1 |  3
 2142761564 |  1 |  3
(2 rows)
 
postgres=# select t1.xc_node_id,pgxc_node.node_name,t1.* from t1,pgxc_node where t1.xc_node_id=pgxc_node.node_id;
 xc_node_id | node_name | f1 | f2 
------------+-----------+----+----
 2142761564 | dn001   |  1 |  3
 2142761564 | dn001   |  1 |  3
(2 rows)
 
postgres=# 
```



### grouping sets/rollup/cube用法

#### group by用法

销售明细表

```
create table t_grouping(id int,dep varchar(20),product varchar(20),num int);
insert into t_grouping values(1,'业务1部','手机',90);
insert into t_grouping values(2,'业务1部','电脑',80);
insert into t_grouping values(3,'业务1部','手机',70);
insert into t_grouping values(4,'业务2部','电脑',60);
insert into t_grouping values(5,'业务2部','手机',50);
insert into t_grouping values(6,'业务2部','电脑',60);
insert into t_grouping values(7,'业务3部','手机',70);
insert into t_grouping values(8,'业务3部','电脑',80);
insert into t_grouping values(9,'业务3部','手机',90);

```

```
postgres=# select dep,product,sum(num) from t_grouping group by dep,product order by dep,product;
  dep  | product | sum 
---------+---------+-----
 业务1部 | 电脑   |  80
 业务1部 | 手机   | 160
 业务2部 | 电脑   | 120
 业务2部 | 手机   |  50
 业务3部 | 电脑   |  80
 业务3部 | 手机   | 160
```

按dep,product两级汇总分数

#### 使用grouping sets

> grouping set说明：GROUPING SETS的每个子列表可以指定零个或多个列或表达式，并且与其直接在GROUP BY子句中的解释方式相同。 一个空的分组集合意味着所有的行都被聚合到一个组中

如按name,class单级分别汇总，再计算一个总分

```
postgres=# select dep,product,sum(num) from t_grouping group by grouping sets((dep),(product),()) order by dep,product;
  dep  | product | sum 
---------+---------+-----
 业务1部 |     | 240
 业务2部 |     | 170
 业务3部 |     | 240
     | 电脑   | 280
     | 手机   | 370
     |     | 650
 
```

使用grouping sets代替group by 

```
postgres=# select dep,product,sum(num) from t_grouping group by grouping sets((dep,product)) order by dep,product;
  dep  | product | sum 
---------+---------+-----
 业务1部 | 电脑   |  80
 业务1部 | 手机   | 160
 业务2部 | 电脑   | 120
 业务2部 | 手机   |  50
 业务3部 | 电脑   |  80
 业务3部 | 手机   | 160
```



#### 使用rollup

 rollup((a),(b))等价于grouping sets((a,b),(a),())

 ```
postgres=# select dep,product,sum(num) from t_grouping group by rollup((dep),(product)) order by dep,product;
  dep  | product | sum 
---------+---------+-----
 业务1部 | 电脑   |  80
 业务1部 | 手机   | 160
 业务1部 |     | 240
 业务2部 | 电脑   | 120
 业务2部 | 手机   |  50
 业务2部 |     | 170
 业务3部 | 电脑   |  80
 业务3部 | 手机   | 160
 业务3部 |     | 240
     |     | 650
 ```



该功能等价于grouping sets((dep, product),( dep),())

```
postgres=# select dep,product,sum(num) from t_grouping group by grouping sets((dep, product),( dep),()) order by dep,product;
  dep  | product | sum 
---------+---------+-----
 业务1部 | 电脑   |  80
 业务1部 | 手机   | 160
 业务1部 |     | 240
 业务2部 | 电脑   | 120
 业务2部 | 手机   |  50
 业务2部 |     | 170
 业务3部 | 电脑   |  80
 业务3部 | 手机   | 160
 业务3部 |     | 240
     |     | 650
```



#### 使用cube

cube((a),(b))等价于grouping sets((a,b),(a),(b),()) 

```
postgres=# select dep,product,sum(num) from t_grouping group by cube((dep),(product)) order by dep,product;
  dep  | product | sum 
---------+---------+-----
 业务1部 | 电脑   |  80
 业务1部 | 手机   | 160
 业务1部 |     | 240
 业务2部 | 电脑   | 120
 业务2部 | 手机   |  50
 业务2部 |     | 170
 业务3部 | 电脑   |  80
 业务3部 | 手机   | 160
 业务3部 |     | 240
     | 电脑   | 280
     | 手机   | 370
     |     | 650
```

该功能等价于grouping sets((name,class),(name),(class),())

```
postgres=# select dep,product,sum(num) from t_grouping group by grouping sets((dep,product),(dep),(product),()) order by dep,product;
  dep  | product | sum 
---------+---------+-----
 业务1部 | 电脑   |  80
 业务1部 | 手机   | 160
 业务1部 |     | 240
 业务2部 | 电脑   | 120
 业务2部 | 手机   |  50
 业务2部 |     | 170
 业务3部 | 电脑   |  80
 业务3部 | 手机   | 160
 业务3部 |     | 240
     | 电脑   | 280
     | 手机   | 370
     |     | 650
```


