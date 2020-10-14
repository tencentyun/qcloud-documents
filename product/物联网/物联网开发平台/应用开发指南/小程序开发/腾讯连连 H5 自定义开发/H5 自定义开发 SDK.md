
## 基本参数

H5 SDK 提供产品信息、设备数据、用户信息与家庭信息等基本参数供 H5 面板使用，可通过 `sdk.属性名` 取得。

| 属性名            | 类型                                                         | 描述                                                         |
| ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| deviceId          | string                                                       | 设备 ID，由 `{productId}/{deviceName}` 组成                  |
| productId         | string                                                       | 产品 ID                                                      |
| deviceName        | string                                                       | 设备名称                                                     |
| deviceInfo        | [DeviceList](https://cloud.tencent.com/document/product/1081/40780#devicelist) \| [ShareDevices](https://cloud.tencent.com/document/product/1081/40780#sharedevices) | 设备信息，数据结构同 [DeviceList](https://cloud.tencent.com/document/product/1081/40780#devicelist)；如果是分享设备，则数据结构同 [ShareDevices](https://cloud.tencent.com/document/product/1081/40780#sharedevices) |
| roomList          | [RoomList](https://cloud.tencent.com/document/product/1081/40780#roomlist)[] | 当前家庭的房间列表                                           |
| roomName          | string                                                       | 当前设备的房间名称                                           |
| dataTemplate      | string                                                       | 设备所在产品的物模型，与【数据模板】>【查看JSON】中展示的物模型定义一致 |
| deviceStatus      | number                                                       | 设备在线状态，在线: 1，非在线: 0                             |
| deviceDisplayName | string                                                       | 设备展示名称，会依次取：AliasName > productInfo&#46;name > deviceName 来展示 |
| isShareDevice     | boolean                                                      | 是否是分享设备                                               |
| familyId          | string                                                       | 设备所在家庭id，如果是分享设备则无此值                       |
| roomId            | string                                                       | 设备所在房间id，如果是分享设备则无此值                       |
| familyInfo        | [FamilyList](https://cloud.tencent.com/document/product/1081/40780#familylist) | 设备所在家庭详情，如果是分享设备则无此值                     |
| isFamilyOwner     | boolean                                                      | 用户是否是当前家庭的所有者                                   |
| userInfo          | object                                                       | 用户信息<br>Avatar: string; 头像 URL<br>CountryCode: string; 国家代码<br>Email: string; 邮箱地址<br>NickName: string; 昵称<br>PhoneNumber: string; 手机号码<br>UserID: string; 用户 ID |

## 设备管理

### 获取产品信息
执行以下命令代码获取产品信息：
```typescript
sdk.getProductInfo({ productId?: string }) => Promise<{
  ProductId: string,
  Name: string,
  Description: string,
  DataTemplate: string,
  NetType: string,
  CategoryId: number,
  ProductType: number,
  UpdateTime: number,
}>
```

#### 参数说明

| 参数名    | 参数描述                          | 类型   | 必填 |
| --------- | --------------------------------- | ------ | ---- |
| productId | 可选，不传则使用当前设备的产品 ID | string | 否   |

#### 返回值

一个 Promise，输出参数如下。

| 参数名       | 参数描述                             | 类型   |
| ------------ | ------------------------------------ | ------ |
| ProductId    | 产品 ID                              | string |
| Name         | 产品名称                             | string |
| Description  | 产品描述                             | string |
| DataTemplate | 产品数据模板                         | string |
| NetType      | 通信方式（子设备为接入网关协议）     | string |
| CategoryId   | 产品分类 ID                          | number |
| ProductType  | 产品类型（0: 普通产品；5: 网关产品） | number |
| UpdateTime   | 最后更新的 Unix 时间戳（秒级）       | number |

### 获取设备信息
执行以下命令代码获取设备信息：
```typescript
sdk.getDeviceInfo({ deviceId?: string }) => Promise<{
  ProductId: string,
  DeviceName: string,
  DeviceId: string,
  IconUrl: string,
  AliasName: string,
  UserId: string,
  RoomId: string,
  CreateTime: number,
  UpdateTime: number
} | {
  ProductId: string,
  DeviceName: string,
  DeviceId: string,
  IconUrl: string,
  AliasName: string,
  CreateTime: string
}>
```

#### 参数说明

| 参数名   | 参数描述                          | 类型   | 必填 |
| -------- | --------------------------------- | ------ | ---- |
| deviceId | 可选，不传则使用当前设备的设备 ID | string | 否   |

#### 返回值

一个 Promise，输出参数请参见 [DeviceList](https://cloud.tencent.com/document/product/1081/40780#devicelist)（非分享设备）及 [ShareDevices](https://cloud.tencent.com/document/product/1081/40780#sharedevices)（分享设备）

### 控制设备属性

执行以下命令代码对设备发起控制操作：
```typescript
sdk.controlDeviceData(data, deviceId?: string) => Promise
```

#### 参数说明

| 参数名   | 参数描述                          | 类型   | 必填 |
| -------- | --------------------------------- | ------ | ---- |
| data     |                                   | object | 是   |
| deviceId | 可选，不传则使用当前设备的设备 ID | string | 否   |

#### 返回值

返回一个 Promise，输出参数请参见 [用户控制设备](https://cloud.tencent.com/document/product/1081/40805)。

### 获取设备物模型数据
执行以下命令代码获取设备物理模型数据：
```typescript
sdk.getDeviceData({ deviceId?: string }) => Promise<object>
```

#### 参数说明

| 参数名   | 参数描述                          | 类型   | 必填 |
| -------- | --------------------------------- | ------ | ---- |
| deviceId | 可选，不传则使用当前设备的设备 ID | string | 否   |

#### 返回值

一个 Promise，输出参数为设备的物模型数据。

### 获取设备物模型历史数据
执行以下命令代码获取物模型历史数据：
```typescript
sdk.getDeviceDataHistory(options) => Promise<{
  RequestId: string,
  Context: string,
  FieldName: string,
  Listover: boolean,
  Results: DataHistoryItem[]
}>
```

#### 参数说明

| 参数名    | 参数描述                     | 类型   | 必填 |
| --------- | ---------------------------- | ------ | ---- |
| FieldName | 查询的属性名称               | string | 是   |
| MaxTime   | 结束时间，毫秒时间戳         | number | 是   |
| MinTime   | 开始时间，毫秒时间戳         | number | 是   |
| Context   | 翻页游标，首次查询时，可不带 | string | 否   |
| Limit     | 单页数据量                   | number | 是   |

#### 返回值

返回一个 Promise，输出参数请参见 [获取设备物模型历史数据](https://cloud.tencent.com/document/product/1081/43119)。

### 获取设备当前状态
执行以下命令代码获取设备当前状态：
```typescript
sdk.getDeviceStatus({ deviceId?: string }) => Promise<0 | 1>
```

#### 参数说明

| 参数名   | 参数描述                          | 类型   | 必填 |
| -------- | --------------------------------- | ------ | ---- |
| deviceId | 可选，不传则使用当前设备的设备 ID | string | 否   |

#### 返回值

一个 Promise，输出参数取值如下：
- 0：设备离线
- 1：设备在线

### 删除设备

执行以下命令代码询问用户是否确认删除设备，若用户确认，则删除指定设备，删除成功后 H5 面板将自动关闭：
```typescript
sdk.deleteDevice({ deviceId?: string }) => Promise<void>
```

#### 参数说明

| 参数名   | 参数描述                          | 类型   | 必填 |
| -------- | --------------------------------- | ------ | ---- |
| deviceId | 可选，不传则使用当前设备的设备 ID | string | 否   |

#### 返回值

一个 Promise。

### 获取自定义分享参数

若该设备是分享设备，且分享方设置自定义分享参数，则被分享方将在接受分享后，可通过执行以下命令代码获取自定义分享参数：
```typescript
sdk.getShareParams({ deviceId?: string }) => Promise<any>
```

#### 参数说明

| 参数名   | 参数描述                          | 类型   | 必填 |
| -------- | --------------------------------- | ------ | ---- |
| deviceId | 可选，不传则使用当前设备的设备 ID | string | 否   |

#### 返回值

一个 Promise，输出参数为自定义分享参数。

### 检查设备是否有可升级固件

执行以下命令代码检查指定设备是否有可升级固件，若有可升级固件，且设备在线，则弹出固件升级提示。
```typescript
sdk.checkFirmwareUpgrade({ deviceId?: string, silent?: boolean }) => Promise<{
  CurrentVersion: string;
  DstVersion: string;
}>
```

#### 参数说明

| 参数名   | 参数描述                                                     | 类型    | 必填 |
| -------- | ------------------------------------------------------------ | ------- | ---- |
| deviceId | 可选，不传则使用当前设备的设备 ID                            | string  | 否   |
| silent   | 可选，默认为 false。<li> true:静默检查固件升级，不弹出提示框<li>false：静默检查固件升级，弹出提示框| boolean | 否   |

#### 返回值

一个 Promise，输出参数请参见 [查询设备固件是否升级](https://cloud.tencent.com/document/product/1081/47129)。

### 进行固件升级

跳转到小程序的固件升级页面，进行固件升级。

```typescript
sdk.goFirmwareUpgradePage({ deviceId?: string }) => Promise
```

#### 参数说明

| 参数名   | 参数描述                          | 类型   | 必填 |
| -------- | --------------------------------- | ------ | ---- |
| deviceId | 可选，不传则使用当前设备的设备 ID | string | 否   |

## 用户管理

### 获取用户信息
执行以下命令代码获取用户信息：
```typescript
sdk.getUserInfo() => Promise<{
  Avatar: string;
  CountryCode: string;
  Email: string;
  NickName: string;
  PhoneNumber: string;
  UserID: string;
}>
```

#### 返回值

一个 Promise，输出参数如下。

| 参数名      | 参数描述 | 类型   |
| ----------- | -------- | ------ |
| Avatar      | 头像 URL | string |
| CountryCode | 国家代码 | string |
| Email       | 邮箱地址 | string |
| NickName    | 昵称     | string |
| PhoneNumber | 手机号码 | string |
| UserID      | 用户 ID  | string |

## 界面组件

### tips 组件

tips 组件，样式和风格与连连小程序一致。

<span id="sdk-tips-show"></span>

#### 展示 tips
执行以下命令代码展示 tips：
```typescript
sdk.tips.show(message, options) => Promise
```

##### 参数说明

| 参数名                | 参数描述                                                     | 类型                                         | 必填 |
| --------------------- | ------------------------------------------------------------ | -------------------------------------------- | ---- |
| message               | 提示文本                                                     | string                                       | 是   |
| options.type          | tips 类型                                                    | 'info' \| 'danger' \| 'loading' \| 'success' | 否   |
| options.waitForHide   | 若为 true，则 show 方法返回一个Promise，并且当关闭后才会触发 resolve | boolean                                      | 否   |
| options.duration      | 展示提示的时间，单位毫秒，默认 1500                          | number                                       | 否   |
| options.delayDuration | 默认为 0，单位毫秒，提示会在该延时后展示                     | number                                       | 否   |
| options.canClickClose | 默认为 true，点击 mask 是否能够关闭提示                      | boolean                                      | 否   |
| options.canBeReplace  | 默认为 false，为 false 时上一个提示未关闭前，再次调用 tips.show会被忽略 | boolean                                      | 否   |

#### 关闭 tips
执行以下命令代码关闭 tips：
```typescript
sdk.tips.hide() => Promise
```

<span id="sdk-tips-show-loading-tips"></span>

#### 展示 loading tips
执行以下命令代码展示 loading tips：
```typescript
sdk.tips.showLoading(message, options) => Promise
```
封装后的 `tips.show` 方法，等价于：
```javascript
sdk.tips.show(message, {
  type: 'loading',
  canBeReplace: true,
  duration: 0,
  delayDuration: 200,
  canClickClose: false,
  ...options,
});
```

##### 参数说明

请参见 [展示 tips 参数说明](#sdk-tips-show)。

#### 关闭 loading tips
执行以下命令代码关闭 loading tips：
```typescript
sdk.tips.hideLoading() => Promise
```

[展示 loading tips](#sdk-tips-show-loading-tips) 后必须主动调用本接口，否则 tips 将会一直保留。

```typescript
sdk.tips.hideLoading() => Promise
```

#### 展示成功 tips
执行以下命令代码展示成功 tips：
```typescript
sdk.tips.showSuccess: (message, options) => Promise
```
封装后的 `tips.show` 方法，等价于：
```javascript
sdk.tips.show(message, { type: 'success', ...options });
```

##### 参数说明

请参见 [展示 tips 参数说明](#sdk-tips-show)。

#### 展示提示 tips
执行以下命令代码展示提示 tips：
```typescript
sdk.tips.showInfo: (message, options) => Promise
```
封装后的 `tips.show` 方法，等价于：
```javascript
sdk.tips.show(message, { type: 'info', ...options });
```

##### 参数说明

请参见 [展示 tips 参数说明](#sdk-tips-show)。

#### 展示错误 tips
执行以下命令代码展示错误 tips：
先标准化处理错误展示信息，然后展示错误 tips。
```typescript
sdk.tips.showError: (error, options) => Promise
```
等价于：
```javascript
sdk.tips.show(getErrorMsg(error), { type: 'error', ...options });
```

##### 参数说明

| 参数名  | 参数描述                                    | 类型                             | 必填 |
| ------- | ------------------------------------------- | -------------------------------- | ---- |
| error   | 错误对象或错误信息                          | Error \| { code, msg } \| string | 是   |
| options | 请参见 [展示 tips 参数说明](#sdk-tips-show) | object                           | 否   |

<span id="sdk-tips-show-modal"></span>

#### 展示模态对话框

执行以下命令代码展示一个弹窗，参数、功能、样式同小程序原生 showModal 基本一致。
```typescript
sdk.tips.showModal(options) => Promise<boolean>
```

##### 参数说明

| 参数名       | 参数描述                      | 类型    | 必填 |
| ------------ | ----------------------------- | ------- | ---- |
| title        | 弹窗标题                      | string  | 否   |
| content      | 弹窗内容                      | string  | 否   |
| showCancel   | 是否展示取消按钮，默认为 true | boolean | 否   |
| cancelText   | 取消按钮文案，默认为"取消"    | string  | 否   |
| cancelColor  | 取消按钮颜色，默认为"#6C7078" | string  | 否   |
| confirmText  | 确认按钮文案，默认为"确定"    | string  | 否   |
| confirmColor | 确认按钮颜色，默认为"#0066FF" | string  | 否   |

##### 返回值

返回一个 `Promise<boolean>`：
- true ：代表用户单击确认。
- false ：代表用户单击取消。

#### 展示确认模态对话框

基于 `sdk.tips.showModal` 封装，用于向用户进行二次确认操作时使用。
```typescript
sdk.tips.confirm(title, content, options) => Promise<boolean>
```

##### 参数说明

| 参数名  | 参数描述                                      | 类型   | 必填 |
| ------- | --------------------------------------------- | ------ | ---- |
| title   | 弹窗标题                                      | string | 否   |
| content | 弹窗内容                                      | string | 否   |
| options | 请参见 [展示模态对话框](#sdk-tips-show-modal) | object | 否   |

##### 示例代码
用户确认示例代码如下：
```javascript
const isConfirm = await sdk.tips.confirm('确认删除该设备吗？');

if (isConfirm) {
  // 用户确认，执行后续流程
}
```

#### 展示提示模态对话框

基于 `sdk.tips.showModal` 封装，用于向用户进行消息提示操作时使用。
```typescript
sdk.tips.alert(content, options) => Promise<boolean>
```

##### 参数说明

| 参数名  | 参数描述                                      | 类型   | 必填 |
| ------- | --------------------------------------------- | ------ | ---- |
| content | 弹窗内容                                      | string | 否   |
| options | 请参见 [展示模态对话框](#sdk-tips-show-modal) | object | 否   |

##### 示例代码
向用户进行消息提示的示例代码如下：
```javascript
await sdk.tips.alert('该功能暂时无法使用，请稍后再试');
```

### 设备离线提示组件

设备离线提示组件，样式和风格与连连小程序一致。

#### 展示设备离线提示
执行以下命令代码展示设备离线提示：
```typescript
sdk.offlineTip.show() => void
// 或
sdk.showOfflineTip() => void
```

#### 关闭设备离线提示
执行以下命令代码关闭设备离线提示：
```typescript
sdk.offlineTip.hide() => void
// 或
sdk.hideOfflineTip() => void
```

### H5 自定义设备详情视图

<span id="sdk-show-device-detail">

#### 展示 H5 自定义设备详情视图

执行以下命令代码在当前 H5 展示一个铺满全屏的设备详情视图，支持增加自定义菜单项及按钮。
```typescript
sdk.showDeviceDetail(options) => void
```

##### 参数说明

| 参数名                  | 参数描述                                   | 类型                                     | 必填 |
| ----------------------- | ------------------------------------------ | ---------------------------------------- | ---- |
| deviceInfo              | 展示详情的设备信息，不传则使用当前设备信息 | object                                   | 否   |
| labelWidth              | 设备详情的 label 宽度，默认 110，单位 px     | number                                   | 否   |
| marginTop               | 设备详情的上间距，默认 10，单位 px         | number                                   | 否   |
| shareParams             | 自定义分享参数                             | object \| string                         | 否   |
| extendItems             | 自定义菜单配置                             | ExtendItemConfig[]                       | 否   |
| extendItems.labelIcon   | 展示在 label 前的 icon 地址                | string                                   | 否   |
| extendItems.label       | 自定义菜单项的标题                         | string                                   | 是   |
| extendItems.content     | 自定义菜单项的内容                         | string                                   | 否   |
| extendItems.className   | 自定义菜单项的样式类名                     | string                                   | 否   |
| extendItems.onClick     | 点击自定义菜单项后触发的回调               | () => any                                | 否   |
| extendButtons           | 自定义按钮配置                             | ExtendButtonConfig[]                     | 否   |
| extendButtons.text      | 自定义按钮文案                             | string                                   | 是   |
| extendButtons.className | 自定义按钮的样式类名                       | string                                   | 否   |
| extendButtons.type      | 自定义按钮的风格                           | '' \| 'danger' \| 'primary' \| 'warning' | 否   |
| extendButtons.onClick   | 自定义按钮点击后触发的回调                 | () => any                                | 是   |
| containerClassName      | 容器的样式类名                             | string                                   | 否   |

#### 关闭 H5 自定义设备详情视图
执行以下命令代码关闭 H5 自定义设备详情视图：
```typescript
sdk.hideDeviceDetail() => void
```

## 调用小程序能力

<span id="sdk-go-device-detail-page"></span>

### 跳转小程序的标准设备详情页面
执行以下命令代码跳转到小程序的标准设备详情页面：
```typescript
sdk.goDeviceDetailPage({
  reload?: boolean,
  deviceId?: string,
  isShareDevice?: string,
  shareParams?: object | string,
}) => Promise
```

#### 参数说明

| 参数名        | 参数描述                                                     | 类型             | 必填 |
| ------------- | ------------------------------------------------------------ | ---------------- | ---- |
| reload        | 如果为 `true`，则进入详情页后会重新拉取一次该设备的数据      | boolean          | 否   |
| deviceId      | 可选，不传则使用当前设备的设备 ID                            | string           | 否   |
| isShareDevice | 可选，设备是否为分享设备，不传则使用当前的 `sdk.isShareDevice` | boolean          | 否   |
| shareParams   | 可选，设备自定义分享参数                                     | object \| string | 否   |

### 跳转小程序的反馈页面
执行以下命令代码跳转小程序的反馈页面：
```typescript
sdk.goFeedBackPage() => Promise
```

### 跳转小程序的设备信息页面
执行以下命令代码跳转小程序的设备信息页面：
```typescript
sdk.goDeviceInfoPage({ deviceId?: string }) => Promise
```

#### 参数说明

| 参数名   | 参数描述                          | 类型   | 必填 |
| -------- | --------------------------------- | ------ | ---- |
| deviceId | 可选，不传则使用当前设备的设备 ID | string | 否   |

### 跳转小程序的修改设备名称页面
执行以下命令代码跳转小程序的修改设备名称页面：
```typescript
sdk.goEditDeviceNamePage: ({ deviceId?: string, name?: string }) => Promise
```

#### 参数说明

| 参数名   | 参数描述                             | 类型   | 必填 |
| -------- | ------------------------------------ | ------ | ---- |
| deviceId | 可选，不传则使用当前设备的设备 ID    | string | 否   |
| name     | 可选，不传则使用当前设备的 aliasName | string | 否   |

### 跳转小程序的房间设置页面
执行以下命令代码跳转小程序的房间设置页面：
```typescript
sdk.goRoomSettingPage({ deviceId?: string }) => Promise
```

#### 参数说明

| 参数名   | 参数描述                          | 类型   | 必填 |
| -------- | --------------------------------- | ------ | ---- |
| deviceId | 可选，不传则使用当前设备的设备 ID | string | 否   |

### 跳转小程序的设备分享页面
执行以下命令代码跳转小程序的设备分享页面：
```typescript
sdk.goShareDevicePage({ deviceId?: string }) => Promise
```

#### 参数说明

| 参数名   | 参数描述                          | 类型   | 必填 |
| -------- | --------------------------------- | ------ | ---- |
| deviceId | 可选，不传则使用当前设备的设备 ID | string | 否   |

### 小程序刷新数据

小程序在当前 H5 面板关闭后必须进行一次数据刷新，执行以下命令代码进行数据刷新：
```typescript
sdk.reloadAfterUnmount() => Promise
```

### 返回小程序的上一级页面
执行以下命令代码用于主动关闭 H5 面板：
```typescript
sdk.navBack() => Promise
```

### 设置当前页面的分享内容

设置当前页面的分享内容，通过 [wx.miniProgram.postMessage](https://developers.weixin.qq.com/miniprogram/dev/component/web-view.html) 向小程序推送分享信息，具体参考 [小程序页面分享文档](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onShareAppMessage-Object-object)。

```typescript
sdk.setShareConfig({ title: string, imgUrl: string? }) => Promise
```

#### 参数说明

| 参数名 | 参数描述                             | 类型   | 必填 |
| ------ | ------------------------------------ | ------ | ---- |
| title  | 分享的标题                           | string | 是   |
| imgUrl | 分享图片的地址，默认会取当前页面截图 | string | 否   |

## 应用端 API

H5 SDK 对应用端 API 的调用过程进行了封装，发送请求时会自动带上公共参数 `AccessToken` 与 `RequestId`。

### 调用应用端 API
执行以下命令代码进行调用应用端 API：
```typescript
sdk.requestTokenApi: (action, data, options) => Promise
```

#### 参数说明

| 参数名  | 参数描述                                                     | 类型   | 必填 |
| ------- | ------------------------------------------------------------ | ------ | ---- |
| action  | 具体应用端 API Action 名称，如：`AppGetDeviceStatuses`       | string | 是   |
| data    | 接口调用参数                                                 | object | 否   |
| options | 请参见 [wx.request](https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html) | object | 否   |

#### 返回值

- 请求成功（code=0）：返回一个 resolved 的 Promise，其值为应用端 API 响应中的 `Response` 部分数据。
- 请求失败：返回一个 rejected 的 Promise，其值的数据结构为：`{ code, msg, ...detail }`。

## 事件监听

### 监听事件
执行以下命令代码进行事件监听：
```typescript
sdk.on(type: string, listener: (...args) => void) => void
```

#### 参数说明

| 参数名   | 参数描述             | 类型              | 必填 |
| -------- | -------------------- | ----------------- | ---- |
| type     | 要监听的事件         | string            | 是   |
| listener | 事件触发时的回调函数 | (...args) => void | 是   |

### 取消监听事件
执行以下命令代码取消事件监听：
```typescript
sdk.off(type: string, listener: (...args) => void) => void
```

#### 参数说明

| 参数名   | 参数描述                                                   | 类型              | 必填 |
| -------- | ---------------------------------------------------------- | ----------------- | ---- |
| type     | 要取消监听的事件                                           | string            | 是   |
| listener | 要取消监听的事件的回调函数，不传则清除该事件的所有回调函数 | (...args) => void | 否   |

### WebSocket 事件

#### wsClose 事件
WebSocket 的 `close` 事件。

| 参数名 | 参数描述             | 类型   |
| ------ | -------------------- | ------ |
| code   | 服务器发送的关闭码   | number |
| reason | 服务器关闭连接的原因 | string |

#### wsError 事件

WebSocket 的错误事件。

#### wsControl 事件

当 WebSocket 收到 `control` 指令后触发。

| 参数名     | 参数描述 | 类型   |
| ---------- | -------- | ------ |
| deviceId   | 设备 ID  | string |
| deviceData | 设备数据 | object |

#### wsReport 事件

当 WebSocket 收到 `report` 指令后触发。

| 参数名     | 参数描述 | 类型   |
| ---------- | -------- | ------ |
| deviceId   | 设备 ID  | string |
| deviceData | 设备数据 | object |

#### wsStatusChange 事件

当 WebSocket 收到 `wsStatusChange` 指令后触发。

| 参数名       | 参数描述     | 类型   |
| ------------ | ------------ | ------ |
| deviceId     | 设备 ID      | string |
| deviceStatus | 设备在线状态 | 0 \| 1 |

### 前后台切换事件

#### appShow 事件

当小程序 [App.onShow](https://developers.weixin.qq.com/miniprogram/dev/reference/api/App.html#onShow-Object-object) 执行后触发。

#### appHide 事件

当小程序 [App.onHide](https://developers.weixin.qq.com/miniprogram/dev/reference/api/App.html#onHide) 执行后触发。

#### pageShow 事件

当小程序 [Page.onShow](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onShow) 执行后触发。

#### pageHide 事件

当小程序 [Page.onHide](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onHide) 执行后触发。

## 底层 SDK 能力

### 应用开发 SDK

```typescript
sdk.appDevSdk
```

应用开发 SDK 实例，H5 SDK 底层依赖 [应用开发小程序端 SDK](https://github.com/tencentyun/qcloud-iotexplorer-appdev-miniprogram-sdk#readme)，更多调用能力请参考应用开发 SDK 文档。

### JS SDK

```typescript
sdk.wx
```

微信 JS SDK 实例，具体用法请参见 [小程序 web-view 文档](https://developers.weixin.qq.com/miniprogram/dev/component/web-view.html)，使用前需要先调用 [初始化 JS SDK](#sdk-wx-sdk-ready)。

<span id="sdk-wx-sdk-ready"></span>

### 初始化 JS SDK

```typescript
sdk.wxSdkReady() => Promise
```

#### 示例代码

```javascript
sdk.wxSdkReady().then(() => wx.miniProgram.navigateBack());
```
