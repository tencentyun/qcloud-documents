### 用户绑定和接收 push
#### 用户绑定
Wns 会对每一个设备记录一个设备 ID 来进行标识, 可以通过后端的 API 对某一个设备进行消息推送(PUSH). 但是应用本身可能也有自己的用户 id (后面简称 uid), 如果需要对某一个 uid 进行消息推送时, 客户端就得在用户登录和注销时调用绑定/注销的相应方法. 调用后, Wns 后台会记录两者的对应关系, 此后就能对该 uid 进行消息推送
```
/*! @brief
 * 第三方应用层可选调用接口。如果第三方应用后台需要通过WNS服务发送针对指定用户的数据，
 * 则第三方应用终端，在用户登录成功后，需要绑定第三方用户ID到WNS服务。
 * 对新uid进行绑定前, 需要使用unbind对旧bid进行解绑
 * 
 * @param uid 第三方应用的用户唯一标识
 * @param completion 回调Block
 */
- (void)bind:(NSString *)uid completion:(void(^)(NSError *error))completion;


/*! @brief 注销绑定。应用的用户注销时请调用该接口.
 *
 * @param uid 第三方应用的用户唯一标识
 * @param completion 回调Block
 */
- (void)unbind:(NSString *)uid completion:(void(^)(NSError *error))completion;

```

#### 接收 Push
```
/*! @brief 设置Wns Push的数据接收block。
 *
 * @param completion 回调Block，参数cmd标识服务推送数据命令字，参数data标识服务器推送数据，参数error标识错误信息
 */
- (void)setPushDataReceiveBlock:(void(^)(NSString *cmd, NSData *data, NSError *error))completion;

/*! @brief 向服务器注册苹果的推送服务所使用的devicetoken
 *
 * @param deviceToken 用户设备Tokon。
 * @param completion 回调Block, error为nil时表示注册成功
 */
- (void)registerRemoteNotification:(NSString *)deviceToken completion:(void(^)(NSError *error))completion;

```
