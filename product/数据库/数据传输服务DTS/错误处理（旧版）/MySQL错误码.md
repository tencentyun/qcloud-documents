
|错误码|	说明	|处理措施|
|---------|--------|----------|
|-254 |查询目标实例获取信息失败|确认目标实例处于正常状态，迁移任务进行过程中请不要对目标实例并发其他任务。|
|-419  |阿里云迁移，目标实例版本不符合要求|阿里云迁移，目前只支持目标实例5.6的 TencentDB 版本，且目标实例同步状态为【异步】，目前暂不支持目标实例为半同步或者强同步的实例。|
|-256  |和源实例建立连接失败|检查源实例帐号的连接权限，确保可通过输入帐号密码与源实例建立连接，检查源实例的可连接状态。|
|-255 |查询源实例信息失败|请保证在迁移过程中源实例可正常连接，源实例对应帐号权限不要进行修改。errormsg 有 MySQL 原生报错信息。|
|-260 |源实例和目标实例的 GTID 配置不符合要求|<li>对于目标 MySQL 5.7 实例，源实例和目标实例需要同时开启或者关闭 GTID。 <li>对于其他版本 MySQL 实例，不支持从源 GTID 迁移到目标非 GTID。|
|-261| 源实例在 ONLINE 迁移模式下，需要开启 binlog|online 迁移模式，源实例没有设置 log_bin 为1，没有开启 binlog，无法同步增量数据。|
|-262 |源实例在 ONLINE 迁移模式下，binlog 格式不能为 statement|online 迁移模式，源实例的 binlog 格式需为 row 或者 mixed。|
|-267 |源实例的 innodb_stats_on_metadata 需要设置为 off|迁移过程需要配置 innodb_stats_on_metadata 为 off。|
|-264 |源实例在 ONLINE 迁移模式下，server_id 需要配置为非1正整数，且与目标实例不同|online 迁移模式，源实例需要配置正确的 server_id，同时与目标实例不同。|
|-418 |指定库表迁移（非 schema）模式下，源实例 events 需要为 disable 状态|对于 online、backup 模式下的指定库表迁移，源实例的 events 需要配置为 disable（状态配置源实例 set global event_scheduler=OFF）。|
|2001041 |源实例是正在同步的 slave，但没有开启 log_slave_update|对于源实例是 slave 且正在同步的情况，需要配置 log_slave_updates 为 on。|
|2001040 |源实例是 5.7，包含不支持的列类型|源实例是5.7的情况，目前不支持 json 和虚拟列。|
|-257 |源和目标兼容性不满足要求|兼容性要求： <br>目前迁移支持同大版本 mysql 迁移（源和目标版本相同） <br>对于不同大版本，只支持(5.1 > 5.5，5.5 > 5.6)<br>character_set_server lower_case_table_names 这两个 global 配置需要源和目标相同。|
|-258 |online 或者 backup，目标实例容量不足|需要是源实例容量的1.3倍以上。|
|-259 |整实例迁移目标实例不为空|整实例迁移请确保目标实例没有用户 db，避免出现覆盖。|
|2001037 |库表模式迁移，输入的库表在源没有找到|库表模式迁移，请确保输入库表在源能够找到。|
|-268 |库名重复|库表迁移模式，对于整库迁移，请确保源实例和目标实例不存在重复的库表。|
|-269| 表名重复|库表迁移模式，请确保迁移目标库表在源和目标没有重复的库表名。|
|-265| 库表模式迁移，外键依赖的表没有在迁移目标库表当中|-|
|-266 |目标库表存在存储引擎不支持|对于源库表，目前支持存储引擎：<li>5.6不支持：MEMORY、BLACKHOLE、 CSV、ARCHIVE 引擎。 <li> 5.7不支持：MRG_MYISAM、MEMORY、BLACKHOLE、CSV、ARCHIVE。<li>支持 tokudb 引擎。|
|-420| 源 tokudb 存在压缩|quicklz/lzma/snappy/uncompressed 对于 toku 这几种 row_format 不支持。|
|-421 |源 tokudb 存在 cluster index|存在 column_key 为 CLU 的表。|
|-292 |目标实例 RO 状态不正常|迁移任务发起需要目标实例 RW 和 RO 均处于正常状态。|
|-405 |源实例存在 row_format 为 fixed 的库表|源实例库表建议修改为非 row_format 格式的 innodb 引擎库表。格式修改后，数据库表会被重建。|
|-417 |目标实例和源实例主从关系异常|检查源实例网络连接是否正常，检查在迁移过程中是否有用户自身对目标实例进行写入形成双写。 |
|-253 |收到用户终止撤销任务的请求|收到用户发送的终止撤销迁移任务的请求，撤销迁移任务，撤销成功任务进入回滚完成状态。|
|-407 |用户输入参数有误|输入参数有误，检查输入参数格式，例如库表名称是否合法等。|
|-411 |源实例帐号权限检查需求失败 | 请提供满足要求的源实例用户帐号权限需求详情，根据需求的任务配置，给出满足权限需求的用户帐号。<br>例如：全量检测是需要对 session 进行 binlog 格式的设置，这个是需要 super 权限的，解决办法：1.选抽样检测就不需要 super 权限，2.通过对帐号增加 super 权限授权。</br>|
|6001000|备份系统异常|请通过 [在线支持](https://cloud.tencent.com/online-service?from=connect-us) 联系我们处理。|
|-41 |同步数据失败，主从异常|请通过 [在线支持](https://cloud.tencent.com/online-service?from=connect-us) 联系我们处理。|
|996|内部错误，迁移模式和对比方式不同，后端是不同的配置，如果配置文件找不到就报错|请通过 [在线支持](https://cloud.tencent.com/online-service?from=connect-us) 联系我们处理。|

>?如遇到其他错误码，请通过 [在线支持](https://cloud.tencent.com/online-service?from=connect-us) 反馈。
