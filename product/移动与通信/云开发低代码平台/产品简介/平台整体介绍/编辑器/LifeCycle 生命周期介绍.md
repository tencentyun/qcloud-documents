
微搭支持应用、页面级别的生命周期函数，当对应的生命周期函数触发时，便会自动执行函数下已配置的自定义方法。

## 应用生命周期

在低码编辑器中，选择**全局**文件夹下的 lifecycle 文件，即可对应用的生命周期进行管理。

![](https://qcloudimg.tencent-cloud.cn/raw/6938066e431c962c2b70b7e9122158a7.png)

应用生命周期说明：

| 函数名                  | 说明                                                     |
| ----------------------- | -------------------------------------------------------- |
| onAppLaunch             | 当应用初始化完成时触发（全局只触发一次）                 |
| onAppShow               | 监听小程序切前台事件。该事件与 App.onShow 的回调参数一致 |
| onAppHide               | 监听小程序切后台事件。该事件与 App.onHide 的回调时机一致 |
| onAppError              | 小程序发生脚本错误或 API 调用报错时触发                  |
| onAppPageNotFound       | 小程序要打开的页面不存在时触发                           |
| onAppUnhandledRejection | 小程序有未处理的 Promise 拒绝时触发                      |



## 页面生命周期

在低码编辑器中，选择对应页面文件夹下的 lifecycle 文件，即可对该页面的生命周期进行管理。

![](https://qcloudimg.tencent-cloud.cn/raw/feb997066d2e6d1447513dc5db0877d4.png)

页面生命周期说明：

| 函数名       | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| onPageLoad   | 页面加载时触发。一个页面只会调用一次，可以在 onLoad 的参数中获取打开当前页面路径中的参数 |
| onPageShow   | 页面显示/切入前台时触发                                      |
| onPageReady  | 页面初次渲染完成时触发。一个页面只会调用一次，代表页面已经准备妥当，可以和视图层进行交互 |
| onPageHide   | 页面隐藏/切入后台时触发。 如 app.navigateTo 或底部 tab 切换到其他页面，小程序切入后台等。 |
| onPageUnload | 页面卸载时触发。如 app.redirectTo 或 app.navigateBack 到其他页面时。 |



