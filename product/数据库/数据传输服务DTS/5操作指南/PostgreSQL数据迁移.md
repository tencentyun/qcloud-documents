## 操作场景
数据传输服务 DTS 支持数据迁移功能，提供自建 PostgreSQL 数据库到 TencentDB 的连续数据复制，用户可在不停服的情况下对数据进行在线热迁移，支持具有公网 IP/Port 或专线接入腾讯云的本地 IDC 或腾讯云 CVM 上 PostgreSQL 数据库迁移。

>!数据迁移目前只支持 PostgreSQL 数据库的版本是9.3.x、9.5.x，同时9.3.x不支持增量同步，9.5.x需要通过在线 [同步插件](https://main.qcloudimg.com/raw/97b6b39254c963fcafc228a9c565a2e0.zip) 才能支持，具体配置操作详见 [同步插件配置](#.E5.90.8C.E6.AD.A5.E6.8F.92.E4.BB.B6.E9.85.8D.E7.BD.AE)。

## 操作步骤

### 新建 DTS 数据迁移任务
登录 [DTS 控制台](https://console.cloud.tencent.com/dtsnew/migrate/page)，进入数据迁移页，单击【新建任务】。


### 设置源和目标数据库
跳转页面后，填写任务设置、源库设置和目标库设置。
#### 任务设置
* 任务名称：为任务指定名称。
* 定时执行：为迁移任务指定开始时间。

#### 源库设置和目标库设置
源库类型：目前支持有公网 IP 的 PostgreSQL、云服务器上的自建 PostgreSQL、专线接入腾讯云的 PostgreSQL、VPN 接入的 PostgreSQL、云数据库 PostgreSQL 五种源库类型。

| 源库类型 | 说明 | 
|---------|---------|
| 有公网 IP 的 PostgreSQL |  能够通过公网 IP 访问的 PostgreSQL 数据库。所需信息：<br><li>PostgreSQL 主机地址<li>PostgreSQL 端口<li>PostgreSQL 账号<li>PostgreSQL 密码 | 
| 云服务器上的自建 PostgreSQL |  支持基础网络和私有网络两种环境下基于云服务器 CVM 的自建 PostgreSQL 数据库。使用时需要指定云服务器 CVM 的实例 ID 和所处的网络环境。所需信息：<br><li>所属地域：目前仅支持同地域内的 CVM 自建 PostgreSQL 迁移 TencentDB。若 CVM 与 TencentDB 分处于不同地域，使用 CVM 公网网络，选择【有公网 IP 的 PostgreSQL】项实现迁移<li>CVM 网络：支持基础网络和私有网络<li>私有网络：如选择私有网络，需选择所属的私有网络及子网<li>云服务器实例 ID<li>PostgreSQL 端口<li>PostgreSQL 账号<li>PostgreSQL 密码 | 
| 专线接入的 PostgreSQL |  本地 IDC 自建 PostgreSQL 使用 [专线接入DC](https://cloud.tencent.com/product/dc) 服务与腾讯云相连接后，可使用 DTS 数据迁移至腾讯云。所需信息：<br><li> 专线网关：接入腾讯云的数据库服务器所使用的专线网关，[了解专线网关](https://cloud.tencent.com/document/product/216/19256)<li>私有网络：专线网关所属的私有网络<li> PostgreSQL主机地址：IDC 内的 PostgreSQL 主机地址，DTS 数据迁移将通过专线网关映射 IP 后访问<li>PostgreSQL 端口<li>PostgreSQL 账号<li>PostgreSQL 密码		 | 
| VPN 接入的 PostgreSQL |  本地 IDC 自建 PostgreSQL 通过 [VPN 连接服务](https://cloud.tencent.com/product/vpn) 或云服务器上自建 VPN 服务接入与腾讯云相连接后，可使用 DTS 数据迁移至腾讯云。所需信息：<br><li>所属地域：目前仅支持同地域内的 VPN 服务<li>VPN 类型：[云 VPN 服务](https://cloud.tencent.com/product/vpn) 或云服务器上自建 VPN<li>VPN 网关：仅 [云 VPN 服务](https://cloud.tencent.com/product/vpn) 需要补充 VPN 网关信息，[了解 VPN](https://cloud.tencent.com/product/vpn)<li>私有网络：VPN 服务所属的私有网络<li>PostgreSQL 主机地址：IDC 内的 PostgreSQL 主机地址，DTS 数据迁移将通过专线网关映射 IP 后访问<li>PostgreSQL 端口<li>PostgreSQL 账号<li>PostgreSQL 密码		 | 
| 云数据库 PostgreSQL |TencentDB for PostgreSQL 云数据库实例。所需信息：<br><li>PostgreSQL 实例 ID<li>PostgreSQL 账号<li>PostgreSQL 密码   | 
	
![](https://main.qcloudimg.com/raw/c57aaf34e4a594d2e22e525339e83927.png)

### 选择所要迁移的数据库
选择要迁移的数据库（可选择全部迁移或部分库表迁移）。
![](https://main.qcloudimg.com/raw/22aeb31026feb69a5478fe04bbcb2049.png)

### 校验迁移任务
单击【下一步：校验任务】，对迁移任务信息进行校验，只有所有校验项通过后才能启动迁移任务，校验完成后，单击【启动】即可。
任务校验存在3种状态：
 - 通过：表示校验完全通过。
 - 警告：表示校验不通过，迁移过程中或迁移后可能影响数据库正常运行但不影响迁移任务的执行。
 - 失败：表示校验不通过，无法进行迁移。如果校验失败，请根据出错的校验项，检查并修改迁移任务信息，然后重试校验。
![](https://main.qcloudimg.com/raw/5eea31c81b6fbf11ce2a800609f1cbbb.png)

### 启动迁移
校验通过后，返回数据迁移列表，在【操作】列，单击【立即启动】开始迁移数据。需要注意的是，如果您设定了迁移任务的定时时间，则迁移任务会在设定的时间开始排队并执行，如果没有设置定时任务，则迁移任务会立即执行。
迁移启动后，您可以在迁移任务下看到对应的迁移进度信息。在鼠标指向步骤后的感叹号提示符时，可显示迁移所需流程和当前所处阶段。

>!由于系统设计限制，一次性提交或排队多个迁移任务将按排队时间串行执行。

### 增量同步
创建迁移任务时默认必选增量同步选项，在数据迁移完成后，会将目标 TencentDB for PostgreSQL 库设置成源数据库的备库，通过主备同步来把迁移过程中源库的新增的数据同步到目标 TencentDB for PostgreSQL 库中。此时，源库上的修改都会同步到目标 TencentDB for PostgreSQL 中。
迁移完成后，您必须手动单击【完成】，源库和目标库同步关系会断开，即可完成迁移。

>!在断开同步前，不能往目标数据库实例写入数据，否则可能引起源库和目标库数据不一致而数据比对失败，从而导致迁移失败。

### 停止迁移
在迁移过程中，如果您需要停止迁移，可在迁移任务的【操作】列，单击【撤销】停止迁移。

>!
>- 再次启动可能导致校验失败或任务失败，您可能需要手动清空目标库内的可能产生冲突的数据库或表，才能再次启动迁移任务。
>- 迁移单独的表时，需保证所有表外键依赖的表必须被迁移。

### 完成迁移
![](https://main.qcloudimg.com/raw/ae86eb048301493f2eb4d687f91f9cb5.png)

## 同步插件配置
1. 下载并拷贝 [dts_decoding](https://main.qcloudimg.com/raw/97b6b39254c963fcafc228a9c565a2e0.zip) 到 PostgreSQL 安装路径的 lib 目录下。
![](https://main.qcloudimg.com/raw/1fdb249844a331ffb073cf0544ac8c3f.png)
2. 修改 data 目录 postgresql.conf 配置文件。
```
wal_level >= logical
 可用 max_replication_slots >= 迁移的数据库数目
 可用 max_wal_senders       >= 迁移的数据库数目
```
![](https://main.qcloudimg.com/raw/1a6819eff953e9d885175f0ff7cdde42.png)
![](https://main.qcloudimg.com/raw/41a8bb56280c4f6e82c9a9025e611b49.png)
3. 修改 data 目录 pg_hba.conf 配置文件。
 需要配置 replication 连接 
![](https://main.qcloudimg.com/raw/9ea1ec694a672b98f168a81ee7080c6a.png)
4. 重启源实例。
>!如果使用指定库表功能，表使用了 rule 或者关联了其他表，有可能会导致增量迁移插入数据不成功，原因是一些 SQL 不在迁移的支持功能中。如果发生这种问题，可以使用 schema 迁移功能或者全部实例迁移功能。





