# wx.getConnectedBluetoothDevices(Object object)

## 功能描述

根据主服务 UUID 获取已连接的蓝牙设备。

## 参数

### Object object

| 属性     | 类型           | 默认值 | 必填 | 说明                                                 |
| :------- | :------------- | :----- | :--- | :--------------------------------------------------- |
| services | Array.&lt;string&gt; |        | 是   | 蓝牙设备主服务的 UUID 列表（支持 16/32/128 位 UUID） |
| success  | function       |        | 否   | 接口调用成功的回调函数                               |
| fail     | function       |        | 否   | 接口调用失败的回调函数                               |
| complete | function       |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行）     |

#### object.success 回调函数

##### 参数

###### Object res

| 属性    | 类型           | 说明             |
| :------ | :------------- | :--------------- |
| devices | Array.&lt;Object&gt; | 搜索到的设备列表 |

| 结构属性 | 类型   | 说明                           |
| :------- | :----- | ------------------------------ |
| name     | string | 蓝牙设备名称，某些设备可能没有 |
| deviceId | string | 用于区分设备的 id              |

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

## 示例代码

```js
wx.getConnectedBluetoothDevices({
  services: ['FEE7'],
  success (res) {
    console.log(res)
  }
})
```