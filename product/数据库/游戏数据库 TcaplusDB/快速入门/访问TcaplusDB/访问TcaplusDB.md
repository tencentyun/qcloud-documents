TcaplusDB 数据可以通过多种方式进行访问读取，如客户端工具、各语言 SDK 工具包、RESTFul 接口。

## 通过 client 工具访问 TcaplusDB 数据
tcaplus_client 是一个 TcaplusDB 表访问的客户端工具，可通过下表中的下载链接进行下载。

Linux x86_64 平台的 TcaplusServiceAPI 发布包包含64位 Linux 版本的 tcaplus_client 工具：

| 版本 | 操作系统|下载包名 | 
|---------|---------|---------|
| 3.36.0.192960 | Linux |[TcaplusPbApi3.36.0.192960.x86_64](https://tcaplusdb-sdk-1301716906.cos.ap-shanghai.myqcloud.com/3.36.0.192960/TcaplusPbApi3.36.0.192960.x86_64_release_20200115.tar.gz) |

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
>

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


下文分别演示以上语句的执行方法和作用。

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
查看表记录总数。使用语法为：`count 表名;`
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


## 通过 C++ SDK 接口访问 TcaplusDB 数据
SDK 工具支持 C++ 以及 Java 两种语言，[C++ SDK 接口说明](https://cloud.tencent.com/document/product/596/31665)

## 通过 RESTFul API 接口访问 TcaplusDB 数据
[RESTFul API 接口说明](https://cloud.tencent.com/document/product/596/31664)
