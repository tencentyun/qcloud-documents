腾讯云统计客户投诉中关于推流不成功的原因，主要集中在如下三个点上：
![](//mc.qcloudimg.com/static/img/b7f0fb7d7115c87e2748ada5fdaf971b/image.png)

## txSecret 不正确
腾讯云目前要求推流地址都要加防盗链以确保安全，防盗链计算错误或者已经过了有效期的推流URL，都会被腾讯云**踢掉**，这种情况下 RTMP SDK 会抛出 **PUSH_WARNING_SERVER_DISCONNECT** 事件， [RTMP SDK DEMO](https://cloud.tencent.com/document/product/454/6555) 此时的表现如下：
![](//mc.qcloudimg.com/static/img/83e5c2dce6707f5c0c5e6dfc8fc548e5/image.png)

阅读 [如何获取推流URL？](https://cloud.tencent.com/document/product/454/7915) 了解如何获取可靠的推流URL。

## txTime 已过期
有些客户担心自己的直播流量被人盗用，会将 txTime 设置的过于保守，比如从当前时间开始往后推 5 分钟。其实由于有 txSercet 签名的存在，txTime 的有效期不用设置的太短。相反，如果有效期设置的太短，当主播在直播过程中遭遇网络闪断时，会因为推流 URL 过期而无法恢复推流。

txTime 建议设置为当前时间往后推 12 或者 24 小时为宜，也就是要长于一场普通直播的直播时间。

## 推流URL被占用
一个推流 URL 同时只能有一个推流端，第二个尝试去推流的 Client 会被腾讯云拒绝掉，这种情况下 RTMP SDK 会抛出 **PUSH_WARNING_SERVER_DISCONNECT** 事件。

## 连不上云服务器
RTMP推流所使用的默认端口号是 **1935** ，如果您测试时所在网络的防火墙不允许 1935 端口通行，就会遇到连不上与服务器的问题。此时，您可以通过切换网络（比如 4G ）来排查是不是这个原因导致的问题。

## 小直播推流地址
小直播的推流 URL 可以用调试的办法获取，您可以全局搜索代码寻找关键字 **startPush**，然后在此处打下调试断点，这里是小直播对 RTMP SDK 的调用点，startPush 的参数即为推流URL。



