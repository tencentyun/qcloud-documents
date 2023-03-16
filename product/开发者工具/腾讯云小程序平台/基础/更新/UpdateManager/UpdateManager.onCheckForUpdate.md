### .onCheckForUpdate

#### UpdateManager.onCheckForUpdate(function callback)

监听向后台请求检查更新结果事件。在小程序冷启动时自动检查更新，不需由开发者主动触发。

#### 参数

##### function callback

向后台请求检查更新结果事件的回调函数

###### 参数

**Object res**

属性        | 类型      | 说明    
--------- | ------- | ------
hasUpdate | boolean | 是否有新版本