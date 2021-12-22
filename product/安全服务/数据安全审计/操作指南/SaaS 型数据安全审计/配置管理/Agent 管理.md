## Agent 部署
1. 登录 [数据安全审计控制台](https://console.cloud.tencent.com/dsaudit)，在左侧导航栏中，单击**配置管理** > **Agent 管理** > **Agent 部署**，进入 Agent 部署页面。
2. 在 Agent 部署页面，根据数据资产添加位置，提供下载链接。配置步骤以及配置注意事项，详情请参见 [Agent 部署](https://cloud.tencent.com/document/product/856/66492)。
3. 在 Agent 部署页面，分为腾讯云内网 Agent 和 腾讯云外 Agent。
 - 腾讯云内网 Agent
以腾讯云内网 Agent 为例。数据资产为腾讯云内资产（关系型云数据库、NoSQL 云数据库、企业分布式云数据库、自建数据库），即可下载 Linux Agent 或下载 Windows Agent。
![](https://qcloudimg.tencent-cloud.cn/raw/c65640511285a11d7eb9e64e529bcec3.png)
 - 腾讯云外 Agent
 以腾讯云外Agent为例。数据资产为腾讯云外资产（腾讯云外数据库）。即可下载 Linux Agent 或下载 Windows Agent。
![](https://qcloudimg.tencent-cloud.cn/raw/d2a196af563c93b1fd11bef5a08a5cbe.png)

## Agent 列表
1. 登录 [数据安全审计控制台](https://console.cloud.tencent.com/dsaudit)，在左侧导航栏中，单击**配置管理** > **Agent 管理** > **Agent 列表**，进入 Agent 列表页面。
2. 在 Agent 列表页面，可以查看所有已配置成功的 Agent。Agent 列表默认展示内容包括：部署 IP、流量来源、VPC、地域、操作系统、最后上报时间、运行状态、开启状态及相关操作。
![](https://qcloudimg.tencent-cloud.cn/raw/cea0da9df20e4aac101fe28aa7a55b1b.png)
3. 在 Agent 列表页面，您可以按**流量来源、地域、数据资产、部署 IP、运行状态**对 Agent 进行搜索。
![](https://qcloudimg.tencent-cloud.cn/raw/af8c89875e236a70e99373452fc4c4c7.png)
4. 在 Agent 列表页面，选择所需部署 IP，单击**编辑**，可以查看和修改 Agent 配置相关信息。
>?设置停止审计阈值。为尽最大可能保证业务运行不受影响，您可以设置基于 CPU 与内存使用率的阈值，当 Agent 宿主机性能超过阈值时，Agent 并暂停流量采集，待宿主机性能降回阈值以下时再恢复采集。如您要求 Agent 任何情况都进行工作，可将负载检测开关关闭，Agent 将持续审计数据。
>
![](https://qcloudimg.tencent-cloud.cn/raw/f05bb7bf100a734517208ab43d936215.png)
5. 在 Agent 列表页面，选择所需部署 IP，单击**卸载** > **确定**，等待卸载完成后，单击**删除**即可删除该部署 IP。
![](https://qcloudimg.tencent-cloud.cn/raw/a89bf73778a84e9e435245b64e588d38.png)
