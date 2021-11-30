云数据仓库 ClickHouse 本身提供两种客户端接口，分别基于 HTTP 和 TCP 协议。

## 基于 HTTP 协议
主要用来支持轻量级的简单操作，方便跨平台和编程语言。EMR 集群内的 `clickhouse-server` 进程会启动8123的 HTTP 服务，可以发送简单的 GET 请求检查服务是否正常。
```
$ curl http://127.0.0.1:8123Ok.
```
还可以通过 query 参数发送请求，例如查询 testdb 中 account 表的数据。
```
$ wget -q -O- 'http://127.0.0.1:8123/?query=SELECT * from testdb.account'1       GHua    WuHan Hubei     19902       SLiu    ShenZhen Guangzhou      19913       JPong   Chengdu Sichuan 1992
```
其他用法可参考官方文档 [HTTP Interface](https://clickhouse.tech/docs/en/interfaces/http/)。

## 基于 TCP 协议
主要在 clickhouse-client 端使用，在云数据仓库 ClickHouse 集群内输入 clickhouse-client 命令，会输出版本信息、连接到的 clickhouse-server 地址、默认使用的数据库等。**可以通过 quit、exit 或 q 等退出使用。**
```
$ clickhouse-client
ClickHouse client version 19.16.12.49.
Connecting to localhost:9000 as user default.
Connected to ClickHouse server version 19.16.12 revision 54427.
```
#### clickhouse-client 使用的主要参数：

| 参数 | 说明  |
|---------|----------|
|  -C --config-file | 指定客户端使用的配置文件 |
|  -h --host  |指定 clickhouse-server 的 IP 地址  |
|  --port | 指定 clickhouse-server 的端口地址 |
|   -u --user |用户名  |
|  --password  |密码  |
|  -d --database | 数据库名称 |
|  -V --version | 查看客户端版本 |
|  -E --vertical | 查询结果按照垂直格式显示 |
|  -q --query | 非交互模式下传入的 SQL 语句 |
| -t --time | 非交互模式下显示执行时间 |
|  --log-level | 客户端日志级别 |
| --send_logs_level | 指定服务端返回日志数据的级别 |
|  --server_logs_file | 指定服务端日志保存路径 |

其他参数可参考官方文档 [Command-line Client](https://clickhouse.tech/docs/en/interfaces/cli/)。
