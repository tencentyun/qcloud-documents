
## 简介
全量导出表格中的数据，提供打印到控制台/输出到文件两种方式。

## 语法
```
## 导出部分字段
dump key1, key2, value1, value2 [into result.csv] from table limit 10;
 
## 按 xml 格式导出
dump * [into 文件名] from table limit 10 using tdr;
 
## 按 csv 格式导出
dump * [into 文件名] from table limit 10;
```

## 参数

|  参数          | Protobuf                                      | TDR                             | 必填项       |
| ----- | --------------------------------------------------- | ------------------------------------------------------- | ------ |
| table | 表格的名字                                                   | 表格的名字                                                   | 是     |
| key   | 主键字段名，必须填入所有 key 值                                | 主键字段名，必须填入所有 key 值         | 是     |
| value | 非主键字段名                                                 | 非主键字段名                                                 | 否     |
| limit | LIST 表：导出 key 的个数，一个 key 对应多条记录<br>GENERIC 表：导出记录的条数，一个 key 对应一条记录 | LIST 表：导出 key 的个数，一个 key 对应多条记录<br>GENERIC 表：导出记录的条数，一个 key 对应一条记录 | 否     |
| using | 不支持                                                       | 一 xml 格式导出数据，文件结构严格满足 xml 语法，该操作必须在启动 client 时提供 tdr 文件 | 否     |
| into  | 导出数据到文件                                               | 导出数据到文件                                               | 否     |


## 错误
请参考 [错误码列表](https://cloud.tencent.com/document/product/596/49767)。

## 示例

```
tcaplus> dump * from table_list limit 0;
uin,name,key1,level,count,array_count,items,c_int8,c_uint8,c_int16,c_uint16,c_int32,c_uint32,c_int64,c_uint64,c_float,c_double,c_string,c_string_128K,c_string_256K,c_binary,binary,selector,single_struct,simple_struct,single_union_selector,single_union,array,c_union,union_array,c_struct,struct_array
99,"99",99,1,0,1,0x,-1,2,-3,4,-5,6,-7,0,1.234568,9.876543,"","123456789","123456789",0x,0,0,0x,0x,0,0x,0x,0x,0x,0x,0x
99,"99",99,1,0,1,0x,-1,2,-3,4,-5,6,-7,0,1.234568,9.876543,"","123456789","123456789",0x,0,0,0x,0x,0,0x,0x,0x,0x,0x,0x
99,"99",99,1,0,1,0x,-1,2,-3,4,-5,6,-7,0,1.234568,9.876543,"","123456789","123456789",0x,0,0,0x,0x,0,0x,0x,0x,0x,0x,0x
99,"99",99,1,0,1,0x,-1,2,-3,4,-5,6,-7,0,1.234568,9.876543,"","123456789","123456789",0x,0,0,0x,0x,0,0x,0x,0x,0x,0x,0x
 
dump 4 records successful
 
dump time: 121671 us
 
tcaplus> dump * into table_list.txt from table_list limit 0;
 
dumped 4 records successful
 
tcaplus> dump * into table_list.xml from table_list limit 0 using tdr;
 
dumped 4 records successful
```
