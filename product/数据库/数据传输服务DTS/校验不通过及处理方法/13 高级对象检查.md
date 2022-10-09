
## MySQL/MariaDB/Percona 检查详情
选择迁移/同步高级对象时，DTS 会对如下内容进行校验。报错项必须要处理才能继续任务，警告项用户评估业务风险后可忽略，继续任务。

- 报错项：目标实例参数 log_bin_trust_function_creators 必须为 ON。

- 警告项：
   - 迁移/同步高级对象与库表重命名功能冲突，选择高级对象后需要取消库表重命名。
   - 选择高级对象的函数，存储过程时，DTS 会检查源库中 `DEFINER` 对应的 user1（ [DEFINER = user1]）和执行任务账号 user2 是否一致。
     - 如果一致则迁移/同步后不做改动。
     - 如果不一致，则迁移/同步后修改 user1 在目标库中的 `SQL SECURITY` 属性，由 `DEFINER` 转换为 `INVOKER`（ [INVOKER = user1]），同时设置目标库中 `DEFINER` 为执行任务账号的 user2（[DEFINER = 执行任务账号user2]）。
     
   - 高级对象的迁移/同步时间：  
     - 存储过程和函数，在“源库导出”阶段进行迁移/同步。 
     - 触发器和事件，没有增量任务，在任务结束时进行迁移/同步；有增量任务，在用户单击**完成**操作后开始迁移/同步，所以单击**完成**后任务的过渡时间会长一些。

## 修复方法

修改 log_bin_trust_function_creators 参数。

log_bin_trust_function_creators 用于控制是否信任用户将存储函数写入 binlog 日志中。设置为 OFF ，仅 SUPER 权限的用户可将创建的存储函数操作写入 binlog 日志，设置为 ON ，非 SUPER 权限的用户也可将创建的存储函数操作写入 binlog 日志中。

发生报错时，请参考如下步骤进行修改。

1. 登录源数据库。
2. 参考如下内容修改 log_bin_trust_function_creators 参数。
```
set global log_bin_trust_function_creators = ON;
```
3. 通过如下命令查看参数修改是否生效。
```
show variables like '%log_bin_trust_function_creators%';
```
系统显示结果类似如下：
```
mysql>  show variables like '%log_bin_trust_function_creators%';
+---------------------------------+-------+
| Variable_name                   | Value |
+---------------------------------+-------+
| log_bin_trust_function_creators | ON    |
```
4. 重新执行校验任务。


