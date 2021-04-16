本文档将为您介绍如何部署审计 Agent，并指导您操作审计列表。
## Agent 配置
1. 登录 [数据安全审计控制台](https://console.cloud.tencent.com/cds/audit)，找到需要操作的审计系统，单击【管理】，进入数据安全审计管理系统登录界面。 
![](https://main.qcloudimg.com/raw/58e92bf681bdc797d2978ba51775b30e.png) 
2. 以 useradmin 账号登录数据安全审计管理页面，在左侧导航栏中，选择【数据资产与 Agent】>【审计用 Agent】，即可进入审计用 Agent 页面。
3. Agent 部署。在审计用 Agent 页面，选择【Agent 配置】>【添加 Agent】，可配置审计 Agent 的各类参数并提供下载链接，配置步骤以及配置注意事项，请参见 [Agent 部署](https://cloud.tencent.com/document/product/856/17385)。
4. 添加完成 Agent 后，在 Agent 配置页面，可查看所有已正确安装且能实现 DSA 实例网络互通的 Agent 信息。
![](https://main.qcloudimg.com/raw/9a16918f26f9d8ea3ddeb53981c929c8.png)
列表各字段含义如下：
	- Agent 名称：用于配置该 Agent 的名称。
	- 审计服务 IP： Agent 回传数据的源 IP。
	- 审计服务端口：该 Agent 配置的审计端口。
	- 数据库 IP：单击 【详情】 可查看该 Agent 审计的数据库的所有 IP 地址。
	- 审计 IP：用于显示该 Agent 配置的审计范围，由于 IP 范围内容较多，可单击 【详情】 进行阅览。
	- 操作：用于下载该 Agent 的链接。
		- 单击【下载 Linux Agent】或【下载 Windows Agent】，弹出部署 IP 窗口，可以按 IP 部署或按 IP 段部署（IP 段支持全段审计），单击【确定】即可开始下载 Agent 。
>!
>- 若部署机器操作系统 centos 版本号小于7 或者ubuntu 版本号小于11，必须勾选下方说明，否则无法部署 Agent。
>- 请添加安装包需要部署机器的 IP 或 IP 列表。
>- 如未添加 IP 信息却部署了会导致 Agent 无法启动。
>- 如有新的机器要部署请重新下载安装包并填写机器的 IP 信息。
>
![](https://main.qcloudimg.com/raw/3e822fe28ace8d60fe55f610c27169c0.png)
		- 单击【删除】，可删除该条 Agent 信息。
 	
## 审计列表
1. 登录 [数据安全审计控制台](https://console.cloud.tencent.com/cds/audit)，找到需要操作的审计系统，单击【管理】，进入数据安全审计管理系统登录界面。 
![](https://main.qcloudimg.com/raw/58e92bf681bdc797d2978ba51775b30e.png) 
2. 以 useradmin 账号登录数据安全审计管理页面，在左侧导航栏中，选择【审计用 Agent】>【审计列表】，即可进入审计列表中。
3. 在审计列表中，可以查看所有已配置的 Agent。审计列表默认展示内容包括：deployMac、部署服务器 IP、审计服务、部署状态、Agent 状态、系统类型、部署时间运行时长及相关操作。
	- **搜索**：您可以按照部署状态、Agent 状态、审计服务 IP、Port（端口）对 Agent 进行搜索。。
	- **查看 Agent 配置详情**：在“审计服务”栏中，单击【Agent 配置详情】，可以查看 Agent 配置相关信息。
	- **相关操作**：在右侧操作栏，可以对 Agent 进行启动、停止、卸载、删除的相关操作。
![](https://main.qcloudimg.com/raw/31018efa7d99d3d9210154d485e04350.png)
