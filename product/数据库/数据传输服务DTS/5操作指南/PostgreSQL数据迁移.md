数据传输服务 DTS 支持数据迁移功能，提供自建 PostgreSQL 数据库到云数据库TencentDB的连续数据复制，用户可在不停服的情况下对数据进行在线热迁移，支持具有公网 IP/Port 或专线接入腾讯云的本地 IDC 或腾讯云云服务器 CVM 上 PostgreSQL 数据库迁移。

>注意：
>数据迁移目前只支持 PostgreSQL 数据库的版本是9.3.x,9.5.x，同时9.3.x 不支持增量同步，9.5.x 需要通过在线 [同步插件][1] 才能支持，具体配置操作详见 [同步插件配置](#.E5.90.8C.E6.AD.A5.E6.8F.92.E4.BB.B6.E9.85.8D.E7.BD.AE)。

## 操作步骤

### 新建DTS数据迁移服务
登录控制台，进入数据迁移页面，单击【新建任务】
![](https://mc.qcloudimg.com/static/img/2ad6200dc53556f2c03f45e7a1af8320/image.png)
### 填写配置
跳转页面后，填写任务设置、源库设置和目标库设置。信息详情：
![](https://main.qcloudimg.com/raw/19a5f00919d635d96aef413d7a63201f.png)
#### 任务设置
* 任务名称： 为任务指定名称
* 定时执行：可为您的迁移任务指定开始时间
![](https://mc.qcloudimg.com/static/img/6d45bf22f31923704b6055f3f94f1781/image.png)
##### 源库信息
* 源库类型：目前支持有公网 IP 的 PostgreSQL，云服务器上的自建 PostgreSQL，专线接入腾讯云的 PostgreSQL，VPN 接入的 PostgreSQL 四种源库类型
###### 有公网 IP 的 PostgreSQL：能够通过公网 IP 访问的 PostgreSQL 数据库。
所需信息：
* PostgreSQL 主机地址
* PostgreSQL 端口
* PostgreSQL 账号
* PostgreSQL 密码
![](https://main.qcloudimg.com/raw/b9135f84c4d8d92d947ebd093cd353f6.png)
###### 云服务器上的自建 PostgreSQL：支持基础网络和私有网络两种环境下基于云服务器 CVM 的自建 PostgreSQL 数据库。使用时需要指定云服务器 CVM 的实例 ID 和所处的网络环境。
所需信息：
* 所属地域：目前仅支持同地域内的 CVM 自建 PostgreSQL 迁移 TencentDB。若 CVM 与 TencentDB 分处于不同地域，使用 CVM 公网网络，选择【有公网 IP 的 PostgreSQL】项实现迁移。
* CVM 网络：支持基础网络和私有网络
* 私有网络：如选择私有网络，需选择所属的私有网络及子网。
* 云服务器实例 ID
* PostgreSQL 端口
* PostgreSQL 账号
* PostgreSQL 密码
![](https://main.qcloudimg.com/raw/cd7763bdc84eda652493d8ddd6e53f38.png)

###### 专线接入的 PostgreSQL：本地 IDC 自建 PostgreSQL 使用 [专线接入DC][2] 服务与腾讯云相连接后，可使用DTS数据迁移至腾讯云。所需信息：
* 专线网关：接入腾讯云的数据库服务器所使用的专线网关。[了解专线网关][3]
* 私有网络：专线网关所属的私有网络
* PostgreSQL主机地址：IDC 内的 PostgreSQL 主机地址，DTS 数据迁移将通过专线网关映射 IP 后访问
* PostgreSQL 端口
* PostgreSQL 账号
* PostgreSQL 密码
	![](https://main.qcloudimg.com/raw/2ed7d52a0c966284d74d78a662adbbe2.png)
		
###### VPN 接入的 PostgreSQL：本地 IDC 自建 PostgreSQL 通过 [腾讯云VPN连接服务][4] 或云服务器上自建 VPN 服务接入与腾讯云相连接后，可使用 DTS 数据迁移至腾讯云。
所需信息：
* 所属地域：目前仅支持同地域内的 VPN 服务。
* VPN 类型：[云VPN服务][4] 或云服务器上自建 VPN。
* VPN 网关：仅 [云VPN服务][4] 需要补充 VPN 网关信息。[了解VPN][5]
* 私有网络：VPN 服务所属的私有网络。
* PostgreSQL 主机地址：IDC 内的 PostgreSQL 主机地址，DTS 数据迁移将通过专线网关映射 IP 后访问
* PostgreSQL 端口
* PostgreSQL 账号
* PostgreSQL 密码
		
![](https://main.qcloudimg.com/raw/7599a0e9665796a1bc3d7e337606fcff.png)

### 选择所要迁移的数据库
 选择要迁移的数据库(可选择全部迁移或部分库表迁移)，创建并检查迁移任务信息。
 ![](https://main.qcloudimg.com/raw/22aeb31026feb69a5478fe04bbcb2049.png)
### 校验迁移任务信息
 在创建完迁移任务后，您需要对迁移任务信息进行校验，单击【下一步：校验任务】进行校验，只有所有校验项通过后才能启动迁移任务，单击【启动】即可。
![](https://main.qcloudimg.com/raw/5eea31c81b6fbf11ce2a800609f1cbbb.png)
任务校验存在3种状态：

 - 通过：表示校验完全通过
 - 警告：表示校验不通过，迁移过程中或迁移后可能影响数据库正常运行但不影响迁移任务的执行。
 - 失败：表示校验不通过，无法进行迁移。如果校验失败，请根据出错的校验项，检查并修改迁移任务信息，然后重试校验。

### 启动迁移
在校验通过后，您可以单击【启动】立即开始迁移数据。需要注意的是，如果您设定了迁移任务的定时时间，则迁移任务会在设定的时间开始排队并执行，如果没有设置定时任务，则迁移任务会立即执行。
迁移启动后，您可以在迁移任务下看到对应的迁移进度信息。在鼠标指向步骤后的感叹号提示符时，可显示迁移所需流程和当前所处阶段。
> **注意：**
> 由于系统设计限制，一次性提交或排队多个迁移任务将按排队时间串行执行。

### 增量同步
在创建迁移任务时默认必选增量同步选项，在数据迁移完成后，会将目标 TencentDB for PostgreSQL 库设置成源数据库的备库，通过主备同步来把迁移过程中源库的新增的数据同步到目标 TencentDB for PostgreSQL 库中。此时，源库上的修改都会同步到目标 TencentDB for PostgreSQL 中。
在迁移完成后，您必须手动单击【 完成】键，源库和目标库同步关系会断开，即可完成迁移。
> **注意：**
> 在断开同步前，不要往目标数据库实例写入数据，否则可能引起源库和目标库数据不一致而数据比对失败，从而导致迁移失败。

### 停止迁移
在迁移过程中，如果您需要停止迁移，可以单击右侧【撤销】按钮。
![](https://main.qcloudimg.com/raw/48844d9bf0f005015b89c67c67ce0e68.png)

>**注意：**
1. 再次启动可能导致校验失败或任务失败，您可能需要手动清空目标库内的可能产生冲突的数据库或表，才能再次启动迁移任务。
2. 迁移单独的表时，需保证所有表外键依赖的表必须被迁移。

### 完成迁移
![](https://main.qcloudimg.com/raw/4c6727dbdfcc9ced708406ca75ac97eb.png)

## 同步插件配置
1. 下载并拷贝 [dts_decoding][1] 到 PostgreSQL 安装路径的lib目录下
![](https://main.qcloudimg.com/raw/7958a443bc4564a95242949b2951d648.png)
2. 修改 data 目录 postgresql.conf 配置文件
```
wal_level >= logical
 可用 max_replication_slots >= 迁移的数据库数目
 可用 max_wal_senders       >= 迁移的数据库数目
 ```
![](https://main.qcloudimg.com/raw/231de9bb2bead27f73beed2a9279eeb4.png)
![](https://main.qcloudimg.com/raw/dd91f8795d5d8a06349e50b99ccb54ce.png)
3. 修改 data 目录 pg_hba.conf 配置文件
 需要配置 replication 连接 
![](https://main.qcloudimg.com/raw/9ea1ec694a672b98f168a81ee7080c6a.png)
4. 重启源实例

>注意：
>如果使用指定库表功能，表使用了 rule 或者关联了其他表，有可能会导致增量迁移插入数据不成功，原因是一些 SQL 不在迁移的支持功能中。如果发生这种问题，可以使用 schema 迁移功能或者全部实例迁移功能。














[1]:  https://main.qcloudimg.com/raw/97b6b39254c963fcafc228a9c565a2e0.zip
[2]:	https://cloud.tencent.com/product/dc
[3]:	https://cloud.tencent.com/document/product/216/549
[4]:	https://cloud.tencent.com/product/vpn
[5]:	https://cloud.tencent.com/product/vpn
[6]:	https://cloud.tencent.com/document/product/215/4956
