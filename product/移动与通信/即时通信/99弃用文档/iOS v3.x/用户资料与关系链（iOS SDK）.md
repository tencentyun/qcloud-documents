云通信 IM 提供了用户资料托管，App 开发者使用简单的接口就可实现用户资料存储功能，另外，为了方便不同用户定制化资料，也提供用户资料的自定义字段。

## 用户资料介绍

用户资料保存用户的信息，比如昵称、头像等。

## 设置自己的资料

设置自己的资料通过`modifySelfProfile`方法完成
```
@interface TIMFriendshipManager : NSObject
/**
 *  设置自己的资料
 *
 *  @param values    需要更新的属性，可一次更新多个字段
 *  @param succ 成功回调
 *  @param fail 失败回调
 *
 *  @return 0 发送请求成功
 */
- (int)modifySelfProfile:(NSDictionary<NSString *, id> *)values succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```
通过values字典，可以一次设置多个字段。举例来说，设置昵称的代码如下：
```
[[TIMFriendshipManager sharedInstance] modifySelfProfile:@{TIMProfileTypeKey_Nick:@"我的昵称"} succ:nil fail:nil];
```

设置不存在的键值可能会导致失败，后台定义了一些常用的键值

Key | Value  | 说明
--- | --- | --
TIMProfileTypeKey_Nick | NSString | 昵称 
TIMProfileTypeKey_FaceUrl | NSString | 头像 
TIMProfileTypeKey_AllowType | NSNumber | 好友申请
TIMProfileTypeKey_Gender | NSNumber | 性别 
TIMProfileTypeKey_Birthday | NSNumber | 生日 
TIMProfileTypeKey_Location | NSString | 位置 
TIMProfileTypeKey_Language | NSNumber | 语言
TIMProfileTypeKey_Level | NSNumber | 等级 
TIMProfileTypeKey_Role | NSNumber | 角色 
TIMProfileTypeKey_SelfSignature | NSString | 签名 
TIMProfileTypeKey_Custom_Prefix | NSData,NSNumber, | 自定义字段前缀

自定义字段需要您加上我们的前缀。比如后台有一个自定义字段`Blood`，类型为整数，设置代码是
```
NSString *key = [TIMProfileTypeKey_Custom_Prefix stringByAppendingString:@"Blood"];
[[TIMFriendshipManager sharedInstance] modifySelfProfile:@{key:@1} succ:nil fail:nil];
```


## 获取资料

### 获取自己的资料 

可通过 `TIMFriendshipManager` 的 `getSelfProfile` 方法获取用户自己的资料。

**原型：**

```
/**
 *  用户资料
 */
@interface TIMUserProfile : TIMCodingModel

/**
 *  用户identifier
 */
@property(nonatomic,strong) NSString* identifier;

/**
 *  用户昵称
 */
@property(nonatomic,strong) NSString* nickname;

/**
 *  好友验证方式
 */
@property(nonatomic,assign) TIMFriendAllowType allowType;

/**
 * 用户头像
 */
@property(nonatomic,strong) NSString* faceURL;

/**
 *  用户签名
 */
@property(nonatomic,strong) NSData* selfSignature;

/**
 *  用户性别
 */
@property(nonatomic,assign) TIMGender gender;

/**
 *  用户生日
 */
@property(nonatomic,assign) uint32_t birthday;

/**
 *  用户区域
 */
@property(nonatomic,strong) NSData* location;

/**
 *  用户语言
 */
@property(nonatomic,assign) uint32_t language;

/**
 *  等级
 */
@property(nonatomic,assign) uint32_t level;

/**
 *  角色
 */
@property(nonatomic,assign) uint32_t role;

/**
 *  自定义字段集合,key是NSString类型,value是NSData类型或者NSNumber类型
 *  (key值按照后台配置的字符串传入)
 */
@property(nonatomic,strong) NSDictionary* customInfo;

@end
```

**参数说明：**

|参数 | 说明|
|--- | ---|
|succ | 成功回调，返回 TIMUserProfile 结构，包含用户资料 |
|fail | 失败回调，会返回错误码和错误信息，详见 [错误码](https://cloud.tencent.com/document/product/269/1671) |

**返回值：**

|返回 | 说明|
|--- | ---|
|0 | 表示发送数据成功 |
|非 0 | 表示发送数据失败|



### 获取好友的资料

可通过 `TIMFriendshipManager` 的 `getUsersProfile` 方法获取好友的资料。该方法支持从缓存和后台两种方式获取，当forceUpdate = YES时，会强制从后台拉取数据，并把返回的数据缓存下来；当forceUpdate = NO时，则先在本地查找，如果没有再向后台请求数据。建议只在显示资料的时候强制拉取，以减少等待时间。

**原型：**

```
/**
 *  获取指定好友资料
 *
 *  @param users 用户id
 *  @prarm forceUpdate 强制从后台拉取
 *  @param succ 成功回调
 *  @param fail 失败回调
 *
 *  @return 0 发送请求成功
 */
- (int)getUsersProfile:(NSArray<NSString *> *)users forceUpdate:(BOOL)forceUpdate succ:(TIMGetProfileArraySucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数 | 说明
--- | ---
users | 用户列表，NSString\* 数组 
forceUpdate | 强制从后台拉取
succ | 成功回调，返回 TIMUserProfile 数组，包含用户资料 
fail | 失败回调，会返回错误码和错误信息，详见错误码表 

**返回值：**

返回 | 说明
--- | ---
0 | 表示发送数据成功 
非 0 | 表示发送数据失败


示例中获取『iOS_002』和『iOS_003』两个用户的资料。 **示例：** 

```
NSMutableArray * arr = [[NSMutableArray alloc] init];
[arr addObject:@"iOS_002"];
[arr addObject:@"iOS_003"];
[[TIMFriendshipManager sharedInstance] getUsersProfile:arr forceUpdate:NO succ:^(NSArray * arr) {
	for (TIMUserProfile * profile in arr) {
		NSLog(@"user=%@", profile);
	}
}fail:^(int code, NSString * err) {
	NSLog(@"GetFriendsProfile fail: code=%d err=%@", code, err);
}];
```


缓存的时间可通过TIMFriendProfileOption设置，默认缓存时间一天。
```
/**
 * 资料与关系链
 */
@interface TIMFriendProfileOption : NSObject

/**
 * 关系链最大缓存时间
 * 默认缓存一天；获取资料和关系链超过缓存时间，将自动向服务器发起请求
 */
@property NSInteger expiredSeconds;

@end
```
设置的方法是 `-[TIMManager setUserConfig:]`，示例代码：
```
TIMUserConfig *config = ...;
TIMFriendProfileOption *option = [TIMFriendProfileOption new];
option.expiredSeconds = 60*60; //1小时
config.friendProfileOpt = option;
[[TIMManager sharedInstance] setUserConfig:config];
```
