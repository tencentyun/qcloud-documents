## 环境准备
1. 准备服务器，在服务器上安装其所支持的 Windows 系统（请参见 [环境要求](https://cloud.tencent.com/document/product/1009/39853)），本文以 Windows Server 2012 服务器为例进行说明。
2. 服务器接入企业网络、配置 IP 、配置防火墙策略。
	- 配置 IP：请为 Windows Server 2012 配置固定 IP，根据企业网络 IP 范围进行取值，例如10.10.0.0/24，请分配一个未使用的 IP，例如10.12.90.236。
	- 配置防火墙策略：配置需要放行的端口，配置方式请参见 [基础网络配置](https://cloud.tencent.com/document/product/1009/39926)。
3. 将 [授权获取指引](https://cloud.tencent.com/document/product/1009/39851)  中获取到的安装包，上传到 Windows Server 2012 系统中，可通过 U 盘挂载的方式拷贝。

## 安装过程
1. 将安装包拷贝到 Windows 服务器中后，双击运行 PCMgrEnterprise_xxxx.exe。
<img src="https://main.qcloudimg.com/raw/aa44a0c0d58a0b19f07b9d9346ae60ac.png" />
2. 进入安装界面，选择合适的安装路径，配置完成后，单击【立即安装】，即可开始安装。
	>!
	- 请为安装目录磁盘保留**至少5GB可用空间**，建议保留1T及以上，以供存储更多的补丁和日志数据。
	- 可根据需要，安装页面右上角单击【设置】，配置端口号（默认情况下，无需修改，如有特殊需求，请参见 [基础网络配置](https://cloud.tencent.com/document/product/1009/39926) 进行设置），以及级联部署时的上级控制中心（默认情况下，无级联部署，默认填空即可。如需要级联部署，请参见 [复杂级联部署结构及配置](https://cloud.tencent.com/document/product/1009/39927) 进行设置）。
	- 根据终端机器配置不同，安装过程将持续数分钟至数十分钟，请耐心等待安装完成。
>
![](https://main.qcloudimg.com/raw/35c72c0586b2604cd0f4b3ef153d669b.png)

3. 安装完成后，可通过浏览器输入产品安装所在服务器的地址，即可进入控制中心 Web 页面。
例如，安装服务器的 IP 地址是10.12.90.236，则在浏览器地址栏中输入`http://10.12.90.236`，并单击【回车】，出现以下登录页面，使用默认出厂帐号：admin，密码：admin，进行登录。具体登录链接获取，请参见 [登录及帐号控制](https://cloud.tencent.com/document/product/1009/40015)。
![](https://main.qcloudimg.com/raw/c057bc120491a3508a09e1db9d7a9eb5.png)

## 授权导入
1. 初次登录，系统会提示导入授权文件，单击【导入】，进行授权文件导入操作即可（授权文件申请，请参见 [授权获取指引](https://cloud.tencent.com/document/product/1009/39851)）。
![](https://main.qcloudimg.com/raw/8d01ead486b3d0abd8a28868834132d6.png)
2. 当授权文件导入成功后，可在御点后台控制中心右上角的【产品信息】中，查看授权文件详情。
![](https://main.qcloudimg.com/raw/ac5d5772bfad2af141402cbbbc6ee2f1.png)

## 卸载过程

如果确认不再需要本系统，可执行卸载程序，在安装目录下找到`..\Public\ Uninst.exe`执行卸载即可。

## 服务查看

- 在客户端打开任务管理器，单击服务里的服务与应用程序：DaemonSrv 为御点服务端的服务。
<img src="https://main.qcloudimg.com/raw/eb4c4765eed370cd97eadf8329da8d42.png"  />
- 桌面生成的快捷方式为御点的 web 页面，双击后即可打开御点后台控制中心页面。
![](https://main.qcloudimg.com/raw/c12d37ce73b6735c4f0139fd69de1e39.png)
- 在客户端打开任务管理器，单击任务管理器进程，如下所示，可以看到御点的服务程序已经启动。
<img src="https://main.qcloudimg.com/raw/edcedfc3a617393466e34cc71db0c96e.png"  />
