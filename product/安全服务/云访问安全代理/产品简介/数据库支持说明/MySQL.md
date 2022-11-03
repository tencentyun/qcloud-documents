## 数据库字段类型支持情况

| 字段类型     | 字段加密  | 字段模糊查询 | 字段脱敏 |
| ----------- | ------- | ------- | ------- |
| char        | AES/SM4 |支持      | 支持    |
| varchar     | AES/SM4 |支持      | 支持    | 
| tinytext    | AES/SM4 |支持      | 支持    |
| text        | AES/SM4 |支持      | 支持    |
| mediumtext  | AES/SM4 |支持      | 支持    |
| longtext    | AES/SM4 |支持      | 支持    |
| tinyblob    | AES/SM4 |不支持    | 不支持  |
| blob        | AES/SM4 |不支持    | 不支持  |
| longblob    | AES/SM4 |不支持    | 不支持  |
| tinyint     | -       | -       | 支持    |
| smallint    | -       | -       | 支持    |
| mediumint   | -       | -       | 支持    |
| int/integer | -       | -       | 支持    |
| bigint      | -       | -       | 支持    |
| float       | -       | -       | 支持    |
| double      | -       | -       | 支持    |
| decimal     | -       | -       | 支持    |
| date        | -       | -       | -      |
| time        | -       | -       | -      |
| year        | -       | -       | -      |
| datetime    | -       | -       | -      |
| timestamp   | -       | -       | -      |


## 功能支持和使用限制
### 数据库

- 支持 **MySQL 5.7及以上**版本的数据库和兼容 MySQL 协议的数据库（如 `TDSQL`、`MariaDB`）。
- 不支持**8.0及以上**版本新增的 SQL 语法。
- 数据库、表和字段名不区分大小写。
- 加密字段长度需预先扩容以支持存储明文加密后更大长度的密文。
- 加密字段需使用**区分大小写**的`collation`，如 `utf8_general_bin`。

### 连接

- 同一连接内不允许切换登录用户。
- 仅只支持使用 `utf8` 和 `utf8mb4` 字符集连接代理。
- 应用连接代理的账号认证方式支持 `mysql_native_password`。
- 代理连接后端数据库的账号认证方式支持 `mysql_native_password` 和 `caching_sha2_password`。

### 加解密和脱敏

- 加解密算法支持 `AES` 和 `SM4` 算法。
- 支持对字符串和二进制类型字段的加解密。
- 支持对字符串和数值类型字段的动态脱敏。
- 支持两个及以上连续字符的密文模糊查询，仅支持`LIKE`语法，不支持正则查询。
- 密文模糊查询不支持转义字符，不支持`NO_BACKSLASH_ESCAPES`选项。
- 加密后密文超过字段长度时会保存**明文**。
- 同时存在密文和明文时，只能查询到到密文数据，存量明文数据需全量加密成密文。
- 支持 `SELECT`, `INSERT`, `REPLACE`, `UPDATE`, `DELETE` 语句中  `WHERE、ON、IN、INSERT VALUE、SET` 等各字段中非表达式的值加解密。
- 支持 `ROW` 条件中非表达式的值加解密，如支持 ` where (id, 'n2' , addr)=(2, name,'a2')` 中的字段加解密。
- 支持 `table references` 和 `where condition` 中的子查询字段中非表达式的值加解密。
- `UNION` 语句使用第一个 `SELECT 子句` 的加解密策略。
- 不支持存储过程的加解密。
- 不支持 `INSERT INTO ... SELECT ...` 等不经过代理处理的数据的加解密。
- 连接查询时，`JOIN`连接字段需选择同样的密钥和加密算法，否则密文不一致，无法正确进行连接查询。
- 支持`GROUP BY`, 但不保证和明文一致的顺序
- `information_schema`，`sys`，`mysql` 等内置数据库不支持加解密和脱敏。

### 协议

- 支持 `COM_QUERY`,`COM_STMT_PREPARE` 和 `COM_STMT_EXECUTE` 协议中字段加解密。
- 不支持 `COM_STMT_SEND_LONG_DATA`，`COM_STMT_RESET` 协议。
- 不支持 `COM_QUERY Protocol::LOCAL_INFILE_Data` 协议。

### 语句

- DML 执行前，需先切换到或指定相应的库。
- 加密字段不支持函数操作。
- 加密字段不支持数学运算。
- 加密字段不支持 `ORDER BY`。
- 加密字段不支持正则查询。
- 不支持包含自定义变量的语句。
- 不支持 `SELECT INTO` 语句。
- 不支持 `mysqldump` 中使用 CASB 不支持的特性和条件。
- 不支持 `CREATE TABLE xx AS SELECT`、`CHECK TABLE`、`CHECKSUM TABLE` 语法。
- 不支持 TDSQL 自定义的管理语法, 如 `help`, `repair` 等。
- 不支持 **COM_QUERY 协议**的  `Prepare`、`Execute` 语句的加解密。
- 除了 TDSQL 增删改查语句的行首注释外，SQL 语句中的其余注释不会生效。
- TDSQL 的 ShardKey 字段不能配置加密。

### 其他

- 所有表结构必须预先在策略控制台定义，账号必须和相应数据源绑定后才能通过 proxy 操作相应的数据源。
- 数据源删除后重新添加时，需断开存量连接，建立新的 MySQL 连接查询。
- 单次查询处理的数据大小需小于2^24字节。

## 常用 SQL 语句支持情况
>?示例中已配置加密策略的字段名称为：crypto_column。

- **插入语句**
<table>
<thead>
<tr>
<th width="20%">类型</th>
<th width="20%">支持情况</th>
<th width="60%">SQL 样例</th>
</tr>
</thead>
<tbody><tr>
<td>指定列名插入加密字段</td>
<td>支持</td>
<td>INSERT INTO table_a (id, col1, col2, crypto_column) VALUES (1, 'a', 'b', 'c');</td>
</tr>
<tr>
<td>不指定列名插入加密字段</td>
<td>支持</td>
<td>INSERT INTO table_a VALUES (1, 'a', 'b', 'c');</td>
</tr>
</tbody></table>

- **删除语句**
<table>
<thead>
<tr>
<th width="20%">类型</th>
<th width="20%">支持情况</th>
<th width="60%">SQL 样例</th>
</tr>
</thead>
<tbody><tr>
<td>加密字段作为查询条件</td>
<td>支持</td>
<td>DELETE FROM table_a WHERE crypto_column = 'c';</td>
</tr>
<tr>
<td>加密字段作为子查询语句的查询条件</td>
<td>支持</td>
<td>DELETE FROM table_a WHERE col1 IN (SELECT col2 FROM table_b WHERE crypto_column = 'c');</td>
</tr>
</tbody></table>

- **更新语句**
<table>
<thead>
<tr>
<th width="20%">类型</th>
<th width="20%">支持情况</th>
<th width="60%">SQL 样例</th>
</tr>
</thead>
<tbody><tr>
<td>加密字段作为查询条件</td>
<td>支持</td>
<td>UPDATE table_a SET col1 = 'd' WHERE crypto_column = 'c';</td>
</tr>
<tr>
<td>更新加密字段</td>
<td>支持</td>
<td>UPDATE table_a SET crypto_column = 'd' WHERE id = 1;</td>
</tr>
</tbody></table>

- **查询语句**
<table>
<thead>
<tr>
<th width="20%">类型</th>
<th width="20%">支持情况</th>
<th width="60%">SQL 样例</th>
</tr>
</thead>
<tbody><tr>
<td>加密字段作为返回结果，<code>SELECT</code>语法的支持</td>
<td>支持</td>
<td>SELECT crypto_column FROM table_a;</td>
</tr>
<tr>
<td>加密字段作为返回结果，<code>SELECT *</code>语法的支持</td>
<td>支持</td>
<td>SELECT * FROM table_a;</td>
</tr>
<tr>
<td>加密字段使用别名</td>
<td>支持</td>
<td>SELECT crypto_column a, col2 b  FROM table_a;</td>
</tr>
<tr>
<td>加密字段作为查询条件, 等值匹配</td>
<td>支持</td>
<td>SELECT * FROM table_a WHERE crypto_column = 'c';</td>
</tr>
<tr>
<td>加密字段作为查询条件，<code>IN</code>条件查询</td>
<td>支持</td>
<td>SELECT * FROM table_a WHERE crypto_column IN ('a', 'b', 'c');</td>
</tr>
<tr>
<td>加密字段作为子查询的条件</td>
<td>支持</td>
<td>SELECT crypto_column FROM (select * FROM table_a WHERE crypto_column = 'c') a;</td>
</tr>
<tr>
<td><code>JOIN</code>查询，加密字段作为<code>WHERE</code>条件</td>
<td>支持</td>
<td>SELECT table_a.id FROM table_a JOIN table_b ON table_a.id = table_b.id WHERE table_a.crypto_column = 'c';</td>
</tr>
<tr>
<td><code>JOIN</code>查询，加密字段作为<code>ON</code>条件</td>
<td>支持</td>
<td>SELECT table_a.id FROM table_a JOIN table_b ON table_a.id = table_b.id AND table_a.crypto_column = 'c';</td>
</tr>
<tr>
<td><code>JOIN</code>查询，加密字段作为返回结果</td>
<td>支持</td>
<td>SELECT table_a.crypto_column FROM table_a JOIN table_b ON table_a.id = table_b.id;</td>
</tr>
<tr>
<td><code>JOIN</code>查询，加密字段作为连表条件</td>
<td>支持:连表的加密字段需配置相同密钥和算法</td>
<td>SELECT table_a.id FROM table_a JOIN table_b ON table_a.crypto_column = table_b.crypto_column;</td>
</tr>
<tr>
<td><code>GROUP BY</code> 加密字段</td>
<td>支持</td>
<td>SELECT * FROM table_a WHERE id&gt;10 GROUP BY crypto_column;</td>
</tr>
<tr>
<td><code>ORDER BY</code> 加密字段</td>
<td>不支持</td>
<td>SELECT * FROM table_a WHERE id&gt;10 ORDER BY crypto_column;</td>
</tr>
<tr>
<td>加密字段模糊查询</td>
<td>支持:需配置密文模糊检索算法</td>
<td>SELECT * FROM table_a WHERE crypto_column LIKE '%cc%';</td>
</tr>
<tr>
<td>加密字段正则查询</td>
<td>不支持</td>
<td>SELECT * FROM table_a WHERE crypto_column REGEXP '^cc';</td>
</tr>
<tr>
<td>加密字段范围查询</td>
<td>不支持</td>
<td>SELECT * FROM table_a WHERE crypto_column &gt; 'a' AND crypto_column &lt; 'd';</td>
</tr>
<tr>
<td>函数处理加密字段</td>
<td>不支持</td>
<td>SELECT * FROM table_a WHERE substr(crypto_column, 0, 2) = 'aa';</td>
</tr>
</tbody></table>
