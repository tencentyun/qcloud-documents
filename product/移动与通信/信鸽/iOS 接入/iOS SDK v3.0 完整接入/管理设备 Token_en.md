## Registering a Device Token
After the push service is activated, if the registration is successful, the App calls the callback method of the UIApplicationDelegate proxy object (see below), where the developer can call the API for registering the device Token (optional).
```
- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken;
```

#### APIs
```
- (void)registerDeviceToken:(nonnull NSData *)deviceToken;
```
#### Example
```
- (void)application:(UIApplication *)application
    didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
      [[XGPushTokenManager defaultTokenManager] registerDeviceToken:deviceToken];
}
```
## Binding/Unbinding Tags and Accounts
Developers can bind a tag to different users and then push messages to the tag. This allows all devices under the tag to receive the messages pushed. Multiple tags can be bound to a single device.
>**Note:**
>Only one account can be bound to a single device. When an account is bound, the previous account becomes invalid automatically. A maximum of 15 devices can be bound to one account. When the limit is exceeded, a previously bound device is unbound at random and then a new device is registered.

#### APIs
```
- (void)bindWithIdentifier:(nullable NSString *)identifier type:(XGPushTokenBindType)type;
- (void)unbindWithIdentifer:(nullable NSString *)identifier type:(XGPushTokenBindType)type;
```
#### Example

- Binding tag:
```
[[XGPushTokenManager defaultTokenManager] bindWithIdentifier:@"your tag" type:XGPushTokenBindTypeTag];
```
- Unbinding tag:
```
[[XGPushTokenManager defaultTokenManager] unbindWithIdentifer:@"your tag" type:XGPushTokenBindTypeTag];
```
- Binding account:
```
  [[XGPushTokenManager defaultTokenManager] bindWithIdentifier:@"your account" type:XGPushTokenBindTypeAccount];
```
- Unbinding account:
```
[[XGPushTokenManager defaultTokenManager] unbindWithIdentifer:@"your account" type:XGPushTokenBindTypeAccount];
```



