# wx.getSelectedTextRange(Object object)

## 功能描述

在input、textarea等 focus 之后，获取输入框的光标位置。注意：只有在 focus 的时候调用此接口才有效。

## 参数

### Object object

| 属性     | 类型     | 默认值 | 必填 | 说明                                             |
| :------- | :------- | :----- | :--- | :----------------------------------------------- |
| success  | function |        | 否   | 接口调用成功的回调函数                           |
| fail     | function |        | 否   | 接口调用失败的回调函数                           |
| complete | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### object.success 回调函数

##### 参数

###### Object res

| 属性  | 类型   | 说明               |
| :---- | :----- | :----------------- |
| start | number | 输入框光标起始位置 |
| end   | number | 输入框光标结束位置 |

## 示例代码

```js
wx.getSelectedTextRange({
  complete: res => {
    console.log('getSelectedTextRange res', res.start, res.end)
  }
})
```