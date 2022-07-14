## 概述
应用性能观测（APM）继承了 TAPM 协议，您只需要简单修改上报信息，即可完成从 TAPM 到 APM 的迁移。
整个过程预计耗时10分钟。

## 准备工作
我们已经把您默认添加到了应用性能观测服务的白名单，您无需再次提交开白申请，直接登录 [应用性能观测控制台](https://console.cloud.tencent.com/apm) 即可开始体验。

### 创建业务系统
应用性能观测服务继承 TAPM 原有业务系统的概念，以便更好地组织和管理被监控的服务，并实现业务监控。您可以参考 TAPM 业务系统部署关系在 APM 创建业务系统，两个业务系统的作用都是应用分组。
>?为了更好的帮助您管理成本，不同的业务系统在应用性能观测平台中是不同的资源实例，所以不同业务系统间会进行数据隔离。后续您也可以在计费结算中，得到业务系统维度的成本统计。

进入 [应用性能观测控制台](https://console.cloud.tencent.com/apm) **资源管理**页面，单击**新建**即可创建业务系统。

>!业务系统创建成功之后，我们会为您自动分配上报 Token 。

### 获取上报地址和 Token

进入 [应用性能观测控制台](https://console.cloud.tencent.com/apm) **应用监控** > **应用列表**页面，单击**接入应用**，在添加应用列 Java 语言与自研探针的数据采集方式。
在应用接入步骤获取您的接入点和 Token，如下图所示：
![](https://main.qcloudimg.com/raw/d7d94913947d31edf70e85c6462c6bac.png)

## 上报切换
#### 方法一：修改配置文件
在您的服务器上的 TAPM 目录下，找到 `tapm.properties` 文件，将上一步获取的接入点和 Token 信息按如下方式替换：
```java
collector.addresses=<接入点>
license_key=<Token>
app_name=<上报的服务名称>
```

重启您的应用。等待5分钟，当您的 Java 应用服务有 HTTP 请求进入，性能数据将发送到应用性能观测系统。

#### 方法二：修改 JVM 参数
如果您是通过配置 JAVA_OPTS 完成的接入，修改 license_key（token） 和 collector.addresses（接入点）即可。（中间以空格分隔）：
<dx-codeblock>
:::  java
    -Dtapm.app_name=${APP_NAME}//应用名称
    -Dtapm.license_key=${LICENSE_KEY}//token
    -Dtapm.collector.addresses=${COLLECTOR_ADDRESSES}//接入点
:::
</dx-codeblock>



<dx-alert infotype="explain" title="迁移常见疑问">
1. 是否会迁移 TAPM 里的监控数据？
考虑到 Trace 数据的时效性较强，同时目前 TAPM 仅处于内测阶段。我们将不会迁移您的历史数据。
2. APM 和 TAPM 相比有哪些变化？
   -  集成云监控告警能力，提供更可靠易用的应用性能指标告警
   -  拓展了语言支持以及协议兼容
   -  架构优化，更稳定的性能
   </dx-alert>




<dx-alert infotype="explain" title="">
如迁移过程中有任何疑问，您可通过以下方式加入微信交流群：

添加小助手微信（微信号：hitherecm ），回复 “APM” ，小助手将会拉您进入微信交流群。
直接扫描以下二维码，添加小助手微信，小助手将会拉您进入微信交流群。
<img src="https://main.qcloudimg.com/raw/c20740abb44f5cdf8de337879b658366.jpg" style="width: 20%"></img>
</dx-alert>

