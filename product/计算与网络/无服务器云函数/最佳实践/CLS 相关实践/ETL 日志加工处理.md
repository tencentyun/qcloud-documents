## 操作场景

本文为您介绍使用 [云函数 SCF](https://cloud.tencent.com/document/product/583) 对 CLS 日志进行加工处理。其中，CLS 主要用于日志采集，SCF 主要提供数据加工的节点计算能力。
数据流程如下：
![](https://main.qcloudimg.com/raw/a85af098f1795b522140a6a4fadac0a6.svg)

## 操作步骤

[](id:step01)
### 创建日志集和主题
1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)，在左侧导航栏中单击**日志主题**。
2. 进入日志集管理页面，在页面上方选择日志集的地域。
3. 单击**创建日志主题**，在弹出的创建日志集窗口中，填写相关信息：
      - 日志主题名称：例如 project_test
      - 日志集名称：例如 nginx
![](https://main.qcloudimg.com/raw/6e2ff86cd07c0e132bee42850dfa678f.png)
4. 单击**确定**，即可创建日志集和主题。
5. 日志主题新增成功，将进入日志主题管理页，如下图所示：
      ![](https://main.qcloudimg.com/raw/14416fdbda5ac39e4a650d1e37a5118c.png)
   
>? ETL 数据处理的源端和终端均为 CLS，故至少需创建两个 Topic。

[](id:step03)

### 创建云函数 SCF

1. 登录云函数控制台，选择左侧导航栏中的 **[函数服务](https://console.cloud.tencent.com/scf/list)**。
2. 在“函数服务”页面上方选择**北京**地域，并单击**新建**进入新建函数页面，配置以下参数：
	- **函数名称**：命名为 “CLSdemo”。
	- **运行环境**：选择 “Python 2.7”。
	- **创建方式**：选择**模板函数**。
	- **模糊搜索**：输入“CLS日志ETL”，并进行搜索。
3. 单击模板中的**查看详情**，即可在弹出的“模板详情”窗口中查看相关信息，支持下载操作。
 <img src="https://main.qcloudimg.com/raw/e0cfb537bc59933a254b4bcc1c67c458.png" width="100%">
4. 基本信息配置完成之后，单击**下一步**，进入函数配置页面。
5. 函数配置保持默认配置，单击**完成**，完成函数的创建。


[](id:step04)

### 配置 CLS 触发器

1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf/index?rid=1)，选择左侧导航栏中的**函数服务**。
2. 在“函数服务”列表页面上方，选择期望配置 CLS 触发器的函数所在的地域及命名空间。
3. 单击函数名，进入该函数的详情页面。
4. 在该函数的详情页面，选择左侧的**触发管理**，进入触发器浏览及操作界面，单击**创建触发器**，开始创建一个新的触发器。
5. 在弹出的“创建触发器”窗口中添加已创建的函数。如下图所示：
![](https://main.qcloudimg.com/raw/f14b4d014c955731b0ee5eef8323e9a1.png)
6. 完成触发器配置后，单击**提交**，完成触发器创建。

[](id:step05)

### 测试函数功能

1. 下载 [测试样例](https://main.qcloudimg.com/raw/6e0d4837eefd0ce77dac8a3973acdf39.zip) 中的日志文件，并解压出 demo-scf1.txt，导入至源端 CLS 服务。
2. 切换至 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=8&ns=default)，查看执行结果。
   在函数详情页面中选择**日志查询**页签，可以看到打印出的日志信息。如下图所示：
   ![](https://main.qcloudimg.com/raw/b4d8dd0a4a236ab4cb35f2e7d3160649.png)
3. 切换至终端 CLS 日志服务，查看数据加工结果。
> ?您可以根据自身的需求编写具体的数据加工处理方法。
