# wx.offKeyboardHeightChange(function listener)

## 功能描述

移除键盘高度变化事件的监听函数

## 参数

### function listener

onKeyboardHeightChange 传入的监听函数。不传此参数则移除所有监听函数。

## 示例代码

```js
const listener = function (res) { console.log(res) }

wx.onKeyboardHeightChange(listener)
wx.offKeyboardHeightChange(listener) // 需传入与监听时同一个的函数对象
```