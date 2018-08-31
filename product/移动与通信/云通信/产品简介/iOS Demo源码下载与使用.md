
## 导读
本文主要介绍IM SDK Demo iOS版本的简单使用。包括源码下载地址，图文结合的使用向导，基础功能的展示等，希望用户通过本文，对IMSDK的基本功能有一个系统的认识。
基本功能列表

| 功能名称 | 功能概述 |
|---------|---------|---------|
| 注册 | 手机号注册，ID注册(注册之后生成唯一ID，以登录时使用) |
| 登录/登出 | 使用注册所得ID以及密码登录IMSDK(登出IMSDK) |
| 获取最近会话 | 获取最近会话列表，按时间排序(最新的会话排列在最靠前的位置) |
| 获取最后一条消息 | 获取会话的最新的一条消息(通常这个功能用于会话列表的展示) |
| 获取消息时间戳 | 获取发送/接收的消息时间戳(通常这个功能用于会话列表的展示) |
| 获取好友列表 | 获取好友列表，并且分组显示(提供好友分组功能) |
| 获取群列表 | 获取公开群(Public),私有群(Private),聊天室(chatRoom) |
| 获取未决信息 | 获取好友添加，加群申请等未决信息 |
| 添加好友 | 查找并添加好友,同意好友申请,拒绝好友申请等操作(可带备注信息) |
| 添加群组 | 查找并添加群组,同意添加，拒绝添加等操作(可带备注信息) |
| 群组操作 | 包括群名称,群介绍,群名片,群消息提醒,管理员,禁言,加群验证,加群,退群,邀请加群,获取群成员列表等相关操作 |
| 好友设置 | 包括备注名,分组设置,加入黑名单,删除好友等相关操作 |
| 消息收发 | 支持文本,图片,表情,文件,语音,小视频消息,支持消息漫游(7天) |
| 黑名单 | 提供黑名单功能(加入黑名单的好友会自动解除好友关系,移除黑名单不会自动恢复好友关系) |
| APNS | Demo中提供APNS的实现方法，由于Demo中是企业证书，用户无法感知到消息推送，可以参考Demo中的代码进行APNS的开发(App Store中下载安装是可以体验推送功能的) |
| 个人设置 | 用户昵称设置(头像设置Demo中不提供，SDK支持头像设置) |


## AppStore 下载

Demo在AppStore上名为“随心聊IM”，下载地址：https://itunes.apple.com/cn/app/sui-xin-liaoim/id1112479040?mt=8

<img src="//mccdn.qcloud.com/static/img/71db8d792764f22984f8a644f879aa5a/image.png" width=320 />

## 从源码下载并构建

### 从官网下载
从[官网](https://cloud.tencent.com/product/im.html)下载IM iOS SDK压缩包，并解压。
工程路径：IM_iOS_SDK_x.x.x/samples/sample , 其中x.x.x是版本号。eg：IM_iOS_SDK_1.9.1/samples/sample
使用最新版本的Xcode打开工程文件 TIMChat.xcodeproj 即可运行
### 从github下载
从[github](https://github.com/zhaoyang21cn/iOS_Suixinliao)下载源码，所有配置与官网相同。

注：若使用真机编译不过，请检查Bundle Identifier是否正确

## 登录/注册

### 使用手机号

使用手机号注册、登录流程：
<img src="//mccdn.qcloud.com/static/img/8c4527cda87f3abc7dc25e8cb0681dd2/image.png" width=360 />

### 用户名
使用用户名id注册登录流程：
<img src="//mccdn.qcloud.com/static/img/0cbc851406f865e2ea03e1016e910be8/image.png" width=360 />

### 游客

如果用户只是想简单的体验一下demo，可以直接使用游客登录，无需注册登录帐号，即可体验demo中的功能


## 联系人

### 新朋友

新朋友中显示好友未决、已决列表(已经拒绝添加的好友不会显示)。用户的申请加好友信息可在这里进行审核，同时可以查看已经添加过哪些好友
<img src="//mccdn.qcloud.com/static/img/42b9753addf1988f84c933ab8bdc2cd9/image.png" width=360 />

### 公开群

展示公开群（类型为Public），单击对应的群，可进入到聊天界面，也可在本界面创建公开群
<img src="//mccdn.qcloud.com/static/img/212a1b150a3ecedc6944799d53ed0eaa/image.png" width=360 />

### 讨论组

展示讨论组（类型为Private），单击对应的讨论组，可进入到聊天界面，也可在本界面创建讨论组
<img src="//mccdn.qcloud.com/static/img/2876b83580a3af81fd1b5d96cd597c0d/image.png" width=360 />

### 聊天室

展示聊天室（类型为ChatRoom）单击对应的聊天室。可进入到聊天界面，也可在本界面创建聊天室
<img src="//mccdn.qcloud.com/static/img/68ea8f874540d4355f99691a288fc65e/image.png" width=360 />

### 联系人列表

展示所有的好友，支持分组展示。单击分组名称，收起或展开分组好友，单击对应好友，可进入聊天界面
<img src="//mccdn.qcloud.com/static/img/a65e04f917358d677e14350e50eeef83/image.jpg" width=360 />

### 添加好友

添加好友，添加群组以及分组管理的入口在联系人界面的右上角“＋”。
<img src="//mccdn.qcloud.com/static/img/18976651f50554a3be9bac00bc6e1d6d/image.jpg" width=360 />
添加好友
<img src="//mccdn.qcloud.com/static/img/506b7d2fd9ea71634b72d6588bce4181/image.png" width=360 />

### 添加群组

<img src="//mccdn.qcloud.com/static/img/6cafdeaccfbada9aeec1fe98e25b01c7/image.png" width=360 />

### 分组管理
<img src="//mccdn.qcloud.com/static/img/f80894da99e59d1b6d2bbe759828667c/image.png" width=360 />

## 会话

### 会话列表

展示所有的会话信息，并按照时间的先后顺序展示，最新的会话现在在最顶部
<img src="//mccdn.qcloud.com/static/img/43def83f8eacda056955678c84c29f7c/image.png" width=360 />

## 消息发送

### 文本
<img src="//mccdn.qcloud.com/static/img/127d9d38220b057d649ef683d4158b3c/image.png" width=360 />

### 语音
<img src="//mccdn.qcloud.com/static/img/3fef3c299fe4668a506bf3c13e029f20/image.png" width=360 />
### 图片/文件/小视频
<img src="//mccdn.qcloud.com/static/img/827be0482beb012e800aed5d97a924ff/image.png" width=360 />
### 表情
<img src="//mccdn.qcloud.com/static/img/ec24125aebf6c4bd7e6d5596501b931a/image.png" width=360 />

## 设置

### 个人信息

个人id的展示，昵称的展示和修改

### 好友申请

设置好友申请的审核规则，目前有“同意任何用户加好友”、“拒绝任何人加好友”、“需要验证”三个选项

### 黑名单

添加黑名单
<img src="//mccdn.qcloud.com/static/img/d50599e54cfc0e70dd4b696718bf6353/image.png" width=360 />
展示被加入黑名单的好友列表。

### 控制台日志

显示控制台日志的开关,这个开关主要是方便调试时的使用，打开控制台日志开关，sdk的日志会输出到控制台，不需要再查看caches目录下的日志

### 日志级别

打印到日志文件中的日志级别，debug为最高级别，日志文件所在路径 ：Library/Caches/imsdk_xxxxxxxx.log。调试的时候，最好都设置为Debug级别，方便跟踪问题。

### 退出登录
登出SDK，反初始化App数据，退回登录界面，用户可以再次登录其它帐号。如果登出一个并没有登录的帐号，会返回登出失败。

