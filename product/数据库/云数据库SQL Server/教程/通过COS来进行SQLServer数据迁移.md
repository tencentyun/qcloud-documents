云数据库 SQL Server 现已支持用户通过 COS 文件来进行数据迁移。具体步骤如下：

### 1.上传备份到 COS
已经创建 Bucket 后，可以跳过 1.1 和 1.2 步。
1.1 登录[腾讯云控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2F)，单击页面右上角【云产品】-【对象存储】
![](https://main.qcloudimg.com/raw/062794e8beff4e38f47d9f875ae14874.png)
1.2 选择【bucket 列表】，单击页面左上角【创建Bucket】
![](https://main.qcloudimg.com/raw/a28c4a31de1c406b8f154ae11a024530.png)
![](https://main.qcloudimg.com/raw/183b14813cf347f2c53fd8842b014e61.png)
>注释1：Bucket 的地域需要和迁移目标的 SQLServer 实例的地域相同。
Cos 迁移不支持跨地域。

1.3 单击【选择Bucket】- 【上传文件】-【文件信息】
![](https://main.qcloudimg.com/raw/968885446c9b7752c833ac166e5f8713.png)
![](https://main.qcloudimg.com/raw/59032f360cf78fd670a6acfc1dceffd0.png)
得到【源文件连接】。

### 2.通过 COS 的源文件连接备份还原
2.1 登录[腾讯云控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2F)，单击页面左上角【云产品】-【关系型数据库】，在左侧菜单栏单击【SQLServer】-【数据传输】，单击选择页面左上角【创建任务】
![](https://main.qcloudimg.com/raw/a42addc7282971bd635cc293d9be8086.png)
![](https://main.qcloudimg.com/raw/bbf3e56be9709c6cc423218fe6e90e07.png)
2.2 创建任务填写，单击【下一步】
![](https://main.qcloudimg.com/raw/2e9f9c55b9a09a0038afb43772d4b033.png)
>注释2：cos 源文件连接为步骤1得到【源文件连接】。这里注意的是地域必须和 COS 源文件连接的地域相同。
注释3：选择目标实例 ID .(只能选择同一地域下的实例)

2.3 cos 迁移目前不支持类型选择和数据库设置，在右下角单击【创建任务】-【启动】
![](https://main.qcloudimg.com/raw/0d6fd452e28c76b5a18ca67ab3293e41.png)
即可在数据传输列表中，查看到创建的迁移任务
![](https://main.qcloudimg.com/raw/e95aed63e9143b3af10231f760dda419.png)
单击【启动】迁移任务，稍等片刻，即可完成迁移。

### 常见问题：
1.备份文件必须是只包含一个库的备份文件，且确认能够解析。
2.备份的实例版本要与目标实例版本相同，或低于目标实例版本。例如从 2012 版本的 SQLServer 实例迁移到 2008 版本的 SQLServer 实例是不支持的。
3.确认目标 SQLServer 实例中没有重名的数据库，否则会导致迁移失败。
