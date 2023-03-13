# wx.offCompassChange(function listener)

## 功能描述

移除罗盘数据变化事件的监听函数

## 参数

### function listener

onCompassChange 传入的监听函数。不传此参数则移除所有监听函数。

## 示例代码

```js
const listener = function (res) { console.log(res) }

wx.onCompassChange(listener)
wx.offCompassChange(listener) // 需传入与监听时同一个的函数对象
```