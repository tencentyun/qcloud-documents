SQL 作业是通过 SQL 语句直接编写业务逻辑的方式。对于流计算开发人员来说，是一种实现简单高效、体验友好的作业开发方式。

## 前提条件
创建 SQL 作业时，需要先准备好上下游数据，具体请参见 [上下游数据一览](https://cloud.tencent.com/document/product/849/38374)。

## 操作步骤
### 1. 创建 SQL 作业
登录 [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus)，单击左侧菜单栏【流计算 Oceanus】下的【作业管理】，进入作业管理页面。单击【新建SQL作业】，进入创建 SQL 作业页面，输入相关信息购买和创建作业。
![](https://main.qcloudimg.com/raw/6affb1561ae37df0a3d99277d796c6de.png)

相关信息如下：

| 参数     | 说明                                                     |
| -------- | -------------------------------------------------------- |
| 地域     | 作业所在地域                                             |
| 作业名称 | 给作业取一个名字                                         |

### 2. 流计算服务委托授权
在【作业管理】页面单击某个作业名称打开【作业详情】页，单击【分析开发】，在未授权时，弹出访问授权对话框如下。单击【前往授权】，授权流计算作业访问您的 CKafka、TencentDB 等资源。
![角色授权弹框](https://main.qcloudimg.com/raw/0810024f6f10d6fb8a4ce689a274537f.png)

> ? 此授权的详细说明参见 [流计算服务委托授权](https://cloud.tencent.com/document/product/849/38290)。

### 3. 编写 SQL 语句
在【作业管理】页面单击某个作业名称打开【作业详情】页，单击【分析开发】，进入作业开发页。在代码编辑框输入 SQL 语句进行业务逻辑开发，SQL 语句编写请参见 [SQL 手册-术语表](https://cloud.tencent.com/document/product/849/18149)。单击【语法检查】检查语法是否完全正确，如果提示错误，请根据提示修改 SQL 语句。

编写 SQL 语句方式如下：
1. 直接编写 SQL 语句
可直接在代码编辑框中输入 SQL 语句。
![直接编写SQL作业](https://main.qcloudimg.com/raw/af29d424f7341bde943ea85100b54117.png)
2. 通过【分析模板】生成 SQL 语句
单击代码编辑框上方的【分析模板】，在弹出的【选择模板】对话框中选择一个合适的模板，将模板代码添加到代码编辑框中，然后根据自己的业务实际情况修改代码逻辑。
![选择模板](https://main.qcloudimg.com/raw/75150c95a0f3860f54763651bfe05d0e.png)
3. 通过【选择数据流】生成 SQL 语句
单击代码编辑框上方的【选择数据流】，通过【添加数据流DDL】对话框自动生成 SQL 代码，然后编写计算逻辑。

 示例如下：类型选择 CKafka，实例 ID 选择您在准备工作中创建的 CKafka，Topic 选择作为数据源的 Topic，数据格式选择 json，输入字段结构，单击【预校验】来校验输入的字段结构是否与 CKafka 中一致，最后单击【添加】。
![添加数据流DDL](https://main.qcloudimg.com/raw/0df6e8e9fdb6517893a9294a44b91dba.png)
添加完数据流以后，在代码编辑框中会生成如下代码：
```mysql
CREATE TABLE `page_visits` (
  `record_time` VARCHAR,
  `user_id` VARCHAR,
  `page_id` VARCHAR
) WITH (
  `type` = 'ckafka',
  `instanceId` = 'ckafka-xxxxxxxx',
  `encoding` = 'json',
  `topic` = 'page_visits'
);
```
您可以用同样的方式添加其他数据流如 TencentDB For MySQL 等。

### 4. 调试 SQL 作业
编写完代码后，可选择在发布之前先进行调试。我们为用户提供了一套独立的模拟环境，用户可以在该环境中上传数据，模拟运行并检查输出结果。
1. 选择【分析开发】>【调试】，会进入调试页面，如下所示：
![上传调试数据界面](https://main.qcloudimg.com/raw/905a6eb15b9b37adc81ebea131b37530.png)
2. 单击对应数据源的【上传】，从本地上传数据文件，单击【开始调试】，界面显示如下：
![等待调试结果界面](https://main.qcloudimg.com/raw/b7901616dbf6e72c11c53590e48502df.png)
3. 单击【确定】，等待片刻后，会显示调试结果，可单击【下载结果】下载调试结果。
![调试结果](https://main.qcloudimg.com/raw/82c70664e043a33dc92e97008854b30d.png)
根据调试结果判断 SQL 代码的执行达到预期效果，即可进行发布。

### 5. 发布运行 SQL 作业
#### 参数设置
在【分析开发】页的【参数设置】区域，设置是否开启 checkpoint 以及时间间隔。
![保存并发布运行](https://main.qcloudimg.com/raw/6218e32d518094aeea9ef8981aafcc66.png)

| 参数       | 说明                                                         |
| ---------- | ------------------------------------------------------------ |
| checkpoint | 定时快照，用来保存作业的运行状态，当作业意外崩溃时可从最近快照点恢复 |
| 时间间隔   | 进行 checkpoint 操作的时间间隔                               |

#### 发布运行
单击【保存并发布运行】，弹出如下对话框，允许指定数据消费时间点来运行作业，可以选择您期望的时间点，单击【确定】，提交运行作业。
>?消费时间点指定流计算作业从何时开始消费数据。

![指定时间运行](https://main.qcloudimg.com/raw/70f9feb243741c1ab714e0da827c315a.png)

 

