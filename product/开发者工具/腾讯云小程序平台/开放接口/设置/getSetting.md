# wx.getSetting

### wx.getSetting(Object object)

获取用户的当前设置。

#### 参数

##### Object object

 属性              | 类型     | 默认值 | 必填 | 说明                                                         
 ----------------- | -------- | ------ | ---- | ------------------------------------------------------------ 
 withSubscriptions | Boolean  | false  | 否   | 是否同时获取用户订阅消息的订阅状态，默认不获取。注意：withSubscriptions 只返回用户勾选过订阅面板中的“总是保持以上选择，不再询问”的订阅消息。 
 success           | function |        | 否   | 接口调用成功的回调函数                                       
 fail              | function |        | 否   | 接口调用失败的回调函数                                       
 complete          | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行）             

###### object.success 回调函数

**参数**

**Object res**

 属性                 | 类型                                                         | 说明                                                         
 -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ 
 authSetting          | [AuthSetting](./AuthSetting.md) | 用户授权结果                                                 
#### 示例代码

```js
wx.getSetting({
  success(res) {
    console.log(res.authSetting)
    // res.authSetting = {
    //   "scope.userInfo": true,
    //   "scope.userLocation": true
    // }
  }
})
```
```javascript
wx.getSetting({
  withSubscriptions: true,
  success (res) {
    console.log(res.authSetting)
    // res.authSetting = {
    //   "scope.userInfo": true,
    //   "scope.userLocation": true
    //   "setting.appMsgSubscribed": true, // 长期订阅开关，true：打开；false：关闭
    // }
    console.log(res.subscriptionsSetting)
    // res.subscriptionsSetting = {
    //   itemSettings: {   // 订阅消息
    //     SYS_MSG_TYPE_INTERACTIVE: 'accept', // 小程序系统订阅消息：好友互动提醒
    //     SYS_MSG_TYPE_RANK: 'accept', // 小程序系统订阅消息：排行榜超越提醒
    //     118d4118a4609537873d18fdsfe932332: 'reject', // 普通一次性订阅消息
    //     53231118a4609537873d18fdsfe932332: 'ban', // 普通一次性订阅消息
    //   }
    // }
  }
})
```