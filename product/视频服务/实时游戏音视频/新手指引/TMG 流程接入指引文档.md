## TMG 流程接入指引文档
### 一、账号开通
### 1. 接入概述
主要分如下几步：
1. 注册腾讯云账号
2. 开通互动直播
3. 创建应用
4. 信令通道开通

### 2. 详细步骤
#### 2.1 注册腾讯云账号
注册腾讯云账号并完成相关资料的提交，支持邮箱、微信、QQ 多种方式参考 [如何注册成为腾讯云用户](//www.qcloud.com/document/product/378/8415)

不要使用个人QQ号，而是使用公共QQ号，避免后续出现交接问题。

#### 2.2 开通互动直播
通过腾讯云官网[云产品-互动直播](//www.qcloud.com/product/ilvb)。如下图

![开通互动直播](https://mc.qcloudimg.com/static/img/b095673b7245e928ac4418dde3a8336e/image.png)

![填写信息](https://mc.qcloudimg.com/static/img/a26d76e96130caa3cc929e5905ad393d/image.png)

请填写该页面所需信息。
#### 2.3 创建应用
访问腾讯云[业务后台](//www.qcloud.com/login?s_url=https%3A%2F%2Fconsole.qcloud.com%2Filvb)，若没有通过开发者资质审核，需先实名认证，参考[指引](//www.qcloud.com/document/product/378/3629)（推荐使用个人认证）。
填写基本信息后，即可创建一个新应用，获得对应的 AppId 和 AccountType（***注***：谨记这两个参数，接口 SetAppInfo 会使用这两个参数） 

![获得id和type](https://mc.qcloudimg.com/static/img/e52f0fb14bbda2d6915874aaa1036e4d/image.png)

#### 2.4 信令通道开通
接入方式是使用SDK内置的HTTP信令通道，方法如下：
1. 提供 appID 给腾讯云接口人（或者管理员）配置为支持 http 通道；
2. 集成功能时，enterroom 进房操作使用[音视频权限秘钥加密权限位](//www.qcloud.com/document/product/268/3220)，参考下一节音视频秘钥说明。

### 二、 音视频秘钥
### 1. 概述
互动直播提供音视频密钥，用于相关功能的加密和鉴权。目前主要用于上下行权限的加密和跨房间连麦。
* 密钥：APPID 对应音视频密钥的 md5 值，长度16字节
* 加密算法：TEA 加密
* 加密库及例子：附件[tea.zip](https://mc.qcloudimg.com/static/archive/343de5a224bef9be41bb81192affdebb/tea.zip)

在腾讯云后台如下位置获取密钥

![获取秘钥](https://mc.qcloudimg.com/static/img/8a42ee6789477a4074c2fc2b49724f80/image.png)

页面修改密钥后，15分钟 ~ 1小时内生效，不建议频繁更换。
### 2. 进房权限加密

| 字段描述 | 类型/长度 | 值定义/备注 |
|---------|---------|---------|
| cVer | unsigned char/1 | 版本号，填0 |
| wAccountLen | unsigned short /2 | 第三方自己的帐号长度 |
| buffAccount | wAccountLen | 第三方自己的帐号字符 |
| dwSdkAppid | unsigned int/4 | sdkappid |
| dwAuthId | unsigned int/4 | 群组号码，即：roomId |
| dwExpTime | unsigned int/4 | 过期时间 <br>（当前时间 + 有效期（单位：秒，建议300秒））  |
| dwPrivilegeMap | unsigned int/4 | 权限位， 建议：<br>纯音频场景<br>需要上麦建议设置为：AUTH_BITS_CREATE_ROOM&#124;AUTH_BITS_JOIN_ROOM&#124;<br>AUTH_BITS_SEND_AUDIO&#124;AUTH_BITS_RECV_AUDIO<br>不需要上麦建议设置为：AUTH_BITS_CREATE_ROOM&#124;AUTH_BITS_JOIN_ROOM&#124;<br>AUTH_BITS_RECV_AUDIO<br>视频场景：<br>需要上麦建议设置为：AUTH_BITS_CREATE_ROOM&#124;AUTH_BITS_JOIN_ROOM&#124;<br>AUTH_BITS_SEND_AUDIO&#124;AUTH_BITS_RECV_AUDIO&#124;<br>AUTH_BITS_SEND_CAMERA_VIDEO&#124;AUTH_BITS_RECV_CAMERA_VIDEO&#124;<br>AUTH_BITS_SEND_SCREEN_VIDEO&#124;AUTH_BITS_RECV_SCREEN_VIDEO<br>不需要上麦建议设置为：AUTH_BITS_CREATE_ROOM&#124;AUTH_BITS_JOIN_ROOM&#124;<br>AUTH_BITS_RECV_AUDIO&#124;AUTH_BITS_RECV_CAMERA_VIDEO&#124;<br>AUTH_BITS_RECV_SCREEN_VIDEO<br>[更详细说明请查看这里](//www.qcloud.com/document/product/268/3227) |
| dwAccountType | unsigned int/4 | 第三方帐号类型，[在这里可以找到](//www.qcloud.com/login?s_url=https%3A%2F%2Fconsole.qcloud.com%2Filvb) |

#### 2.1 密文内容

#### 2.2 加密方法
1. 点击下载 [google protobuf](//github.com/google/protobuf) 使用，序列化后，输出二进制字符串；
2. 密文中的数字转换成网络字节序（大端字节序）,把加密串转换成16进制字符串，大小写均可；
3. 3.用 tea 加密对二进制字符串加密，symmetry_encrypt 函数输出的字符串即为加密串（authBuf）；

#### 2.3 使用方法
后台生成加密串（authBuf）后，下发给客户端。

客户端进房时调用 JoinRoom 函数时，传入 authBuf。