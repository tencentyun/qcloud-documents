以下是通过 client 工具访问 TcaplusDB 表的步骤。

tcaplus_client 是在 TcaplusServiceAPI 发布包 bin 目录中的一个 TcaplusDB 表访问工具，它本身也是 TcaplusServiceAPI 的一个应用程序。

Linux x86_64 平台的 TcaplusServiceAPI 发布包将包含64位 linux 版本的 tcaplus_client 工具，Windows x64 平台的 TcaplusServiceAPI 发布包将包含64位 Windows 版本的 tcaplus_client 工具，接下来的演示将基于 Linux x86_64 版本的工具进行。

> ! 相关操作需要在用户腾讯云账号下申请的 CVM 中进行。

在本例中，假设用户获取到如下接入点信息，并且在 ZoneId 为1的部署单元中创建了表 tb_online

* AppId：2
* AppKey：3aa84dd773826cd655e9f24a249d68bb
* tcapdir 接入点：10.125.32.21:9999
* ZoneId：1

## 权限操作

首先需要给 tcaplus_client 工具赋予可执行权限，当直接执行 ./tcaplus_client 不带任何参数时，会打印连接所需的参数信息，用户可以根据自己的游戏业务进行填写。

```
# ./tcaplus_client
--------------------------------------------------------------------------------
 invalid parameters, please start the client as following:

    ./tcaplus_client -a app_id -z zone_id -s signature -d dir_server_url [-t table_name] [-l log_file.xml] [-T tdr_file.tdr] [-e execute_command]

    the params in [] are optional, and theire order is not important.

    -a(--ap_id)    APP ID

    -z(--zone_id)    ZONE ID    -s(--signature)    PASSWORD



    -d(--dir)    dir server addr

    -t(--table)    table to add

    -l(--log)    log file name that must be client_log.xml, and log class name be client

    -T(--tdr)    tdr filename 

    -e(--execute)    content following should be with qoutes.

    e.g. ./tcaplus_client -a 2 -z 3 -s "FE6533875C8385C3" -d 172.25.40.181:9999 -T table_test.tdr 
--------------------------------------------------------------------------------
```

## 连接

使用命令连接 TcaplusDB。

```
./tcaplus_client -a 2 -z 1 -s "3aa84dd773826cd655e9f24a249d68bb" -d 10.125.32.21:9999
+------------------------------------------------------------------------------+
|    tcaplus_client x86_64  build at Wed Jan 18 22:08:38 CST 2017              |
|                                                                              |
|    Welcome!                                                                  |
+------------------------------------------------------------------------------+

tcaplus>
```

在提示符之后输入 help，可以看到进一步的帮助信息，通过 `> help 具体命令` 可以查看具体的使用方法。

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

接下来将演示如何分别通过 Update 和 Select 命令执行写和读操作。

## 写操作

使用 update 命令写入记录。

```
tcaplus>update tb_online set gamesvrid=4099, logintime=101 where uin=1024 and name="tcaplus_user" and region=10;
--------------------------------------------------------------------------------
        success. 
--------------------------------------------------------------------------------
update time: 5593 us
```

## 读操作

使用 select 命令将刚刚写入的数据读出来。

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
