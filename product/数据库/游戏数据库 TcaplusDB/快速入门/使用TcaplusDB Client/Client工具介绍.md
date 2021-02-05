本文介绍如何通过客户端工具 tcaplus_client 访问数据。

所有数据操作语句必须带 where 条件，where 条件中必须包含主键字段，如果包含多个主键，则使用 and 将多个主键字段连接起来。

## 通过 client 工具访问 TcaplusDB 数据
tcaplus_client 是一个 TcaplusDB 表访问的客户端工具，可通过下表中的下载链接进行下载。

Linux x86_64 平台的 TcaplusServiceAPI 发布包包含64位 Linux 版本的 tcaplus_client 工具：

| 版本          | 发布时间   | 操作系统     | 下载包名                                                     |
| ------------- | ---------- | ------------ | ------------------------------------------------------------ |
| 3.46.0.199033 | 2020/12/28 | Linux x86_64 | [下载](https://tcaplusdb-sdk-1301716906.cos.ap-shanghai.myqcloud.com/release/3-46/TcaplusPbApi3.46.0.199033.x86_64_release_20201210.tar.gz) |

>?
>- 相关操作需要在用户腾讯云账号下申请的同 VPC 网络、同子网的云服务器 CVM 中进行。
>- 旧版本 3.36.0.192960，可通过 [该地址](https://tcaplusdb-sdk-1301716906.cos.ap-shanghai.myqcloud.com/3.36.0.192960/TcaplusPbApi3.36.0.192960.x86_64_release_20200115.tar.gz) 下载。

### 安装客户端
下载完成 TcaplusServiceApi 安装包后，将其 [通过上传工具](https://cloud.tencent.com/document/product/213/39138) 上传至与 TcaplusDB 集群同一VPC，同一子网的云服务器中。

1. 上传完成后，执行下列命令解压安装包。
```
tar -xf TcaplusPbApi3.46.0.199033.x86_64_release_20201210.tar.gz -C tcaplus
```
2. 解压完成后，进入至 tcaplus 的 bin 目录中，并赋予可执行权限：
```
cd tcaplus/release/x86_64/bin
chmod +x tcaplus_client
```
3. 直接执行`./tcaplus_client`命令，会提示连接数据库所需的参数信息，用户可以根据自己的集群信息进行填写。
>!下文示例中，app_id 代表集群接入 ID、App 代表集群、zone 代表表格组。


```
## ./tcaplus_client
--------------------------------------------------------------------------------
 invalid parameters, please start the client as following:

    ./tcaplus_client -a app_id -z zone_id -s signature -d dir_server_url [-t table_name] [-l log_file.xml] [-T tdr_file.tdr] [-e execute_command]

    the params in [] are optional, and their order is not important.

    -a(--ap_id)    APP ID

    -z(--zone_id)    ZONE ID

    -s(--signature)    PASSWORD

    -d(--dir)    dir server addr

    -t(--table)    table to add

    -l(--log)    log file name that must be client_log.xml, and log class name be client

    -T(--tdr)    tdr filename 

    -e(--execute)    SQL command need to execute, the content should be in quotes.

    e.g. ./tcaplus_client -a 2 -z 3 -s "FE6533875C8385C3" -d 172.25.40.181:9999 -T table_test.tdr -e "select a, b from table where key = 1;" 
--------------------------------------------------------------------------------
```

### 连接 TcaplusDB（默认场景）
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
--------------------------------------------------------------------------------
```

### 参数说明
| 参数 | 说明                                          | 是否必填 |
| ---- | --------------------------------------------- | -------- |
| -a   | 接入 ID                                       | 是       |
| -z   | 表格组 ID                                     | 是       |
| -s   | 集群密码                                      | 是       |
| -d   | 集群 IP 地址及端口                            | 是       |
| -t   | 表格名                                        | 否       |
| -l   | 日志文件输出设置，文件名必须是 client_log.xml | 否       |
| -T   | tdr 文件路径                                  | 否       |
| -e   | 需要执行的 SQL 语句                           | 否       |
| -v   | 版本查询                                      | 否       |
| <    | 重定向 SQL 语句到 client 执行                 | 否       |

### 连接 TcaplusDB（使用 TDR）
如果需要使用 using tdr，必须在 client 启动参数中添加 TDR 文件路径，可通过 [TDR 工具](#tdrgj) 把多个 XML 格式的元数据描述库转换成二进制格式。如果多个 XML 文件之间存在依赖关系，则被依赖的 XML 文件必须放在参数表前面。

使用示例：
```
[root@test-PC0 /opt]# ./tcaplus_client -a 2 -z 3 -s C12901752D0D3347 -d 8.x.x.8:9999 -T /mnt/e/tdr/2.3.table_list.tdr
 
====== Welcome to use tcaplus_client, use "help" to show usage ======
tcaplus > exit

[root@test-PC0 /opt]# ./tcaplus_client -a 2 -z 3 -s C12901752D0D3347 -d 8.x.x.8:9999 -T /mnt/e/tdr/2.3.table_list.tdr -e "show tables;"
-------------------------------------------
| Table Name                    Type      |
-------------------------------------------
| MTownRoleInfo                 GENERIC   |
| table_generic                 GENERIC   |
| table_generic_xiahuaxian      GENERIC   |
| table_list                    LIST      |
| test_table                    GENERIC   |
-------------------------------------------
```

#### [TDR 工具](id:tdrgj)
TDR 文件需要使用 TDR 工具生成，其主要是由数据定义文件（TDR 结构 xml 格式）生成，[工具下载地址](https://tcaplusdb-sdk-1301716906.cos.ap-shanghai.myqcloud.com/tdr)。

使用示例：
```
tdr -B -o ov_res.tdr ov_res.xml
        #xml 格式元数据库生成 .tdr 二进制库
tdr -C -o ov_res.c --old_xml_tagset  ov_res.xml
        #使用老标签集的 xml 格式元数据库生成 .c 文件
tdr -H -O "include" --add_custom_prefix="m_" --no_type_prefix
        #xml 元数据库生成 .h 文件，生成的文件保存在 include 目录
        #结构体（struct）/联合体（union）成员名添加前缀"m_"，但不添加类型前缀
tdr -G -m Pkg -x ATTR -o Pkg.xml net_protocol.xml
        #为 Pkg 生成 xml 格式的配置文件, 剪切版本为 Pkg 的最大版本， 文件名为 Pkg.xml
tdr -T -u prefixfile
        #导出生成 .h 文件时使用的数据成员前缀表到文件 prefixfile 中
tdr -A --indent-size=8 net_protocol.xml
        #根据 net_protocol.xml 中描述的协议生成 ActionScript3 语言的类文件，缩进大小为8个空格
tdr -P --indent-size=8 net_protocol.xml
        #根据 net_protocol.xml 中描述的协议生成 C++ 语言的类文件，缩进大小为8个空格
tdr -S --indent-size=8 net_protocol.xml
        #根据 net_protocol.xml 中描述的协议生成 C# 语言的类文件，缩进大小为8个空格
tdr -E 0x83010404
        #查询错误号0x83010404对应的错误信息
```

#### tdr2xml 工具
tdr2xml 工具可以把二进制元数据文件反编译成一个 xml 格式的元数据描述文件，[工具下载地址](https://tcaplusdb-sdk-1301716906.cos.ap-shanghai.myqcloud.com/tdr2xml)。

用法：
```
tdr2xml   [-o --out_file=FILE] [-h --help] [-v --version] DRFILE
各选项的含义如下：
-o, --out_file=FILE 指定输出文件的名字，缺省为 a.xml
-h, --help 输出使用帮助
-v, --version 输出版本信息
```

使用示例：
```
tdr2xml –o net_cs.xml  net_cs.tdr
```
将保存在 net_cs.tdr 文件中的元数据描述二进制自定义格式转换成 xml 格式的描述文件。
