## 简介
MySQL Change Data Capture 连接器可连接第三方MySQL数据库系统并监控binlog中的 [DML](https://baike.baidu.com/item/%E6%95%B0%E6%8D%AE%E6%93%8D%E7%BA%B5%E8%AF%AD%E8%A8%80/10826467) 操作，捕获 MySQL 数据库 DML 操作记录并触发 iPaaS 集成流，完成相应的集成业务逻辑。

## 类型映射关系
MySQL 数据类型和 MySQL Change Data Capture 连接器捕获到的 DML 记录中的数据类型映射关系如下表。

| MySQL 类型 | MySQL Change Data Capture 连接器类型 |
| --- | --- |
| `BOOLEAN, BOOL` | `BOOLEAN` |
| `BIT(1)` | `BOOLEAN` |
| `BIT(>1)` | `BYTES` |
| `TINYINT` | `INT16` |
| `SMALLINT[(M)]` | `INT16` |
| `MEDIUMINT[(M)]` | `INT32` |
| `INT, INTEGER[(M)]` | `INT32` |
| `BIGINT[(M)]` | `INT64` |
| `REAL[(M,D)]` | `FLOAT32` |
| `FLOAT[(M,D)]` | `FLOAT64` |
| `DOUBLE[(M,D)]` | `FLOAT64` |
| `CHAR(M)]` | `STRING` |
| `VARCHAR(M)]` | `STRING` |
| `BINARY(M)]` | `BYTES` or `STRING` |
| `VARBINARY(M)]` | `BYTES` or `STRING` |
| `TINYBLOB` | `BYTES` or `STRING` |
| `TINYTEXT` | `STRING` |
| `BLOB` | `BYTES` or `STRING` |
| `TEXT` | `STRING` |
| `MEDIUMBLOB` | `BYTES` or `STRING` |
| `MEDIUMTEXT` | `STRING` |
| `LONGBLOB` | `BYTES` or `STRING` |
| `LONGTEXT` | `STRING` |
| `JSON` | `STRING` |
| `ENUM` | `STRING` |
| `SET` | `STRING` |
| `YEAR[(2\\|4)]` | `INT32` |
| `TIMESTAMP[(M)]` | `STRING` |

## MySQL 配置
需要在 MySQL Server 端进行必要的配置并且生效后，才可以使用 MySQL Change Data Capture 连接器，否则 MySQL Change Data Capture 连接器将无法捕获到 DML 操作并触发流。
以 Linux 环境为例说明如何配置 MySQL。
1. 开启 Binlog。
 1. 使用命令行工具连接到 MySQL 数据库所在服务器，执行一下命令以 root 用户登录数据库。
```sql
  mysql -uroot -ppassword
``` 
  2. 执行以下命令，查询 MySQL 数据库是否开启了 Binlog。
```sql
show variables like 'log_bin';
```
    - 若变量 log_bin 的值为“OFF”，则说明 Binlog 未开启，继续执行下一步。
    - 若变量 log_bin 的值为“ON”，则说明 Binlog 已开启，继续执行以下 SQL 命令，检查相关参数的配置是否符合要求。
```sql
  show variables like '%binlog_format%';
  show variables like '%binlog_row_image%';
```
    - 变量 binlog_format 的值应该为“ROW”，变量 binlog_row_image 的值应该为“FULL”。如果满足要求，直接跳到 2，否则继续执行下一步。
 3. 执行以下命令退出数据库。
```
exit;
```
 4. 执行以下命令编辑 MySQL 配置文件，然后按 **i** 进入输入模式。
```sql
  vi /etc/my.cnf
```
 5. 在配置文件中增加如下配置，开启 Binlog。
```
server-id = 123
log_bin = mysql-bin
binlog_format = row
binlog_row_image = full
expire_logs_days = 14
gtid_mode = on
enforce_gtid_consistency = on
```
 其中：
    - **server-id** 的值应为大于1的整数，请根据实际情况设置。
    - **expire_logs_days** 为 Binlog 日志文件保留时间，超过保留时间的 Binlog 日志会被自动删除，应保留至少2天的日志文件。
    - **gtid_mode = on** 和 **enforce_gtid_consistency = on** 仅当 MySQL 的版本大于等于5.6.5时才需要添加，否则删除这两行内容。
 6. 按 Esc 退出输入模式，然后输入 `:wq` 并回车，保存退出。
 7.执行以下命令重启 MySQL 数据库。
```
  service mysqld restart
```
 8. 以 root 用户登录数据库，执行以下命令，查询变量 log_bin 的值是否为“ON”，即是否已开启 Binlog。
```sql
show variables like 'log_bin';
```
2. 在数据库中执行以下命令创建数据连接器连接数据库的用户并配置权限。
```sql
CREATE USER 'ipaas'@'%' IDENTIFIED BY 'password';
GRANT SELECT, RELOAD, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'ipaas'@'%';
```
其中：
 - **ipaas** 为数据连接器连接用户名，请根据实际情况设置。
 - **password** 为数据连接器t连接用户密码，请根据实际情况设置。
3. 执行以下命令退出数据库连接。
```sql
exit;
```

## 连接器配置

**MySQL Change Data Capture 连接器配置参数**

| 参数        | 数据类型   | 描述                                                                                                       | **是否必填** | **默认值**  |
| --------- | ------ | -------------------------------------------------------------------------------------------------------- | -------- | -------- |
| 数据库类型     | enum   | 数据库类型，仅支持 MySQL                                                                                          | 是        | MySQL    |
| 数据库Host地址 | string | MySQL 数据库地址                                                                                               | 是        | -        |
| 端口号       | int    | MySQL 数据库端口号                                                                                              | 是        | -        |
| 用户名       | string | 用于连接数据库的用户名                                                                                              | 是        | -        |
| 密码        | string | 用于连接数据库的用户密码                                                                                             | 是        | -        |
| 安全网关      | -      | 选择用于连接用户内网MySQL的代理，安全网关的配置可参见 [安全网关](https://cloud.tencent.com/document/product/1270/51656)              | 否        | -        |
| 消息确认模式    | enum   | 消息确认模式：<li>流开始前立即确认：change 消息只会处理一次，无论流运行成功如否</li><li>流运行成功后确认：change 消息仅在流运行成功才会确认，流运行失败的 change 信息会重试</li> | 否        | 流运行成功后确认 |

连接器配置界面如下：
![连接器配置界面](https://qcloudimg.tencent-cloud.cn/raw/3ca916b9ef9dfa8eec116fa4a128bbec.png)

## 操作说明
MySQL Change Data Capture 连接器目前仅支持作为 Trigger 节点使用，可将捕获到的 dml 操作作为触发消息源，触发后续的业务逻辑流执行。

#### 参数配置

| 参数  | 数据类型   | 描述                                                     | **是否必填** | **默认值** |
| --- | ------ | ------------------------------------------------------ | -------- | ------- |
| 数据库 | string | 选中的待同步数据库名称，根据连接参数自动从 MySQL 数据库中查询并列出                    | 是        | -       |
| 表   | string | 选中待同步的表名称，根据连接参数和选中的数据库名称，自动从 MySQL 数据库中查询并列出            | 是        | -       |
| 字段  | list   | 选中的待同步字段名称列表，根据连接参数和选中的数据库名称、表名称，自动从 MySQL 数据库中查询并列出，可多选 | 是        | -       |

参数配置界面如下：
![参数配置](https://qcloudimg.tencent-cloud.cn/raw/9e92f5bd2532ed4e8823333a181803dc.png)

#### 输出

| message 属性 | 值                                                                                                    |
| ---------- | ---------------------------------------------------------------------------------------------------- |
| payload    | 执行成功后，payload 为 json 序列化后的 byte 数组，struct 为：<br/>[{"xxx": "xyz"}, {"xxx": "xyz"}]，列表中每一个记录都是一个 dml 操作的信息   |
| error      | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute  | 执行成功后，attribute 为 dict，包含一个 key 为 totalCount， value 为 payload 中列表记录总数的键值对                                  |
| variable   | 继承上个组件的 variable 信息                                                                                  |

**payload 示例：**
```json
 [
     {
         "after":{
             "c":"111222dgfgh",
             "id":8,
             "k":8,
             "pad":"abcsgfhg"
         },
         "before":{
             "c":"111222",
             "id":8,
             "k":8,
             "pad":"abcsgfhg"
         },
         "op":"u",
         "source":{
             "db":"cdctest2",
             "snapshot":"false",
             "table":"cdctest1"
         },
         "transaction":null,
         "ts_ms":1662712532622
     },
     {
         "after":{
             "c":"1111",
             "id":9,
             "k":9,
             "pad":"zzz"
         },
         "before":{
             "c":"3333dfsdgh",
             "id":9,
             "k":9,
             "pad":"zzz"
         },
         "op":"u",
         "source":{
             "db":"cdctest2",
             "snapshot":"false",
             "table":"cdctest1"
         },
         "transaction":null,
         "ts_ms":1662712532623
     }
 ]
```

### payload 说明
#### Snapshot
发布一条由 MySQL Change Data Capture 连接器触发的流之后，连接器会从保存的 binlog 初始 Offset 位置开始捕获 DML 信息，保存的 Offset 称之为一个 snapshot（快照）。
- 如果 Offset 不存在，连接器会从 binlog 的最初位置开始同步，此时会创建 snapshot，并全量同步数据库状态。
- 如果 Offset 存在，连接器会从该 snapshot 记录的位置开始同步。

采集到的 DML 信息中，按照事件类型可以分为4种：
- Read Event：仅出现在 snapshot 阶段，此时 snapshot 被置为 true。
```json
 {
    "after":{
        "account_type":"a",
        "acct_id":9999,
        "acct_name":"093592",
        "id":9999
    },
    "before":null,
    "op":"r",
    "source":{
        "connector":"mysql",
        "db":"ipaas_test",
        "file":"mysql-bin.000005",
        "gtid":null,
        "name":"_7ef6d5bd9f7fac34ca74b91088375d03f4b94d3af0aeef61dec9e9743336d19e",
        "pos":154,
        "query":null,
        "row":0,
        "sequence":null,
        "server_id":223344,
        "snapshot":true,
        "table":"account_info",
        "thread":null,
        "ts_ms":1662644525154,
        "version":"1.9.3.Final"
    },
    "transaction":null,
    "ts_ms":1662644525154
}
```
- Create Event：Insert 操作对应的记录。
> ```json
 {
    "op":"c",
    "ts_ms":1465491411815,
    "before":null,
    "after":{
        "account_type":"a",
        "acct_id":9999,
        "acct_name":"093592",
        "id":9999
    },
    "source":{
        "version":"1.9.3.Final",
        "connector":"mysql",
        "name":"_7ef6d5bd9f7fac34ca74b91088375d03f4b94d3af0aeef61dec9e9743336d19e",
        "ts_ms":0,
        "snapshot":false,
        "db":"ipaas_test",
        "table":"account_info",
        "server_id":223344,
        "gtid":null,
        "file":"mysql-bin.000005",
        "pos":154,
        "row":0,
        "thread":7,
        "query":null
    },
		 "transaction":null
}
```
- Update Event：Update 操作对应的记录。
```json
 {
    "before":{
        "account_type":"a",
        "acct_id":9999,
        "acct_name":"093592",
        "id":9999
    },
    "after":{
        "account_type":"a",
        "acct_id":9999,
        "acct_name":"0935921",
        "id":9999
    },
    "source":{
        "version":"1.9.3.Final",
        "name":"_7ef6d5bd9f7fac34ca74b91088375d03f4b94d3af0aeef61dec9e9743336d19e",
        "connector":"mysql",
        "ts_ms":1465581029100,
        "snapshot":false,
        "db":"ipaas_test",
        "table":"account_info",
        "server_id":223344,
        "gtid":null,
        "file":"mysql-bin.000005",
        "pos":484,
        "row":0,
        "thread":7,
        "query":null
    },
    "op":"u",
		 "transaction":null,
    "ts_ms":1465581029523
}
```
- Delete Event：Delete 操作对应的记录。
```json
 {
    "before":{
        "account_type":"a",
        "acct_id":9999,
        "acct_name":"0935921",
        "id":9999
    },
    "after":null,
		"op":"d",
    "source":{
        "version":"1.9.3.Final",
        "connector":"mysql",
        "name":"_7ef6d5bd9f7fac34ca74b91088375d03f4b94d3af0aeef61dec9e9743336d19e",
        "ts_ms":1465581902300,
        "snapshot":false,
        "db":"ipaas_test",
        "table":"account_info",
        "server_id":223344,
        "gtid":null,
        "file":"mysql-bin.000005",
        "pos":805,
        "row":0,
        "thread":7,
        "query":null
    },
		 "transaction":null,
    "ts_ms":1465581902461
}
```

#### GTID
当 MySQL Server 由于某些原因不可用时，MySQL Change Data Capture 连接器会停止采集 DML 操作记录，直到 MySQL Server 重新可用，按照 GTID 的配置情况，这里后有两种不同的行为模式：
- 对于打开 GTID 的 MySQL Cluster，连接器会连接到失效 Server 外的另一个 Server 上，找到上一次事务中的 binlog 位置，并开始同步。
- 对于未打开 GTID 的，仅当连接器重连上失效 Server 后，才可以从原来的位置继续同步。

### 使用示例
1. 新建连接器配置，填写配置参数，单击**测试连接**，测试连接器配置是否正确。
   ![](https://qcloudimg.tencent-cloud.cn/raw/4108fc4b9f98b9739226171adac19678.png)
2. 在操作配置中，依次下拉选择数据库、表，选中待同步的数据库和表后，在自动刷新到界面的待选择字段名列表中勾选想要同步的字段，并保存。
   ![参数配置](https://qcloudimg.tencent-cloud.cn/raw/9e92f5bd2532ed4e8823333a181803dc.png)
3. 在 trigger 节点后增加业务逻辑，此处仅以打印日志作为示例：
   ![](https://qcloudimg.tencent-cloud.cn/raw/04d35961bd922b06c977afc6b6c1c17e.png)
