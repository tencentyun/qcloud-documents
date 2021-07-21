
DBMS_RANDOM 包用于产生随机值。DBMS_RANDOM 中可以使用的存储过程及函数如下表所示：

| 存储过程/函数 | 描述                                                         |
| ------------- | ------------------------------------------------------------ |
| \*INITIALIZE   | 用一个种子值来初始化 DBMS_RANDOM                              |
| NORMAL        | 返回服从正态分布的一组数                                     |
| \*RANDOM       | 返回值的范围为： [-2^31, 2^31)，返回的是整数                 |
| \*SEED         | 功能和 INITIALIZE 函数类似，实际上，INITIALIZE 函数被淘汰，推荐的替代函数即是 SEED 函数。与 INITIALIZE 函数不同的是，SEED 函数同时支持数值和字符作为种子值，而 INITIALIZE 函数只支持数值 |
| \*STRING       | 随机生成字符串                                               |
| \*TERMINATE    | 在使用完 DBMS_RANDOM 包后，用该函数进行终止                    |
| \*VALUE        | 随机返回数值                                                 |

示例：
```
Create table random_t1(col1 int,col2 numeric,col3 numeric,col4 numeric,col5  numeric);
Create table random_t2 as select * from random_t1;
begin
perform dbms_random.initialize(100);
for i in 1..100 loop
insert into random_t1 values(i,dbms_random.normal(),dbms_random.random(),dbms_random.value(),dbms_random.value(10,20));
end loop;
end;
/
begin
perform dbms_random.initialize(100);
for i in 1..100 loop
insert into random_t2 values(i,dbms_random.normal(),dbms_random.random(),dbms_random.value(),dbms_random.value(10,20));
end loop;
end;
/
select * from random_t1 minus select * from random_t2;
Drop table if exists random_t1;
Drop table if exists random_t2;
```
   
