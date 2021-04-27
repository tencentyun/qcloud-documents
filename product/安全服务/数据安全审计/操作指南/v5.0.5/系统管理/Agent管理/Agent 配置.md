配置 Agent 后可将 Agent 部署在 Linux 系统或 Windows 系统，进行具体审计组配置后，实现对数据库操作的管理。
## 操作步骤
1. 登录 [数据安全审计控制台](https://console.cloud.tencent.com/cds/audit)，找到需要操作的审计系统，单击【管理】，进入数据安全审计管理系统登录界面。 
![](https://main.qcloudimg.com/raw/58e92bf681bdc797d2978ba51775b30e.png) 
2. 以 sysadmin 账号登录数据安全审计管理页面，在左侧导航栏中，选择【Agent 管理】>【Agent 配置】，即可进入 Agent 配置页面。
>?如忘记登录密码，可以 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=517&level2_id=727&source=0&data_title=%E5%85%B6%E4%BB%96%E8%85%BE%E8%AE%AF%E4%BA%91%E4%BA%A7%E5%93%81&level3_id=729&radio_title=%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5&queue=15&scene_code=17784&step=2) 找回密码。 
> 
3. Agent 部署。在 Agent 配置页面，单击【配置 Agent】，可配置审计 Agent 的各类参数并提供下载链接。
4. 配置 Agent。配置 Agent 用于展示所有已正确安装且能实现 DSA 实例网络互通的 Agent 信息。
![](https://main.qcloudimg.com/raw/ea099f2ea5c41c023c6ee52a0e1faa71.png)
列表各字段含义如下：
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
		- 单击【Linux 批量部署】 ，输入部署地址，支持按 IP 或按 IP 段部署，支持添加多行，输入服务器 IP 、SSH 端口号、用户名、密码， 输入完成后单击【确定】即可。
![](https://main.qcloudimg.com/raw/95a28667e75dce962ce3b2ae747c9c20.png)
