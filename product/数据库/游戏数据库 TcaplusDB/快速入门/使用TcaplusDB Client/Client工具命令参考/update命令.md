
## 简介
更新表格中一条数据，可采用显示声明参数或传入文件两种方式操作。

## 语法
```
## 显示声明字段的值，更新对应的记录
update table set value1 = 1, value2 = "abc", value3 = 0x123456 where key1 = 1 and key2 = "abc" and [-index = 1];
 
## 导入 csv 文件替换对应的记录
update table infile 文件名 [where -index = 0];
 
## 导入 xml 文件替换对应的记录
update table infile 文件名 [where -index = 0] using tdr;
```

## 参数

|  参数          | Protobuf                                      | TDR                             | 必填项       |
| --------- | ------------------------------------- | ------------------------------------------- | ------------ |
| table     | 表格的名字                                   | 表格的名字                                  | 是           |
| key       | 主键字段名，必须填入所有 key 值              | 主键字段名，必须填入所有 key 值               | 是       |
| value     | 非主键字段名                  | 非主键字段名                                 | 至少一个或\* |
| \-index   | LIST 表：必须指定“\-index”，只替换指定记录<br>GENERIC 表：不支持 | LIST 表：如果指定“\-index”会返回相同 key 下的第 index 条记录，如果不指定“\-index”，则返回所有记录<br>GENERIC 表：不支持 | 否           |
| using tdr | 不支持                 | 以 xml 格式输出数据，文件结构必须严格满足 xml 语法，该操作必须在启动 client 时提供 tdr 文件 | 否           |
| infile    | 从文件中读取数据                          | 从文件中读取数据                          | 否           |


## 错误
请参考 [错误码列表](https://cloud.tencent.com/document/product/596/49767)。

## 示例
```
tcaplus> update table_list set level=99 and count= 88 where uin=99 and name = "99" and key1=99 and -index=0;
 
update success
 
update time: 117086 us
```
