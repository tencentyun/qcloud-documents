# setBackgroundColor

- 功能描述

动态设置窗口的背景色

- 参数

**Object object**

| 属性                  | 类型     | 默认值 | 必填 | 说明                                                |
| :-------------------- | :------- | :----- | :--- | :-------------------------------------------------- |
| backgroundColor       | string   |        | 否   | 窗口的背景色，必须为十六进制颜色值                  |
| backgroundColorTop    | string   |        | 否   | 顶部窗口的背景色，必须为十六进制颜色值，仅 iOS 支持 |
| backgroundColorBottom | string   |        | 否   | 底部窗口的背景色，必须为十六进制颜色值，仅 iOS 支持 |
| success               | function |        | 否   | 接口调用成功的回调函数                              |
| fail                  | function |        | 否   | 接口调用失败的回调函数                              |
| complete              | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行）    |

- 示例代码

```js
wx.setBackgroundColor({
  backgroundColor: '#ffffff', // 窗口的背景色为白色
})

wx.setBackgroundColor({
  backgroundColorTop: '#ffffff', // 顶部窗口的背景色为白色
  backgroundColorBottom: '#ffffff', // 底部窗口的背景色为白色
})
```