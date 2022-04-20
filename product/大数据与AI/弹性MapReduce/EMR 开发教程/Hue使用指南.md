Hue 是一个开源的 Apache Hadoop UI 系统，由 Cloudera Desktop 演化而来，最后 Cloudera 公司将其贡献给 Apache 基金会的 Hadoop 社区，它是基于 Python Web 框架 Django 实现的。通过使用 Hue 我们可以在浏览器端的 Web 控制台上与 Hadoop 集群进行交互来分析处理数据，例如操作 HDFS 上的数据、运行 MapReduce Job、执行 Hive 的 SQL 语句和浏览 HBase 数据库等。

## 访问 Hue WebUI
**使用 Hue 组件管理工作流时，请先登录 Hue 控制台页面，具体步骤如下：**
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，单击对应集群 **ID/名称**，进入集群详情页面，然后单击**集群服务**。
2. 在列表页找到 Hue 组件，单击 **WebUI 访问地址**进入 Hue 页面。
3. 首次登录 Hue 控制台页面，请使用 root 帐号，密码为创建集群时提供的密码。
![](https://qcloudimg.tencent-cloud.cn/raw/fe7b2fa224ee12a8a5ded70ccc4a99a7.png)

>! 由于 EMR 产品的组件启动帐号为 hadoop。请在首次以 root 帐号登录 Hue 控制台后，新建 hadoop 帐号。后续所有作业需通过 hadoop 帐号来提交。

## 用户权限管理
首先使用管理员账号登录 hue。
1. 添加用户。
	1. 单击右方的** Add user**。
![](https://qcloudimg.tencent-cloud.cn/raw/34bd048f7de580e9bff702b29948bbfc.png)
	2. 填写用户信息。
![](https://qcloudimg.tencent-cloud.cn/raw/6430783ac956a685869baf3c8f0d211c.png)
	3. 填写用户组以及其他信息。
![](https://qcloudimg.tencent-cloud.cn/raw/fd48a071256ec993b39975f066445720.png)
	4. 单击** Add User**按钮添加用户。
![](https://qcloudimg.tencent-cloud.cn/raw/b45249ecbc4bf18288b6a1809d003073.png)
2. 权限控制。
hue 通过将不同的权限添加到组，用户通过加入不同的组获得对应权限。
	1. 单击用户管理页面上方的 **Groups**，然后单击右侧的 **Add group**。
![](https://qcloudimg.tencent-cloud.cn/raw/6b857c8fa14a766f73b62ff1f9077e92.png)
	2. 填写用户组信息，可勾选那些用户加入此组，并勾选此用户组的权限，单击下方的 **Add Group**。
![](https://qcloudimg.tencent-cloud.cn/raw/3fbccd716621bae652c293563f3b098e.png)

## 数据导入
Hue 支持4种导入方式：本地文件、HDFS 上的文件、外部数据库以及人工导入。
![](https://qcloudimg.tencent-cloud.cn/raw/a65e26d2349659cc3d497bfb2c4ac009.png)
1. 本地文件导入。
	1. 单击浏览选择 csv 文件，hue 会自动识别出分隔符并生成预览，单击 Next 导入到表。
![](https://qcloudimg.tencent-cloud.cn/raw/88e2cece5e749f9fcbf8e8f7edfd0af3.png)
	2. 填写需要导入的表信息等，单击保存。
![](https://qcloudimg.tencent-cloud.cn/raw/a47b12e883dcd11d0d6b35ffb45e7bfd.png)
2. HDFS 文件导入。
	1. 选择 HDFS 上的 csv 文件。
![](https://qcloudimg.tencent-cloud.cn/raw/c85db98b103806a35e8e1363d87c497c.png)
	2. 填写需要导入的表信息等，单击保存。
![](https://qcloudimg.tencent-cloud.cn/raw/65c00836a506c4619e40b9b15eed0439.png)
3. 外部数据库 External Database.
	1. 填写外部数据库信息，单击 **Test Connection** 获取到数据库信息，选择库和表后单击 Next。
![](https://qcloudimg.tencent-cloud.cn/raw/4e7b192e8cbb52970282dd29774ebaaa.png)
	2. 填写需要导入的目的表信息，并单击 lib 选择 mysql 驱动，然后单击保存。
![](https://qcloudimg.tencent-cloud.cn/raw/b466c8315dc8c7aeb449164327702194.png)

## Job 管理
单击右侧的 **Jobs**标签，即可进入任务管理页面，单击上方的各个任务类型标签，可进行查看管理。
![](https://qcloudimg.tencent-cloud.cn/raw/d0d9f3254368fda9b4044db6055813c0.png)
![](https://qcloudimg.tencent-cloud.cn/raw/7aaae821f6ebfab18b64da888fa9a053.png)

## Table 管理
1. 单击右侧的 **Tables** 进入到 Table 管理页面，可以查看到基本的数据库信息。
![](https://qcloudimg.tencent-cloud.cn/raw/058bdbd72391b69a0eae466869a47bf0.png)
2. 单击其中一个数据库，可查看此数据库的表。
![](https://qcloudimg.tencent-cloud.cn/raw/a14dba986a6192e6246a179560bc790f.png)
3. 单击各个表，可以查看表的具体详情信息。
![](https://qcloudimg.tencent-cloud.cn/raw/cc89817cc1759903a516db03a3f5abfb.png)
