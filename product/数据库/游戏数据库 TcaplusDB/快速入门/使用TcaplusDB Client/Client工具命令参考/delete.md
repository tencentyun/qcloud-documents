
## 简介
根据指定的 key 删除表格中一条数据，如果不指定 -index，则删除符合条件的所有记录。

## 语法
```
delete from table where key1 = 1 and key2 = "abc" [and -index = 1] [by partkey];
```

## 参数

|  参数          | Protobuf                                      | TDR                             | 必填项       |
| ---------- | ------------------------------------- | -------------------------------- | ------------ |
| table      | 表格的名字                                        | 表格的名字                                  | 是           |
| key        | 主键字段名，必须填入所有 key 值          | 主键字段名，必须填入所有 key 值          | 是           |
| value      | 非主键字段名                             | 非主键字段名                            | 至少一个或\* |
| \-index    | LIST 表：必须指定“\-index”，只替换指定记录<br>GENERIC 表：不支持 | LIST 表：如果指定“\-index”会返回相同 key下 的第 index 条记录，如果不指定“\-index”，则返回所有记录<br>GENERIC表：不支持 | 否           |
| by partkey | 不支持         | LIST 表不支持 <br> GENERIC 表通过表格的部分 key 删除记录      | 否           |


## 错误
请参考 [错误码列表](https://cloud.tencent.com/document/product/596/49767)。

## 示例
```
tcaplus> delete from table_list where  uin=99 and name = "99" and key1=99 and -index=0;
 
delete success
 
delete time: 10263 us
 
tcaplus> delete from table_generic_xiahuaxian  where _uin=99 and name = "danmi_test_1" and _key3=4 by partkey;
 
delete success
 
delete time: 14405 us
```
