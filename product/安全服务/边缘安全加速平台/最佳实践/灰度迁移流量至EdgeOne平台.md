## 场景介绍
通过购买 EdgeOne 服务，来保障网站的安全和提升用户服务体验。考虑到用户服务稳定，期望将流量平滑灰度切换至 EdgeOne。
 
假设需要迁移的域名为 `www.site.com`，当前所有流量直接指向源站服务器，源站地址为 `origin.site.com`。

制定分三阶段灰度切换至 EdgeOne：首先灰度1%，其次30%，最后100%。

<img src="https://qcloudimg.tencent-cloud.cn/raw/9fbd9c59c70a4c105fa5fa940efff6b8.png" width=700px>


## 步骤一：添加站点和域名
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，根据 [站点接入](https://cloud.tencent.com/document/product/1552/70788) 指引添加站点，购买企业版本套餐，以及通过 CNAME 接入站点 `site.com`。
>?流量调度管理功能使用前提：站点选购企业版套餐，并采用 CNAME 接入模式。

2. 根据 [CNAME 接入](https://cloud.tencent.com/document/product/1552/70824) 添加域名 `www.site.com`，添加后先不进行 CNAME 解析切换。

## 步骤2：添加初始灰度策略

1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，在左侧导览中，选择站点后单击**域名服务**，选择**流量调度管理**页面。
2. 在流量调度管理页面，单击**添加调度策略**，选择 `www.site.com`，单击**创建**。
3. 添加服务商，本场景因为是从源站迁移，则输入源站域名 `origin.site.com`，服务名称可自定义填写。
<img width="1153" alt="image" src="https://user-images.githubusercontent.com/116173601/204138663-dcd17898-5484-4f44-8db6-47e5f143f6f0.png">
4. 添加初始灰度策略并提交配置，考虑先将1%流量从源站切换到 EdgeOne，服务一段时间无问题之后再增加灰度比例，则默认策略添加服务商源站域名权重99，EdgeOne 权重1。
<img width="1155" alt="image" src="https://user-images.githubusercontent.com/116173601/204138748-21565ddb-4c56-42d9-b4a9-850c8227edd7.png">

## 步骤三：切换解析开始灰度

添加策略完成后，EdgeOne 会给域名分配一个流量调度 CNAME，该 CNAME 与域名的默认 CNAME 一致，您还需要前往您的 DNS 解析服务商完成 CNAME 配置，方可触发流量调度策略生效。域名解析切换可参见 [CNAME 接入](https://cloud.tencent.com/document/product/1552/70824) 第4部分。
![](https://qcloudimg.tencent-cloud.cn/raw/d91fd285951411702432814413cc2a7a.png)

## 步骤四：变更灰度比例
1. 变更灰度30%流量切换至 EdgeOne：灰度服务一段时间，确认服务没有问题后，可以进入流量调度管理进行变更灰度比例。
进入流量调度管理页面，选择 `www.site.com`，单击操作列**管理**进入编辑页面，编辑默认策略，将 EdgeOne 权重变更为30，源站域名变更为70，单击**保存**则策略立即生效，现网等待 dns 缓存过期后生效。
![](https://qcloudimg.tencent-cloud.cn/raw/ef268408369a23587d1b811e9b278c0c.png)
2. 变更灰度100%流量切换至 EdgeOne：编辑默认策略，删除源站域名，只保留 EdgeOne，单击**保存**立即生效，则是100%流量切换至 EdgeOne。
![](https://qcloudimg.tencent-cloud.cn/raw/7592020d076edec1da90e3517f957895.png)


## 步骤五：完成灰度流程
100%灰度服务一段时间，确认服务没问题后，可以选择停用和关闭流量调度策略，停用和关闭对您的服务没有影响，流量依然全部采用 EdgeOne 服务。
![](https://qcloudimg.tencent-cloud.cn/raw/6ff66eb5df1796f11874533d9f2b8693.png)

