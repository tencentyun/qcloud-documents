# startSoterAuthentication
## 功能描述

开始生物认证。

## 参数

### Object object

| 属性             | 类型           | 默认值 | 必填 | 说明                                                         |
| :--------------- | :------------- | :----- | :--- | :----------------------------------------------------------- |
| authContent      | string         | ''     | 否   | 验证描述，即识别过程中显示在界面上的对话框提示内容           |
| success          | function       |        | 否   | 接口调用成功的回调函数                                       |
| fail             | function       |        | 否   | 接口调用失败的回调函数                                       |
| complete         | function       |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行）             |

## 示例代码

```js
wx.startSoterAuthentication({
   authContent: '生物认证解锁',
   success() {
     // 认证成功
   }
})
```