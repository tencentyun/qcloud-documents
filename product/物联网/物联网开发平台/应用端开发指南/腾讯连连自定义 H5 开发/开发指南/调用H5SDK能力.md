## 引入 H5 SDK

直接通过 Window 访问。

```
window.h5PanelSdk;
```

或 webpack 配置 externals。

```
// webpack.config.js
module.exports = {
  externals: {
    'qcloud-iotexplorer-h5-panel-sdk': 'h5PanelSdk',
  },
};
```



## 获取基本参数

H5 SDK 提供产品信息、设备数据、用户信息与家庭信息等基本参数供 H5 面板使用，可通过 `sdk.属性名` 取得。具体的参数列表，请参见 [基本参数](https://cloud.tencent.com/document/product/1081/67446)。

```javascript
console.log(sdk.deviceId);
```



## 调用应用端 API

关于应用端 API 的信息，请参见 [应用端 API 简介](https://cloud.tencent.com/document/product/1081/40773)。

H5 SDK 对应用端 API 的调用过程已进行封装，发送请求时将会自动带上公共参数 `AccessToken` 与 `RequestId`。以下示例代码以调用 [获取设备当前状态](https://cloud.tencent.com/document/product/1081/40804) 应用端 API 为例。

```javascript
const action = 'AppGetDeviceStatuses'; // 请求应用端 API 的 Action 名
const params = { // 请求应用端 API 的参数
  DeviceIds: [sdk.deviceId]
};
sdk.requestTokenApi(action, params).then(data = >  {
  // 请求成功
  console.log(data);
}).catch(err = >  {
  // 请求失败
  console.error(err);
});

```



## 控制设备

调用 H5 SDK 的 [控制设备属性](https://cloud.tencent.com/document/product/1081/67447#sdk-control-device-data) 接口可对指定设备发起控制操作。

```javascript
// 指定要控制的设备的属性数据
const deviceData = {
  light_switch: 0
};

// 控制 H5 面板当前设备
sdk.controlDeviceData(deviceData).then(data = >  {
  // 请求成功
  console.log(data);
}).catch(err = >  {
  // 请求失败
  console.error(err);
});

// 控制指定设备
const deviceId = '要控制的设备 ID';
sdk.controlDeviceData(deviceData, deviceId).then(data = >  {
  // 请求成功
  console.log(data);
}).catch(err = >  {
  // 请求失败
  console.error(err);
});

```



## 固件升级

SDK 封装了检查固件更新的接口，以及一个默认样式的固件升级提示。开发者通过调用 H5 SDK 提供的接口，可以检查设备当前是否有可升级固件，以及进行固件升级操作。

### 检查固件升级

调用 H5 SDK 的 [检查设备是否有可升级固件](https://cloud.tencent.com/document/product/1081/67447#sdk-check-firmware-upgrade) 接口，可以检查指定设备是否有可升级固件。开发者可以直接使用 H5 SDK 提供的默认样式固件升级提示，也可以利用该接口的返回值来实现自定义的固件升级提示，详情如下。

- 方式一：使用 H5 SDK 提供的默认样式固件升级提示
  执行以下命令调用 `sdk.checkFirmwareUpgrade` 。

```javascript
sdk.checkFirmwareUpgrade();
```

若当前设备有可升级固件，且设备在线，则弹出默认样式的固件升级提示。
![](https://main.qcloudimg.com/raw/9f5a254dfd4c92fde9e850249e4b14e7.png)

- 方式二：使用自定义的固件升级提示
  调用 `sdk.checkFirmwareUpgrade` 时传入 `silent` 参数值为 `true`，则不会弹出上述的默认样式固件升级提示。开发者可根据接口返回的固件升级信息，展示自定义的固件升级提示。其中 `CurrentVersion` 为设备当前固件版本，`DstVersion` 为固件可升级版本。

```javascript
sdk.checkFirmwareUpgrade({
  silent: true // silent 参数为 true 则不弹出 H5 SDK 的默认固件升级提示
}).then(({ CurrentVersion, DstVersion }) = >  {
  if (DstVersion && CurrentVersion !== DstVersion) {
    // 开发者需要在此处实现自定义的固件升级提示的展示
  }
});
```

### 进行固件升级

调用 H5 SDK 的 [进行固件升级](#H5面板SDK/sdk-go-firmware-upgrade-page) 接口，可对指定设备进行固件升级。调用该接口后，会跳转至小程序的固件升级页面，进行固件升级操作。

```javascript
// 对当前设备进行固件升级
sdk.goFirmwareUpgradePage();

// 对指定设备进行固件升级
sdk.goFirmwareUpgradePage({
  deviceId: '要进行固件升级的设备 ID'
});

```



## 长连接通信

H5 SDK 初始化时默认自动连接 WebSocket 服务端，并订阅当前设备的上报数据以及状态信息。

```javascript
// 监听设备上报数据推送
sdk.on('wsReport', ({ deviceId, deviceData }) = >  {
  console.log('websocket device report', deviceId, deviceData);
});

// 监听设备在线状态变更推送
sdk.on('wsStatusChange', ({ deviceId, deviceStatus }) = >  {
  console.log('websocket device status change', deviceId, deviceStatus);
});

// 监听设备控制推送
sdk.on('wsControl', ({ deviceId, deviceData }) = >  {
  console.log('websocket device control', deviceId, deviceData);
});

```



## 设备详情

H5 SDK 为开发者提供两种设备详情页面，开发者可以根据需要选择使用。

- 标准设备详情：跳转到小程序标准面板的设备详情页面。
- H5 自定义设备详情：在 H5 面板内展示设备详情页面，可在标准设备详情的基础上增加自定义的菜单和按钮。

#### 调用标准设备详情

执行以下代码后，将跳转到小程序标准面板的设备详情页面。

```javascript
sdk.goDeviceDetailPage();
```

<span id="h5-device-detail-example"> </span>

#### 调用 H5 自定义设备详情

执行以下代码后，将在 H5 面板内展示设备详情页面。关于 H5 自定义设备详情的接口参数描述，详见 [展示 H5 自定义设备详情视图](https://cloud.tencent.com/document/product/1081/67449#sdk-show-device-detail)。

```javascript
sdk.showDeviceDetail({
  labelWidth: 120, // 设备详情的label宽度
  marginTop: 8, // 设备详情的上间距
  shareParams: { // 设备分享时设置自定义分享参数
    a: 'a',
    b: 'b',
  },
  extendItems: [
    {
      labelIcon: 'https://main.qcloudimg.com/raw/be1d876d55ec2479d384e17c94****e69.svg',
      label: '自定义菜单',
      content: '自定义菜单内容（可选）',
      onClick: () = >  console.log('点击自定义菜单'),
    },
  ],
  extendButtons: [
    {
      text: '自定义按钮',
      type: 'warning',
      onClick: () = >  console.log('点击自定义按钮'),
    },
    {
      text: '自定义按钮2',
      type: 'primary',
      onClick: () = >  console.log('点击自定义按钮2'),
    },
    {
      text: '获取自定义分享参数',
      onClick: async () = >  {
        const shareParams = await sdk.getShareParams();
        console.log('自定义分享参数: ', shareParams);
      }
    },
    {
      text: '关闭设备详情',
      type: '',
      onClick: () = >  sdk.hideDeviceDetail(),
    },
  ],
});

```

<span id="gateway-panel-override" > </span > 

## 子设备使用网关面板

平台支持设定网关的面板配置对所有子产品生效，开启后，网关下的子产品将使用网关的面板配置。配置步骤如下：

1. 登录腾讯云 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer)，选择项目与网关产品，进入网关产品的产品详情页面。
2. 选择**交互开发** > **面板类型**，单击**配置**，进入面板配置页面。
   ![](https://main.qcloudimg.com/raw/26a4007c739f2ac1852554eaee0f28d0.png)
3. 在面板类型中选择**自定义 H5 面板**。
   ![](https://main.qcloudimg.com/raw/24b2e9a4553fc50fb5ee82a8bf87a487.png)
4. 开启网关子设备中**面板配置对所有子产品生效**的开关。
   ![](https://main.qcloudimg.com/raw/6ac2a5fbef758b9cbc224a7560c35589.png)



## 监听页面显示、隐藏事件

H5 SDK 提供页面显示、隐藏事件回调。当 H5 页面或小程序切换到前台或后台时，会触发相应的事件。开发者可以通过监听这些事件，在对应事件触发时执行自己的业务逻辑。

```javascript
// 监听 H5 页面切前台
sdk.on('pageShow', () = >  {
  console.log('on pageShow');
});

// 监听 H5 页面切后台
sdk.on('pageHide', () = >  {
  console.log('on pageHide');
});

// 监听小程序切前台
sdk.on('appShow', () = >  {
  console.log('on appShow');
});

// 监听小程序切后台
sdk.on('appHide', () = >  {
  console.log('on appHide');
});

// H5 页面切前台时，刷新页面标题的设备名称
sdk.on('pageShow', async () = >  {
  const deviceInfo = await sdk.getDeviceInfo();

  // 设备展示名称
  const deviceDisplayName = deviceInfo.AliasName || sdk.productInfo.Name;
  // 更新页面标题
  window.document.title = deviceDisplayName;
});

```



## 蓝牙设备通信

H5 面板内无法直接调用小程序的蓝牙接口，H5 SDK 中已封装 H5 面板与小程序间的蓝牙协议通信机制。要在 H5 面板使用蓝牙通信能力，必须使用 H5 SDK 提供的蓝牙模块。关于蓝牙设备的 H5 面板开发，请参见 [蓝牙设备文档](https://cloud.tencent.com/document/product/1081/67444)。

<span id="upload-h5-panel" > </span > 
