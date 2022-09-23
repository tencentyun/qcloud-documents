## TUICallKit API 简介

TUICallKit API 是音视频通话组件的**含 UI 接口**，使用TUICallKit API，您可以通过简单接口快速实现一个类微信的音视频通话场景，更详细的接入步骤，详情请参见 [快速接入TUICallKit](https://cloud.tencent.com/document/product/647/78730?!preview)。

## API 概览

| API | 描述 |
|-----|-----|
| [createInstance](#createinstance)       | 创建 TUICallKit 实例（单例模式） |
| [setSelfInfo](#setselfinfo)             | 设置用户的昵称、头像             |
| [call](#call)                           | 发起 1v1 通话                    |
| [groupCall](#groupcall)                 | 发起群组通话                     |
| [joinInGroupCall](#joiningroupcall)     | 主动加入当前的群组通话中         |
| [setCallingBell](#setcallingbell)       | 设置自定义来电铃音               |
| [enableMuteMode](#enablemutemode)       | 开启/关闭静音模式                |
| [enableFloatWindow](#enablefloatwindow) | 开启/关闭悬浮窗功能              |

## API 详情

### createInstance
创建 TUICallKit 的单例。

```objc
- (instancetype)createInstance;
```

### setSelfInfo
设置用户昵称、头像。用户昵称不能超过500字节，用户头像必须是 URL 格式。

```objc
- (void)setSelfInfo:(NSString * _Nullable)nickname avatar:(NSString * _Nullable)avatar succ:(TUICallSucc)succ fail:(TUICallFail)fail
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| nickName | NSString | 目标用户的昵称 |
| avatar | NSString | 目标用户的头像 | 

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
发起群组通话，注意：使用群组通话前需要创建IM 群组，如果已经创建，请忽略。

```objc
- (void)groupCall:(NSString *)groupId userIdList:(NSArray<NSString *> *)userIdList callMediaType:(TUICallMediaType)callMediaType;
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| groupId | NSString | 此次群组通话的群 ID |
| userIdList | NSArray | 目标用户的 userId 列表 |
| callMediaType | TUICallMediaType | 通话的媒体类型，比如视频通话、语音通话 |

### joinInGroupCall
发起群组通话，注意：使用群组通话前需要创建IM 群组，如果已经创建，请忽略。

```objc
- (void)joinInGroupCall:(TUIRoomId *)roomId groupId:(NSString *)groupId callMediaType:(TUICallMediaType)callMediaType;
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomId | TUIRoomId | 此次通话的音视频房间 ID，目前仅支持数字房间号，后续版本会支持字符串房间号 |
| groupId | NSString | 此次群组通话的群 ID |
| callMediaType | TUICallMediaType | 通话的媒体类型，比如视频通话、语音通话 |

### setCallingBell
设置自定义来电铃音。
这里仅限传入本地文件地址，需要确保该文件目录是应用可以访问的。
- 铃声设置后与设备绑定，更换用户，铃声依旧会生效。
- 如需恢复默认铃声，`filePath` 传空即可。

```objc
- (void)setCallingBell:(NSString *)filePath;
```

### enableMuteMode
开启/关闭静音模式。

```objc
- (void)enableMuteMode:(BOOL)enable;
```

### enableFloatWindow
开启/关闭悬浮窗功能。
默认为`false`，通话界面左上角的悬浮窗按钮隐藏，设置为 true 后显示。

```objc
- (void)enableFloatWindow:(BOOL)enable;
```
