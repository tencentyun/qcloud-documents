本文将指导您初始化 SDK 和如何调用登录接口。
## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。
[Demo 代码下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/MAC_TRTC.zip)

## 前提条件
要求用户在[ 实时音视频官网 ](https://cloud.tencent.com/product/trtc)完成服务开通及应用创建。

## 相关概念
 - [实时音视频应用](https://cloud.tencent.com/document/product/647/16792#.E5.AE.9E.E6.97.B6.E9.9F.B3.E8.A7.86.E9.A2.91.E5.BA.94.E7.94.A8)
 - [应用标识( sdkAppId )](https://cloud.tencent.com/document/product/647/16792#.E5.BA.94.E7.94.A8.E6.A0.87.E8.AF.86.EF.BC.88-sdkappid-.EF.BC.89)
 - [帐号类型( accountType )](https://cloud.tencent.com/document/product/647/16792#.E5.B8.90.E5.8F.B7.E7.B1.BB.E5.9E.8B.EF.BC.88-accounttype-.EF.BC.89)
 - [用户标识( userId )](https://cloud.tencent.com/document/product/647/16792#.E7.94.A8.E6.88.B7.E6.A0.87.E8.AF.86.EF.BC.88-userId-.EF.BC.89)
 - [用户签名( userSig )](https://cloud.tencent.com/document/product/647/16792#.E7.94.A8.E6.88.B7.E7.AD.BE.E5.90.8D.EF.BC.88-usersig-.EF.BC.89)

## 获取 userSig
客户端的每一个用户都需要一个独立的 userSig，userSig 是有效期的( 在生成时设置，一般为三个月 )，如果 userSig 过期，用户登录时会收到错误码 8051，这时用户需要重新生成 userSig，拿到新的 userSig再登录。

```objc
ERR_EXPIRE              = 8051,    //票据过期(需更新票据userSig)
```

> 注意： 关于 userSig 的获取请参考[ 用户鉴权 ](https://cloud.tencent.com/document/product/647/16792#.E7.94.A8.E6.88.B7.E7.AD.BE.E5.90.8D.EF.BC.88-usersig-.EF.BC.89)。 在调试期间您可以直接使用控制台的开发辅助工具生成 userSig。


## 初始化 iLiveSDK

建议在程序启动时就将 SDK 初始化，初始化需要用到在腾讯云后台创建应用时分配的 SDKAppId，本示例代码中在本地配置了SDKAppId，读取配置获取信息即可，示例代码如下：
```objc
> AppDelegate.m

// 导入头文件
#import <ILiveSDK/ILiveSDK.h>


- (void)applicationDidFinishLaunching:(NSNotification *)aNotification {

    [[ILiveSDK getInstance] initSdk:[TCLiveConfigInfo getInstance].sdkAppID];

}

```

## 调用登录接口

登录接口位于 ILiveLoginManager 类中，使用时需将其导入，调用方法：
```
- (void)iLiveLogin:(NSString *)uid sig:(NSString *)sig succ:(TCIVoidBlock)succ failed:(TCIErrorBlock)failed;
```

填入后台开发辅助工具生成的 userId 和 userSig ：
```objc

> ViewController.m

// 导入头文件
#import <ILiveSDK/ILiveLoginManager.h>

- (IBAction)onLogin:(id)sender {
    if ([self.inputTextField stringValue].length >0) {
        NSDictionary *dic = [[TCLiveConfigInfo getInstance] parseLoginInfoConfig];
        for (NSDictionary *user in dic[@"users"]) {
            NSString *userid = user[@"userId"];
            NSInteger selectIndex = [self.userName indexOfSelectedItem];
            NSString *selectName = [self.userName itemTitleAtIndex:selectIndex];
            if ([userid isEqualToString:selectName]) {
                [TCLiveConfigInfo getInstance].userToken = user[@"userToken"];
                [TCLiveConfigInfo getInstance].userID = selectName;
                break;
            }
        }
        //step2 登录
        [[ILiveLoginManager getInstance] iLiveLogin:[TCLiveConfigInfo getInstance].userID sig:[TCLiveConfigInfo getInstance].userToken succ:^{
            NSLog(@"-----> login  succ");
        } failed:^(NSString *module, int errId, NSString *errMsg) {

            NSLog(@"-----> login  fail,%@ %d %@",module, errId, errMsg);
        }];

        NSString *defaultRole = [[TCLiveConfigInfo getInstance].roles firstObject][@"name"];
        _vc = [[TCLiveRoomWC alloc] initWithRoomID:[self.inputTextField stringValue] role:defaultRole];
        [_vc.window orderFront:nil];
    }
    else{

    }

}

```
## 监听用户状态
用户在登录后，有可能被强制下线的(帐号重复登录被踢，userSig 过期 )，所以当应用需要监听这两个状态时可进行如下步骤实现：

设置监听对象调用方法：
```objc
[[ILiveSDK getInstance] setUserStatusListener:self];
```
监听对象遵守TIMUserStatusListener协议，并实现以下方法：
```objc
/**
 *  踢下线通知
 */
- (void)onForceOffline;

/**
 *  用户登录的userSig过期（用户需要重新获取userSig后登录）
 */
- (void)onUserSigExpired;
```
>**注意：**
>示例程序中用 storyboard 搭建了一个简单界面，实际应用中客户需根据自己的业务逻辑，将登录代码放置与合适的位置。
> 且以上仅为示例代码，实际过程中（客户采用独立帐号模式），登录流程应为：
>
> 客户端显示登录界面，用户输入帐号密码，客户的业务后台验证通过后使用实时音视频后台 SDK 生成 userSig 返回给客户端，客户端再拿用户输入的用户名和业务后台返回的 userSig 调用 ILiveSDK的登录接口。

运行程序，控制台输出登录成功！，即说明 ILiveSDK 登录成功。
