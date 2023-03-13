# wx.navigateToMiniProgram
### wx.navigateToMiniProgram(Object object)

打开另一个小程序

#### 参数

##### Object object

属性         | 类型       | 默认值     | 必填 | 说明                                                         
---------- | -------- | ------- | -- | -----------------------------------------------------------
appId      | string   |         | 是  | 要打开的小程序 appId                                              
path       | string   |         | 否  | 打开的页面路径，如果为空则打开首页                                          
extraData  | object   |         | 否  | 需要传递给目标小程序的数据，目标小程序可在 `App.onLaunch`，`App.onShow` 中获取到这份数据。
envVersion | string   | release | 否  | 要打开的小程序版本。仅在当前小程序为开发版或体验版时此参数有效。如果当前小程序是正式版，则打开的小程序必定是正式版。 
success    | function |         | 否  | 接口调用成功的回调函数                                                
fail       | function |         | 否  | 接口调用失败的回调函数                                                
complete   | function |         | 否  | 接口调用结束的回调函数（调用成功、失败都会执行）                                   

**object.envVersion 的合法值**

值       | 说明 
------- | ---
develop | 开发版
trial   | 体验版
release | 正式版

#### 使用限制

##### 需要用户触发跳转

若用户未点击小程序页面任意位置，则开发者将无法调用此接口自动跳转至其他小程序。

##### 需要用户确认跳转

在跳转至其他小程序前，将统一增加弹窗，询问是否跳转，用户确认后才可以跳转其他小程序。如果用户点击取消，则回调 `fail cancel`。

##### 每个小程序可跳转的其他小程序数量限制为不超过 10 个

开发者提交新版小程序代码时，如使用了跳转其他小程序功能，则需要在代码配置中声明将要跳转的小程序名单，限定不超过 10 个，否则将无法通过审核。该名单可在发布新版时更新，不支持动态修改。配置方法详见 [配置](/develop/frame/dispose.md)。调用此接口时，所跳转的 appId 必须在配置列表中，否则回调 `fail appId "${appId}" is not in navigateToMiniProgramAppIdList`。

#### 示例代码

```js
wx.navigateToMiniProgram({
  appId: '',
  path: 'page/index/index?id=123',
  extraData: {
    foo: 'bar'
  },
  envVersion: 'develop',
  success(res) {
    // 打开成功
  }
})
```