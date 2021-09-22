## 操作场景

虚拟主机（Virtual Host，简称 Vhost）是 TDMQ RabbitMQ 版中的一个资源管理概念，用作逻辑隔离，不同Vhost 之间的 Exchange 和 Queue 相互隔离，互不干扰。

用户不同的业务场景一般都可以通过 Vhost 做隔离，并且针对不同的业务场景设置专门的配置，例如消息保留时间。

本文档指导您使用消息队列 TDMQ RabbitMQ 版时，创建多个Vhost，以便在同一个集群下将 TDMQ RabbitMQ 版应用于不同的场景。

>?同一个 Vhost 下的 Exchange 和 Queue 的名称唯一。

## 前提条件

[已创建集群]()。

## 操作步骤

### 创建 Vhost

1. 登录 [TDMQ 控制台](https://console.cloud.tencent.com/tdmq)，选择地域后，单击目标集群的ID进入集群基本信息页面。

2. 选择顶部【Vhost】页签，单击【新建】进入创建Vhost页面。

3. 在新建Vhost对话框，设置Vhost的相关属性配置。
   
    ![](https://main.qcloudimg.com/raw/c87ba46c5d7e458f392c41579964be9a.png)
    
    - Vhost名称：设置Vhost的名称（创建后不可修改），3-64个字符，只能包含字母、数字、“-”及“_”
    - 消息TTL：设置未消费消息的保留时间，过期未 ACK（确认消息） 则自动删除，范围：60秒-15天
    - 说明：Vhost 的备注说明
    
4. 单击【提交】完成所在集群Vhost的创建。

后续步骤：接下来就可以在该 Vhost 中 [创建 Exchange ]() 和[Queue]()进行消息的生产和消费了。

### 配置权限

**前提条件**：[已创建角色](https://console.cloud.tencent.com/tdmq/role)。

1. 在 Vhost 列表页面，单击目标 Vhost 操作栏的**配置权限**。

2. 在**配置权限**页面，单击**新建**，为刚刚创建的角色添加生产消费权限。

   ![](https://main.qcloudimg.com/raw/515644356c3ec5d005f61ea19fa6e807.png)

### 



### 修改 Vhost

如果需要重新修改编辑Vhost，可以通过以下步骤操作：
1. 在【Vhost】列表页，单击操作列的【编辑】，进入编辑页面。
2. 修改消息 TTL 或说明，单击【提交】完成修改。

### 删除 Vhost
如果想删掉创建的Vhost，可以通过以下步骤操作：
1. 在【Vhost】列表页，单击操作列的【删除】。
2. 在删除的确认弹框中，单击【确定】，即可删除命名空间。

>!Vhost 删除后，该 Vhost 下的所有资源将会被清空，且无法恢复。

