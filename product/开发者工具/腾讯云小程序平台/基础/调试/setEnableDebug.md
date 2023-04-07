# setEnableDebug

- 功能描述

设置是否打开调试开关。此开关对正式版也能生效。

- 参数

**Object object**

| 属性        | 类型     | 默认值 | 必填 | 说明                                             |
| :---------- | :------- | :----- | :--- | :----------------------------------------------- |
| enableDebug | boolean  |        | 是   | 是否打开调试                                     |
| success     | function |        | 否   | 接口调用成功的回调函数                           |
| fail        | function |        | 否   | 接口调用失败的回调函数                           |
| complete    | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行） |

- 示例代码

```javascript
// 打开调试
wx.setEnableDebug({
  enableDebug: true
})

// 关闭调试
wx.setEnableDebug({
  enableDebug: false
})
```

- Tips

在正式版打开调试还有一种方法，就是先在开发版或体验版打开调试，再切到正式版就能看到vConsole。