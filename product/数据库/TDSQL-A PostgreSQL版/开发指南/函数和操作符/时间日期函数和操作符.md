## 日期/时间操作符
| **操作符** | **示例**                                                    | **结果**                        |
| ---------- | ----------------------------------------------------------- | ------------------------------- |
| +          | date '2001-09-28' + integer '7'                             | date '2001-10-05'               |
| +          | date '2001-09-28' + interval '1 hour'                       | timestamp '2001-09-28 01:00:00' |
| +          | date '2001-09-28' + time '03:00'                            | timestamp '2001-09-28 03:00:00' |
| +          | interval '1 day' + interval '1 hour'                        | interval '1 day 01:00:00'       |
| +          | timestamp '2001-09-28 01:00' + interval '23 hours'          | timestamp '2001-09-29 00:00:00' |
| +          | time '01:00' + interval '3 hours'                           | time '04:00:00'                 |
| -          | - interval '23 hours'                                       | interval '-23:00:00'            |
| -          | date '2001-10-01' - date '2001-09-28'                       | integer '3' (days)            |
| -          | date '2001-10-01' - integer '7'                             | date '2001-09-24'               |
| -          | date '2001-09-28' - interval '1 hour'                       | timestamp '2001-09-27 23:00:00' |
| -          | time '05:00' - time '03:00'                                 | interval '02:00:00'             |
| -          | time '05:00' - interval '2 hours'                           | time '03:00:00'                 |
| -          | timestamp '2001-09-28 23:00' - interval '23 hours'          | timestamp '2001-09-28 00:00:00' |
| -          | interval '1 day' - interval '1 hour'                        | interval '1 day -01:00:00'      |
| -          | timestamp '2001-09-29 03:00' - timestamp '2001-09-27 12:00' | interval '1 day 15:00:00'       |
| *          | 900 * interval '1 second'                                   | interval '00:15:00'             |
| *          | 21 * interval '1 day'                                       | interval '21 days'              |
| *          | double precision '3.5' * interval '1 hour'                  | interval '03:30:00'             |
| /          | interval '1 hour' / double precision '1.5'                  | interval '00:40:00'             |

## 日期/时间函数
| **函数**                                                     | **返回值类型**           | **描述**                                                     |
| ------------------------------------------------ | ------------------------ | ----------------------------------------- |
| age(timestamp,timestamp)                   | interval                 | 减去参数，生成一个使用年、月的符号化的结果        |
| age(timestamp)                                               | interval                 | 从 current_date 减去                           |
| clock_timestamp()                                            | timestamp with time zone | 当前日期和时间                              |
| current_date                                                 | date                     | 当前日期                                     |
| current_time                                                 | time with time zone      | 当前时间                              |
| current_timestamp                                            | timestamp with time zone | 当前日期和时间                         |
| date_part(text,timestamp)                                    | double precision         | 获得子域                            |
| date_part(text,interval)                                     | double precision         | 获得子域                                |
| date_trunc(text,timestamp)                                   | timestamp                | 截断到指定精度                         |
| date_trunc(text,interval)                                    | interval                 | 截断到指定精度                          |
| extract(field from timestamp)                                | double precision         | 获得子域                                |
| extract(field from interval)                                 | double precision         | 获得子域                           |
| isfinite(date)                                               | bool                     | 测试有限日期                     |
| isfinite(timestamp)                                          | bool                     | 测试有限时间戳                           |
| isfinite(interval)                                           | bool                     | 测试有限间隔                                 |
| justify_days(interval)                       | interval                 | 调整间隔，30天时间周期可以表示为月                     |
| justify_hours(interval)                      | interval                 | 调整间隔，24小时时间周期可以表示为日                         |
| justif_interval(interval)                                    | interval                 | 调整间隔                                                     |
| localtime                                                    | time                     | 当前时间                                                     |
| localtimestamp                                | timestamp                | 当前日期和时间                                               |
| make_date(year int,   month int,  day int)       | date         | 从年、月、日创建日期                 |
| make_interval(  years int DEFAULT 0,   months int DEFAULT 0,   weeksint DEFAULT 0,   days int DEFAULT 0,   hours int DEFAULT 0,   minsint DEFAULT 0,   secs double precision   DEFAULT 0.0) | interval                 | 从年、月、周、日、时、分、秒创建 interval         |
| make_time(hour int,   min int,  sec double precision) | time           | 从时、分、秒创建时间                     |
| make_timestamp(year int,   monthint,   day int,   hour int,   minint, sec double precision) | timestamp         | 从年、月、日、时、分、秒创建时间戳                 |
| make_timestamptz(year int,  month int,   day int,   hour int,  min int,  sec double precision,   [ timezone text ]) | timestamp with time zone | 从年、月、日、时、分、秒创建带时区的时间戳，如果没有指定 timezone，则使用当前时区 |
| now()                                                        | timestamp with time zone | 当前日期和时间                        |
| statement_timestamp()                                        | timestamp with time zone | 当前日期和时间               |
| timeofday()                                                  | text                     | 当前日期和时间                                               |
| transaction_timestamp()                                      | timestamp with time zone | 当前日期和时间                           |
| to_timestamp(double precision)             | timestamp with time zone | 把 UNIX 时间转换成 timestamp                |

## OVERLAPS
```
(start1, end1) OVERLAPS (start2, end2)
(start1, length1) OVERLAPS (start2, length2)
```
操作符 OVERLAPS 通过如上两个表达式，在两个时间域重叠的时候得到真，不重叠时得到假。
示例：
```
postgres=# SELECT (DATE '2001-02-16', DATE '2001-12-21') OVERLAPS
postgres-#    (DATE '2001-10-30', DATE '2002-10-30');
 overlaps 
----------
 t
(1 row)

postgres=# SELECT (DATE '2001-02-16', INTERVAL '100 days') OVERLAPS
postgres-#    (DATE '2001-10-30', DATE '2002-10-30');
 overlaps 
----------
 f
(1 row)
```

## EXTRACT
```
EXTRACT(field FROM source)
```
EXTRACT 函数从日期/时间值中抽取子域。
- source 必须是一个类型 timestamp、time 或 interval 的值表达式。
- field 是一个标识符或者字符串，它指定从源值中抽取的域。

EXTRACT 函数返回类型为 double precision 的值。
示例：
```
postgres=# SELECT EXTRACT(DAY FROM TIMESTAMP '2001-02-16 20:38:40');
 date_part 
-----------
    16
(1 row)
 
postgres=# SELECT EXTRACT(DECADE FROM TIMESTAMP '2001-02-16 20:38:40');
 date_part 
-----------
    200
(1 row)
 
postgres=# SELECT EXTRACT(DOY FROM TIMESTAMP '2001-02-16 20:38:40');
 date_part 
-----------
    47
(1 row)
 
postgres=# SELECT EXTRACT(HOUR FROM TIMESTAMP '2001-02-16 20:38:40');
 date_part 
-----------
    20
(1 row)
```

## DATE_TRUNC
```
date_trunc('field', source)
```
DATE_TRUNC 函数在概念上和用于数字的 trunc 函数类似。
- source 是类型 timestamp 或 interval 的值表达式。
- field 指定对输入值选用什么样的精度进行截断，有效值为：microseconds、milliseconds、second、minute、hour、day、week、month、quarter、year、decade、century、millennium。

返回值是 timestamp 类型或者所有小于选定的精度的域都设置为零的 interval。
示例：
```
postgres=# SELECT date_trunc('hour', TIMESTAMP '2001-02-16 20:38:40');
   date_trunc   
---------------------
 2001-02-16 20:00:00
(1 row)

postgres=# SELECT date_trunc('year', TIMESTAMP '2001-02-16 20:38:40');
   date_trunc   
---------------------
 2001-01-01 00:00:00
(1 row)
```

## AT TIME ZONE
AT TIME ZONE 结构允许把时间戳转换成不同的时区。
示例：
```
postgres=# SELECT TIMESTAMP '2001-02-16 20:38:40' AT TIME ZONE 'MST';
    timezone    
------------------------
 2001-02-17 11:38:40+08
(1 row)
 
postgres=# SELECT TIMESTAMP WITH TIME ZONE '2001-02-16 20:38:40-05' AT TIME ZONE 'MST';
    timezone   
---------------------
 2001-02-16 18:38:40
(1 row)
```
第一个例子接受一个无时区的时间，戳然后把它解释成 MST 时间（UTC-7），然后这个时间转换为 PST（UTC-8）来显示。 第二个例子接受一个指定为 EST（UTC-5）的时间戳，然后把它转换成 MST（UTC-7）的当地时间。
函数 timezone(zone,timestamp) 等效于 SQL 兼容的结构 timestamp AT TIME ZONE zone。

## 当前日期/时间
如下函数可以获取当前日期和时间：
```
CURRENT_DATE
CURRENT_TIME
CURRENT_TIMESTAMP
CURRENT_TIME(precision)
CURRENT_TIMESTAMP(precision)
LOCALTIME
LOCALTIMESTAMP
LOCALTIME(precision)
LOCALTIMESTAMP(precision)
```

## 延时执行
通过如下函数可以让服务器进程延时执行：
```
pg_sleep(seconds)
pg_sleep_for(interval)
pg_sleep_until(timestamp with time zone)
```
pg_sleep 让当前的会话进程休眠 seconds 秒以后再执行。
seconds 是一个 double precision 类型的值，所以可以指定带小数的秒数。
pg_sleep_for 是针对用 interval 指定的较长休眠时间的函数。
pg_sleep_until 则可以用来休眠到一个指定的时刻唤醒。
示例：
```
SELECT pg_sleep(1.5);
SELECT pg_sleep_for('5 minutes');
SELECT pg_sleep_until('tomorrow 03:00');
```
