TDSQL 支持分表，通过分表键（shardkey）把一个大表水平拆分到多个数据库，下面详细介绍分表的方法。

## 如何选择分表键
一旦定好分表键，就不能轻易修改，因此开发人员需要提前评估。选择分表键的时候主要考虑两个维度：
- 通过该分表键能否对数据进行均衡的存储和访问。
- 多个相关联的表能否使用同一个分表键。（相同分表键数据会存储在同一个物理分片中，大多数的业务逻辑需要进行 `join` 时，可无需走分布式事务逻辑而直接在单节点内执行，效率大大提升。）


 **例子：**假设业务有两张表，一个用于记录用户的基本信息，一个用于用户的订单信息，此时若选取用户 ID 作为分表键，则理论数据分布和访问将会比较均衡，同时单个用户对应的基本信息和订单信息均会在一个后端数据库中，方便后续的 join 等操作。


## 创建一张分表
分表创建时必须指定shardkey的值（通常写作建表语句最后面），该值为表中的一个字段名字，会用于后续sql的路由选择：

```
	mysql> create table test1 ( a int, b int, c char(20),primary key (a,b),unique key u_1(a,c) ) shardkey=a;
	Query OK, 0 rows affected (0.07 sec)

```
由于在TDSQL中，shardkey对应后端数据库的分区字段，因此必须是主键和所有唯一索引的一部分，否则没法创建表：

```
	mysql> create table test1 ( a int, b int, c char(20),primary key (a,b),unique key u_1(a,c),unique key u_2(b,c) ) shardkey=a;;

	此时有一个唯一索引u_2不包含shardkey，没法创建表，会报如下错误：
	ERROR 1105 (HY000): A UNIQUE INDEX must include all columns in the table's partitioning function

	例如正确的写法：
	 create table test1 ( a int, b int, c char(20),primary key (a,b),unique key u_1(a,c) ) shardkey=a;;

```	
因为主键索引或者unique key索引意味着需要全局唯一，而要实现全局唯一索引则必须包含shard key字段



除了上面的限制外，shardkey字段还有如下要求：

	1.shardkey字段的类型必须是int,bigint,smallint/char/varchar
	2.shardkey字段的值不应该有中文，网关不会转换字符集，所以不同字符集可能会路由到不同的分区
	3.不要update shardkey字段的值
	4.shardkey=a 放在sql的最后面
	5.访问数据尽量都能带上shardkey字段，这个不是强制要求，但是不带shardkey的sql会路由到所有节点，影响性能。

>**注意：**
>`shardkey` 是系统标记分表键的关键字，不可占用。
>`shardkey=noshardkey_allset` 定义该表为广播表的关键字，广播表表示该表不分表，但会在每个物理分片中都存储一份。

## 常见 DML 操作

使用分表时，对 DML 有一定的要求，具体如下(下面的例子中 a 为 shardkey )。

### select 最好带上分表键
由于分布式路由默认采用 hash 方式，`select` 最好带上分表键（shardkey）。
- 若是`=`或者`in`，路由将自动跳转到对应分片，此时效率最高。
- 如下两条 sql 根据 shardkey 的值直接可以发送到对应的数据库，通常 5 ms 内可以处理完成。
```
	mysql> select a,b,c from test.test1 where a=2 order by b;
	mysql> select a,b,c from test.test1 where a in (2) order by b;
```
- 若无`=`或者`in`，分布式系统将自动全表扫描，然后在网关进行结果集聚合，此时效率较低：
- 如下两条 sql 都会发到所有的后端数据库，然后需要对数据进行额外的汇总排序，通常要 5-20 ms 才能处理完成。
```
	mysql> select a,b,c from test.test1 where a>2 order by b;
	mysql> select a,b,c from test.test1 where c=2 order by b;
```

### insert/replace 字段必须包含分表键

`insert/replace` 字段必须包含分表键（shardkey），否则路由不知道应该将数据插入到哪个物理分片，会拒绝执行该 sql。
> **注意：**
> 使用广播表或单表时除外。

```
	mysql> insert into test.test1 (b,c) values(4,"record3");
	ERROR 1105 (07000): Proxy Warning - sql have no shardkey

	mysql> insert into test.test1 (a,c) values(4,"record3");
	Query OK, 1 row affected (0.01 sec)
```

### delete/update 字段必须包含分表键

delete/update 时为了安全考虑，执行该类 sql 的时候必须带有 `where` 条件，系统拒绝执行该 sql 命令,`where` 条件最好也和 `select` 一样带上分表键（shardkey）。
>**注意：**
>使用广播表或单表时除外。

```
	mysql> delete from test.test1;
	ERROR 1005 (07000): Proxy Warning - sql is not legal,tokenizer_gram went wrong
	mysql> delete from test.test1 where a=1;
	Query OK, 1 row affected (0.01 sec)
```

### 修改分表键值
同时 `update` 不能修改分表键（shardkey） 字段的值，需要的话先 `insert` 再 `delete`。
>不能更换 shardkey 字段类型、修改字段名称、删除 shardkey 字段、或更换 shardkey 字段，除非您新建一个表。

```
	mysql> update test.test1 set a=10 where d=1;
	ERROR 7013 (HY000): Proxy ERROR:combine_sql_key return null,something went wrong
	mysql> update test.test1 set d=1 where a=1;
	Query OK, 0 rows affected (0.00 sec)
```

## 常见错误

- 表没有主键：
```
	mysql> create table test.e1 ( a int ,b int) shardkey=a;
	ERROR 1105 (HY000): This table type requires a primary key
```

- 主键或者唯一键没有包含分表键（shardkey）：
```
	mysql> create table test.e2 ( a int not null,b int not null, c char(20) not null,primary key(a,b) ) shardkey=c;
	ERROR 1105 (HY000): A PRIMARY KEY must include all columns in the table's partitioning function
```

- 分表键（shardkey）的拼写错误或者列名错误：
```
	mysql> create table test.e3 ( a int key,b int,c char(20)) shardkey1=d;
	ERROR 1911 (HY000): Unknown option 'shardkey1'
	mysql> create table test.e4 ( a int key,b int,c char(20)) shardkey=d;
	ERROR 7008 (HY000): Proxy ERROR:shardkey must be one of the column
```
