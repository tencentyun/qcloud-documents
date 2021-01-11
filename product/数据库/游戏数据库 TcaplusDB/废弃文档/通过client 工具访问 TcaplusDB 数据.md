本文为您介绍如何通过客户端工具 tcaplus_client 访问 TcaplusDB 数据。
所有数据操作语句必须带 where 条件，where 条件中必须包含主键字段，如果包含多个主键，则使用 and 将多个主键字段连接起来。

## client 工具
tcaplus_client 是一个 TcaplusDB 表访问的客户端工具，可通过下表中的下载链接进行下载。

Linux x86_64 平台的 TcaplusServiceAPI 发布包包含64位 Linux 版本的 tcaplus_client 工具：

| 版本          | 操作系统 | 下载包名                                                     |
| ------------- | -------- | ------------------------------------------------------------ |
| 3.36.0.192960 | Linux    | [TcaplusPbApi3.36.0.192960.x86_64](https://tcaplusdb-sdk-1301716906.cos.ap-shanghai.myqcloud.com/3.36.0.192960/TcaplusPbApi3.36.0.192960.x86_64_release_20200115.tar.gz) |

>?相关操作需要在用户腾讯云账号下申请的同 VPC 网络，同子网的云服务器 CVM 中进行。

### 安装客户端
下载完成 TcaplusServiceApi 安装包后，将其 [通过上传工具](https://cloud.tencent.com/document/product/213/39138) 上传至与 TcaplusDB 集群同一VPC，同一子网的云服务器中。

1. 上传完成后，执行下列命令解压安装包。
```
tar -xf TcaplusServiceApi3.32.0.191008.x86_64_release_20190409.tar.gz -C tcaplus
```
2. 解压完成后，进入至 tcaplus 的 bin 目录中，并赋予可执行权限：
```
cd tcaplus/release/x86_64/bin
chmod +x tcaplus_client
```
3. 直接执行`./tcaplus_client`命令，会提示连接数据库所需的参数信息，用户可以根据自己的集群信息进行填写。
>!下文示例中，app_id 代表集群接入 ID、App 代表集群、zone 代表表格组。


```
# ./tcaplus_client
--------------------------------------------------------------------------------
 invalid parameters, please start the client as following:
    ./tcaplus_client -a app_id -z zone_id -s signature -d dir_server_url [-t table_name] [-l log_file.xml] [-T tdr_file.tdr] [-e execute_command]
    the params in [] are optional, and theire order is not important.
    -a(--ap_id)    App ID
    -z(--zone_id)    ZONE ID
	-s(--signature)    PASSWORD
    -d(--dir)    dir server addr
    -t(--table)    table to add
    -l(--log)    log file name that must be client_log.xml, and log class name be client
    -T(--tdr)    tdr filename 
    -e(--execute)    content following should be with qoutes.
    e.g. ./tcaplus_client -a 2 -z 3 -s "test@Password1" -d 172.xx.xx.181:9999 -T table_test.tdr 
--------------------------------------------------------------------------------
```

### 连接 TcaplusDB
使用命令连接 TcaplusDB，如下示例中，访问点信息如下，并且在表格组 ID 为1的表格组中创建了表 tb_online。
- 集群接入ID：2
- 连接密码：test@Password1
- 内网地址:内网端口：10.125.32.21:9999
- 表格组ID：1

```
./tcaplus_client -a 2 -z 1 -s "test@Password1" -d 10.125.32.21:9999
+------------------------------------------------------------------------------+
|    tcaplus_client x86_64  build at Wed Jan 18 22:08:38 CST 2017              |
|                                                                              |
|    Welcome!                                                                  |
+------------------------------------------------------------------------------+

tcaplus>
```

在提示符之后输入 help，可看到进一步的帮助信息，通过 `> help 具体命令` 可以查看具体使用方法。
```
tcaplus>help
--------------------------------------------------------------------------------
    show                 get server status related information. executing help show for details.
    dir                  add dir server url. if no dir_server_url added ,
                         commands will fail when executing.
    desc                 output current table struction description
    count                output table row count
    select               query data
    update               update record. if record does not exist then add it or update it if exists.
    insert               insert a new record (not implemented)
    delete               delete record(s)
    bson                 execute bson query
    dump                 dump records from tcaplus to file with csv format
    load                 load records from csv file and import the records to tcplus
    clean                clean table
    quit                 exit the client
    help                 follow a command to get details.
                         e.g. help show, help dir etc.
    note: tdr mode means starting client with -T, and none tdr mode starting client without -T
--------------------------------------------------------------------------------
```


## 语句执行方法
<br>下文分别演示以上语句的执行方法和作用。

#### desc 操作
查看表的定义信息。嵌套字段只能看到其属性为嵌套类型，但是无法查看嵌套结构体的定义。
使用语法为：`desc 表名;`
```
tcaplus>desc game_players;
TableName:game_players
TableType:PROTOBUF
-------------------------------------------------------------------------
| Field                         Type                          Key       |
-------------------------------------------------------------------------
| player_id                     int64                         key       |
| player_email                  string                        key       |
| player_name                   string                                  |
| game_server_id                int32                                   |
| login_timestamp               string                                  |
| logout_timestamp              string                                  |
| is_online                     int8                                    |
| pay                           message                                 |
-------------------------------------------------------------------------
```

#### count 操作
查看表记录总数。
使用语法为：`count 表名;`
```
tcaplus>count t1;
-------------------------------------------
| TableName                     COUNT(*)  |
-------------------------------------------
| t1                            15        |
-------------------------------------------
```

#### 导出数据
使用 dump 命令导出指定表所有的记录，导出文件是 json 格式。
使用语法：`dump * from 表名 into 文件名;`
```
tcaplus>dump * from player into player.txt;
--------------------------------------------------------------------------------
      dump from table("player") success. total record number is 4
--------------------------------------------------------------------------------
```

#### 导入数据
使用 load 命令从 csv 文件中导入指定表的记录。无法直接导入 dump 导出的文件。
使用语法：`load 表名 from 文件;`
```
tcaplus>load hehe from test1;
--------------------------------------------------------------------------------
      1 records loaded successfully.
--------------------------------------------------------------------------------
```

#### 清空表数据
因为安全原因，当前客户端工具不支持直接清除表数据。如需清空整张表数据，请通过控制台 [清理表](https://console.cloud.tencent.com/tcaplusdb/table) 功能进行。


### 插入数据
insert 语句当前无法使用，可使用 update 命令插入记录。

### 修改数据
使用 update 命令写入记录。当 where 条件中的主键字段值无可匹配的项，则为新增记录。
语法为：`update 表 set 字段=值[,字段2=值2…] where 主键字段=值 [and 主键字段2=值2…];`
```
tcaplus>update tb_online set gamesvrid=4099, logintime=101 where uin=1024 and name="tcaplus_user" and region=10;
--------------------------------------------------------------------------------
        success. 
--------------------------------------------------------------------------------
update time: 5593 us
```

### 读取数据
使用 select 命令读取部分字段数据。
语法为：`select 字段[,字段2…] from 表 where 主键字段=值 [and 主键字段2=值];`
输入的数据中 recDataVersion 列指的当前记录的版本号。
```
tcaplus>select gamesvrid, logintime from tb_online where uin=1024 and name="tcaplus_user" and region=10;
+------+--------------+--------+------------------+--------------+-----------+
| uin  | name         | region | recDataVersion   | gamesvrid    | logintime |
+------+--------------+--------+------------------+--------------+-----------+
| 1024 | tcaplus_user | 10     | 2                | 4099         | 101       |
+------+--------------+--------+------------------+--------------+-----------+
totally 1 record(s) responded.
query time 8686 us
```

支持 select * from 表 where 主键字段=值，如下所示：
```
tcaplus>select * from test where id=1 and name=1;
+----+------+------------------+----+
| id | name | recDataVersion   | em |
+----+------+------------------+----+
| 1  | 1    | 1                | 1  |
+----+------+------------------+----+
totally 1 record(s) responded.
query time 7537 us
```

支持 \G 以及 \P 格式化输出，\G 代表根据字段横版输出，\P 则是按照表格输出的方式输出，默认不带格式化输出字段则是根据 \P 模式输出：
```
tcaplus>select * from hehe where id=1 and name=1 \G;
----------------------------------------1.row----------------------------------------
id: 1
name: 1
recDataVersion: 1
em: 1
responding record total:1
query time 3285 us
```

select 语句支持导出数据至文件。
语法为：`select * into [outfile] 文件名 from 表名 where 主键=值 [and 主键2=值];`

```
tcaplus>select * into outfile test2.xml from hehe where id=1 and name=1;
+----+------+------------------+----+
| id | name | recDataVersion   | em |
+----+------+------------------+----+
| 1  | 1    | 1                | 1  |
+----+------+------------------+----+
totally 1 record(s) responded.
query time 5399 us
```

### 删除数据
使用 delete 命令删除写入的记录。
语法为：`delete from 表名 where 主键=值 [and 主键2=值];`
```
tcaplus>delete from hehe where id=4 and name=4;
--------------------------------------------------------------------------------
        success
--------------------------------------------------------------------------------
delete time 4280 us
```
