## 概述

通过 [qcloud-iotexplorer-bluetooth-adapter-llsync](https://www.npmjs.com/package/qcloud-iotexplorer-bluetooth-adapter-llsync) sdk， 小程序可以完成和标准蓝牙设备进行连接，绑定，控制等流程。通过下面的图片可以直观地了解整个流程:

<img src=https://iot-public-1256872341.cos.ap-guangzhou.myqcloud.com/shuaisguo/1629101191691.gif style="width: 200px">

您也可以通过官方的[小程序 SDK demo](https://github.com/tencentyun/qcloud-iotexplorer-appdev-miniprogram-sdk-demo)的 添加标准蓝牙设备 部分来掌握连接标准蓝牙设备的流程。



## 1. 创建一个 bluetoothAdapter

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



## 2. 获取蓝牙设备列表

通过 bluetoothAdapter.startSearch方法，我们可以发现设备，获得设备列表。

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

> ! 如果设备无法搜索到，请确认设备没有被绑定



## 3. 连接设备

用户从上面获取到的设备中选择一个，并发起连接操作时，可以调用 `bluetoothAdapter.connectDevice` 方法进行连接。连接成功后会返回一个 deviceAdapter，可以用来向连接的设备发送Wi-Fi，token等数据。

> ! 如果在连接时提示没有权限操作该产品，请到控制台/应用开发对应用和产品进行关联

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



## 4. 绑定设备

绑定设备时，可以传入familyId, roomId, 从而将设备绑定到特定的家庭和房间，绑定完成后，可以在设备列表中看到该设备。

```ts
try {
  const deviceId = await deviceAdapter.bindDevice({ familyId, roomId });
} catch (err) {
  console.log(err);
}
```


## 5. 鉴权设备

设备完成绑定后，并不能立即向蓝牙发送控制指令，在发送指令前需要先完成设备鉴权。

```ts
// ...连接设备操作

// 接下来连接鉴权
if (!deviceAdapter.authorized) {
	await deviceAdapter.authenticateConnection({
		deviceName: deviceName,
	});
}
```



## 6. 控制设备

完成绑定和鉴权设备之后，我们就可以向设备发送控制数据了，比如向设备下发一个 `property` 或者一个 `action`。这一切都可以调用应用端API完成，详见[设备控制](https://cloud.tencent.com/document/product/1081/47686#.E6.8E.A7.E5.88.B6.E8.AE.BE.E5.A4.87)

> ! 如果控制设备无效，可检查上一步鉴权设备是否成功。



## 7. 解绑设备

设备绑定后，也可以通过小程序发起删除设备的操作，这时，如果没有连接和鉴权，首先要连接和鉴权设备，如第4，第5步所示；然后调用`unbindDevice`，解绑完成后会断开连接，设备会恢复到未绑定的状态。

```ts
try{
  await deviceAdapter.unbindDevice({ familyId, deviceName });
} catch (err) {
  console.log(err);
}
```



## 8. 断开设备

我们可以通过`deviceAdapter.disconnectDevice()`断开设备连接：

```
await deviceAdapter.disconnectDevice()
```



## 9. deviceAdapter事件

| 事件       | 描述                   | 参数                          |
| ---------- | ---------------------- | ----------------------------- |
| connect    | 蓝牙设备连接时触发     | DeviceInfo                    |
| disconnect | 蓝牙设备连接断开时触发 | DeviceInfo                    |
| authorized | 蓝牙设备授权完成时触发 | { version, mtu, otaVersion, } |