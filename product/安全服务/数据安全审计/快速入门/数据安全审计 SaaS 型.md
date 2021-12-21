本文将为您介绍如何快速使用数据安全审计 SaaS 型。
## 前提条件
已购买 [数据安全审计SaaS型](https://cloud.tencent.com/document/product/856/64697)。
已完成配置数据资产实例，操作详情请参见 [管理自建数据库]()。

## 步骤1：同步数据资产
1. 登录 [数据安全审计控制台](https://console.cloud.tencent.com/dsgc/dsaudit)，单击**立即进入**。
![](https://qcloudimg.tencent-cloud.cn/raw/8d656cb1a704ecdf9d3f54f261a8a10b.png)
2. 进入数据安全审计服务之后，单击侧边栏的**数据资产**，进入数据资产页面。
![](https://qcloudimg.tencent-cloud.cn/raw/7fe7c7a5c58ab1b91fd1cfc7d6599be4.png)
3. 通过单击**更新资产列表**拉取云数据库列表，也可使用自建数据库的添加数据资产功能，当需要审计腾讯云外的数据资产时，可在腾讯云外数据库添加。
4. 添加数据库后，可通过单击对应数据库后面的![](https://qcloudimg.tencent-cloud.cn/raw/d3638827e13e926286f7fee006ba8801.png)，开启审计权限，允许数据安全审计采集其日志进行安全分析。
![](https://qcloudimg.tencent-cloud.cn/raw/1c140874a233d33bce9cc6e8e23ee18e.png)
>!
>- 开启审计权限将消耗 License 授权资产数。
>- 部分操作需要用户授权，只需按提示操作即可。


## 步骤2： 部署 Agent

数据安全审计部署的核心目标是把 Agent 安装到数据库服务器或访问数据库的应用服务器中。
#### Agent 程序部署位置
根据所添加的数据库在云环境中的实际部署方式，您需要将 Agent 程序部署在以下位置：
 - 云服务器自建数据库：Agent 程序需要部署在数据库所在的云服务器上。
 - 云数据库：Agent 程序需要部署在对应的应用服务器上，通常为访问数据库的应用系统所在服务器。

#### 配置数据资产方式
 - 腾讯云内网 Agent：确保部署 Agent 的 VPC 已在 VPC 通道列表中，添加该 VPC 的资产即可自动创建VPC通道。
 - 腾讯云外 Agent：需要开通白名单，腾讯云外 Agent 才能正常上报流量。请 [联系我们](https://cloud.tencent.com/online-service) 协助开通。   


### Agent 下载
1. 登录 [数据安全审计控制台](https://console.cloud.tencent.com/dsaudit)，在左侧导航栏中，单击**配置管理** > **Agent 管理** > **Agent 部署**，进入 Agent 部署页面。
2. 在 Agent 部署页面，选择下载 Linux Agent、下载 Windows Agent 进行配置 Agent。

### Agent 安装
下载 Agent 完成后，需要将 Agent 安装在相应服务器上才能实现审计效果。
- 如果您使用的是云服务器 + 自建数据库模式，则建议您将 Agent 安装在数据库服务器上。
- 如果您使用的是云数据库，则需要在连接数据库的应用服务器上安装 Agent。

#### Linux 版本
1. 将 `dsaagent_innernet_linux _xxx.zip` 安装包上传到需要安装的机器上，如 /data。
2. 使用 `unzip dsaagent_innernet_xxx.zip` 命令进行解压，得到 /data/CapAgent 目录。
3. 执行 `cd CapAgent/bin`，再执行`./start.sh`，结果如下。
![](https://qcloudimg.tencent-cloud.cn/raw/81b0f1add2be91ed9930ced33b975d39.png)
4. 在命令行，执行 `netstat -ano | grep 7000` 如下图即确认连接成功。
![](https://qcloudimg.tencent-cloud.cn/raw/cb7d4975c71891640172832428d420d7.png)

#### Windows 版本
数据安全审计 Agent Windows 版本只支持 **Windows vista/2008 及以上版本**。
1. 下载 Windows 版本 Agent 后，解压到安装目录。
2. 进入 CapAgent下的 bin 目录，执行. start.bat。
3. 执行成功后，Console 显示结果如下图所示。同时，可以在任务管理器中，看到 CapAgentForWin.exe 进程。
![](https://qcloudimg.tencent-cloud.cn/raw/d7bfc6e6d21ac23cbb2fd9e35f146d26.png)
4. 检查CapAgentForWin成功启动并连接审计服务成功。
i. 在任务管理器中确认 CapAgentForWin 进程已运行。
![](https://qcloudimg.tencent-cloud.cn/raw/5ebac0aaadfc5ceaa350f14c1fd04062.png)
ii. 在 cmd 控制台，执行 `netstat -ano | findstr 7000`，如下图即确认连接成功。
![](https://qcloudimg.tencent-cloud.cn/raw/0fa3c0a35ba97567d719d44f0782cbcd.png)
5. Agent 停止。
在 CapAgent_win/bin 目录下执行 stop.bat 即可。


## 步骤3：配置审计规则
1. 在 **[审计规则](https://console.cloud.tencent.com/dsaudit/rule)** > **规则列表**页面，可查看系统中的审计规则，若内置规则无法满足您的特定需要，您可以单击**新建**创建自定义规则。
![](https://qcloudimg.tencent-cloud.cn/raw/e0cef05f6f25ef6b459ffc8b8852b686.png)
2. 单击**规则启用**，进入规则启用页面，选择数据资产，为其启用需要的审计规则。
![](https://qcloudimg.tencent-cloud.cn/raw/57607f148276a893738fb00ca4e46b3d.png)


## 步骤4：查看审计日志
1. 完成以上配置后，在 [审计日志](https://console.cloud.tencent.com/dsaudit/log) 页面，可查看数据库的操作日志。
![](https://qcloudimg.tencent-cloud.cn/raw/ef4f3fadafe426e2bdeb4aebb30a33d5.png)
2. 在 [审计风险](https://console.cloud.tencent.com/dsaudit/risk) 页面，可查看发现的数据安全风险，安全管理人员可根据风险提示，判断是否需要采取进一步措施。
![](https://qcloudimg.tencent-cloud.cn/raw/bb22bea5912ec790ce9d5033ff06dbda.png)
