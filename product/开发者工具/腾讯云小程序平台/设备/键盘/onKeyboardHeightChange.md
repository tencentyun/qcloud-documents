# onKeyboardHeightChange(function listener)

## 功能描述

监听键盘高度变化事件

## 参数

### function listener

键盘高度变化事件的监听函数

#### 参数

##### Object res

| 属性   | 类型   | 说明     |
| :----- | :----- | :------- |
| height | number | 键盘高度 |

## 示例代码

```js
wx.onKeyboardHeightChange(res => {
  console.log(res.height)
})
```