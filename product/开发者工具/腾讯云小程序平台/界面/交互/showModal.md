# showModal

- 功能描述

显示模态对话框

- 参数

**Object object**

| 属性            | 类型     | 默认值  | 必填 | 说明                                               | 最低版本                                                     |
| :-------------- | :------- | :------ | :--- | :------------------------------------------------- | :----------------------------------------------------------- |
| title           | string   |         | 否   | 提示的标题                                         |                                                              |
| content         | string   |         | 否   | 提示的内容                                         |                                                              |
| showCancel      | boolean  | true    | 否   | 是否显示取消按钮                                   |                                                              |
| cancelText      | string   | 取消    | 否   | 取消按钮的文字，最多 4 个字符                      |                                                              |
| cancelColor     | string   | #000000 | 否   | 取消按钮的文字颜色，必须是 16 进制格式的颜色字符串 |                                                              |
| confirmText     | string   | 确定    | 否   | 确认按钮的文字，最多 4 个字符                      |                                                              |
| confirmColor    | string   | #576B95 | 否   | 确认按钮的文字颜色，必须是 16 进制格式的颜色字符串 |                                                              |
| success         | function |         | 否   | 接口调用成功的回调函数                             |                                                              |
| fail            | function |         | 否   | 接口调用失败的回调函数                             |                                                              |
| complete        | function |         | 否   | 接口调用结束的回调函数（调用成功、失败都会执行）   |                                                              |

**object.success 回调函数**

- 参数

**Object res**

| 属性    | 类型    | 说明                                                         | 最低版本                                                     |
| :------ | :------ | :----------------------------------------------------------- | :----------------------------------------------------------- |
| confirm | boolean | 为 true 时，表示用户点击了确定按钮                           |                                                              |
| cancel  | boolean | 为 true 时，表示用户点击了取消（用于 Android 系统区分点击蒙层关闭还是点击取消按钮关闭） |    |

- 示例代码

```js
wx.showModal({
  title: '提示',
  content: '这是一个模态弹窗',
  success (res) {
    if (res.confirm) {
      console.log('用户点击确定')
    } else if (res.cancel) {
      console.log('用户点击取消')
    }
  }
})
```

- 注意

  - Android 6.7.2 以下版本，点击取消或蒙层时，回调 fail, errMsg 为 "fail cancel"；

  - Android 6.7.2 及以上版本 和 iOS 点击蒙层不会关闭模态弹窗，所以尽量避免使用「取消」分支中实现业务逻辑