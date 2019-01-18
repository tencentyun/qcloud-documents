Setting a protocol proxy bound with device Token is to make it easy for developers to check the Token binding result. Developers can select how to implement the protocol based on their own needs.

**Example**
```
[[XGPushTokenManager defaultTokenManager].delegatge = <#your delegate#>;
```
The protocol method is as follows:

```
/**
 @brief Monitor the binding of token object

 @param identifier token Identifier of the bound Token object
 @param type Type of the bound token object
 @param error token Result on whether the token object is bound
 */
- (void)xgPushDidBindWithIdentifier:(nullable NSString *)identifier type:(XGPushTokenBindType)type error:(nullable NSError *)error;

/**
 @brief Monitor the unbinding of the token object

 @param identifier token Identifier of the bound Token object
 @param type Type of the bound token object
 @param error token Result on whether the token object is bound
 */
- (void)xgPushDidUnbindWithIdentifier:(nullable NSString *)identifier type:(XGPushTokenBindType)type error:(nullable NSError *)error;
```

