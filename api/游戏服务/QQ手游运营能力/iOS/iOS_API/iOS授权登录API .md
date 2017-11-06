
## 功能描述

整个授权过程可以分为 **发送请求获取用户授权** 和 **获取用户授权结果** 两个部分。
- 发送请求获取用户授权：
在取得用户授权之前，开发者必须清楚自己需要用户的哪些信息。 iOS SDK 提供多种选择，开发者可以根据自己的需要请求用户进行授权。具体可以获取的授权信息参见下表的参数说明。设置完需要请求的授权信息之后即可发送请求。
>**注意：**
>inSafari 参数从 iOS SDK1.3 版本后弃用。
- 获取用户授权结果:
获取用户授权结果，采用的是代理回调的方式，所以开发者需要实现 TencentLoginDelegate 协议。登录结果分为三种：登录成功、登录失败和登录取消。

```
- (void)tencentDidLogin;  // 登录成功后的回调
- (void)tencentDidNotLogin:(BOOL)cancelled;  // 登录失败后的回调
- (void)tencentDidNotNetWork;  // 登录时网络有问题的回调
```
## 方法原型

```
/**
 * 登录授权
 *
 * \param permissions 授权信息列
 */
- (BOOL)authorize:(NSArray *)permissions;

```

## 参数说明

| 参数名 | 参数说明 | 
|---------|---------|
| kOPEN_PERMISSION_GET_USER_INFO | 获取用户信息。 | 
| kOPEN_PERMISSION_GET_SIMPLE_USER_INFO | 移动端获取用户信息。 | 
| kOPEN_PERMISSION_GET_INFO | 获取登录用户自己的详细信息。 | 
| kOPEN_PERMISSION_GET_VIP_RICH_INFO | 获取会员用户详细信息。 | 
| kOPEN_PERMISSION_GET_VIP_INFO | 获取会员用户基本信息。 | 
|kOPEN_PERMISSION_GET_OTHER_INFO | 获取其他用户的详细信息。 | 
| kOPEN_PERMISSION_ADD_TOPIC | 发表一条说说到QQ空间 (**需要申请权限**)。 | 
| kOPEN_PERMISSION_ADD_ONE_BLOG | 发表一篇日志到QQ空间 (**需要申请权限**)。 | 
| kOPEN_PERMISSION_ADD_ALBUM | 创建一个QQ空间相册 (**需要申请权限**)。 | 
| kOPEN_PERMISSION_UPLOAD_PIC |上传一张照片到QQ空间相册 (**需要申请权限**)。 | 
| kOPEN_PERMISSION_LIST_ALBUM |获取用户QQ空间相册列表 (**需要申请权限**)。 | 
| kOPEN_PERMISSION_ADD_SHARE |同步分享到QQ空间、腾讯微博。 | 
| kOPEN_PERMISSION_CHECK_PAGE_FANS |验证是否认证空间粉丝。 | 

## 实际示例
### 发送请求获取用户授权：

```
// 其中_tencentOAuth为TencentOAuth类的实例
NSArray* permissions = [NSArray arrayWithObjects:kOPEN_PERMISSION_GET_USER_INFO,
kOPEN_PERMISSION_GET_SIMPLE_USER_INFO,kOPEN_PERMISSION_ADD_SHARE,nil];
TencentOAuth *_tencentOAuth = [TencentOAuth initWithAppid:appid andDelegate:delegate];
[_tencentOAuth authorize:permissions inSafari:NO];
```
### 获取用户授权结果：

```
// 登录时权限信息的获得
- (NSArray *)getAuthorizedPermissions:(NSArray *)permissions
withExtraParams:(NSDictionary *)extraParams;
```
