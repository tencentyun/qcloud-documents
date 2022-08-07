## TUICallKit API 简介

TUICallKit API 是音视频通话组件的**含 UI 接口**，使用TUICallKit API，您可以通过简单接口快速实现一个类微信的音视频通话场景，更详细的接入步骤，详见：[快速接入TUICallKit（）]()

<h2 id="TUICallKit">API 概览</h2>

| API | 描述 |
|-----|-----|
| [createInstance](#createInstance) | 创建 TUICallKit 实例（单例模式）|
| [destroyInstance](#destroyInstance) | 销毁 TUICallKit 实例（单例模式）|
| [setSelfInfo](#setSelfInfo) | 设置用户的昵称、头像|
| [call](#call) | 发起 1v1 通话|
| [groupCall](#groupCall) | 发起群组通话|
| [joinInGroupCall](#joinInGroupCall) | 主动加入当前的群组通话中 |
| [setCallingBell](#setCallingBell) | 设置自定义来电铃音 |
| [enableMuteMode](#enableMuteMode) | 开启/关闭静音模式 |
| [enableFloatWindow](#enableFloatWindow) | 开启/关闭悬浮窗功能 |

<h2 id="TUICallKit">API 详情</h2>

### createInstance
创建 TUICallKit 的单例。
```javascript
const TUICallKit = uni.requireNativePlugin('TUICallKit');
const sdkAppId = 0;
const userId = 'chard';
const userSig = '';
TUICallKit.createInstance(sdkAppId, userId, userSig);
```
| 参数 | 类型 | 含义 |
|-----|-----|-----|
| sdkAppId | Number | 用户 sdkAppId |
| userId | String | 用户 ID |
| userSig | String | 用户签名 | 

### destroyInstance
销毁 TUICallKit 的单例。
```javascript
const TUICallKit = uni.requireNativePlugin('TUICallKit');
TUICallKit.destroyInstance();
```

### setSelfInfo
设置用户昵称、头像。用户昵称不能超过500字节，用户头像必须是URL格式。

```javascript
const TUICallKit = uni.requireNativePlugin('TUICallKit');
TUICallKit.setSelfInfo(nickname, avatar, (code, message) => {
  if (code === 0) {
    console.log('setSelfInfo success');
  } else {
    console.log(`setSelfInfo failed, error message = ${message}`);
  }
});
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| nickname | String | 目标用户的昵称 |
| avatar | String | 目标用户的头像 | 
| callback | Function | 设置用户昵称、头像回调。code = 0 表示设置成功；code != 0 表示设置失败，失败原因见 message |

### call
拨打电话（1v1通话）

```javascript
const TUICallKit = uni.requireNativePlugin('TUICallKit');
const userId = 'chard';
const callMediaType = 1; // 语音通话(callMediaType = 1)、视频通话(callMediaType = 2)
TUICallKit.call(userId, callMediaType);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 目标用户的userId |
| callMediaType | Number | 通话的媒体类型，比如：语音通话(callMediaType = 1)、视频通话(callMediaType = 2) |

### groupCall
发起群组通话，注意：使用群组通话前需要创建IM 群组，如果已经创建，请忽略；

```javascript
const TUICallKit = uni.requireNativePlugin('TUICallKit');
const groupId = 'myGroup';
const userIdList = ['chard', 'linda', 'rg'];
const callMediaType = 1; // 语音通话(callMediaType = 1)、视频通话(callMediaType = 2)
TUICallKit.groupCall(groupId, userIdList, callMediaType);
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| groupId | String | 此次群组通话的群 Id. |
| userIdList | List | 目标用户的userId 列表 |
| callMediaType | Number | 通话的媒体类型，比如：语音通话(callMediaType = 1)、视频通话(callMediaType = 2) |

### joinInGroupCall
发起群组通话，注意：使用群组通话前需要创建IM 群组，如果已经创建，请忽略；

```javascript
const TUICallKit = uni.requireNativePlugin('TUICallKit');
const roomId = 9898;
const groupId = 'myGroup';
const callMediaType = 1; // 语音通话(callMediaType = 1)、视频通话(callMediaType = 2)
TUICallKit.joinInGroupCall(roomId, groupId, callMediaType, (code, message) => {
  if (code === 0) {
    console.log('joinInGroupCall success');
  } else {
    console.log(`joinInGroupCall failed, error message = ${message}`);
  }
});
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomId | Number | 此次通话的音视频房间 Id，目前仅支持数字房间号，后续版本会支持字符串房间号 |
| groupId | String | 此次群组通话的群 Id |
| callMediaType | TUICallDefine.MediaType | 通话的媒体类型，比如视频通话、语音通话 |
| callback | Function | 设置用户昵称、头像回调。code = 0 表示设置成功；code != 0 表示设置失败，失败原因见 message |


### setCallingBell
设置自定义来电铃音，这里仅限传入本地文件地址，需要确保该文件目录是应用可以访问的。

```javascript
const TUICallKit = uni.requireNativePlugin('TUICallKit');
const filePath = './**';
TUICallKit.setCallingBell(filePath);
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| filePath | String | 来电铃音本地文件地址 |

### enableMuteMode
开启/关闭静音模式。

```javascript
const TUICallKit = uni.requireNativePlugin('TUICallKit');
const enable = true;
TUICallKit.enableMuteMode(enable);
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | Boolean | 开启、关闭静音；true 表示开启静音 |

### enableFloatWindow
开启/关闭悬浮窗功能，设置为false后，通话界面左上角的悬浮窗按钮会隐藏。

```javascript
const TUICallKit = uni.requireNativePlugin('TUICallKit');
const enable = true;
TUICallKit.enableFloatWindow(enable);
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | Boolean | 开启、关闭悬浮窗功能；true 表示开启浮窗 |
