## 登录

用户登录腾讯后台服务器后才能正常收发消息，登录需要用户提供 `UserID`、`UserSig`。如果用户保存用户票据，可能会存在过期的情况，如果用户票据过期，`login` 将会返回 `6206` 错误码，开发者可根据错误码进行票据更换。登录为异步过程，通过回调函数返回是否成功，成功后方能进行后续操作。登录成功或者失败后使用闭包 `succ` 和 `fail` 进行回调。

>!
>- 如果此用户在其他终端被踢，登录将会失败，返回错误码（`ERR_IMSDK_KICKED_BY_OTHERS：6208`）。开发者必须进行登录错误码 `ERR_IMSDK_KICKED_BY_OTHERS` 的判断。关于被踢的详细描述，参见 [用户状态变更](https://cloud.tencent.com/document/product/269/9148#.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4)。
>- 只要登录成功以后，用户没有主动登出或者被踢，网络变更会自动重连，无需开发者关心。不过特别需要注意被踢操作，需要注册 [用户状态变更回调](https://cloud.tencent.com/document/product/269/9148#.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4)，否则被踢时得不到通知。

**原型：**

```
/**
 *  登录信息
 */
@interface TIMLoginParam : NSObject
/**
 * 用户名
 */
@property(nonatomic,retain) NSString* identifier;
/**
 *  鉴权 Token
 */
@property(nonatomic,retain) NSString* userSig;

@end
```

```
/**
 *  登录
 *
 *  @param param 登录参数
 *  @param succ  成功回调
 *  @param fail  失败回调
 *
 *  @return 0 请求成功
 */
- (int)login:(TIMLoginParam*)param succ:(TIMLoginSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
param | 登录参数，详细信息参见 [TIMLoginParam](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/iOS/ImSDK/Classes/TIMLoginParam.html) 结构说明
succ | 登录成功回调
fail | 登录失败回调

**示例：**

```
TIMLoginParam * login_param = [[TIMLoginParam alloc ]init];
// identifier 为用户名
login_param.identifier = @"iOS_001";
//userSig 为用户登录凭证
login_param.userSig = @"usersig";
[[TIMManager sharedInstance] login: login_param succ:^(){
    NSLog(@"Login succ");
} fail:^(int code, NSString * err) {
    NSLog(@"Login Failed: %d->%@", code, err);
}];
```
UserSig 正确的签发方式请参考 [登录鉴权](https://cloud.tencent.com/document/product/269/31999)。
## 登出

如用户主动注销或需要进行用户的切换，则需要调用注销操作。

**原型：**

```
@interface TIMManager : NSObject
/**
 *  登出
 *
 *  @param succ 成功回调，登出成功
 *  @param fail 失败回调，返回错误码和错误信息
 *
 *  @return 0 发送登出包成功，等待回调
 */
- (int)logout:(TIMLoginSucc)succ fail:(TIMFail)fail; 
@end
```

**示例：**

>!在需要切换帐号时，需要 `logout` 回调成功或者失败后才能再次 `login`，否则 `login` 可能会失败。

```
[[TIMManager sharedInstance] logout:^() {
    NSLog(@"logout succ");
} fail:^(int code, NSString * err) {
    NSLog(@"logout fail: code=%d err=%@", code, err);
}];
```

## 无网络情况下查看消息

如用当前网络异常，或者想在不调用 `login` 的时候查看用户消息，可调用 `initStorage` 方法初始化存储，完成后可获取会话列表和消息。

**原型：**

```
@interface TIMManager : NSObject
/**
 *  初始化存储，仅查看历史消息时使用，如果要收发消息等操作，如 login 成功，不需要调用此函数
 *
 *  @param userID 用户名
 *  @param succ  成功回调，收到回调时，可以获取会话列表和消息
 *  @param fail  失败回调
 *
 *  @return 0 请求成功
 */
- (int)initStorage:(NSString*)userID succ:(TIMLoginSucc)succ fail:(TIMFail)fail; 
@end
```

**参数说明：**

| 参数 | 说明 |
| --- | --- |
| userID | 用户名 |
| succ | 成功回调，成功后可获取会话列表，以及进一步登录 |
| fail | 失败回调 |

以下示例中初始化存储，成功后可获取会话列表。**示例：**

```
TIMLoginParam * login_param = [[TIMLoginParam alloc ]init]; 
[[TIMManager sharedInstance] initStorage: @"iOS_001" succ:^(){
    NSLog(@"Init Succ");
} fail:^(int code, NSString * err) {
    NSLog(@"Init Failed: %d->%@", code, err);
}];
```

## 获取当前登录用户

通过 `TIMManager` 成员方法 `getLoginUser` 可以获取当前用户名，也可以通过这个方法判断是否已经登录。返回值为当前登录的用户名，需要注意的是，如果是自有帐号登录，用户名与登录所传入的 `UserID` 相同，如果是第三方帐号，如微信登录，QQ 登录等，登录后会有内部转换过的 `UserID`，后续搜索好友，入群等，都需要使用转换后的 `UserID` 操作。

**原型：**

```
@interface TIMManager : NSObject
 
/**
 *  获取当前登录的用户
 *
 *  @return 如果登录返回用户的 identifier，如果未登录返回 nil
 */
- (NSString*)getLoginUser;
 
@end
```

## IM SDK 同步离线消息

IM SDK 启动后会同步离线消息和最近联系人。如果不需要离线消息，可以在发消息时使用：[发送在线消息](https://cloud.tencent.com/doc/product/269/9150#.E5.9C.A8.E7.BA.BF.E6.B6.88.E6.81.AF)。默认登录后会异步获取离线消息以及同步资料数据（如果有开启，可参见关系链资料章节），同步完成后会通过 `onRefresh` 回调通知更新界面，用户得到这个消息时，可以刷新界面，例如会话列表的未读等。

```
@interface TIMUserConfig : NSObject
/**
 *  会话刷新监听器（未读计数、已读同步）
 */
@property(nonatomic,retain) id<TIMRefreshListener> refreshListener;
@end
```


