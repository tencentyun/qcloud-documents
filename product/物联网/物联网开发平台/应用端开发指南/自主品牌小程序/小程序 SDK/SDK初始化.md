SDK 初始化后，才能通过 SDK 使用物联网开发平台提供的云端能力。初始化 SDK 需要依次完成以下步骤：

1. 调用 `AppDevSdk` 的构造函数并传入配置项，创建 SDK 对象。
2. 调用 SDK 对象的 `init` 函数初始化 SDK。



## SDK 对象构造函数

```typescript
AppDevSdk(sdkOptions)
```

### 配置项

| 参数名         | 参数描述                                                     | 类型                                         | 必填 |
| -------------- | ------------------------------------------------------------ | -------------------------------------------- | ---- |
| getAccessToken | 获取 accessToken 的回调，返回一个 Promise，其值为 [微信号注册登录](https://cloud.tencent.com/document/product/1081/40781) 应用端 API 的返回结果 | Promise<{ Token:string, ExpireAt?: number }> | 是   |
| appKey         | 在 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer) > **应用开发** > **小程序开发**中申请的 AppKey | string                                       | 是   |
| debug          | 是否为调试模式，默认为：false，开启调试模式后会开启打印调试日志 | boolean                                      | 否   |
| wsConfig       | WebSocket 的配置                                             | WsOptions                                    | 否   |
| plugins        | 导入到 SDK 的配网插件数组                                    | AppDevPlugin[]                               | 否   |
| apiUrl         | 物联网开发平台的接口 URL，默认为：`https://iot.cloud.tencent.com/api/exploreropen/`，一般无需更改 | string                                       | 否   |
| defaultUin     | 未登录状态下的默认 uin，以及调试模式下的固定 uin，默认为：unknown，一般无需更改 | string                                       | 否   |
| reporter       | SDK 运行日志的回调函数                                       | (eventName: string, params: any) => void     | 否   |

### getAccessToken 回调函数

SDK 初始化时，将调用 `getAccessToken` 回调函数以取得物联网开发平台的 AccessToken。开发者需要在 `getAccessToken` 函数中实现获取 AccessToken 的流程，请参见 [接入微信登录]()。

### WsOptions 数据结构

| 属性名                | 属性描述                                                     | 类型    | 必填 |
| --------------------- | ------------------------------------------------------------ | ------- | ---- |
| autoReconnect         | WebSocket 断开后是否自动连接，默认为：true，自动重连每两秒尝试一次 | boolean | 否   |
| disconnectWhenAppHide | 当 App.onHide 触发时，是否自动断开 WebSocket，默认为：true   | boolean | 否   |
| connectWhenAppShow    | 当 App.onShow 触发时，是否自动连接 WebSocket，默认为：true   | boolean | 否   |
| url                   | websocket 服务的 URL，默认为：wss://iot.cloud.tencent.com/ws/explorer | string  | 否   |
| heartbeatInterval     | 心跳包的发送间隔，单位毫秒，默认为：60000                    | number  | 否   |



## SDK 初始化

```typescript
sdk.init(options) => Promise<void>
```

调用后将依次执行：

1. 登录（调用 `getAccessToken` 回调函数，取得平台的 AccessToken）。
2. 连接 WebSocket。

`init` 函数可同时多次调用（返回同一个缓存的 Promise）。若一次执行未完成或已执行成功，多次调用后拿到的会是同一个 Promise。若执行失败，则该缓存的 Promise 在 reject 之后会被释放，再次调用则将重新执行。

### 参数说明

| 参数名 | 参数描述                                        | 类型    | 必填 |
| ------ | ----------------------------------------------- | ------- | ---- |
| reload | 是否清理缓存的 Promise 并重新执行，默认为 false | boolean | 否   |

### 示例代码

```javascript
const getAccessToken = async () => {
  // 获取小程序登录凭证（code）
  const code = await new Promise((resolve, reject) => {
    wx.login({
      success: (res) => resolve(res.code),
      fail: reject
    });
  });

  // 获取小程序用户信息
  const userInfo = await new Promise((resolve, reject) => {
    wx.getUserInfo({
      success: (res) => resolve(res.userInfo),
      fail: reject
    });
  });

  // 调用开发者自建的后台服务端获取 AccessToken
  // 请根据实际情况调整实现
  const resp = await new Promise((resolve, reject) => {
    wx.request({
      url: '开发者自建的后台服务端 URL',
      data: {
        code: code,
        userInfo: userInfo
      },
      header: {
        'content-type': 'application/json'
      },
      success(res) {
        resolve(res.data);
      },
      fail(err) {
        reject(err);
      }
    });
  });

  return {
    Token: resp.Token,
    ExpireAt: resp.ExpireAt,
  };
};

const sdk = new AppDevSdk({
  appKey: '此处填写您的 AppKey',
  getAccessToken: getAccessToken
});

// SDK 初始化
sdk.init();
```

