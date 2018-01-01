本文以指定某用户拥有 CMQ 队列模型的**消费消息及批量消费消息 写权限**为例，演示如何设置 CMQ 权限。CMQ 的 CAM 权限管理能力，目前处于灰度阶段，您可联系我们的一线技术支持寻求帮助。

**注意**：
CAM 上线前，原协作者账户、子账户均可以登录 CMQ 控制台，并看到根账户的资源列表（即 list 接口权限，原先用的是根账户密钥）。接入 CAM 后，子账户默认是没有获取根账户资源列表权限的（登录控制台用的是子账户的密钥），需要根账户通过 CAM 授权，才有访问权限。

控制台操作指南如下：

## 一、创建用户

1. 访问[用户与权限控制台](https://console.cloud.tencent.com/cam)，并点击【新建用户】。

2. 如果该用户需要登录腾讯云控制台或者调用云 API，则需要选择【允许该用户登录腾讯云】、并填写【QQ帐号】作为登录凭证。
**注意：**
子账户的 QQ 号，建议使用未在腾讯云注册的 QQ 号（子账户无需充值费用，CMQ 费用会在主账户扣除）
[免费申请 QQ号 >>](https://ssl.zc.qq.com/chs/index.html)
![](//mccdn.qcloud.com/static/img/717db35eae2332917a152eb69e8b4339/image.png)

3. 为该用户关联策略（策略描述了权限，关联策略后用户即获得策略描述的权限）。
![](//mccdn.qcloud.com/static/img/6554d84d46a16ea7f708402600bfe08b/image.png)

4. 在【用户管理】列表中，即可查看刚刚添加的子用户。
![](//mccdn.qcloud.com/static/img/f25458bc47e905348883376d3d645244/image.png)

## 二、新建自定义策略

我们可以创建某自定义策略指定开启具体 API 接口的权限，如指定 CMQ Queue 的写权限（消费消息、批量消费消息）。

1. 配置服务类型，勾选【队列模型】。
![](//mc.qcloudimg.com/static/img/ebe81c0f3661863f9961db0c5716081d/image.png)

2. 指定具体 API 接口。
![](//mc.qcloudimg.com/static/img/6237ef0c57ef39db790e19638f4e1bc5/image.png)

3. 指定资源对象。
示例中，我们指定该策略，将该根账户下存量的，新增的（包括该子账户创建的）的所有 Queue 作为关联对象。
**注意：**
子账户默认没有 CMQ 的 list 接口权限（即登录 CMQ 的控制台，无法在控制台看到具体的资源列表，可根据您的情况，考虑是否对子账户添加 list 权限）
![](//mc.qcloudimg.com/static/img/ee8053f051805493d53d6f4f67f2d531/image.png)

## 三、关联子用户

将创建的策略关联到子用户，这样，该子用户将对该子用户内的所有 Queue 资源拥有消费消息、批量消费消息的权限。

![](//mc.qcloudimg.com/static/img/0bfdf9df7ad29dbae8e51c28904be972/image.png)


## 四、子用户登录

使用子账户登录后，若找不到对应的资源，请在控制台右上角，点击切换协作者开发商帐号。

![](//mc.qcloudimg.com/static/img/477c491f7e6c5b1b3a8968499590e92d/image.jpg)

