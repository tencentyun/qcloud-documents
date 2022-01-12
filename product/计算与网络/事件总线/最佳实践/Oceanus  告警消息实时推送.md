## 背景介绍

监控与报警系统对于业务生产环境来说是不可或缺的，一旦有故障发生，需要有完善的监控告警链路，保证告警消息可以实时完成推送并进行处理。

腾讯云事件总线（EventBridge）是一款安全、稳定、高效的无服务器事件管理平台。事件中心的事件总线可以接收来自您自己的应用程序、软件即服务（SaaS）和腾讯云服务的实时事件及相关数据流，通过集成消息推送和 SCF 云函数，可以实现邮件、短信、企业微信、钉钉、飞书等多种方式的通知。

流计算 Oceanus 是大数据产品生态体系的实时化分析利器，是基于 Apache Flink 构建的具备一站开发、无缝连接、亚秒延时、低廉成本、安全稳定等特点的企业级实时大数据分析平台。流计算 Oceanus 以实现企业数据价值最大化为目标，加速企业实时化数字化的建设进程。

通过结合 EventBridge + 云函数 SCF，可以实时捕获 Oceanus 集群异常事件并完成推送，本文演示如何捕获 Oceanus 集群状态变更，并发送到企业微信或钉钉、飞书客户端。

## 架构设计
整体架构设计如图，从图上可以看出，当 Oceanus 发生状态变更时（如实例异常，实例隔离，实例下线等）， Oceanus 系统会产生告警事件并主动推送给 EB，经过 EB 绑定的告警规则筛选后，完成到指定目标的推送，并可以基于 SCF 云函数，推送给更多第三方服务。
![](https://qcloudimg.tencent-cloud.cn/raw/859ef386ce6a5cc57b15d219426d115e.png)

## 基本步骤
**1. 登录[EventBridge 控制台](https://console.cloud.tencent.com/eb)，配置告警规则**

![](https://docimg4.docs.qq.com/image/ywr6eYkK3QKT9DQhU74MCA.png?w=1280&h=388.3835616438356)

**2. 以「流计算 Oceanus TaskManager CPU 负载过高」事件告警配置为例，您可以选择指定的事件告警类型，也可以选择全部告警事件，详细事件匹配规则请参见[管理事件规则](https://cloud.tencent.com/document/product/1359/56084)
![](https://docimg3.docs.qq.com/image/g3YmgwjiG0QA32PYpqkFzw.png?w=1280&h=703.7578814627996)**


**3. 配置推送目标**

   可以自由选择投递目标，此处以消息推送和云函数两个投递目标为例：
- 消息推送：通过配置消息推送，将您的告警事件推送至指定的消息接收渠道，完成用户及时触达。
![](https://docimg9.docs.qq.com/image/yg7MTSTIlNUMg-Em4hI1Rw.png?w=1202&h=556)
- 云函数投递：事件总线支持通用 HTTP 协议的 webhook 直接投递，如果您的投递目标对于请求格式有严格要求，建议先通过云函数完成投递事件格式转换，再通过 EB 将原始事件直接发送给指定函数，完成推送链路搭建
![](https://docimg6.docs.qq.com/image/ECG6Be4HFGdXqRHVQquWGA.png?w=1216&h=894)

**4. 告警链路测试**

配置完成后，回到事件集控制台，选择刚刚已绑定的事件集，单击发送事件，可以选择已绑定的事件规则模版，单击发送进行测试。
> 注：测试模版里只支持修改 data 字段里的内容，其它字段已固定，无法自定义修改。

![](https://docimg5.docs.qq.com/image/a63b9-GJAMZtmv6gkPLi5Q.png?w=1280&h=405.8124174372523)
![](https://docimg10.docs.qq.com/image/7f4u4wAot7j0-0zLge3-4A.png?w=1280&h=694.4329896907217)

配置完成后，即可在腾讯云事件总线控制台，完成告警规则的查看与管理。
