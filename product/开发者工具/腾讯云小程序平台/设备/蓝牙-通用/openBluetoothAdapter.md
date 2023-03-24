# wx.openBluetoothAdapter(Object object)

> 支持度：
>
> Android：支持
>
> iOS：支持

## 功能描述

初始化蓝牙模块。iOS 上开启主机/从机（外围设备）模式时需分别调用一次，并指定对应的 `mode`。

## 参数

### Object object

| 属性     | 类型     | 合法值及说明                                          | 默认值  | 必填 | 说明                                             | 最低版本                                                     |
| :------- | :------- | ----------------------------------------------------- | :------ | :--- | :----------------------------------------------- | :----------------------------------------------------------- |
| mode     | string   | central：主机模式<br>peripheral：从机（外围设备）模式 | central | 否   | 蓝牙模式，可作为主/从设备，仅 iOS 需要。         |    |
| success  | function |                                                       |         | 否   | 接口调用成功的回调函数                           |                                                              |
| fail     | function |                                                       |         | 否   | 接口调用失败的回调函数                           |                                                              |
| complete | function |                                                       |         | 否   | 接口调用结束的回调函数（调用成功、失败都会执行） |                                                              |

## 错误

| 错误码 | 错误信息             | 说明                                          |
| :----- | :------------------- | :-------------------------------------------- |
| 0      | ok                   | 正常                                          |
| -1     | already connect      | 已连接                                        |
| 10000  | not init             | 未初始化蓝牙适配器                            |
| 10001  | not available        | 当前蓝牙适配器不可用                          |
| 10002  | no device            | 没有找到指定设备                              |
| 10003  | connection fail      | 连接失败                                      |
| 10004  | no service           | 没有找到指定服务                              |
| 10005  | no characteristic    | 没有找到指定特征                              |
| 10006  | no connection        | 当前连接已断开                                |
| 10007  | property not support | 当前特征不支持此操作                          |
| 10008  | system error         | 其余所有系统上报的异常                        |
| 10009  | system not support   | Android 系统特有，系统版本低于 4.3 不支持 BLE |
| 10012  | operate time out     | 连接超时                                      |
| 10013  | invalid_data         | 连接 deviceId 为空或者是格式不正确            |

## object.fail 回调函数返回的 state 参数（仅 iOS）

| 状态码 | 说明   |
| :----- | :----- |
| 0      | 未知   |
| 1      | 重置中 |
| 2      | 不支持 |
| 3      | 未授权 |
| 4      | 未开启 |

## 注意

- 其他蓝牙相关 API 必须在 [wx.openBluetoothAdapter](./openBluetoothAdapter.md) 调用之后使用。否则 API 会返回错误（errCode=10000）。
- 在用户蓝牙开关未开启或者手机不支持蓝牙功能的情况下，调用 [wx.openBluetoothAdapter](/openBluetoothAdapter.md) 会返回错误（errCode=10001），表示手机蓝牙功能不可用。
  <!-- 此时小程序蓝牙模块已经初始化完成，可通过 [wx.onBluetoothAdapterStateChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.onBluetoothAdapterStateChange.html) 监听手机蓝牙状态的改变，也可以调用蓝牙模块的所有API。 -->

## 示例代码

```js
wx.openBluetoothAdapter({
  success (res) {
    console.log(res)
  }
})
```