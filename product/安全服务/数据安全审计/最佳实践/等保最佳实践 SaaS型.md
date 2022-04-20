为助力企业等保合规，本文为您介绍数据安全审计 SaaS 型各能力与等保相关条款的对应关系，以便有针对性地提供佐证材料。
>?若您使用的是数据安全审计传统型，请参见 [数据安全审计传统型](https://cloud.tencent.com/document/product/856/63886) 文档。

## 前提条件
已购买 [数据安全审计 SaaS 型](https://cloud.tencent.com/document/product/856/17379)，并按照 [快速入门](https://cloud.tencent.com/document/product/856/64700) 完成产品初始化和部署工作。

## 等保二级
**a) 应启用安全审计功能，审计覆盖到每个用户，对重要的用户行为和重要安全事件进行审计；**

本条款主要考察如下三点：
- **是否开启了安全审计功能**
  1. 登录 [数据安全审计控制台](https://console.cloud.tencent.com/cds/audit)，显示立即进入，表明已经完成产品购买。
  ![](https://qcloudimg.tencent-cloud.cn/raw/bef6d8fa05236237600a79625064c03b.png)
  2. 单击**立即进入**，跳转至数据安全审计概览页。可以查看到产品服务状态及资产安全概况，证明产品已正常运行。
![](https://qcloudimg.tencent-cloud.cn/raw/ad227cc784d2fc3bc005538312b0f307.png)

- **审计范围是否覆盖到每个用户**
在 [审计日志页面](https://console.cloud.tencent.com/dsaudit/log)，可以审计到每个用户名。
![](https://qcloudimg.tencent-cloud.cn/raw/7fc572cff390f0a0801c8e459b1bf592.png)

- **是否对重要的用户行为和重要安全事件进行审计**
通过 [审计日志](https://console.cloud.tencent.com/dsaudit/log) 或 [审计风险](https://console.cloud.tencent.com/dsaudit/risk) 页面，可以筛选风险等级（即重要的用户行为和重要安全事件）查看日志。
![](https://qcloudimg.tencent-cloud.cn/raw/484009d2cca1b86dbc823e78d9d73acf.png)


**b) 审计记录应包括事件的日期和时间、用户、事件类型、事件是否成功及其他与审计相关的信息；**

在 [审计日志页面](https://console.cloud.tencent.com/dsaudit/log)，单击任意一条日志后方的**操作**，弹出审计日志详情，可以查看相关的信息。
![](https://qcloudimg.tencent-cloud.cn/raw/0e81c6b176b832d0c33942b25ffde81e.png)

**c) 应对审计记录进行保护，定期备份，避免受到未预期的删除、修改或覆盖等。**

数据安全审计 SaaS 型的审计日志存储于腾讯云 Elasticsearch Service，通过多可用区部署、定期备份方式保证数据可用性。可在概览页的服务状态栏，存储空间的详情说明中查看存储机制及预计可继续存储时长。


**其他：《网络安全法》要求网络日志保留六个月以上。**

在 [审计日志页面](https://console.cloud.tencent.com/dsaudit/log)，选中**近半年**，可以查看近六个月的日志。
![](https://qcloudimg.tencent-cloud.cn/raw/0683adbbfbadb8b16e81774082d2b7f4.png)


## 等保三级
**a) 应启用安全审计功能，审计覆盖到每个用户，对重要的用户行为和重要安全事件进行审计；**

本条款主要考察如下三点：
- **是否开启了安全审计功能**
  1. 登录 [数据安全审计控制台](https://console.cloud.tencent.com/cds/audit)，显示立即进入，表明已经完成产品购买。
  ![](https://qcloudimg.tencent-cloud.cn/raw/bef6d8fa05236237600a79625064c03b.png)
  2. 单击**立即进入**，跳转至数据安全审计概览页。可以查看到产品服务状态及资产安全概况，证明产品已正常运行。
![](https://qcloudimg.tencent-cloud.cn/raw/ad227cc784d2fc3bc005538312b0f307.png)


- **审计范围是否覆盖到每个用户**
在 [审计日志页面](https://console.cloud.tencent.com/dsaudit/log)，可以审计到每个用户名。
![](https://qcloudimg.tencent-cloud.cn/raw/7fc572cff390f0a0801c8e459b1bf592.png)


- **是否对重要的用户行为和重要安全事件进行审计**
通过 [审计日志](https://console.cloud.tencent.com/dsaudit/log) 或 [审计风险](https://console.cloud.tencent.com/dsaudit/risk) 页面，可以筛选风险等级（即重要的用户行为和重要安全事件）查看日志。
![](https://qcloudimg.tencent-cloud.cn/raw/484009d2cca1b86dbc823e78d9d73acf.png)


**b) 审计记录应包括事件的日期和时间、用户、事件类型、事件是否成功及其他与审计相关的信息；**

在 [审计日志页面](https://console.cloud.tencent.com/dsaudit/log)，单击任意一条日志后方的**操作**，弹出审计日志详情，可以查看相关的信息。
![](https://qcloudimg.tencent-cloud.cn/raw/0e81c6b176b832d0c33942b25ffde81e.png)

**c) 应对审计记录进行保护，定期备份，避免受到未预期的删除、修改或覆盖等。**

数据安全审计 SaaS 型的审计日志存储于腾讯云 Elasticsearch Service，通过多可用区部署、定期备份方式保证数据可用性。后续版本将在产品页面添加相关说明。

**d) 应对审计进程进行保护，防止未经授权的中断。**

审计进程包含两部分：审计服务器的进程和 Agent 进程。

- **审计服务器的进程**
审计服务器部署在腾讯云侧，由腾讯云进行相关安全保障，用户不具有直接进入产品后台操作的权限。当确有必要，需要进入后台操作时，根据腾讯云流程，需要用户 [提交工单](https://console.cloud.tencent.com/workorder/category)，由腾讯云技术人员得到授权后进行操作。会留存详细的工单记录，便于事后查证。

- **Agent 进程**
Agent 部署在用户的数据库或云服务器上，数据安全审计将对其进行守护检测，当检测到 Agent 中断时，将及时产生告警。
![](https://qcloudimg.tencent-cloud.cn/raw/86f7ccc497402e6617af552bf88cd7b1.png)

**其他：《网络安全法》要求网络日志保留六个月以上。**

在 [审计日志页面](https://console.cloud.tencent.com/dsaudit/log)，选中**近半年**，可以查看近六个月的日志。
![](https://qcloudimg.tencent-cloud.cn/raw/0683adbbfbadb8b16e81774082d2b7f4.png)

