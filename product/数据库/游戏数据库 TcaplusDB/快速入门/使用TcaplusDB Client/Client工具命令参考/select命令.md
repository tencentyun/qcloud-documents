
## 简介
用户可以使用 select 命令从数据库中获取指定的整条记录的值或部分记录的部分字段的值，如果没有匹配的记录，将会返回错误。

## 语法
```
select key1, key2, key3, value1, value2 [into result.csv] from table where key1 = 1 and key2 = "abc" [and -index = 1] [\P] [\G] [using tdr]
select * [into result.xml] from table where key1 = 1 and key2 = "abc" [and -index = 1] using tdr [\P];
```

## 参数

|  参数          | Protobuf                                      | TDR                             | 必填项       |
| --------- | ---------------------------------------- | -------------------------------------------- | ------------ |
| table     | 表格的名字                                                   | 表格的名字                              | 是           |
| key       | 主键字段名，支持分布式索引查询，可填入部分 key 值       | 主键字段名，必须填入所有 key 值        | 是     |
| value     | 非主键字段名                            | 非主键字段名                           | 至少一个或\* |
| \-index   | LIST 表：如果指定“\-index”会返回相同 key 下的第 index 条记录，如果不指定“\-index”，则返回所有记录<br>GENERIC 表：不支持 | LIST 表：如果指定“\-index”会返回相同 key 下的第 index 条记录，如果不指定“\-index”， 则返回所有记录<br>GENERIC 表：不支持 | 否           |
| \\P       | 打印时延数据                              | 打印时延数据                           | 否           |
| \\G       | 竖排打印                                    | 竖排打印                                    | 否           |
| using tdr | 不支持        | 以 xml 格式输出数据，文件结构必须严格满足 xml 语法，该操作必须在启动 client 时提供 tdr 文件 | 否           |
| into      | 输出数据到文件                           | 输出数据到文件                           | 否           |


## 错误
请参考 [错误码列表](https://cloud.tencent.com/document/product/596/49767)。

## 示例

```
tcaplus> select * from test_table where gameid=1234 and itemid=12323 and name='testname';
+------+------+----------+------+----+-----+
|gameid|itemid|name      |typeid|Data|uname|
+------+------+----------+------+----+-----+
|1234  |12323 |"testname"|0     |9   |"ab" |
+------+------+----------+------+----+-----+
1 records selectd, select time: 9802 us
 
tcaplus> select uname from test_table where gameid=1234 and itemid=12323 and name='testname';
+------+------+----------+-----+
|gameid|itemid|name      |uname|
+------+------+----------+-----+
|1234  |12323 |"testname"|"ab" |
+------+------+----------+-----+
1 records selectd, select time: 9457 us
 
tcaplus> select * into test.txt from test_table where gameid=1234 and itemid=12323 and name='testname';
1 records are stored to test.csv, select time: 10198 us
 
tcaplus> select * from test_table where gameid=1234 and itemid=12323 and name='testname' \P \G;
gameid: 1234
itemid: 12323
name: "testname"
typeid: 0
Data: 9
uname: "ab"
 
API ----      -1us    --->ProxyFront----      10us    --->ProxyEnd---     364us    --->SvrMainStart
|                              |                             |                           |381us
|11380us                       |4138us                       |4104us                   SvrWorkerStart
|                              |                             |                           |61us
API <---   34197us    ----ProxyFront<---      24us    ----ProxyEnd<--    3298us    ----SvrWorkerEnd
1 records selectd, select time: 11380 us
 
 
tcaplus> select * into table_list.xml from table_list where uin=99 and name = "99" and key1=99 using tdr;
11 records are stored to table_list.xml, select time: 135299 us
 
tcaplus> select c_string from table_list where uin=99 and name = "99" and key1=99;
+---+----+----+--------+
|uin|name|key1|c_string|
+---+----+----+--------+
|99 |"99"|99  |" "     |
+---+----+----+--------+
|99 |"99"|99  |""      |
+---+----+----+--------+
|99 |"99"|99  |""      |
+---+----+----+--------+
|99 |"99"|99  |""      |
+---+----+----+--------+
|99 |"99"|99  |""      |
+---+----+----+--------+
|99 |"99"|99  |" "     |
+---+----+----+--------+
|99 |"99"|99  |" "     |
+---+----+----+--------+
|99 |"99"|99  |" "     |
+---+----+----+--------+
|99 |"99"|99  |" "     |
+---+----+----+--------+
|99 |"99"|99  |" "     |
+---+----+----+--------+
|99 |"99"|99  |" "     |
+---+----+----+--------+
11 records selectd, select time: 102572 us
 
tcaplus> select c_string from table_list where uin=99 and name = "99" and key1=99 and -index=9;
+---+----+----+--------+
|uin|name|key1|c_string|
+---+----+----+--------+
|99 |"99"|99  |" "     |
+---+----+----+--------+
1 records selectd, select time: 9886 us
```

