## 为何要派发?

UserSig是使用腾讯云通讯服务（[IM](https://cloud.tencent.com/product/im)）所需的一种安全票据，所以如果您准备使用腾讯云 IM 服务实现聊天室功能，就需要您的后台工程师生成 UserSig 给返回给终端 APP；如果您已经有自己的 IM 解决方案（也就是已经有自己的聊天室了），可以免去这部分工作。

## 什么是UserSig?
腾讯云 IM 的前身是 QQ 的即时通讯消息系统，我们将 QQ 的消息模块进行了抽离，变成了适合移动端接入的 IM SDK。将消息后台进行改造，使其脱离对 QQ 号码的绑定，构成了现在的 IM 云通讯后台。

您可以把 IM SDK 理解为一个没有用户交互界面的 QQ，把 IM SDK 集成到您的 APP 里，就相当于把一个 QQ 的消息内核集成在您的 APP 内部。

我们都知道，QQ 可以用来收发单聊和群聊的消息，但前提是您必须先登录才能使用。我们也都知道，登录 QQ 用的是 QQ 号和密码，登录 IM SDK 也是一样，只是肯定不能再用 QQ 号和密码了，而是使用您指定的用户名（userid）和密码（usersig）。

- **用户名（userid）**
可以是您目前 APP 里的用户ID，比如您有一个用户，他/她的账号 ID 是 27149， 那么您就可以用 27149 作为登录 IM SDK 的 userid。

- **密码（usersig）**
既然您指定了 27149 是您的用户，腾讯云如何才能确认该用户是您认可的合法用户呢？usersig 就是用于解决这个问题的，usersig 本质是对 userid、appid 等信息的非对称加密。

 非对称加密用的加密密钥和解密密钥是不同的，您的服务器可以持有私钥并对 userid 和 appid 进行非对称加密，加密之后的结果就是 usersig ；而腾讯云同步持有您的公钥，这样一来，腾讯云就可以确认 usersig 是否合法，从而可以确认它是否是由您的服务器签发的。

![](https://mc.qcloudimg.com/static/img/1e218acdf45772973f9f6c363ab55d89/image.jpg)

## 如何生成UserSig?

### step1：获取签发UserSig用的私钥

进入云通讯 [管理控制台](https://console.cloud.tencent.com/avc)，如果还没有开通服务，直接点击 **开通云通讯** 按钮即可。新开通的账号下，应用列表是空的，点击 **创建应用接入** 按钮创建一个新的应用：
![](//mc.qcloudimg.com/static/img/897bff65af6202322a434b6fa3f8a0bd/image.png)

点击 **确定** 按钮，之后就可以在应用列表中看到刚刚添加的项目了，如下图所示：
![](https://mc.qcloudimg.com/static/img/fff565dc81ba26ca7af4951264b7bb4c/image.png)

点击 **应用配置** 链接，会进入应用配置界面，再点击 **账号体系集成** 右侧的 **编辑** 按钮，按照下图所示进行配置即可（账号名称和管理员名称推荐用英文，账号名称随便填写，管理员名称在调用 IM 的 REST API 时可以用到）。
![](https://mc.qcloudimg.com/static/img/1104e8354d234d949840c9b6c396fd24/image.png)

点击 **保存** 按钮，页面会自动刷新，之后就可以看到 **下载公私钥** 的按钮了。
![](https://mc.qcloudimg.com/static/img/67810cab51216a813b47edcb960ab67a/image.png)

点击 **下载公私钥** 按钮，会得到一个叫做 **keys.zip** 的压缩包，里面有一个 private_key 和 一个 public_key，**private_key** 就是用来签发 UserSig 的私钥了。
![](https://mc.qcloudimg.com/static/img/615590334ba32627857fdb309176682f/image.png)

### step2：测试private_key
可以在 **开发辅助工具** 中测试一下 private_key 是否能正常进行签名。
![](https://mc.qcloudimg.com/static/img/b7d40f17068d9f6605bcac81e2891b5e/image.png)

### step3：集成生成代码
我们在官网的 SDK 下载区提供了一份计算UserSig 的简单版源码，有 java 和 php 两个版本的，如果您需要其他版本的，可以到 [DOC](https://cloud.tencent.com/document/product/269/1510) 里寻找。

-[**UserSig计算源码下载（java | PHP | nodejs）**](https://cloud.tencent.com/document/product/454/7873#Server)


## 如何使用 UserSig？
如果您是后台研发工程师，剩下的工作就不需要您操心了，您可以通知您的同事（终端开发工程师）阅读 IM SDK 的接入文档（[iOS](https://cloud.tencent.com/document/product/269/9149) | [Android](https://cloud.tencent.com/document/product/269/9233)），完成后续接入工作。

