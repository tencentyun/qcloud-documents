您可以创建告警用于在云产品状态改变时触发警报并发送相关消息。创建的告警会根据每隔一段时间监控的指标相对于给定阈值的情况判断是否需要触发相关通知。
状态改变触发告警后，您可以及时进行相应的预防或补救措施。因此，合理地创建告警能帮助您提高应用程序的健壮性和可靠性。有关告警的更多信息，请参考云监控的 [告警配置][1] 文章。
当用户需要针对某个产品的某个状态发送告警时，需要先创建告警策略。告警策略包括名称、类型和告警触发条件三个必要组成部分。每个告警策略是一系列告警触发条件的集合，告警触发条件是“或”关系，即一个条件满足，就会发送告警。告警将发送至告警策略关联的所有人，用户接收到告警后可以及时查看并采取相应措施。
>**注意：**
请确认您已经设置默认告警接收人，否则腾讯云 CDB 的默认告警策略将无法通知到您。

您可以根据以下指引进行告警策略的创建：

## 创建告警策略
1. 单击导航栏中【云产品】 > 【基础产品】 > 【监控与管理】 > 【云监控】，进入【云监控】产品介绍后，单击【免费使用】。进入云监控 [管理控制台](https://console.cloud.tencent.com/monitor/overview)。
![](//mc.qcloudimg.com/static/img/886cd2f9011883ee3d541928c6619f9b/image.png)
![](//mc.qcloudimg.com/static/img/286402320d17a7a66f8d6b81542a6b40/image.png)
2. 单击【我的告警】 > 【告警策略】，在告警策略列表页上单击【新增告警策略】按钮。
![](//mc.qcloudimg.com/static/img/12704bae3992fd2cedee31ba89071c2a/image.png)
2. 在 **新增告警策略** 中，输入策略名称、选择策略类型（要作用的产品）并选择告警触发条件。
告警触发条件是指标、比较关系、阈值、统计周期和持续周期组成的一个有语义的条件。例如：指标为 **磁盘使用率**、比较关系为 >、阈值为 80%、统计周期为 5 分钟、持续周期为 2 个周期。表示：每 5 分钟收集一次磁盘使用率数据，若某台云数据库的 **磁盘使用率** 连续两次大于 80% 则触发告警。单击【下一步：关联告警对象】
![](//mc.qcloudimg.com/static/img/fc3830b9c4910feb7a08da76c64098e2/image.png)
3. 选择对象所在的地域或通过对象的实例 ID 搜索需要关联的对象实例，勾选后单击【下一步：设置接收组】。
![](//mc.qcloudimg.com/static/img/7a7fbad0bc58f746c6ee410fcb2034f3/image.png)
4. 在 **选择告警接受组** 中选择需要收到告警信息的用户组，单击【完成】，即可完成告警策略的创建。
![](//mc.qcloudimg.com/static/img/6ed5a8d41b98c0e8b840a78ce5238fc7/image.png)

## 关联对象
创建完告警策略后，您可以为其关联一些告警对象，对象达到告警触发条件时会发送告警。您可以通过以下配置关联告警对象。
1. 登录到云监控 [管理控制台](https://console.cloud.tencent.com/monitor/overview) 后单击【我的告警】 > 【告警策略】。在告警策略列表页中，单击刚刚创建的告警策略。
![](//mc.qcloudimg.com/static/img/6f881d6e32e9ab3df483bd1821d7fb64/image.png)
2. 在 **管理告警策略** 页面中，单击【新增关联】。
![](//mc.qcloudimg.com/static/img/a34ebce6478c8b40d3194161fd85a830/image.png)
2. 选择您需要关联的云产品，单击【应用】按钮，即可关联告警对象。
![](//mc.qcloudimg.com/static/img/2e7b0fd3a6c3b53b29f2c9665f1925f2/image.png)

## 设置接收告警的对象
告警接收对象决定了什么人能够接收到告警信息。您可以通过以下配置告警接收对象。
1. 登录到云监控 [管理控制台](https://console.cloud.tencent.com/monitor/overview) 后单击【我的告警】 > 【告警策略】。在告警策略列表页中，单击刚刚创建的告警策略。
![](//mc.qcloudimg.com/static/img/6f881d6e32e9ab3df483bd1821d7fb64/image.png)
1. 在 **管理告警策略** 页面中，在详情页中单击【管理告警接收组】
![](//mc.qcloudimg.com/static/img/a8c1dd33a761c4758d5bd203242b7f04/image.png)
2. 选择需要通知的用户组，单击【保存】，即可完成告警接收对象的设置。
![](//mc.qcloudimg.com/static/img/e33bb450c694a5672050ab70d0ad8b0a/image.png)

[1]:	https://cloud.tencent.com/doc/product/248/1073
[2]:	https://console.cloud.tencent.com/
[3]:	https://console.cloud.tencent.com/
[4]:	https://console.cloud.tencent.com/
