## SDK开发
- 调用云支付即可使用云支付提供的对外接口，也可以使用SDK提供的接口，SDK对请求参数进行打包、签名、封装HTTPS请求等操作使得商户调用云支付系统更加方便。
- 当前SDK只支持刷卡支付、查询订单、撤单、门店上传、门店下载5个接口。其中刷卡支付为异步方式，刷卡接口调用成功只代表支付提交成功，支付结果需要通过查询订单得到。撤单接口为同步调用云支付接口。后续会提供其他场景的接口。
- 当前只提供了windows环境下的SDK，后续会提供其他环境。[点击下载SDK](https://)
## windows下的SDK使用说明
### 支付类 ###
- 初始化函数

使用云支付类接口时需要在进程启动时调用初始化函数，函数定义如下：

![](https://mc.qcloudimg.com/static/img/8467956ce8023751457553f8e5eeb730/image.png)

初始函数的参数打包的格式如下图，其中有些参数可以不用设置，如果不设置，会使用系统的默认值，建议使用默认值。

![](https://mc.qcloudimg.com/static/img/48d7fb3ec045bc4578f85dbaf4aab608/image.png)

初始参数打包例子：

![](https://mc.qcloudimg.com/static/img/e9956b2451c74fdebb3654d4eb20ab53/image.png)

- 结束函数

使用云支付类接口时需要在进程退出时调用结束函数，函数定义如下：

![](https://mc.qcloudimg.com/static/img/025565506110172861aada26e31e56f5/image.png)

- 刷卡支付

接口定义如下，返回0表示受理支付成功，-1表示受理失败。如果支付受理成功，并不表示支付成功，需要通过查单接口去查询是否支付成功。

![](https://mc.qcloudimg.com/static/img/0cfdb97230024a8782dbd33813476ccb/image.png)

构造刷卡支付请求参数的例子：

![](https://mc.qcloudimg.com/static/img/86c0df6aabe415992a81b79393c6a116/image.png)

调用SDK刷卡支付接口的例子：

![](https://mc.qcloudimg.com/static/img/9cdc522402c312881e0d722fa725ed25/image.png)

- 查询订单

可以查询一个订单的支付结果，支付成功则返回具体的订单信息，接口定义如下：

![](https://mc.qcloudimg.com/static/img/96050fc5a9d5967e2123b1fbe5e58b88/image.png)

构造查询订单请求参数的例子：

![](https://mc.qcloudimg.com/static/img/4115697df52d15e320e38a757f883d79/image.png)

调用SDK查单接口的例子：

![](https://mc.qcloudimg.com/static/img/ee4effb08cc8aeb52174c42b21bba375/image.png)

如果支付成功，订单信息保存在order中，为json格式，需要按照cloud_pay_sdk.proto中OrderSdk的结构去解析具体的订单信息。

- 撤单订单

商户可以主动调用撤单接口，撤单接口为同步调用云支付的撤单接口。

![](https://mc.qcloudimg.com/static/img/ab9b90d624442171ec0ca01b90de34d8/image.png)

构造撤销订单请求参数的例子：

![](https://mc.qcloudimg.com/static/img/cb7e1634b485fead75e95c7d6a5758c9/image.png)

调用SDK撤销订单接口的例子：

![](https://mc.qcloudimg.com/static/img/2ffd3ce5845656e809a90dbfead44ec5/image.png)

### 门店类 ###

- 初始化函数

调用门店的接口，需要先调用门店相关的初始化函数。

![](https://mc.qcloudimg.com/static/img/ac910ffb35e3823df41eaf5e857e0604/image.png)

初始函数的参数打包的格式如下图，其中有些参数可以不用设置，如果不设置使用系统的默认值，建议使用默认值。

![](https://mc.qcloudimg.com/static/img/a0d0c863e9fee8b529375dc91d2d93a4/image.png)

构造门店初始化请求参数的例子：

![](https://mc.qcloudimg.com/static/img/b2b3f609f6e78bd152a7ff0f1565155a/image.png)

- 设置门店信息

接口定义如下：

![](https://mc.qcloudimg.com/static/img/9f89cdd93c3ba64f9a04c702f95c42e0/image.png)

构造门店请求的参数的例子：

![](https://mc.qcloudimg.com/static/img/26abe441c73affc7794c6f667d2b5002/image.png)

调用设置门店接口的例子：

![](https://mc.qcloudimg.com/static/img/834800a1bceeca22a609b958f68b7ede/image.png)

- 查询门店信息

接口定义如下：

![](https://mc.qcloudimg.com/static/img/d5857289db182db67bcf882d6b8611be/image.png)

查询门店接口参数打包的例子：

![](https://mc.qcloudimg.com/static/img/70fe8fd183c2fcdfe4a3a59b3e73ceec/image.png)

调用查询门店接口的例子：

![](https://mc.qcloudimg.com/static/img/ac464c1d700788e404813440b7eba188/image.png)