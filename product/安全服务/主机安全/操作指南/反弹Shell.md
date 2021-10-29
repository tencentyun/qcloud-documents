本文档将为您介绍如何对反弹 Shell 详情进行查看和处理，同时指导您如何创建白名单，用于设置被允许的反向连接行为。
## 背景信息
反弹 Shell 功能是基于腾讯云安全技术及多维度多手段，对服务器上的 Shell 反向连接行为进行识别记录，为您的云服务器提供反弹 Shell 行为的实时监控能力。

## 前提条件
反弹 Shell 功能为专业版付费功能，需升级为 [专业版主机安全](https://buy.cloud.tencent.com/yunjing) 进行使用。


## 操作步骤
### 事件列表
1. 登录 [主机安全控制台](https://console.cloud.tencent.com/cwp/manage/maliciousRequest)，在左侧导航栏，选择**入侵检测** > **反弹 Shell**，进入反弹 Shell的事件列表标签页面。
2. 在反弹 Shell 的“事件列表”标签页面，可查看反弹 Shell 事件列表，并进行相关操作。
	在事件列表标签界面，可查看发生反弹 Shell 的服务器/名称、连接进程、发现时间、状态（全部、待处理及已确认），操作（详情、加白名单及删除）等12个字段，展示列表详情信息可进行自定义。
	- **筛选事件**：反弹 Shell 事件列表支持选择日期查看相应事件，支持按关键字及标签查询（多个关键字用竖线 “|” 分隔，多个过滤标签用回车键分隔）事件，同时支持按状态（全部、待处理及已确认）筛选事件。
	![](https://main.qcloudimg.com/raw/76e1a8aafd23d9289373b194918e53aa.png)
	- **自定义设置列表字段**：在反弹 Shell 事件列表上方，单击<img src="https://main.qcloudimg.com/raw/9ebb9fa1652d9154137fa1d934329043.png" style="margin:0;">，可设置列表展示字段，选择完成后，单击**确定**，即可设置成功。
	![](https://main.qcloudimg.com/raw/b8a81050619e8c3f8d0c2b3c83c5c676.png)
	- **事件导出**：在反弹 Shell 事件列表上方，单击<img src="https://main.qcloudimg.com/raw/ac6451a8dab74a5cf57770ff8af30954.png" style="margin:0;">，可将反弹 Shell 事件列表导出。
	- **详情**：在目标反弹 Shell 事件的右侧操作栏，单击**详情**，可查看反弹 Shell 事件详情。
![](https://main.qcloudimg.com/raw/3aed9137c50a621fcb545a6d2980bcfb.png)
	- **加白名单**：如需将反弹 Shell 事件加入白名单，可在目标反弹 Shell 事件的右侧操作栏，单击**加白名单**，确认无误后，在弹窗中，单击**提交**，即可将该反弹 Shell 事件标记为白名单事件。
	- **删除**：反弹 Shell 事件列表支持对反弹 Shell 事件进行删除。
		- **方式1**：在目标反弹 Shell 事件的右侧操作栏，单击**删除**，确认无误后，即可删除该事件。
		- **方式2**：全选或勾选需要删除的反弹 Shell 事件，在反弹 Shell 事件列表上方，单击**删除**，确认无误后，即可删除选中事件。
	![](https://main.qcloudimg.com/raw/dd5e33d4223b316e8e968e8c16b03870.png)
3. 单击反弹 Shell 事件的服务器 IP，可查看该服务器详情。	
![](https://main.qcloudimg.com/raw/a12e00eb81b03cc4530e46e82b7547a1.png)

### 白名单管理
反弹 Shell 功能支持添加白名单，通过设置白名单提权条件，将满足条件的事件标记为白名单。
1. 登录 [主机安全控制台](https://console.cloud.tencent.com/cwp/manage/maliciousRequest)，在左侧导航栏，选择**入侵检测** > **反弹 Shell **，进入反弹 Shell 页面。
2. 在“反弹 Shell ”页面，选择**白名单管理** > **添加白名单**。
![](https://main.qcloudimg.com/raw/6d529dc645370d679d952754d03eca5a.png)
3. 在“添加白名单”页面，设置反弹 Shell 条件，包括：目标主机、自定义连接进程（支持多个进程名，以英文逗号分隔），同时选择该条件覆盖的服务器范围，单击**确定**。
>!
>- IP地址格式：单个 IP（127.0.0.1）、IP 范围（127.0.0.1-127.0.0.254）、IP 网段（127.0.0.1/24）。
>- 端口格式：80,8080（支持多个端口并以英文逗号分隔，不限端口请留空）。
>- 勾选两个条件时，需要同时满足才能命中白名单。
>- 若服务器范围选择全部服务器，将对用户 APPID 下所有服务器添加信任该白名单条件，请谨慎操作。
>
![](https://main.qcloudimg.com/raw/915ec17a661b23c432a8ccd4305fd9d6.png)
4. 设置完成后，可在白名单管理列表查看该条件，且在事件列表满足该条件的事件即会被标记为白名单事件。
5. 在白名单管理页面，可对白名单进行筛选删除等操作。
	- **筛选**：已配置的白名单支持按关键字及标签查询（多个关键字用竖线 “|” 分隔，多个过滤标签用回车键分隔）筛选。
![](https://main.qcloudimg.com/raw/c0a30d4174892453ff194d19c65aebd3.png)
	-  **自定义设置列表字段**：在白名单列表上方，单击<img src="https://main.qcloudimg.com/raw/9ebb9fa1652d9154137fa1d934329043.png" style="margin:0;">，可设置列表展示字段，选择完成后，单击**确定**，即可设置成功。
![](https://main.qcloudimg.com/raw/6d589c9c894e2cffa69bbf5661decc85.png)
	- **编辑**：在目标白名单的右侧操作栏，单击**编辑**，可对已创建的白名单进行编辑。
![](https://main.qcloudimg.com/raw/bf735b637fbeb43a762220b4fad3e6af.png)
	- **删除**：在白名单列表中，支持对已配置的白名单进行删除。
		- **方式1**：在目标白名单的右侧操作栏，单击**删除**，确认无误后，即可删除该白名单。
		- **方式2**：全选或勾选需要删除的规则，在规则列表上方，单击**删除**，确认无误后，即可删除选中白名单。
![](https://main.qcloudimg.com/raw/6517915f204ab26d4d5ccd04cc764695.png)
