## 基本参数

H5 SDK 提供产品信息、设备数据、用户信息与家庭信息等基本参数供 H5 面板使用，可通过 `sdk.属性名` 取得。

| 属性名            | 类型                                                         | 描述                                                         |
| ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| deviceId          | string                                                       | 设备 ID，由 `{productId}/{deviceName}` 组成                  |
| productId         | string                                                       | 产品 ID                                                      |
| deviceName        | string                                                       | 设备名称                                                     |
| deviceInfo        | [DeviceList](https://cloud.tencent.com/document/product/1081/40780#devicelist) \| [ShareDevices](https://cloud.tencent.com/document/product/1081/40780#sharedevices) | 设备信息，数据结构同 [DeviceList](https://cloud.tencent.com/document/product/1081/40780#devicelist)；如果是分享设备，则数据结构同 [ShareDevices](https://cloud.tencent.com/document/product/1081/40780#sharedevices) |
| roomList          | [RoomList](https://cloud.tencent.com/document/product/1081/40780#roomlist)[] | 当前家庭的房间列表                                           |
| roomName          | string                                                       | 当前设备的房间名称                                           |
| dataTemplate      | string                                                       | 设备所在产品的物模型，与【数据模板】>【查看JSON】中展示的物模型定义一致 |
| deviceStatus      | number                                                       | 设备在线状态，在线：1，非在线：0                             |
| deviceDisplayName | string                                                       | 设备展示名称，会依次取：AliasName > productInfo&#46；name > deviceName 来展示 |
| isShareDevice     | boolean                                                      | 是否是分享设备                                               |
| familyId          | string                                                       | 设备所在家庭 ID，如果是分享设备则无此值                      |
| roomId            | string                                                       | 设备所在房间 ID，如果是分享设备则无此值                      |
| familyInfo        | [FamilyList](https://cloud.tencent.com/document/product/1081/40780#familylist) | 设备所在家庭详情，如果是分享设备则无此值                     |
| isFamilyOwner     | boolean                                                      | 用户是否是当前家庭的所有者                                   |
| userInfo          | object                                                       | 用户信息<li>Avatar：string；头像 URL<li>CountryCode：string；国家代码<li>Email：string；邮箱地址<li>NickName：string；昵称<li>PhoneNumber：string；手机号码<li>UserID：string；用户 ID |

## 设备管理

### 获取产品信息

- **接口定义**
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
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>productId</td>
<td>可选，不传则使用当前设备的产品 ID</td>
<td>string</td>
<td>否</td>
</tr>
</tbody></table>
- **返回值**
  返回一个 Promise，输出参数如下。
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
</tr>
</thead>
<tbody><tr>
<td>ProductId</td>
<td>产品 ID</td>
<td>string</td>
</tr>
<tr>
<td>Name</td>
<td>产品名称</td>
<td>string</td>
</tr>
<tr>
<td>Description</td>
<td>产品描述</td>
<td>string</td>
</tr>
<tr>
<td>DataTemplate</td>
<td>产品数据模板</td>
<td>string</td>
</tr>
<tr>
<td>NetType</td>
<td>通信方式（子设备为接入网关协议）</td>
<td>string</td>
</tr>
<tr>
<td>CategoryId</td>
<td>产品分类 ID</td>
<td>number</td>
</tr>
<tr>
<td>ProductType</td>
<td>产品类型（0：普通产品；5：网关产品）</td>
<td>number</td>
</tr>
<tr>
<td>UpdateTime</td>
<td>最后更新的 Unix 时间戳（秒级）</td>
<td>number</td>
</tr>
</tbody></table>


### 获取设备信息

- **接口定义**
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
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>deviceId</td>
<td>可选，不传则使用当前设备的设备 ID</td>
<td>string</td>
<td>否</td>
</tr>
</tbody></table>
- **返回值**
  返回一个 Promise，输出参数请参见 [DeviceList](https://cloud.tencent.com/document/product/1081/40780#devicelist)（非分享设备）和 [ShareDevices](https://cloud.tencent.com/document/product/1081/40780#sharedevices)（分享设备）。

<span id="sdk-control-device-data"></span>

### 控制设备属性

- **接口定义**
```typescript
sdk.controlDeviceData(data, deviceId?: string) => Promise
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>data</td>
<td>要控制的设备属性数据</td>
<td>object</td>
<td>是</td>
</tr>
<tr>
<td>deviceId</td>
<td>可选，不传则使用当前设备的设备 ID</td>
<td>string</td>
<td>否</td>
</tr>
</tbody></table>
- **返回值**
  返回一个 Promise，输出参数请参见 [用户控制设备](https://cloud.tencent.com/document/product/1081/40805)。

### 获取设备物模型数据

- **接口定义**
```typescript
sdk.getDeviceData({ deviceId?: string }) => Promise<object>
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>deviceId</td>
<td>可选，不传则使用当前设备的设备 ID</td>
<td>string</td>
<td>否</td>
</tr>
</tbody></table>
- **返回值**
  返回一个 Promise，输出参数为设备的物模型数据。

### 获取设备物模型历史数据

- **接口定义**
```typescript
sdk.getDeviceDataHistory({
	FieldName: string,
	MaxTime: number,
	MinTime: number,
	Context?: string,
	Limit: number
}) => Promise<{
	RequestId: string,
	Context: string,
	FieldName: string,
	Listover: boolean,
	Results: DataHistoryItem[]
}>
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>FieldName</td>
<td>查询的属性名称</td>
<td>string</td>
<td>是</td>
</tr>
<tr>
<td>MaxTime</td>
<td>结束时间，毫秒时间戳</td>
<td>number</td>
<td>是</td>
</tr>
<tr>
<td>MinTime</td>
<td>开始时间，毫秒时间戳</td>
<td>number</td>
<td>是</td>
</tr>
<tr>
<td>Context</td>
<td>翻页游标，首次查询时可不传</td>
<td>string</td>
<td>否</td>
</tr>
<tr>
<td>Limit</td>
<td>单页数据量</td>
<td>number</td>
<td>是</td>
</tr>
</tbody></table>
- **返回值**
  返回一个 Promise，输出参数请参见 [获取设备物模型历史数据](https://cloud.tencent.com/document/product/1081/43119)。

### 获取设备当前状态

- **接口定义**
```typescript
sdk.getDeviceStatus({ deviceId?: string }) => Promise<0 | 1>
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>deviceId</td>
<td>可选，不传则使用当前设备的设备 ID</td>
<td>string</td>
<td>否</td>
</tr>
</tbody></table>
- **返回值**
  返回一个 Promise，输出参数取值如下：
 - 0：设备离线
 - 1：设备在线

### 删除设备

- **接口定义**
```typescript
sdk.deleteDevice({ deviceId?: string }) => Promise<void>
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>deviceId</td>
<td>可选，不传则使用当前设备的设备 ID</td>
<td>string</td>
<td>否</td>
</tr>
</tbody></table>
- **返回值**
  返回一个 Promise。

### 获取自定义分享参数
若该设备是分享设备，且分享方设置了自定义分享参数，则被分享方在接受分享后可通过该接口获取自定义分享参数。

- **接口定义**
```typescript
sdk.getShareParams({ deviceId?: string }) => Promise<any>
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>deviceId</td>
<td>可选，不传则使用当前设备的设备 ID</td>
<td>string</td>
<td>否</td>
</tr>
</tbody></table>
- **返回值**
  返回一个 Promise，输出参数为自定义分享参数。

<span id="sdk-check-firmware-upgrade"></span>

### 检查设备是否有可升级固件

检查指定设备是否有可升级固件，若有可升级固件，且设备在线，则弹出固件升级提示。
- **接口定义**
```typescript
sdk.checkFirmwareUpgrade({
	deviceId?: string,
	silent?: boolean
}) => Promise<{
	CurrentVersion: string,
	DstVersion: string,
}>
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>deviceId</td>
<td>可选，不传则使用当前设备的设备 ID</td>
<td>string</td>
<td>否</td>
</tr>
<tr>
<td>silent</td>
<td>可选，默认为 false。<br><ul><li>true：只检查固件升级，不弹出固件升级提示</li><li>false：检查固件升级，若有可升级固件，且设备在线，则弹固件升级提示</li></ul></td>
<td>boolean</td>
<td>否</td>
</tr>
</tbody></table>
- **返回值**
  返回一个 Promise，输出参数请参见 [查询设备固件是否升级](https://cloud.tencent.com/document/product/1081/47129)。
	
<span id="sdk-go-firmware-upgrade-page"></span>
### 进行固件升级
跳转到小程序的固件升级页面，进行固件升级。
- **接口定义**
```typescript
sdk.goFirmwareUpgradePage({ deviceId?: string }) => Promise
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>deviceId</td>
<td>可选，不传则使用当前设备的设备 ID</td>
<td>string</td>
<td>否</td>
</tr>
</tbody></table>

## 用户管理

### 获取用户信息

- **接口定义**
```typescript
sdk.getUserInfo() => Promise<{
	Avatar: string,
	CountryCode: string,
	Email: string,
	NickName: string,
	PhoneNumber: string,
	UserID: string
}>
```
-  **返回值**
   返回一个 Promise，输出参数如下。
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
</tr>
</thead>
<tbody><tr>
<td>Avatar</td>
<td>头像 URL</td>
<td>string</td>
</tr>
<tr>
<td>CountryCode</td>
<td>国家代码</td>
<td>string</td>
</tr>
<tr>
<td>Email</td>
<td>邮箱地址</td>
<td>string</td>
</tr>
<tr>
<td>NickName</td>
<td>昵称</td>
<td>string</td>
</tr>
<tr>
<td>PhoneNumber</td>
<td>手机号码</td>
<td>string</td>
</tr>
<tr>
<td>UserID</td>
<td>用户 ID</td>
<td>string</td>
</tr>
</tbody></table>

## 界面组件

### tips 组件

tips 组件，样式和风格与连连小程序一致。

<span id="sdk-tips-show"></span>

#### 展示 tips
 - **接口定义**
```typescript
sdk.tips.show(message, options) => Promise
```
 - **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>message</td>
<td>提示文本</td>
<td>string</td>
<td>是</td>
</tr>
<tr>
<td>options.type</td>
<td>tips 类型</td>
<td>'info' | 'danger' | 'loading' | 'success'</td>
<td>否</td>
</tr>
<tr>
<td>options.waitForHide</td>
<td>若为 true，则 show 方法返回一个 Promise，并且当关闭后才会触发 resolve</td>
<td>boolean</td>
<td>否</td>
</tr>
<tr>
<td>options.duration</td>
<td>展示提示的时间，单位毫秒，默认1500</td>
<td>number</td>
<td>否</td>
</tr>
<tr>
<td>options.delayDuration</td>
<td>默认为0，单位毫秒，提示会在该延时后展示</td>
<td>number</td>
<td>否</td>
</tr>
<tr>
<td>options.canClickClose</td>
<td>默认为 true，点击 mask 是否能够关闭提示</td>
<td>boolean</td>
<td>否</td>
</tr>
<tr>
<td>options.canBeReplace</td>
<td>默认为 false，为 false 时上一个提示未关闭前，再次调用 tips.show 会被忽略</td>
<td>boolean</td>
<td>否</td>
</tr>
</tbody></table>

#### 关闭 tips
**接口定义**
```typescript
sdk.tips.hide() => Promise
```

<span id="sdk-tips-show-loading-tips"></span>

#### 展示 loading tips
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

 - **接口定义**
```typescript
sdk.tips.showLoading(message, options) => Promise
```
 - **参数说明**
   请参见 [展示 tips 参数说明](#sdk-tips-show)。

#### 关闭 loading tips
  [展示 loading tips](#sdk-tips-show-loading-tips) 后必须主动调用本接口，否则 tips 将会一直保留。
	
**接口定义**
```typescript
sdk.tips.hideLoading() => Promise
```

#### 展示成功 tips
封装后的 `tips.show` 方法，等价于：
```javascript
sdk.tips.show(message, { type: 'success', ...options });
```
- **接口定义**
```typescript
sdk.tips.showSuccess(message, options) => Promise
```
- **参数说明**
  请参见 [展示 tips 参数说明](#sdk-tips-show)。

#### 展示提示 tips
封装后的 `tips.show` 方法，等价于：
```javascript
sdk.tips.show(message, { type: 'info', ...options });
```
 - **接口定义**
```typescript
sdk.tips.showInfo(message, options) => Promise
```
 - **参数说明**
   请参见 [展示 tips 参数说明](#sdk-tips-show)。

#### 展示错误 tips
  先标准化处理错误展示信息，然后展示错误 tips。等价于：
```javascript
sdk.tips.show(getErrorMsg(error), { type: 'error', ...options });

```
 - **接口定义**
```typescript
sdk.tips.showError(error, options) => Promise
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>error</td>
<td>错误对象或错误信息</td>
<td>Error | { code, msg } | string</td>
<td>是</td>
</tr>
<tr>
<td>options</td>
<td>请参见 <a href="#sdk-tips-show">展示 tips 参数说明</a></td>
<td>object</td>
<td>否</td>
</tr>
</tbody></table>

<span id="sdk-tips-show-modal"></span>

#### 展示模态对话框
展示一个弹窗，参数、功能、样式同小程序原生 showModal 基本一致。

 - **接口定义**
```typescript
sdk.tips.showModal({
	 title?: string,
	 content?: string,
	 showCancel?: boolean,
	 cancelText?: string,
	 cancelColor?: string,
	 confirmText?: string,
	 confirmColor?: string,
}) => Promise<boolean>
```
 - **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>title</td>
<td>弹窗标题</td>
<td>string</td>
<td>否</td>
</tr>
<tr>
<td>content</td>
<td>弹窗内容</td>
<td>string</td>
<td>否</td>
</tr>
<tr>
<td>showCancel</td>
<td>是否展示取消按钮，默认为 true</td>
<td>boolean</td>
<td>否</td>
</tr>
<tr>
<td>cancelText</td>
<td>取消按钮文案，默认为“取消”</td>
<td>string</td>
<td>否</td>
</tr>
<tr>
<td>cancelColor</td>
<td>取消按钮颜色，默认为“#6C7078”</td>
<td>string</td>
<td>否</td>
</tr>
<tr>
<td>confirmText</td>
<td>确认按钮文案，默认为“确定”</td>
<td>string</td>
<td>否</td>
</tr>
<tr>
<td>confirmColor</td>
<td>确认按钮颜色，默认为“#0066FF”</td>
<td>string</td>
<td>否</td>
</tr>
</tbody></table>
 - **返回值**
  返回一个 `Promise<boolean>`：
  - true ：代表用户单击确认。
  - false ：代表用户单击取消。

#### 展示确认模态对话框
 基于 `sdk.tips.showModal` 封装，用于向用户进行二次确认操作时使用。
 
 - **接口定义**
```typescript
sdk.tips.confirm(title, content, options) => Promise<boolean>
```
 - **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>title</td>
<td>弹窗标题</td>
<td>string</td>
<td>否</td>
</tr>
<tr>
<td>content</td>
<td>弹窗内容</td>
<td>string</td>
<td>否</td>
</tr>
<tr>
<td>options</td>
<td>请参见 <a href="#sdk-tips-show-modal">展示模态对话框</a></td>
<td>object</td>
<td>否</td>
</tr>
</tbody></table>
 - **示例代码**
 用户确认示例代码如下：
```javascript
const isConfirm = await sdk.tips.confirm('确认删除该设备吗？');
if (isConfirm) {
  // 用户确认，执行后续流程
}
```

#### 展示提示模态对话框
  基于 `sdk.tips.showModal` 封装，用于向用户进行消息提示操作时使用。
	
 - **接口定义**
```typescript
sdk.tips.alert(content, options) => Promise<boolean>
```
 -  **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>content</td>
<td>弹窗内容</td>
<td>string</td>
<td>否</td>
</tr>
<tr>
<td>options</td>
<td>请参见 <a href="#sdk-tips-show-modal">展示模态对话框</a></td>
<td>object</td>
<td>否</td>
</tr>
</tbody></table>

 - **示例代码**
 向用户进行消息提示的示例代码如下：
```javascript
await sdk.tips.alert('该功能暂时无法使用，请稍后再试');
```

### 设备离线提示组件

设备离线提示组件，样式和风格与连连小程序一致。

#### 展示设备离线提示
**接口定义**
```typescript
sdk.offlineTip.show() => void
// 或
sdk.showOfflineTip() => void
```

#### 关闭设备离线提示
**接口定义**
```typescript
sdk.offlineTip.hide() => void
// 或
sdk.hideOfflineTip() => void
```

### H5 自定义设备详情视图

<span id="sdk-show-device-detail"></span>

#### 展示 H5 自定义设备详情视图
在当前 H5 展示一个铺满全屏的设备详情视图，支持增加自定义菜单项及按钮。

- **接口定义**
```typescript
sdk.showDeviceDetail({
	deviceInfo?: object,
	labelWidth?: number,
	marginTop?: number,
	shareParams?: object,
	extendItems?: ExtendItemConfig[],
	extendButtons?: ExtendButtonConfig[],
	containerClassName?: string
}) => void
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>deviceInfo</td>
<td>展示详情的设备信息，不传则使用当前设备信息</td>
<td>object</td>
<td>否</td>
</tr>
<tr>
<td>labelWidth</td>
<td>设备详情的 label 宽度，默认110，单位 px</td>
<td>number</td>
<td>否</td>
</tr>
<tr>
<td>marginTop</td>
<td>设备详情的上间距，默认10，单位 px</td>
<td>number</td>
<td>否</td>
</tr>
<tr>
<td>shareParams</td>
<td>自定义分享参数</td>
<td>object | string</td>
<td>否</td>
</tr>
<tr>
<td>extendItems</td>
<td>自定义菜单配置</td>
<td>ExtendItemConfig[]</td>
<td>否</td>
</tr>
<tr>
<td>extendItems[].labelIcon</td>
<td>展示在 label 前的 icon 地址</td>
<td>string</td>
<td>否</td>
</tr>
<tr>
<td>extendItems[].label</td>
<td>自定义菜单项的标题</td>
<td>string</td>
<td>是</td>
</tr>
<tr>
<td>extendItems[].content</td>
<td>自定义菜单项的内容</td>
<td>string</td>
<td>否</td>
</tr>
<tr>
<td>extendItems[].className</td>
<td>自定义菜单项的样式类名</td>
<td>string</td>
<td>否</td>
</tr>
<tr>
<td>extendItems[].onClick</td>
<td>点击自定义菜单项后触发的回调</td>
<td>() =&gt; any</td>
<td>否</td>
</tr>
<tr>
<td>extendButtons</td>
<td>自定义按钮配置</td>
<td>ExtendButtonConfig[]</td>
<td>否</td>
</tr>
<tr>
<td>extendButtons[].text</td>
<td>自定义按钮文案</td>
<td>string</td>
<td>是</td>
</tr>
<tr>
<td>extendButtons[].className</td>
<td>自定义按钮的样式类名</td>
<td>string</td>
<td>否</td>
</tr>
<tr>
<td>extendButtons[].type</td>
<td>自定义按钮的风格</td>
<td>'' | 'danger' | 'primary' | 'warning'</td>
<td>否</td>
</tr>
<tr>
<td>extendButtons[].onClick</td>
<td>自定义按钮点击后触发的回调</td>
<td>() =&gt; any</td>
<td>是</td>
</tr>
<tr>
<td>containerClassName</td>
<td>容器的样式类名</td>
<td>string</td>
<td>否</td>
</tr>
</tbody></table>

#### 关闭 H5 自定义设备详情视图
 **接口定义**
```typescript
sdk.hideDeviceDetail() => void
```

## 调用小程序能力

<span id="sdk-go-device-detail-page"></span>

### 跳转小程序的标准设备详情页面

- **接口定义**
```typescript
sdk.goDeviceDetailPage({
	reload?: boolean,
	deviceId?: string,
	isShareDevice?: string,
	shareParams?: object | string,
}) => Promise
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>reload</td>
<td><ul><li>如果为 <code>true</code>，则进入详情页后会重新拉取一次该设备的数据</li><li>如果为 <code>false</code>，则进入详情页后会使用缓存的设备数据</li></ul></td>
<td>boolean</td>
<td>否</td>
</tr>
<tr>
<td>deviceId</td>
<td>可选，不传则使用当前设备的设备 ID</td>
<td>string</td>
<td>否</td>
</tr>
<tr>
<td>isShareDevice</td>
<td>可选，设备是否为分享设备，不传则使用当前的 <code>sdk.isShareDevice</code></td>
<td>boolean</td>
<td>否</td>
</tr>
<tr>
<td>shareParams</td>
<td>可选，设备自定义分享参数</td>
<td>object | string</td>
<td>否</td>
</tr>
</tbody></table>

### 跳转小程序的反馈页面

**接口定义**
```typescript
sdk.goFeedBackPage() => Promise
```
### 跳转小程序的设备信息页面
- **接口定义**
```typescript
sdk.goDeviceInfoPage({ deviceId?: string }) => Promise
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>deviceId</td>
<td>可选，不传则使用当前设备的设备 ID</td>
<td>string</td>
<td>否</td>
</tr>
</tbody></table>

### 跳转小程序的修改设备名称页面

- **接口定义**
```typescript
sdk.goEditDeviceNamePage: ({ deviceId?: string, name?: string }) => Promise
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>deviceId</td>
<td>可选，不传则使用当前设备的设备 ID</td>
<td>string</td>
<td>否</td>
</tr>
<tr>
<td>name</td>
<td>可选，不传则使用当前设备的 aliasName</td>
<td>string</td>
<td>否</td>
</tr>
</tbody></table>

### 跳转小程序的房间设置页面

- **接口定义**
```typescript
sdk.goRoomSettingPage({ deviceId?: string }) => Promise
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>deviceId</td>
<td>可选，不传则使用当前设备的设备 ID</td>
<td>string</td>
<td>否</td>
</tr>
</tbody></table>

### 跳转小程序的设备分享页面

- **接口定义**
```typescript
sdk.goShareDevicePage({ deviceId?: string }) => Promise
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>deviceId</td>
<td>可选，不传则使用当前设备的设备 ID</td>
<td>string</td>
<td>否</td>
</tr>
</tbody></table>

### 小程序刷新数据

要求小程序在当前 H5 面板关闭后进行一次数据刷新。

**接口定义**
```typescript
sdk.reloadAfterUnmount() => Promise
```

### 返回小程序的上一级页面
可用于主动关闭 H5 面板。

**接口定义**
```typescript
sdk.navBack() => Promise
```

### 设置当前页面的分享内容

设置当前页面的分享内容，通过 [wx.miniProgram.postMessage](https://developers.weixin.qq.com/miniprogram/dev/component/web-view.html) 向小程序推送分享信息，具体参考 [小程序页面分享文档](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onShareAppMessage-Object-object)。

- **接口定义**
```typescript
sdk.setShareConfig({ title: string, imgUrl: string? }) => Promise
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>title</td>
<td>分享的标题</td>
<td>string</td>
<td>是</td>
</tr>
<tr>
<td>imgUrl</td>
<td>分享图片的地址，默认会取当前页面截图</td>
<td>string</td>
<td>否</td>
</tr>
</tbody></table>

## 应用端 API

H5 SDK 对应用端 API 的调用过程进行了封装，发送请求时会自动带上公共参数 `AccessToken` 与 `RequestId`。

### 调用应用端 API

- **接口定义**
```typescript
sdk.requestTokenApi(action, data, options) => Promise
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>action</td>
<td>具体应用端 API Action 名称，如：<code>AppGetDeviceStatuses</code></td>
<td>string</td>
<td>是</td>
</tr>
<tr>
<td>data</td>
<td>接口调用参数</td>
<td>object</td>
<td>否</td>
</tr>
<tr>
<td>options</td>
<td>请参见 <a href="https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html" target="_blank">wx.request</a></td>
<td>object</td>
<td>否</td>
</tr>
</tbody></table>
- **返回值**
 - 请求成功（code=0）：返回一个 resolved 的 Promise，其值为应用端 API 响应中的 `Response` 部分数据。
 - 请求失败：返回一个 rejected 的 Promise，其值的数据结构为：`{ code, msg, ...detail }`。

## 事件监听

### 监听事件

- **接口定义**
```typescript
sdk.on(type: string, listener: (...args) => void) => void
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>type</td>
<td>要监听的事件</td>
<td>string</td>
<td>是</td>
</tr>
<tr>
<td>listener</td>
<td>事件触发时的回调函数</td>
<td>(...args) =&gt; void</td>
<td>是</td>
</tr>
</tbody></table>

### 取消监听事件

- **接口定义**
```typescript
sdk.off(type: string, listener: (...args) => void) => void
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>type</td>
<td>要取消监听的事件</td>
<td>string</td>
<td>是</td>
</tr>
<tr>
<td>listener</td>
<td>要取消监听的事件的回调函数，不传则清除该事件的所有回调函数</td>
<td>(...args) =&gt; void</td>
<td>否</td>
</tr>
</tbody></table>

### WebSocket 事件
- **wsClose 事件**：WebSocket 的 `close` 事件。
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
</tr>
</thead>
<tbody><tr>
<td>code</td>
<td>服务器发送的关闭码</td>
<td>number</td>
</tr>
<tr>
<td>reason</td>
<td>服务器关闭连接的原因</td>
<td>string</td>
</tr>
</tbody></table>
- **wsError 事件**：WebSocket 的错误事件。
- **wsControl 事件**：当 WebSocket 收到 `control` 指令后触发。
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
</tr>
</thead>
<tbody><tr>
<td>deviceId</td>
<td>设备 ID</td>
<td>string</td>
</tr>
<tr>
<td>deviceData</td>
<td>设备数据</td>
<td>object</td>
</tr>
</tbody></table>
- **wsReport 事件**：当 WebSocket 收到 `report` 指令后触发。
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
</tr>
</thead>
<tbody><tr>
<td>deviceId</td>
<td>设备 ID</td>
<td>string</td>
</tr>
<tr>
<td>deviceData</td>
<td>设备数据</td>
<td>object</td>
</tr>
</tbody></table>
- **wsStatusChange 事件**：当 WebSocket 收到 `wsStatusChange` 指令后触发。
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
</tr>
</thead>
<tbody><tr>
<td>deviceId</td>
<td>设备 ID</td>
<td>string</td>
</tr>
<tr>
<td>deviceStatus</td>
<td>设备在线状态</td>
<td>0 | 1</td>
</tr>
</tbody></table>
- **wsEventReport 事件**：当 WebSocket 收到 `wsEventReport` 指令后触发。
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
</tr>
</thead>
<tbody><tr>
<td>deviceId</td>
<td>设备 ID</td>
<td>string</td>
</tr>
<tr>
<td>Payload</td>
<td>设备回复详情</td>
<td>object</td>
</tr>
</tbody></table>
- **wsActionPush 事件**：当 WebSocket 收到 `wsActionPush` 指令后触发。
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
</tr>
</thead>
<tbody><tr>
<td>deviceId</td>
<td>设备 ID</td>
<td>string</td>
</tr>
<tr>
<td>Payload</td>
<td>下发的 Action 指定详情</td>
<td>object</td>
</tr>
</tbody></table>
- **wsActionReport 事件**：当 WebSocket 收到 `wsActionReport` 指令后触发。
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
</tr>
</thead>
<tbody><tr>
<td>deviceId</td>
<td>设备 ID</td>
<td>string</td>
</tr>
<tr>
<td>Payload</td>
<td>设备回复的 Action 响应详情</td>
<td>object</td>
</tr>
</tbody></table>

### 前后台切换事件
- **appShow 事件**：当小程序 [App.onShow](https://developers.weixin.qq.com/miniprogram/dev/reference/api/App.html#onShow-Object-object) 执行后触发。
- **appHide 事件**：当小程序 [App.onHide](https://developers.weixin.qq.com/miniprogram/dev/reference/api/App.html#onHide) 执行后触发。
- **pageShow 事件**：当小程序 [Page.onShow](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onShow) 执行后触发。
- **pageHide 事件**：当小程序 [Page.onHide](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onHide) 执行后触发。

## 蓝牙模块

### 名词解释
<table>
<tr>
<th>名词</th><th>解释</th>
</tr>
<tr>
<td>serviceId</td><td>服务 id，蓝牙服务的 uuid，搜索设备时主要通过 <code>serviceId</code> 来过滤我们需要的设备。</td>
</tr>
<tr>
<td>deviceId</td><td>小程序 API 搜索出来的设备的标识，连接设备时主要通过 <code>deviceId</code> 来标识需要连接的设备。</td>
</tr>
<tr>
<td>explorerDeviceId</td><td>物联网开发平台侧定义的设备 ID，查询设备数据和上报设备数据时以设备 ID 作为设备标识。</td>
</tr>
<tr>
<td>BlueToothAdapter 蓝牙适配器</td><td>全局单例，实例上声明了蓝牙搜索、连接等方法。</td>
</tr>
<tr>
<td>DeviceAdapter 设备适配器</td><td>真正用来连接设备以及跟设备进行通信的模块，每一个设备连接对应一个设备适配器实例，设备适配器会在连接设备后实例化，并在设备断开连接后销毁。根据不同的 <code>serviceId</code> 来区别不同类型设备的适配器构造函数。</td>
</tr>
</table>

### 蓝牙适配器

#### 添加设备适配器
添加一个设备适配器。默认无任何设备适配器，使用蓝牙模块时需要根据具体设备情况创建一个设备适配器，并调用本接口将其构造函数添加到蓝牙适配器中。
 - **接口定义**
```typescript
sdk.bluetoothAdapter.addAdapter(deviceAdapter: DeviceAdapterConstructor) => void
```
 - **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>deviceAdapter</td>
<td>要添加的设备适配器的构造函数</td>
<td>DeviceAdapterConstructor</td>
<td>是</td>
</tr>
</tbody></table>
 - **示例代码**
 ```javascript
class DemoDeviceAdapter extends DeviceAdapter {
	static serviceId = '0000FFF0-0000-1000-8000-00805F9B34CC';
	static deviceFilter(deviceInfo) {
		if (deviceInfo.advertisServiceUUIDs) {
			const matchedServiceId = deviceInfo.advertisServiceUUIDs.find(id => id === DemoDeviceAdapter.serviceId);
			if (matchedServiceId && deviceInfo.advertisData) {
				try {
					const macArr = deviceInfo.advertisData.slice(2);
					const mac = macArr.join(':');
					return {
						...deviceInfo,
						deviceName: mac,
						serviceId: matchedServiceId,
					};
				} catch (err) {
					console.error('parse mac error', err);
				}
			}
		}
	}
	handleBLEMessage(hex) {
		return {
			type: 'unknown',
			data: hex,
		};
	}
}
sdk.bluetoothAdapter.addAdapter(DemoDeviceAdapter);
 ```

#### 初始化蓝牙模块

初始化蓝牙模块，包括初始化蓝牙模块、打通小程序间蓝牙通信以及注册全局回调等。本接口可重复调用，可在每次使用蓝牙模块前调用。

 - **接口定义**
```typescript
sdk.blueToothAdapter.init() => Promise<void>
```
 - **返回值**
   返回一个带缓存的 Promise，初始化成功后 resolve。若初始化未完成或已初始化成功，则多次调用后返回同一个 Promise。若初始化失败，则该缓存的 Promise 在 reject 之后会被释放，再次调用则将重新初始化。
 - **示例代码**
```javascript
sdk.blueToothAdapter.init().then(() => {
  // 调用蓝牙模块能力
});
```

<span id="sdk-bluetooth-adapter-start-search"></span>

#### 开始搜索蓝牙设备

开始搜索蓝牙设备。（将会调用 [wx.startBluetoothDevicesDiscovery](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.startBluetoothDevicesDiscovery.html)，比较耗费系统资源，务必在不需要搜索后调用 [停止搜索蓝牙设备](#sdk-bluetooth-adapter-stop-search)，如离开页面后）

-  **接口定义**
```typescript
sdk.blueToothAdapter.startSearch({
	 serviceId?: string,
	 serviceIds?: string[],
	 ignoreDeviceIds?: string[],
	 onSearch: (DeviceInfo[]) => void,
 	onError: (Error) => void,
	 timeout: number
}) => Promise<void>
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>serviceId</td>
<td>指定需要搜索的 serviceId，不传的话会使用当前支持的所有 DeviceAdapter 的 serviceId 来匹配</td>
<td>string</td>
<td>否</td>
</tr>
<tr>
<td>serviceIds</td>
<td>参数描述同 serviceId</td>
<td>string[]</td>
<td>否</td>
</tr>
<tr>
<td>ignoreDeviceIds</td>
<td>可选，需要过滤掉的 deviceId 列表（例如刚添加完的设备），搜索结果中将不会出现这些设备</td>
<td>string[]</td>
<td>否</td>
</tr>
<tr>
<td>onSearch</td>
<td>当搜索结果更新后调用，返回搜索到的设备列表</td>
<td>(DeviceInfo[]) =&gt; void</td>
<td>是</td>
</tr>
<tr>
<td>onError</td>
<td>当搜索过程中发生错误后调用，触发后设备搜索将会中止</td>
<td>(Error) =&gt; void</td>
<td>是</td>
</tr>
<tr>
<td>timeout</td>
<td>可选，默认20000，单位毫秒，超过指定时长没有搜索到设备后将会触发超时错误</td>
<td>number</td>
<td>是</td>
</tr>
</tbody></table>
- **返回值**
  返回一个 Promise。

<span id="sdk-bluetooth-adapter-stop-search"></span>

#### 停止搜索蓝牙设备

**接口定义**
```typescript
sdk.blueToothAdapter.stopSearch() => void
```

<span id="sdk-bluetooth-adapter-search-device"></span>

#### 搜索单个蓝牙设备

开始搜索蓝牙设备，并在搜索到第一个满足条件的设备后停止搜索。

- **接口定义**
```typescript
sdk.blueToothAdapter.searchDevice({
	deviceName: string,
	serviceId?: string,
	serviceIds?: string[],
	ignoreDeviceIds?: string[]
}) => Promise<DeviceInfo>
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>deviceName</td>
<td>指定需要搜索的设备 deviceName</td>
<td>string</td>
<td>是</td>
</tr>
<tr>
<td>serviceId</td>
<td>指定需要搜索的 serviceId，不传的话会使用当前支持的所有 DeviceAdapter 的 serviceId 来匹配</td>
<td>string</td>
<td>否</td>
</tr>
<tr>
<td>serviceIds</td>
<td>参数描述同 serviceId</td>
<td>string[]</td>
<td>否</td>
</tr>
<tr>
<td>ignoreDeviceIds</td>
<td>可选，需要过滤掉的 deviceId 列表（例如刚添加完的设备），搜索结果中将不会出现这些设备</td>
<td>string[]</td>
<td>否</td>
</tr>
</tbody></table>
- **返回值**
返回一个 Promise，在找到第一个满足条件的设备后 resolve。

#### 连接蓝牙设备

连接指定蓝牙设备。

- **接口定义**
```typescript
blueToothAdapter.connectDevice(deviceInfo: DeviceInfo, options?: { autoNotify?: boolean }) => Promise<DeviceAdapter>
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>deviceInfo</td>
<td>传入 <a href="#sdk-bluetooth-adapter-start-search">开始搜索蓝牙设备</a> 或 <a href="#sdk-bluetooth-adapter-search-device">搜索单个蓝牙设备</a> 接口搜索出来的 DeviceInfo</td>
<td>DeviceInfo</td>
<td>是</td>
</tr>
<tr>
<td>options.autoNotify</td>
<td>可选，默认为 true。指定为 true 时，在连接设备后，会自动去拉取服务列表，以及主服务下的特征值列表，并会自动订阅第一个 notifyId 或 indicateId 特征值的 notify。若设备含有多个服务或多个 notify 特征值，请传 false，并自行通过 getBLEDeviceServices、getBLEDeviceCharacteristics、notifyBLECharacteristicValueChange等方法获取及订阅特征值。</td>
<td>boolean</td>
<td>否</td>
</tr>
</tbody></table>
- **返回值**
返回一个 Promise，连接成功后返回设备适配器。

#### 获取设备适配器实例

根据 `deviceId` 查询对应的设备适配器实例。

- **接口定义**
```typescript
sdk.blueToothAdapter.getDeviceAdapter(deviceId: string) => DeviceAdapter
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>deviceId</td>
<td>要获取设备适配器实例的 deviceId</td>
<td>string</td>
<td>是</td>
</tr>
</tbody></table>
- **返回值**
返回对应 `deviceId` 的设备适配器实例。

#### 监听事件
监听蓝牙适配器事件。

- **接口定义**
```typescript
sdk.blueToothAdapter.on(type: string, listener: (...args) => void) => void
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>type</td>
<td>要监听的事件</td>
<td>string</td>
<td>是</td>
</tr>
<tr>
<td>listener</td>
<td>事件触发时的回调函数</td>
<td>(...args) =&gt; void</td>
<td>是</td>
</tr>
</tbody></table>

#### 取消监听事件
取消监听蓝牙适配器事件。

- **接口定义**
```typescript
sdk.blueToothAdapter.off(type: string, listener: (...args) => void) => void
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>type</td>
<td>要取消监听的事件</td>
<td>string</td>
<td>是</td>
</tr>
<tr>
<td>listener</td>
<td>要取消监听的事件的回调函数，不传则清除该事件的所有回调函数</td>
<td>(...args) =&gt; void</td>
<td>否</td>
</tr>
</tbody></table>

#### 蓝牙适配器事件

**adapterStateChange 事件**：当适配器状态变化时触发。
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
</tr>
</thead>
<tbody><tr>
<td>available</td>
<td>蓝牙适配器是否可用</td>
<td>boolean</td>
</tr>
<tr>
<td>discovering</td>
<td>蓝牙适配器是否处于搜索状态</td>
<td>boolean</td>
</tr>
</tbody></table>

### 设备适配器

#### 自定义设备适配器
自定义设备适配器类需要继承 `DeviceAdapter`，并补充以下实现。

- **serviceId**：自定义设备适配器类需要设置该属性，代表该设备的主服务 ID。
- **deviceFilter**：自定义设备适配器类需要实现该静态方法，在搜索蓝牙设备时会将每个搜出的设备信息传入该方法，如果判断是本产品的设备，则需在除入参 deviceInfo 之外返回设备唯一标识 deviceName 及 serviceId，否则返回空。
```typescript
DeviceAdapter.deviceFilter: (deviceInfo: DeviceInfo) => { 
	deviceName: string, 
	serviceId: string,
	...deviceInfo
}
```
- **handleBLEMessage**：自定义设备适配器类需要实现该方法，用于处理收到 `onBLECharacteristicValueChange` 回调后的协议解析。
```typescript
DeviceAdapter.handleBLEMessage: (hexString, { serviceId, characteristicId }) => {
	reportData?: any,
	...any
}
```

返回值中如果返回 `reportData`，则会将该部分数据上报到云端（注意需与产品定义物模型匹配），其他字段则会透传到 `message` 事件的 payload 中。

#### 设备适配器属性
<table>
<thead>
<tr>
<th>属性名</th>
<th>属性描述</th>
<th>类型</th>
</tr>
</thead>
<tbody><tr>
<td>explorerDeviceId</td>
<td>只读，设备的 explorerDeviceId</td>
<td>string</td>
</tr>
<tr>
<td>isConnected</td>
<td>只读，设备当前是否连接状态</td>
<td>boolean</td>
</tr>
<tr>
<td>deviceId</td>
<td>只读，设备的 deviceId</td>
<td>string</td>
</tr>
<tr>
<td>serviceId</td>
<td>只读，设备的主服务 ID，实际上既是挂在构造函数上的静态属性 DeviceAdapter.serviceId</td>
<td>string</td>
</tr>
<tr>
<td>originName</td>
<td>只读，设备的原始名称，即小程序接口搜索出来时的 name 字段</td>
<td>string</td>
</tr>
<tr>
<td>explorerDeviceId</td>
<td>只读，设备的 explorerDeviceId</td>
<td>string</td>
</tr>
</tbody></table>

#### 断开设备连接
**接口定义**
```typescript
deviceAdapter.disconnectDevice() => void
```

#### 获取设备服务列表

- **接口定义**
```typescript
deviceAdapter.getBLEDeviceServices() => Promise<ServiceList>
```
- **返回值**
返回一个 Promise，`ServiceList` 数据结构请参见 [wx.getBLEDeviceServices](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.getBLEDeviceServices.html)。

#### 获取设备指定服务的特征值列表
获取设备指定服务中的特征值列表，并将特征值存放在 `deviceAdapter` 实例上。
- **接口定义**
```typescript
deviceAdapter.getBLEDeviceCharacteristics({ serviceId: string }) => Promise<CharacteristicsList>
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>serviceId</td>
<td>可选，指定要获取特征值列表的服务 ID，默认为主服务 ID</td>
<td>string</td>
<td>否</td>
</tr>
</tbody></table>
- **返回值**
返回一个 Promise，`CharacteristicsList` 数据结构请参见 [wx.getBLEDeviceCharacteristics](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.getBLEDeviceCharacteristics.html)。
- **说明**
将获取到的特征值按照如下数据结构存放在 `deviceAdapter` 实例上。
```typescript
deviceAdapter.characteristicsMap[serviceId] = {
	notifyIds: string[],
	indicateIds: string[],
	writeIds: string[],
	readIds: string[]
}
```

#### 读取指定特征值的二进制数据

- **接口定义**
```typescript
deviceAdapter.readBLECharacteristicValue({
	serviceId?: string,
	characteristicId: string
}) => Promise<void>
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>serviceId</td>
<td>可选，默认为主服务 ID</td>
<td>string</td>
<td>否</td>
</tr>
<tr>
<td>characteristicId</td>
<td>需要读取的特征值 ID，默认会取主服务下的第一个 read 特征值</td>
<td>string</td>
<td>是</td>
</tr>
</tbody></table>
- **返回值**
返回一个 Promise。接口读取到的信息需要在 `onBLECharacteristicValueChange` 方法注册的回调中获取，具体参见 [wx.readBLECharacteristicValue](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.readBLECharacteristicValue.html)。

#### 获取蓝牙设备信号强度

- **接口定义**
```typescript
deviceAdapter.getBLEDeviceRSSI() => Promise
```
- **返回值**
返回一个 Promise，具体数据结构请参见 [wx.getBLEDeviceRSSI](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.getBLEDeviceRSSI.html)。

#### 启用特征值变化时的 notify 功能

- **接口定义**
```typescript
deviceAdapter.notifyBLECharacteristicValueChange({
	characteristicId?: string,
	serviceId?: string,
	state?: boolean
}) => Promise<void>
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>serviceId</td>
<td>需要订阅的服务 ID，默认会取主服务 ID</td>
<td>string</td>
<td>否</td>
</tr>
<tr>
<td>characteristicId</td>
<td>需要订阅的特征值 ID，默认会取主服务下的第一个 notify 或 indicate 特征值</td>
<td>string</td>
<td>否</td>
</tr>
<tr>
<td>state</td>
<td>是否启用 notify，默认为 true</td>
<td>boolean</td>
<td>否</td>
</tr>
</tbody></table>
- **返回值**
返回一个 Promise。

#### 写入二进制数据到指定特征值中

- **接口定义**
```typescript
deviceAdapter.write(hexString: string, options?: {
	writeId?: string,
	serviceId?: string
}) => Promise
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>hexString</td>
<td>需要写给蓝牙设备的十六进制字符串</td>
<td>string</td>
<td>是</td>
</tr>
<tr>
<td>options.writeId</td>
<td>可选，需要写入的特征值 ID，默认会取主服务下的第一个 writeId</td>
<td>string</td>
<td>否</td>
</tr>
<tr>
<td>options.serviceId</td>
<td>可选，需要写入的服务 ID，默认会取主服务 ID</td>
<td>string</td>
<td>否</td>
</tr>
</tbody></table>

#### 监听事件

监听设备适配器事件。

- **接口定义**
```typescript
deviceAdapter.on(type: string, listener: (...args) => void) => void
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>type</td>
<td>要监听的事件</td>
<td>string</td>
<td>是</td>
</tr>
<tr>
<td>listener</td>
<td>事件触发时的回调函数</td>
<td>(...args) =&gt; void</td>
<td>是</td>
</tr>
</tbody></table>

#### 取消监听事件
取消监听设备适配器事件。

- **接口定义**
```typescript
deviceAdapter.off(type: string, listener: (...args) => void) => void
```
- **参数说明**
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
<th>必填</th>
</tr>
</thead>
<tbody><tr>
<td>type</td>
<td>要取消监听的事件</td>
<td>string</td>
<td>是</td>
</tr>
<tr>
<td>listener</td>
<td>要取消监听的事件的回调函数，不传则清除该事件的所有回调函数</td>
<td>(...args) =&gt; void</td>
<td>否</td>
</tr>
</tbody></table>

#### 设备适配器事件
- **connect 事件**：设备连接后触发。
- **disconnect 事件**：设备断开后触发。
- **message 事件**：当收到 `onBLECharacteristicValueChange` 回调，并经过 `handleBLEMessage` 处理后触发。
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
</tr>
</thead>
<tbody><tr>
<td>timestamp</td>
<td>收到设备消息的时间戳，单位毫秒</td>
<td>number</td>
</tr>
<tr>
<td>dataReported</td>
<td>收到设备的消息是否已上报云端</td>
<td>boolean</td>
</tr>
<tr>
<td>（其他）</td>
<td>handleBLEMessage 函数返回的其他参数将会透传到 message 事件中</td>
<td>any</td>
</tr>
</tbody></table>
- **bLEConnectionStateChange 事件**：当 `onBleConnectionStateChange` 触发时触发，若 `connected` 为 true，则接下来会触发 `connect` 事件，否则会触发 `disconnect` 事件。
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数描述</th>
<th>类型</th>
</tr>
</thead>
<tbody><tr>
<td>connected</td>
<td>设备是否连接</td>
<td>boolean</td>
</tr>
</tbody></table>


## ASR 语音识别

### 语音识别

目前支持两种场景，分别为“录音文件”与“一句话识别”，两种场景下入参会有所不同。
由于识别过程是异步，因此接口“voiceRecognition”并不会立即返回识别结果，可以理解为该接口是创建了一个“异步任务”，当这个成功被创建的“异步任务”执行完后，会通过 websocket 将结果推送到所有订阅该 deviceId 的终端上，下文为您详细介绍 ASR 语音识别。

#### voiceRecognition

#### 接口定义

```typescript
sdk.voiceRecognition({...}) => Promise<{...}>
```

#### 参数说明

- 关于“录音文件”场景支持的音频类型、大小限制以及相关字段的详细介绍，详情请参见 [ 录音文件识别](https://cloud.tencent.com/document/api/1093/37823)。
- 关于“一句话识别”场景支持的音频类型、大小限制以及相关字段的详细介绍，详情请参见 [一句话识别](https://cloud.tencent.com/document/api/1093/35646)。

#### 公共参数

| 参数名   | 参数描述             | 类型            | 必填 |
| -------- | -------------------- | --------------- | ---- |
| DeviceId | 默认使用当前设备的设备 ID  | string      | 否   |
| AudioType | 识别场景。<br><li>“录音文件”取值“file”<br><li>“一句话识别”取值“sentence” | string   | 是  |
| Data | 音频文件 | Blob \| File | 是  |
| ResourceName | 文件名称，如果 Data 类型是 File，则取其“name”作为默认值 | string | 否  |
| EngineType | 引擎模型类型，默认值为“16k_zh” | string | 否  |
| FilterDirty | 是否过滤脏词 | number | 否   |
| FilterModal | 是否过滤语气词 | number | 否  |
| FilterPunc | 是否过滤标点符号 | number | 否  |
| ConvertNumMode | 是否进行阿拉伯数字智能转换 | number | 否 |

#### 录音文件额外参数

| 参数名   | 参数描述             | 类型            | 必填 |
| -------- | -------------------- | --------------- | ---- |
| ChannelNum | 语音声道数，默认为1        | number      | 否   |
| SpeakerDiarization | 是否开启话者分离| number   | 否  |
| SpeakerNumber | 话者分离人数 | number | 否  |

#### 返回值说明

| 参数名   | 参数描述             | 类型            |
| -------- | -------------------- | --------------- |
| ResourceToken | 某个设备下，音频文件的唯一标示        | string      |

#### 监听识别结果 - asrResponse

对于“录音文件”场景，如果音频文件过大，后台可能会对音频文件进行分片识别，每个分片识别完成后，都将推送一条 websocket 消息，但推送的消息不保证顺序（例如有可能分片2的结果先到达）。

对于“asrResponse”事件，实际是基于“wsControl”事件进行二次封装；当然，您也可以通过监听“wsControl”事件获取识别结果。

#### 接口定义
```
sdk.on('asrResponse', ({ deviceId, data }) => void)
```

#### 返回值说明
| 参数名                 | 参数描述            | 类型     |
|:--------------------|:----------------|:-------|
| deviceId            | 设备 ID            | string |
| data                |  识别结果数据               | object |
| data.resource_token | 某个设备下，音频文件的唯一标示 | string |
| data.result_code    | 状态码，0代表成功      | number |
| data.total_num   | 分片总数   | number |
| data.seq | 当前分片序号 | number | 
| data.res_text | 当前分片识别结果，对于“录音文件”场景，识别结果会包含分段时间戳 | string |


### 获取语音文件下载链接（仅限“录音文件”场景）

#### 接口定义

```typescript
sdk.getAsrDownloadUrl({...}) => Promise<{...}>
```

#### 参数说明

| 参数名                 | 参数描述            | 类型     | 必填   |
|:--------------------|:----------------|:-------|:-----|
| DeviceId            | 设备 ID            | string | 是 |
| ResourceToken       | 调用 voiceRecognition 返回的 ResourceToken    | string | 是 |

#### 返回值说明

| 参数名                 | 参数描述            | 类型     |
|:--------------------|:----------------|:-------|
| ResourceURL       | cos 访问链接            | string |

## 音乐服务

### 公共说明

#### 获取实例

```typescript
let tmeSdk = await sdk.getTMESdk();
```



#### 接口通用返回

**接口统一返回值**

TMESDK接口调用的返回值统一为 `Promise<TMEResponse>` 结构。

```typescript
interface TMEResponse {
  error_code: number,
  error_msg: string,
  data?: any;
}
```

- 调用成功：返回一个 resolved 的 Promise，其值为 TMEResponse 结构，error_code=0，data 为返回结果。
- 调用失败：返回一个 rejected 的 Promise，有响应的错误码（error_code）及提示信息（error_msg）。

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

跳转酷狗音乐小程序授权，当再次返回 h5 时，Promise 状态改变。

**接口定义**

```typescript
tmeSdk.login() => Promise
```

**返回值**

返回一个`Promise<TMEResponse>`



#### 用户设备登出

原 token 将登出

**接口定义**

```typescript
tmeSdk.getUserInfo() => Promise<TMEResponse>
```

**返回值**

返回一个`Promise<TMEResponse>`



#### 校验设备授权

**接口定义**

```typescript
tmeSdk.checkDeviceAuth() => Promise<TMEResponse>
```

**返回值**

返回一个`Promise<TMEResponse>`



#### 获取用户信息

**接口定义**

```typescript
tmeSdk.getUserInfo() => Promise<TMEResponse>
```

**返回值**

返回一个`Promise<TMEResponse>`，其中data如下：

| 属性名           | 描述                   | 类型           |
| ---------------- | ---------------------- | -------------- |
| userid           | 用户id                 | string         |
| nick_name        | 用户昵称               | string         |
| img              | 用户头像               | string         |
| is_vip           | 是否vip 0:否 1:是      | enum:  `0` `1` |
| vip_end_time     | vip有效期终止时间      | string         |
| car_vip_end_time | 车机会员有效期终止时间 | string         |
| svip_end_time    | 豪V有效期终止时间      | string         |



### 播控部分

#### 接口描述

调用播控 SDK，会下发物模型属性+control_seq，需要设备上报相同的 control_seq。

- 若在超时范围内收到上报，视为下发播控成功，返回resolved状态的`Promise<TMEResponse>`

- 若超时未收到上报，返回rejected状态的`Promise<TMEResponse>`

超时设置可以通过 `tmeSdk.config.timeout` 来配置，默认值为10000，单位：毫秒(ms)。



####  通用播控接口

**接口定义**

```typescript
tmeSdk.controlKugouDeviceData(deviceData) => Promise<TMEResponse>
```

**参数说明**

| 参数名     | 参数描述       | 类型   | 必填 |
| ---------- | -------------- | ------ | ---- |
| deviceData | 设备物模型数据 | object | 是   |

**返回值**

返回一个`Promise<TMEResponse>`



#### 播放

**接口定义**

```typescript
tmeSdk.play() => Promise<TMEResponse>
```

**返回值**

返回一个`Promise<TMEResponse>`



#### 音乐

**接口定义**

```typescript
tmeSdk.pause() => Promise<TMEResponse>
```

**返回值**

返回一个`Promise<TMEResponse>`



#### 上一首

**接口定义**

```typescript
tmeSdk.preSong() => Promise<TMEResponse>
```

**返回值**

返回一个`Promise<TMEResponse>`



#### 下一首

**接口定义**

```typescript
tmeSdk.nextSong() => Promise<TMEResponse>
```

**返回值**

返回一个`Promise<TMEResponse>`



#### 设置播放模式

**接口定义**

```typescript
tmeSdk.setPlayMode(play_mode: number) => Promise<TMEResponse>
```

**参数说明**

| 参数名    | 参数描述                                   | 类型              | 必填 |
| --------- | ------------------------------------------ | ----------------- | ---- |
| play_mode | 播放模式：0:顺序播放 1:单曲循环 2:随机播放 | enum: `0` `1` `2` | 是   |

**返回值**

返回一个`Promise<TMEResponse>`



#### 设置音量

**接口定义**

```typescript
tmeSdk.setVolume(volume: number) => Promise<TMEResponse>
```

**参数说明**

| 参数名 | 参数描述        | 类型   | 必填 |
| ------ | --------------- | ------ | ---- |
| volume | 音量：0-100之间 | number | 是   |

**返回值**

返回一个`Promise<TMEResponse>`



#### 设置播放进度

**接口定义**

```typescript
tmeSdk.setPlayPosition(play_position: number) => Promise<TMEResponse>
```

**参数说明**

| 参数名        | 参数描述             | 类型   | 必填 |
| ------------- | -------------------- | ------ | ---- |
| play_position | 播放进度：单位:秒(s) | number | 是   |

**返回值**

返回一个`Promise<TMEResponse>`



#### 设置播放质量

**接口定义**

```typescript
tmeSdk.setPlayQuality(recommend_quality: number) => Promise<TMEResponse>
```

**参数说明**

| 参数名            | 参数描述                       | 类型              | 必填 |
| ----------------- | ------------------------------ | ----------------- | ---- |
| recommend_quality | 播放质量：0:标准 1:高清 2:无损 | enum: `0` `1` `2` | 是   |

**返回值**

返回一个`Promise<TMEResponse>`



#### 设置当前播放歌曲

设置当前播放的歌曲

| 参数名       | 参数描述                                                 | 类型             | 必填 |
| ------------ | -------------------------------------------------------- | ---------------- | ---- |
| songId       | 歌曲ID                                                   | string           | 是   |
| songIndex    | 歌曲所在播放列表的位置，从0开始                          | number           | 是   |
| newQueueType | 播放列表的类型： `playlist` `newSongs` `recommendDailty` | string           | 是   |
| newQueueId   | 播放列表ID（当类型为"每日推荐"时，不填）                 | string \| number | 否   |

播放列表目前支持三种类型：歌单(playlist)、新歌首发(newSongs)、每日推荐(recommendDaily)

**返回值**

返回一个`Promise<TMEResponse>`



### 内容部分

#### 拉取内容通用接口

请求酷狗API拉取内容通用接口

**接口定义**

```typescript
tmeSdk.requestTMEApi(action: string, params) => Promise<TMEResponse>
```

**参数说明**

| 参数名 | 描述     | 类型   | 必填 |
| ------ | -------- | ------ | ---- |
| action | 请求行为 | string | 是   |
| params | 请求参数 | object | 否   |

**返回值**

返回一个`Promise<TMEResponse>`

注：action、params 及 返回值 data 参考 [音乐服务](https://cloud.tencent.com/document/product/1081/60545)



#### 获取设备当前播放歌曲

**接口定义**

```typescript
tmeSdk.getCurrentPlaySong() => Promise<TMEResponse>
```

**返回值**

返回一个`Promise<TMEResponse>`，data 为歌曲信息



#### 获取设备当前播放列表

根据目前支持的播放类型(playType)，拉取对应的歌单列表，并查出歌曲的详细信息

**接口定义**

```typescript
tmeSdk.getCurrentPlayQueue() => Promise<TMEResponse>
```

**返回值**

返回一个`Promise<TMEResponse>`

TMEResponse中data如下

| 属性名   | 描述                                                         | 类型                                         |
| -------- | ------------------------------------------------------------ | -------------------------------------------- |
| playType | 播放列表类型                                                 | enum: `playlist` `newSongs` `recommendDaily` |
| queueId  | 当前播放列表id，根据playType对应playlist_id、album_id、top_id | string \| number                             |
| total    | 列表中歌曲总数                                               | number                                       |
| songs    | 歌曲数组，具体歌曲属性参考TME文档中Song属性                  | Array[]                                      |



#### 获取歌曲详细信息

**接口定义**

```typescript
tmeSdk.getSongDetail() => Promise<TMEResponse>
```

通过调用 requestTMEApi，请求歌曲播放链接与歌曲信息，返回歌曲的详细信息

**参数说明**

| 参数名  | 描述   | 类型   | 必填 |
| ------- | ------ | ------ | ---- |
| song_id | 歌曲 ID | string | 是   |

**返回值**

返回一个`Promise<TMEResponse>`，data 为歌曲信息



#### 获取歌单详细信息

**接口定义**

```typescript
tmeSdk.getPlaylistDetail() => Promise<TMEResponse>
```

通过调用 requestTMEApi，请求歌单列表与歌曲信息，丰富列表中的歌曲信息，返回歌单列表

**参数说明**

| 参数名 | 描述                                                         | 类型   | 必填 |
| ------ | ------------------------------------------------------------ | ------ | ---- |
| action | 新歌首发(awesome_newsong)、每日推荐(awesome_everyday)、歌单歌曲(playlist_song) | string | 是   |
| params | 参考应用端 API=>音乐服务中对应 API 的 KugouParams                | object | 是   |

**返回值**

返回一个`Promise<TMEResponse>`，data 为歌单列表

注：action、params 及返回值 data 参考 [音乐服务](https://cloud.tencent.com/document/product/1081/60545)



## 底层 SDK 能力

### 应用开发 SDK
H5 SDK 底层依赖应用开发小程序端 SDK。通过以下代码可以获取应用开发 SDK 的实例，更多调用能力请参见 [应用开发小程序端 SDK](https://github.com/tencentyun/qcloud-iotexplorer-appdev-miniprogram-sdk#readme) 文档。

**接口定义**
```typescript
sdk.appDevSdk
```

### 微信 JS SDK
通过以下代码可以获取微信 JSSDK 实例，具体用法请参见 [小程序 web-view 文档](https://developers.weixin.qq.com/miniprogram/dev/component/web-view.html)。使用前需要先调用 [初始化 JSSDK](#sdk-wx-sdk-ready)。

**接口定义**
```typescript
sdk.wx
```


<span id="sdk-wx-sdk-ready"></span>

### 初始化 JS SDK

- **接口定义**
```typescript
sdk.wxSdkReady() => Promise
```
- **返回值**
返回一个带缓存的 Promise，初始化成功后 resolve。若初始化未完成或已初始化成功，则多次调用后返回同一个 Promise。若初始化失败，则该缓存的 Promise 在 reject 之后会被释放，再次调用则将重新初始化。
- **示例代码**
```javascript
sdk.wxSdkReady().then(() => wx.miniProgram.navigateBack());
```
