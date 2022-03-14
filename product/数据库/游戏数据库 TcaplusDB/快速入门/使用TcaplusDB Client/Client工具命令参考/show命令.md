
## 简介
查询服务端、表格基本信息。show tables 可查询表格类型、协议类型。show status 可查询当前的连接状态，目录服务器信息以及接入层信息。

## 语法
```
show [status/tables];
```

## 参数

| 参数名 | 说明 |
| ------ | ---- |
| table  | 表名 |

## 示例
查询当前表格组下的表格信息：
```
tcaplus> show tables;
 
----------------------------------------------------------
| Table Name                         Type      Protocol  |
----------------------------------------------------------
| test_table                         GENERIC   TDR       |
| tbMailTest                         LIST      PROTOBUF  |
| pb_generic_index_shardingkey       GENERIC   PROTOBUF  |
| pb_generic_index_noshardkey        GENERIC   PROTOBUF  |
| pb_generic_noindex_noshardkey      GENERIC   PROTOBUF  |
| pb_list                            LIST      PROTOBUF  |
| pb_list2                           LIST      PROTOBUF  |
| pb_sortedlist                      LIST      PROTOBUF  |
| aes_info                           GENERIC   TDR       |
| auth_info                          GENERIC   TDR       |
| depend_me_services                 GENERIC   TDR       |
| host_info                          GENERIC   TDR       |
| instance_info                      GENERIC   TDR       |
| node_info                          GENERIC   TDR       |
| service_depends                    GENERIC   TDR       |
| service_info                       GENERIC   TDR       |
| token_info                         GENERIC   TDR       |
| cl_list                            LIST      PROTOBUF  |
| cl_generic                         GENERIC   PROTOBUF  |
| table_generic                      GENERIC   TDR       |
----------------------------------------------------------
```
