## 操作场景
在配置同步任务时，可以选择 SQL 同步策略，设置后，只有满足设置条件的 SQL 数据才会同步到目标数据库，这样用户可以根据场景，灵活设置多个数据库之间的同步方案，或者进行数据表的拆分。

DTS 支持如下维度的 SQL 过滤：
- DML 过滤：支持类型 Insert、Update、Delete。

- DDL 过滤：支持选择具体的 DDL 操作，如 CREATE TABLE、CREATE VIEW、 DROP INDEX 等。

- Where 条件过滤：支持对单个表设置自定义过滤条件。
  
> ?当前支持在如下数据同步链路中进行 DDL 过滤和 Where 条件过滤。
>
> - MySQL > MySQL/MariaDB/TDSQL-C MySQL
> - MariaDB > MySQL/MariaDB
> - Percona > MySQL/MariaDB
> - TDSQL-C MySQL > MySQL/TDSQL-C MySQL

## 约束限制
Where 条件过滤支持对单张表进行设置，需要对多张表进行过滤时，对每张表分别进行设置即可。

## 操作步骤
1. 在 [同步任务](https://console.cloud.tencent.com/dts/replication) 的**设置同步选项和同步对象**页面中，选择不同的 SQL 策略。
   - DML：支持类型 Insert、Update、Delete。
   - DDL：
     - 勾选 **DDL**，不勾选 **DDL 自定义**开关，则同步源数据库的所有 DDL 到目标数据库。
     - 勾选 **DDL**，同时勾选 **DDL 自定义**开关，可以自定义选择具体的 DDL 策略，只有勾选的策略会同步到目标库。
     - 不勾选 **DDL**，则所有的 DDL 都不会同步到目标库。
<img src="https://qcloudimg.tencent-cloud.cn/raw/d8a552de769ff3fe7062ffb4ae2485f4.png" style="zoom:70%;" /> 
2. 在同步对象选项右侧的已选对象中，选择对应的表，单击右边的编辑按钮，设置 Where 条件过滤。
<img src="https://qcloudimg.tencent-cloud.cn/raw/6ebdcf5b24f2038f6037e919b58638ab.png" style="zoom:50%;" />
>?Where 条件过滤设置规则说明：
>- 对于 INSERT 操作，需要插入的数据满足条件过滤规则才能生效，对于 DELETE 操作，需要删除的数据满足条件过滤规则才能生效，对于 UPDATE 操作，则需要更新前后的数据都满足条件过滤规则才能生效。
>- 输入的规则必须是一个合法的 BOOL 表达式，并且表达式的规则相对于 MySQL 更为严格，一些在 MySQL 中支持但可能产生 WARNING 的语法（如字符串同数字比较，c1 + c2 < "abc" ），此处不支持。逻辑运算、算术运算、比较运算规则和优先级同 MySQL 一致，支持通过括号改变运算优先级，操作数中有 NULL 时，运算规则也同 MySQL 一致。DTS 系统会对输入的条件过滤规则进行验证，如果不合法会给出提醒。
>- 基本的运算规则如下：
>  - 支持引入列名作为变量。
>  - 支持逻辑运算（NOT，AND，OR，XOR，&&，||）。
>  - 支持数字类型（有符号/无符号的整型 TINYINT、SMALLINT、MEDIUMINT、INT、BIGINT，浮点类型 FLOAT 和 DOUBLE，精确类型  DECIMAL）及其算术运算（+、-、\*、/、%、DIV、MOD）和比较运算（=、!=、>、<、>=、<=、<>、<=>）。  
>  - 支持字符串类型（CHAR，VARCHAR）及其比较运算（二进制比较）。  
>  - 支持日期类型（DATE，DATETIME，TIMESTAMP）及其比较运算。 
>  - 支持时间类型（TIME）及其比较运算。支持日期/时间类型变量同字符串比较，此时字符串被转换为日期/时间类型常量，按照日期/时间比较规则进行。  
>  - 输入 TIMESTAMP 默认时区为 UTC+0 时区，比较时会转换为 UTC+0 时区进行。 
>    示例：输入过滤规则为 'c1 > "2016-10-01 09:00:00"'，其中 c1 为 TIMESTAMP 类型的列。则"2016-10-01 09:00:00"解析为 UTC+0 时区时间，相当于"2016-10-01 09:00:00 +00:00"，比较时 c1 也会转换为 UTC+0 时区时间。
>   
3. 单击**确定**。
4. 单击**保存并下一步**进行后续同步任务流程。

