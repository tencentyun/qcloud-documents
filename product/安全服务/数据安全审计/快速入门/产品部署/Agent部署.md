数据安全审计部署的核心目标是把 Agent 安装到数据库服务器或访问数据库的应用服务器中，并且确保数据库服务器或访问数据库的应用服务器，与数据安全审计的审计实例能实现网络连通。
Agent 部署流程如下图所示，其中前五步为参数配置操作：
![0](https://main.qcloudimg.com/raw/a8ad2c956f3d8f53b55df06b56749e9c.png)
## Agent 程序部署位置
根据所添加的数据库在云环境中的实际部署方式，您需要将 Agent 程序部署在以下位置：
- 云服务器自建数据库：Agent 程序需要部署在数据库所在的云服务器上。
- 云数据库 TencentDB：Agent 程序需要部署在对应的应用服务器上，通常为访问数据库的应用系统所在服务器。

## 编辑 Agent 配置

1. 已完成 [控制台登录](https://cloud.tencent.com/document/product/856/17381) 操作后，通过 sysadmin 账号登录数据安全审计管理页面（默认密码在购买时将通过站内信发送），在左侧导航中，选择【Agent 管理】>【Agent 配置】，在 Agent 配置页面单击【配置 Agent】，进入编辑 Agent 配置页面。
![](https://main.qcloudimg.com/raw/3268da84fb9a7b4b14b04f45624ca699.png)
<span id="ip"></span>
2. 在编辑 Agent 配置页面，编辑审计服务 IP及审计端口，审计服务 IP 指定了 Agent 数据安全审计实例的 IP 地址。
 - 若您仅有一个数据安全审计且与被审计数据库在同一个地域，则只填写数据安全审计实例内网 IP 地址即可。
 - 若您有多个数据安全审计实例，请设置与被审计数据库同一地域的数据安全审计实例内网 IP。
 ![](https://main.qcloudimg.com/raw/d1b9d13f6a23526322bba0609bfe962c.png)
3. 在编辑 Agent 配置页面设置数据库信息，数据库信息帮助 Agent 准确识别流量中与数据库访问相关的会话，数据库信息提供 IP 列表和自动检测两种输入方式。
	- **IP 列表**：IP 列表需要管理员输入完整的数据库 IP 和开发端口，因此 Agent 无论安装在数据库服务器还是应用服务器上，都能够准确定位数据库访问流量。
>!Agent 将只对填入的 IP 和端口进行审计，若漏填 IP 将导致审计日志缺失。
>
![](https://main.qcloudimg.com/raw/74668117776b390c1a838de6186bc849.png)
	- **自动检查**：Agent 若安装在数据库服务器上，可以自动遍历数据库服务器网卡，根据端口来判断开放了数据库服务的 IP ，以此定位 Agent 需要检测的 IP 流量。此类模式仅需填写数据库开放服务的端口：
![](https://main.qcloudimg.com/raw/ce55e41bc2273d90c4fc240aa1ae30e0.png)
4. 在编辑 Agent 配置页面，设置审计 IP 范围。审计 IP 范围可设置 Agent 审计的源 IP 段，数据安全审计支持全量审计和范围审计。您可根据需求通过添加、删除、修改等操作进行设置。
 - **范围审计**：若只希望部分 IP 段的访问操作不被记录，则可设置审计 IP 范围。
 - **全量审计**：默认审计 IP 范围为0.0.0.0 - 255.255.255.255，即全网段审计。
 
![](https://main.qcloudimg.com/raw/af3d6e407b3d8819332d585efb7dad75.png)
5. 设置停止审计阈值。若被审计数据库因性能导致濒临宕机，可以通过关闭更多服务和进程缓解宕机情况。您可以设置一个基于 CPU 与内存使用率的阈值，当被审计数据库超过阈值时，Agent 将发送告警信息并停止工作，缓解数据库的性能压力。
>!如您要求 Agent 任何情况都进行工作，可将负载检测开关关闭，Agent 将持续审计数据。
>
![6](https://main.qcloudimg.com/raw/bc4e60fe5c85232c44bedf97a6485f3a.png)
6. 下载 Agent。所有配置完成后，单击【配置并下载 Agent】，即可下载您设置好的 Agent 了。

## Agent 安装
下载 Agent 完成后，需要将 Agent 安装在相应服务器上才能实现审计效果。
- 如果您使用的是云服务器 + 自建数据库模式，则建议您将 Agent 安装在数据库服务器上。
- 如果您使用的是 TencentDB，则需要在连接数据库的应用服务器上安装 Agent。

部署前确认 Agent 部署的机器和审计服务网络是否连通，使用 telnet 审计服务 IP 7000  （审计服务 IP 为 Agent 配置时审计服务 [分配的 IP](#ip)），如下图所示，表示网络已经连通，如有问题请 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=517&level2_id=727&source=0&data_title=%E5%85%B6%E4%BB%96%E8%85%BE%E8%AE%AF%E4%BA%91%E4%BA%A7%E5%93%81&level3_id=729&radio_title=%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5&queue=3232&scene_code=17784&step=2) 联系我们。
![](https://main.qcloudimg.com/raw/eab4cefe9c9c88c22e53de7b79254cba.png)
### Linux 版本
1.  将 CapAgent_xxx.zip 安装包上传到需要安装的机器上，如 /data 目录。
2.  使用`unzip CapAgent_xxx.zip`命令进行解压，得到 /data/CapAgent 目录。
3.  执行命令`chmod -R 755 CapAgent`。
4. 执行`cd CapAgent/bin`，再执行`./start.sh`，结果如下，如未得到以下结果，请 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=517&level2_id=727&source=0&data_title=%E5%85%B6%E4%BB%96%E8%85%BE%E8%AE%AF%E4%BA%91%E4%BA%A7%E5%93%81&level3_id=728&radio_title=%E5%8A%9F%E8%83%BD%E5%92%A8%E8%AF%A2&queue=3&scene_code=17783&step=2) 联系我们。
 ![7](https://main.qcloudimg.com/raw/2a2d4a87638c95f01da0df14a7fa053a.png)
5. 在命令行，执行`netstat -ano | grep 7000`如下图即确认连接成功。
![](https://main.qcloudimg.com/raw/a7762658df48cbf24ddccdadc913003b.png)

### Windows 版本
>!数据安全审计 Agent Windows 版本只支持 Windows vista/2008 及以上版本。
>
1. 下载 Windows 版本 Agent 后，解压到安装目录，进入 “CapAgent/conf” 目录，修改 config.ini 中 device 配置为本机访问数据库网卡的 IP（一般为内网 IP），如下图所示：
![](https://main.qcloudimg.com/raw/6bdcb038c6f9362390828c93fe81b023.png)
2. 进入 CapAgent_win 目录，执行文件夹中 AuditCapAgentSteup.exe 程序依次安装 Python3.8 环境、npcap0.9984、执行 CapAgent_win。 
![](https://main.qcloudimg.com/raw/8a8c6a51f86f56957a06d4958739ccfa.png)
  1. 安装 Python3.8 环境，单击【下一步】，选择 Python3.8 安装的位置，单击【安装】。
  ![](https://main.qcloudimg.com/raw/4a8f10fe38a4b235d0c7002aece4ca96.png)
 2. 安装 Npcap0.9984，勾选全部，单击【Install】。
 ![](https://main.qcloudimg.com/raw/8c8caa52b579fd3bed6505337d6c721c.png)
3. 执行成功后，Console 显示结果如下图所示。同时，可以在任务管理器中，看到 CapAgentForWin.exe 进程。
![](https://main.qcloudimg.com/raw/92974ca82bfbdca31856679bd96e9c68.png)
4. 检查 CapAgent_win 成功启动并连接审计服务成功。
	- 在任务管理器中确认 CapAgent_win 进程已运行，
![](https://main.qcloudimg.com/raw/80a15aaa41765a8fd6cc5d6b90e47e2c.png)
	- 在 cmd 控制台，执行`netstat -ano | findstr 7000`，如下图即确认连接成功。
	![](https://main.qcloudimg.com/raw/7ddc1fc5c52c35ad938418e14b12dd43.png)
5. Agent 停止。
在 CapAgent_win/bin 目录下执行 stop.bat 即可。
