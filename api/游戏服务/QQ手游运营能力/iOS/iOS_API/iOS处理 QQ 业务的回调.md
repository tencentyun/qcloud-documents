
在使用 QQApiInterface 的方法时需要设置回调才能正确调用。设置方法如下：

```
- (BOOL)application:(UIApplication *)application handleOpenURL:(NSURL *)url {
[QQApiInterface handleOpenURL:url delegate:qqApiDelegate];
return YES;
}
```

在 handleOpenURL 中添加 `QQApiInterface handleOpenURL:url delegate: qqApiDelegate` 代码，可以在 QQAPIDemoEntry 类中实现 QQApiInterfaceDelegate 的回调方法。

>**注意：**
>添加关于 onReq 和 onResp 的说明，同时微信与 QQ 回调相同，提醒开发者注意采用不同的代理处理回调。
