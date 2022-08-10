## TUICallEngine API 简介

TUICallEngine API 是音视频通话组件的**无 UI 接口**。

## API 概览

| API | 描述 |
|-----|-----|
| [createInstance](#createInstance) | 创建 TUICallEngine 实例（单例模式）|
| [destroyInstance](#destroyInstance) | 销毁 TUICallEngine 实例（单例模式）|
| [on](#on) | 监听事件|
| [off](#off) | 取消监听事件|
| [login](#login) | 登录接口|
| [logout](#logout) | 登出接口|
| [setSelfInfo](#setSelfInfo) | 设置用户昵称和头像|
| [call](#call) | C2C邀请通话|
| [groupCall](#groupCall) | 群聊邀请通话|
| [accept](#accept) | 接听通话 |
| [reject](#reject) | 拒绝通话 |
| [hangup](#hangup) | 结束通话|
| [switchCallMediaType](#switchCallMediaType) | 当前通话类型切换|
| [startRemoteView](#startRemoteView) | 启动远端画面渲染|
| [stopRemoteView](#stopRemoteView) | 停止远端画面渲染|
| [startLocalView](#startLocalView) | 启动本地画面渲染|
| [stopLocalView](#stopLocalView) | 停止本地画面渲染|
| [openCamera](#opencamera) | 开启摄像头|
| [closeCamara](#closecamara) | 关闭摄像头|
| [openMicrophone](#openMicrophone) | 打开麦克风|
| [closeMicrophone](#closeMicrophone) | 关闭麦克风|
| [setVideoQuality](#setVideoQuality) | 设置视频质量|
| [getDeviceList](#getDeviceList) | 获取设备列表|
| [switchDevice](#switchDevice) | 切换摄像头或麦克风设备|

## API 详情

### createInstance
创建 TUICallEngine 的单例。

```javascript
const tuiCallEngine = TUICallEngine.createInstance({
    SDKAppID: 0, // 接入时需要将0替换为您的云通信应用的 SDKAppID
    tim: tim         // tim 参数适用于业务中已存在 TIM 实例，为保证 TIM 实例唯一性
});
```
**参数如下表所示：**

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| SDKAppID | Number | 云通信应用的 SDKAppID |
| tim | Any | TIM 实例（选填） |

### destroyInstance
销毁 TUICallEngine 的单例。

```javascript
tuiCallEngine.destroyInstance().then(() => {
    //success
}).catch(error => {
    console.warn('destroyInstance error:', error);
});
```

### on
监听事件。

```javascript
let onError = function(error) {
    console.log(error);
};
tuiCallEngine.on(TUICallEvent.ERROR, onError, this);
```
**参数如下表所示：**

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| eventName | String | 事件名 |
| callback | function | 事件响应回调 |
| context | Any | 期望 callback 执行时的上下文 |


### off
取消监听事件。
```javascript
let onError = function(error) {
    console.log(error);
};
tuiCallEngine.off(TUICallEvent.ERROR, onError, this);
```
**参数如下表所示：**

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| eventName | String | 事件名 |
| callback | function | 事件响应回调 |
| context | Any | 期望 callback 执行时的上下文 |

### login
登录接口。
```javascript
let promise = tuiCallEngine.login({userID: 'your userID', userSig: 'your userSig'});
promise.then(() => {
    //success
}).catch(error => {
    console.warn('login error:', error);
});
```

**参数如下表所示：**

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userID | String | 当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（_） |
| userSig | String | 腾讯云设计的一种安全保护签名，获取方式请参考 [如何计算UserSig](https://cloud.tencent.com/document/product/647/17275)。 |


### logout
登出接口。
```javascript
let promise = tuiCallEngine.logout();
promise.then(() => {
    //success
}).catch(error => {
    console.warn('logout error:', error);
});
```

### setSelfInfo
设置用户昵称和头像。
```javascript
let promise = tuiCallEngine.setSelfInfo({
    nickName: 'video', 
    avatar:'http(s)://url/to/image.jpg'
});
promise.then(() => {
    //success
}).catch(error => {
    console.warn('setSelfInfo error:', error);
});
```
**参数如下表所示：**

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| nickName | String | 昵称 |
| avatar | String | 头像地址 |


### call
C2C邀请通话，被邀请方会收到 TUICallEvent.INVITED 事件。

>! 离线推送仅适用于终端（Android 或 iOS)，Web 和 微信小程序不支持。


```javascript
let promise = tuiCallEngine.call({
    userID: 'user1', 
    type: 1, 
});
promise.then(() => {
    //success
}).catch(error => {
    console.warn('call error:', error);
});
```

**参数如下表所示：**

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userID | String | 被邀请方 userID |
| type | Number | 0-未知， 1-语音通话，2-视频通话 |


### groupCall
IM 群组邀请通话，被邀请方会收到 `EVENT.INVITED` 事件。
>! 离线推送仅适用于终端（Android 或 iOS)，Web 和 微信小程序不支持。

```javascript
let promise = tuiCallEngine.groupCall({
    userIDList: ['user1', 'user2'], 
    type: 1, 
    groupID: 'IM群组 ID', 
});
promise.then(() => {
    //success
}).catch(error => {
    console.warn('groupCall error:', error);
});
```
**参数如下表所示：**
<table>
    <thead>
        <tr>
            <th>参数</th>
            <th>类型</th>
            <th>含义</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>userIDList</td>
            <td>Array</td>
            <td>邀请列表</td>
        </tr>
        <tr>
            <td>type</td>
            <td>Number</td>
            <td>0-未知， 1-语音通话，2-视频通话</td>
        </tr>
        <tr>
            <td>groupID</td>
            <td>String</td>
            <td>IM 群组</td>
        </tr>
        <tr>
            <td>timeout</td>
            <td>String</td>
            <td>超时时长(选填)</td>
        </tr>
        <tr>
            <td>roomID</td>
            <td>String</td>
            <td>房间 ID(选填)</td>
        </tr>
        <tr>
            <td>offlinePushInfo</td>
            <td>Object</td>
            <td>
                <p>自定义离线消息推送（选填，需 tsignaling 版本 &gt;= 0.8.0）</p>
                <table>
                    <thead>
                        <tr>
                            <th style="text-align:left">name</th>
                            <th style="text-align:left">Type</th>
                            <th style="text-align:left">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="text-align:left">title</td>
                            <td style="text-align:left">string</td>
                            <td style="text-align:left">离线推送标题（选填）</td>
                        </tr>
                        <tr>
                            <td style="text-align:left">description</td>
                            <td style="text-align:left">string</td>
                            <td style="text-align:left">离线推送内容（选填）</td>
                        </tr>
                        <tr>
                            <td style="text-align:left">androidOPPOChannelID</td>
                            <td style="text-align:left">string</td>
                            <td style="text-align:left">离线推送设置 OPPO 手机 8.0 系统及以上的渠道 ID （选填）</td>
                        </tr>
                        <tr>
                            <td style="text-align:left">extension</td>
                            <td style="text-align:left">string</td>
                            <td style="text-align:left">离线推送透传内容（选填）（tsignaling 版本 &gt;= 0.9.0）</td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
    </tbody>
</table>

### accept

当您作为被邀请方收到 `TUICallEvent.INVITED` 事件的回调时，可以调用该接口接听来电。

```javascript
tuiCallEngine.on(TUICallEvent.INVITED, () => {
    tuiCallEngine.accept().promise.then(() => {
        //success
    }).catch(error => {
        console.warn('accept error:', error);
    });
});
```

### reject

拒绝当前通话，当您作为被叫收到 `TUICallEvent.INVITED ` 的回调时，可以调用该函数拒绝来电。
```javascript
tuiCallEngine.on(TUICallEvent.INVITED, () => {
    tuiCallEngine.reject().then(() => {
        //success
    }).catch(error => {
        console.warn('reject error:', error);
    });
});
```

### hangup
挂断当前通话，当您处于通话中，可以调用该函数结束通话。
- 当您处于通话中，可以调用该接口结束通话
- 当未拨通时, 可用来取消通话

```javascript
tuiCallEngine.hangup().then(() => {
     //success
 }).catch(error => {
        console.warn('hangup error:', error);
 });
```

### switchCallMediaType
当前通话类型切换。
- 仅支持1v1通话过程中使用
- 失败监听 ERROR 事件，code: 60001
```javascript
// 1 表示语音通话；2 表示视频通话
tuiCallEngine.switchCallMediaType(2).then(() => {
    //success
}).catch(error => {
    console.warn('switchCallMediaType error:', error);
});
```

**参数如下表所示：**

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| newMediaType | Number | 1-语音通话，2-视频通话 |


### startRemoteView
启动远端画面渲染。

```javascript
let promise = tuiCallEngine.startRemoteView({
    userID: 'user1', 
    videoViewDomID: 'video_1',
});
promise.then(() => {
    //success
}).catch(error => {
    console.warn('startRemoteView error:', error);
});
```
**参数如下表所示：**

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userID | String | 用户 ID |
| videoViewDomID | String | 该用户数据将渲染到该 dom id 节点里 |


### stopRemoteView
停止远端画面渲染

```javascript
tuiCallEngine.stopRemoteView({userID: 'user1'});
```

**参数如下表所示：**

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userID | String | 用户id |

### startLocalView
启动本地画面渲染

```javascript
let promise = tuiCallEngine.startLocalView({
    userID: 'user1', 
    videoViewDomID: 'video_1'
});
promise.then(() => {
    //success
}).catch(error => {
    console.warn('startLocalView error:', error);
});
```

**参数如下表所示：**

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userID | String | 用户 id |
| videoViewDomID | String | 该用户数据将渲染到该dom id节点里 |

### stopLocalView
停止本地画面渲染

```javascript
let promise = tuiCallEngine.stopLocalView({userID: 'user1'});
promise.then(() => {
    //success
}).catch(error => {
    console.warn('stopLocalView error:', error)
});
```
**参数如下表所示：**

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userID | String | 用户 id |

### openCamera
开启摄像头。
```javascript
tuiCallEngine.openCamera().then(() => {
    //success
}).catch(error => {
    console.warn('openCamera error:', error);
});
```
### closeCamara
关闭摄像头
```javascript
tuiCallEngine.closeCamera().then(() => {
    //success
}).catch(error => {
    console.warn('closeCamara error:', error);
});
```

### openMicrophone
打开麦克风。
```javascript
tuiCallEngine.openMicrophone().then(() => {
    //success
}).catch(error => {
    console.warn('openMicrophone error:', error);
});
```

### closeMicrophone
关闭麦克风。
```javascript
tuiCallEngine.closeMicrophone().then(() => {
    //success
}).catch(error => {
    console.warn('closeMicrophone error:', error);
});
```

### setVideoQuality
设置视频质量。
```javascript
const profile = '720p';
tuiCallEngine.setVideoQuality(profile).then(() => {
    //success
}).catch(error => {
    console.warn('setVideoQuality error:', error)
});    // 设置视频质量为720p     
```

**参数如下表所示：**


|视频 Profile	|分辨率（宽 x 高）|
|-----|-----|
|480p |640 x 480|
|720p	|1280 x 720|
|1080p	|1920 x 1080|


### getDeviceList
获取设备列表。
```javascript
tuiCallEngine.getDeviceList("camera").then((devices) => {
    console.log(devices);
}).catch(error => {
    console.warn('getDeviceList error:', error);
});
```
**参数如下表所示：**

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| deviceType | String | 'camera'-摄像头，'microphones'-麦克风 |

### switchDevice
切换摄像头或麦克风设备。
```javascript
let promsie = tuiCallEngine.switchDevice({
    deviceType: 'video', 
    deviceId: cameras[0].deviceId
});
promise.then(() => {
    //success
}).catch(error => {
    console.warn('switchDevice error:', error)
});
```

**参数如下表所示：**
<table class="params">
    <thead>
        <tr>
            <th>参数</th>
            <th>类型</th>
            <th>含义</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>deviceType</td>
            <td>String</td>
            <td>
                <p>需要切换的设备类型</p>
                <ul>
                    <li>'video' 摄像头</li>
                    <li>'audio' 麦克风</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>deviceId</td>
            <td>String</td>
            <td>
                <p>需要切换的设备ID</p>
                <ul>
                    <li>摄像头设备标识通过 getCameras() 获取。</li>
                    <li>麦克风设备标识通过 getMicrophones() 获取。</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>
