# wx.canIUse(string schema)

判断小程序的API，回调，参数，组件等是否在当前版本可用。

#### 参数

##### string schema

使用 `${API}.${method}.${param}.${options}` 或者 `${component}.${attribute}.${option}` 方式来调用

#### 返回值

##### boolean

当前版本是否可用

#### 参数说明

* `${API}` 代表 API 名字
* `${method}` 代表调用方式，有效值为return, success, object, callback
* `${param}` 代表参数或者返回值
* `${options}` 代表参数的可选值
* `${component}` 代表组件名字
* `${attribute}` 代表组件属性
* `${option}` 代表组件属性的可选值

#### 示例代码

```js
wx.canIUse('openBluetoothAdapter')
wx.canIUse('getSystemInfoSync.return.screenWidth')
wx.canIUse('getSystemInfo.success.screenWidth')
wx.canIUse('showToast.object.image')
wx.canIUse('onCompassChange.callback.direction')
wx.canIUse('request.object.method.GET')

wx.canIUse('live-player')
wx.canIUse('text.selectable')
wx.canIUse('button.open-type.contact')
```