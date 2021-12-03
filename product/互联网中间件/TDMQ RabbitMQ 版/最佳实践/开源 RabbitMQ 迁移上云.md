## 操作场景
该任务指导您将开源 RabbitMQ 的元数据迁移至腾讯云消息队列 RabbitMQ 版。

## 前提条件

向消息队列 RabbitMQ 版导入元数据文件时，您需要先从开源 RabbitMQ 导出元数据文件。从开源 RabbitMQ 导出元数据文件请参考 [导出开源 RabbitMQ 元数据](#export)。

## 操作步骤

### 导出开源 RabbitMQ 元数据[](id:export)

#### 通过控制台导出开源 RabbitMQ 元数据

1. 打开浏览器登录开源 RabbitMQ 控制台。
2. 在 Overview 页面下方，单击 **Export definitions**。在输入框中填写目标文件名后，在“Virtual host”处选择“All”或某个 Vhost，单击右侧的 **Download broker definitions**，导出全部 Vhosts 或某个 Vhost 的元数据文件。
![](https://qcloudimg.tencent-cloud.cn/raw/5faa9f9ac376fe202882d5a090fd0c53.png)

#### 使用开源 RabbitMQ HTTP API 导出元数据

1. 打开终端。
2. 在终端输入以下命令以导出开源 RabbitMQ 元数据文件。
	- 导出 All Vhosts 的元数据文件：
	```
	wget http://<开源 RabbitMQ IP 地址>:15672/api/definitions --user <开源 RabbitMQ 用户名>  --password <开源 RabbitMQ 密码>  -O <元数据文件保存路径>
	```
	- 导出某一个 Vhost 的元数据文件：
	```
	wget http://<开源 RabbitMQ IP 地址>:15672/api/definitions/<Vhost 名称> --user <开源 RabbitMQ 用户名>  --password <开源 RabbitMQ 密码>  -O <元数据文件保存路径>
	```
	
### 在消息队列 RabbitMQ 版控制台导入元数据

1. 登录 [消息队列 RabbitMQ 版控制台](https://console.cloud.tencent.com/tdmq/rabbit-cluster)，在左侧导航栏单击**迁移上云**。
2. 在迁移上云页面，选择目标地域后，单击**新建任务**。
![](https://qcloudimg.tencent-cloud.cn/raw/5f52006a9fcc1df81b0e822aae37d9fb.png)
3. 在新建任务页面，创建导入开源 RabbitMQ 元数据任务，填写相关字段：
<dx-tabs>
::: 集群迁移
![](https://qcloudimg.tencent-cloud.cn/raw/815bdd1d86c2d2dc585920987aa040f0.png)
:::
::: 导入 Vhost
![](https://qcloudimg.tencent-cloud.cn/raw/e1afafb104c5e2ed26e6764a64beafdf.png)
:::
</dx-tabs>


字段填写说明：

| 字段       | 说明                                                         |
| :--------- | :----------------------------------------------------------- |
| 任务类型   | 可选集群迁移或导入 Vhost。选择集群迁移时，导入从开源 RabbitMQ 导出的 All Vhosts 元数据；选择导入 Vhost 时，导入从开源 RabbitMQ 导出的单个 Vhost 元数据文件。 |
| 集群       | 选择待导入的目标集群，可选已创建的集群，也可以新建集群。     |
| Vhost 名称  | 选择“导入 Vhost”任务类型时，需填写 Vhost 名称。              |
| 消息 TTL   | 指定未消费消息的过期时间，任务类型为集群迁移导入多个 Vhost 元数据时，为导入的所有 Vhosts 设定消息 TTL，后续可在集群管理-Vhost-操作-编辑处修改。 |
| 元数据文件 | 单击上传从开源 RabbitMQ 导出的元数据文件，可对文件内容进行在线修改。元数据文件格式请参考 [元数据文件格式说明](#format)。 |

4. 单击**创建任务**，完成迁移。提交迁移上云任务。
提交后，系统会对元数据文件进行格式校验。格式校验通过后，即跳转至迁移上云首页，显示迁移进度。

>!同一消息队列 RabbitMQ 集群下，在同一时间内仅能执行一个迁移上云任务。在上一个迁移任务执行结束后，才能继续向该消息队列 RabbitMQ 集群创建新的迁移上云任务。


### 查看迁移任务详情

1. 进入 [迁移上云](https://console.cloud.tencent.com/tdmq/rabbit-migrate) 界面，选择目标地域后，即可查看该地域下所有迁移上云的任务列表。
![](https://qcloudimg.tencent-cloud.cn/raw/cddd79fa84d2f4beeb2ca08500e4feab.png)
2. 状态列展示了某一迁移上云任务的执行结果。各状态说明如下：

| 状态     | 说明                                                         |
| :------- | :----------------------------------------------------------- |
| 迁移中   | 元数据文件正在迁移。                                         |
| <nobr>迁移成功</nobr> | 导入任务中涉及的全部 Vhosts 元数据文件均迁移成功。           |
| 迁移失败 | 任务类型为导入 Vhost 时，单一 Vhost 元数据文件导入失败；或任务类型为集群迁移时，所有 Vhosts 元数据文件均导入失败。 |
| 部分失败 | 任务类型为集群迁移时，部分 Vhosts 元数据文件导入失败。       |
| 迁移超时 | 导入元数据文件时超时。                                       |

3. 单击操作列的**查看详情**，查看元数据文件导入详情。
	 ![](https://qcloudimg.tencent-cloud.cn/raw/475a0e7aa59ff87b654a20c12a2b4d5c.png)

## 元数据导入说明

### 元数据文件格式说明[](id:format)

| 任务类型                         | 集群迁移                                                     | 导入 Vhost                                                   |
| :------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 文件格式                         | json                                                         | json                                                         |
| 字段要求                         | 数据中必须包含 "vhosts" 列表，且 exchanges、queues、bindings 列表中需包含"vhost"字段 |                                                              |
| 命名规范                         | Vhosts、exchanges、queues、bindings 命名规则需符合 TDMQ RabbitMQ 命名规则限制，详情见[使用限制](https://cloud.tencent.com/document/product/1495/61823) | exchanges、queues、bindings 命名规则需符合 TDMQ RabbitMQ 命名规则限制，详情见[使用限制](https://cloud.tencent.com/document/product/1495/61823) |
| 开源 RabbitMQ 元数据文件导出方式 | 在开源 RabbitMQ 控制台的 Overview 界面，使用 Export definitions 功能，将 Virtual host 选为 All，导出 All Vhost 的元数据。若您想删除某些 Vhost 不予导入，请您在"vhosts"列表中删除某些 Vhost 名称后再进行集群迁移 | 在开源 RabbitMQ 控制台的 Overview 界面，使用 Export definitions 功能，Virtual host 处选择导出某一 Vhost 的元数据 |

### 元数据兼容性说明

消息队列 RabbitMQ 版对开源 RabbitMQ 元数据兼容性如下表：

| 元数据字段        | 说明                                                         | 兼容性                                                       |
| :---------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| rabbitmq_version  | 开源 RabbitMQ 的集群版本                                     | 否                                                           |
| users             | 开源 RabbitMQ 的用户信息                                     | 否                                                           |
| vhosts            | 开源 RabbitMQ 中的 Vhost 列表                                | 是，开源 RabbitMQ 默认创建的名为“/” 的Vhost，由于消息队列 RabbitMQ 版命名限制，将被自动更名为“\__default_vhost__” |
| permissions       | 开源 RabbitMQ 用户管理 Vhost 权限                            | 否                                                           |
| parameters        | 开源 RabbitMQ 运行参数                                       | 否                                                           |
| global_parameters | 开源 RabbitMQ 全局参数                                       | 否                                                           |
| policies          | 开源 RabbitMQ 为某个 Vhost 设定的，应用于该 Vhost 下的队列或 exchanges 的可选参数，如 TTL 和队列长度限制等 | 否，若您需使用这些可选参数，可以前往控制台进行编辑，或在删除后重新创建 |
| queues            | 开源 RabbitMQ 的队列                                         | 是                                                           |
| exchanges         | 开源 RabbitMQ 的 Exchange                                    | 是                                                           |
| bindings          | 开源 RabbitMQ 的绑定关系                                     | 是                                                           |

