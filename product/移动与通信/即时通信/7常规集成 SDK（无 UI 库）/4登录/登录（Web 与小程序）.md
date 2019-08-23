
用户登录 IM SDK 才能正常收发消息，登录需要用户提供 UserID、UserSig 等信息，具体含义请参见 [登录鉴权](https://cloud.tencent.com/document/product/269/31999) 。

## 登录接口

**接口名**

```javascript
tim.login(options)
```

**请求参数**

| 名称      | 类型     | 描述                                                         |
| --------- | -------- | ------------------------------------------------------------ |
| UserID  | String | 用户 ID。                                                       |
| UserSig | String | 用户登录即时通信 IM 时使用的密码，其本质是 App Server 用密钥对 UserID 等信息加密后的数据。<br/>具体生成方法请参见 [生成 UserSig](https://cloud.tencent.com/document/product/269/32688)。 |

**返回值**

该接口返回 `Promise` 对象。

## 示例

```javascript
let promise = tim.login({userID: 'your userID', userSig: 'your userSig'});
promise.then(function(imResponse) {
  console.log(imResponse.data); // 登录成功
}).catch(function(imError) {
  console.warn('login error:', imError); // 登录失败的相关信息
});
```



## 多端登录场景

如果此帐号已在其他页面登录，再在当前页面登录成功，有可能会将其他页面踢下线。用户被踢下线时会触发事件`KICKED_OUT`，用户可在监听到事件后做相应处理。

**监听示例**

```javascript
let onKickedOut = funciton (event) {
  console.log(event.data.type); // mutipleAccount(同一设备，同一帐号，多页面登录被踢)
};
tim.on(TIM.EVENT.KICKED_OUT, onKickedOut);
```

如需支持多实例登录（允许在多个网页中同时登录同一帐号），请到 [即时通信 IM 控制台](https://console.cloud.tencent.com/avc)，找到相应 SDKAppID，【应用配置】 > 【功能配置】> 【Web端实例同时在线】配置实例个数。配置将在50分钟内生效。
