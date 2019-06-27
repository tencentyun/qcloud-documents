## 操作场景
云数据库 SQL Server 支持用户通过 COS 文件来进行数据迁移，帮助您完成将阿里云或自建 SQL Server 数据库迁移至云数据库 SQL Server。
>!
>- 迁移之前需保证目的实例的 SQL Server 版本不低于源实例的版本。
>- 迁移的 bak 文件需保证每个 bak 文件只包含一个库。
>- 迁移库不能与云 SQL Server 库有库名重复的情况。

## 操作步骤
### 上传备份至 COS
1. 登录 [腾讯云控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2F)，在左上角选择【云产品】>【对象存储】，进入 COS 控制台，或者直接登录 [COS 控制台](https://console.cloud.tencent.com/cos5)。
![](https://main.qcloudimg.com/raw/08f65940f28d9f3e2400473f4be08270.png)
2. 选择【存储桶列表】，单击【创建存储桶】。
3. 在弹出的创建页面，配置对应信息，单击【确定】。
 - Bucket 的地域需要和迁移目标的 SQL Server 实例的地域相同。
 - COS 迁移不支持跨地域。  
![](https://main.qcloudimg.com/raw/4638c16ce60b47ced0348c092d7b4a78.png)
4. 返回存储桶列表，选择对应的存储桶，在【操作】列单击【文件列表】。
5. 在文件列表页，单击【上传文件】，可以选择单个或多个文件上传。
6. 文件上传完后，可在【操作】列单击【文件信息】，查看获取【对象地址】。
![](https://main.qcloudimg.com/raw/6f1639a7df6015e52d6a98913839352f.png)

### 通过 COS 源文件迁移数据
1. 登录 [腾讯云控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2F)，在左上角选择【云产品】>【关系型数据库】>【SQL Server】，进入 SQL Server 控制台，或者直接登录 [SQL Server 控制台](https://console.cloud.tencent.com/sqlserver)。
![](https://main.qcloudimg.com/raw/331ba40db9eaf166fa8334946e93150d.png)
2. 在左侧栏选择【数据传输】，单击【创建任务】，创建新的离线迁移任务。
  - 【任务名称】：用户自定义。
  - 【源实例类型】：选择【SQL Server 备份还原(COS方式)】。
  - 【地域】：源库信息的地域必须和 COS 源文件连接的地域相同。
  - 【COS 原文件链接】：上传源文件到 COS 后可查看文件信息，获取 COS 对象地址。
  - 【目标库类型】和【目标库地域】：根据源库的配置由系统自动生成。
  - 【实例 ID】：选择需要迁入的实例，只能选择同一地域下的实例。
![](https://main.qcloudimg.com/raw/9de77ed9d505eb7e8a4d7cc6a7de056c.png)
![](https://main.qcloudimg.com/raw/5c884d7ede2c8a38f538108b38a100ec.png)
3. 配置完成后，单击【下一步】。
4. 【选择类型】和【数据库设置】目前支持调整，单击【创建任务】。
5. 返回任务列表，此时任务状态为【初始化】，选择并单击【启动】同步任务。
6. 数据同步完成（即进度条为100%）后，需要手动单击【完成】，同步进程才会结束，根据【状态】查看迁移是否成功。
 - 任务状态变为【任务成功】时，表示数据迁移成功。
 - 任务状态变为【任务失败】时，表示数据迁移失败，请查看失败信息，并根据失败信息修正后重新迁移。


