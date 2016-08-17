
## 1. 小米证书申请

### 1.1 概述

由于小米ROM深度定制了安卓系统，加强了权限的控制，第三方APP默认不会在系统的自启动白名单里，APP在后台很容易被系统杀掉，或者用户手动将APP杀死， 因为没有自启动权限，APP的service无法自动重启，从而导致被杀死后无法收到消息。

为了保证APP被杀后，在小米设备上仍然能够收消息，需要集成小米推送。

> 注： 如果不需要对小米设备做推送适配，可以忽略此文章。

### 1.2 小米推送证书申请

首先，需要到 [小米开发者中心](http://dev.xiaomi.com/developer/selectBindType?userId=557535808) 注册开发者帐号。请根据指引完成资料填写，并等待资格审核通过。这里请根据个人实际情况选择帐号类型。

![小米推送-注册](//mccdn.qcloud.com/static/img/04a4cfcc6a1d02125a61674f2a916a40/image.png)

开发者帐号审核通过后，进入 `管理控制台 -> 消息推送`，然后创建一个新的应用。

![小米推送-创建应用](//mccdn.qcloud.com/static/img/53bd8862d2ba5fe46bd9e0fc6026a740/image.png)

根据指引创建应用成功后，进入该应用的详情页面，就可以看到该应用的详细信息，包括`应用包名`，`AppID`，`AppKey`，`AppSecret`。把这些信息记录下来，以备后用。

![小米推送-应用详情](//mccdn.qcloud.com/static/img/e108aef3f58418eddd1b77c9c452ee3d/image.png)

## 2. 华为证书申请

### 2.1 概述

同小米设备一样，华为手机同样对安卓系统进行了深度定制，第三方APP默认不会在系统的自启动白名单中，导致APP被杀后，APP的service无法自动重启。

为了保证APP被杀后，在华为设备上仍然能够收到消息，需要集成华为推送。

> 注： 如果不需要对华为设备做推送适配，可以忽略此文章。

### 2.2 华为推送证书申请

首先， 需要到 [华为开发者联盟](http://developer.huawei.com/cn/consumer/devunion/openPlatform/html/regLogin_smrz.html) 注册开发者帐号。请根据指引完成资料填写，并等待资格审核通过。这里请根据个人实际情况选择帐号类型。

![华为推送-注册](//mccdn.qcloud.com/static/img/d14b455655295a549fd5cd800b622be4/image.png)

开发者帐号审核通过后，可以进入 `管理中心 -> 创建移动应用` 新建一个应用。

![华为推送-创建应用](//mccdn.qcloud.com/static/img/7d95c138939902013fb9b96198f3d44c/image.png)

根据指引创建应用成功后，为该应用添加Push权益。

![华为推送-添加权益1](//mccdn.qcloud.com/static/img/99210a7c4506f4b6fe44db5d54c29438/image.png)

![华为推送-添加权益2](//mccdn.qcloud.com/static/img/9fd84e68a74606074a6543787c5d1690/image.png)

然后进入该应用详情页面就可以看到该应用对应的`应用包名`，`APP ID`，`APP SECRET`。把这些信息记录下来，以备后用。

![华为推送-应用详情](//mccdn.qcloud.com/static/img/90deabf4a7f7f637fe1357464b423c19/image.png)
