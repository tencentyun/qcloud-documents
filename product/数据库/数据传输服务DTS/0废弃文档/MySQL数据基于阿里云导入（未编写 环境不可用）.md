数据传输服务 DTS 支持数据迁移功能，提供自建 MySQL 数据库到云数据库 TencentDB 的连续数据复制，用户可在不停服的情况下对数据进行在线热迁移，支持具有公网 IP/Port 或专线接入腾讯云的本地 IDC 或腾讯云云服务器 CVM 上 MySQL 数据库迁移。**MySQL5.7 暂不支持数据传输服务，可通过下载冷备文件自行导入。**

>该功能预计逐步在成都，北京，广州，深圳，上海，美西，北美，新加坡等地灰度开放

## 准备
### 注意事项
- DTS 数据迁移任务分为冷备数据导出和增量数据同步两步，其中，**冷备数据导出以及迁移后的数据对比过程会对源库负载产生一定的影响**，建议在业务低峰期或在备库上做数据库迁移。
- **仅部分库表迁移任务在增量同步开始阶段和迁移任务完成时，会重启目标 TencentDB 实例，源数据库不受影响。**
- **需要具有源实例的 super 权限**
### 源实例 super 权限
建议用户用于迁移的账号具有源实例 super 权限，需要 super 权限的场景主要有以下几种：
-  数据迁移完成前，DTS 会进行数据一致性检查，需要 super 权限修改 session 参数、binlog_format。
-  **若在 binlog 同步过程中，用户在源实例创建了 Event，且这个 Event 指定了非用于 DTS 数据迁移的账号做 DEFINER，此时不具备 super 权限将会报错。**

### 支持迁移的数据库
- 支持基础网络、VPC 网络的 CVM 自建 MySQL 数据库迁移至 TencentDB 实例。
- 支持具有公网 IP/Port 的 MySQL 数据库迁移至 TencentDB 实例。
- 支持 VPN 接入、专线接入腾讯云的 MySQL 数据库迁移至 TencentDB 实例。

### 预先检查以下几项
1. 检查目标 TencentDB 实例是否有同名库表，避免冲突；
2. 检查数据库版本，可支持 MySQL 5.1/5.5/5.6 版本迁移上云；由于目前腾讯云 TencentDB 已不再支持 MySQL 5.1 版本，因此我们推荐您在迁移前完成 MySQL 5.1 升级到 MySQL 5.5，然后再迁移至 TencentDB for MySQL 5.5。当然您也可以选择使用 DTS 数据迁移工具直接从本地 MySQL 5.1 迁移至腾讯云 TencentDB for MySQL 5.5。
3. 检查目标 TencentDB 实例容量必须大于源实例；
4. 在源 MySQL 数据库上创建迁移账号（若有已授权可用于数据迁移的账号，也可不创建）；
		
			GRANT ALL PRIVILEGES ON *.* TO "迁移账号"@"%" IDENTIFIED BY "迁移密码";

			FLUSH PRIVILEGES;	
  
5. 确认源库 MySQL 变量
	  通过 `SHOW GLOBAL VARIABLES LIKE 'XXX'`; 
	  
	  查看 MySQL 全局变量，确认当前状态是否可以进行迁移：
		
            server_id > 1
            
            log_bin = ON;
            
            binlog_format = ROW/MIXED
            
            binlog_row_image = FULL
            
            innodb_stats_on_metadata = 0
            
            wait_timeout 建议大于或等于3600秒，务必小于7200秒
            
            interactive_timeout 与wait_timeout设置相同时长
            
            如果源实例为slave角色，需要在源实例中确认以下参数：
            
            log_slave_updates = 1           
		
6. 修改变量值：

	a.  修改源库 MySQL 配置文件`my.cnf`，需重启：
	
		        log-bin=[自定义binlog文件名]
		        
	b.  动态修改配置：
         
                set global server_id = 99;
                
                set global binlog_format=ROW;
               
                set global binlog_row_image=FULL;
                
                set global innodb_stats_on_metadata = 0;
		

## 操作步骤

### 新建 DTS 数据迁移服务
登录控制台，进入数据迁移页面，单击【新建任务】
![](https://mc.qcloudimg.com/static/img/2ad6200dc53556f2c03f45e7a1af8320/image.png)


###  修改配置
跳转页面后，填写任务设置、源库设置和目标库设置。信息详情：
![](https://mc.qcloudimg.com/static/img/513a6893e79862359ee52fd6d2d97c5b/image.png)

#### 任务设置
	
* 任务名称： 为任务指定名称
* 定时执行：可为您的迁移任务指定开始时间
![](https://mc.qcloudimg.com/static/img/6d45bf22f31923704b6055f3f94f1781/image.png)

##### 源库信息
* 源库类型：目前支持有公网 IP 的 MySQL，云主机上的自建 MySQL，专线接入腾讯云的 MySQL，VPN 接入的 MySQL 四种源库类型
###### 有公网 IP 的 MySQL：能够通过公网 IP 访问的 MySQL 数据库。
所需信息：
* MySQL 主机地址
* MySQL 端口
* MySQL 账号
* MySQL 密码
		
![](https://mc.qcloudimg.com/static/img/d7ea867e99cf6dcaeea777f1f8a498e2/image.png)
		
###### 云主机上的自建 MySQL：支持基础网络和私有网络两种环境下基于云主机 CVM 的自建 MySQL 数据库。使用时需要指定云主机 CVM 的实例 ID 和所处的网络环境。
所需信息：
* 所属地域：目前仅支持同地域内的 CVM 自建 MySQL 迁移 TencentDB。若 CVM 与 TencentDB 分处于不同地域，使用 CVM 公网网络，选择【有公网 IP 的 MySQL】项实现迁移。
* CVM 网络：支持基础网络和私有网络
* 私有网络：如选择私有网络，需选择所属的私有网络及子网。
* 云主机实例 ID
* MySQL 端口
* MySQL 账号
* MySQL 密码
			
![](https://mc.qcloudimg.com/static/img/1f7d1837b9c18ae22835460215c48daf/image.png)
	
###### 专线接入的 MySQL：本地 IDC 自建 MySQL 使用 [专线接入 DC][1] 服务与腾讯云相连接后，可使用 DTS 数据迁移至腾讯云。所需信息：
* 专线网关：接入腾讯云的数据库服务器所使用的专线网关。[了解专线网关][2]
* 私有网络：专线网关所属的私有网络
* MySQL 主机地址：IDC 内的 MySQL 主机地址，DTS 数据迁移将通过专线网关映射 IP 后访问
* MySQL 端口
* MySQL 账号
* MySQL 密码
	
![](https://mc.qcloudimg.com/static/img/4d6317bb20e5551f9a5ff58218ae9c18/image.png)
		
###### VPN 接入的 MySQL：本地 IDC 自建 MySQL 通过 [腾讯云VPN连接服务][3] 或云主机上自建 VPN 服务接入与腾讯云相连接后，可使用 DTS 数据迁移至腾讯云。
所需信息：
* 所属地域：目前仅支持同地域内的 VPN 服务。
* VPN 类型：[云VPN服务][3] 或云主机上自建 VPN。
* VPN 网关：仅 [云VPN服务][3] 需要补充 VPN 网关信息。[了解VPN][4]
* 私有网络：VPN 服务所属的私有网络。
* MySQL 主机地址：IDC 内的 MySQL 主机地址，DTS 数据迁移将通过专线网关映射 IP 后访问
* MySQL 端口
* MySQL 账号
* MySQL 密码
		
![](https://mc.qcloudimg.com/static/img/dd72353254680fb09b2d004c50d33c01/image.png)

### 选择所要迁移的数据库
 选择要迁移的数据库(可选择全部迁移或部分库表迁移)，创建并检查迁移任务信息。

>**注意：**
>1. 仅在整实例迁移时会迁移 character_set_server、lower_case_table_names 配置项
>2. 若源实例所迁移的库表字符集设置和目标实例字符集设置不一致，则迁移会保留源实例的字符集设置。
		
![](https://mc.qcloudimg.com/static/img/4c944c5a4b9871eb971c22a4344933a5/image.png)

**数据迁移**：将选中数据库中的数据导出，然后在 TencentDB for MySQL 中导入。
**增量同步**：在进行数据导出导入后，设置 TencentDB for MySQL 为源库的备库，进行主备增量同步。
**覆盖 root 账号**：因 root 账号将用于云数据库安全效验，若源库 root 账号不存在，会对后续使用 TencentDB 造成不便。因此在整实例迁移时，需指定是否使用源库 root 账号覆盖目标库 root 账号。如需使用源库 root 账号或目标库未设置 root，则选【是】，如需保留目标库的 root 账号，则选【否】。

### 数据一致性检测
选择数据检测类型(可选择全部检测或部分检测或不检测) 
![](https://mc.qcloudimg.com/static/img/6c49e44bbc5c289f218892290ea396e7/image.png)

>**注意：**
>选择部分检测选项时，需填写检测比例

### 校验迁移任务信息
 在创建完迁移任务后，您需要对迁移任务信息进行校验，单击【下一步：校验任务】进行校验，只有所有校验项通过后才能启动迁移任务，单击【启动】即可。
![](https://mc.qcloudimg.com/static/img/f71f17469f53e1d7a32d4c836ce7ef4d/image.png)
任务校验存在 3 种状态：

 - 通过：表示校验完全通过
 - 警告：表示校验不通过，迁移过程中或迁移后可能影响数据库正常运行但不影响迁移任务的执行。
 - 失败：表示校验不通过，无法进行迁移。如果校验失败，请根据出错的校验项，检查并修改迁移任务信息，然后重试校验。失败原因请参考：“校验失败说明”。
 
### 启动迁移
在校验通过后，您可以单击【启动迁移】立即开始迁移数据。需要注意的是，如果您设定了迁移任务的定时时间，则迁移任务会在设定的时间开始排队并执行，如果没有设置定时任务，则迁移任务会立即执行。
迁移启动后，您可以在迁移任务下看到对应的迁移进度信息。在鼠标指向步骤后的感叹号提示符时，可显示迁移所需流程和当前所处阶段。
 
> **注意：**
> 由于系统设计限制，一次性提交或排队多个迁移任务将按排队时间串行执行。

### 增量同步
在创建迁移任务时默认必选增量同步选项，在数据迁移完成后，会将目标 TencentDB for MySQL 库设置成源数据库的备库，通过主备同步来把迁移过程中源库的新增的数据同步到目标 TencentDB for MySQL 库中。此时，源库上的修改都会同步到目标 TencentDB for MySQL 中。
在迁移完成后，你可以单击【停止】键，源库和目标库同步关系会断开，再将业务切换到目标 TencentDB for MySQL 实例上则可完成迁移。
> **注意：**
> 在断开同步前，不要往目标数据库实例写入数据，否则可能引起源库和目标库数据不一致而数据比对失败，从而导致迁移失败。


### 停止迁移
在迁移过程中，如果您需要停止迁移，可以单击【停止】按钮。
![](https://mc.qcloudimg.com/static/img/2c7a3c1534676cf9753010e986681938/image.png)


>**注意：**
1. 再次启动可能导致校验失败或任务失败，您可能需要手动清空目标库内的可能产生冲突的数据库或表，才能再次启动迁移任务。
2. 迁移单独的表时，需保证所有表外键依赖的表必须被迁移。

### 完成迁移
当迁移进度达到 100% 时，可单击右侧【完成】按钮，完成迁移任务。
![](https://mc.qcloudimg.com/static/img/1fff643dd6dd18a8c678e7ae1462d317/image.png)

>**注意：**
> 当迁移处于【未结束】状态时，迁移任务将一直进行，数据库数据同步。




[1]:	https://cloud.tencent.com/product/dc
[2]:	https://cloud.tencent.com/document/product/216/549
[3]:	https://cloud.tencent.com/product/vpn
[3]:	https://cloud.tencent.com/product/vpn
[4]:	https://cloud.tencent.com/document/product/215/4956

[img-creat0]: //mc.qcloudimg.com/static/img/d782322e94fc253a41f95e642f794b32/create0.png
[img-creat1]: //mc.qcloudimg.com/static/img/123cd23d3449cd5497502d8572f4b0a0/creat1.png
[img-creat2]: //mc.qcloudimg.com/static/img/8b75f2ad6610107c0856ea5e335c5923/create3.png
[img-init1]:  //mc.qcloudimg.com/static/img/cb72f72cf07d6b72c516d17d8ae8a114/init1.png
[img-init2]:  //mc.qcloudimg.com/static/img/3085341d195ecd9c0b5e130d86634e5e/init2.png
[img-init3]:  //mc.qcloudimg.com/static/img/5662f6a28286a2bb7ec3d1506206b5c7/init3.png
[img-init4]:  //mc.qcloudimg.com/static/img/2973c030e020d1a6e18ea882c062c741/init4.png
[img-init5]:  //mc.qcloudimg.com/static/img/f4f7f8156acd6899bcc534aa3913fa18/init5.png
[img-init6]:  //mc.qcloudimg.com/static/img/2402e535c9e893ba899ccf756e0c204c/init6.png
[img-init7]:  //mc.qcloudimg.com/static/img/d745dd9b585ca0a62cc30cabb1f31a3c/init7.png
[img-init8]:  //mc.qcloudimg.com/static/img/21effe29a213a3d3315ee776b8eed362/init8.png