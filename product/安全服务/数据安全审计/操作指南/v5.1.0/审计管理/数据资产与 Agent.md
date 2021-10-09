## Agent 下载
1. 以 useradmin 账号登录数据安全审计管理页面，在左侧导航栏中，选择**数据资产与Agent** > **审计用Agent**，即可进入审计用 Agent 页面。
2. Agent 部署。在审计用 Agent 页面，选择 **Agent 下载** > **添加**，可配置审计 Agent 的各类参数并提供下载链接，配置步骤以及配置注意事项，请参见 [Agent 部署](https://cloud.tencent.com/document/product/856/17385)。
3. 添加完成 Agent 后，在 Agent 配置页面，可查看所有已正确安装且能实现 DSA 实例网络互通的 Agent 信息。
![](https://main.qcloudimg.com/raw/4cd2fc3a3ce54459c3df060d21b0542d.png)
列表各字段含义如下：
	- Agent 名称：用于配置该 Agent 的名称。
	- 审计服务 IP： Agent 回传数据的源 IP。
	- 审计服务端口：该 Agent 配置的审计端口。
	- 数据库资产：可查看该 Agent 审计的数据库的所有 IP 地址。
	- 操作：用于下载该 Agent 的链接。
		- 在右侧操作栏，选择**下载** > **下载 Linux Agent**或**下载 Windows Agent**，弹出部署 IP 窗口，单击**确定**即可开始下载 Agent 。
>!
>- 若部署机器操作系统 centos 版本号小于7 或者ubuntu 版本号小于11，必须勾选下方说明，否则无法部署 Agent。
>- 请添加安装包需要部署机器的 IP 或 IP 列表。
>- 如未添加 IP 信息却部署了会导致 Agent 无法启动。
>- 如有新的机器要部署请重新下载安装包并填写机器的 IP 信息。
>
![](https://main.qcloudimg.com/raw/3e822fe28ace8d60fe55f610c27169c0.png)
		- 在右侧操作栏，选择**下载** > **Linux 批量部署** ，输入部署地址，支持按 IP 或按 IP 段部署，支持添加多行，输入服务器 IP 、SSH 端口号、用户名、密码， 输入完成后单击**确定**即可。
![](https://main.qcloudimg.com/raw/f5503266981ba5cf40eef4194cd6210a.png)
		- 在右侧操作栏，单击**删除**，可删除该条 Agent 信息。
 	
## Agent 列表
1. 以 useradmin 账号登录数据安全审计管理页面，在左侧导航栏中，选择**审计用 Agent** > **Agent 列表**，即可进入审计列表中。
2. 在审计列表中，可以查看所有已配置的 Agent。Agent 列表默认展示内容包括：Agent 名称、部署 Mac、部署 IP、操作系统、部署时间、最新上报时间、运行状态、开启状态及相关操作。
	- **搜索**：您可以按数据资产、Agent 状态、Agent名称、IP、对 Agent 进行搜索。
	- **查看 Agent 配置详情**：在“操作”栏中，单击**编辑**，可以查看 Agent 配置相关信息。
	- **相关操作**：在右侧操作栏，可以对 Agent 进行启动、停止、编辑、卸载、删除的相关操作。
![](https://main.qcloudimg.com/raw/7353023575bb6a65e1cd4eeb65859f74.png)
