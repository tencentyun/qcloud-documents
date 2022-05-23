## 操作场景

该任务将指导您在 Slack 群创建一个机器人，用于在 Slack 群接收消息。

## 操作步骤

### 创建机器人
1. 登录消息中心控制台，在左侧导航栏单击 [机器人接收管理](https://console.cloud.tencent.com/message/robot)。
2. 在机器人接收管理页签，单击**新建机器人**。
3. 在新建机器人窗口，填写以下配置信息：
![](https://qcloudimg.tencent-cloud.cn/raw/9f53cea6d07f99f0d210598e02eff4e3.png)
	- 机器人类型：支持单个机器人、机器人组（可添加多个机器人 Webhook 地址）。
	- 机器人平台：选择“飞书”。
	- 机器人名称：填写机器人名称。
	- 安全配置：默认
	- Webhook 地址：参考[获取Webhook地址](#webhook)
4. 单击**确定**，创建成功。



### 获取 Webhook 地址[](id:webhook)
1. 前往 [Slack API 页面](https://api.slack.com/apps) ，单击 **Create New App**。
![](https://qcloudimg.tencent-cloud.cn/raw/31a04c403816f6f9c1734e9b139ec4e0.png)
2. 在创建 App 页面，单击 **From scratch**。
![](https://qcloudimg.tencent-cloud.cn/raw/e1be3aaa815237a1638d12b4e0b7ee9e.png)
3. 填写机器人信息后，单击 **Create App**。
![](https://qcloudimg.tencent-cloud.cn/raw/febb7220b717eff4f375cf71f23f833c.png)
	- App Name：机器人名称
	- Pick a workspace to develop your app in ：选择要接收消息的群
4. 单击页面左侧的**App Home**。
![](https://qcloudimg.tencent-cloud.cn/raw/21eb15f8caa6876508d7efc9dd4f4d70.png)
5. 单击 **Edit**，编辑机器人名称，使机器人生效。
![](https://qcloudimg.tencent-cloud.cn/raw/c121e3a9f58e8eb3bdddc90ef6731699.png)
6. 单击页面左侧的**Incoming Webhooks** ，添加 Webhook。
![](https://qcloudimg.tencent-cloud.cn/raw/7b5f65c08a3e0aabfcbc68121f493970.png)
7. 单击**Off**，启用 Webhooks。
![](https://qcloudimg.tencent-cloud.cn/raw/6881b1252cc7afe8771ccdc8a8c08618.png)
8. 下滑至页面底部，单击 **Add New Webhooks to Workspace**。 
![](https://qcloudimg.tencent-cloud.cn/raw/fb48696bee1b6431cfd85616de6f93fc.png)
9. 在新开的页面，选择需要接收消息的群，单击**允许**。
![](https://qcloudimg.tencent-cloud.cn/raw/cac85e33282e1115c59a44dd88fc919f.png)
10. 刷新页面后，下滑至页面底部，即可看到 Webhook 地址。
![](https://qcloudimg.tencent-cloud.cn/raw/6ef07e26c6f36a50ef36205314ed2ec9.png)
