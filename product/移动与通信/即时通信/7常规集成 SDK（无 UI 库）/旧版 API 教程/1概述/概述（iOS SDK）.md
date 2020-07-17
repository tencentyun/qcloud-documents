## IM SDK 基本概念

**会话：**IM SDK 中会话（Conversation）分为两种，一种是 **C2C 会话**，表示单聊情况自己与对方建立的对话，读取消息和发送消息都是通过会话完成。另一种是**群会话**，表示群聊情况下，群内成员组成的会话，群会话内发送消息群成员都可接收到。如下图所示，一个会话表示与一个好友的对话。

![](https://main.qcloudimg.com/raw/1cdf0ae83214cd804e13e54cafc3e288.jpg)

**消息：**IM SDK 中消息（Message）表示要发送给对方的内容，消息包括若干属性，如是否自己已读，是否已经发送成功，发送人帐号，消息产生时间等。一条消息由若干 `Elem` 组合而成，每种 `Elem` 可以是文本、图片、表情等等，消息支持多种 `Elem` 组合发送。

![](https://main.qcloudimg.com/raw/61e24f0e5e9d0f3bba699609bc604d42.png)

**群组 ID：**群组 ID 唯一标识一个群，由后台生成，创建群组时返回。

## IM SDK 对象简介

iOS IM SDK 对象主要分为通讯管理器、会话、消息、群管理，具体的含义参见下表。

| 对象 | 介绍 | 功能 |
| --- | --- | --- |
| TIMManager | 管理器类 | 负责基本的 SDK 操作，包含初始化登录、注销、创建会话等 |
| TIMConversation | 会话 | 负责会话相关操作，包含发送消息、获取会话消息缓存、获取未读计数等 |
| TIMMessage | 消息 | 包含文本、图片等不同类型消息 |
| TIMGroupManager | 群管理器 | 负责创建群、增删成员、以及修改群资料等 |
| TIMFriendshipManager | 好友关系链管理器 | 负责添加、删除好友以及好友资料管理等 |


## 调用顺序介绍

IM SDK 调用 API 需要遵循以下顺序，其余辅助方法需要在登录成功后调用。

| 步骤 | 对应函数 | 说明 |
| --- | --- |  --- |
| 初始化 | TIMManager:initSdk | 设置 SDK 配置信息 |
| 初始化 | TIMManager:setUserConfig | 设置用户的配置信息 |
| 登录 | TIMManager:login | 登录 |
| 消息收发 | TIMManager:getConversation | 获取会话 |
| 消息收发 | TIMConversation:sendMessage | 发送消息 |
| 群组管理 | TIMGroupManager | 群组管理 |
| 关系链管理 | TIMFriendshipManager | 关系链管理 |
| 注销 | TIMManager:logout | 注销（用户可选） |

