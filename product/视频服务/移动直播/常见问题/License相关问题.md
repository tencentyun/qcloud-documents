[](id:que1)
### 移动直播 License 是必须购买的吗？
移动直播 SDK 的直播推流功能，必须通过购买移动直播 License 进行解锁。
>! 短视频 License 无法解锁移动直播相关功能。


[](id:que2) 
### 移动直播 License 有单独购买入口吗？
不支持单独购买。
- 直播推流 License（原移动直播基础版 SDK License） ：需购买云直播10TB及以上 [流量资源包](https://cloud.tencent.com/document/product/267/34174) 获取一年使用授权。
- 移动直播企业版 SDK License：需 [联系腾讯云商务](https://cloud.tencent.com/apply/p/h1qsz5vhvko) 申请。

[](id:que3)
### 直播推流 License（原移动直播基础版 SDK License） 和移动直播企业版 License 有什么区别？
直播推流 License（原移动直播基础版 SDK License） 即可解锁直播推流和播放功能，以及基础的美颜功能（美白、磨皮等）。
移动直播企业版 License 是在其之上，增加了高级美颜（大眼、瘦脸）、绿幕功能、动效贴纸、AI 抠图等能力，还可以配合美妆和手势素材实现额外的功能。

>?
>- SDK 下载中的3个版本的 SDK 均可用直播推流 License（原移动直播基础版 SDK License） 来解锁直播推流和播放功能。
>- 企业版中的高级美颜相关功能只能通过移动直播企业版 License 来解锁。


[](id:que4)
### 一个账号下能创建多个 License 吗？
同一个账号下创建 License 的数量没有限制。为了方便用户管理，相同包名的 License 建议通过续期的方式延长有效时间。

[](id:que5)
### 相同包名可以创建多个 License 吗？
可以，多个 License 填写相同的包名不会影响使用，不过同时创建多个 License 有效期会各自计算，一般不建议创建多个相同包名的 License。

[](id:que6)
### License 可以修改吗？
移动直播 License 可通过续期来延长有效时间，包名信息不支持修改，请您在添加 License 先核对包名在应用商店里是否被占用，提交后不支持修改和替换。

[](id:que7)
### 为什么我创建了多个 License ，但是 licenseurl 和 key 都是一样的？
同一个账号下移动直播的 licenseurl 和 key 默认是相同的。这样保证了测试 License 、正式 License、不同包名的 License 均可以复用相同的接口信息。

>?不建议使用免费测试的 License 发布到线上运行。您可以通过添加新的正式版 License，即可无需再修改接口中的 licenseurl 和 key，切换到正式版 License。

[](id:que8)
### 关联 License 的资源包是不是只能这个 License 使用？
该账号下的标准直播播放域名产生的日结流量后付费消耗均可抵扣。资源包关联只是用于同步有效期，里面的流量不限于 License 使用（流量用尽也不影响 License 的使用）。
**例如：**
用户甲是日结流量后付费计费，购买了一个10TB标准直播流量包和50TB标准直播流量包，分别创建了 License A 和 License B：
   - License A 对应的 App 使用的是`abc.com`域名播放，产生了20TB的播放流量。
   - License B 对应的 App 使用的是`def.com`域名播放，产生了30TB的播放流量。

只要`abc.com`和`def.com`这两个是属于用户甲云直播账号下标准直播的播放域名，即可使用购买的10TB + 50TB来抵扣，抵扣后用户甲的标准直播流量包剩余10TB流量。  

[](id:que9)
### 购买移动直播 License 可以用于小程序直播吗？
不支持，移动直播 License 仅支持 iOS 和 Android 端的 App 在使用移动直播 SDK 直播功能时使用。小程序端接入直播功能需要先具备对应的服务类目，详情参见 [方案选择](https://cloud.tencent.com/document/product/1078/37707)。  
