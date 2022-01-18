## SDK 初始化

SDK 初始化后，才能通过 SDK 使用物联网开发平台提供的云端能力。初始化 SDK 需要依次完成以下步骤：

1. 调用 `AppDevSdk` 的构造函数并传入配置项，创建 SDK 对象。
2. 调用 SDK 对象的 `init` 函数初始化 SDK。

### SDK 对象构造函数

```typescript
AppDevSdk(sdkOptions)
```

#### 配置项

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

#### getAccessToken 回调函数

SDK 初始化时，将调用 `getAccessToken` 回调函数以取得物联网开发平台的 AccessToken。开发者需要在 `getAccessToken` 函数中实现获取 AccessToken 的流程，请参见 [接入微信登录]()。

#### WsOptions 数据结构

| 属性名                | 属性描述                                                     | 类型    | 必填 |
| --------------------- | ------------------------------------------------------------ | ------- | ---- |
| autoReconnect         | WebSocket 断开后是否自动连接，默认为：true，自动重连每两秒尝试一次 | boolean | 否   |
| disconnectWhenAppHide | 当 App.onHide 触发时，是否自动断开 WebSocket，默认为：true   | boolean | 否   |
| connectWhenAppShow    | 当 App.onShow 触发时，是否自动连接 WebSocket，默认为：true   | boolean | 否   |
| url                   | websocket 服务的 URL，默认为：wss://iot.cloud.tencent.com/ws/explorer | string  | 否   |
| heartbeatInterval     | 心跳包的发送间隔，单位毫秒，默认为：60000                    | number  | 否   |

### SDK 初始化

```typescript
sdk.init(options) => Promise< void >
```

调用后将依次执行：

1. 登录（调用 `getAccessToken` 回调函数，取得平台的 AccessToken）。
2. 连接 WebSocket。

`init` 函数可同时多次调用（返回同一个缓存的 Promise）。若一次执行未完成或已执行成功，多次调用后拿到的会是同一个 Promise。若执行失败，则该缓存的 Promise 在 reject 之后会被释放，再次调用则将重新执行。

#### 参数说明

| 参数名 | 参数描述                                        | 类型    | 必填 |
| ------ | ----------------------------------------------- | ------- | ---- |
| reload | 是否清理缓存的 Promise 并重新执行，默认为 false | boolean | 否   |

#### 示例代码

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

## 应用端 API

应用端 API 是物联网开发平台为了满足智能家居场景，为用户开发自有品牌的小程序或 App 而提供的云端服务，包括用户管理、设备管理、设备定时、家庭管理等基础能力。关于应用端 API 的更多信息，请参见 [应用端 API 简介](https://cloud.tencent.com/document/product/1081/40773)。

### 调用应用端 API

调用应用端 API 并获得响应数据。

```typescript
sdk.requestApi(Action: string, payload?: object, options?: object) => Promise< response >
```

#### 参数说明

| 参数名  | 参数描述                                                     | 类型   | 必填 |
| ------- | ------------------------------------------------------------ | ------ | ---- |
| Action  | 请求应用端 API 的 Action 名                                  | string | 是   |
| payload | 请求应用端 API 的数据，会自动带上公共参数 `AccessToken` 与 `RequestId` | object | 否   |
| options | 请求的选项，将透传给 [wx.request](https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html) | object | 否   |

#### 返回值

- 请求成功（code=0）：返回一个 resolved 的 Promise，其值为应用端 API 响应中的 `Response` 部分数据。
- 请求失败：返回一个 rejected 的 Promise，其值的数据结构为：`{ code, msg, ...detail }`。

#### 示例代码

```javascript
sdk.requestApi('AppGetFamilyDeviceList', { FamilyId: 'default' })
  .then(data => {
    // 请求成功
    console.log(data);
  })
  .catch(err => {
    // 请求失败
    console.error(err);
  });
```

> ! 
>- 腾讯云物联网开发平台是基于**家庭**的设备体系，每个家庭有其对应的 `FamilyId`，每台设备均归属一个家庭。
>- 开发者也可以选择不关注家庭这一概念，对所有需要传`FamilyId`的接口（例如 [获取用户绑定设备列表](https://cloud.tencent.com/document/product/1081/40803)）传入`default` 作为 `FamilyId`，SDK 会自动完成内部的家庭相关的逻辑（SDK 会为用户创建一个默认家庭，若`FamilyId`入参的值为`default`，SDK 会自动替换为用户默认家庭的`FamilyId`）。


## 设备配网

SDK 目前支持 softAP、SmartConfig、simpleConfig、AirKiss、BLE-Combo 这五种方式进行设备配网。这五种配网方式是以**插件**的方式按需引入的，这里为了方便大家理解，下图是设计思路，可以看出这5个插件的依赖关系
![](https://main.qcloudimg.com/raw/69f79c09c8b3a995cb90b8d2e0de952e.png)

通过4步可以运行插件，以`SoftAp`为例，其余的配网方式步骤一样，后面关于配网步骤和参数说明会具体阐述。

1. 安装依赖。
```bash
npm install qcloud-iotexplorer-appdev-plugin-wificonf-core
```
2. 注册插件。
```javascript
const SoftApPlug = require('qcloud-iotexplorer-appdev-plugin-wificonf-softap');
SoftApPlug.install(sdk);
```
3. 生成配网 Token，调用 [生成 Wi-Fi 设备配网 Token](https://cloud.tencent.com/document/product/1081/44044) 应用端 API 获取 Wi-Fi 设备配网 Token。
   <dx-codeblock>
   :::  JavaScript
   sdk.requestApi('AppCreateDeviceBindToken')
    .then(data => {
    const bindDeviceToken = data.Token;
    });
   :::
   </dx-codeblock>
4. 运行插件，`plugin` 注册时的名称分别为：`wifiConfSoftAp` 、`wifiConfSmartConfig` 、`wifiConfSmartConfig` 、`wifiConfAirKiss` 、`wifiConfBleCombo`。
``` JavaScript
/** 
- pluginNames: wifiConfSoftAp | wifiConfSmartConfig | wifiConfSimpleConfig | wifiConfAirKiss | wifiConfBleCombo
*/
sdk.plugins['wifiConfSoftAp'].start({
wifiConfToken: bindDeviceToken,
targetWifiInfo: wifiInfo,
familyId,
roomId,
onProgress,
onComplete,
onError,
autoRetry: true, // 自动处理故障流程
});
```

### softAP 配网

关于 softAP 方式配网的流程，请参见 [softAP 配网开发](https://cloud.tencent.com/document/product/1081/43695)。各端交互的简易的流程如下：
![SoftAPFlows](https://main.qcloudimg.com/raw/858ade66bfbcadc01c389a07cdd5fed2.png)
腾讯连连中 `softAP` 配网页面如下，供开发者开发时参考。
![](https://main.qcloudimg.com/raw/a9914f2a21fd0063cd2ac48ad639fe82.gif)

#### softAPOpts 配网参数



| 参数名         | 参数描述                                                     | 类型                                                  | 必填 |
| -------------- | ------------------------------------------------------------ | ----------------------------------------------------- | ---- |
| wifiConfToken  | Wi-Fi 设备配网 Token，从后台接口 [生成 Wi-Fi 设备配网 Token](https://cloud.tencent.com/document/product/1081/44044) 获取 | string                                                | 是   |
| targetWifiInfo | 目标 Wi-Fi 信息，需要设备去连接的 Wi-Fi 的信息               | WifiInfo                                              | 是   |
| softAPInfo     | 设备热点信息，如果传该配置，则首先会调用 wx.connectWifi 去连接设备热点；如果不传，则需要自行引导用户去连接设备热点 | WifiInfo                                              | 否   |
| familyId       | 家庭ID，默认为：'default'，即用户默认家庭 ID                 | 'default' \｜string                                   | 是   |
| roomId         | 房间ID，默认为：''，即用户默认房间 ID                        | '' \| string                                          | 否   |
| onProgress     | 配网过程执行到每个步骤时触发的回调，回调中入参为当前步骤的详情<li>code：步骤代码，详见 [配网步骤](#softAP) 小节</li><li>msg：步骤描述，自行从`WifiConfStepDesp`拿code取</li><li>detail：步骤详情，根据每个步骤不同而不同</li> | ({ code: WifiConfStepCode, detail?: object }) => void | 否   |
| onError        | 配网失败时触发<li>code：错误代码，详见 [错误码 ](#test2) 小节</li><li>msg：错误描述，自行从`WifiConfErrorMsg`拿code取</li><li>detail：错误详情</li> | ({ code: WifiConfErrorCode, detail }) => void         | 是   |
| onComplete     | 配网完成后触发                                               | () => void                                            | 是   |
| udpAddress     | 连接上设备热点后，小程序发起 UDP 通信的地址，默认为：'192.168.4.1'，一般无需更改 | string                                                | 否   |
| udpPort        | 连接上设备热点后，小程序发起 UDP 通信的端口，默认为：8266，一般无需更改 | number                                                | 否   |
| stepInterval   | 配网过程中，每一步中间等待的间隔，单位毫秒，默认为：1000，一般无需更改 | number                                                | 否   |
| autoRetry      | 配网失败之后是否要启动自动错误处理后直接重试，[自动错误处理](#autoRetry) 章节，默认为：false | boolean                                               | 否   |

#### WifiInfo 数据结构

| 属性名   | 属性描述      | 类型   | 必填 |
| -------- | ------------- | ------ | ---- |
| SSID     | Wi-Fi 的 SSID | string | 是   |
| password | Wi-Fi 的 密码 | string | 是   |

#### 示例代码

```javascript
const WifiConfConstants = require('qcloud-iotexplorer-appdev-plugin-wificonf-core').constants;

const {
   // 错误的中文描述
   WifiConfErrorMsg, 
   // 步骤code
   WifiConfStepCode, 
   // 步骤code的中文描述 
   WifiConfStepDesp
} = WifiConfConstants;

/**
 * softap配网
 */
function SoftApConfigure({
  token,
  wifiInfo = {
    SSID: '';
    password: '';
    BSSID: '';
  },
  familyId = 'default',
  roomId,
  reporter,
  onStepChange,
  onStatusChange,
}) {
  const onProgress = (data) => {
    reporter.info(data.code, data.detail);

    switch (data.code) {
      case WifiConfStepCode.CREATE_UDP_CONNECTION_SUCCESS:
        onStepChange(1);
        break;

      case WifiConfStepCode.PROTOCOL_SUCCESS:
        onStepChange(2);
        break;
      case WifiConfStepCode.SOFTAP_GET_DEVICE_SIGNATURE_SUCCESS:
      case WifiConfStepCode.BUSINESS_QUERY_TOKEN_STATE_SUCCESS:
        onStepChange(3);
        break;
      case WifiConfStepCode.WIFI_CONF_SUCCESS:
        onStepChange(4);
        break;
    }
  };

  const onComplete = ({ productId, deviceName }) => {
    onStatusChange({
      status: 'success',
      productId,
      deviceName,
    });
  };

  const onError = async ({ code, detail }) => {
    reporter.error(code, detail);

    onStatusChange({ status: 'error' });
  };

  sdk.plugins['wifiConfSoftAp'].start({
    wifiConfToken: token,
    targetWifiInfo: wifiInfo,
    autoRetry: true, // 自动处理故障流程
    familyId,
    roomId,
    onProgress,
    onComplete,
    onError
  });
}

module.exports = SoftApConfigure;
```

<span id="softAP"></span>

#### 配网步骤v1.0（已废弃，不建议使用）

| 步骤                                                  | 描述                                                         |
| ----------------------------------------------------- | ------------------------------------------------------------ |
| WifiConfStepCode.WIFI_CONF_START                      | 开始配网                                                     |
| WifiConfStepCode.PROTOCOL_START                       | 配网协议开始                                                 |
| WifiConfStepCode.CONNECT_SOFTAP_START                 | 开始连接设备热点                                             |
| WifiConfStepCode.CONNECT_SOFTAP_SUCCESS               | 连接设备热点成功                                             |
| WifiConfStepCode.CREATE_UDP_CONNECTION_START          | 开始与设备建立 UDP 连接                                      |
| WifiConfStepCode.CREATE_UDP_CONNECTION_SUCCESS        | 与设备建立 UDP 连接成功                                      |
| WifiConfStepCode.SOFTAP_SEND_TARGET_WIFIINFO_START    | 开始发送目标 Wi-Fi 信息                                      |
| WifiConfStepCode.SOFTAP_SEND_TARGET_WIFIINFO_SUCCESS  | 发送目标 Wi-Fi 信息成功<br>detail: { response }，收到设备的具体响应 |
| WifiConfStepCode.SOFTAP_GET_DEVICE_SIGNATURE_START    | 开始获取设备签名                                             |
| WifiConfStepCode.SOFTAP_GET_DEVICE_SIGNATURE_SUCCESS  | 获取设备签名成功<br>detail: { signature }                    |
| WifiConfStepCode.SOFTAP_RECONNECT_TARGET_WIFI_START   | 开始手机连接目标 Wi-Fi                                       |
| WifiConfStepCode.SOFTAP_RECONNECT_TARGET_WIFI_SUCCESS | 手机连接目标 Wi-Fi 成功                                      |
| WifiConfStepCode.PROTOCOL_SUCCESS                     | 配网协议成功                                                 |
| WifiConfStepCode.BUSINESS_START                       | 业务流程开始                                                 |
| WifiConfStepCode.BUSINESS_ADD_DEVICE_START            | 开始添加设备                                                 |
| WifiConfStepCode.BUSINESS_ADD_DEVICE_SUCCESS          | 添加设备成功                                                 |
| WifiConfStepCode.BUSINESS_SUCCESS                     | 业务流程成功<br>detail: { productId, deviceName}，请求参数   |
| WifiConfStepCode.WIFI_CONF_SUCCESS                    | 配网成功                                                     |

#### 配网步骤v2.0

| 步骤                                                  | 描述                                                         |
| ----------------------------------------------------- | ------------------------------------------------------------ |
| WifiConfStepCode.WIFI_CONF_START                      | 开始配网                                                     |
| WifiConfStepCode.PROTOCOL_START                       | 配网协议开始                                                 |
| WifiConfStepCode.CONNECT_SOFTAP_START                 | 开始连接设备热点                                             |
| WifiConfStepCode.CONNECT_SOFTAP_SUCCESS               | 连接设备热点成功                                             |
| WifiConfStepCode.CREATE_UDP_CONNECTION_START          | 开始与设备建立 UDP 连接                                      |
| WifiConfStepCode.CREATE_UDP_CONNECTION_SUCCESS        | 与设备建立 UDP 连接成功                                      |
| WifiConfStepCode.SOFTAP_SEND_TARGET_WIFIINFO_START    | 开始发送目标 Wi-Fi 信息                                      |
| WifiConfStepCode.SOFTAP_SEND_TARGET_WIFIINFO_SUCCESS  | 发送目标 Wi-Fi 信息成功<br>detail: { response }，收到设备的具体响应 |
| WifiConfStepCode.SOFTAP_RECONNECT_TARGET_WIFI_START   | 开始手机连接目标 Wi-Fi                                       |
| WifiConfStepCode.SOFTAP_RECONNECT_TARGET_WIFI_SUCCESS | 手机连接目标 Wi-Fi 成功                                      |
| WifiConfStepCode.PROTOCOL_SUCCESS                     | 配网协议成功                                                 |
| WifiConfStepCode.BUSINESS_START                       | 业务流程开始                                                 |
| WifiConfStepCode.BUSINESS_QUERY_TOKEN_STATE_START     | 开始查询配网TOKEN状态                                        |
| WifiConfStepCode.BUSINESS_QUERY_TOKEN_STATE_SUCCESS   | 查询配网TOKEN状态成功                                        |
| WifiConfStepCode.BUSINESS_ADD_DEVICE_START            | 开始添加设备                                                 |
| WifiConfStepCode.BUSINESS_ADD_DEVICE_SUCCESS          | 添加设备成功                                                 |
| WifiConfStepCode.BUSINESS_SUCCESS                     | 业务流程成功<br>detail: { productId, deviceName}，请求参数   |
| WifiConfStepCode.WIFI_CONF_SUCCESS                    | 配网成功                                                     |

### SmartConfig 配网

关于 SmartConfig 方式配网的流程，请参见 [SmartConfig 配网开发](https://cloud.tencent.com/document/product/1081/43696)。一键配网的配网流程图文版本如下：
![oneKeyConfigure](https://main.qcloudimg.com/raw/f60365f1a09b87ded109ca2e4fc1493e.png)
腾讯连连中一键配网的页面交互流程如下，也给出来作为参考。
![](https://main.qcloudimg.com/raw/7ccf24038d855864f83134c5705957e9.gif)

#### smartConfigOpts 配网参数

| 参数名         | 参数描述                                                     | 类型                                                       | 必填 |
| -------------- | ------------------------------------------------------------ | ---------------------------------------------------------- | ---- |
| wifiConfToken  | Wi-Fi 设备配网 Token，从后台接口 [生成 Wi-Fi 设备配网 Token](https://cloud.tencent.com/document/product/1081/44044) 获取 | string                                                     | 是   |
| targetWifiInfo | 目标 Wi-Fi 信息，需要设备去连接的 Wi-Fi 的信息               | WifiInfo                                                   | 是   |
| familyId       | 家庭 ID，默认为：'default'，即用户默认家庭 ID                | 'default' \| string                                        | 否   |
| roomId         | 房间ID，默认为：''，即用户默认房间 ID                        | '' \| string                                               | 否   |
| onProgress     | <li>code：步骤代码，详见 [配网步骤](#SmartConfig) 小节</li><li>msg：步骤描述，自行从`WifiConfStepDesp`拿code取</li><li>detail：步骤详情，根据每个步骤不同而不同</li> | ({ code: WifiConfStepCode, detail?: object }) => void      | 否   |
| onError        | 配网失败时触发<li>code：错误代码，详见 [错误码](#test2) 小节</li><li>msg：错误描述，自行从`WifiConfErrorMsg`拿code取</li><li>detail：错误详情</li> | ({ code: WifiConfErrorCode, msg: string, detail }) => void | 是   |
| onComplete     | 配网完成后触发                                               | () => void                                                 | 是   |
| udpPort        | 小程序和设备连上同一个局域网之后，小程序发起 UDP 通信的端口，默认为：8266，一般无需更改 | number                                                     | 否   |
| stepInterval   | 配网过程中，每一步中间等待的间隔，单位毫秒，默认为：1000，一般无需更改 | number                                                     | 否   |
| autoRetry      | 配网失败之后是否要启动自动错误处理后直接重试，[自动错误处理](#autoRetry) 章节，默认为：false | boolean                                                    | 否   |

#### WifiInfo 数据结构

| 属性名   | 属性描述       | 类型   | 必填 |
| -------- | -------------- | ------ | ---- |
| SSID     | Wi-Fi 的 SSID  | string | 是   |
| BSSID    | Wi-Fi 的 BSSID | string | 是   |
| password | Wi-Fi 的 密码  | string | 是   |

#### 示例代码

```javascript
const WifiConfConstants = require('qcloud-iotexplorer-appdev-plugin-wificonf-core').constants;

const {
   // 错误的中文描述
   WifiConfErrorMsg, 
   // 步骤code
   WifiConfStepCode, 
   // 步骤code的中文描述 
   WifiConfStepDesp
} = WifiConfConstants;

/**
 * smartconfig一键配网
 */
function SmartConfigConfigure({
  token,
  wifiInfo = {
    SSID: '';
    password: '';
    BSSID: '';
  },
  familyId = 'default',
  roomId,
  reporter,
  onStepChange,
  onStatusChange,
}) {
  const onProgress = (data) => {
    reporter.info(data.code, data.detail);

    switch (data.code) {
      case WifiConfStepCode.PROTOCOL_SUCCESS:
        onStepChange(1);
        break;
      case WifiConfStepCode.CREATE_UDP_CONNECTION_SUCCESS:
        onStepChange(2);
        break;
      case WifiConfStepCode.BUSINESS_QUERY_TOKEN_STATE_SUCCESS:
        onStepChange(3);
        break;
      case WifiConfStepCode.WIFI_CONF_SUCCESS:
        onStepChange(4);
        break;
    }
  };

  const onComplete = ({ productId, deviceName }) => {
    onStatusChange({
      status: 'success',
      productId,
      deviceName,
    });
  };

  const onError = async ({ code, detail }) => {
    reporter.error(code, detail);

    onStatusChange({ status: 'error' });
  };

  sdk.plugins['wifiConfSmartConfig'].start({
    wifiConfToken: token,
    targetWifiInfo: wifiInfo,
    autoRetry: true, // 自动处理故障流程
    familyId,
    roomId,
    onProgress,
    onComplete,
    onError
  });
}

module.exports = SmartConfigConfigure;
```

<span id="SmartConfig"></span>

#### 配网步骤

`sdk.plugins['wifiConfSmartConfig'].start()` 配网过程中，每执行完一个步骤就会触发一次 `onProgress` 回调，入参为：`{ code, detail }` 形式。

| 步骤                                                | 描述                                                         |
| --------------------------------------------------- | ------------------------------------------------------------ |
| WifiConfStepCode.WIFI_CONF_START                    | 开始配网                                                     |
| WifiConfStepCode.PROTOCOL_START                     | 配网协议开始                                                 |
| WifiConfStepCode.PROTOCOL_DETAIL                    | 配网协议的细节，详细日志                                     |
| WifiConfStepCode.PROTOCOL_SUCCESS                   | 配网协议成功，获取到设备地址<br>`detail: { data: { address } }`，收到设备局域网地址，用于给设备发送信息 |
| WifiConfStepCode.BUSINESS_START                     | 业务流程开始                                                 |
| WifiConfStepCode.BUSINESS_QUERY_TOKEN_STATE_START   | 开始查询配网TOKEN状态                                        |
| WifiConfStepCode.BUSINESS_QUERY_TOKEN_STATE_SUCCESS | 查询配网TOKEN状态成功                                        |
| WifiConfStepCode.BUSINESS_ADD_DEVICE_START          | 开始添加设备                                                 |
| WifiConfStepCode.BUSINESS_ADD_DEVICE_SUCCESS        | 添加设备成功                                                 |
| WifiConfStepCode.BUSINESS_SUCCESS                   | 业务流程成功<br>detail: { productId, deviceName}，请求参数   |
| WifiConfStepCode.WIFI_CONF_SUCCESS                  | 配网成功                                                     |

### simpleConfig 配网

关于 simpleConfig 方式配网的流程，请参见 [simpleConfig 配网开发](https://cloud.tencent.com/document/product/1081/48407)。一键配网的配网流程图文版本如下：
![oneKeyConfigure](https://main.qcloudimg.com/raw/f60365f1a09b87ded109ca2e4fc1493e.png)
腾讯连连中一键配网的页面交互流程如下，也给出来作为参考。
![](https://main.qcloudimg.com/raw/18d692f6e63dd582c72e5ba190ac763d.gif)

#### simpleConfigOpts 配网参数

| 参数名         | 参数描述                                                     | 类型                                                  | 必填 |
| -------------- | ------------------------------------------------------------ | ----------------------------------------------------- | ---- |
| wifiConfToken  | Wi-Fi 设备配网 Token，从后台接口 [生成 Wi-Fi 设备配网 Token](https://cloud.tencent.com/document/product/1081/44044) 获取 | string                                                | 是   |
| targetWifiInfo | 目标 Wi-Fi 信息，需要设备去连接的 Wi-Fi 的信息               | WifiInfo                                              | 是   |
| familyId       | 家庭 ID，默认为：'default'，即用户默认家庭 ID                | 'default' \| string                                   | 否   |
| roomId         | 房间ID，默认为：''，即用户默认房间 ID                        | '' \| string                                          | 否   |
| onProgress     | <li>code：步骤代码，详见 [配网步骤](#simpleConfig) 小节</li><li>msg：步骤描述，自行从`WifiConfStepDesp`拿code取</li><li>detail：步骤详情，根据每个步骤不同而不同</li> | ({ code: WifiConfStepCode, detail?: object }) => void | 否   |
| onError        | 配网失败时触发<li>code：错误代码，详见 [错误码](#test2) 小节</li><li>msg：错误描述，自行从`WifiConfErrorMsg`拿code取</li><li>detail：错误详情</li> | ({ code: WifiConfErrorCode, detail }) => void         | 是   |
| onComplete     | 配网完成后触发                                               | () => void                                            | 是   |
| udpPort        | 小程序和设备连上同一个局域网之后，小程序发起 UDP 通信的端口，默认为：8266，一般无需更改 | number                                                | 否   |
| stepInterval   | 配网过程中，每一步中间等待的间隔，单位毫秒，默认为：1000，一般无需更改 | number                                                | 否   |
| autoRetry      | 配网失败之后是否要启动自动错误处理后直接重试，[自动错误处理](#autoRetry)章节，默认为:false | boolean                                               | 否   |

#### WifiInfo 数据结构

| 属性名   | 属性描述      | 类型   | 必填 |
| -------- | ------------- | ------ | ---- |
| SSID     | Wi-Fi 的 SSID | string | 是   |
| password | Wi-Fi 的 密码 | string | 是   |

#### 示例代码

```javascript
const WifiConfConstants = require('qcloud-iotexplorer-appdev-plugin-wificonf-core').constants;

const {
   // 错误的中文描述
   WifiConfErrorMsg, 
   // 步骤code
   WifiConfStepCode, 
   // 步骤code的中文描述 
   WifiConfStepDesp
} = WifiConfConstants;

/**
 * simpleConfig一键配网
 */
function SimpleConfigConfigure({
  token,
  wifiInfo = {
    SSID: '';
    password: '';
  },
  familyId = 'default',
  roomId,
  reporter,
  onStepChange,
  onStatusChange,
}) {
  const onProgress = (data) => {
    reporter.info(data.code, data.detail);

    switch (data.code) {
      case WifiConfStepCode.PROTOCOL_SUCCESS:
        onStepChange(1);
        break;
      case WifiConfStepCode.CREATE_UDP_CONNECTION_SUCCESS:
        onStepChange(2);
        break;
      case WifiConfStepCode.BUSINESS_QUERY_TOKEN_STATE_SUCCESS:
        onStepChange(3);
        break;
      case WifiConfStepCode.WIFI_CONF_SUCCESS:
        onStepChange(4);
        break;
    }
  };

  const onComplete = ({ productId, deviceName }) => {
    onStatusChange({
      status: 'success',
      productId,
      deviceName,
    });
  };

  const onError = async ({ code, detail }) => {
    reporter.error(code, detail);

    onStatusChange({ status: 'error' });
  };

  sdk.plugins['wifiConfSimpleConfig'].start({
    wifiConfToken: token,
    targetWifiInfo: wifiInfo,
    autoRetry: true, // 自动处理故障流程
    familyId,
    roomId,
    onProgress,
    onComplete,
    onError
  });
}

module.exports = SimpleConfigConfigure;
```

<span id="simpleConfig"></span>

#### 配网步骤

`sdk.plugins['wifiConfSimpleConfig'].start()` 配网过程中，每执行完一个步骤就会触发一次 `onProgress` 回调，入参为：`{ code, detail }` 形式。

| 步骤                                                | 描述                                                         |
| --------------------------------------------------- | ------------------------------------------------------------ |
| WifiConfStepCode.WIFI_CONF_START                    | 开始配网                                                     |
| WifiConfStepCode.PROTOCOL_START                     | 配网协议开始                                                 |
| WifiConfStepCode.PROTOCOL_DETAIL                    | 配网协议的细节，详细日志                                     |
| WifiConfStepCode.PROTOCOL_SUCCESS                   | 配网协议成功，获取到设备地址<br>`detail: { data: { address } }`，收到设备局域网地址，用于给设备发送信息 |
| WifiConfStepCode.BUSINESS_START                     | 业务流程开始                                                 |
| WifiConfStepCode.BUSINESS_QUERY_TOKEN_STATE_START   | 开始查询配网TOKEN状态                                        |
| WifiConfStepCode.BUSINESS_QUERY_TOKEN_STATE_SUCCESS | 查询配网TOKEN状态成功                                        |
| WifiConfStepCode.BUSINESS_ADD_DEVICE_START          | 开始添加设备                                                 |
| WifiConfStepCode.BUSINESS_ADD_DEVICE_SUCCESS        | 添加设备成功                                                 |
| WifiConfStepCode.BUSINESS_SUCCESS                   | 业务流程成功<br>detail: { productId, deviceName}，请求参数   |
| WifiConfStepCode.WIFI_CONF_SUCCESS                  | 配网成功                                                     |

### AirKiss 配网

关于 AirKiss 方式配网的流程，请参见 [AirKiss 配网开发](https://cloud.tencent.com/document/product/1081/48406)。一键配网的配网流程图文版本如下：
![oneKeyConfigure](https://main.qcloudimg.com/raw/f60365f1a09b87ded109ca2e4fc1493e.png)
腾讯连连中一键配网的页面交互流程如下，也给出来作为参考。
![](https://main.qcloudimg.com/raw/741b5a69403cce3d00b09fe05bddb43d.gif)

#### airKissOpts 配网参数

| 参数名         | 参数描述                                                     | 类型                                                  | 必填 |
| -------------- | ------------------------------------------------------------ | ----------------------------------------------------- | ---- |
| wifiConfToken  | Wi-Fi 设备配网 Token，从后台接口 [生成 Wi-Fi 设备配网 Token](https://cloud.tencent.com/document/product/1081/44044) 获取 | string                                                | 是   |
| targetWifiInfo | 目标 Wi-Fi 信息，需要设备去连接的 Wi-Fi 的信息               | WifiInfo                                              | 是   |
| familyId       | 家庭 ID，默认为：'default'，即用户默认家庭 ID                | 'default' \| string                                   | 否   |
| roomId         | 房间ID，默认为：''，即用户默认房间 ID                        | '' \| string                                          | 否   |
| onProgress     | <li>code：步骤代码，详见 [配网步骤](#AirKiss) 小节</li><li>msg：步骤描述，自行从`WifiConfStepDesp`拿code取</li><li>detail：步骤详情，根据每个步骤不同而不同</li> | ({ code: WifiConfStepCode, detail?: object }) => void | 否   |
| onError        | 配网失败时触发<li>code：错误代码，详见 [错误码](#test2) 小节</li><li>msg：错误描述，自行从`WifiConfErrorMsg`拿code取</li><li>detail：错误详情</li> | ({ code: WifiConfErrorCode, detail }) => void         | 是   |
| onComplete     | 配网完成后触发                                               | () => void                                            | 是   |
| udpPort        | 小程序和设备连上同一个局域网之后，小程序发起 UDP 通信的端口，默认为：8266，一般无需更改 | number                                                | 否   |
| stepInterval   | 配网过程中，每一步中间等待的间隔，单位毫秒，默认为：1000，一般无需更改 | number                                                | 否   |
| autoRetry      | 配网失败之后是否要启动自动错误处理后直接重试，[自动错误处理](#autoRetry)章节，默认为:false | boolean                                               | 否   |

#### WifiInfo 数据结构

| 属性名   | 属性描述      | 类型   | 必填 |
| -------- | ------------- | ------ | ---- |
| SSID     | Wi-Fi 的 SSID | string | 是   |
| password | Wi-Fi 的 密码 | string | 是   |

#### 示例代码

```javascript
const WifiConfConstants = require('qcloud-iotexplorer-appdev-plugin-wificonf-core').constants;

const {
   // 错误的中文描述
   WifiConfErrorMsg, 
   // 步骤code
   WifiConfStepCode, 
   // 步骤code的中文描述 
   WifiConfStepDesp
} = WifiConfConstants;

/**
 * AirKiss一键配网
 */
function AirKissConfigure({
  token,
  wifiInfo = {
    SSID: '';
    password: '';
  },
  familyId = 'default',
  roomId,
  reporter,
  onStepChange,
  onStatusChange,
}) {
  const onProgress = (data) => {
    reporter.info(data.code, data.detail);

    switch (data.code) {
      case WifiConfStepCode.PROTOCOL_SUCCESS:
        onStepChange(1);
        break;
      case WifiConfStepCode.CREATE_UDP_CONNECTION_SUCCESS:
        onStepChange(2);
        break;
      case WifiConfStepCode.BUSINESS_QUERY_TOKEN_STATE_SUCCESS:
        onStepChange(3);
        break;
      case WifiConfStepCode.WIFI_CONF_SUCCESS:
        onStepChange(4);
        break;
    }
  };

  const onComplete = ({ productId, deviceName }) => {
    onStatusChange({
      status: 'success',
      productId,
      deviceName,
    });
  };

  const onError = async ({ code, detail }) => {
    reporter.error(code, detail);

    onStatusChange({ status: 'error' });
  };

  sdk.plugins['wifiConfAirKiss'].start({
    wifiConfToken: token,
    targetWifiInfo: wifiInfo,
    autoRetry: true, // 自动处理故障流程
    familyId,
    roomId,
    onProgress,
    onComplete,
    onError
  });
}

module.exports = AirKissConfigure;
```

<span id="AirKiss"></span>

#### 配网步骤

`sdk.plugins['wifiConfAirKiss'].start()` 配网过程中，每执行完一个步骤就会触发一次 `onProgress` 回调，入参为：`{ code, detail }` 形式。

| 步骤                                                | 描述                                                         |
| --------------------------------------------------- | ------------------------------------------------------------ |
| WifiConfStepCode.WIFI_CONF_START                    | 开始配网                                                     |
| WifiConfStepCode.PROTOCOL_START                     | 配网协议开始                                                 |
| WifiConfStepCode.PROTOCOL_DETAIL                    | 配网协议的细节，详细日志                                     |
| WifiConfStepCode.PROTOCOL_SUCCESS                   | 配网协议成功，获取到设备地址<br>`detail: { data: { address } }`，收到设备局域网地址，用于给设备发送信息 |
| WifiConfStepCode.BUSINESS_START                     | 业务流程开始                                                 |
| WifiConfStepCode.BUSINESS_QUERY_TOKEN_STATE_START   | 开始查询配网TOKEN状态                                        |
| WifiConfStepCode.BUSINESS_QUERY_TOKEN_STATE_SUCCESS | 查询配网TOKEN状态成功                                        |
| WifiConfStepCode.BUSINESS_ADD_DEVICE_START          | 开始添加设备                                                 |
| WifiConfStepCode.BUSINESS_ADD_DEVICE_SUCCESS        | 添加设备成功                                                 |
| WifiConfStepCode.BUSINESS_SUCCESS                   | 业务流程成功<br>detail: { productId, deviceName}，请求参数   |
| WifiConfStepCode.WIFI_CONF_SUCCESS                  | 配网成功                                                     |

<span id="test2"></span>

### 错误码

| 错误码                            | 描述                                                         |
| --------------------------------- | ------------------------------------------------------------ |
| UDP_NOT_RESPONSED                 | 超时未收到设备响应                                           |
| UDP_CLOSED                        | 设备连接中断                                                 |
| UDP_ERROR                         | 配网过程中触发 udp.onError 事件<br>`detail: { errMsg }`，错误信息 |
| UDP_SEND_MSG_FAIL                 | 与设备 UDP 通信时，发送消息失败                              |
| CONNECT_SOFTAP_FAIL               | 手机连接设备热点失败<br>`detail: { errMsg }`，错误信息       |
| BUSINESS_WIFI_RECONNECT_FAIL      | 手机连接 Wi-Fi 路由器失败<br>`detail: { errMsg }`，错误信息  |
| BUSINESS_DEVICE_ERROR             | 收到设备响应的错误<br>`detail: { errMsg }`，错误信息         |
| BUSINESS_INVALID_RESPONSE         | 收到非法的设备响应<br>`detail: { response }`，具体的设备端响应 |
| BUSINESS_DEVICE_CONNECT_MQTT_FAIL | 设备连接 MQTT 服务失败                                       |
| BUSINESS_DEVICE_CONNECT_WIFI_FAIL | 设备连接目标 Wi-Fi 失败                                      |
| BUSINESS_QUERY_BIND_TOKEN_TIMEOUT | 设备连接云端超时                                             |
| WIFI_CONF_FAIL                    | 配网流程失败<br>`detail: { errMsg }`，错误信息               |
| PROTOCOL_FAIL                     | 配网协议失败<br>`detail: { errMsg }`，错误信息               |
| PROTOCOL_TIMEOUT                  | 配网协议超时                                                 |
| PROTOCOL_INVALID_RESPONSE         | 配网协议收到非法响应<br>`detail: { errMsg }`，错误信息       |

<span id="autoRetry"></span>

### 自动处理故障

配网流程中会出现一些错误，具体在 [错误码](#test2) 章节有展开叙述，在成功率不断优化的实践当中，总结一些可以自动处理的错误类型，处理成功后自动重试，全程用户无感知。

| 错误码            | 错误处理方式                                                 |
| ----------------- | ------------------------------------------------------------ |
| PROTOCOL_TIMEOUT  | 超时未收到设备响应，其原因可能是中途网络被切走，导致设备和手机无法通信造成超时；自动处理方式：检查当前网络是不是目标网络，否则切到目标网络，重新配网。 |
| UDP_ERROR         | UDP 通道发生错误，可能的原因其一如上（中途网络被切走，导致设备和手机无法通信造成超时），其二是 Wi-Fi 切换之后，底层 UDP 还未切换，会发包失败；自动处理方式：延迟2s之后重新配网 |
| UDP_SEND_MSG_FAIL | 同上两种处理方式                                             |

### 蓝牙辅助配网

关于 蓝牙辅助方式配网的流程，请参见 [蓝牙辅助配网开发](https://cloud.tencent.com/document/product/1081/48408)。一键配网的配网流程图文版本如下：
![](https://main.qcloudimg.com/raw/e659d1247c28849198cacac0d2abd373.png)
腾讯连连中一键配网的页面交互流程如下，也给出来作为参考。
![](https://main.qcloudimg.com/raw/25e31b76813e9bb37af397ec16bfb067.gif)

<span id="deviceAdapter"></span>

### DeviceAdapter

如上所述，在配网之前，我们需要先发现设备，然后与设备建立蓝牙连接，并获得一个 DeviceAdapter 实例，来实现和蓝牙设备的通信。这个过程可以通过 BlueToothAdapter 完成。整个流程如下：

#### 1. 创建一个 bluetoothAdapter

bluetoothAdapter 可以用来搜索设备，连接到设备。代码如下：

```ts
import { BleComboEspDeviceAdapter, BleComboLLSyncDeviceAdapter } from 'qcloud-iotexplorer-appdev-plugin-wificonf-blecombo';
import { BlueToothAdapter } from 'qcloud-iotexplorer-bluetooth-adapter';
export const bluetoothAdapter = new BlueToothAdapter({
  deviceAdapters: [
    BleComboEspDeviceAdapter,
    BleComboLLSyncDeviceAdapter,
  ],
});
```

在实例化 blueToothAdapter时，我们需要传入想要支持设备的 DeviceAdapter。目前插件内置了两种`DeviceAdapter`:

- BleComboEspDeviceAdapter: 支持通过[BluFi协议](https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/api-guides/blufi.html)进行蓝牙辅助配网
- BleComboLLSyncDeviceAdapter: 支持通过[LLSync协议](https://github.com/tencentyun/qcloud-iot-explorer-BLE-sdk-embedded/blob/master/docs/LLSync%E8%93%9D%E7%89%99%E8%AE%BE%E5%A4%87%E6%8E%A5%E5%85%A5%E5%8D%8F%E8%AE%AE.pdf)进行蓝牙辅助配网

#### 2. 获取蓝牙设备列表

通过 `bluetoothAdapter.startSearch` 方法，我们可以发现设备，获得设备列表。

```ts
  await bluetoothAdapter.startSearch({
    ignoreDeviceIds,
    serviceIds,
    ignoreServiceIds,
    onError: (error) => {
      console.log('----error', error);
      // 搜索设备出错
      bluetoothAdapter.stopSearch();
    },
    onSearch: (devices) => {
      console.log('searched devices', devices);
      if (devices.length > 0) {
        console.log('找到设备', devices); // 此时可以在页面上展示
      }
    },
    timeout: 1.4 * 15 * 1000,
  });
```

在上面的 onSearch 回调函数中，我们可以获得搜寻到的设备列表，这时可以将设备列表展示到页面上，供用户选择要连接哪个设备。此后可以调用`bluetoothAdapter.stopSearch()`来结束搜索。

#### 3. 连接设备

用户从上面获取到的设备中选择一个，并发起连接操作时，可以调用 `bluetoothAdapter.connectDevice` 方法进行连接。连接成功后会返回一个 deviceAdapter，可以用来向连接的设备发送Wi-Fi，token等数据。

```ts
try {
  // device参数是上一步获取的devices中的某一个item
  const deviceAdapter = await bluetoothAdapter.connectDevice(device);

  if (!deviceAdapter) {
    throw {
      code: 'CONNECT_ERROR',
    };
  }
} catch (err) {
  console.error('连接到设备出错');
}
```

在上面三步完成之后，我们已经通过蓝牙连接到了设备，并获得了可以更设备通信的 deviceAdapter，接下来就可以正式进行配网了。

#### bleComboOpts 配网参数

| 参数名         | 参数描述                                                     | 类型                                                  | 必填 |
| -------------- | ------------------------------------------------------------ | ----------------------------------------------------- | ---- |
| wifiConfToken  | Wi-Fi 设备配网 Token，从后台接口 [生成 Wi-Fi 设备配网 Token](https://cloud.tencent.com/document/product/1081/44044) 获取 | string                                                | 是   |
| targetWifiInfo | 目标 Wi-Fi 信息，需要设备去连接的 Wi-Fi 的信息               | WifiInfo                                              | 是   |
| familyId       | 家庭 ID，默认为：'default'，即用户默认家庭 ID                | 'default' \| string                                   | 否   |
| roomId         | 房间ID，默认为：''，即用户默认房间 ID                        | '' \| string                                          | 否   |
| onProgress     | <li>code：步骤代码，详见 [配网步骤](#BleCombo) 小节</li><li>msg：步骤描述，自行从`WifiConfStepDesp`拿code取</li><li>detail：步骤详情，根据每个步骤不同而不同</li> | ({ code: WifiConfStepCode, detail?: object }) => void | 否   |
| onError        | 配网失败时触发<li>code：错误代码，详见 [错误码](#blecombo_error_code) 小节</li><li>msg：错误描述，自行从`WifiConfErrorMsg`拿code取</li><li>detail：错误详情</li> | ({ code: WifiConfErrorCode, detail }) => void         | 是   |
| onComplete     | 配网完成后触发                                               | () => void                                            | 是   |
| deviceAdapter  | 用于和设备进行蓝牙通信的设备适配器实例，连接蓝牙之后获得，详见[DeviceAdapter](#deviceAdapter) | DeviceAdapter                                         | 是   |
| bleComboProto  | 使用的蓝牙配网协议，目前支持ESP官方和LLsync两种协议          | 'BLE_COMBO_ESP' / 'BLE_COMBO_LLSYNC'                  | 否   |

#### WifiInfo 数据结构

| 属性名   | 属性描述      | 类型   | 必填 |
| -------- | ------------- | ------ | ---- |
| SSID     | Wi-Fi 的 SSID | string | 是   |
| password | Wi-Fi 的 密码 | string | 是   |

#### 示例代码

```javascript
  // 这里可以进行一些UI进度更新操作
  const onStepChange = (progress) => {
    console.log(progress);
  }

  // 这里是配网进行过程中的回调函数
  const onProgress = (data) => {
    console.info(data.code, data.detail);
    switch (data.code) {
      case WifiConfStepCode.PROTOCOL_START: // 开始配网
        onStepChange(1);
        break;
      case WifiConfStepCode.PROTOCOL_SUCCESS: // 设备联网成功，设备可以访问互联网
        onStepChange(2);
        break;
      case WifiConfStepCode.BUSINESS_QUERY_TOKEN_STATE_SUCCESS: // 发送token到设备成功，设备开始连接云端
        onStepChange(3);
        break;
      case WifiConfStepCode.WIFI_CONF_SUCCESS: // 配网成功
        onStepChange(4);
        break;
    }
  };

  const onComplete = ({ productId, deviceName }) => {
    // 配网成功后，可以拿到设备的 productId 和 设备名称
    console.log('配网成功', productId, deviceName);
  };

  const onError = async ({ code, detail }) => {
    console.error('配网出错', code, detail);
  };

  const config = {
    wifiConfToken, // 用于设备连接云端的token
    targetWifiInfo: { // 用于设备联网的wifi信息，由用户填入
      SSID: '您的Wi-Fi名称';
      password: '您的Wi-Fi密码';
      BSSID: '';
    },
    deviceAdapter, // 由连接设备之后获得
    wifiConfType: 'ble', // 'ble' | 'llsyncble'
    familyId: 'default',
    roomId,

    onProgress, // 用来更新页面的进度条
    onError,
    OnComplete,
  }

  // 开始执行配网逻辑 go!
  sdk.plugins['wifiConfBleCombo'].start(config);
```

<span id="BleCombo"></span>

#### 配网状态码

`sdk.plugins['wifiConfBleCombo'].start(bleComboOpts)` 配网过程中，每执行完一个步骤就会触发一次 `onProgress` 回调，入参为：`{ code, detail }` 形式。

| 步骤                                    | 描述                                  |
| --------------------------------------- | ------------------------------------- |
| WifiConfStepCode.PROTOCOL_START         | 开始配网                              |
| WifiConfStepCode.PROTOCOL_SUCCESS       | 设备联网成功，设备可以访问互联网      |
| WifiConfStepCode.BLE_SEND_TOKEN_START   | 开始发送token到设备，用于连接云端     |
| WifiConfStepCode.BLE_SEND_TOKEN_SUCCESS | 发送token到设备成功，设备开始连接云端 |
| WifiConfStepCode.WIFI_CONF_SUCCESS      | 配网成功                              |

<span id="blecombo_error_code"></span>

#### 蓝牙辅助配网错误码

在 `onError`回调函数中，我们可以拿到配网失败的错误码。

| CODE                 | 描述                |
| -------------------- | ------------------- |
| PROTOCOL_FAIL        | 设备连接失败        |
| BLE_SEND_TOKEN_ERROR | 发送token到设备失败 |
| WIFI_CONF_FAIL       | 配网失败            |

<span id="moduleLog"></span>

### 模组日志收集

当发生错误的时候，只看`onProgress` 或者 `onError`里面打印出来的信息并不能准确定位到问题，需要结合设备端日志查看，我们制定了跟设备端的日志交互协议，原理如下：
![](https://main.qcloudimg.com/raw/8d3701cd1d3cf40de5169f4ed3e76558.png)

#### 示例代码

```javascript
const { collectModuleLog } =  require('qcloud-iotexplorer-appdev-plugin-wificonf-core').utils;

collectModuleLog({
   // 用于上报的对象
   reporter: console,
   sdk: sdk,
})
```

#### 日志上报打印详情

日志收集的过程以及结果会通过`reporter.info(code, detail)`的回调打印出来，可以通过这个方法来收集信息以及日志的上报。

| 步骤                                                  | 描述                                            |
| ----------------------------------------------------- | ----------------------------------------------- |
| WifiConfStepCode.MODULE_REPORT_START                  | 开始配网日志收集                                |
| WifiConfStepCode.MODULE_REPORT_CONNECT_WIFI_START     | 日志收集开始连接设备热点                        |
| WifiConfStepCode.MODULE_REPORT_CONNECT_WIFI_SUCCESS   | 日志收集连接设备热点成功                        |
| WifiConfStepCode.MODULE_REPORT_COMMUNICATE_AP_START   | 开始收集设备端日志                              |
| WifiConfStepCode.MODULE_REPORT_COMMUNICATE_AP_SUCCESS | 收集成功<br>`detail: { moudleDetail}`，日志详情 |

#### 错误码

| 错误码                             | 描述             |
| ---------------------------------- | ---------------- |
| MODULE_REPORT_COMMUNICATE_AP_ERROR | 和设备端通信失败 |
| MODULE_REPORT_TIMEOUT              | 收集日志超时     |



## 长连接通信

### 订阅设备信息

通过 WebSocket 监听服务端实时推送的设备上下线状态及属性数据。

```typescript
sdk.subscribeDevices(deviceList: string[] | deviceInfo[]): Promise< void >

```

#### 参数

| 参数名     | 参数描述                                                     | 类型                     | 必填 |
| ---------- | ------------------------------------------------------------ | ------------------------ | ---- |
| deviceList | 设备 ID 列表，或设备信息列表（deviceInfo 需包含 DeviceId 字段） | string[] \| deviceInfo[] | 是   |

#### 示例代码

##### 通过设备 ID 列表订阅

```javascript
sdk.subscribeDevices([
  'Product1/Device1',
  'Product1/Device2',
  'Product2/Device3'
]);

```

##### 通过设备列表订阅

```javascript
sdk.requestApi('AppGetFamilyDeviceList', { FamilyId: 'default' })
  .then(data => {
    sdk.subscribeDevices(data.DeviceList);
  })

```

### 手动建立长连接

手动连接 WebSocket。一般不需要调用，除非关闭了`sdkOptions.disconnectWhenAppHide`选项。

```typescript
sdk.connectWebsocket() => Promise< void >

```

#### 示例代码

```javascript
sdk.connectWebsocket();

```

### 手动断开长连接

手动断开 WebSocket。一般不需要调用，除非关闭了`sdkOptions.autoReconnect`与`sdkOptions.connectWhenAppShow`选项。

```typescript
sdk.disconnectWebsocket() => Promise< void >

```

#### 示例代码

```javascript
sdk.disconnectWebsocket();

```

### 监听事件

监听 WebSocket 事件。

```typescript
sdk.on(type: EventTypes, listener: (...args) => void) => void

```

#### 参数

| 参数名   | 参数描述             | 类型            | 必填 |
| -------- | -------------------- | --------------- | ---- |
| type     | 要监听的事件         | EventTypes      | 是   |
| listener | 事件触发时的回调函数 | (param) => void | 是   |

#### 示例代码

```javascript
const { EventTypes } = require('qcloud-iotexplorer-appdev-sdk').AppDevSdk.constants;

// 监听设备上报数据推送
sdk.on(EventTypes.WsReport, ({ deviceId, deviceData }) => {
  console.log('websocket device report', deviceId, deviceData);
});

```

### 取消监听事件

取消监听 WebSocket 事件。

```typescript
sdk.off(type: EventTypes, listener: (...args) => void) => void

```

#### 参数

| 参数名   | 参数描述                                                   | 类型                    | 必填 |
| -------- | ---------------------------------------------------------- | ----------------------- | ---- |
| type     | 要取消监听的事件                                           | EventTypes              | 是   |
| listener | 要取消监听的事件的回调函数，不传则清除该事件的所有回调函数 | (param) => void \| null | 否   |

#### 示例代码

```javascript
const { EventTypes } = require('qcloud-iotexplorer-appdev-sdk').AppDevSdk.constants;

const listener = ({ deviceId, deviceData }) => {
  console.log('websocket device report', deviceId, deviceData);
};

// 监听设备上报数据推送
sdk.on(EventTypes.WsReport, listener);

// 取消监听设备上报数据推送
sdk.off(EventTypes.WsReport, listener);

```

### 事件列表

| 事件类型                  | 描述                   | 参数                               |
| ------------------------- | ---------------------- | ---------------------------------- |
| EventTypes.WsReport       | 设备上报数据           | { deviceId, deviceData }           |
| EventTypes.WsControl      | 设备控制数据           | { deviceId, deviceData }           |
| EventTypes.WsStatusChange | 设备在线状态变更       | { deviceId, deviceStatus }         |
| EventTypes.WsEventReport  | 设备事件上报           | { Payload }                        |
| EventTypes.WsActionReport | 设备行为上报           | { Payload }                        |
| EventTypes.WsActionPush   | 设备行为下发           | { Payload }                        |
| EventTypes.WsPush         | WebSocket 推送原始数据 | { push, action, params }           |
| EventTypes.WsError        | WebSocket 发生错误     | WebSocket error 事件的原始错误信息 |
| EventTypes.WsClose        | WebSocket 连接关闭     | { code, reason }                   |

## 错误处理

SDK 所有接口的错误都经过标准化处理为 `{ code, msg, ...detail }` 的形式。具体取值根据接口的不同而不同。

### 全局错误码

> ! 下文中描述为一个对象的 detail ，实际上是解构到错误对象当中的。例如 `INTERNAL_ERROR` 的具体 Error 为 `{ code: 'INTERNAL_ERROR', msg: Error.message, stack: Error.stack, error: Error }`。

| 错误码                           | 描述                                                         |
| -------------------------------- | ------------------------------------------------------------ |
| ErrorCode.VERIFY_LOGIN_FAIL      | 未登录或登录态已失效                                         |
| ErrorCode.INTERNAL_ERROR         | JS Error 和 detail: { stack, error }分别为错误堆栈和原始错误对象 |
| ErrorCode.GET_USERINFO_NEED_AUTH | 调用 [wx.getUserInfo](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/user-info/wx.getUserInfo.html) 时用户未授权用户信息权限，遇到该错误时需要引导用户授权<br>detail: { errMsg }，小程序 API 的原始错误信息 |
| ErrorCode.WX_API_FAIL            | 调用小程序 API 报错<br>detail: { errMsg }，小程序 API 的原始错误信息 |

### 调用应用端 API 错误码

除以上全局错误码，其余错误码为应用端 API 响应中的错误码，具体错误码请查看对应的应用端 API 文档。同时接口的错误中会包含标识该次请求的 `detail.reqId`，可用来查询该次请求的详细日志。

## 迁移指南

### 从 v0.x 版本迁移到 v1.x 版本

#### 更新项目依赖

更新小程序 SDK 到 v1.x 版本，需要更新项目依赖，请在项目目录下的命令行中执行以下命令：

```bash
npm install qcloud-iotexplorer-appdev-sdk@1
```

> ? 如果您使用了微信开发者工具的 npm 支持，在更新项目依赖后，需要选择微信开发者工具菜单栏的**工具** > **构建 npm**以重新构建 npm 依赖。

#### 调整导入 SDK 的方式

导入 v0.x 版本小程序 SDK 的方式为：

```javascript
// 导入 SDK
const {
  QcloudIotExplorerAppDevSdk
} = require('qcloud-iotexplorer-appdev-sdk/qcloud-iotexplorer-appdev-sdk');

// 导入常量
const {
  EventTypes,
} = require('qcloud-iotexplorer-appdev-sdk/qcloud-iotexplorer-appdev-sdk');

const sdk = new QcloudIotExplorerAppDevSdk({
  // 参数略
});
```

小程序 SDK 升级到 v1.x 版本后，导入的方式需要调整为：

```javascript
// 导入 SDK
const { AppDevSdk } = require('qcloud-iotexplorer-appdev-sdk');

// 导入常量
const { EventTypes } = AppDevSdk.constants;

const sdk = new AppDevSdk({
  // 参数略
});
```

#### 调整配网代码

v0.x 版本小程序 SDK 内置支持 Softap 配网及 SmartConfig 配网。v1.x 版本小程序 SDK 增加了更多配网方式的支持，并将配网模块独立出来，开发者可以按需导入。关于小程序 SDK 具体支持的配网方式，请参见 [设备配网](#.E8.AE.BE.E5.A4.87.E9.85.8D.E7.BD.91)。

选择需要安装的配网插件，并在命令行中执行相应的安装命令。下面以安装 AirKiss 配网插件为例。

```bash
npm install qcloud-iotexplorer-appdev-plugin-wificonf-airkiss
```

向 SDK 注册配网插件，请参照以下代码（以 AirKiss 配网插件为例）。

```javascript
import AirKissPlug from 'qcloud-iotexplorer-appdev-plugin-wificonf-airkiss';

AirKissPlug.install(sdk);
```

调用配网插件进行配网，请参照以下代码（以 AirKiss 配网插件为例）。

```javascript
import { constants as WifiConfConstants } from 'qcloud-iotexplorer-appdev-plugin-wificonf-core';

const {
   WifiConfErrorMsg, WifiConfStepCode,
} = WifiConfConstants;

/**
 * airkiss一键配网
 */
export function AirKissConfigure({
  token,
  wifiInfo = {
    SSID: '';
    password: '';
    BSSID: '';
  },
  familyId = 'default',
  roomId,
  reporter,
  onStepChange,
  onStatusChange,
}) {
  const onProgress = (data) => {
    reporter.info(data.code, data.detail);

    switch (data.code) {
      case WifiConfStepCode.PROTOCOL_SUCCESS:
        onStepChange(1);
        break;
      case WifiConfStepCode.CREATE_UDP_CONNECTION_SUCCESS:
        onStepChange(2);
        break;
      case WifiConfStepCode.BUSINESS_QUERY_TOKEN_STATE_SUCCESS:
        onStepChange(3);
        break;
      case WifiConfStepCode.WIFI_CONF_SUCCESS:
        onStepChange(4);
        break;
    }
  };

  const onComplete = ({ productId, deviceName }) => {
    onStatusChange({
      status: 'success',
      productId,
      deviceName,
    });
  };

  const onError = async ({ code, detail }) => {
    reporter.error(code, detail);

    onStatusChange({ status: 'error' });
  };

  sdk.plugins['wifiConfAirKiss'].start({
    wifiConfToken: token,
    targetWifiInfo: wifiInfo,
    autoRetry: true, // 自动处理故障流程
    familyId,
    roomId,
    onProgress,
    onComplete,
    onError
  });
}
```

## 添加 LLSync 蓝牙设备

通过 [qcloud-iotexplorer-bluetooth-adapter-llsync](https://www.npmjs.com/package/qcloud-iotexplorer-bluetooth-adapter-llsync) sdk， 小程序可以完成和标准蓝牙设备进行连接，绑定，控制等流程。通过下面的图片可以直观地了解整个流程:

<img src=https://iot-public-1256872341.cos.ap-guangzhou.myqcloud.com/shuaisguo/1629101191691.gif style="width: 300px">

您也可以通过官方的 [小程序 SDK demo](https://github.com/tencentyun/qcloud-iotexplorer-appdev-miniprogram-sdk-demo) 的添加标准蓝牙设备部分来掌握连接标准蓝牙设备的流程。

### 1. 创建一个 bluetoothAdapter

bluetoothAdapter 可以用来搜索设备，连接到设备。代码如下：

```ts
import { BlueToothAdapter } from 'qcloud-iotexplorer-bluetooth-adapter';
import { LLSyncDeviceAdapter } from 'qcloud-iotexplorer-bluetooth-adapter-llsync';

// 关于appDevSdk文档，详见https://www.npmjs.com/package/qcloud-iotexplorer-appdev-sdk
const options = {
  appDevSdk, // 通过qcloud-iotexplorer-appdev-sdk得到的实例
}
LLSyncDeviceAdapter.injectOptions(options);
export const bluetoothAdapter = new BlueToothAdapter({
  deviceAdapters: [
    LLSyncDeviceAdapter,
  ],
});
```

### 2. 获取蓝牙设备列表

通过 bluetoothAdapter.startSearch 方法，我们可以发现设备，获得设备列表。

```ts
  const serviceIds = [LLSyncDeviceAdapter.serviceId];
  await bluetoothAdapter.startSearch({
    serviceIds,
    onError: (error) => {
      console.log('----error', error);
      // 搜索设备出错
      bluetoothAdapter.stopSearch();
    },
    onSearch: (devices) => {
      console.log('searched devices', devices);
      if (devices.length > 0) {
        console.log('找到设备', devices); // 此时可以在页面上展示
      }
    },
    timeout: 1.4 * 15 * 1000,
  });
```

在上面的 onSearch 回调函数中，我们可以获得搜寻到的设备列表，这时可以将设备列表展示到页面上，供用户选择要连接哪个设备。

**tip:** 如果设备无法搜索到，请确认设备没有被绑定。

### 3. 连接设备

用户从上面获取到的设备中选择一个，并发起连接操作时，可以调用 `bluetoothAdapter.connectDevice` 方法进行连接。连接成功后会返回一个 deviceAdapter，可以用来向连接的设备发送Wi-Fi，token等数据。

**tip**: 如果在连接时提示没有权限操作该产品，请到控制台/应用开发对应用和产品进行关联

```ts
try {
  // device 参数是上一步 onSearch 回调中获取 devices 数组的某一项
  const deviceAdapter = await bluetoothAdapter.connectDevice(device);

  if (!deviceAdapter) {
    throw {
      code: 'CONNECT_ERROR',
    }
  }
} catch (err) {
  console.error('连接到设备出错');
}

```

在这一步中，可以通过连接设备获得 deviceAdapter实例 ，通过 deviceAdapter，我们可以完成后续设备的绑定和解绑操作。

### 4. 绑定设备

绑定设备时，可以传入familyId, roomId, 从而将设备绑定到特定的家庭和房间，绑定完成后，可以在设备列表中看到该设备。

```ts
try {
  const deviceId = await deviceAdapter.bindDevice({ familyId, roomId });
} catch (err) {
  console.log(err);
}

```

### 5. 解绑设备

设备绑定后，也可以通过小程序发起删除设备的操作，这时需要调用解绑api，解绑完成后设备会恢复未绑定的状态。

```ts
try{
  await deviceAdapter.unbindDevice({ familyId, deviceId });
} catch (err) {
  console.log(err);
}

```

### 6. 断开设备

我们可以通过 `deviceAdapter.disconnectDevice()` 断开设备连接：

```
await deviceAdapter.disconnectDevice()
```

### 7. deviceAdapter 事件

|事件|描述|参数|
|---|---|---|
connect |  蓝牙设备连接时触发 |DeviceInfo
disconnect|蓝牙设备连接断开时触发|DeviceInfo|
authorized|蓝牙设备授权完成时触发|{ version, mtu, otaVersion, }|

## 音乐服务

### 公共说明

#### 获取实例

```typescript
npm install qcloud-iotexplorer-tme-sdk

import { TMESdkForMiniProgram } from 'qcloud-iotexplorer-tme-sdk';
// 注：appDevSdk为初始化后的实例
const tmeSdk = new TMESdkForMiniProgram(appDevSdk);
```



#### 接口通用返回

**接口统一返回值**

接口调用的返回值统一为 `Promise<TMEResponse>` 类型

```typescript
interface TMEResponse {
  error_code: number,
  error_msg: string,
  data?: any;
}
```

- 调用成功：返回一个 resolved 的 Promise，其值为 TMEResponse 类型，error_code=0，data 为返回结果。
- 调用失败：返回一个 rejected 的 Promise，包含错误码（error_code）及提示信息（error_msg）

| 属性名     | 描述     | 类型   |
| ---------- | -------- | ------ |
| error_code | 错误码   | number |
| error_msg  | 错误信息 | string |
| data       | 响应数据 | object |

**错误码列表**

| 错误码 | 说明                                                    |
| :----- | :------------------------------------------------------ |
| 200001 | 参数错误                                                |
| 200002 | 系统繁忙,如幂等接口并发调用等，通常由于用户并发操作造成 |
| 200003 | 认证信息过期或错误,请重新登录                           |
| 200004 | 设备未激活                                              |
| 200005 | 当前sp暂未支持此接口                                    |
| 200006 | 系统错误,如内部调用超时等，由于服务内部异常导致         |
| 200200 | 可直充剩余次数为0                                       |
| 400000 | 登录授权失败                                            |
| 400001 | 设备端超时无响应                                        |
| 400002 | 调用SDK参数错误                                         |



### 登录授权部分

#### 用户设备登录授权

跳转酷狗音乐小程序授权，当再次返回 h5 或小程序时，Promise 状态改变。

**接口定义**

```typescript
tmeSdk.login(deviceId: string) => Promise<TMEResponse>
```

**参数说明**

| 参数名   | 参数描述 | 类型   | 必填 |
| -------- | -------- | ------ | ---- |
| deviceId | 设备Id   | string | 是   |

**返回值**

返回一个 `Promise<TMEResponse>`



#### 用户设备登出

原 token 将登出。

**接口定义**

```typescript
tmeSdk.getUserInfo(deviceId: string) => Promise<TMEResponse>
```

**参数说明**

| 参数名   | 参数描述 | 类型   | 必填 |
| -------- | -------- | ------ | ---- |
| deviceId | 设备 Id   | string | 是   |

**返回值**

返回一个 `Promise<TMEResponse>`



#### 校验设备授权

**接口定义**

```typescript
tmeSdk.checkDeviceAuth(deviceId: string) => Promise<TMEResponse>
```

**参数说明**

| 参数名   | 参数描述 | 类型   | 必填 |
| -------- | -------- | ------ | ---- |
| deviceId | 设备 Id   | string | 是   |

**返回值**

返回一个 `Promise<TMEResponse>`



#### 获取用户信息

**接口定义**

```typescript
tmeSdk.getUserInfo(deviceId: string) => Promise<TMEResponse>
```

**参数说明**

| 参数名   | 参数描述 | 类型   | 必填 |
| -------- | -------- | ------ | ---- |
| deviceId | 设备 Id   | string | 是   |

**返回值**

返回一个 `Promise<TMEResponse>`，其中data如下：

| 属性名           | 描述                   | 类型           |
| ---------------- | ---------------------- | -------------- |
| userid           | 用户id                 | string         |
| nick_name        | 用户昵称               | string         |
| img              | 用户头像               | string         |
| is_vip           | 是否 vip 0:否 1:是      | enum:  `0` `1` |
| vip_end_time     | vip 有效期终止时间      | string         |
| car_vip_end_time | 车机会员有效期终止时间 | string         |
| svip_end_time    | 豪V有效期终止时间      | string         |



### 播控部分

#### 接口描述

调用播控 SDK，会下发物模型属性 +control_seq，需要设备上报相同的 control_seq

- 若在超时范围内收到上报，视为下发播控成功，返回resolved状态的 `Promise<TMEResponse>`
- 若超时未收到上报，返回 rejected 状态的 `Promise<TMEResponse>`

超时设置可以通过 `tmeSdk.config.timeout` 来配置，默认值为10000，单位：毫秒(ms)



#### 通用播控接口

**接口定义**

```typescript
tmeSdk.controlKugouDeviceData(deviceData, deviceId: string) => Promise<TMEResponse>
```

**参数说明**

| 参数名     | 参数描述       | 类型   | 必填 |
| ---------- | -------------- | ------ | ---- |
| deviceData | 设备物模型数据 | object | 是   |
| deviceId   | 设备 Id         | string | 是   |

**返回值**

返回一个 `Promise<TMEResponse>`



#### 播放

**接口定义**

```typescript
tmeSdk.play(deviceId: string) => Promise<TMEResponse>
```

**参数说明**

| 参数名   | 参数描述 | 类型   | 必填 |
| -------- | -------- | ------ | ---- |
| deviceId | 设备 Id   | string | 是   |

**返回值**

返回一个 `Promise<TMEResponse>`



#### 暂停

**接口定义**

```typescript
tmeSdk.pause(deviceId: string) => Promise<TMEResponse>

```

**参数说明**

| 参数名   | 参数描述 | 类型   | 必填 |
| -------- | -------- | ------ | ---- |
| deviceId | 设备 Id   | string | 是   |

**返回值**

返回一个 `Promise<TMEResponse>`



#### 上一首

**接口定义**

```typescript
tmeSdk.preSong(deviceId: string) => Promise<TMEResponse>

```

**参数说明**

| 参数名   | 参数描述 | 类型   | 必填 |
| -------- | -------- | ------ | ---- |
| deviceId | 设备 Id   | string | 是   |

**返回值**

返回一个 `Promise<TMEResponse>`



#### 下一首

**接口定义**

```typescript
tmeSdk.nextSong(deviceId: string) => Promise<TMEResponse>

```

**参数说明**

| 参数名   | 参数描述 | 类型   | 必填 |
| -------- | -------- | ------ | ---- |
| deviceId | 设备 Id   | string | 是   |

**返回值**

返回一个 `Promise<TMEResponse>`



#### 设置播放模式

**接口定义**

```typescript
tmeSdk.setPlayMode(playMode: number, deviceId: string) => Promise<TMEResponse>

```

**参数说明**

| 参数名   | 参数描述                                   | 类型              | 必填 |
| -------- | ------------------------------------------ | ----------------- | ---- |
| playMode | 播放模式：0:顺序播放 1:单曲循环 2:随机播放 | enum: `0` `1` `2` | 是   |
| deviceId | 设备Id                                     | string            | 是   |

**返回值**

返回一个 `Promise<TMEResponse>`



#### 设置音量

**接口定义**

```typescript
tmeSdk.setVolume(volume: number, deviceId: string) => Promise<TMEResponse>

```

**参数说明**

| 参数名   | 参数描述        | 类型   | 必填 |
| -------- | --------------- | ------ | ---- |
| volume   | 音量：0-100之间 | number | 是   |
| deviceId | 设备Id          | string | 是   |

**返回值**

返回一个`Promise<TMEResponse>`



#### 设置播放进度

**接口定义**

```typescript
tmeSdk.setPlayPosition(playPosition: number, deviceId: string) => Promise<TMEResponse>

```

**参数说明**

| 参数名       | 参数描述             | 类型   | 必填 |
| ------------ | -------------------- | ------ | ---- |
| playPosition | 播放进度：单位:秒(s) | number | 是   |
| deviceId     | 设备Id               | string | 是   |

**返回值**

返回一个 `Promise<TMEResponse>`



#### 设置播放质量

**接口定义**

```typescript
tmeSdk.setPlayQuality(recommendQuality: number, deviceId: string) => Promise<TMEResponse>

```

**参数说明**

| 参数名           | 参数描述                       | 类型              | 必填 |
| ---------------- | ------------------------------ | ----------------- | ---- |
| recommendQuality | 播放质量：0:标准 1:高清 2:无损 | enum: `0` `1` `2` | 是   |
| deviceId         | 设备Id                         | string            | 是   |

**返回值**

返回一个 `Promise<TMEResponse>`



#### 设置当前播放歌曲

**接口定义**

```typescript
tmeSdk.playSong(songId: string, songIndex: string, newQueueType: string, newQueueId: string | number, deviceId: string) => Promise<TMEResponse>

```

**参数说明**

| 参数名       | 参数描述                                                  | 类型             | 必填 |
| ------------ | --------------------------------------------------------- | ---------------- | ---- |
| songId       | 歌曲 ID                                                    | string           | 是   |
| songIndex    | 歌曲所在播放列表的位置，从0开始                           | number           | 是   |
| newQueueType | 播放列表的类型： `playlist` `newSongs` `recommendDailty`  | string           | 是   |
| newQueueId   | 播放列表 ID（当类型为"每日推荐"时，不存在id，传undefined） | string \| number | 是   |
| deviceId     | 设备 Id                                                    | string           | 是   |

播放列表目前支持三种类型：歌单(playlist)、新歌首发(newSongs)、每日推荐(recommendDaily)

**返回值**

返回一个 `Promise<TMEResponse>`



### 内容部分

#### 拉取内容通用接口

请求酷狗 API 拉取内容通用接口

**接口定义**

```typescript
tmeSdk.requestTMEApi(action: string, params, deviceId: string) => Promise<TMEResponse>

```

**参数说明**

| 参数名   | 描述                         | 类型   | 必填 |
| -------- | ---------------------------- | ------ | ---- |
| action   | 接口 action                   | string | 是   |
| params   | 请求参数，无请求参数时，传{} | object | 是   |
| deviceId | 设备 Id                       | string | 是   |

**返回值**

返回一个`Promise<TMEResponse>`

注：action、params 及 返回值 data 参考 [音乐服务](https://cloud.tencent.com/document/product/1081/60545)

#### 获取设备当前播放歌曲

**接口定义**

```typescript
tmeSdk.getCurrentPlaySong(deviceId: string) => Promise<TMEResponse>

```

**参数说明**

| 参数名   | 描述   | 类型   | 必填 |
| -------- | ------ | ------ | ---- |
| deviceId | 设备 Id | string | 是   |

**返回值**

返回一个 `Promise<TMEResponse>`，data 为歌曲信息



#### 获取设备当前播放列表

根据目前支持的播放类型(playType)，拉取对应的歌单列表，并查出歌曲的详细信息

**接口定义**

```typescript
tmeSdk.getCurrentPlayQueue(deviceId: string) => Promise<TMEResponse>

```

**参数说明**

| 参数名   | 描述   | 类型   | 必填 |
| -------- | ------ | ------ | ---- |
| deviceId | 设备 Id | string | 是   |

**返回值**

返回一个 `Promise<TMEResponse>`

TMEResponse 中 data 如下

| 属性名   | 描述                                                         | 类型                                         |
| -------- | ------------------------------------------------------------ | -------------------------------------------- |
| playType | 播放列表类型                                                 | enum: `playlist` `newSongs` `recommendDaily` |
| queueId  | 当前播放列表 id，根据 playType 对应 playlist_id、album_id、top_id | string \| number                             |
| total    | 列表中歌曲总数                                               | number                                       |
| songs    | 歌曲数组，具体歌曲属性参考 TME 文档中 Song 属性                  | Array[]                                      |



#### 获取歌曲详细信息

**接口定义**

```typescript
tmeSdk.getSongDetail(songId: string, deviceId: string) => Promise<TMEResponse>

```

通过调用 requestTMEApi，请求歌曲播放链接与歌曲信息，返回歌曲的详细信息

**参数说明**

| 参数名   | 描述   | 类型   | 必填 |
| -------- | ------ | ------ | ---- |
| songId   | 歌曲 ID | string | 是   |
| deviceId | 设备 Id | string | 是   |

**返回值**

返回一个 `Promise<TMEResponse>`，data 为歌曲信息



#### 获取歌单详细信息

**接口定义**

```typescript
tmeSdk.getPlaylistDetail(action: string, params, deviceId: string) => Promise<TMEResponse>

```

通过调用 requestTMEApi，请求歌单列表与歌曲信息，丰富列表中的歌曲信息，返回歌单列表

**参数说明**

| 参数名   | 描述                                                         | 类型   | 必填 |
| -------- | ------------------------------------------------------------ | ------ | ---- |
| action   | 新歌首发(awesome_newsong)、每日推荐(awesome_everyday)、歌单歌曲(playlist_song) | string | 是   |
| params   | 参考应用端 API=>音乐服务中对应 API 的 KugouParams                | object | 是   |
| deviceId | 设备 Id                                                       | string | 是   |

**返回值**

返回一个 `Promise<TMEResponse>`，data 为歌单列表



