
## 小米证书申请

### 概述

由于小米 ROM 深度定制了 Android 系统，加强了权限的控制，第三方 App 默认不会在系统的自启动白名单里，App 在后台很容易被系统杀掉，或者用户手动将 App 杀死。 因为没有自启动权限，App 的 `service` 无法自动重启，从而导致被杀死后无法收到消息。为了保证 App 被杀后，在小米设备上仍然能够收消息，需要集成小米推送。

> 注： 如果不需要对小米设备做推送适配，可以忽略此文章。

### 小米推送证书申请

首先，需要到 [小米开发者中心](http://dev.xiaomi.com/developer/selectBindType?userId=557535808) 注册开发者帐号。请根据指引完成资料填写，并等待资格审核通过。这里请根据个人实际情况选择帐号类型。

![小米推送-注册](//mccdn.qcloud.com/static/img/04a4cfcc6a1d02125a61674f2a916a40/image.png)

开发者帐号审核通过后，进入【管理控制台】-【消息推送】，然后创建一个新的应用。

![小米推送-创建应用](//mccdn.qcloud.com/static/img/53bd8862d2ba5fe46bd9e0fc6026a740/image.png)

根据指引创建应用成功后，进入该应用的详情页面，就可以看到该应用的详细信息，包括`应用包名`，`AppID`，`AppKey`，`AppSecret`。把这些信息记录下来，以备后用。

![小米推送-应用详情](//mccdn.qcloud.com/static/img/e108aef3f58418eddd1b77c9c452ee3d/image.png)

## 华为证书申请

### 概述

同小米设备一样，华为手机同样对 Android 系统进行了深度定制，第三方 App 默认不会在系统的自启动白名单中，导致 App 被杀后，App 的 `service` 无法自动重启。为了保证 App 被杀后，在华为设备上仍然能够收到消息，需要集成华为推送。

> 注： 如果不需要对华为设备做推送适配，可以忽略此文章。

### 华为推送证书申请

首先， 需要到 [华为开发者联盟](http://developer.huawei.com/cn/consumer/devunion/openPlatform/html/regLogin_smrz.html) 注册开发者帐号。请根据指引完成资料填写，并等待资格审核通过。这里请根据个人实际情况选择帐号类型。

![华为推送-注册](//mccdn.qcloud.com/static/img/d14b455655295a549fd5cd800b622be4/image.png)

开发者帐号审核通过后，可以进入【管理中心】-【创建移动应用】新建一个应用。

![华为推送-创建应用](//mccdn.qcloud.com/static/img/7d95c138939902013fb9b96198f3d44c/image.png)

根据指引创建应用成功后，为该应用添加 Push 权益。

![华为推送-添加权益1](//mccdn.qcloud.com/static/img/99210a7c4506f4b6fe44db5d54c29438/image.png)

![华为推送-添加权益2](//mccdn.qcloud.com/static/img/9fd84e68a74606074a6543787c5d1690/image.png)

然后进入该应用详情页面就可以看到该应用对应的`应用包名`，`APP ID`，`APP SECRET`。把这些信息记录下来，以备后用。

![华为推送-应用详情](//mccdn.qcloud.com/static/img/90deabf4a7f7f637fe1357464b423c19/image.png)


## 魅族证书申请

### 概述

魅族推送（Push）是魅族公司向开发者提供的消息推送服务，通过在云端与客户端之间建立一条稳定，可靠的长连接，为开发者提供向客户端应用实时推送消息的服务，通过推送消息，魅族推送服务能有效地帮助开发者拉动用户活跃度，改善产品体验。为了保证 App 被杀后，在魅族设备上仍然能够收到消息，需要集成魅族推送。

> 注： 如果不需要对魅族设备做推送适配，可以忽略此文章。

### 魅族推送证书申请

首先需要到 [Flyme 开放平台](http://open.flyme.cn/) 注册开发者帐号。请根据指引完成资料填写，并等待资格审核通过。这里请根据个人实际情况选择帐号类型。

开发者身份认证通过后，请登录推送平台，进入首页请单击右上角【新建应用】。

![魅族推送-创建应用1](https://main.qcloudimg.com/raw/afd484e453ab12ea507626b642b43fa0.jpg)

进入应用创建页面，输入应用名称、应用包名、应用图标，单击【创建】即可。

![魅族推送-创建应用2](https://main.qcloudimg.com/raw/555a9c49901468d238371005155959b3.jpg)

完成创建后单击【打开应用】进入【配置管理】中的【应用配置】查看应用信息。

>注：其中 App Secret 是可以进行重置操作的（之前旧 App Secret 的服务端身份识别会失效，以重置后的为准）。

![魅族推送-应用信息1](https://main.qcloudimg.com/raw/643327bf05b42404aa76871e6d2071b6.jpg)

![魅族推送-应用信息2](https://main.qcloudimg.com/raw/0087408a7bcaf309a8181ff6a04ff218.jpg)

## OPPO证书申请

### 概述

Opush是ColorOS上的系统级通道，为开发者提供稳定，高效的消息推送服务。为了保证 App 被杀后，在OPPO设备上仍然能够收到消息，需要集成Opush。

> 注： 如果不需要对OPPO设备做推送适配，可以忽略此文章。

### OPPO推送证书申请

首先需要到 [OPPO 开放平台](https://open.oppomobile.com) 注册开发者帐号。请根据指引完成资料填写，并等待资格审核通过。这里请根据个人实际情况选择帐号类型。

开发者身份认证通过后，请登录推送平台，进入首页请单击右上角【新建应用】。

![OPPO推送-创建应用1](https://main.qcloudimg.com/raw/eb832d1035713d214272841d085106b6.jpg)

进入应用创建页面，输入应用名称、应用包名、应用图标，单击【创建】即可。

![OPPO推送-创建应用2](https://main.qcloudimg.com/raw/e2965a10c86bc84735c321ec98ef2de5.jpg)

审核通过之后，就可以获得推送接口，查看应用信息。

![OPPO推送-应用信息1](https://main.qcloudimg.com/raw/718ca50a93fdd52ad71e9d32b87e3f03.jpg)

## vivo证书申请

### 概述

vivo推送是vivo公司向开发者提供的消息推送服务，通过在云端与客户端之间建立一条稳定、可靠的长连接，为开发者提供向客户端应用实时推送消息的服务，支持百亿级的通知/消息推送，秒级触达移动用户。

开发者可以方便地通过嵌入 SDK，通过 API 调用或者Web端可视化操作，实现对特定用户推送，大幅提升用户活跃度，有效唤醒沉睡用户，并实时查看推送效果。

> 注： 如果不需要对vivo设备做推送适配，可以忽略此文章。

### vivo推送证书申请

首先需要到 [vivo 开放平台](https://dev.vivo.com.cn/home) 注册开发者帐号。请根据指引完成资料填写，并等待资格审核通过。这里请根据个人实际情况选择帐号类型。

开发者身份认证通过后，请登录推送平台，进入消息推送界面单击【创建】。

![vivo推送-创建应用1](https://main.qcloudimg.com/raw/f75ea7bb41aa270ecd3c3afd1d4d2d79.png)

进入应用创建页面，输入相应信息，单击【提交申请】。

![vivo推送-创建应用2](https://main.qcloudimg.com/raw/d92273efe228390568eba94bf8cbf658.png)

审核通过即可查看应用信息。

![vivo推送-应用信息1](https://main.qcloudimg.com/raw/a797bea6eab2ea478a70de93e09d205d.png)





