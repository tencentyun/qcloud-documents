## 操作场景
消息队列 CKafka 支持用户转储消息的能力，您可以将 Ckafka 消息进行转储以便于对数据进行分析与下载等操作，常见转储场景有对象存储 COS、Elasticsearch Service（ES）、云数据库等。

## 前提条件
该功能目前依赖云函数 SCF，使用时需开通 SCF 产品功能。

## 操作步骤
### Ckafka 转储对象存储（COS）
1. 登录 [消息队列 CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在实例列表页，单击目标实例 ID，进入topic 管理标签页。
3. 在 topic 管理标签页，单击操作列的**消息转储**。
4. 单击**添加消息转储**，选择转储类型为对象存储（COS），填写以下信息：
![](https://main.qcloudimg.com/raw/ddb3f3d079f0ec8ab288f934facd8dce.png)
 - 转储类型：选择希望转储的函数模板，支持 COS 和通用模板两种转储类型。
 - 时间粒度：根据消息量的大小，选取汇聚消息的时间间隔，时间间隔为5 - 60分钟不等。为保证转储性能，聚合文件数量与 Partition 数量，partition_max 设置数值有关，具体详见文档底部产品限制说明。
 - 存放 Bucket：对不同的 topic，选取相应的 COS 中 Bucket，则请求消息会自动在 Bucket 下创建 instance-id/topic-id/date/timestamp 为名称的文件路径进行存储。相关路径如无法满足业务需要，请创建完成后在云函数 CkafkaToCosConsumer 下自行修改。
 - 起始位置：转储时历史消息的处理方式，topic offset 设置。
 - 角色授权：使用 SCF 产品功能，您需要授予一个第三方角色代替您执行访问相关产品权限。
 - 云函数授权：知晓并同意开通创建云函数，该函数创建后需用户前往云函数设置更多高级配置及查看监控信息。

>?如果您还未创建对象存储的 Bucket，请在 [新建 Bucket](https://console.cloud.tencent.com/cos/bucket) 后选取相应的存储位置。

### Ckafka 转储通用模板
1. 登录 [消息队列 CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在实例列表页，单击目标实例 ID，进入topic 管理标签页。
3. 在 topic 管理标签页，单击操作列的**消息转储**。
4. 单击**添加消息转储**，选择转储类型为通用模板，填写以下信息：
![](https://main.qcloudimg.com/raw/c9a8ce56182f59f086db1fb99d29e50a.png)
 - 转储类型：选择希望转储的函数模板，支持 COS 和通用模板两种转储类型。
 - 起始位置：转储时历史消息的处理方式，topic offset 设置。
 - 角色授权：使用 SCF 产品功能，您需要授予一个第三方角色代替您执行访问相关产品权限。
 - 云函数授权：知晓并同意开通创建云函数，该函数创建后需用户前往云函数设置更多高级配置及查看监控信息。
5. 单击**提交**，完成消息转储。

>?
>- 通用模板默认将不开启 Ckafka 触发器，选择通用模板需跳转云函数或本地使用 [SCF 通用模板](https://github.com/tencentyun/scf-demo-repo/tree/master/Python2.7-CkafkaTriggerTemplate) 进行代码编辑，请创建完成后在消息转储列表跳转到云函数控制台修改相关代码并开启 Ckafka 触发器。
>- 通用转储模板常见的转储应用场景有 [Elasticsearch Service](https://cloud.tencent.com/product/es)、[MySQL](https://cloud.tencent.com/product/cdb)、[PostgreSQL](https://cloud.tencent.com/product/postgres) 等。

### Ckafka 转储角色授权指引
#### COS 转储角色授权：

1. 在 CKafka 控制台的消息转储页，单击**新建运行角色**。
![](https://main.qcloudimg.com/raw/1945e5c557b5dcee7ba1da4ce16f2ae0.png)
2. 在跳转后的新页面选择角色载体信息，COS 转储推荐添加角色载体为云函数（SCF）：
（支持角色的服务列表动态更新，SCF 在列表中的具体位置以控制台显示为准）
![](https://main.qcloudimg.com/raw/6171856c8d21ba5f63829a573a0bd154.png)
3. 配置角色策略，COS 转储推荐添加如下策略：
```
QcloudSCFFullAccess
QcloudCOSFullAccess
QcloudCKafkaFullAccess
```
![](https://main.qcloudimg.com/raw/482cdacc368f9a43a297725299588ce8.png)
4. 定义角色名称，单击**完成**。
![](https://main.qcloudimg.com/raw/a4b6fe1e4a7119283d7a67dc0daf6e92.png)
5. 在 Ckafka 控制台，刷新消息转储页面并选择相应角色。
![](https://main.qcloudimg.com/raw/bbd89e73e9f1e1f1cffbb09a7728b7cc.png)

#### 通用转储角色授权：
在通用转储模板中授权函数访问其他的云服务，如果不访问任何云服务，则不用提供运行角色。操作流程同上。

## 产品限制和费用计算
- 转储速度与 Ckafka 实例峰值带宽上限有关，如出现消费速度过慢，请检查 Ckafka 实例的峰值带宽。
- Ckafka 转储 COS 的单个文件最大500MB，如超过该数值，会自动分包上传。
- 当前仅支持和 CKafka 实例同地域的 COS 进行消息存储。为保证低延时，不支持跨地域存储。
- 使用 COS 消息转储，文件内容是 CKafka 消息里的 value，用 utf-8 String 序列化拼接而成，暂不支持二进制的数据格式。
- 开启转 COS 的操作账号必须对目标 COS Bucket 具备写权限。
- 使用 COS 消息转储必须至少拥有一个 VPC 网络环境，如在创建时选择基础网络请参考 [路由接入方式](https://cloud.tencent.com/document/product/597/36348) 绑定 VPC 网络。
- 该功能基于云函数 SCF 服务提供。SCF 为用户提供了一定量 [免费额度](https://cloud.tencent.com/document/product/583/12282) ，超额部分产生的收费，请以 SCF 服务的 [计费规则](https://cloud.tencent.com/document/product/583/17299) 为准。






