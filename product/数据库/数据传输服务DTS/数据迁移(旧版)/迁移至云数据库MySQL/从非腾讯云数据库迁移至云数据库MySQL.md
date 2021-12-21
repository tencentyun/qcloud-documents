
## 操作场景
数据传输服务 DTS 支持数据迁移功能，提供自建 MySQL 数据库到云数据库 TencentDB 的连续数据复制，用户可在不停服的情况下对数据进行在线热迁移，支持具有公网 IP/Port 或专线接入腾讯云的本地 IDC 或腾讯云 CVM 上 MySQL 数据库迁移。现已支持 MySQL 5.7 数据传输服务。

## 准备事项
### 注意事项
- DTS 数据迁移任务分为冷备数据导出和增量数据同步两步，其中，冷备数据导出以及迁移后的数据对比过程会对源库负载产生一定的影响，建议在业务低峰期或在备库上做数据库迁移。
- 指定库表迁移
 如 lower_case_table_name 在迁移校验任务会检查源和目标的此项配置是否一致，不一致报错，会提前避免   lower_case_table_name 引起的重启问题。 
- 整实例迁移
 -  迁移配置，如源实例一些必须要重启的参数（如 lower_case_table_name）与目标实例不同，设置需要重启目标实例。 
 -  导入全量备份后，需要重启目标实例。
- 部分场景需要具有源实例的 super 权限。

### 源实例 super 权限
大部分场景对源实例无 super 权限要求，仅以下场景中需具有源实例的 super 权限。
- 用户在“数据一致性检测”中选择了“全量检测”校验模式。
- 若在 binlog 同步过程中，用户在源实例创建了 Event，且这个 Event 指定了非用于 DTS 数据迁移的帐号做 DEFINER，此时不具备 super 权限将会报错。

### 支持迁移的数据库
- 支持基础网络、VPC 网络的 CVM 自建 MySQL 数据库迁移至 TencentDB 实例。
- 支持具有公网 IP/Port 的 MySQL 数据库迁移至 TencentDB 实例。
- 支持 VPN 接入、专线接入腾讯云的 MySQL 数据库迁移至 TencentDB 实例。

### 预先检查项
1. 检查目标 TencentDB 实例是否有同名库表，避免冲突。
2. 检查数据库版本，可支持 MySQL 5.1/5.5/5.6/5.7 版本迁移上云；由于目前腾讯云 TencentDB 已不再支持 MySQL 5.1 版本，因此我们推荐您在迁移前完成 MySQL 5.1 升级到 MySQL 5.5，然后再迁移至 TencentDB for MySQL 5.5。当然您也可以选择使用 DTS 数据迁移工具直接从本地 MySQL 5.1 迁移至腾讯云 TencentDB for MySQL 5.5。
3. 检查目标 TencentDB 实例容量必须大于源实例。
4. 在源 MySQL 数据库上创建迁移帐号（若有已授权可用于数据迁移的帐号，也可不创建）。
```  	
        GRANT ALL PRIVILEGES ON *.* TO '迁移帐号'@'%' IDENTIFIED BY '迁移密码';
    		FLUSH PRIVILEGES;	
```
5. 确认源库 MySQL 变量。
    通过 `SHOW GLOBAL VARIABLES LIKE 'XXX'; `查看 MySQL 全局变量，确认当前状态是否可以进行迁移：
```    	
            server_id > 1      
            log_bin = ON;            
            binlog_format = ROW/MIXED           
            binlog_row_image = FULL            
            innodb_stats_on_metadata = 0            
            wait_timeout 建议大于或等于3600秒，务必小于7200秒            
            interactive_timeout 与wait_timeout设置相同时长            
            如果源实例为slave角色，需要在源实例中确认以下参数：           
            log_slave_updates = 1           
```
6. 修改变量值。
    a.  对于自建 MySQL 数据库，修改源库 MySQL 配置文件`my.cnf`，需重启：
```
  	        log-bin=[自定义binlog文件名]
```
  b.  动态修改配置：
```
             set global server_id = 99;                
             set global binlog_format=ROW;              
             set global binlog_row_image=FULL;                
             set global innodb_stats_on_metadata = 0;
```


## 操作步骤
### 1. 新建迁移任务
登录 [DTS 控制台](https://console.cloud.tencent.com/dts/migration)，进入数据迁移页面，单击【新建迁移任务】。

###  2. 设置源和目标数据库
设置任务、源库和目标库，网络连通性测试成功后，单击【新建】。

#### a. 任务设置
- 任务名称：为任务指定名称。
- 定时执行：可为您的迁移任务指定开始时间。
- 标签：用于从不同维度对资源分类管理。

#### b. 源库设置
源库类型：支持有公网 IP 的 MySQL、云服务器上的自建 MySQL、专线接入腾讯云的 MySQL、VPN 接入等 MySQL 源库类型。

> ?
>
> 源数据库的账号长度不能超过16位。如果账号超过16位需要用户重新创建一个符合要求的账号。

| 源库类型 | 说明 |
|---------|---------|
| 有公网 IP 的 MySQL | 能够通过公网 IP 访问的 MySQL 数据库，所需信息：<li> MySQL 主机地址<li> MySQL 端口<li> MySQL 帐号<li> MySQL 密码	 |
| 云服务器上的自建 MySQL | 支持基础网络和私有网络两种环境下基于 CVM 的自建 MySQL 数据库，使用时需要指定 CVM 的实例 ID，所需信息：<li>所属地域：CVM 自建 MySQL，均可通过腾讯云内网迁移到云数据库 MySQL<li>云服务器实例 ID<li>MySQL 端口<li> MySQL 帐号<li>MySQL 密码			 |
| 专线接入腾讯云的 MySQL | 本地 IDC 自建 MySQL 使用 [专线接入 DC](https://cloud.tencent.com/product/dc) 服务与腾讯云相连接后，可使用DTS数据迁移至腾讯云。所需信息：<li>专线网关：接入腾讯云的数据库服务器所使用的专线网关，了解 [专线网关](https://cloud.tencent.com/document/product/216/19256)<li>私有网络：专线网关所属的私有网络<li>MySQL 主机地址：IDC 内的 MySQL 主机地址，DTS 数据迁移将通过专线网关映射 IP 后访问<li> MySQL 端口<li> MySQL 帐号<li> MySQL 密码 |
| VPN 接入的 MySQL | 本地 IDC 自建 MySQL 通过 [腾讯云 VPN 连接服务](https://cloud.tencent.com/product/vpn) 或云服务器上自建 VPN 服务接入与腾讯云相连接后，可使用 DTS 数据迁移至腾讯云。所需信息：<li>所属地域：目前仅支持同地域内的 VPN 服务<li>VPN 类型：云 VPN 服务或云服务器上自建 VPN <li>VPN 网关：仅云 VPN 服务需要补充 VPN 网关信息，了解 [VPN](https://cloud.tencent.com/document/product/215/20084)<li> 私有网络：VPN 服务所属的私有网络 <li> MySQL 主机地址：IDC 内的 MySQL 主机地址，DTS 数据迁移将通过专线网关映射 IP 后访问<li> MySQL 端口<li> MySQL 帐号<li> MySQL 密码	 |

#### c. 目标库设置
选择目标数据库实例，并输入目标库上的帐号及密码。

### 3. 设置迁移选项及选择迁移对象
选择要迁移的数据库（可选择全部迁移或部分库表迁移），创建并检查迁移任务信息。
>!
>1. 仅在整实例迁移时会迁移 character_set_server、lower_case_table_names 配置项。
>2. 若源实例所迁移的库表字符集设置和目标实例字符集设置不一致，则迁移会保留源实例的字符集设置。

- **迁移类型**：支持结构迁移、全量迁移、全量 + 增量迁移。
- **迁移对象**：支持整个实例、指定对象。
- **使用源库 root 帐号覆盖目标库**：因 root 帐号将用于云数据库安全校验，若源库 root 帐号不存在，会对后续使用 TencentDB 造成不便。因此在整实例迁移时，需指定是否使用源库 root 帐号覆盖目标库 root 帐号。如需使用源库 root 帐号或目标库未设置 root，则选【是】，如需保留目标库的 root 帐号，则选【否】。
- **目标库只读**：选择只读后，在数据迁移过程中，从源数据库迁移的数据在目标数据库只能读取（Read Only），无法更改，直至用户单击完成迁移任务。
- **数据一致性检测**：支持全量检测和不检测。
![](https://main.qcloudimg.com/raw/13107b3c5af08b20d2d05d14744d744e.png)

### 4. 校验迁移任务
 在创建完迁移任务后，您需要对迁移任务信息进行校验，单击【下一步：校验任务】进行校验，只有所有校验项通过后才能启动迁移任务，单击【启动任务】即可。
 任务校验存在 3 种状态：

 - 通过：表示校验完全通过
 - 警告：表示校验不通过，迁移过程中或迁移后可能影响数据库正常运行但不影响迁移任务的执行。
 - 失败：表示校验不通过，无法进行迁移。如果校验失败，请根据出错的校验项，检查并修改迁移任务信息，然后重试校验。失败原因可单击【查看详情】查看“校验详情”。

![](https://main.qcloudimg.com/raw/a884ae48b08083d1a60e267d01f7124b.png)

### 5. 启动迁移
校验通过后，在迁移任务列表单击【立即启动】立即开始迁移数据。需要注意的是，如果您设定了迁移任务的定时时间，则迁移任务会在设定的时间开始排队并执行，如果没有设置定时任务，则迁移任务会立即执行。
迁移启动后，您可以在迁移任务下看到对应的迁移进度信息。在鼠标指向步骤后的感叹号提示符时，可显示迁移所需流程和当前所处阶段。

>!由于系统设计限制，一次性提交或排队多个迁移任务将按排队时间串行执行。

### 6. 增量同步
在创建迁移任务时默认必选增量同步选项，在数据迁移完成后，会将目标 TencentDB for MySQL 库设置成源数据库的备库，通过主备同步来把迁移过程中源库的新增的数据同步到目标 TencentDB for MySQL 库中。此时，源库上的修改都会同步到目标 TencentDB for MySQL 中。

>!在断开同步前，不要往目标数据库实例写入数据，否则可能引起源库和目标库数据不一致而数据比对失败，从而导致迁移失败。


### 7.（可选）撤销迁移
>!
1. 如果是单击【撤销】，不会对目标实例同步的数据进行清理。
2. 再次启动可能导致校验失败或任务失败，您可能需要手动清空目标库内的可能产生冲突的数据库或表，才能再次启动迁移任务。
3. 迁移单独的表时，需保证所有表外键依赖的表必须被迁移。

在迁移过程中，如果您需要撤销迁移，可以单击【撤销】。
![](https://main.qcloudimg.com/raw/1404b46bdbe53bdd83201bad3ae39af9.png)


### 8. 完成迁移
>!当迁移处于“未结束”状态时，迁移任务将一直进行，数据持续同步。

当迁移进度达到100%、目标与源库数据差距为0MB及目标与源库时间延迟为0秒时，即表示数据已经同步一致，可在单击右侧【完成】完成迁移任务。
![](https://main.qcloudimg.com/raw/886a3c922df903a812bcbb7120aa847e.png)
完成后效果如下：
![](https://main.qcloudimg.com/raw/a539d58244ae7ffcbdc367b655fd1738.png)
