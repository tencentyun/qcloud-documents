## 米大师

支付是每个 App 变现的基本手段，[腾讯米大师](http://wiki.open.qq.com/wiki/米大师简介) 原本是腾讯开放平台上的移动支付平台，这个平台其实主要是针对腾讯内部客户的，外部客户接入起来可能并不是很友好，现在腾讯云上终于通过[移动开发平台](https://cloud.tencent.com/document/product/666) 来免费开放出来了。

目前市面上比较常见的第三方支付集成接入服务商有 BeeCloud 和 Ping++，两个公司都是在 2014 年创立或者产品上线，并且很多功能方面都比较类似，这里我们拿来和米大师来进行比较。

通过第三方接入支付的优势：

* 第三方支付平台往往支持多支付渠道以及多平台集成，开发者集成支付时可以一劳永逸。
* 第三方支付平台可以提供一个统一的数据分析平台，帮助开发者更好的分析用户的支付情况。
* 第三方支付平台一般会对支付渠道提供的接口进行再封装，简化用户的接入步骤。

通过第三方接入支付的劣势：

* 需要开发者在第三方平台上配置支付渠道的关键信息，具有一定的安全风险。
* 开发者应用的支付信息可能会有泄漏风险。
* 第三方平台往往是收费服务，对中小开发者具有一定的负担。

下面从产品功能、收费情况、示例Demo、接入流程来和米大师进行整体的比较。


## 功能

产品功能

主要特性：

* BeeCloud 和 Ping++ 支持 test 和 live 两种模式，不同的模式下有不同的 secret key，test 模式下的支付是在虚拟环境下，用户不需要商户认证和申请支付渠道就可以跑通支付流程，但是不会产生任何的真实交易，这样可以降低用户的体验门槛。
* Beecloud 和 Ping++ 支持微信、支付宝、银联等多种支付渠道，需要用户首先进行企业认证。
* Beecloud 和 Ping++ 支持网页收款、线下收款、移动 APP 收款，这里我们主要比较移动 APP 收款模式。
* ping++ 支持聚合支付、会员账户系统、多级商户系统和资金存管服务，这是 BeeCloud 所没有的。

米大师与之对比可以看出：

* 米大师上线了会员账户系统和营销系统，方便对用户进行管理。
* 米大师暂时不支持 test 模式，用户需要申请好支付渠道后才能进行调试。
* 米大师目前只支持微信支付和 QQ 支付两种渠道，暂时不支持支付宝。

## 收费情况

### Beecloud 

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/PR-manuscript/Android/beecloud_pay.png)

### ping++ 

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/PR-manuscript/Android/ping_pay.png)

### 米大师

米大师目前完全免费。

## 示例 Demo

BeeCloud 提供了示例 demo（[apk 包](https://beecloud.cn/demo/)）这个 demo 是 live 环境，可以让用户体验整个支付流程。同时 BeeCloud 还提供了[示例工程 demo](https://github.com/beecloud/beecloud-android)，用户可以在 test 环境下测试 demo。

Ping++ 只提供了[示例工程 demo](https://github.com/PingPlusPlus/pingpp-android) 用户同样可以在 test 环境下测试 demo。

米大师目前只提供了[示例工程 demo](https://github.com/tencentyun/tac-sdk-android-samples)，需要用户现在控制台上配置好支付渠道信息后才可以正确拉起支付。


## 接入流程

### BeeCloud

BeeCloud 移动 APP 支付收款流程：

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/PR-manuscript/Android/beecloud_step.png)

### Ping++ 和米大师

Ping++ 和米大师 移动 APP 支付收款流程：

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/PR-manuscript/Android/midas_step.png)


我们可以看出，由于 BeeCloud 帮助用户封装了下单接口，使得用户使用起来更加方便，但是我们可以看到这仍然无法避免用户需要使用自己的服务器获取支付结果。而米大师和 Ping++ 均需要用户去搭建自己的服务器，并部署支付相关接口，这里 Ping++ 提供了服务端 SDK，而米大师暂时只提供了 API 接口。


## 调试工具

BeeCloud 提供了[工具](https://beecloud.cn/rest/#/api/bill)来帮助用户进行测试：

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/PR-manuscript/Android/beecloud_tools.png)

同样的 Ping++ 也有类似的[工具](https://dashboard2.pingxx.com/app/app_aPG088GyHunP5m1y/setting/debug)

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/PR-manuscript/Android/ping_tools.png)

米大师目前没有类似的工具供用户使用。

## 总结

* 作为第三方支付平台，我们首先最关心的是自身数据的安全性，米大师作为腾讯支付的前排兵，支持腾讯旗下的微信支付和 QQ 支付还是很靠谱的。
* 目前 BeeCloud 和 Ping++ 都是收费的，尤其是 Ping++ 的收费相对较高，并且还没有免费版本，这对于米大师这样一个全免费的平台还是有很大的吸引力的。





