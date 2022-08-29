## TUICallKit API 简介

TUICallKit API 是音视频通话组件的**含 UI 接口**，使用 TUICallKit API，您可以通过简单接口快速实现一个类微信的音视频通话场景，更详细的接入步骤，详见：[快速接入TUICallKit](https://cloud.tencent.com/document/product/647/78733?!preview)

[](id:TUICallKit)
## API 概览


| API | 描述 |
|-----|-----|
| [init](#init) | 初始化 TUICallKit |
| [call](#call) | 发起 1v1 通话 |
| [setSelfInfo](#setselfInfo) | 设置用户的头像、昵称 |
| [destroyed](#destroyed) | 销毁 TUICallKit |

[](id:TUICallEngine)
## API 详情

### init
初始化 TUICallKit。

```javascript
init()
```


### call
C2C 邀请通话，被邀请方会收到的回调，如果当前处于通话中，可以调用该函数以邀请第三方进入通话。

```javascript
call({
    userID:"xxxxxxx",
    type:MEDIA_TYPE.AUDIO
})
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userID | String | 目标用户的 userId |
| type | [MEDIA_TYPE](#MEDIA_TYPE) | 通话的媒体类型，AUDIO：语音通话，VIDEO：视频通话 |

[](id:MEDIA_TYPE)
#### 通话的类型

| MEDIA_TYPE | 说明 |
|-----|-----|
| AUDIO | 音频 |
| VIDEO | 视频 |

### setSelfInfo
设置用户头像、昵称的接口。

```javascript
setSelfInfo('xxxxxxx','头像.png') ;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| nickName | String | 设置昵称 |
| avatar | String | 头像地址 |

### destroyed
销毁 TUICallKit。

```javascript
destroyed()
```