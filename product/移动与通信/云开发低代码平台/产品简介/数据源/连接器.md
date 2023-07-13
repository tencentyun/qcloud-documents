## MySQL 连接器介绍
MySQL 连接器提供了连接您自有的 MySQL 数据库，对接微搭开发的应用，以获取或操作数据库中的数据。
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/9b4f17b8d8dfa7765f8511d1fb1baecd.png" />

在使用 MySQL 连接器时，有两项配置需要进行操作：连接器配置及表达式编写。
- 连接配置：通过配置连接器，确定连接 MySQL 数据库的地址、方法、连接的数据库、认证等相关信息。
- Query 表达式编写：通过编写表达式，可以使用 SQL 语句进行数据库操作。同时可以通过表达式与页面组件、代码实现联动。 

### 连接配置说明

通过微搭编辑器的代码区，可以通过**新建 MySQL 查询**能力来新建表达式。在首次创建 MySQL 表达式时，如果没有 MySQL 连接配置，将会弹窗要求新建 MySQL 连接配置；在完成连接配置后，后续如果希望创建新的连接配置，或者修改当前连接配置，也可以通过连接配置选择的下拉菜单选择执行。
<img style="width:600px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/d1a5ff05924bfd682b6d1ac81a49d336.png" />

1. 连接配置用于告知微搭平台连接 MySQL 数据库的相关配置信息，在创建或修改连接配置时，有如下信息需要填写：
 - 连接配置名称、标识：用于标明数据库连接配置的名称、唯一标识。
 - 连接类型选择：MySQL 连接器支持通过公网对接第三方 MySQL，通过内网对接腾讯云 TDSQL-C MySQL版及 TencentDB MySQL。
 - 主机及端口：当选择通过IP/域名连接数据库时，需要填写 MySQL 数据的主机地址及连接端口，主机地址可以填写外网 IP 或域名。
 - 数据库ID：当选择连接腾讯云数据库时，可以通过填写对应的数据库实例 ID 确定所需连接的数据库。
 - 数据库名：填写需要连接及使用的数据库。
 - 用户名及密码：填写连接数据库所使用的用户名及密码认证信息。
 - SQL 预编译：默认开启状态，开启后，表达式中的 SQL 语句将预编译后执行。预编译可以极大的提高 SQL 执行时的安全性，避免 SQL 注入等风险。预编译详细说明可见 [MySQL Prepared Statements](https://dev.mysql.com/doc/refman/8.0/en/sql-prepared-statements.html)。开启预编译后，SQL 语句中不可以在数据库名、表名等位置使用参数传递。如需动态表名、数据库名，可以通过关闭预编译的方式提供，同时也可以通过编写多个表达式并选择执行的方式达到同样目的。
 - 连接参数：用于设置与数据库建立连接时的可选参数配置。连接参数详细请参见 [MySQL connection options](https://dev.mysql.com/doc/refman/8.0/en/connection-options.html)。
2. 在完成连接配置填写后，可以通过连接测试能力，验证连接配置的正确性。如测试失败，可以根据测试返回的 MySQL 报错，调整修正连接配置。
3. 完成测试后，可以单击**保存**，保存连接配置。如果是修改连接配置，在保存后，新的配置信息将生效，基于此连接配置的表达式，均将使用新的配置信息进行后续 SQL 的执行。
4. 如果后续需要修改连接配置，也可以通过下拉菜单选中配置，并通过单击**修改**，在打开的修改窗口中进行配置的修改调整。
>? 通过域名或 IP 的方式，仅支持通过公网访问数据库；通过数据库 ID 对接腾讯云数据库，仅可以支持上海地区的 TDSQL-C MySQL版及 TencentDB MySQL 数据库


### Query 表达式编写说明
通过微搭编辑器的代码区，可以通过**新建 MySQL 查询**能力来新建表达式。在完成 MySQL 连接配置后，就可以通过编写 SQL 语句实现表达式获取数据或操作数据的需求。
<img style="width:600px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/5f5e1b4fda04ac0c36152e64d74bc664.png" />


#### SQL 语句编写
SQL 语句根据实际业务需求进行编写即可。可以使用的包括 `SELECT`、`INSERT`、`UPDATE`、`DELETE` 语句。当前在 MySQL 连接器的表达式中暂时**不提供库表相关操作**的支持，包括 `CREATE`、`DROP`、`ALTER`、`TRUNCATE`。

SQL 语句示例如下：
```SQL
SELECT * FROM users；
# 从指定表中查询数据；可通过修改'users'指定到所需操作的表，可通过修改 '*' 为指定获取字段；

INSERT INTO users (name, email, phone) VALUES  ('{{$w.form.inputname.value}}', '{{$w.form.inputemail.value}}', '{{$w.form.inputphone.value}}')；
# 向指定表中插入数据；可通过修改'users'指定到所需操作的表，可通过 {{参数}} 引用组件、变量数据；

UPDATE users SET email='{{$w.form.modifyemail.value}}', phone='{{$w.form.modifyphone.value}}' WHERE id={{$w.selectuser.data.id}}；
# 更新指定表中的数据；可通过修改'users'指定到所需操作的表，可通过 {{参数}} 引用组件、变量数据；

DELETE FROM user WHERE id={{$w.selectuser.data.id}}；
# 删除指定表中的数据；可通过修改'users'指定到所需操作的表，可通过 {{参数}} 引用组件、变量数据；
```

在 SQL 语句的输入框中支持同时写入多条语句，使用 `;` 进行语句间分隔即可。表达式的输出值，以最后一条执行的 SQL 语句为准。
 
#### 参数获取
在 SQL 语句中，可以通过 `{{ }}` 的方式编写表达式，获取应用或页面的变量、组件值，用于 SQL 语句执行时的参数传递。
表达式的详细说明请参见 [表达式介绍](https://cloud.tencent.com/document/product/1301/86577)，如果需要获取组件、控件中的数据、属性，同样可以参见 [获取组件属性值](https://cloud.tencent.com/document/product/1301/90463)。
例如，在表达式中可以通过 `{{'%' + $w.input.value + '%'}}` 的方式实现拼接，达到使用 SQL 语句，通过用户输入，进行模糊查询的效果：`SELECT * from userinfo where username = {{'%' + $w.input.value + '%'}}`
特定系统参数获取：在表达式中，可以通过 `{{SERVER.userId}}` 获取当前应用的登录用户 ID，此表达式在运行后端解析，不依赖前端控件参数传递。
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/bfd3b7d6434dbe657ce7fddf258f5654.png" />



#### 表达式返回值
SQL 语句执行完成以后，结果将以 JSON 的形式返回。返回值可以在表达式参数中获取。
在表达式执行后，可以通过表达式的 records 字段获取到 SQL 的执行返回内容。当查询语句时，records 字段内包含查询到的具体数据，当插入、更新、删除语句时，records 字段内包含 affectedRows 字段，用于标识执行操作的行数。

在前端应用、代码、控件中，可以通过 `$w.queryname.records` 的方式，获取到 Query 的执行内容，其中 queryname 根据具体创建 Query 时的名称来确定。

表达式的详细引用和使用方式请参见 [Query 数据查询介绍](https://cloud.tencent.com/document/product/1301/93144)。

## 使用示例

通过本示例，将提供数据库数据表准备、连接配置、表达式编写和控件对接的完整示例。


### 数据库数据表准备

1. 准备自有的 MySQL 数据库，准备好数据库的连接信息，认证信息，例如：
 - Host: gz-cdb-xxxxxxx.sql.tencentcdb.com
 - Port: 63999
 - User: wedatest
 - Password: xxxxxx
2. 在数据库中创建 `test` 库，并使用如下接口创建表 `userinfo`。
```SQL
CREATE TABLE `userinfo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` text NOT NULL,
  `password` text,
  `email` text,
  `phone` text,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8
```
3. 表创建完成后，通过执行如下 SQL 语句，在表中预先准备一定的测试数据。
```SQL
INSERT INTO `userinfo` (`username`, `email`, `phone`) VALUES ('user1', 'user1@qq.com', '18612345678');
INSERT INTO `userinfo` (`username`, `email`, `phone`) VALUES ('user2', 'user2@qq.com', '18612345679');
INSERT INTO `userinfo` (`username`, `email`, `phone`) VALUES ('user3', 'user3@qq.com', '18612345680');
```

### 应用创建

通过微搭控制台，创建自定义应用。

### 配置数据库连接，创建查询表达式

1. 在应用代码区，新建数据查询，选择新建 MySQL 查询，创建表达式名字为 query1。
如果弹出连接配置信息，根据数据库的连接信息配置连接，填写连接配置名，填写数据库的 HOST 地址、PORT 端口、数据库名 test、认证 User 用户名、Password 登录密码。
<img style="width:600px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/19645c0adf2089022b6000089cca8bbb.png" />
2. 配置完成后测试连接，确保测试通过后保存配置。
3. 编写如下 SQL 语句：
```SQL
select * from userinfo
```
4. 保存表达式并测试运行，检查是否获取到数据库中已插入的数据，确保 SQL 运行正常。<br>
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/c999943ed826de739d717aa759d14bb6.png" />

### 对接应用控件，提供数据展示
1. 在应用中添加数据表格组件，编辑表格组件的表达式，填写为 `$w.query1.data.records`，其中 query1 为前面步骤创建的 MySQL 表达式名称。
2. 调整表格组件的列管理，确保包含了 `id`、`username`、`email`、`phone`、`created_at`、`updated_at` 列。
3. 刷新编辑区页面，可以查看到当前表格中已有了数据库中的内容。<br>
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/cf5684f89d1cf9da1dca155bbe0e4863.png" />


### 增加添加用控件，提供数据插入

1. 在页面上新增表单容器 form1，并在表单容器中新增3个单行输入，组件 ID 分别为 input1、input2、input3，分别用于用户名、手机、邮箱输入，根据情况配置好标题及数据校验规则。
2. 在表单容器中增加按钮，标题为新增，组件 ID 为 button1。

### 创建新增表达式
1. 在代码区再次新建 MySQL 查询，创建表达式名字为 query2，连接配置使用之前已经创建好的连接。
2. 编写如下 SQL 语句：
```SQL
INSERT INTO userinfo (`username`, `email`, `phone`) VALUES ({{$w.input1.value}}, {{$w.input3.value}}, {{$w.input2.value}});
```
3. 触发方式选择为手动触发执行。<br>
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/7296093d79ebc3e63252d4844b741d49.png" />



### 关联表达式与按钮控件
选择表单控件中的按钮，添加点击事件，选择**调用数据查询**，选择 Query 为新增表达式创建的 query2。
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/ebda3020d39eaeae1a594b3ff4efdf11.png" />


### 验证表达式执行
在页面的控件中填写具体插入用户信息，例如：“user4”，“1861234578”，“user4@qq.com”，并单击按钮，执行新增过程。执行完成后刷新页面，查看数据表格中是否已有新增的用户信息。


