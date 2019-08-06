

## 导读
本文主要介绍IM SDK Demo Android版本的简单使用。包括源码下载地址，图文结合的使用向导，基础功能的展示等，希望用户通过本文，对IMSDK的基本功能有一个系统的认识。

**基本功能列表:**

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
| 个人设置 | 用户昵称设置(头像设置Demo中不提供，SDK支持头像设置) |

## 应用商店下载

随心聊IM在应用宝上架地址：http://android.myapp.com/myapp/detail.htm?apkName=com.tencent.qcloud.timchat

<img src="//mccdn.qcloud.com/static/img/c231fdc846106f2e1de017b41c9ac141/image.png" width=320>

可下载安装试用。

## 源码下载与编译
### 从github下载
从[github](https://github.com/zhaoyang21cn/Android_Suixinliao)下载源码。
### 从官网下载
从[官网](https://cloud.tencent.com/product/im.html)下载IM Android SDK。
工程路径：IM_iOS_SDK_x.x.x/samples/sample , 其中x.x.x是版本号。用Android Studio打开（File ->open）sample工程即可。
## Demo使用
### 注册和登录
#### 手机号注册和登录
Demo支持手机号注册登录。填入手机号和手机号所在地，然后单击获取验证码。收到验证码后，填写正确验证码即可登录。
<img src="//mccdn.qcloud.com/static/img/f8576103a512565ae4426cba9358fa0b/image.png" width=360/>
#### 帐号密码注册和登录
Demo支持帐号密码注册登录。按照界面提示填入用户名和密码注册，注册成功后会自动登录。
<img src="//mccdn.qcloud.com/static/img/27b471be081822ba5ec289272671faa2/image.png" width=360/>
使用已经注册的帐号登录，单击进入用户名登录界面，填写用户名和密码，单击登录按钮即可登录。
<img src="//mccdn.qcloud.com/static/img/ca08651f039eeb2ad3eaf4c18008813e/image.png" width=360/>
### 联系人
#### 添加好友
Demo主界面的第二个tab为联系人，在联系人tab中单击右上角按钮，然后选择添加好友。
<img src="//mccdn.qcloud.com/static/img/3352b17b669d2844547b6f1ec9defb92/image.png" width=360/>
在添加好友界面里搜索（使用软键盘搜索按钮）指定的帐号或名称。搜索结果在下方以列表形式显示。
<img src="//mccdn.qcloud.com/static/img/408c7fb67ef3ec938a656ca9ca641e1f/image.png" width=360/>
选择一个需要添加的对象，进入添加好友界面。可以在添加好友界面设置备注名，分组，附加信息，然后发送添加请求，对方同意请求后即成为好友。
<img src="//mccdn.qcloud.com/static/img/ef062d61e5a6698e8ff6606ddbc244e0/image.png" width=360/>
#### 新朋友
新朋友中显示好友未决、已决列表(已经拒绝添加的好友不会显示)。用户的申请加好友信息可在这里进行审核，同时可以查看已经添加过哪些好友。
<img src="//mccdn.qcloud.com/static/img/bda68e6d1417c5c7a2e43c03661f0805/image.png" width=360/>
#### 好友分组管理
在联系人界面中好友可以分组显示，用户可以在联系人详细资料界面设置这个联系人的分组。
<img src="//mccdn.qcloud.com/static/img/b1a659ed918c9560c36ed5a8399400fb/image.png" width=360/>
### 群组
Demo中群组分为三种不同类型，分别是公开群，讨论组，聊天室。上述三种群有各自不同的特征，详见SDK文档。用户也可以自定义自己的群组类型。
#### 创建群
在公开群/讨论组/聊天室列表中选择右上角创建按钮，进入创建群界面。
<img src="//mccdn.qcloud.com/static/img/d9a1d7fe513f7ef9e0799439f7ac92ce/image.png" width=360/>
选择群名称和邀请的群成员，然后创建群。
<img src="//mccdn.qcloud.com/static/img/26bf8a0f0e3a207a52b2f6413350dd97/image.png" width=360/>
<img src="//mccdn.qcloud.com/static/img/48da99b55679de174e2dca85ac56614a/image.png" width=360/>
#### 群组消息
群管理员收到他人申请加群，或者邀请入群等需要处理的群管理消息时，会收到群组消息。群组消息会在会话列表中显示。用户可以在群组消息里面处理相关的群组事务。
<img src="//mccdn.qcloud.com/static/img/ae43276cfbe20639bae43bd80e10da1d/image.png" width=360/>
### 聊天
Demo支持文本，表情，图片，语音，小视频的收发。
<img src="//mccdn.qcloud.com/static/img/0c8b473c0a4a720990632985c8d20ea6/image.png" width=360/>
### 关于
在设置tab中单击进入关于页面。在关于页面中可以查看当前Demo使用的IMSDK，QAL，TLS的版本号，一般来说Demo中使用了当前发布包中的SDK，遇到使用问题SDK版本是一个重要的信息。另外在关于中可以设置日志等级，设置后需要杀掉进程重启才能生效。
<img src="//mccdn.qcloud.com/static/img/25939945c1a4a997473a8f304f2ce17e/image.png" width=360/>
