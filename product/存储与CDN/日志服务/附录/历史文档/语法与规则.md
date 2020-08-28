
##  语法规则（Lucene）

| 保留关键字    | 说明                                                         |
| :------------ | :----------------------------------------------------------- |
| \_\_SOURCE\_\_    | 查询某个 SOURCE 源的日志，支持通配符，例如 `__SOURCE__:"127.0.0.*"` |
| \_\_FILENAME\_\_  | 查询来源为某个文件的日志，支持通配符 ，例如 `__FILENAME__:"/var/log/access.*"` |
| AND           | 与逻辑操作符，例如 `level:ERROR AND pid:1234`                |
| OR            | 或逻辑操作符，例如 `level:ERROR OR level:WARNING`            |
| NOT           | 非逻辑操作符，例如 `level:ERROR NOT pid:1234`                |
| TO            | 范围 逻辑操作符，例如 `request_time:[0.1 TO 1.0]`            |
| ""            | 双引号，引用一个短语词组（短语当作一个整体词组），例如 `name:"john Smith"` |
| ：             | 冒号，表示作用于的 key 字段，即键值检索，例如 `level:ERROR`    |
| *             | 通配符查询，匹配零个、单个、多个字符，例如 `host:www.test*.com` |
| ?             | 通配符查询，匹配单个字符，例如 `host:www.te?t.com`           |
| ()            | 分组操作符，控制逻辑运算优先级，例如 `(ERROR OR WARNING) AND pid:1234` |
| >             | 范围操作符，表示大于某个数值，例如 `status:>400`             |
| >=            | 范围操作符，表示大于等于某个数值，例如 `status:>=400`        |
| <             | 范围操作符，表示小于某个数值，例如 `status:<400`             |
| <=            | 范围操作符，表示小于等于某个数值，例如 `status:<=400`        |
| []            | 范围操作符，包含边界值的范围，例如 `age:[20 TO 30]`          |
| {}            | 范围操作符，不包含边界值的范围，例如 `age:{20 TO 30}`        |
| \             | 转义符号，转义后的字符表示符号本身，例如 `url:\/images\/favicon.ico"` |
| +             | 逻辑操作符，类似 AND，`+A` 表示 `A` 一定存在，例如 `+level:ERROR +pid:1234` |
| -             | 逻辑操作符，类似 NOT，`-A` 表示 `A` 不存在，例如 `+level:ERROR -pid:1234` |
| \|\|          | 或逻辑，类似 OR，例如 `level:ERROR \|\| level:WARNING`          |
| &&            | 与逻辑，类似 AND，例如 `level:ERROR && pid:1234`              |
| !             | 非逻辑，类似 NOT，例如 `level:ERROR !pid:1234`                |
| /             | 正则表达式标识符，/${regExp}/ ,  例如 `/[mb]oat/`表示搜索包含 moat 或 boat 的结果 |
| \_exists\_    | \_exists\_:key，返回 key 不为空的值，例如 `_exists_:userAgent`  表示搜索 `userAgent `字段有值的结果 |
| ~             | 相似搜索，例如 `level:errro~`，可以命中 level 为 error 关键字的结果 |

>?
>
> - 语法操作符区分大小写，例如 AND、OR 表示检索逻辑运算符，而 and、or 视为普通词组。
> - 多个检索语句用空格连接时，视为”或“逻辑，例如 `warning error` 表示包含 `warning` 或 `error` 关键字的结果。
> - 语法中的字符均为保留字符，若检索关键字中包含这些语法保留字符，均需要转义。
> - 使用键值检索时（形如 key：value），键名（key）必须在日志主题的键值索引配置项里面。



##  检索语句示例

| 检索场景                                                     | 检索语句                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 检索包含 `ERROR` 关键字的日志                               | `ERROR`                                                      |
| 检索失败的日志（状态码大于400）                             | `status:>400`                                                |
| 检索 `GET` 请求中失败（状态码大于400）的日志                 | `method:GET AND status:>400`                                 |
| 检索 `ERROR` 或 `WARNING` 级别的日志                         | `level:ERROR OR level:WARNING`                               |
| 检索非 `INFO` 级别 的日志                                   | `NOT level:INFO`                                             |
| 检索`192.168.10.10`主机上非 `INFO` 级别的日志              | `__SOURCE__:192.168.10.10 NOT level:INFO`                    |
| 检索`192.168.10.10`主机上`/var/log/access.log` 文件中不包含 `INFO` 级别的日志 | `(__SOURCE__:192.168.10.10 AND __FILENAME__:"/var/log/access.*") NOT level:INFO` |
| 检索`192.168.10.10`主机上 `ERROR` 或 `WARNING` 级别的日志  | `__SOURCE__:192.168.10.10 AND (level:ERROR OR level:WARNING)` |
| 检索 `4XX` 状态码的日志                                     | `status:[400 TO 500}`                                        |
| 检索元数据中容器名为 `nginx` 的日志                           | `__TAG__.container_name:nginx`                               |
| 检索元数据中容器名为 `nginx`，且请求延时大于1s 的日志        | `__TAG__.container_name:nginx AND request_time:>1`           |
| 检索包含 `message` 字段的日志，即 `message` 字段有值的日志  | `message:*` 或者 `_exists_:message`                          |
| 检索不包含 `message` 字段的日志                             | `NOT _exists_:message`                                       |
| 检索 `message` 字段为空的日志                              | `message:""`                                                 |

