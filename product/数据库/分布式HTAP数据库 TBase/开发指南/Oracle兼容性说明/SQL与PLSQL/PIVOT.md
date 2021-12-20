PIVOT 是 Oracle 的行转列函数，通过 PIVOT 函数，可以快速实现行转列的输出，而不需要用 DECODE 或 CASE 结合 GROUP BY 复杂的 SQL 实现。

TDSQL PostgreSQL版（Oracle 兼容）兼容 PIVOT 用法。

## 语法
```
SELECT STATEMENT
PIVOT (aggreate_function FOR pivot_column IN ( list of values) )
[ ORDER BY { column_name | expr } [, ...] ];
```
    
## 示例
```
postgres=# create table stu_score (stu_name varchar2(16),course varchar2(16),score number(5,2));
CREATE TABLE
postgres=# insert into stu_score values('STU_A','CHINESE',70);
INSERT 0 1
postgres=# insert into stu_score values('STU_A','ENGLISH',80);
INSERT 0 1
postgres=# insert into stu_score values('STU_A','MATH',81);
INSERT 0 1
postgres=# insert into stu_score values('STU_B','CHINESE',86);
INSERT 0 1
postgres=# insert into stu_score values('STU_B','ENGLISH',77);
INSERT 0 1
postgres=# insert into stu_score values('STU_B','MATH',69);
INSERT 0 1
postgres=# insert into stu_score values('STU_C','CHINESE',80);
INSERT 0 1
postgres=# insert into stu_score values('STU_C','ENGLISH',82);
INSERT 0 1
postgres=# insert into stu_score values('STU_C','MATH',88);
INSERT 0 1
postgres=# select * from stu_score;
  stu_name | course  | score 
----------+---------+-------
  STU_B| CHINESE | 86.00
  STU_B| ENGLISH | 77.00
  STU_B| MATH| 69.00
  STU_C| CHINESE | 80.00
  STU_C| ENGLISH | 82.00
  STU_C| MATH| 88.00
  STU_A| CHINESE | 70.00
  STU_A| ENGLISH | 80.00
  STU_A| MATH| 81.00
(9 rows)
    
postgres=# select * from stu_score
pivot ( max(score) for course in ('CHINESE' as CHINESE,'ENGLISH' as ENGLISH,'MATH' as MATH));
  stu_name | chinese | english | math  
----------+---------+---------+-------
  STU_B|   86.00 |   77.00 | 69.00
  STU_C|   80.00 |   82.00 | 88.00
  STU_A|   70.00 |   80.00 | 81.00
(3 rows)
```
