## 操作场景

本文为您介绍使用 [云函数 SCF](https://cloud.tencent.com/document/product/583) 对 CLS 日志进行加工处理。其中，CLS 主要用于日志采集，SCF 主要提供数据加工的节点计算能力。
数据流程如下：
![](https://main.qcloudimg.com/raw/5225188c50c85b874e8f96bee8ff1bdb.jpg)

## 操作步骤

<span id="step01"></span>

### 创建日志集

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)，在左侧导航栏中单击【日志集管理】。
2. 进入日志集管理页面，在页面上方选择日志集的地域。
3. 单击【创建日志集】，在弹出的创建日志集窗口中，填写相关信息：
   ![](https://main.qcloudimg.com/raw/52704e1f3bdf6efe4c7e9b266e2ca451.jpg)
4. 单击【确定】，即可创建日志集。

<span id="step02"></span>

### 创建日志主题

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)，在左侧导航栏中单击【日志集管理】。
2. 找到已创建的日志集，在其右侧操作栏中，单击【查看】，进入日志集详情页面。
3. 单击【新增日志主题】，在新增日志主题窗口中，填写如下相关信息：
   - 日志主题名称：例如：nginx。
   - 主题分区（Partition）数量： 主题分区介绍请参见 [主题分区介绍](https://cloud.tencent.com/document/product/614/39259)，默认新建1个分区。
   ![](https://main.qcloudimg.com/raw/8b2da321ec50fce2315395ac067a7605.jpg)
4. 单击【确定】，新增日志主题。
5. 日志主题新增成功，将进入日志主题管理页。
   ![](https://main.qcloudimg.com/raw/08e9dc61f1cc8bfcb1923345c86bef45.jpg)
>? ETL 数据处理的源端和终端均为 CLS，故至少需创建两个 Topic。

<span id="step03"></span>

### 创建云函数 SCF

1. 登录云函数控制台，选择左侧导航栏中的【[函数服务](https://console.cloud.tencent.com/scf/list)】。
2. 在“函数服务”页面上方选择**北京**地域，并单击【新建】进入新建函数页面，配置以下参数：
	- **函数名称**：命名为 “CLSdemo”。
	- **运行环境**：选择 “Python 2.7”。
	- **创建方式**：选择【模板函数】。
	- **模糊搜索**：输入“CLS日志ETL”，并进行搜索。
3. 单击模板中的【查看详情】，即可在弹出的“模板详情”窗口中查看相关信息，支持下载操作。
 <img src="https://main.qcloudimg.com/raw/7510ff0cd7fc0c2a33219a407c06a3a5.png" width="100%">
4. 基本信息配置完成之后，单击【下一步】，进入函数配置页面。
5. 函数配置保持默认配置，单击【完成】，完成函数的创建。
> ! 函数需要在【函数配置】页面中，选择和 CLS 相同的 VPC 和子网。如下图所示：
>   ![](https://main.qcloudimg.com/raw/a329381190dcf6ad0883f5f8a51a9567.png)

<span id="step04"></span>

### 配置 CLS 触发器

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)，在左侧导航栏中单击【日志集管理】。
2. 找到已创建的日志集，在其右侧操作栏中，单击【查看】，进入日志集详情页面。
3. 在日志主题详情页面，选择【函数处理】并单击【新建】。在弹出的“函数处理”窗口中添加已创完成的函数。如下图所示：
![](https://main.qcloudimg.com/raw/ee3aa3a2ca88355e80a415a402c2994f.jpg)
主要参数信息如下，其余配置项请保持默认：
	- **命名空间**：选择函数所在的命名空间。
	- **函数名**：选择 [创建云函数 SCF](#step03) 步骤中已创建的云函数。
	- **别名**：选择函数别名。
	- **最长等待时间**：单次事件拉取的最长等待事件，默认60s。

<span id="step05"></span>

### 测试函数功能

1. 下载 [测试样例](https://main.qcloudimg.com/raw/6e0d4837eefd0ce77dac8a3973acdf39.zip) 中的日志文件，并解压出 demo-scf1.txt，导入至源端 CLS 服务。
2. 切换至 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=8&ns=default)，查看执行结果。
   在函数详情页面中选择【日志查询】页签，可以看到打印出的日志信息。如下图所示：
   ![](https://main.qcloudimg.com/raw/b4d8dd0a4a236ab4cb35f2e7d3160649.png)
3. 切换至终端 CLS 日志服务，查看数据加工结果。
> ?您可以根据自身的需求编写具体的数据加工处理方法。
