## 登录
用户登录 IM SDK 才能正常收发消息，登录需要用户提供 UserID、UserSig 等信息，具体含义请参见 [登录鉴权](https://cloud.tencent.com/document/product/269/31999)。登录成功后，需要先等 SDK 处于 ready 状态才能调用 [sendMessage](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/SDK.html#sendMessage) 等需要鉴权的接口，您可以通过监听事件 [TIM.EVENT.SDK_READY](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.SDK_READY) 获取 SDK 状态。

>!默认情况下，不支持多实例登录，即如果此帐号已在其他页面登录，若继续在当前页面登录成功，有可能会将其他页面踢下线。用户被踢下线时会触发事件`TIM.EVENT.KICKED_OUT`，用户可在监听到事件后做相应处理。多端登录监听示例如下：
```javascript
let onKickedOut = function (event) {
  console.log(event.data.type); // mutipleAccount(同一设备，同一帐号，多页面登录被踢)
};
tim.on(TIM.EVENT.KICKED_OUT, onKickedOut);
```
如需支持多实例登录（允许在多个网页中同时登录同一帐号），请登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)，找到相应 SDKAppID，选择【应用配置】>【功能配置】>【登录与消息】>【Web端实例同时在线】配置实例个数。配置将在50分钟内生效。

**接口名**

```javascript
tim.login(options)
```

**请求参数**

| 名称      | 类型     | 描述                                                         |
| --------- | -------- | ------------------------------------------------------------ |
| userID  | String | 用户 ID。                                                       |
| userSig | String | 用户登录即时通信 IM 的密码，其本质是对 UserID 等信息加密后得到的密文。<br/>具体生成方法请参见 [生成 UserSig](https://cloud.tencent.com/document/product/269/32688)。 |

**返回值**

该接口返回 `Promise` 对象。

**示例**

```javascript
let promise = tim.login({userID: 'your userID', userSig: 'your userSig'});
promise.then(function(imResponse) {
  console.log(imResponse.data); // 登录成功
}).catch(function(imError) {
  console.warn('login error:', imError); // 登录失败的相关信息
});
```



## 登出
该接口通常在切换帐号时调用，清除登录态以及内存中的所有数据。
>!
>- 调用此接口的实例会发布 [SDK_NOT_READY](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.SDK_NOT_READY) 事件，此时该实例下线，无法收发消息。
>- 如果您在 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) 配置的“Web端实例同时在线个数”大于 1，且同一帐号已登录`a1`和`a2`两个实例（含小程序端），执行`a1.logout()`后，`a1`会下线，无法收发消息。而`a2`实例不会受影响。<br/>
>- 多实例被踢：如果“Web端实例同时在线个数”配置为2，且您的某一帐号已登录`a1`和`a2`两个实例，当使用此帐号成功登录第三个实例`a3`时，`a1`或`a2`中的一个实例会被踢下线（通常是最先处在登录态的实例会触发）。假设`a1`实例被踢下线，`a1`实例内部会执行登出流程，然后抛出 [KICKED_OUT](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/module-EVENT.html#.KICKED_OUT) 事件，接入侧可以监听此事件，并在触发时跳转到登录页。此时`a1`实例下线，而`a2`和`a3`实例可以正常运行。

**接口名**

```js
tim.logout();
```

**请求参数**

无

**返回值**

该接口返回`Promise`对象：
- `then`的回调函数参数为 [IMResponse](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMResponse)，`IMResponse.data`为空对象。表示成功登出。

- `catch`的回调函数参数为 [IMError](https://imsdk-1252463788.file.myqcloud.com/IM_DOC/Web/global.html#IMError)。

**示例**

```js
let promise = tim.logout();
promise.then(function(imResponse) {
  console.log(imResponse.data); // 登出成功
}).catch(function(imError) {
  console.warn('logout error:', imError);
});
```
