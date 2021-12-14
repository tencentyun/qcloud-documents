
## 操作场景
云数据库 SQL Server 支持数据源是云服务器 CVM 自建的 SQL Server 数据库进行数据迁移，本文将指导您如何配置迁移任务，帮助您将 CVM 上自建的 SQL Server 数据库迁移至云数据库 SQL Server。
>!
>- 迁移前需保证目的实例的 SQL Server 版本不低于源实例的版本。
>- 支持单个 bak 文件及 tar 压缩文件上传进行恢复。
>- 迁移库不能与云数据库 SQL Server 库有库名重复的情况。

## 操作步骤
### 步骤一：创建迁移任务
1. 登录 [SQL Server 控制台](https://console.cloud.tencent.com/sqlserver)，在左侧栏选择【数据迁移旧版】。
2. 单击【创建任务】，填写任务名称、源库信息、目标库信息，源实例类型选择【云服务器自建SQL Server数据库】。
![](https://main.qcloudimg.com/raw/da77fa7fe6ed5dc4c493861d1850ee3d.png)
3. 单击【下一步】后，需先对 [源 SQL Server 实例进行相关配置](#step2) 再继续 [配置迁移任务](#step3)。
>?若出现报错信息为 “源实例信息校验不通过！” ，请检查以下几项进行排查：
>- 源 SQL Server 实例 sa 账号是否存在。
>- 源 SQL Server 实例 sa 账号密码是否正确。
>- 源 SQL Server 实例 IP 和 PORT 连通性是否正常。

### [步骤二：配置源 SQL Server 实例](id:step2)
1. 源 SQL Server 实例开启 sa 账户。
2. 在【连接】里选择【允许远程连接到此服务器】，并设置合理的远程查询超时值。
![](https://main.qcloudimg.com/raw/5f0cec5032756cbf39c3260447746781.png)
3. 在【安全性】里选择【SQL Server 和 Windows 身份验证模式】。
![](https://main.qcloudimg.com/raw/8665101c74549911a0e6ee8e90850151.png)
4. 开启网络协议 TCP/IP。
![](https://main.qcloudimg.com/raw/21b80c7353bf17fc2d867cc70b2a6f8c.png)
5. 启动内置帐户选择【localsystem】。
![](https://main.qcloudimg.com/raw/5b929ede440766e2913f4e96a448acb6.png)
6. Windows 防火墙允许 SQL Server 端口通信，以及445端口通信（基础网络）或49001端口通信（私有网络）。
7. （可选）【CVM 网络】选择【私有网络】时，需配置 freeSSHd 工具。
 1. 下载安装 [freeSSHd](http://www.freesshd.com/freeSSHd.exe)，默认安装即可，同意启动 freeSSHd 服务。
 2.  双击 freeSSHd 桌面图标，右键任务栏 freeSSHd 图标打开 setting 设置页面，进行配置。
 3.  选择【SSH】选项，配置端口为49001（此处端口默认为22，需要改为49001）。![](https://main.qcloudimg.com/raw/72d8780b85afa18524dc2fb81bcd6baf.png)
 4.  选择【Server status】选项，启动 ssh server。
 5.  选择【Authentication】选项，选择【Allowed】允许密码授权。
 6.  选择【Users】选项，添加用户 tencent_vpc_migrate（该用户名不可更改），密码 tencent_vpc_migrate（该密码不可更改），配置如下图所示：
 ![](https://main.qcloudimg.com/raw/9d8658d6f44517e7554c3416780f0a58.png)
 7.  使用 D:\dbbackup\（**此路径不可改变**）为 SQL Server 迁移中使用的备份文件夹，选择【SFTP】选项，并将此路径配置到“SFTP home path”中。

### [步骤三：配置迁移任务](id:step3)
选择迁移类型、设置数据库（选择需要迁移的库表），单击【保存并校验】，如校验不通过可按错误提示完成修复。
![](https://main.qcloudimg.com/raw/6ea9a3c3c3496a3c3782037e0e988ff3.png)

### 步骤四：启动迁移任务
任务创建完后，返回任务列表，此时任务状态为【初始化】，选择并单击【启动】同步任务。

### 步骤五：完成迁移任务
数据同步完成（即进度条为100%）后，需要手动单击【完成】，同步进程才会结束；如果在配置迁移任务时勾选了【增量同步】，需在进度条在99%时手动单击【完成】；根据【状态】查看迁移是否成功。
 - 任务状态变为【任务成功】时，表示数据迁移成功。
 - 任务状态变为【任务失败】时，表示数据迁移失败，请查看失败信息，并根据失败信息修正后重新迁移。
