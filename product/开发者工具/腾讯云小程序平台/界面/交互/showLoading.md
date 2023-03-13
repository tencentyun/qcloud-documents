# showLoading

- 功能描述

显示 loading 提示框。需主动调用 wx.hideLoading 才能关闭提示框

- 参数

**Object object**

| 属性     | 类型     | 默认值 | 必填 | 说明                                             |
| :------- | :------- | :----- | :--- | :----------------------------------------------- |
| title    | string   |        | 是   | 提示的内容                                       |
| mask     | boolean  | false  | 否   | 是否显示透明蒙层，防止触摸穿透                   |
| success  | function |        | 否   | 接口调用成功的回调函数                           |
| fail     | function |        | 否   | 接口调用失败的回调函数                           |
| complete | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行） |

- 示例代码

```js
wx.showLoading({
  title: '加载中',
})

setTimeout(function () {
  wx.hideLoading()
}, 2000)
```

- 注意
  - [wx.showLoading](./showLoading.md) 和 [wx.showToast](./showToast.md) 同时只能显示一个
  - [wx.showLoading](./showLoading.md) 应与 [wx.hideLoading](./hideLoading.md) 配对使用