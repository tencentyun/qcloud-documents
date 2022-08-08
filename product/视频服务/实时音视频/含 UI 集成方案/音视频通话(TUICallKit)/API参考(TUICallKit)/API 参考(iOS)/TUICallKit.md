## TUICallKit API 简介

TUICallKit API 是音视频通话组件的**含 UI 接口**，使用TUICallKit API，您可以通过简单接口快速实现一个类微信的音视频通话场景，更详细的接入步骤，详见：[快速接入TUICallKit（）]()

<h2 id="TUICallKit">API 概览</h2>


| API | 描述 |
|-----|-----|
| [createInstance](#sharedinstance) | 创建 TUICallKit 实例（单例模式）|
| [setSelfInfo](#setSelfInfo) | 设置用户的头像、昵称|
| [call](#call) | 发起 1v1 通话|
| [groupCall](#groupCall) | 发起群组通话|
| [joinInGroupCall](#joinInGroupCall) | 主动加入当前的群组通话中 |
| [setCallingBell](#setCallingBell) | 设置自定义来电铃音 |
| [enableMuteMode](#enableMuteMode) | 开启/关闭静音模式 |
| [enableFloatWindow](#enableFloatWindow) | 开启/关闭悬浮窗功能 |

<h2 id="TUICallKit">API 详情</h2>

### createInstance
创建 TUICallKit 的单例。
```objc
- (instancetype)createInstance;
```
### call
拨打电话（1v1通话）

```objc
- (void)call:(NSString *)userId callMediaType:(TUICallMediaType)callMediaType;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString | 目标用户的userId |
| callMediaType | TUICallMediaType | 通话的媒体类型，比如视频通话、语音通话 |

### groupCall
发起群组通话，注意：使用群组通话前需要创建IM 群组，如果已经创建，请忽略；

```objc
- (void)groupCall:(NSString *)groupId userIdList:(NSArray<NSString *> *)userIdList callMediaType:(TUICallMediaType)callMediaType;
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| groupId | NSString | 此次群组通话的群 Id. |
| userIdList | NSArray | 目标用户的userId 列表 |
| callMediaType | TUICallMediaType | 通话的媒体类型，比如视频通话、语音通话 |

### joinInGroupCall
发起群组通话，注意：使用群组通话前需要创建IM 群组，如果已经创建，请忽略；

```objc
- (void)joinInGroupCall:(TUIRoomId *)roomId groupId:(NSString *)groupId callMediaType:(TUICallMediaType)callMediaType;
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomId | TUIRoomId | 目标用户的userId 列表 |
| groupId | NSString | 此次群组通话的群 Id. |
| callMediaType | TUICallMediaType | 通话的媒体类型，比如视频通话、语音通话 |


### setCallingBell
设置自定义来电铃音，这里仅限传入本地文件地址，需要确保该文件目录是应用可以访问的。

```objc
- (void)setCallingBell:(NSString *)filePath;
```

### enableMuteMode
开启/关闭静音模式。

```objc
- (void)enableMuteMode:(BOOL)enable;
```


### enableFloatWindow
开启/关闭悬浮窗功能，设置为false后，通话界面左上角的悬浮窗按钮会隐藏。

```objc
- (void)enableFloatWindow:(BOOL)enable;
```

