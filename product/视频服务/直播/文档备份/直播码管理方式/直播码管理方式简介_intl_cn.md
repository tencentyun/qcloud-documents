直播码管理方式为需要集中式管理直播的高并发直播活动的用户提供了基于“域名+直播码”的管理方式。

这种方式同基于“直播频道”概念的最大区别是：

#### 1. 直播频道
频道的推流和拉流地址，为系统指定，用户无法自定义；且需要通过API或控制台提前申请；
![](//mccdn.qcloud.com/static/img/d69db1638b3fe56b5ab4404bd07701b1/image.png)

例如： 用户发起申请后，获得类似如下信息
直播频道ID:   160931048506819*****
直播推流地址：rtmp://2000.livepush.myqcloud.com/live/2000_f3d7cff5e69511e5b91fa4dcbe*****?bizid=2000
直播收看地址：http://2000.liveplay.myqcloud.com/2000_f3d7cff5e69511e5b91fa4dcbef*****.m3u8

#### 2. 直播码

在腾讯云配置固定域名后，用户可以使用自定义直播码来区分不同的直播活动。推流和播放地址无需事先申请。
![](//mccdn.qcloud.com/static/img/c8bf4d030358304f3af86737492e7bd9/image.png)

例如： 用户获得腾讯云分配的如下域名： 5000.livepush.myqcloud.com/live/
则可自定义直播码，例如5000__ test2016011415 （前面5000_为固定前缀，和域名前缀一致）
##### 对应直播推流地址：
rtmp://5000.livepush.myqcloud.com/live/5000_test2016011415
##### 对应rtmp/hls直播播放地址：
rtmp://5000.liveplay.myqcloud.com/live/5000_test2016011415
http://5000.liveplay.myqcloud.com/5000_test2016011415.m3u8


#### 注意：
当前直播码管理方式仅提供给部分客户使用。暂不开放注册和服务申请。
直播频道相关功能和操作方式，不适用于直播码管理方式。