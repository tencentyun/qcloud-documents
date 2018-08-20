
## MySQL实例参数修改
对于云数据库MySQL版实例，您可以通过控制台修改参数。对于某些重要参数而言，使用不恰当的修改方式会导致灾备实例异常或数据不一致，所以本文将介绍一些重要参数的修改建议以减少您在设置参数时的疑虑。


### 1. 影响灾备实例的参数

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

### 2. 参数修改方式
目前提供使用控制台修改参数，但对于某一些重要的参数，使用不恰当的修改方式会导致灾备实例的同步异常或数据不一致。避免影响灾备实例，建议在业务上线前提前做好规划，如果因为业务的因素不得不对其进行修改，建议按照以下步骤进行操作：<br>
1、请选择业务低峰期对其参数进行修改，如有业务停机时间，暂停业务可加速参数修改操作；<br>
2、将主实例设置FTWRL(FLUSH TABLES WITH READ LOCK)锁；

`添加FTWRL锁命令如下：`<br>
`FLUSH TABLES WITH READ LOCK;`

> *说明：FTWRL是FLUSH TABLES WITH READ LOCK的简称(FTWRL)，该命令主要用于保证备份一致性。为了达到这个目的，它需要关闭所有表对象，在业务高峰期执行命令时容易导致库hang住。 FTWRL通过持有以下两把全局的MDL(MetaDataLock)锁*
 *全局读锁(lockglobalreadlock) 会导致所有的更新操作被堵塞*
 *全局COMMIT锁(makeglobalreadlockblockcommit) 会导致所有的活跃事务无法提交*

3、进入<a href="https://console.cloud.tencent.com/" target="_blank">MySQL管理控制台</a>配置灾备实例的参数，并重启灾备实例；<br>
4、进入<a href="https://console.cloud.tencent.com/" target="_blank">MySQL管理控制台</a>配置主实例的参数，并断开所有的会话，再释放FTWRL锁；

`释放FTWRL锁命令如下：`<br>
`UNLOCK TABLES;`

>  *说明：修改参数后对老连接不生效，因此需要在执行修改参数操作后，断开所有的会话，避免因老连接参数未生效而影响主、备实例的数据一致性。*












