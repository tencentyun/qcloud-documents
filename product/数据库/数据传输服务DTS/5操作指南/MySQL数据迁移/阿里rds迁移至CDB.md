## 操作场景
本文将指导您使用腾讯云提供的数据迁移产品 DTS 将阿里云数据库（RDS）的数据迁移到腾讯云云数据库中。

## 环境要求
- 阿里云云数据库 MySQL 5.6 或更低版本。
- 腾讯云云数据库 MySQL 5.6 实例。
>!数据传输过程中，腾讯云数据库的数据复制方式必须为异步复制，如需修改数据复制方式，在数据传输完成后升级即可。

## 操作步骤

### 1. 获取源数据库基本信息和 AccessKey 
1.1 登录 [RDS 管理控制台](https://account.aliyun.com/login/login.htm?oauth_callback=https%3A%2F%2Frdsnew.console.aliyun.com%2F%3Fspm%3Da2c4g.11186623.2.5.cdjgiR)，选择目标实例。
1.2 在目标实例的基础信息页即可获取我们所需的信息，具体如图所示：
![](https://main.qcloudimg.com/raw/e55af45a5c36a99097418808cc542389.png)
>!阿里云提供的外网地址需要将其转化成 IP 格式。此处列举一个 [IP/服务器地址查询 ](http://ip.chinaz.com) 的网址。
>
1.3 将鼠标悬停于右上方头像处，在出现的下拉菜单中选择【accesskeys】，进入页面后即可获取所需的 Accesskey。
![](https://main.qcloudimg.com/raw/2d67bd05558d5762c322d0c33d344332.png)
	
### 2. 创建腾讯云云数据库的 DTS 任务
登录 [DTS 控制台](https://console.cloud.tencent.com/dtsnew/migrate/page)，进入数据迁移页面，单击【新建任务】，跳转页面后，填写任务设置、源库设置和目标库设置。


#### 2.1 任务设置
- 任务名称：为任务指定名称。
- 定时执行：可为您的迁移任务指定开始时间。
![](https://mc.qcloudimg.com/static/img/6d45bf22f31923704b6055f3f94f1781/image.png)

#### 2.2 源库信息
根据需要选择接入类型，依次填写对应的源库连接信息。
>!您需要在阿里云开通 TencentDB 对外映射出去的 IP 的白名单。否则在测试连通性时将不通过。例如，
>- 有公网 IP 的 MySQL 腾讯云的映射，您需要将相对应的地区外网 IP 添加到阿里云的白名单中。
>-  DTS 配置时源库类型为“专线”或者“VPN”会在任务生成后出现对外映射的 IP，需将此 IP 添加到阿里云白名单中。
>
![](https://main.qcloudimg.com/raw/b099d7a519f80fcdb450e8476a17d314.png)

#### 2.3 目标库信息
目标实例类型选择 TencentDB 实例，填写对应的目标库链接信息。
![](https://main.qcloudimg.com/raw/28b1998fd0b7e512be01c281490703bb.png)

#### 2.4 选择所要迁移的数据库
选择要迁移的数据库,创建并检查迁移任务信息。
![](https://main.qcloudimg.com/raw/ed8274a0b47d81ecf1466adea1fac10c.png)
#### 2.5 数据一致性检测
选择数据检测类型（可选择全部检测或不检测）。
>!选择部分检测选项时，需填写检测比例。
>
![](https://main.qcloudimg.com/raw/efa134922b1097f832f0c1e41fafaef3.png)

#### 2.6 校验迁移任务信息
创建完迁移任务后，您需要对迁移任务信息进行校验，单击【下一步：校验任务】进行校验，只有所有校验项通过后才能启动迁移任务，单击【启动】即可。
 任务校验存在3种状态：
 - 通过：表示校验完全通过。
 - 警告：表示校验不通过，迁移过程中或迁移后可能影响数据库正常运行但不影响迁移任务的执行。
 - 失败：表示校验不通过，无法进行迁移。如果校验失败，请根据出错的校验项，检查并修改迁移任务信息，然后重试校验。
![](https://main.qcloudimg.com/raw/f0d5e8a304edd34bebe4d21d9ff4746d.png)

### 3. 启动迁移
>!由于系统设计限制，一次性提交或排队多个迁移任务将按排队时间串行执行。
>
在校验通过后，您可以单击【启动迁移】立即开始迁移数据。需要注意的是，如果您设定了迁移任务的定时时间，则迁移任务会在设定的时间开始排队并执行，如果没有设置定时任务，则迁移任务会立即执行。
迁移启动后，您可以在迁移任务下看到对应的迁移进度信息。在鼠标指向步骤后的感叹号提示符时，可显示迁移所需流程和当前所处阶段。
>?出现错误："errMsg": "发起备份任务失败SDK.ServerUnreachable Unable to connect server:HTTP Error 403: Forbidden"
>可以从以下方面进行排查：
>- 检查阿里云的密钥是否有对源 RDS 实例发起冷备的权限。若使用阿里云主帐号，即拥有所有权限，可排除该原因。
>- 登录阿里云控制台，检查该 RDS 实例是否已经存在冷备或者升级等互斥任务，若设置了自动备份，则需要关闭自动备份选项。
>- 如经过以上两步，问题仍然存在，请向阿里云咨询使用 [云 API](https://help.aliyun.com/document_detail/26272.html?spm=a2c4g.11186623.6.916.voEDSM) 发起冷备任务失败的原因。  

### 4. 撤销迁移
在迁移过程中，如果您需要撤销迁移，可以单击【撤销】。
![](https://main.qcloudimg.com/raw/d57e495a06627c9d10274c3e3ea9beba.png)

### 5. 迁移任务割接
- 保证业务侧对阿里云 RDS 不再进行写入，可通过更改业务连接的账号密码或调整授权，但需确保用于 DTS 同步的账号可正常读写。
- 断开阿里云 RDS 的业务连接，通过`show processlist`命令验证没有业务连接。
- 通过`show master status`获取阿里云 RDS 最新 gtid，然后与 TencentDB 同步的 gtid（通过`show slave status`获取）进行对比，保证 TencentDB 与阿里云 RDS 同步没有延迟。
-  验证原阿里云 RDS 账号是否可以登录 TencentDB，如无法登录可尝试把原阿里云 RDS 账号权限提至最高权限。具体操作为：
   保持 DTS 任务继续同步，在阿里云 RDS 上添加高权限账号（可改变账号密码的加密方式为通用加密方式），然后通过 DTS 同步到 TencentDB。
- 用户通过 DTS 控制台（见下图）或自行抽取核心表内容检查数据一致性。
![](https://main.qcloudimg.com/raw/bb535aba27effc701d14544b3a5ba09a.png)
- 通过`show slave status`记录 TencentDB 的同步位点。


### 6. 完成迁移
当迁移进度达到100%时，可单击右侧【完成】，完成迁移任务，或调用 DTS 云 [API](https://cloud.tencent.com/document/product/571/18122) 断开同步，完成迁移任务。。
![](https://main.qcloudimg.com/raw/30dbf7018d72cee1daef076323dd5377.png)
>!当迁移处于【未结束】状态时，迁移任务将一直进行，数据库数据同步。

### 7. 重启业务
关闭 TencentDB 的只读功能，启动应用程序，并持续观察 TencentDB 状态，确保应用可正常运行。 


