## 1. 业务后台配置参数错误有什么表现？
### 1.1 appid 或者 bizid 
主要表现 主播端推流一直失败。原因主要是生成推流地址无效，腾讯云拒绝推流请求。从log中可以看到**RTMP服务器主动断开**的信息。

![](//mc.qcloudimg.com/static/img/e3b6f9f974f561e0e3ef182580445673/image.png)

### 1.2 推流防盗链key 
主要表现直播端推流一直失败。主要原因是推流防盗链key参入了txSecret的计算，推流防盗链key错误，导致txSecret错误，最终导致服务器对txSecret校验失败，被腾讯云拒绝。从log中可以看到**RTMP服务器主动断开**的信息。

![](//mc.qcloudimg.com/static/img/fca49e4e78c906ff27461fa8594b6d58/image.png)

### 1.3  API鉴权key 
主要表现推流播放均正常，但是没有在终端的回看列表中。
回看记录生成过程：
- 直播结束，腾讯云录制完成通知小直播后台，就是您在控制台配置的回调URL来进行通知的。
- 小直播后台用API鉴权key校验回调的合法性。校验失败的话，就不会在数据库插入回看记录。
- 校验通过，会向tape_data表中写入一条回看记录。
- 写入数据库成功，你才会真正有一条回看记录。
 
主要原因分是API鉴权key配置错误，导致业务后台对回调的鉴权失败，最终没有生成回看记录。

### 1.4  COS APPID 
主要表现头像和封面的上传失败。主要原因是COS 上传请求所用到的签名是由业务后台下发的。由于签名错误，导致COS上传请求失败。通过终端的日志关键字 “**ERROR_PROXY_APPID_USERID_NOTMATCH**”可以确认。

![](//mc.qcloudimg.com/static/img/378e8a055f12f6aa77b2958ad1c3f149/image.png)

### 1.5  COS Bucket名称 
主要表现 头像和封面的上传失败。主要原因是COS Bucket可以理解是一个虚拟磁盘，磁盘指定错了，COS上传就失败，报找不到Bucket的错误。通过终端的日志关键字 “**ERROR_PROXY_SIGN_BUCKET_NOTMATCH**”可以确认。
 
 ![](//mc.qcloudimg.com/static/img/92e096149bef3408c9713df93ab321ac/image.png)
 
### 1.6 COS SecretId 
 主要表现头像和封面的上传失败。主要原因 COS 上传请求所用到的签名是由业务后台下发的。COS SecretId 用来指定签名用的秘钥，需和COS SecretKey配对使用。通过终端的日志关键字 “**PROXY_AUTH_SECRETID_NOEXIST**”可以确认。
 
 ![](//mc.qcloudimg.com/static/img/3fbfd0180fc165784c1ce30e513be5c7/image.png)
 
### 1.7  COS SecretKey 
 主要表现头像和封面的上传失败。主要原因COS 上传请求所用到的签名是由业务后台下发的。COS SecretKey错误导致签名失败。通过终端的日志关键字 “**ERROR_PROXY_AUTH_FAILED**”可以确认。
 
 ![](//mc.qcloudimg.com/static/img/f1ac76d8ea4b70b883c4a45d74ee888d/image.png)

## 2. 终端（ios为例）参数错误有什么表现？
### 2.1 kTCIMSDKAppId 或者 kTCIMSDKAccountType
主要表现登录失败。

![](//mc.qcloudimg.com/static/img/0b18fc2a7d5f7f86bbd4d56f743cee1e/image.png)

### 2.2 kTCCOSAppId 或者 kTCCOSBucket
主要表现头像或封面上传失败。log表现如下：

![](//mc.qcloudimg.com/static/img/4192cf72b525664098fb69cd2e02ba7c/image.png)

### 2.3 kTCCOSRegion 
主要表现像或封面上传失败。主要原因是 kTCCOSRegion 是 COS 4.0 新增的参数，用于指定COS 机房的位置，设置错误会提示Bucket找不到。log表现如下：

![](//mc.qcloudimg.com/static/img/b023701ec5c2fe69ab35816b422afe16/image.png)

### 2.4 kHttpServerAddr 
主要表现拉取列表等相关功能异常，提示请求超时。主要原因是server的地址错误导致终端没有访问到正确的后台服务。

![](//mc.qcloudimg.com/static/img/c1ce2290019c67ae00395be67360e3d5/image.png)

## 3. 为何拉取回看列表失败？
回看列表生成过程在 **1.3  API鉴权key** 有说明。回看列表是存放在数据 tape_data表中的。遇到拉取失败可以从以下几个方面一一排查。

![](//mc.qcloudimg.com/static/img/f28487d33a502e571737bc9c687647ac/image.png)

### 3.1 回调后写数据库是否正常
 一般您不改动我们的的后台源码，一般不会有问题。如果您有改动到createDB脚本，那么就有必要排查一下这里。log是一个很好的排查问题的工具。后台开启调试log的方法，是在 live_demo_service/目录下创建 log 目录，即可。关注 mysql_XXXX.log。可能是字段属性修改，导致了数据库插入操作失败。
 
### 3.2 API鉴权Key是否正确
 确保OutDefine.php 中 CALL_BACK_KEY的值和控制台API鉴权Key一致，他的作用前文已解释。
 
### 3.3 回调URL设置是否正确
 检查腾讯云官网-管理中心-直播-接入管理-直播码接入-接入配置中回调URL是否正确填写。如果错误的话，直播结束后，业务后台收不到腾讯云服务器的通知回调，也就没有生成回看纪录。
 
![](//mc.qcloudimg.com/static/img/61187098d48fecd3f4554d45a8503aa6/image.png)

## 4. 为何拉取播放列表失败？
主要依赖数据库的live_data（直播列表）和tape_data（回看列表）两个表来生成的。确保 **kHttpServerAddr** 没有填错，终端网络正常的情况下。可以排查一下server。
Android app登录之后提示拉取列表失败，logcat中可以看到信息“**HTTP Req error, error code:500**”，iphone app登录后提示**internal server error**。后台log目录下的mysql_errorxxxxxxxx.log打开可以看到信息**mysqli_connect failed, error:Access denied for user 'live_user'@'localhost' to database 'live'**]
由于数据库访问失败导致接口失败。确认方法在live_demo_service/conf 目录下打开 cdn.route.ini 文件，确保DB 参数和您创建数据库时指定的是一致的。PHP通过cdn.route.ini指定的参数来访问本地数据库的。具体对应关系如图：

![](//mc.qcloudimg.com/static/img/1a5a63e3ac06eb9eab85a0b0ed1b8879/image.png)


## 5. 为何拉取头像或封面失败？
主要表现上传头像或者封面成功，但是下载头像或封面失败。主要原因是COSv4版本的域名加速默认是关闭的。而COS上传返回的是CDN的地址，可以设置域名加速解决。

![](//mc.qcloudimg.com/static/img/a2fd6cf344295b547d8d7c417142af45/image.png)

## 6. 为何COS参数设置没有问题但上传还是失败？
- **主要表现** COS参数，终端和小直播后台设置正确。但是头像和封面上传还是失败。
- **主要原因** 2016年11月份 COS 服务端进行了一次版本升级，增加了区域参数。新的系统和旧系统是完全独立的两套，需要分别配合对应终端的cos sdk版本才能使用。新开通COS服务的都是v4版本。老版本COS可以 [提交工单](https://console.cloud.tencent.com/workorder/category/create?level1_id=83&level2_id=84&level1_name=%E5%AD%98%E5%82%A8%E4%B8%8ECDN&level2_name=%E5%AF%B9%E8%B1%A1%E5%AD%98%E5%82%A8%20COS) 申请切成新版COS。2016年12月30日开始小直播源码包也搭载了终端cos sdk v4版本。bucket可以理解为是COS 中的一个虚拟硬盘。老版本的COS服务端创建的bucket，用新版本cos sdk v4上传是会失败的 报 **bucket notexist **的错误。
- **解决办法** 是在cos v4平台下创建一个新的bucket，将后台和终端COS相关参数更新为新的bucket即可。

## 7. 注册或登录返回“登录失败注册操作被安全打击”
一般是由于在同一网络下注册操作过于频繁而被后台拒绝，请降低注册频率。

## 问题不在列表中怎么办？
可以[提交工单](https://console.cloud.tencent.com/workorder/category/create?level1_id=29&level2_id=307&level1_name=%E8%A7%86%E9%A2%91%E4%B8%8E%E9%80%9A%E4%BF%A1%E6%9C%8D%E5%8A%A1&level2_name=%E7%A7%BB%E5%8A%A8%E7%9B%B4%E6%92%ADMLVB%EF%BC%88%E5%B0%8F%E7%9B%B4%E6%92%AD%EF%BC%89)反馈给我们。
