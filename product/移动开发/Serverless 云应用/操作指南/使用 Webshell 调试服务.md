本文将先向您介绍 Serverless云应用 的 Webshell 功能，以及如何使用 Webshell 完成基本的运维需求。



## 操作背景

容器是一个暂态的、供服务运行的环境，您在使用 Serverless 云应用时只需关注自己的服务，不需要涉及对容器的直接操作，包括创建、配置、更新、重启、销毁等等。但为了方便进行线上问题定位、排查，特别是调试关于代码本身的问题，Serverless 云应用在控制台提供了简易版 Webshell，供您查看并调试自己的容器。

> !通过 Webshell 直接操作容器可能会带来风险。Serverless 云应用只是为您提供了一个直达容器的途径，您在Webshell 中做的一切操作，Serverless 云应用都无法感知、无法管控。
> - 若您在 Webshell 中的操作引起容器 OOM，可能会带来服务中断。
> - 若您在 Webshell 中直接修改了容器配置，可能会导致与 Serverless 云应用中记录的容器配置不一致，引起后续操作混乱。



## 步骤1：登录控制台

登录 [Serverless 云应用控制台](https://console.cloud.tencent.com/tcb/service)，再按需要切换到指定的环境。
![](https://main.qcloudimg.com/raw/7ccca44479b1c0cf092234a8e0f1ee5a.png)

> ?Serverless 云应用公测期间，需要先 [申请开通](https://cloud.tencent.com/apply/p/y5uji0g6a7p)，审核通过后，云开发控制台的左侧菜单才会出现 【Serverless 云应用】入口，否则入口将不可见。公测结束后，**Serverless 云应用**的入口将对所有云开发用户开放。



## 步骤2：进入您需要运维的服务详情

单击服务名称进入服务详情页面。

![](https://main.qcloudimg.com/raw/252af6bc138cd26f7f109fe3ed8b5fa2.png)



## 步骤4：进入您需要运维的版本详情

单击版本名称进入版本详情页面。
![](https://main.qcloudimg.com/raw/dd62fe608c1afd19bf9b7e5a696a5ebf.png)

## 步骤5：进入“实例”选项卡

![](https://main.qcloudimg.com/raw/3c4aa09187b8e089c22d8b1ca5e6c076.png)



## 步骤6：选择具体容器进入 Webshell

根据版本的“副本个数”、“扩缩容条件”和当前版本流量情况，您的版本下可能有多个实例（容器）。同一个版本下所有的容器都是根据“版本配置”创建出来的，配置信息完全一致，因此绝大多数情况下您任意选择一个容器进入webshell都可对当前版本进行调试和问题定位。但不排除某些特殊情况下，仅有个别容器状态异常。

单击需要调试的容器对应的【Webshell】。



## 步骤7：视具体情况输入合适的检查命令

您可以开始对自己的服务进行调试。
