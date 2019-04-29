## 注册设备 Token
启动推送服务以后，如果注册推送成功，则应用会调用 UIApplicationDelegate 代理对象的回调方法（如下），开发者可以在其中调用注册设备 Token 的接口（非必须）。
```
- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken;
```

#### 接口
```
- (void)registerDeviceToken:(nonnull NSData *)deviceToken;
```
#### 示例
```
- (void)application:(UIApplication *)application
    didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
      [[XGPushTokenManager defaultTokenManager] registerDeviceToken:deviceToken];
}
```
## 绑定/解绑标签和账号
开发者可以针对不同的用户绑定标签，然后对该标签推送。对标签推送会让该标签下的所有设备都收到推送。一个设备可以绑定多个标签。
>**注意:**
> 一个设备只能绑定一个账号，绑定账号的时候前一个账号自动失效。一个账号最多绑定十五台设备，超过之后会随机解绑一台设备，然后再进行注册。

#### 接口
```
- (void)bindWithIdentifier:(nullable NSString *)identifier type:(XGPushTokenBindType)type;
- (void)unbindWithIdentifer:(nullable NSString *)identifier type:(XGPushTokenBindType)type;
```
#### 示例

- 绑定标签：
```
[[XGPushTokenManager defaultTokenManager] bindWithIdentifier:@"your tag" type:XGPushTokenBindTypeTag];
```
- 解绑标签
```
[[XGPushTokenManager defaultTokenManager] unbindWithIdentifer:@"your tag" type:XGPushTokenBindTypeTag];
```
- 绑定账号：
```
  [[XGPushTokenManager defaultTokenManager] bindWithIdentifier:@"your account" type:XGPushTokenBindTypeAccount];
```
- 解绑账号：
```
[[XGPushTokenManager defaultTokenManager] unbindWithIdentifer:@"your account" type:XGPushTokenBindTypeAccount];
```


