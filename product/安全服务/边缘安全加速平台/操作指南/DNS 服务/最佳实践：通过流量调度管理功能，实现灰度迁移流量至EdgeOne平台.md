## 场景介绍
您想通过购买edgeOne服务，来保障网站的安全和提升用户服务体验。考虑到用户服务稳定，期望将流量平滑灰度切换至EdgeOne。

假设需要迁移的域名为www.site.com，当前所有流量直接指向源站服务器，源站地址为origin.site.com。

制定分三阶段灰度切换至EdgeOne：首先灰度1%，其次30%，最后100%。

<img width="631" alt="image" src="https://user-images.githubusercontent.com/116173601/208424586-f5870946-c994-4ad5-86cf-9c2f0e0e4f1e.png">


## 步骤一：添加站点和域名

登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)

1.参照[站点接入](https://cloud.tencent.com/document/product/1552/70788)指引添加站点，购买企业版本套餐，以及通过CNAME接入站点site.com。
>?
>- 流量调度管理功能使用前提：站点选购企业版套餐，并采用CNAME接入模式。

2.参照[CNAME接入](https://cloud.tencent.com/document/product/1552/70824)添加域名www.site.com，添加后先不进行CNAME解析切换。

## 步奏二：添加初始灰度策略

1.在左侧导览中，选择站点后单击**域名服务**，选择**流量调度管理**页面。

2.在流量调度管理页面，单击**添加调度策略**，选择www.site.com，单击**创建**。

3.添加服务商，本场景因为是从源站迁移，则输入源站域名origin.site.com，服务名称可自定义填写。

<img width="1153" alt="image" src="https://user-images.githubusercontent.com/116173601/204138663-dcd17898-5484-4f44-8db6-47e5f143f6f0.png">

4.添加初始灰度策略并提交配置，考虑先将1%流量从源站切换到EdgeOne，服务一段时间无问题之后再增加灰度比例，则默认策略添加服务商源站域名权重99，EdgeOne权重1。

<img width="1155" alt="image" src="https://user-images.githubusercontent.com/116173601/204138748-21565ddb-4c56-42d9-b4a9-850c8227edd7.png">

## 步骤三：切换解析开始灰度

添加策略完成后，EdgeOne会给域名分配一个流量调度CNAME，该CNAME与域名的默认CNAME一致，您还需要前往您的 DNS 解析服务商完成 CNAME 配置，方可触发流量调度策略生效。域名解析切换可参考[CNAME接入](https://cloud.tencent.com/document/product/1552/70824)第4部分。

<img width="1353" alt="image" src="https://user-images.githubusercontent.com/116173601/204139712-a3385933-30d6-4df7-8fe1-a1fb52d90208.png">

## 步骤四：变更灰度比例

1.变更灰度30%流量切换至EdgeOne：灰度服务一段时间，确认服务没有问题后，可以进入流量调度管理进行变更灰度比例。

进入流量调度管理页面，选择www.site.com，操作栏点击管理进入编辑页面，编辑默认策略，将EdgeOne权重变更为30，源站域名变更为70，保存则策略立即生效，现网等待dns缓存过期后生效。

<img width="1588" alt="image" src="https://user-images.githubusercontent.com/116173601/204226113-bba1fe95-d9ab-45dd-8005-8e07f23fb620.png">

2.变更灰度100%流量切换至EdgeOne：编辑默认策略，删除源站域名，只保留EdgeOne，保存立即生效，则是100%流量切换至EdgeOne。

<img width="1573" alt="image" src="https://user-images.githubusercontent.com/116173601/204227612-300f8a87-fc42-4c1a-934d-a2164fc0e58e.png">


## 步奏五：完成灰度流程

100%灰度服务一段时间，确认服务没问题后，可以选择停用和关闭流量调度策略，停用和关闭对您的服务没有影响，流量依然全部采用EdgeOne服务。

<img width="1264" alt="image" src="https://user-images.githubusercontent.com/116173601/209599077-72ee2ca3-2111-4468-a56e-cf75f987c86b.png">


