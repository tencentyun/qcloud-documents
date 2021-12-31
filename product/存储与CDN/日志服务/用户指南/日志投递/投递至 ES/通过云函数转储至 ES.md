## 操作场景

本文为您介绍如何通过云函数 SCF 将 CLS 日志转储至 Elasticsearch Service（ES）。其中，CLS 主要用于日志采集，SCF 主要提供数据加工的节点计算能力。数据处理流程图请参见 [函数处理概述](https://cloud.tencent.com/document/product/614/49851)。

## 操作步骤

### 新增日志主题

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)。
2. 在左侧导航栏中，单击【日志主题】。
3. 在日志主题管理页面，选择日志主题的地域，单击【创建日志主题】。
4. 在弹出的窗口中，填写如下相关信息：
<img src="https://main.qcloudimg.com/raw/c5d0a78b1ca47d8c17e88d6160e1da97.png" style="width: 50%" /></br>
 - 日志主题名称：例如：nginx。
 - 分区（Partition）数量： 默认新建1个分区。关于主题分区请参见 [主题分区介绍](https://cloud.tencent.com/document/product/614/39259)。
 - 分区自动分裂：默认开启。
 - 最大分裂数量：可自定义分裂数量，最大分裂数量为50个。
 - 日志集操作：
    - 选择现有日志集：在日志集下拉框中选择目标日志集，日志保存时间为日志集保存时间。
    - 创建日志集：
      - 日志集名称：例如 cls_test。
      - 日志保存时间：默认为30天，可自定义设置日志存储时间。
5. 单击【确定】，即可创建日志主题。
日志主题新增成功后，可在日志管理页面单击日志主题ID/名称，查看日志主题的详情信息。
![](https://qcloudimg.tencent-cloud.cn/raw/b5cb91dbc1d0f3b19cc2f87d3650e2c5.png)

>?
>- 若收集云服务器或其他云产品日志，日志服务地域建议选择相同地域。
>- 日志集一旦创建，地域属性将无法修改。
>- 日志保存时间仅支持存储1 - 366天的日志记录。若需更长保存时间，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们。
>

### 创建云函数 SCF

1. 登录云函数控制台，选择左侧导航栏中的【[函数服务](https://console.cloud.tencent.com/scf/list)】。
2. 在“函数服务”页面上方选择**北京**地域，并单击【新建】进入新建函数页面，配置以下参数：
- **函数名称**：命名为 “CLSdemo”。
- **运行环境**：选择 “Python 2.7”。
- **创建方式**：选择【模板函数】。
- **模糊搜索**：输入“CLS 消息转储至 ES”，并进行搜索。
3. 单击模板中的【查看详情】，即可在弹出的“模板详情”窗口中查看相关信息，支持下载操作。
![](https://main.qcloudimg.com/raw/dd8e76ba274ee692d67541c8f66ae9fa.png)
4. 基本信息配置完成之后，单击【下一步】，进入函数配置页面。
5. 函数配置保持默认配置，单击【完成】，完成函数的创建。
> ! 函数需要在【函数配置】页面中，选择和 CLS 相同的 VPC 和子网。如下图所示：
> ![](https://main.qcloudimg.com/raw/a329381190dcf6ad0883f5f8a51a9567.png)
> 

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

### 测试函数功能

1. 下载 [测试样例](https://main.qcloudimg.com/raw/6e0d4837eefd0ce77dac8a3973acdf39.zip) 中的日志文件，并解压出 demo-scf1.txt，导入至源端 CLS 服务。
2. 切换至 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=8&ns=default)，查看执行结果。
在函数详情页面中选择【日志查询】页签，可以看到打印出的日志信息。如下图所示：
![](https://main.qcloudimg.com/raw/b4d8dd0a4a236ab4cb35f2e7d3160649.png)
3. 切换至 [Elasticsearch Service 控制台](https://console.cloud.tencent.com/es)，查看数据转储及加工结果。
> ?您可以根据自身的需求编写具体的数据加工处理方法。
