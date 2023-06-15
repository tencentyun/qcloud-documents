## 适用场景

迁移整体思路是通过数据库层面的数据导入与同步，实现将自建的 Apollo 集群迁移到 TSE Apollo 集群。
请参考以下步骤进行操作：


[](id:step1)
## 步骤1：TSE 创建 Apollo 实例

通过 [TSE 控制台](https://console.cloud.tencent.com/tse/apollo?rid=33) 创建 Apollo 实例，创建的环境信息需跟自建的 Apollo 一致。在数据库迁移的过程中，将会覆盖 TSE Apollo 实例原本的数据，所以建议 TSE Apollo 实例为空库，或在迁移前确保 TSE Apollo 的数据可以被覆盖。


[](id:step2)
## 步骤2：源 Apollo 数据库开启公网访问并检查配置
TSE Apollo 迁移任务支持通过公网的方式，接入源数据库类型为自建数据库、腾讯云数据库、第三方云厂商数据库等，并实施数据迁移。
在开始迁移任务前，您需要先为您的源数据开启公网访问，并将迁移任务的 IP 地址添加到源数据库的白名单中，以便迁移任务可以与需要访问的数据库连通。
同时，请根据以下提供的校验项检查您的源 Apollo 数据库配置，校验失败将会导致迁移失败。


### 操作指引
#### 1. 根据源数据库所在地域，在下方获取对应地域 迁移任务 的 IP 地址，将其加入到源数据库的白名单中。
- 自建数据库，请在防火墙设置中允许 迁移任务 IP 地址访问。
- Windows 系统：打开控制面板找到 Windows 防火墙，查看防火墙策略。
- Linux 系统：请执行 `iptables -L` 命令，查看服务器防火墙策略。
- 腾讯云数据库或者 CVM 上的自建数据库，请参考如下指导将 迁移任务的 IP 地址添加到安全组中。
	- 登录源数据库，在实例列表，单击实例 ID，进入实例管理页面。
	- 在实例管理页面，选择安全组页或者数据安全页， 添加 DTS 服务的 IP 地址到安全组中。 
![](https://qcloudimg.tencent-cloud.cn/image/document/b2d8cb88bef99de2285c35dd44a11499.png)
- 第三方云厂商数据库，请添加 迁移任务 IP 地址到相关的安全组配置中。
- **迁移任务的 IP 地址：**
<table>
<thead>
<tr>
<th>地域</th>
<th>迁移任务 IP 地址</th>
</tr>
</thead>
<tbody><tr>
<td>广州</td>
<td>111.230.198.143,118.89.34.161,123.207.84.254,139.199.74.159</td>
</tr>
<tr>
<td>上海</td>
<td>111.231.139.59,111.231.142.94,115.159.71.186,182.254.153.245</td>
</tr>
<tr>
<td>北京</td>
<td>123.207.145.84,211.159.157.165,211.159.160.104,58.87.92.66</td>
</tr>
<tr>
<td>成都</td>
<td>111.231.225.99,118.24.42.158</td>
</tr>
<tr>
<td>重庆</td>
<td>139.186.122.1/24,129.28.12.1/24,129.28.14.1/24,139.186.77.242,139.186.109.1/24, 139.186.131.1/23,94.191.102.144,94.191.98.210</td>
</tr>
<tr>
<td>杭州ec</td>
<td>111.231.139.59,111.231.142.94,115.159.71.186,182.254.153.245</td>
</tr>
<tr>
<td>南京</td>
<td>129.211.166.117,129.211.167.130</td>
</tr>
<tr>
<td>天津</td>
<td>154.8.246.150,154.8.246.48</td>
</tr>
<tr>
<td>深圳</td>
<td>118.126.124.6,118.126.124.83</td>
</tr>
<tr>
<td>中国香港</td>
<td>119.29.180.130,119.29.208.220,124.156.168.151,150.109.72.54</td>
</tr>
<tr>
<td>北京金融</td>
<td>62.234.240.36,62.234.241.241</td>
</tr>
<tr>
<td>深圳金融</td>
<td>118.89.251.206,139.199.90.75</td>
</tr>
<tr>
<td>上海金融</td>
<td>115.159.237.246,211.159.242.74</td>
</tr>
<tr>
<td>新加坡</td>
<td>119.28.103.40,119.28.104.184,119.28.116.123,150.109.11.113</td>
</tr>
<tr>
<td>雅加达</td>
<td>43.129.33.41,43.129.35.144</td>
</tr>
<tr>
<td>曼谷</td>
<td>150.109.164.203,150.109.164.82</td>
</tr>
<tr>
<td>孟买</td>
<td>119.28.246.130,119.28.246.18</td>
</tr>
<tr>
<td>首尔</td>
<td>119.28.150.71,119.28.157.173</td>
</tr>
<tr>
<td>东京</td>
<td>150.109.195.201,150.109.196.137</td>
</tr>
<tr>
<td>硅谷</td>
<td>49.51.38.216,49.51.39.189</td>
</tr>
<tr>
<td>弗吉尼亚</td>
<td>170.106.2.63,49.51.85.120</td>
</tr>
<tr>
<td>多伦多</td>
<td>45.113.70.156,45.113.70.6,49.51.10.104,49.51.9.221</td>
</tr>
<tr>
<td>法兰克福</td>
<td>49.51.132.38,49.51.133.85</td>
</tr>
</tbody></table>

#### 2. 根据以下的配置校验项，检查您的源 Apollo 数据库配置正确：
<table>
<thead>
<tr>
<th>校验项</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>innodb_stats_on_metadata</td>
<td>源数据库环境变量参数 innodb_stats_on_metadata 需要设置为 OFF。  innodb_stats_on_metadata 参数开启时，每当查询 information_schema 元数据库里的表，Innodb 就会更新 information_schema.statistics 表，导致访问时间变长。关闭后可加快对于 schema 库表的访问。 <br>MySQL 5.6.6 之前版本 innodb_stats_on_metadata 参数预设值为 ON，需要修改为 OFF。MySQL 5.6.6 及其以后的版本预设值为 OFF，不存在问题。</td>
</tr>
<tr>
<td>数据库版本</td>
<td>源数据库版本 ≤ 8.0</td>
</tr>
<tr>
<td>数据库权限</td>
<td>源数据库账号需要至少具备以下权限： RELOAD,LOCK TABLES,REPLICATION CLIENT,REPLICATION SLAVE,SHOW DATABASES,SHOW VIEW,PROCESS</td>
</tr>
<tr>
<td>实例参数检查</td>
<td>1. 源库变量 connect_timeout 必须大于10。 <br>2. 源库表的 row_format 不能为 FIXED。 <br>3. 源库表lower_case_table_names 变量必须为0。</td>
</tr>
<tr>
<td>BINLOG相关参数检查</td>
<td>1. log_bin 变量必须设置为 ON。 <br>2. binlog_format 变量必须设置为 ROW。 <br>3. binlog_row_image 必须设置为 FULL。 <br>4. server_id 参数需要手动设置，且值不能设置为0。 <br>5. 不允许设置 do_db，ignore_db。</td>
</tr>
<tr>
<td>外键依赖检查</td>
<td>外键依赖只能设置为 NO ACTION、RESTRICT。 部分库表迁移时，有外键依赖的表必须齐全。</td>
</tr>
</tbody></table>


## 步骤3：TSE Apollo 中创建迁移任务
在完成源 Apollo 集群数据库的公网访问配置后，请在 TSE Apollo 实例详情页面 - 迁移任务页面下配置并开启迁移任务。
![](https://qcloudimg.tencent-cloud.cn/raw/78aad03e8c21b4fef28d7935deb7d888.png)
- 接入类型：当前仅支持公网接入。
- 数据库类型：当前仅支持MySQL数据库。
- 主机地址：请填入源 Apollo 数据库实例公网地址。
- 端口：请填入源 Apollo 数据库实例公网端口。
- 账号：请填入源 Apollo 数据库账号。
- 密码：请填入源 Apollo 数据库密码。
- 数据库配置：请填入源 Apollo 数据库与 TSE Apollo 数据库的映射关系。
    - 源数据库：请填入源 Apollo 数据库名称。
    - 目标数据库：请选择 TSE Apollo 相应的环境。

单击**提交**后，迁移任务将开始执行。

## 步骤4：数据同步
在完成迁移任务的配置后，将开启源 Apollo 数据库的全量+增量数据迁移，在任务执行过程当中支持向源 Apollo 数据库写入新的数据，目标TSE Apollo 数据库将会实时同步新的数据。

### 注意事项
- 在执行数据迁移时，会占用一定源数据库实例资源，可能会导致源数据库实例负载上升，增加数据库自身压力。如果您的数据库配置过低，建议您在业务低峰期进行迁移。
- 默认采用无锁迁移来实现，迁移过程中对源数据库不加全局锁（FTWRL），仅对无主键的表加表锁，其他不加锁。
- 迁移任务执行时，会使用执行迁移任务的账号在源数据库中写入系统库__tencentdb__，用于记录迁移任务过程中的数据对比信息。
    - 为保证后续数据对比问题可定位，迁移任务结束后不会删除源数据库中的__tencentdb__。
    - __tencentdb__系统库占用空间非常小，约为源数据库存储空间的千分之一到万分之一（例如源数据库为50GB，则__tencentdb__系统库约为5MB-50MB） ，并且采用单线程，等待连接机制，所以对源数据库的性能几乎无影响，也不会抢占资源。

### 操作指引
![](https://qcloudimg.tencent-cloud.cn/raw/6f7b7e640f0958fe2a29c1104bc0d669.png)
- 您可以在 TSE Apollo 实例详情页 - 迁移任务页面下查看迁移任务当前运行的进度与状态：
- 当迁移任务执行至同步增量阶段后，任务将持续同步源 Apollo 数据库中的增量数据，建议您在完成 步骤五：业务应用迁移 后，终止迁移任务。
- 如果在迁移任务执行过程中出现错误，且检查您的源 Apollo 数据库配置无误，可通过 [快速提工单](https://console.cloud.tencent.com/workorder/category?level1_id=517&level2_id=727&source=14&data_title=%E5%85%B6%E4%BB%96%E8%85%BE%E8%AE%AF%E4%BA%91%E4%BA%A7%E5%93%81&step=1)，联系腾讯云助手协助。



## 步骤5：业务应用迁移

### 方式一：原地迁移（推荐）

原地迁移为在原有的服务上，通过逐步修改服务实例的 Apollo 地址来完成整体的迁移。整个过程如下所示：

#### 1. 服务全部实例指向自建 Apollo

![](https://qcloudimg.tencent-cloud.cn/raw/e2cdc982dc78a9a947596538dcfe0f40.png)

#### 2. 迁移部分实例到 TSE Apollo

![](https://qcloudimg.tencent-cloud.cn/raw/c3428948638f1bf3480c6859873f576c.png)

1） 迁移前，人工校验服务的配置内容两边是否一致
2）修改业务应用配置的 Apollo 服务地址，灰度部分服务实例指向 TSE Apollo 集群的服务地址
3）灰度一段时间之后，再迁移剩余的服务实例

如果迁移过程中业务出现问题，则及时回滚配置，连回自建 Apollo。

#### 3. 迁移全部实例到 TSE Apollo

![](https://qcloudimg.tencent-cloud.cn/raw/d0f1b58b9af8091f676ec13069d318ca.png)

迁移过程中，如果有配置变更则需要同时修改自建 Apollo 和 TSE Apollo 的配置。

#### 4. 下线自建 Apollo

![](https://qcloudimg.tencent-cloud.cn/raw/71ecb2d9048a42b7a64ee06434972441.png)

可以通过以下两种方式确认自建 Apollo 集群是否还有客户端使用：

1)  查看 ConfigService 机器 8080 端口的连接数是否为0，如果为0表示没有客户端连接
2)  查看 ConfigDB 的 Instance 表，确认近期没有客户端拉取配置

如果以上两点都确认完成之后，建议的下线自建 Apollo 集群的流程：

1) Kill ConfigService 的进程，不 Kill AdminService 和 Portal 的进程。ConfigService 用于对客户端提供服务，Kill ConfigService 就可认为切断整个 Apollo 服务。只 Kill ConfigService 进程为了下线过程中如果有残留客户端，则可以快速拉起 ConfigService 恢复，减少影响面。
2) 当第一步灰度一段时间之后（1周到1个月），再回收其它服务的资源。

### 方式二：先扩容再缩容

先扩再缩的方式，总的来说先部署一组新的服务并指向 TSE Apollo，通过流量切换的方式把流量从老的服务实例迁移到新的服务实例。最后再缩容掉老的服务实例。

#### 1. 部署一组新的服务实例，流量指向老的服务实例

![](https://qcloudimg.tencent-cloud.cn/raw/109f610bc5ca2efd9e7d0ac8e937895a.png)

#### 2. 流量切换到新的服务实例

![](https://qcloudimg.tencent-cloud.cn/raw/aad436337cae323a474425d2bf685ebe.png)

如果流量切换之后发现业务异常，则切回老的服务实例。

#### 3. 缩容老的服务实例

![](https://qcloudimg.tencent-cloud.cn/raw/6ef6de4684f3cf8459b13bf4af97dd23.png)

当阶段二运行一段时间之后，下线老的服务实例。方式二由于依赖流量切换能力、镜像部署一套服务占用额外的资源等劣势，所以建议优先使用方式一迁移。
