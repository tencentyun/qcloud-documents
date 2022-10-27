## 概述

日志服务提供日志检索及分析能力，可通过检索分析语句检索匹配特定条件的日志，或针对匹配的日志使用 SQL 进行统计分析，获取日志条数、平均响应时间和错误日志占比等统计结果。

检索分析语句由检索条件和 SQL 语句组成，两者通过竖线`|`分割：

```
[检索条件] | [SQL语句]
```

**检索条件支持两种语法规则：**
- **Lucene 语法**：日志服务旧版本检索语法，采用 [开源 Lucene 语法](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html)，所有地域及日志主题均可使用。由于该语法并非专为日志检索设计，对特殊符号、大小写、通配符等有较多限制，使用较为繁琐，容易出现语法错误。
- **CQL 语法**：即 CLS Query Language，日志服务 CLS 专用检索语法。专为日志检索设计，语法学习门槛低，使用容易，推荐使用。
> !
> - CQL 语法当前仅以白名单方式供部分客户使用，可以在检索语句输入框右上角设置功能中查看当前日志主题是否支持 CQL。
> - CQL 暂不支持日志下载及定时 SQL 任务。
![](https://qcloudimg.tencent-cloud.cn/raw/dd6742d759e1d39a11806431ad7ce183.png)

## CQL 语法优势

* CQL 中逻辑操作符不区分大小写，例如：`level:ERROR AND pid:1234` 等价于 `level:ERROR and pid:1234`。
* CQL 中需要转义的特殊符号较少，例如：可直接使用 `url:/book/user/login/` 进行检索，而 lucene 语法会报错，需转义为`url:\/book\/user\/login\/`。
* 检索包含分词的字符串时，CQL 中各个分词之间为与的关系，而 lucene 语法为或的关系。例如：分词符为`/`时，CQL 中 `url:/book/user/login/` 等价于 `url:book AND url:user AND url:login`，lucene 中 `url:\/book\/user\/login\/` 等价于 `url:book OR url:user OR url:login`。
* 检索短语时，CQL 支持通配符，lucene 不支持。例如：分词符为`/`时，CQL 中 `url:"/book/user/log*/"` 可以检索到 `/book/user/login/` 及 `/book/user/logout/`。



## CQL 语法规则

### 语法规则

| 语法      | 说明                                                         |
| :-------- | :----------------------------------------------------------- |
| key:value | 键值检索，查询字段（key）的值中包含 value 的日志，例如：`level:ERROR` |
| value     | 全文检索，查询日志全文中包含 value的 日志，例如：`ERROR`         |
| AND       | “与”逻辑操作符，不区分大小写，例如：`level:ERROR AND pid:1234` |
| OR        | “或”逻辑操作符，不区分大小写，例如：`level:ERROR OR level:WARNING` |
| NOT       | “非”逻辑操作符，不区分大小写，例如：`level:ERROR NOT pid:1234` |
| ()        | 逻辑分组操作符，控制逻辑运算优先级，例如：`level:(ERROR OR WARNING) AND pid:1234` |
| "  "      | [短语检索](#pharseQuery)，使用双引号包裹一个字符串，日志需包含字符串内的各个词，且各个词的顺序保持不变，例如：`name:"john Smith"`<br />短语检索中不存在逻辑操作符，其等同于查询字符本身，例如：`name:"and"` |
| '  '      | [短语检索](#pharseQuery)，使用单引号包裹一个字符串，功能等价于`""`，当被检索短语中包含双引号时，可使用单引号包裹该短语，以避免语法错误，例如：`body:'user_name:"bob"'` |
| *         | [模糊检索](#wildcardQuery)，匹配零个、单个、多个字符，例如：`host:www.test*.com` ，不支持前缀模糊检索 |
| >         | 范围操作符，表示大于某个数值，例如：`status>400`              |
| >=        | 范围操作符，表示大于等于某个数值，例如：`status>=400`         |
| <         | 范围操作符，表示小于某个数值，例如：`status<400`              |
| <=        | 范围操作符，表示小于等于某个数值，例如：`status<=400`         |
| =         | 范围操作符，表示等于某个数值，例如：`status=400`              |
| \         | 转义符号，转义后的字符表示符号本身。当被检索的值包含空格、`:`、`"`、`'`、`*` 时，需进行转义，例如：`body:user_name\:bob` <br />使用双引号进行短语检索时，仅需转义`"`及`*`；使用单引号进行短语检索时，仅需转义`'`及`*`<br />未转义的`*`代表模糊检索 |
| key:\*     | text 类型字段：查询字段（key）存在的日志，无论值是否为空，例如：`url:*`<br>long/double 类型字段：查询字段（key）存在，且值不为空的日志，例如：`response_time:*  `   |
| key:""    | text 类型字段：查询字段（key）存在且值为空的日志，值仅包含分词符时也等价为空，例如：`url:""`<br>long/double 类型字段：查询字段（key）不存在，或值为空的日志，等价于 `NOT key:*` |



### 示例

| 场景                                         | 语句                                               |
| -------------------------------------------- | -------------------------------------------------- |
| 检索来源为某台机器的日志                     | `__SOURCE__:127.0.0.1` 或 `__SOURCE__:192.168.0.*` |
| 检索来源为某个文件的日志                     | `__FILENAME__:"/var/log/access.log"`               |
| 检索包含 `ERROR` 的日志                      | `ERROR`                                            |
| 检索失败的日志（状态码大于400）              | `status>400`                                       |
| 检索 `GET` 请求中失败（状态码大于400）的日志 | `method:GET AND status>400`                        |
| 检索 `ERROR` 或 `WARNING` 级别的日志         | `level:(ERROR OR WARNING)`                         |
| 检索非 `INFO` 级别 的日志                    | `NOT level:INFO`                                   |



### 短语检索

<span id="pharseQuery"></span>

使用双引号或单引号包裹一个字符串进行检索，例如`name:"john Smith"`、`__FILENAME__:"/var/log/access.log"`。与不使用引号包裹的检索相比，短语检索表示日志需在包含字符串内各个词的同时，词之间的顺序也与检索条件严格一致。

例如有如下两条日志，分词符为`/`：

```
#1 __FILENAME__:"/var/log/access.log"
#2 __FILENAME__:"/log/var/access.log"
```

* 使用`__FILENAME__:/var/log/access.log`进行检索时会同时检索到上述两条日志，因为非短语检索不要求词之间的顺序
* 使用`__FILENAME__:"/var/log/access.log"`进行检索时仅会检索到第一条日志

短语检索的检索条件更加严格，检索较长的字符串时，建议使用短语检索。

短语检索内支持使用通配符，例如`__FILENAME__:"/var/log/access_*.log"`，但不支持在词的开头使用通配符，例如`__FILENAME__:"/var/log/*.log"`。且短语检索中的通配符仅能匹配到符合条件的128个词，返回包含这128个词的所有日志，指定的词越精确，查询结果越精确，非短语检索无该限制。



### 模糊检索

<span id="wildcardQuery"></span>

在日志服务中进行模糊检索，需要在词的中间或末尾加上通配符，可使用`*`匹配零个、单个、多个字符，例如：

- `IP:192.168.1.*` 表示在日志中查找 IP 为`192. 168.1`开头的日志，例如`192. 168.1.1`、`192. 168.1.34`等
- `host:www.te*t.com` 表示在日志中查找 host 为 `www.te` 开头、`t.com` 结尾的日志，例如 `www.test.com`、`www.telt.com` 等

>!
>- `*`不能用在词的开头，即不支持前缀模糊检索。
>- long 和 double 类型字段不支持使用`*`进行模糊检索，可以使用数值范围进行检索，例如：`status>400 and status<500`。

如果您需要使用前缀模糊查询，可使用如下方法替代：
- 添加分词符：例如日志为 `host:www.test.com`、`host:m.test.com`，需要查询字段中间包含 test 的日志，可为该字段添加分词符`.`，便可以直接使用 `host:test` 对日志进行检索。
- 使用 SQL中的 LIKE 语法：例如 `* | select * where host like '%test%'`，但这种方式相比检索条件性能较差，不适合日志数据量过大的场景。

短语检索内也支持使用通配符，例如`__FILENAME__:"/var/log/access_*.log"`，但不支持在词的开头使用通配符，例如`__FILENAME__:"/var/log/*.log"`。且短语检索中的通配符仅能匹配到符合条件的128个词，返回包含这128个词的所有日志，指定的词越精确，查询结果越精确，非短语查询无该限制。
