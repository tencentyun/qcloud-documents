数据安全审计部署的核心目标是把 Agent 安装到数据库服务器或访问数据库的应用服务器中。Agent 部署流程如下所示：
<dx-steps>
-配置数据资产实例，操作详情请参见 [管理自建数据库](https://cloud.tencent.com/document/product/856/66075#since)。
-开启审计权限，操作详情请参见 [管理云数据库](https://cloud.tencent.com/document/product/856/66075#cloud)。
-部署 Agent，支持在线部署或下载 Agent。
-Agent 安装。
</dx-steps>

## Agent 程序部署位置
根据所添加的数据库在云环境中的实际部署方式，您需要将 Agent 程序部署在以下位置：
 - 云服务器自建数据库：Agent 程序需要部署在数据库所在的云服务器上。
 - 云数据库：Agent 程序需要部署在对应的应用服务器上，通常为访问数据库的应用系统所在服务器。
 -  Linux 在线部署：对于腾讯云内网的 Linux 系统，推荐使用在线部署。
 
>!
>- 腾讯云内网 Agent：确保部署 Agent 的 VPC 已在 VPC 通道列表中，添加该 VPC 的资产即可自动创建 VPC 通道。
>- 腾讯云外 Agent：需要开通白名单，腾讯云外 Agent 才能正常上报流量。请 [联系我们](https://cloud.tencent.com/online-service) 协助开通。  


 
## 部署 Agent
### 在线部署
1. 登录 [数据安全审计控制台](https://console.cloud.tencent.com/dsaudit)，在左侧导航栏中，单击**配置管理** > **Agent 管理** > **Agent 部署**，进入 Agent 部署页面。
1. 在 Agent 部署页面，单击 **Linux 在线部署**。
2. 在 Agent 在线部署页面，选择 CVM 所在的地域和 VPC ，在需要部署 Agent 的 CVM 后单击**部署**，即可自动部署 Agent 。已经部署的 Agent ，可执行卸载操作（即使 Agent 未连接，在此也可以在线卸载）。还可以选中多个 CVM ，进行批量部署。
>!
>- 在线部署暂时仅支持腾讯云内网的 Linux 操作系统。
>- 使用在线部署的前提是该 CVM 实例已安装 [自动化助手](https://cloud.tencent.com/document/product/1340/51945)。
>
![](https://qcloudimg.tencent-cloud.cn/raw/2947b081fffc641399f94e37ca6e15c7.png)

### 下载 Agent 
1. 登录 [数据安全审计控制台](https://console.cloud.tencent.com/dsaudit)，在左侧导航栏中，单击**配置管理** > **Agent 管理** > **Agent 部署**，进入 Agent 部署页面。
2. 在 Agent 部署页面，选择下载 Linux Agent 或 Windows Agent。
>!Agent 安装包已通过文件名区分部署场景，在部署前仔细检查，避免出错。
>  - 如 dsaagent_innernet_linux _xxx.zip 是腾讯云内网 Linux Agent。
>  - 如 dsaagent_outnet_win_xxx.zip 是腾讯云外 Windows Agent。
>  

## Agent 安装
下载 Agent 完成后，需要将 Agent 安装在相应服务器上才能实现审计效果。
- 如果您使用的是云服务器 + 自建数据库模式，则建议您将 Agent 安装在数据库服务器上。
- 如果您使用的是云数据库，则需要在连接数据库的应用服务器上安装 Agent。

### Linux 版本
>! Linux 需在部署 Agent 之前，安装 python2。
>
1. 将 `dsaagent_innernet_linux _xxx.zip` 安装包上传到需要安装的机器上，如 /data。
2. 使用 `unzip dsaagent_innernet_xxx.zip` 命令进行解压，得到 /data/CapAgent 目录。
3. 执行 `cd CapAgent/bin`，再执行`./start.sh`，结果如下。
![](https://qcloudimg.tencent-cloud.cn/raw/81b0f1add2be91ed9930ced33b975d39.png)
4. 在命令行，执行 `netstat -ano | grep 7000` 如下图即确认连接成功。
![](https://qcloudimg.tencent-cloud.cn/raw/d65b0aa4dd658b6708907e344a8f1391.png)

### Windows 版本
数据安全审计 Agent Windows 版本只支持 Windows vista/2008 及以上版本。
1. 下载 Windows 版本 Agent 后，解压到安装目录。
2. 进入 CapAgent下的 bin 目录，执行 `start.bat`。
3. 执行成功后，Console 显示结果如下图所示。同时，可以在任务管理器中，看到 CapAgentForWin.exe 进程。
![](https://qcloudimg.tencent-cloud.cn/raw/d7bfc6e6d21ac23cbb2fd9e35f146d26.png)
4. 检查 CapAgentForWin 是否成功启动并连接审计服务成功。
i. 在任务管理器中确认 CapAgentForWin 进程已运行。
![](https://qcloudimg.tencent-cloud.cn/raw/5ebac0aaadfc5ceaa350f14c1fd04062.png)
ii. 在 cmd 控制台，执行 `netstat -ano | findstr 7000`，如下图即确认连接成功。
![](https://qcloudimg.tencent-cloud.cn/raw/9fe339420cdd09b4ff0a94f90e844d1f.png)
>?如果 CapAgentForWin 不能运行或 `netstat -ano | findstr 7000` 命令执行不成功，请  [联系我们](https://cloud.tencent.com/online-service) 获得支持。
5. Agent 停止。
在 CapAgent_win/bin 目录下执行 stop.bat 即可。
