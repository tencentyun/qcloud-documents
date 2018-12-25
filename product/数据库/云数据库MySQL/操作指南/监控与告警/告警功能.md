## 操作场景
您可以创建告警用于在云产品状态改变时触发警报并发送相关消息。创建的告警会根据每隔一段时间监控的指标相对于给定阈值的情况判断是否需要触发相关通知。
状态改变触发告警后，您可以及时进行相应的预防或补救措施。因此，合理地创建告警能帮助您提高应用程序的健壮性和可靠性。有关告警的更多信息，请参考云监控的 [告警配置][1] 文章。
当用户需要针对某个产品的某个状态发送告警时，需要先创建告警策略。告警策略包括名称、类型和告警触发条件三个必要组成部分。每个告警策略是一系列告警触发条件的集合，告警触发条件是“或”关系，即一个条件满足，就会发送告警。告警将发送至告警策略关联的所有人，用户接收到告警后可以及时查看并采取相应措施。

>! 请确认您已经设置默认告警接收人，否则腾讯云 TencentDB 的默认告警策略将无法通知到您。


## 操作步骤
## 1. 创建告警策略
1. 单击导航栏中【菜单】 > 【产品】 > 【管理工具】 > 【云监控】，进入【云监控】产品介绍后，单击【立刻体验】。进入云监控 [管理控制台](https://console.cloud.tencent.com/monitor/overview)。

2. 单击【告警配置】 > 【告警策略】，在告警策略列表页上单击【新增】按钮。
![](https://main.qcloudimg.com/raw/97b9c7cb1d51ea636ded26e22057da23.png)

2. 在 **新建策略** 中，设置策略名称、策略类型、所属产品、告警对象、触发条件等内容，单击【完成】。

>? 
>1. 告警触发条件是指标、比较关系、阈值、统计周期和持续周期组成的一个有语义的条件。例如：指标为 **磁盘使用率**、比较关系为 >、阈值为 80%、统计周期为 5 分钟、持续周期为 2 个周期。表示：每 5 分钟收集一次磁盘使用率数据，若某台云数据库的 **磁盘使用率** 连续两次大于 80% 则触发告警。
>2. 可通过选择对象所在的地域或搜索对象的实例 ID 找到需要关联的对象实例。

![](https://main.qcloudimg.com/raw/d9f406ca7b9a4e9eeb25b743bc117288.png)
![](https://main.qcloudimg.com/raw/57f1bbf9632a35b3f0325d9598a15e86.png)
![](https://main.qcloudimg.com/raw/60f2a872d08ca8281313258f7778a79c.png)



## 2. 关联对象
创建完告警策略后，您可以为其关联一些告警对象，对象达到告警触发条件时会发送告警。您可以通过以下配置关联告警对象。
1. 登录到云监控 [管理控制台](https://console.cloud.tencent.com/monitor/overview) 后单击【告警配置】 > 【告警策略】。在告警策略列表页中，单击刚刚创建的告警策略。
![](https://main.qcloudimg.com/raw/8a1cbae22c590bd3299793ea289fef6a.png)
2. 在 **管理告警策略** 页面中，单击【新增对象】。
![](https://main.qcloudimg.com/raw/fc7be989ce8d0e1d276d2d0802cff295.png)
2. 选择您需要关联的云产品，单击【应用】按钮，即可关联告警对象。
![](https://main.qcloudimg.com/raw/421a6dda288be4b931235ea9e03e5328.png)

## 3. 设置接收告警的对象
告警接收对象决定了什么人能够接收到告警信息。您可以通过以下配置告警接收对象。
1. 登录到云监控 [管理控制台](https://console.cloud.tencent.com/monitor/overview) 后单击【告警配置】 > 【告警策略】。在告警策略列表页中，单击刚刚创建的告警策略。
![](https://main.qcloudimg.com/raw/8a1cbae22c590bd3299793ea289fef6a.png)
1. 在 **管理告警策略** 页面中，在详情页中的【告警接收组】内单击【编辑】
![](https://main.qcloudimg.com/raw/6d05a461a7d722aac6e1d8607a3f12cd.png)
2. 选择需要通知的用户组，设置相关信息，单击【保存】，即可完成告警接收对象的设置。
![](https://main.qcloudimg.com/raw/6d6f0a5aa52c541bb00dfd36e97ecd49.png)

[1]:	https://cloud.tencent.com/doc/product/248/1073
[2]:	https://console.cloud.tencent.com/
[3]:	https://console.cloud.tencent.com/
[4]:	https://console.cloud.tencent.com/
