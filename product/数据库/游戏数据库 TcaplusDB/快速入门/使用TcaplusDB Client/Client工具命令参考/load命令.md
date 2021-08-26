
## 简介
导入数据，支持 csv、xml 两种数据格式，如果记录存在更新记录，如果记录不存在新增记录。

## 语法
```
##按 xml 格式导入
load table infile 文件名 using tdr;
 
##按 csv 格式导入
load table infile 文件名;
```

## 参数

|  参数          | Protobuf                                      | TDR                             | 必填项       |
| --------- | -------------- | ------------------------------------------------------------ | ------ |
| table     | 表格名         | 表格名                                                       | 是     |
| using tdr | 不支持       | 一 xml 格式导出数据，文件结构严格满足 xml 语法，该操作必须在启动 client 时提供 tdr 文件 | 否  |
| infile    | 从文件读取数据 | 从文件读取数据                                               | 是     |

## 错误
请参考 [错误码列表](https://cloud.tencent.com/document/product/596/49767)。

## 示例
```
tcaplus> load table_list infile table_list_dump.xml using tdr;
loaded 49 records successful
 
tcaplus> load table_list infile table_list-dump.txt;
loaded 98 records successful
```
