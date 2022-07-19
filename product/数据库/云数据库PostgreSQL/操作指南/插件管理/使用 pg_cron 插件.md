
pg_cron 是一个简单的基于 cron 的 PostgreSQL（10或更高版本）任务调度器，作为扩展在数据库中运行。它使用与常规 cron 相同的语法，允许您直接从数据库定时调度并执行数据库命令。

本文为您介绍 PostgreSQL pg_cron 插件的使用方法。

## 启用 pg_cron 扩展
1. 若需使用 pg_cron，请先 [提交工单](https://console.cloud.tencent.com/workorder/category)，将 pg_cron 添加至数据库 shared_preload_libraries 参数中。修改此参数，需要重启实例，请选择一个业务空闲期去进行操作。

2. 完成参数修改后，请进入 postgres 库中执行，使用管理员账户运行以下命令：
```
CREATE EXTENSION pg_cron;
```

3. 当前 pg_cron 配置仅能在 postgres 库中执行计划任务，若需要在其他 database 中运行计划任务，请参见 [对 postgres 以外的数据库设置定时任务](#wpjhzy)。


4. 默认 pg_cron 创建完成后，其配置数据以及任务执行只能由管理员用户进行设置。若需要其他用户进行 pg_cron 设置或者执行，则需要向其他用户授予 cron 元数据库的权限，请运行以下命令。
```
postgres=> GRANT USAGE ON SCHEMA cron TO other-user;
```
此权限为 other-user 提供了对 cron 元数据的访问权限以计划和取消计划 cron 任务。但是，为了成功运行 cron 任务，还需要具有对 cron 任务中对象的访问权限。如果用户没有权限，则任务将失败，postgresql.log 中将显示错误。
如下实例，用户没有访问 pgbench_accounts 表的权限。
```
2020-12-08 16:41:00 UTC::@:[30647]:ERROR: permission denied for table pgbench_accounts
2020-12-08 16:41:00 UTC::@:[30647]:STATEMENT: update pgbench_accounts set abalance = abalance + 1
2020-12-08 16:41:00 UTC::@:[27071]:LOG: background worker "pg_cron" (PID 30647) exited with exit code 1
```
cron.job_run_details 表中的其他消息如下所示：
```
postgres=> select jobid, username, status, return_message, start_time from cron.job_run_details where status = 'failed';
jobid |  username  | status |                   return_message                    |          start_time
-------+------------+--------+-----------------------------------------------------+-------------------------------
   143 | unprivuser | failed | ERROR: permission denied for table pgbench_accounts | 2020-12-08 16:41:00.036268+00
   143 | unprivuser | failed | ERROR: permission denied for table pgbench_accounts | 2020-12-08 16:40:00.050844+00
   143 | unprivuser | failed | ERROR: permission denied for table pgbench_accounts | 2020-12-08 16:42:00.175644+00
   143 | unprivuser | failed | ERROR: permission denied for table pgbench_accounts | 2020-12-08 16:43:00.069174+00
   143 | unprivuser | failed | ERROR: permission denied for table pgbench_accounts | 2020-12-08 16:44:00.059466+00
(5 rows)
```

##  pg_cron 计划任务配置描述
pg_cron 提供三个主要操作：增加任务项、删除任务项、查看任务信息。

### cron.schedule() 函数
此函数计划 cron 任务。任务最初是在默认 postgres 数据库中计划的。该函数返回一个表示任务标识符的 bigint 值。要计划任务在 PostgreSQL 数据库实例的其他数据库中运行，请参阅 [对 postgres 以外的数据库设置定时任务](#wpjhzy) 中的示例。
该函数有两种语法格式。

**语法**
```
cron.schedule (job_name,
    schedule,
    command
);

cron.schedule (schedule,
    command
);
```

**参数**

| 参数 | 描述 | 
|---------|---------|
| job_name | cron 任务的名字，可为空不设置。 | 
| schedule | 表示 cron 任务时间表的文本。格式是标准 cron 格式。 | 
| command | 要运行的命令的文本。 | 

**示例**
```
postgres=> SELECT cron.schedule ('test','0 10 * * *', 'VACUUM pgbench_history');
 schedule
----------
      145
(1 row)

postgres=> SELECT cron.schedule ('0 15 * * *', 'VACUUM pgbench_accounts');
 schedule
----------
      146
(1 row)
```
schedule 使用标准的 cron 语法，其中 * 表示“每个该时间运行”，特定数字表示“仅在这个数字时运行”。
```
# 格式是：分 时 日 月 星期
# week (0 - 6) = sun,mon,tue,wed,thu,fri,sat
# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,...,sat
# |  |  |  |  |
# *  *  *  *  * 
```

### cron.unschedule() 函数
此函数删除 cron 任务。您可以传入 job_name 或 job_id。请确保您是当前 job_id 所对应的策略的拥有者。该函数返回一个布尔值，指示成功或失败。

该函数使用以下语法格式。
**语法**
```
cron.unschedule (job_id);

cron.unschedule (job_name);
```

**参数**

| 参数 | 描述 | 
|---------|---------|
| job_id | 计划 cron 任务时从 cron.schedule 函数返回的任务标识符。 | 
| job_name | 使用该 cron.schedule 函数计划的 cron 任务的名称。 | 

**示例**
```
postgres=> select cron.unschedule(108);
 unschedule
------------
 t
(1 row)

postgres=> select cron.unschedule('test');
 unschedule
------------
 t
(1 row)
```

### pg_cron 表
将以下各表用于计划任务和记录任务完成的方式。

| 表 | 描述 | 
|---------|---------|
| cron.job | 包含有关每个计划任务的元数据。与此表的大多数交互应使用 cron.schedule 和 cron.unschedule 函数完成。<br>注意：不建议直接向此表授予更新或插入权限。|
| cron.job_run_details | 包含过去运行的计划任务的历史信息。这对于调查运行的任务的状态、返回消息以及开始和结束时间非常有用。<br>为了防止此表无限增长，请定期清除此表。 |

## 设置 pg_cron 定时任务
1. 如果您可能希望在选择的时间计划对特定表执行 vacuum 操作，则可以使用 cron.schedule 函数设置定时任务，如每天22:00 (GMT) 在特定表上使用 VACUUM FREEZE。执行设置语句所返回的数字是指当前任务的任务编号。
```
SELECT cron.schedule('manual vacuum', '0 22 * * *', 'VACUUM FREEZE pgbench_accounts');
 schedule
----------
1
(1 row)
```
2. 其中函数存在3个入参，第一个入参为任务名（字符型），第二个为 cron 定时语法，第三个为具体的执行 SQL。


## 查看 pg_cron 定时任务
在设置了定时任务后，可通过 cron.job 表查看已经配置了的定时任务，如执行以下语句。
```
SELECT * FROM cron.job;

jobid | schedule   |  command  | nodename  | nodeport | database | username | active 
-------+------------+-----------+-----------+----------+----------+----------+--------
    1 | 0 22 * * * |   VACUUM ... | localhost |     5432 | postgres | test     | t
```

## 删除 pg_cron 定时任务
如果某一条定时任务无需使用，则需要将此定时任务删除。执行下列语句可将定时任务删除。
```
SELECT cron.unschedule(1);

 unschedule
------------
          t
```

## 查看定时任务执行历史
运行上述示例之后，您可以按如下方式检查 cron.job_run_details 表中的任务状态以及执行情况。
```
postgres=> select * from cron.job_run_details;
 jobid | runid | job_pid | database | username | command | status | return_message | start_time | end_time
-------+-------+---------+----------+----------+----------------------------------------+-----------+----------------+-------------------------------+-------------------------------
 1 | 1 | 3395 | postgres | adminuser| vacuum freeze pgbench_accounts | succeeded | VACUUM | 2020-12-04 21:10:00.050386+00 | 2020-12-04 21:10:00.072028+00
(1 row)
```

## 清除 pg_cron 历史记录表
1. cron.job_run_details 表包含 cron 任务的历史记录，随着时间的推移，这些历史记录可能会变得非常大。我们建议您计划清除此表的记录。例如，保留一周的条目可能足以进行故障排除。

2. 以下示例使用 cron.schedule 函数计划每天午夜运行以清除 cron.job_run_details 表的记录。如只保留了过去七天的历史记录，如下所示。
```
SELECT cron.schedule('0 0 * * *', $$DELETE 
    FROM cron.job_run_details 
    WHERE end_time < now() – interval '7 days'$$);
```

## 禁用 pg_cron 历史记录	
- 如果需要完全禁用向 cron.job_run_details 表中写入任何内容，请在控制台修改将 cron.log_run 参数设置为 off。
如果您执行此操作，pg_cron 扩展不再写入表，只会在 postgresql.log 文件中生成错误。所有的错误信息将都可以在控制台中的错误日志中查看到。

- 使用以下命令检查 cron.log_run 参数的值。
```
postgres=> SHOW cron.log_run;
```

## [对 postgres 以外的数据库设置定时任务](id:wpjhzy)

默认场景下 pg_cron 的元数据全部保存在 postgres 数据库中。若需要对其他 database 中的对象执行定时任务，则需要执行以下操作。

1. 如需要对 test 数据库执行某一个表的 vacuum 操作，则首先需要使用 pg_cron 的管理员用户在 postgres 库中执行 cron.schedule 函数，设置定时任务。
```
postgres=> SELECT cron.schedule('test manual vacuum', '29 03 * * *', 'vacuum freeze test_table');
```
2. 使用管理员用户，执行数据库更改，使定时任务执行 database 设置为想要设置的库。请注意 jobid 一定要为第一步中执行返回的 jobid。如下命令
```
postgres=> UPDATE cron.job SET database = 'test' WHERE jobid = 106;
```
3. 通过查询 cron.job 表进行验证。
```
postgres=> select * from cron.job;
 jobid | schedule | command | nodename | nodeport | database | username | active | jobname
-------+-------------+----------------------------------------+-----------+----------+-----------+-----------+--------+-------------------------
 2 | 29 03 * * * | vacuum freeze test_table | localhost | 8192 | test | adminuser | t | database1 manual vacuum
 1 | 59 23 * * * | vacuum freeze pgbench_accounts | localhost | 8192 | postgres | adminuser | t | manual vacuum
(2 rows)
```

## [pg_cron 参数](id:pgcs)
以下是用于控制 pg_cron 扩展行为的参数列表。

| 参数 | 描述 | 
|---------|---------|
| cron.database_name |保存 pg_cron 元数据的数据库。 | 
| cron.host |要连接到 PostgreSQL 的主机名。您无法修改此值。 | 
| cron.log_run |将运行的所有任务记录到 job_run_details 表中。值为 on 或 off。 | 
| cron.log_statement |在运行所有 cron 语句之前将其记入日志。值为 on 或 off。 | 
| cron.max_running_jobs |可以同时运行的最大任务数，若需要支持更多的任务，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 支持。 | 
| cron.use_background_workers	|使用后台工作程序而不是客户端会话。您无法修改此值。 | 

使用以下 SQL 命令来显示这些参数及其值。
```
postgres=> SELECT name, setting, short_desc FROM pg_settings WHERE name LIKE 'cron.%' ORDER BY name;
```
