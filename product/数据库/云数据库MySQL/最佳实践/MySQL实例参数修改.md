
## MySQL主实例参数修改的影响
对于云数据库MySQL实例，您可以通过控制台修改主实例的参数。其中对于某些重要参数而言，使用不恰当的修改方式会导致灾备、只读实例异常或数据不一致，本文将介绍如下重要参数修改后的影响。


#### lower_case_table_names
**默认值**：0
**作用：**创建数据库及表时，存储与查询时是否大小写敏感。该参数可以设置的值为0、1，默认的参数值为0，表示创建数据库及表时，存储与查询均区分大小写，反之则不做区分。
**影响：**主实例修改参数后，无法同步修改灾备实例的参数，当主实例大小写敏感而灾备实例大小写不敏感时，比如主实例创建两张表，表名分别为Test、TEst时，当灾备实例在应用对应日志时，会导致数据同步状态异常，而错误原因为TEst表名已存在。



#### auto_increment_increment
**默认值：**1
**作用：**用于自增列AUTO_INCREMENT的增量值，该参数可以设置的范围为1-65535，默认值为1。
**影响：**主实例修改参数后，无法同步修改灾备实例的参数，当主实例修改自增列的增量值，而灾备实例未同步更改，会导致主、备实例的数据不一致。
#### auto_increment_offset
**默认值：**1
**作用：**用于自增列AUTO_INCREMENT的起始值（偏移量），该参数可以设置的范围为1-65535，默认值为1。
**影响：**主实例修改参数后，无法同步修改灾备实例的参数，当主实例修改自增列的起始值，而灾备实例未同步更改，会导致主、备实例的数据不一致。
#### sql_mode
**默认值：**NO_ENGINE_SUBSTITUTION
作用：MySQL可以运行在不同sql mode模式，sql mode模式定义了mysql应该支持的sql语法，数据校验等。该参数5.6版本的默认参数值为NO_ENGINE_SUBSTITUTION，表示使用的存储引擎被禁用或未编译则抛出错误;5.7版本的默认参数值为ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE
,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION，其中ONLY_FULL_GROUP_BY表示在GROUP BY聚合操作时，如果在SELECT中的列、HAVING或者ORDER BY子句的列，必须是GROUP BY中出现或者依赖于GROUP BY列的函数列；STRICT_TRANS_TABLES为启用严格模式；NO_ZERO_IN_DATE是否允许日期中的月份和日包含0，且受是否开启严格模式的影响；NO_ZERO_DATE数据库不允许插入零日期，且受是否开启严格模式的影响；ERROR_FOR_DIVISION_BY_ZERO在严格模式下，INSERT或UPDATE过程中，如果数据被零除，则产生错误而非警告，而非严格模式下，数据被零除时MySQL返回NULL；NO_AUTO_CREATE_USER禁止GRANT创建密码为空的用户；NO_ENGINE_SUBSTITUTION使用的存储引擎被禁用或者未编译则抛出错误
影响：主实例修改参数后，无法同步修改灾备实例的参数，当主实例修改了sql mode模式，而灾备实例未同步更改，如主实例sql mode模式限制小于灾备实例sql mode模式的限制，可能会出现在主实例执行成功的SQL同步至灾备实例时出现报错，进而导致主、备实例数据不一致













