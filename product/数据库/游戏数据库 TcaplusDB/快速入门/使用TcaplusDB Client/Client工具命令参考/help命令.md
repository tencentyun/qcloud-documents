
## 简介
获取指令使用方法。

## 语法
```
## 获取所有指令及其说明
help;
 
## 获取指定指令名的详细说明
help [指令名];
```

## 示例
```
tcaplus> help;
--------------------------------------------------------------------------------
      help: show usage of commands, example: "help select;".
      show: get server status related information. executing "help show;" for details.
      exit/quit: exit the client.
     count: print record number in the database.
 
      desc: print table field name and type.
    select: query records from database.
    insert: insert a new record into database.
   replace: replace a record into the database.
    update: update a record in the database.
    delete: delete record(s) from database.
 
      dump: dump records from database.
      load: load records into the database.
 
    setttl: set ttl for a record
    getttl: get ttl for a record
 
--------------------------------------------------------------------------------
 
tcaplus> help select;
--------------------------------------------------------------------------------
example: select key1, key2, key3, value1, value2 [into result.csv] from table where key1 = 1 and key2 = "abc" [and -index = 1] [\P] [\G];
         query records from database, you can specify part of the fields or whole fields (select *), and you can write the result to a file, which can be used by "insert" and "load"
         for generic table, if the key in where clause is not complete, then it will send "GetByPartkey"
         for list table, if "-index" is not specified in where clause, then it will send "ListGetAll", otherwise it will send "ListGet"
         \P: print time usage in detail
         \G: print fields in column
         Note: "-index" only used for list table
 
example: select * [into result.xml] from table where key1 = 1 and key2 = "abc" [and -index = 1] using tdr [\P];
         if you specify "using tdr", then the records will be parsed by tdr file and print in xml format. you can write the result into a file, which can be used by "load"
         it only support "select *" instead of select part of the fields when specify "using tdr"
         Note: "-index" only used for list table
 
globle index query:
   example: select * from table where key1 > 1 and value1 > 100;
   example: select * from table where value1 like "test";
   example: select field1, field2 from table where key1 > 1 or value1 > 100;
   example: select * from table where value1 between 100 and 200;
   example: select * from table where value1 > 100 limit 100 offset 0;
   example: select sum(value2), max(value2), min(value2), avg(value2), count(*) from table where value1 > 100;
   Note: globle index query is only support generic table;
   Note: current support: =,!=,>,>=,<,<=, like, not like, betwwen, in, not in, and, or, limit offset;
   Note: current support aggregation: count, sum, max, min, avg;
   Note: for protobuf table, it support: "select field1.field2 from test where value1 > 100";
   Note: limit must be used with offset, lack offset will query failed;
   Note: the fields in where condition and in aggregation must had already created index;
   Note: it not support: store the result to a file, such as "select * into file XXX" is not support;
   Note: it not support: "select * from table"; which means to traverse table, you can used api traverse method to traverse table;
   Note: it not support: order by, group by, having, join, union and so on;
   Note: it not support: select a+b XXX; select * from table where a+b>0; select sum(XX),field1 from XXX; select *,field1 from XXX; ......;
--------------------------------------------------------------------------------
```
