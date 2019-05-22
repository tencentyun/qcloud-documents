考虑到数据的安全，目前 TencentDB for SQL Server 尚未开放实例的外网 IP，但有需求的用户可以利用 SSH2 的端口映射在外网连接实例，并对其进行配置和管理，操作步骤非常简单，可按照以下步骤操作：
1. 准备一台具有外网 IP 的 Linux 云主机
2. 在本地使用 SSH 工具（如 SecureCRT 或 PuTTY 等）配置端口映射，在本地启动一个服务端口，然后使用 SSH 工具与 linux 服务器建立连接，即可使用 SSMS 连接本地的服务端口
![](//mccdn.qcloud.com/static/img/3f9a661b42fed1648d8b00091d5ace60/image.png)

**以 SecureCRT 为例：**
1.	进入会话属性设置，并单击添加
![](//mccdn.qcloud.com/static/img/072a1ba13c5281b206d70e7ce5294c17/image.png)
2.	进入会话属性设置页面，配置相应的参数
![](//mccdn.qcloud.com/static/img/edf3d44003eda115015002d28bd98266/image.png)
3.	登录该 Linux 云主机，建立连接
4.	使用 SSMS 连接 SQL Server 实例
![](//mccdn.qcloud.com/static/img/0a25f830093d59d77a2b74f5c3d3e769/image.png)
