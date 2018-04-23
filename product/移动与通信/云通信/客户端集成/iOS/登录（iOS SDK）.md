## 登录

用户登录腾讯后台服务器后才能正常收发消息，登录需要用户提供 `accountType`、`identifier`、`userSig` 等信息。如果用户保存用户票据，可能会存在过期的情况，如果用户票据过期，`login` 将会返回 `70001` 错误码，开发者可根据错误码进行票据更换。登录为异步过程，通过回调函数返回是否成功，成功后方能进行后续操作。登录成功或者失败后，有两种回调方式，一种使用闭包，`succ` 和 `fail` 两种闭包回调，另一种使用 `protocol`，用户实现 `TIMCallback` 接口进行回调。

> **注意：**
>- 如果此用户在其他终端被踢，登录将会失败，返回错误码（`ERR_IMSDK_KICKED_BY_OTHERS：6208`）。开发者必须进行登录错误码 `ERR_IMSDK_KICKED_BY_OTHERS` 的判断。关于被踢的详细描述，参见 [用户状态变更](/doc/product/269/1566#.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4)。
>- 只要登录成功以后，用户没有主动登出或者被踢，网络变更会自动重连，无需开发者关心。不过特别需要注意被踢操作，需要注册 [用户状态变更回调](/doc/product/269/初始化（Android%20SDK）#.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4.EF.BC.88.E4.BA.92.E8.B8.A2.EF.BC.89)，否则被踢时得不到通知。

**原型：**

```
// 登录信息
@interface TIMLoginParam : NSObject{
    NSString*       accountType;         // 用户的帐号类型
    NSString*       identifier;              // 用户名
    NSString*       userSig;             // 鉴权 Token
    NSString*       appidAt3rd;          // App 用户使用 OAuth 授权体系分配的 Appid
    int             sdkAppId;           // 用户标识接入 SDK 的应用 ID
}
```

在自有帐号情况下：`appidAt3rd` 字段与 `sdkAppId` 相同，其他字段 `sdkAppId`、`accountType`、`identifier`、`userSig` 填写相应内容。

```
@interface TIMManager : NSObject
// TIMManager 登录：闭包方式回调
-(int) login: (TIMLoginParam *)param succ:(TIMLoginSucc)succ fail:(TIMFail)fail;
// 登录：TIMLoginCallback回调
-(int) login: (TIMLoginParam *)param cb:(id)cb;
@end
```

**参数说明：**

| 参数 | 说明 |
| --- | --- |
| param | 登录参数，包括帐号类型、用户名、鉴权、Appid、sdkAppId 等 |
| succ | 登录成功回调 |
| fail | 登录失败回调 |

以下示例展示了使用闭包回调方式进行登录。**示例1：**

```
TIMLoginParam * login_param = [[TIMLoginParam alloc ]init];
// accountType 和 sdkAppId 通讯云管理平台分配
// identifier 为用户名，userSig 为用户登录凭证
// appidAt3rd 在私有帐号情况下，填写与 sdkAppId 一样
login_param.accountType = @"107";
login_param.identifier = @"iOS_001";
login_param.userSig = @"usersig";
login_param.appidAt3rd = @"123456";
login_param.sdkAppId = 123456;
[[TIMManager sharedInstance] login: login_param succ:^(){
    NSLog(@"Login Succ");
} fail:^(int code, NSString * err) {
    NSLog(@"Login Failed: %d->%@", code, err);
}];
```

以下示例展示了使用 `protocol` 回调方式进行登录。**示例2：**

```
@interface LoginCallback : NSObject
- (void) onSucc;
- (void)onErr:(int)errCode errMsg:(NSString*)errMsg;
@end
@implementation LoginCallback
- (void) onSucc {
    NSLog(@"Login Succ");
}
- (void)onErr:(int)errCode errMsg:(NSString*)errMsg {
    NSLog(@"Login Failed: code=%d, err=%@", errCode, errMsg);
} 
@end
TIMLoginParam * login_param = [[TIMLoginParam alloc ]init];
// accountType 和 sdkAppId 通讯云管理平台分配
// identifier为用户名，userSig 为用户登录凭证
// appidAt3rd 在私有帐号情况下，填写与 sdkAppId 一样
login_param.accountType = @"107";
login_param.identifier = @"iOS_001";
login_param.userSig = @"usersig";
login_param.appidAt3rd = @"123456"; 
login_param.sdkAppId = 123456; 
LoginCallback * login_cb = [[LoginCallback alloc] init];
[[TIMManager sharedInstance] login: login_param cb:login_cb];
```

## 登出

如用户主动注销或需要进行用户的切换，则需要调用注销操作。

**原型：**

```
@interface TIMManager : NSObject
/**
 *  登出
 *
 *  @param succ 成功回调，登出成功
 *  @param fail 失败回调，返回错误吗和错误信息
 *
 *  @return 0 发送登出包成功，等待回调
 */
-(int) logout:(TIMLoginSucc)succ fail:(TIMFail)fail; 
@end
```

**示例：**

> **注意：**
> 在需要切换帐号时，需要 `logout` 回调成功或者失败后才能再次 `login`，否则 `login` 可能会失败。

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
 *  @param param 登录参数（userSig 不用填写）
 *  @param succ  成功回调，收到回调时，可以获取会话列表和消息
 *  @param fail  失败回调
 *
 *  @return 0 请求成功
 */
-(int) initStorage: (TIMLoginParam *)param succ:(TIMLoginSucc)succ fail:(TIMFail)fail; 
@end
```

**参数说明：**

| 参数 | 说明 |
| --- | --- |
| param | 与登录参数相同，userSig 可不填 |
| succ | 成功回调，成功后可获取会话列表，以及进一步登录 |
| fail | 失败回调 |

以下示例中初始化存储，成功后可获取会话列表。**示例：**

```
TIMLoginParam * login_param = [[TIMLoginParam alloc ]init];
// accountType 和 sdkAppId 通讯云管理平台分配
// identifier为用户名
// appidAt3rd 在私有帐号情况下，填写与 sdkAppId 一样
login_param.accountType = @"107";
login_param.identifier = @"iOS_001";
login_param.appidAt3rd = @"123456";
login_param.sdkAppId = 123456;
[[TIMManager sharedInstance] initStorage: login_param succ:^(){
    NSLog(@"Init Succ");
} fail:^(int code, NSString * err) {
    NSLog(@"Init Failed: %d->%@", code, err);
}];
```

## 获取当前登录用户

通过 `TIMManager` 成员方法 `getLoginUser` 可以获取当前用户名，也可以通过这个方法判断是否已经登录。返回值为当前登录的用户名，需要注意的是，如果是自有帐号登录，用户名与登录所传入的 `identifier` 相同，如果是第三方帐号（如微信登录、QQ 登录等），登录后会有内部转换过的 `identifer`，后续搜索好友，入群等，都需要使用转换后的 `identifier` 操作。

**原型：**

```
@interface TIMManager : NSObject
/**
 *  获取当前登录的用户
 *
 *  @return 如果登录返回用户的 identifier，如果未登录返回 nil
 */
-(NSString*) getLoginUser;
@end
```

## ImSDK 同步离线消息

ImSDK 启动后会同步离线消息和最近联系人，最近联系人可通过 [禁用最近联系人](/doc/product/269/消息收发（iOS%20SDK）#.E6.9C.80.E8.BF.91.E8.81.94.E7.B3.BB.E4.BA.BA.E6.BC.AB.E6.B8.B8) 接口禁用。如果不需要离线消息，可以再发消息时使用：[发送在线消息](/doc/product/269/消息收发（iOS%20SDK）#.E5.9C.A8.E7.BA.BF.E6.B6.88.E6.81.AF)。默认登录后会异步获取离线消息以及同步资料数据（如果有开启 ImSDK 存储，可参见关系链资料章节），同步完成后会通过 `onRefresh` 回调通知更新界面，用户得到这个消息时，可以刷新界面，比如会话列表的未读等等。

```
@interface TIMManager : NSObject
/**
 *  设置会话刷新监听
 *
 *  @param listener 刷新监听（当有未读计数变更、会话变更时调用）
 *
 *  @return 0 设置成功
 */
-(int) setRefreshListener: (id<TIMRefreshListener>)listener;
@end
```