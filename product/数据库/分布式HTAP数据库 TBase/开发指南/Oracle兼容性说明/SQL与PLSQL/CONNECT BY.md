`CONNECT BY` 级联查询，常用于对具有树状结构的记录查询某一节点的所有子孙节点或所有祖辈节点，或通过 `CONNECT BY`  结合 `LEVEL` 来构造数据。

`LEVEL` 关键字，代表树形结构中的层级编号：第一层为数字1，第二层为数字2，依次递增。

`CONNECT_BY_ROOT` 方法，能够获取第一层结点结果集中的任意字段的值。

## 语法
```
SELECT { * | COLUMN | expression ,...} 
FROM table [START WITH condition1]
CONNECT BY [PRIOR] id=parentid
```
一般用来查找存在父子关系的数据，也就是树形结构的数据；其返还的数据也能够明确的区分出每一层的数据。

`start with condition1` 是用于限制第一层数据，或者叫根节点数据，以该部分数据为基础来查找第二层数据，然后以第二层数据查找第三层数据，以此类推。

`connect by [prior] id=parentid` 用于指明 Oracle 在查找数据时以何种关系进行查找。例如，查找第二层的数据时使用第一层数据的 ID 与表中记录的 `parentid` 字段进行匹配，如果该条件成立，那么查找出的数据便是第二层数据，同理查找第三层、第四层……都是按这样的方式进行匹配。

另一种写法：
```
SELECT { * | COLUMN | expression ,...} 
FROM table [START WITH condition1]
CONNECT BY id=[PRIOR] parentid
```
这种用法表示从下往上查找数据，可以理解为从叶子节点往上查找父级节点，用第一层数据的 `parentid` 与表记录中的 `id` 进行匹配。若匹配成功，那么查找出的便是第二层数据。

## 使用限制
- `CONNECT BY` 用法较多，当前 TDSQL PostgreSQL 版（Oracle 兼容）能支持常用的写法，某些写法可能不支持。
- 暂时不支持 `CONNECT_BY_ROOT` 方法。
- 暂不支持基于临时表的 `CONNECT BY`。
- `SELECT *` 输出的字段中也包括隐藏字段 `ctid`、`xc_node_id`、`tableoid`、`_level_1`，需要根据需要输出指定字段。
- `CONNECT BY` 和 `rownum` 结合计算，可能会存在逻辑错误。

## 示例
```
postgres=# create table tab_test (id int, fid int,remark varchar(16));
CREATE TABLE
postgres=# insert into tab_test values(0,-1,'根节点');
INSERT 0 1
postgres=# insert into tab_test values(1,0,'第二层节点1');
INSERT 0 1
postgres=# insert into tab_test values(2,0,'第二层节点2');
INSERT 0 1
postgres=# insert into tab_test values(3,1,'第三层节点1');
INSERT 0 1
postgres=# insert into tab_test values(4,1,'第三层节点2');
INSERT 0 1
  
1）从根节点查找叶子节点
postgres=# select t.id,t.fid,t.remark, level
  from tab_test t
  start with t.id = 0
connect by prior t.id = t.fid;
  id | fid |   remark| level 
----+-----+-------------+-------
  0 |  -1 | 根节点  | 1
  1 |   0 | 第二层节点1 | 2
  2 |   0 | 第二层节点2 | 2
  3 |   1 | 第三层节点1 | 3
  4 |   1 | 第三层节点2 | 3
(5 rows)
    
2）从叶子节点查询上层节点
postgres=# select t.id,t.fid,t.remark, level
  from tab_test t
  start with t.id = 4
connect by t.id = prior t.fid;
  id | fid |   remark| level 
----+-----+-------------+-------
  4 |   1 | 第三层节点2 | 1
  1 |   0 | 第二层节点1 | 2
  0 |  -1 | 根节点  | 3
(3 rows)
postgres=# select t.id,t.fid,t.remark, level
  from tab_test t
  start with t.id = 4
connect by prior t.fid = t.id;
  id | fid |   remark| level 
----+-----+-------------+-------
  4 |   1 | 第三层节点2 | 1
  1 |   0 | 第二层节点1 | 2
  0 |  -1 | 根节点  | 3
(3 rows)
    
3）生成数字序列结果集
postgres=# select rownum from dual connect by rownum<=10;
  rownum 
--------
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
(10 rows)
postgres=# select rownum from dual connect by level<=10;
  rownum 
--------
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
(10 rows)
    
4）字符串分割，由一行变为多行
postgres=# select REGEXP_SUBSTR('01#02#03#04', '[^#]+', 1, rownum::int) as newport 
from dual connect by rownum <= REGEXP_COUNT('01#02#03#04', '[^#]+');
  newport 
---------
  01
  02
  03
  04
(4 rows)
    
5）暂不支持临时表的 connect by
postgres=# select t.*, level
  from (select 1 as num from dual
union
select 2 as num from dual
) t
connect by level <= 3;
ERROR:  connect by support one table yet
```
