UNPIVOT 是 Oracle 的列转行函数，通过 UNPIVOT 函数，可以快速实现列转行的输出，而不需要用多个 SQL UNION [ALL]  实现。
TDSQL PostgreSQL版（Oracle 兼容）兼容 UNPIVOT 用法。

## 语法
```
SELECT STATEMENT
UNPIVOT( column_name FOR unpivot_column IN ( list of values))
[ ORDER BY { column_name | expr } [, ...] ];
```
    
## 示例
```
postgres=# create table stu_score_b as select stu_name,
max(case when course='CHINESE' then score end) CHINESE,
max(case when course='ENGLISH' then score end) ENGLISH,
max(case when course='MATH' then score end) MATH
from stu_score
group by stu_name;
INSERT 0 3
postgres=# select * from stu_score_b;
  stu_name | chinese | english | math  
----------+---------+---------+-------
  STU_B|   86.00 |   77.00 | 69.00
  STU_C|   80.00 |   82.00 | 88.00
  STU_A|   70.00 |   80.00 | 81.00
(3 rows)
    
postgres=# select *
from stu_score_b   
unpivot ( score for course in (CHINESE ,ENGLISH ,MATH )) 
order by stu_name;
  stu_name | score | course  
----------+-------+---------
  STU_A| 81.00 | MATH
  STU_A| 80.00 | ENGLISH
  STU_A| 70.00 | CHINESE
  STU_B| 86.00 | CHINESE
  STU_B| 77.00 | ENGLISH
  STU_B| 69.00 | MATH
  STU_C| 88.00 | MATH
  STU_C| 82.00 | ENGLISH
  STU_C| 80.00 | CHINESE
(9 rows)
    
postgres=# select stu_name,score,course
from stu_score_b unpivot ( score for course in (CHINESE ,ENGLISH ))
order by stu_name;
  stu_name | score | course  
----------+-------+---------
  STU_A| 70.00 | CHINESE
  STU_A| 80.00 | ENGLISH
  STU_B| 86.00 | CHINESE
  STU_B| 77.00 | ENGLISH
  STU_C| 80.00 | CHINESE
  STU_C| 82.00 | ENGLISH
(6 rows)
```
    
