
## 小米证书申请

### 概述

由于小米 ROM 深度定制了安卓系统，加强了权限的控制，第三方 App 默认不会在系统的自启动白名单里，App 在后台很容易被系统杀掉，或者用户手动将 App 杀死。 因为没有自启动权限，App 的 `service` 无法自动重启，从而导致被杀死后无法收到消息。为了保证 App 被杀后，在小米设备上仍然能够收消息，需要集成小米推送。

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

同小米设备一样，华为手机同样对安卓系统进行了深度定制，第三方 App 默认不会在系统的自启动白名单中，导致 App 被杀后，App 的 `service` 无法自动重启。为了保证 App 被杀后，在华为设备上仍然能够收到消息，需要集成华为推送。

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
