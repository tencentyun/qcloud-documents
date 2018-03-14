设置设备 Token 绑定协议代理对象是为了方便查看 Token 绑定的结果，开发者可根据自己的需求选择实现协议的方法。

**示例**
```
[[XGPushTokenManager defaultTokenManager].delegatge = <#your delegate#>;
```
协议方法如下：

```
/**
 @brief 监控token对象绑定的情况

 @param identifier token对象绑定的标识
 @param type token对象绑定的类型
 @param error token对象绑定的结果信息
 */
- (void)xgPushDidBindWithIdentifier:(nullable NSString *)identifier type:(XGPushTokenBindType)type error:(nullable NSError *)error;

/**
 @brief 监控token对象解绑的情况

 @param identifier token对象绑定的标识
 @param type token对象绑定的类型
 @param error token对象绑定的结果信息
 */
- (void)xgPushDidUnbindWithIdentifier:(nullable NSString *)identifier type:(XGPushTokenBindType)type error:(nullable NSError *)error;
```
