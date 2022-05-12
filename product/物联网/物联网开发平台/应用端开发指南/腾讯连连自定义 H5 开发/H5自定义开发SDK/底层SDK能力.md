## 应用开发 SDK
H5 SDK 底层依赖应用开发小程序端 SDK。通过以下代码可以获取应用开发 SDK 的实例，更多调用能力请参见 [应用开发小程序端 SDK](https://github.com/tencentyun/qcloud-iotexplorer-appdev-miniprogram-sdk#readme) 文档。

**接口定义**
```typescript
sdk.appDevSdk
```



## 微信 JS SDK

通过以下代码可以获取微信 JSSDK 实例，具体用法请参见 [小程序 web-view 文档](https://developers.weixin.qq.com/miniprogram/dev/component/web-view.html)。使用前需要先调用 [初始化 JSSDK](#sdk-wx-sdk-ready)。

**接口定义**
```typescript
sdk.wx
```



<span id="sdk-wx-sdk-ready"></span>

## 初始化 JS SDK

**接口定义**

```typescript
sdk.wxSdkReady() => Promise
```
**返回值**

返回一个带缓存的 Promise，初始化成功后 resolve。若初始化未完成或已初始化成功，则多次调用后返回同一个 Promise。若初始化失败，则该缓存的 Promise 在 reject 之后会被释放，再次调用则将重新初始化。

**示例代码**

```javascript
sdk.wxSdkReady().then(() => wx.miniProgram.navigateBack());
```

