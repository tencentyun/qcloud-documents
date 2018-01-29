## Authorization 编程使用指南

## 开始之前


如果这是您首次向应用添加 Authorization，请完成以下步骤：

在 应用云 控制台中关联您的应用

1. 安装 [应用云 SDK]()。
2. 在 [应用云 控制台]()中，将您的应用添加到您的 应用云 项目中。
3. 参考 [Authorization 配置文档]()，配置并初始化  Authorization


## 获取 第三方 用户登录信息

### 获取 QQ 登录用户信息

> 请确保您集成并安装了 TACAuthorizationQQ 模块

首先，您需要引入头文件：

~~~
#import <TACAuthorizationQQ/TACAuthorizationQQ.h>
~~~

然后您就可以使用 `TACQQAuthProvider` 来获取 QQ 的登录信息

~~~
TACQQAuthProvider* provider = [[TACAuthoriztionService defaultService] qqCredentialProvider];
[provider requestCredential:^(TACQQCredential*credential, NSError *error) {
    if (error) {
        TACLogError(@"ERROR %@", error);
    } else {
        [provider requestUserInfoWithCredential:credential completation:^(TACOpenUserInfo *userInfo, NSError *error) {

        }];

        TACLogDebug(@"Credential %@", credential);
    }
}];
~~~


### 获取 微信 登录用户信息

> 请确保您集成并安装了 TACAuthorizationWechat 模块

首先，您需要引入头文件：

~~~
#import <TACAuthorizationWechat/TACAuthorizationWechat.h>
~~~

然后您就可以使用 `TACWechatAuthProvider` 来获取 微信 的登录信息

~~~
TACWechatAuthProvider* provider = [[TACAuthoriztionService defaultService] wechatCredentialProvider];
[provider requestCredential:^(TACCredential *credential, NSError *error) {
    if (error) {
        TACLogError(@"ERROR %@", error);
    } else {
        [provider requestUserInfoWithCredential:credential completation:^(TACOpenUserInfo *userInfo, NSError *error) {

        }];
        TACLogDebug(@"Credential %@", credential);
    }
}];
~~~
