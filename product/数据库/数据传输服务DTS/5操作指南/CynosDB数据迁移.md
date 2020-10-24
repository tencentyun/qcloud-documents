
本文为您介绍通过数据传输服务 DTS，迁移 MySQL 5.7 数据库至云数据库 CynosDB（CynosDB for MySQL）的过程。

## 准备事项
<span id = "zhqxyjc"></span>
#### 帐号权限预检查
出于对用户源数据库的数据安全考虑，DTS 在迁移过程中会遵循最小权限原则，仅需要必要的权限。若用户迁移中使用的帐号超出 DTS 迁移所需的权限，DTS 会给出警告，且迁移无法开始。
因此建议用户在源 MySQL 数据库上创建迁移专用帐号，并进行如下授权：
```  	
# 在源数据库上创建迁移帐号（如 username），并进行相应授权：
create user 'username'@'%' identified by 'password';
grant RELOAD,LOCK TABLES,REPLICATION CLIENT,REPLICATION SLAVE,SHOW DATABASES,SHOW VIEW,LOCK TABLES,PROCESS on *.* to 'username'@'%';
grant SELECT,CREATE,DELETE,INSERT,UPDATE,DROP  on `__tencentdb__`.* to 'dts'@'%';
grant SELECT on *.* to 'username'@'%';            
FLUSH PRIVILEGES;
```

## 操作步骤
### 1. 新建迁移任务
1）登录 [DTS 控制台](https://console.cloud.tencent.com/dts )，在数据迁移页，单击【新建迁移任务】。
2）在“链路地域”选择对应地域，单击【0元购买】。

### 2. 设置迁移任务
设置任务、源库和目标库，网络连通性测试成功后，单击【新建】。
#### a. 任务设置
- 任务名称：为任务指定名称。
- 定时执行：为迁移任务指定开始时间。
>?
> - 修改定时任务，校验通过后，需要重新单击【定时启动】，任务才会定时启动。
> - 如果任务过了定时启动的时间，定时启动会变为立即启动，单击【立即启动】，会立刻启动任务。

#### b. 源库设置
- 源库类型：选择 MySQL。
- 接入类型：支持有公网 IP、云服务器自建、专线接入、VPN 接入等多种 MySQL  源库类型，本文以云数据库 MySQL 为例。
- 数据库实例：选择 MySQL 5.7 数据库实例。
- 帐号：在源库上预先创建的迁移专用帐号。

#### c. 目标库设置
- 目标库类型：选择 CynosDB for MySQL。
- 数据库实例：选择目标数据库实例，并输入目标库上的帐号及密码。
![](https://main.qcloudimg.com/raw/024ac636a6c311938c026a3fb0e8e0a8.png)

### 3. 选择迁移选项和迁移对象
设置要迁移的数据类型和对象，确认无误后，单击【保存】。
- **迁移类型**：【结构迁移】仅在目标库上进行 DDL 的创建，不迁移数据；【全量迁移】仅进行一次性的全量数据迁移（类似数据快照）；【全量+增量迁移】在全量迁移的基础上还会对新写入的增量数据进行迁移。
- **迁移对象**：支持整个实例迁移和指定对象迁移。
>!
>1. 目前仅支持 Table（及其 Index）和 View 两类数据对象的迁移；即使选择整个实例迁移，也仅支持前述两类数据对象。
>2. 源实例的参数设置、帐号、系统库表等不在迁移范围内。
>3. DTS 不做 View 的依赖合法性检查和依赖的自动选择。请用户迁移 View 时，注意同时选择 View 所依赖的对象，否则迁移可能失败。
>4. 在增量迁移的过程中：
>  - 如果源库上选定的迁移对象之中执行了支持的 DDL 操作（包括 CREATE TABLE、ALTER TABLE、RENAME TABLE、TRUNCATE TABLE、DROP TABLE、CREATE VIEW、DROP VIEW、CREATE INDEX、DROP INDEX），则对应的结构变化及其中的数据变化也同样会在目标库中执行。
>  - 如果源库上执行了 DTS 不支持的 DDL 操作，可能导致数据迁移失败。
>
>
![](https://main.qcloudimg.com/raw/db61f5bb7acd4b6d5b48224bb2a96600.png)


### 4. 校验任务
校验任务页面将会显示 DTS 对迁移任务的预检查结果。
- 如果校验通过，单击【启动任务】。
![](https://main.qcloudimg.com/raw/d5f491b52a3daa6dabec548d33ed877c.png)
- 如果校验失败，请根据出错的校验项，单击【查看详情】，并根据提示采取对应调整，然后重试校验。
>?在查询校验结果部分，可能出现“源实例权限检查”不通过的情况（如下图），失败原因及解决办法请参考上文 [帐号权限预检查](#zhqxyjc)。
>
![](https://main.qcloudimg.com/raw/f5efed3e8a80bcb157a2046a033e27ce.png)


### 5. 启动迁移
1）校验通过后，在校验任务页面单击【启动任务】立即开始迁移数据。
>!如果您设定了迁移任务的定时时间，则迁移任务会在设定的时间开始排队并执行，如果没有设置定时任务，则迁移任务会立即执行。
>
2）迁移启动后，返回迁移任务列表，可查看对应的迁移进度信息。鼠标指向下图提示符时，可显示迁移当前所处阶段及其开始时间。
![](https://main.qcloudimg.com/raw/42e549743d4abbf488c142214364e8ed.png)
3）（可选）撤销迁移，在迁移过程中，如果您需要终止迁移任务，可以在 DTS 任务的“操作”列，选择【更多】>【撤销】。
>!撤销迁移任务，并不会回滚 DTS 已经执行的操作，也不会对目标实例已有的数据进行清理。
>
![](https://main.qcloudimg.com/raw/3825a864aa5323aae1c2acace222b56c.png)

### 6. 完成迁移
- **全量迁移**：DTS 会在数据迁移完成后，自动完成迁移任务。
![](https://main.qcloudimg.com/raw/db222f268d0a8fcb0a83fcd5095526e7.png)
- **全量+增量迁移**：当迁移任务进入增量迁移的阶段后，您可通过观察 DTS 任务详情中的“目标与源库数据差距”和“
目标与源库时间延迟”，来了解当前增量数据在目标库上的写入情况。
![](https://main.qcloudimg.com/raw/910362f18b51708a66dccc18148e382c.png)
结合源数据库与目标库之间的数据差距情况，当您认为增量数据已经完成同步时，您可以在 DTS 任务的“操作”列，选择【更多】>【完成】，在弹出对话框单击【确定】，完成迁移任务。
![](https://main.qcloudimg.com/raw/544a905d29c6efba4259582a122ef7e1.png)
