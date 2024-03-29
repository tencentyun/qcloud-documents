
本文主要介绍通过 DTS 数据迁移功能实现腾讯云数据库 MySQL 实例之间的数据迁移。DTS支 持结构迁移、全量数据迁移以及增量数据迁移，可以实现在不停服的情况下，在腾讯云数据库 MySQL 实例之间进行平滑迁移。

## [前提条件](id:qttj)
- 已 [创建云数据库 MySQL](https://cloud.tencent.com/document/product/236/46433)，支持版本：MySQL 5.5、MySQL 5.6、MySQL 5.7。
- 需要您在目标端 MySQL 中创建迁移帐号，需要帐号权限：待迁移对象的全部读写权限。

## 注意事项 
- 腾讯云数据库 MySQL 之间的数据迁移任务分为冷备数据导出和增量数据同步两步，其中，冷备数据导出以及迁移后的数据对比过程会对源库负载产生一定的影响，建议在业务低峰期或在备库上做数据库迁移。
- 如 lower_case_table_name 在迁移校验任务会检查源和目标的此项配置是否一致，不一致报错，请提前避免 lower_case_table_name 引起的重启问题。
- 整实例迁移在导入全量备份后，需要重启目标实例。

## 支持迁移类型
- 结构迁移：DTS 支持将迁移对象的结构定义迁移到目标实例中，目前 DTS 支持结构迁移的对象包括整实例和指定库表。
- 全量迁移：DTS 支持将源端 MySQL 数据库迁移对象中的全量数据，全部迁移到目标端云数据库 MySQL。
- 增量同步：在全量数据迁移的基础上，DTS 会读取并解析源端 MySQL 数据库的 binlog 信息，将源端 MySQL 中的增量更新同步到目标 MySQL。

## 预先检查项
1. 检查目标云数据库 MySQL 是否有同名库表，避免冲突。
2. 检查数据库版本，可支持 MySQL 5.5、MySQL 5.6、MySQL 5.7 版本迁移上云。
3. 检查目标云数据库 MySQL 容量必须大于源云数据库 MySQL。
4. 在源端云数据库 MySQL 上创建迁移帐号（若有已授权可用于数据迁移的帐号，也可不创建）。
```
GRANT ALL PRIVILEGES ON *.* TO '迁移帐号'@'%' IDENTIFIED BY '迁移密码';
FLUSH PRIVILEGES;
```
5. 确认源库 MySQL 变量。
通过`SHOW GLOBAL VARIABLES LIKE 'XXX';`查看 MySQL 全局变量，确认当前状态是否可以进行迁移：
```
server_id > 1
log_bin = ON;
binlog_format = ROW/MIXED
binlog_row_image = FULL
innodb_stats_on_metadata = 0
wait_timeout 建议大于或等于3600秒，务必小于7200秒
interactive_timeout 与 wait_timeout 设置相同时长
```
如果源实例为 slave 角色，需要在源实例中确认以下参数：
```
log_slave_updates = 1
```
6. 修改变量值。
a. 对于自建 MySQL 数据库，修改源库 MySQL 配置文件 my.cnf，需重启：
```
log-bin=[自定义binlog文件名]
```
b. 动态修改配置：
```
set global server_id = 99;
set global binlog_format=ROW;
set global binlog_row_image=FULL;
set global innodb_stats_on_metadata = 0;
```

## 操作步骤
1. 登录 [DTS 数据迁移控制台](https://console.cloud.tencent.com/dts/migration)，单击**新建迁移任务**，进入新建迁移任务页面。
2. 在新建迁移任务页面，选择源数据库和目标数据库的类型、地域信息，然后单击**立即购买**。
3. 在设置源和目标数据库页面，完成任务设置、源库设置和目标库设置，测试源库和目标库连通性通过后，单击**新建**。
>?如果连通性测试失败，请根据提示进行排查并解决后再次重试。
>
 - 任务设置
    - 任务名称：为任务指定名称。
    - 定时执行：可为您的迁移任务指定开始时间。
    - 标签：用于从不同维度对资源分类管理。
 - 源库设置    
    - 源库类型：请选择云数据库。    
> ?源数据库的账号长度不能超过16位。如果账号超过16位需要用户重新创建一个符合要求的账号。
 - 目标库设置    
    - 选择目标数据库实例，并输入目标库上的帐号及密码。
4. 在设置迁移选项及选择迁移对象页面，设置迁移类型、对象，单击**保存**。
>!
>- 仅在整实例迁移时会迁移 character_set_server、lower_case_table_names 配置项。
>- 若源实例所迁移的库表字符集设置和目标实例字符集设置不一致，则迁移会保留源实例的字符集设置。
>
 - 迁移类型：支持结构迁移、全量迁移、全量 + 增量迁移。
 - 迁移对象：支持整个实例、指定对象。
 - 使用源库 root 帐号覆盖目标库：因 root 帐号将用于云数据库安全校验，若源库 root 帐号不存在，会对后续使用云数据库造成不便。因此在整实例迁移时，需指定是否使用源库 root 帐号覆盖目标库 root 帐号。如需使用源库 root 帐号或目标库未设置 root，则选**是**，如需保留目标库的 root 帐号，则选**否**。
 - 目标库只读：选择只读后，在数据迁移过程中，从源数据库迁移的数据在目标数据库只能读取（Read Only），无法更改，直至用户单击完成迁移任务。
 - 数据一致性检测：支持全量检测和不检测。
![](https://main.qcloudimg.com/raw/72abd10c96b576914162f5312e44ecbb.png)
5. 在校验任务页面，进行校验，校验任务通过后，单击**启动任务**。
任务校验存在 3 种状态：
 - 通过：表示校验完全通过
 - 警告：表示校验不通过，迁移过程中或迁移后可能影响数据库正常运行但不影响迁移任务的执行。
 - 失败：表示校验不通过，无法进行迁移。如果校验失败，请根据出错的校验项，检查并修改迁移任务信息，然后重试校验。失败原因可单击【查看详情】查看“校验详情”。
![](https://main.qcloudimg.com/raw/a884ae48b08083d1a60e267d01f7124b.png)
6. 校验通过后，在迁移任务列表单击**立即启动**立即开始迁移数据。需要注意的是，如果您设定了迁移任务的定时时间，则迁移任务会在设定的时间开始排队并执行，如果没有设置定时任务，则迁移任务会立即执行。
迁移启动后，您可以在迁移任务下看到对应的迁移进度信息。在鼠标指向步骤后的感叹号提示符时，可显示迁移所需流程和当前所处阶段。
>!由于系统设计限制，一次性提交或排队多个迁移任务将按排队时间串行执行。
>
7. 创建迁移任务时默认必选增量同步选项，在数据迁移完成后，会将目标云数据库 MySQL 库设置成源数据库的备库，通过主备同步来把迁移过程中源库的新增的数据同步到目标云数据库 MySQL 库中。此时，源库上的修改都会同步到目标云数据库 MySQL 中。
>!在断开同步前，不要往目标数据库实例写入数据，否则可能引起源库和目标库数据不一致而数据比对失败，从而导致迁移失败。
>
8. （可选）在迁移过程中，如果您需要撤销迁移，可以单击**撤销**。
>!
>- 如果是单击**撤销**，不会对目标实例同步的数据进行清理。
>- 再次启动可能导致校验失败或任务失败，您可能需要手动清空目标库内的可能产生冲突的数据库或表，才能再次启动迁移任务。
>- 迁移单独的表时，需保证所有表外键依赖的表必须被迁移。
>
![](https://main.qcloudimg.com/raw/1404b46bdbe53bdd83201bad3ae39af9.png)
9. 完成迁移。
>!当迁移处于**未结束**状态时，迁移任务将一直进行，数据持续同步。
>
当迁移进度达到100%、目标与源库数据差距为0MB及目标与源库时间延迟为0秒时，即表示数据已经同步一致，可在单击右侧**完成**来完成迁移任务。
![](https://main.qcloudimg.com/raw/886a3c922df903a812bcbb7120aa847e.png)
完成后效果如下：
![](https://main.qcloudimg.com/raw/a539d58244ae7ffcbdc367b655fd1738.png)
