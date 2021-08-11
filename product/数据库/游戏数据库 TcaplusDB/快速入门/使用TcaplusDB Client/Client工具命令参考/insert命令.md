
## 简介
向表格中插入一条数据，可采用显示声明参数或传入文件两种方式操作。

## 语法
```
## 显示声明参数的值插入一条数据
insert into table (key1, key2, value1, vlaue2) values (1, "abc", 2, "def") [after -1] [shift none/head/tail];

## 从 csv 格式文件中读取并插入一条数据
insert into table infile result.csv [after -1] [shift none/head/tail];

## 从 xml 格式文件中读取并插入一条数据，该操作必须在启动 client 时提供 tdr 文件
insert into table infile result.xml [after -1] [shift none/head/tail] using tdr;
```

## 参数

| 参数      | Protobuf 和 TDR                                                      | 必填         |
| --------- | ------------------------------------------------------------ | ------------ |
| table     | 表格的名字                                                   | 是           |
| key       | 主键字段名                                                   | 是           |
| value     | 非主键字段名                                                 | 至少一个或\* |
| after     | LIST 表： <br> n > 0 表示从第 n 条数据插入<br>n = -2 表示从队首插入数据 <br>n = -1 表示从队尾插入数据 <br> n < -2 不支持<br>GENERIC 表：不支持 after 字段 | 否           |
| shift     | 如果表格大小超过阈值（即表格的最大 size），可选择： <br>none：不淘汰数据 <br>head：从队头淘汰  <br>   tail：从队尾淘汰数据 | 否           |
| using tdr | Protobuf 表不支持此参数；TDR 表需要以 xml 格式插入数据，文件结构必须严格满足 xml 语法，该操作必须在启动 client 时提供 tdr 文件 | 否           |
| infile    | 从文件中读取数据                                             | 否           |


## 错误
请参考 [错误码列表](https://cloud.tencent.com/document/product/596/49767)。

## 示例
示例文件下载：[result.xml](https://tcaplusdb-sdk-1301716906.cos.ap-shanghai.myqcloud.com/result.xml) [result.csv](https://tcaplusdb-sdk-1301716906.cos.ap-shanghai.myqcloud.com/result.csv)

```
tcaplus>insert into game_players (player_id,player_name,player_email,game_server_id) values (2,name,email,2);
insert success
 
insert time: 45322 us
 
tcaplus> Insert into table_list (uin, name, key1) values (99,99,99) after -1 shift tail;
 
insert success
 
insert time: 22464 us
 
tcaplus> Insert into table_list infile result.xml  using tdr;
 
 
insert success
 
insert time: 9493 us
 
tcaplus> Insert into table_list infile result.csv;
 
 
insert success
 
insert time: 22368 us
```

