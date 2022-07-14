## 操作场景

本文为您介绍使用 [云函数（Serverless Cloud Function，SCF）](https://cloud.tencent.com/document/product/583) 对日志服务（Cloud Log Service，CLS）日志进行处理。其中，CLS 主要用于日志采集，SCF 主要提供节点计算能力。
数据流程如下：
![](https://main.qcloudimg.com/raw/5225188c50c85b874e8f96bee8ff1bdb.jpg)

## 前提条件
已登录 [日志服务控制台](https://console.cloud.tencent.com/cls)。

## 操作步骤

<span id="step02"></span>

### 创建日志主题

参看 [新增日志主题](https://cloud.tencent.com/document/product/614/41035#.E6.96.B0.E5.A2.9E.E6.97.A5.E5.BF.97.E4.B8.BB.E9.A2.98) 文档，创建两个日志主题。

>? ETL 数据处理的源端和终端均为 CLS，故至少需创建两个主题。
>

<span id="step03"></span>

### 创建云函数 SCF

参看 [通过模板创建函数](https://cloud.tencent.com/document/product/583/56125#.E9.80.9A.E8.BF.87.E6.A8.A1.E7.89.88.E5.88.9B.E5.BB.BA.E5.87.BD.E6.95.B0) 文档，创建函数。
主要配置参数如下：
 - 地域：选择**北京**地域。
 - **函数名称**：命名为 “CLSdemo”。
 - **创建方式**：使用**模板创建**，选择**CLS日志ETL**模板。

> ! 函数需要在**函数配置**页面中，选择和 CLS 相同的 VPC 和子网。如下图所示：
>   ![](https://main.qcloudimg.com/raw/a329381190dcf6ad0883f5f8a51a9567.png)

<span id="step04"></span>

### 配置 CLS 触发器

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls/overview)。
2. 在左侧导航栏中，单击**日志主题**，进入日志主题管理页面。
3. 找到刚创建的日志主题，单击日志主题ID/名称，进入该日志主题详情页面。
4. 在日志主题详情页面，选择**函数处理**页签，单击**创建**。
5. 在弹出的“函数处理”窗口中，添加已创完成的函数，单击**确定**。如下图所示：
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
   在函数详情页面中选择**日志查询**页签，可以看到打印出的日志信息。如下图所示：
   ![](https://main.qcloudimg.com/raw/b4d8dd0a4a236ab4cb35f2e7d3160649.png)
3. 切换至终端 CLS，查看数据处理结果。
>? 您可以根据自身的需求编写具体的数据处理方法。
> 
