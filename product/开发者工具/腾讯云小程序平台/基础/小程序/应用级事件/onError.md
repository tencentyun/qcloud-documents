# wx.onError

#### wx.onError(function callback)

监听小程序错误事件。如脚本错误或 API 调用报错等。

<!-- 该事件与 [`App.onError`](https://developers.weixin.qq.com/miniprogram/dev/reference/api/App.html#onerrorstring-error) 的回调时机与参数一致。 -->

#### 参数

##### function callback

小程序错误事件的回调函数

###### 参数

**string error**

错误信息，包含堆栈

