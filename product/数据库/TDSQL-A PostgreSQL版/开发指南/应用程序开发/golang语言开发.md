用户可使用 golang 的 pgx 接口来连接 TDSQL-A PostgreSQL版 数据库，进行数据库交互。开发所需要的资源包可前往 [官网](https://github.com/jackc/pgx) 进行下载。

## 示例1：连接数据库
```
package main
import (
"fmt"
"time"
"github.com/jackc/pgx"
)
func main() {
var error_msg string
//连接数据库
conn, err := db_connect()
if err != nil {
error_msg = "连接数据库失败，详情：" + err.Error()
write_log("Error", error_msg)
return
}/
/程序运行结束时关闭连接
defer conn.Close()
write_log("Log", "连接数据库成功")
}
/*
功能描述：写入日志处理
参数说明：
log_level -- 日志级别，只能是 Error 或 Log
error_msg -- 日志内容
返回值说明：无
*/
func write_log(log_level string, error_msg string) {
//打印错误信息
fmt.Println("访问时间：", time.Now().Format("2006-01-02 15:04:05"))
fmt.Println("日志级别：", log_level)
fmt.Println("详细信息：", error_msg)
}
/*
功能描述：连接数据库
参数说明：无
返回值说明：
conn *pgx.Conn -- 连接信息
err error --错误信息
*/
func db_connect() (conn *pgx.Conn, err error) {
var config pgx.ConnConfig
config.Host = "127.0.0.1" //数据库主机 host 或 IP
config.User = "dbadmin" //连接用户
config.Password = "pgsql" //用户密码
config.Database = "postgres" //连接数据库名
config.Port = 15432 //端口号
conn, err = pgx.Connect(config)
return conn, err
}
```

## 示例2：表创建
```
package main
import (
"fmt"
"time"
"github.com/jackc/pgx"
)
func main() {
var error_msg string
var sql string
//连接数据库
conn, err := db_connect()
if err != nil {
error_msg = "连接数据库失败，详情：" + err.Error()
write_log("Error", error_msg)
return
}/
/程序运行结束时关闭连接
defer conn.Close()
write_log("Log", "连接数据库成功")
//建立数据表
sql = "create table public.tdapg(id varchar(20),nickname varchar(100))
distribute by shard(id) to group default_group;"
_, err = conn.Exec(sql)
if err != nil {
error_msg = "创建数据表失败,详情：" + err.Error()
write_log("Error", error_msg)
return
} else {
write_log("Log", "创建数据表成功")
}
}
/*
功能描述：写入日志处理
*/
func write_log(log_level string, error_msg string) {
//打印错误信息
fmt.Println("访问时间：", time.Now().Format("2006-01-02 15:04:05"))
fmt.Println("日志级别：", log_level)
fmt.Println("详细信息：", error_msg)
}
/*
功能描述：连接数据库
*/
func db_connect() (conn *pgx.Conn, err error) {
var config pgx.ConnConfig
config.Host = "127.0.0.1" //数据库主机 host 或 IP
config.User = "dbadmin" //连接用户
config.Password = "pgsql" //用户密码
config.Database = "postgres" //连接数据库名
config.Port = 15432 //端口号
conn, err = pgx.Connect(config)
return conn, err
}
```

## 示例3：插入数据
```
package main
import (
"fmt"
"strings"
"time"
"github.com/jackc/pgx"
)
func main() {
var error_msg string
var sql string
var nickname string
//连接数据库
conn, err := db_connect()
if err != nil {
error_msg = "连接数据库失败，详情：" + err.Error()
write_log("Error", error_msg)
return
}/
/程序运行结束时关闭连接
defer conn.Close()
write_log("Log", "连接数据库成功")
//插入数据
sql = "insert into public.tdapg values('1','tdapg'),('2','pgxz');"
_, err = conn.Exec(sql)
if err != nil {
error_msg = "插入数据失败,详情：" + err.Error()
write_log("Error", error_msg)
return
} else {
write_log("Log", "插入数据成功")
}
//绑定变量插入数据,不需要做防注入处理
sql = "insert into public.tdapg values($1,$2),($1,$3);"
_, err = conn.Exec(sql, "3", "postgresql", "postgres")
if err != nil {
error_msg = "插入数据失败,详情：" + err.Error()
write_log("Error", error_msg)
return
} else {
write_log("Log", "插入数据成功")
}
//拼接sql 语句插入数据,需要做防注入处理
nickname = "Tdapg is ' good!"
sql = "insert into public.tdapg values('1','" + sql_data_encode(nickname) + "')"
_, err = conn.Exec(sql)
if err != nil {
error_msg = "插入数据失败,详情：" + err.Error()
write_log("Error", error_msg)
return
} else {
write_log("Log", "插入数据成功")
}
}
func sql_data_encode(str string) string {
return strings.Replace(str, "'", "''", -1)
}
/*
功能描述：写入日志处理
参数说明：
log_level -- 日志级别，只能是 Error 或 Log
error_msg -- 日志内容
返回值说明：无
*/
func write_log(log_level string, error_msg string) {
//打印错误信息
fmt.Println("访问时间：", time.Now().Format("2006-01-02 15:04:05"))
fmt.Println("日志级别：", log_level)
fmt.Println("详细信息：", error_msg)
}
/*
功能描述：连接数据库
参数说明：无
返回值说明：
conn *pgx.Conn -- 连接信息
err error --错误信息
*/
func db_connect() (conn *pgx.Conn, err error) {
var config pgx.ConnConfig
config.Host = "127.0.0.1" //数据库主机 host 或 IP
config.User = "dbadmin" //连接用户
config.Password = "pgsql" //用户密码
config.Database = "postgres" //连接数据库名
config.Port = 15432 //端口号
conn, err = pgx.Connect(config)
return conn, err
}
```

## 示例4：数据查询
```
package main
import (
"fmt"
"strings"
"time"
"github.com/jackc/pgx"
)
func main() {
var error_msg string
var sql string
//连接数据库
conn, err := db_connect()
if err != nil {
error_msg = "连接数据库失败，详情：" + err.Error()
write_log("Error", error_msg)
return
}/
/程序运行结束时关闭连接
defer conn.Close()
write_log("Log", "连接数据库成功")
sql = "SELECT id,nickname FROM public.tdapg LIMIT 2"
rows, err := conn.Query(sql)
if err != nil {
error_msg = "查询数据失败,详情：" + err.Error()
write_log("Error", error_msg)
return
} else {
write_log("Log", "查询数据成功")
}
var nickname string
var id string
for rows.Next() {
err = rows.Scan(&id, &nickname)
if err != nil {
error_msg = "执行查询失败，详情：" + err.Error()
write_log("Error", error_msg)
return
}error_msg = fmt.Sprintf("id：%s nickname：%s", id, nickname)
write_log("Log", error_msg)
}rows.Close()
nickname = "tdapg"
sql = "SELECT id,nickname FROM public.tdapg WHERE nickname ='" +
sql_data_encode(nickname) + "' "
rows, err = conn.Query(sql)
if err != nil {
error_msg = "查询数据失败,详情：" + err.Error()
write_log("Error", error_msg)
return
} else {
write_log("Log", "查询数据成功")
}defer rows.Close()
for rows.Next() {
err = rows.Scan(&id, &nickname)
if err != nil {
error_msg = "执行查询失败，详情：" + err.Error()
write_log("Error", error_msg)
return
}error_msg = fmt.Sprintf("id：%s nickname：%s", id, nickname)
write_log("Log", error_msg)
}
}
/*
功能描述：sql 查询拼接字符串编码
参数说明：
str -- 要编码的字符串
返回值说明：
返回编码过的字符串
*/
func sql_data_encode(str string) string {
return strings.Replace(str, "'", "''", -1)
}
/*
功能描述：写入日志处理
参数说明：
log_level -- 日志级别，只能是 Error 或 Log
error_msg -- 日志内容
返回值说明：无
*/
func write_log(log_level string, error_msg string) {
//打印错误信息
fmt.Println("访问时间：", time.Now().Format("2006-01-02 15:04:05"))
fmt.Println("日志级别：", log_level)
fmt.Println("详细信息：", error_msg)
}
/*
功能描述：连接数据库
参数说明：无
返回值说明：
conn *pgx.Conn -- 连接信息
err error --错误信息
*/
func db_connect() (conn *pgx.Conn, err error) {
var config pgx.ConnConfig
config.Host = "127.0.0.1" //数据库主机 host 或 IP
config.User = "dbadmin" //连接用户
config.Password = "pgsql" //用户密码
config.Database = "postgres" //连接数据库名
config.Port = 15432 //端口号
conn, err = pgx.Connect(config)
return conn, err
}
```

## 示例5：copy 数据插入
```
package main
import (
"fmt"
"math/rand"
"time"
"github.com/jackc/pgx"
)
func main() {
var error_msg string
//连接数据库
conn, err := db_connect()
if err != nil {
error_msg = "连接数据库失败，详情：" + err.Error()
write_log("Error", error_msg)
return
}/
/程序运行结束时关闭连接
defer conn.Close()
write_log("Log", "连接数据库成功")
//构造5000行数据
inputRows := [][]interface{}{}
var id string
var nickname string
for i := 0; i < 5000; i++ {
id = fmt.Sprintf("%d", rand.Intn(10000))
nickname = fmt.Sprintf("%d", rand.Intn(10000))
inputRows = append(inputRows, []interface{}{id, nickname})
}copyCount, err := conn.CopyFrom(pgx.Identifier{"dbadmin"}, []string{"id",
"nickname"}, pgx.CopyFromRows(inputRows))
if err != nil {
error_msg = "执行 copyFrom 失败,详情：" + err.Error()
write_log("Error", error_msg)
return
}if copyCount != len(inputRows) {
error_msg = fmt.Sprintf("执行 copyFrom 失败，copy 行数：%d 返回行数为：%d",
len(inputRows), copyCount)
write_log("Error", error_msg)
return
} else {
error_msg = "Copy 记录成功"
write_log("Log", error_msg)
}
}
/*
功能描述：写入日志处理
参数说明：
log_level -- 日志级别，只能是 Error 或 Log
error_msg -- 日志内容
返回值说明：无
*/
func write_log(log_level string, error_msg string) {
//打印错误信息
fmt.Println("访问时间：", time.Now().Format("2006-01-02 15:04:05"))
fmt.Println("日志级别：", log_level)
fmt.Println("详细信息：", error_msg)
}
/*
功能描述：连接数据库
参数说明：无
返回值说明：
conn *pgx.Conn -- 连接信息
err error --错误信息
*/
func db_connect() (conn *pgx.Conn, err error) {
var config pgx.ConnConfig
config.Host = "127.0.0.1" //数据库主机 host 或 IP
config.User = "dbadmin" //连接用户
config.Password = "pgsql" //用户密码
config.Database = "postgres" //连接数据库名
config.Port = 15432 //端口号
conn, err = pgx.Connect(config)
return conn, err
}
```
