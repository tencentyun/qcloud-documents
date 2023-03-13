# wx.openSetting
### wx.openSetting(Object object)

调起客户端小程序设置界面，返回用户设置的操作结果。

用户发生点击行为后，可以跳转打开设置页，管理授权信息。

#### 参数

##### Object object

 属性              | 类型     | 默认值 | 必填 | 说明                                                         
 ----------------- | -------- | ------ | ---- | ------------------------------------------------------------ 
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
wx.openSetting({
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
wx.openSetting({
  success (res) {
    console.log(res.authSetting)
    // res.authSetting = {
    //   "scope.userInfo": true,
    //   "scope.userLocation": true
    // }
  }
})
```