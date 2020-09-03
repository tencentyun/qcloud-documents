

监控告警是用户在使用日志服务时业务可靠性和可用性的保证。

本文档主要示意如何配置 CLS Loglistener 心跳告警策略，方便用户可以第一时间感知到 Loglistener 采集端的异常情况。



## 步骤1：登录云监控控制台


<div style="background-color:#00A4FF; width: 170px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/monitor/overview" target="_blank"  style="color: white; font-size:16px;"  hotrep="document.guide.3128.btn2">点击前往云监控控制台</a></div>




## 步骤2：新增告警策略

1. 在左侧菜单栏中，选择【告警配置】>【告警策略】，进入告警策略页面。
2. 单击【新增】，进入新建策略页面。需依次配置策略类型、告警对象、条件以及接受人等信息
 - 策略名称：填写策略名称。
 - 备注：填写策略备注。
 - 策略类型：选择监控项。
 - 所属项目：根据需求选择项目。
 - 配置告警触发条件
 日志服务会将机器组的心跳异常/正常数量上报云监控，用户可根据选择监控的机器组列表，配置合适的告警触发条件：
		- 例1，当出现心跳异常数 > =1 时，并持续2个统计周期（统计周期为1分钟），则触发告警，告警策略为每五分钟告警一次。配置信息如图：
	![](https://main.qcloudimg.com/raw/6e8fb9ee28a2a67f535d1b96f835a706.jpg)
		- 例2，当现心跳正常数 < 100 时，并持续2个统计周期（统计周期为1分钟），则触发告警，告警策略为每五分钟告警一次。配置信息如图：
	![](https://main.qcloudimg.com/raw/ce9b071a478e5d2e4167562d0f65ce3d.jpg)
 - 配置告警渠道
  告警渠道指定告警联系人（可以指定接收组），当且仅当接收人的手机、邮箱已验证的前提下，才可以正常接收到告警信息。
3. 单击【完成】，即可创建成功。






## 步骤3：接收告警

腾讯云会根据所配置的告警策略进行监控，当满足触发条件时，会通过告警渠道发送告警信息，如图：

![](https://main.qcloudimg.com/raw/1a097c3580815620f07498671e3b528f.jpg)



## 步骤4：查看告警历史

1. 登录 [云监控控制台](https://console.cloud.tencent.com/monitor/overview)。
2. 在左侧菜单栏中单击【告警历史】，可以查看触发告警的历史信息，包括告警触发的开始时间、持续时间等详情。
