## TUICallKit API 简介

TUICallKit API 是音视频通话组件的**含 UI 接口**，使用TUICallKit API，您可以通过简单接口快速实现一个类微信的音视频通话场景，更详细的接入步骤，详情请参见 [快速接入 TUICallKit](https://cloud.tencent.com/document/product/647/78732?!preview)。

## API 概览

| API | 描述 |
|-----|-----|
| [login](#login)                         | 登录                     |
| [logout](#logout)                       | 登出                     |
| [setSelfInfo](#setselfinfo)             | 设置用户的昵称、头像     |
| [call](#call)                           | 发起 1v1 通话            |
| [groupCall](#groupcall)                 | 发起群组通话             |
| [joinInGroupCall](#joiningroupcall)     | 主动加入当前的群组通话中 |
| [setCallingBell](#setcallingbell)       | 设置自定义来电铃音       |
| [enableMuteMode](#enablemutemode)       | 开启/关闭静音模式        |
| [enableFloatWindow](#enablefloatwindow) | 开启/关闭悬浮窗功能      |

## API 详情

### login
登录
```javascript
const TUICallKit = uni.requireNativePlugin('TencentCloud-TUICallKit');
const options = {
  SDKAppID: 0,
  userID: 'chard',
  userSig: '',
};
TUICallKit.login(options, (res) => {
  if (res.code === 0) {
    console.log('login success');
  } else {
    console.log(`login failed, error message = ${res.msg}`);
  }
});
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| options | Object | 初始化参数 |
| options.SDKAppID | Number | 用户 SDKAppID |
| options.userID | String | 用户 ID |
| options.userSig | String | 用户签名 userSig |
| callback | Function | 回调函数，code = 0 表示调用成功；code != 0 表示调用失败，失败原因见 msg | 

### logout
登出
```javascript
const TUICallKit = uni.requireNativePlugin('TencentCloud-TUICallKit');
TUICallKit.logout((res) => {
  if (res.code === 0) {
    console.log('logout success');
  } else {
    console.log(`logout failed, error message = ${res.msg}`);
  }
});
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| callback | Function | 回调函数，code = 0 表示调用成功；code != 0 表示调用失败，失败原因见 msg | 

### setSelfInfo
设置用户昵称、头像。用户昵称不能超过500字节，用户头像必须是URL格式。

```javascript
const TUICallKit = uni.requireNativePlugin('TencentCloud-TUICallKit');
const options = {
  nickName: '',
  avatar: ''
}
TUICallKit.setSelfInfo(options, (res) => {
  if (res.code === 0) {
    console.log('setSelfInfo success');
  } else {
    console.log(`setSelfInfo failed, error message = ${res.msg}`);
  }
});
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| options | Object | 初始化参数 |
| options.nickName | String | 目标用户的昵称，非必填 |
| options.avatar | String | 目标用户的头像，非必填 | 
| callback | Function | 回调函数，code = 0 表示调用成功；code != 0 表示调用失败，失败原因见 msg |

### call
拨打电话（1v1通话）

```javascript
const TUICallKit = uni.requireNativePlugin('TencentCloud-TUICallKit');
const options = { 
  userID: 'chard',
  callMediaType: 1, // 语音通话(callMediaType = 1)、视频通话(callMediaType = 2)
};
TUICallKit.call(options, (res) => {
  if (res.code === 0) {
    console.log('call success');
  } else {
    console.log(`call failed, error message = ${res.msg}`);
  }
});
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| options | Object | 初始化参数 |
| options.userID | String | 目标用户的 userID |
| options.callMediaType | Number | 通话的媒体类型，比如：语音通话(callMediaType = 1)、视频通话(callMediaType = 2) |
| callback | Function | 回调函数，code = 0 表示调用成功；code != 0 表示调用失败，失败原因见 msg |

### groupCall
发起群组通话，注意：使用群组通话前需要创建IM 群组，如果已经创建，请忽略。

```javascript
const TUICallKit = uni.requireNativePlugin('TencentCloud-TUICallKit');
const options = {
  groupID: 'myGroup',
  userIDList: ['chard', 'linda', 'rg'],
  callMediaType: 1, // 语音通话(callMediaType = 1)、视频通话(callMediaType = 2)
};
TUICallKit.groupCall(options, (res) => {
  if (res.code === 0) {
    console.log('call success');
  } else {
    console.log(`call failed, error message = ${res.msg}`);
  }
});
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| options | Object | 初始化参数 |
| options.groupID | String | 此次群组通话的群 ID |
| options.userIDList | List | 目标用户的userId 列表 |
| options.callMediaType | Number | 通话的媒体类型，比如：语音通话(callMediaType = 1)、视频通话(callMediaType = 2) |
| callback | Function | 回调函数，code = 0 表示调用成功；code != 0 表示调用失败，失败原因见 msg |

### joinInGroupCall
发起群组通话，注意：使用群组通话前需要创建IM 群组，如果已经创建，请忽略。

```javascript
const TUICallKit = uni.requireNativePlugin('TencentCloud-TUICallKit');
const options = {
  roomID: 9898,
  groupID: 'myGroup',
  callMediaType: 1, // 语音通话(callMediaType = 1)、视频通话(callMediaType = 2)
};
TUICallKit.joinInGroupCall(options, (res) => {
  if (res.code === 0) {
    console.log('joinInGroupCall success');
  } else {
    console.log(`joinInGroupCall failed, error message = ${res.msg}`);
  }
});
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| options | Object | 初始化参数 |
| options.roomID | Number | 此次通话的音视频房间 ID，目前仅支持数字房间号，后续版本会支持字符串房间号 |
| options.groupID | String | 此次群组通话的群 ID |
| options.callMediaType | Number | 通话的媒体类型，比如：语音通话(callMediaType = 1)、视频通话(callMediaType = 2) |
| callback | Function | 回调函数，code = 0 表示调用成功；code != 0 表示调用失败，失败原因见 msg |

### setCallingBell
设置自定义来电铃音，这里仅限传入本地文件地址，需要确保该文件目录是应用可以访问的。

```javascript
const TUICallKit = uni.requireNativePlugin('TencentCloud-TUICallKit');
const filePath = './**';
TUICallKit.setCallingBell(filePath, (res) => {
  if (res.code === 0) {
    console.log('setCallingBell success');
  } else {
    console.log(`setCallingBell failed, error message = ${res.msg}`);
  }
});
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| filePath | String | 来电铃音本地文件地址 |
| callback | Function | 回调函数，code = 0 表示调用成功；code != 0 表示调用失败，失败原因见 msg |

### enableMuteMode
开启/关闭静音模式。

```javascript
const TUICallKit = uni.requireNativePlugin('TencentCloud-TUICallKit');
const enable = true;
TUICallKit.enableMuteMode(enable);
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | Boolean | 开启、关闭静音；true 表示开启静音 |

### enableFloatWindow
开启/关闭悬浮窗功能，设置为false后，通话界面左上角的悬浮窗按钮会隐藏。

```javascript
const TUICallKit = uni.requireNativePlugin('TencentCloud-TUICallKit');
const enable = true;
TUICallKit.enableFloatWindow(enable);
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | Boolean | 开启、关闭悬浮窗功能；true 表示开启浮窗 |
