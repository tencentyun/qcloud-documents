IM通讯云提供了关系链和用户资料托管，APP开发者使用简单的接口就可实现关系链和用户资料存储功能，另外，为了方便不通用户定制化资料，也提供用户资料和用户关系链的自定义字段（目前此功能为内测功能）。

本节所有的接口不论对独立帐号体系还是托管帐号体系都有有效。 

## 关系链资料介绍

用户关系链是指好友关系，通过接口可以实现加好友、解除好友、获取好友列表等操作。

用户资料保存用户的信息，比如昵称、头像等，另外，还有一种好友资料，只跟好友相关比如备注，分组等。

## 设置自己的资料

### 设置自己的昵称
 
可通过 TIMFriendshipManager的 SetNickname 方法设置用户自己的昵称，昵称最大为64字节： 

**原型： **

```
@interface TIMFriendshipManager : NSObject

/**
 *  设置自己的昵称
 *
 *  @param nick 昵称
 *  @param succ 成功回调
 *  @param fail 失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) SetNickname:(NSString*)nick succ:(TIMSucc)succ fail:(TIMFail)fail;

@end
```
**参数说明：**

参数  | 说明
--- | ---
nick | 要设置的昵称 
succ | 成功回调 
fail | 失败回调，会返回错误码和错误信息，详见错误码表 

**返回值：**

返回 | 说明
--- | ---
0  | 表示发送数据成功 
非0 |  表示发送数据失败 

**示例：**

```
NSString * nick = @"nickname";

[[TIMFriendshipManager sharedInstance] SetNickname:nick succ:^() {
	NSLog(@"SetNickname Succ");
} fail:^(int code, NSString * err) {
	NSLog(@"SetNickname fail: code=%d err=%@", code, err);
}];
```

此示例设置自己的昵称为`nickname`。

### 设置好友验证方式 

可通过 TIMFriendshipManager的 SetAllowType 方法设置好友验证方式，有以下几种验证方式：

- 任何人加好友
- 拒绝任何人加好友
- 需要验证三种方式

用户可根据需要设置其中一种：
 
**原型： **

```
typedef NS_ENUM(NSInteger, TIMFriendAllowType) {
    /**
     *  同意任何用户加好友
     */
    TIM_FRIEND_ALLOW_ANY                    = 0,
    
    /**
     *  拒绝任何人加好友
     */
    TIM_FRIEND_DENY_ANY                     = 1,
    
    /**
     *  需要验证
     */
    TIM_FRIEND_NEED_CONFIRM                 = 2,
};

@interface TIMFriendshipManager : NSObject

/**
 *  设置好友验证方式
 *
 *  @param allowType 好友验证方式，详见 TIMFriendAllowType
 *  @param succ 成功回调
 *  @param fail 失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) SetAllowType:(TIMFriendAllowType)allowType succ:(TIMSucc)succ fail:(TIMFail)fail;

@end
```
**参数说明：**

参数  | 说明
--- | ---
allowType | 好友验证方式，详见 TIMFriendAllowType： 
 | TIM_FRIEND_ALLOW_ANY : 同意任何用户加好友 
| TIM_FRIEND_DENY_ANY : 拒绝任何人加好友 
| TIM_FRIEND_NEED_CONFIRM : 需要验证 
succ | 成功回调 
fail | 失败回调，会返回错误码和错误信息，详见错误码表 

**返回值：**
 
返回 | 说明
--- | ---
0 | 表示发送数据成功 
非0 | 表示发送数据失败 

**示例：**

```
TIMFriendAllowType allowType = TIM_FRIEND_NEED_CONFIRM;

[[TIMFriendshipManager sharedInstance] SetAllowType:allowType succ:^() {
	NSLog(@"SetAllowType Succ");
} fail:^(int code, NSString * err) {
	NSLog(@"SetAllowType fail: code=%d err=%@", code, err);
}];
```

此示例中设置了自己的好友验证方式为需要验证，此时如果有用户申请加好友，会收到加好友的系统通知（详见 8.9. 关系链变更系统通知）。 

### 设置自己的头像
 
TIMFriendshipManager 的 SetFaceURL 方法设置用户自己的头像，当前 ImSDK 不会保存用户图片资源，需要用户上传图片到其他存储平台，通过 ImSDK 设置图片 URL： 

**原型：**

```
@interface TIMFriendshipManager : NSObject

/**
 *  设置自己的头像
 *
 *  @param faceURL 头像
 *  @param succ 成功回调
 *  @param fail 失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) SetFaceURL:(NSString*)faceURL succ:(TIMSucc)succ fail:(TIMFail)fail;

@end
```
**参数说明：**
 
参数 | 说明
--- | ---
faceURL | 要设置的头像 
succ | 成功回调 
fail | 失败回调，会返回错误码和错误信息，详见错误码表 

**返回值：**

返回 | 说明
--- | ---
0 | 表示发送数据成功 
非0 | 表示发送数据失败 

**示例：**

```
NSString * faceUrl = @"http://faceurl";

[[TIMFriendshipManager sharedInstance] SetFaceURL:faceUrl succ:^() {
	NSLog(@"SetFaceURL Succ");
} fail:^(int code, NSString * err) {
	NSLog(@"SetFaceURL fail: code=%d err=%@", code, err);
}];
```

### 设置自己的自定义字段

通过Server配置（内测功能）可以设置自己的自定义字段，通过自定义字段可以做到很多非内置功能，如用户性别、地址等字段。

**原型：**

```
@interface TIMFriendshipManager : NSObject

/**
 *  设置自定义属性
 *
 *  @param custom 自定义属性（NSString*,NSData*）
 *  @param succ   成功回调
 *  @param fail   失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) SetCustom:(NSDictionary*)custom succ:(TIMSucc)succ fail:(TIMFail)fail;

@end
```

**参数说明：**
 
参数 | 说明
--- | ---
custom | 自定义属性，字典类型 key 为`NSString*`， value为 `NSData*`
succ | 成功回调，返回 TIMUserProfile 结构，包含用户资料 
fail | 失败回调，会返回错误码和错误信息，详见错误码表 

**返回值：**

返回 | 说明
--- | ---
0 | 表示发送数据成功

## 获取资料

### 获取自己的资料 

可通过 TIMFriendshipManager 的 GetSelfProfile方法获取用户自己的资料： 

**原型：**

```
/**
 *  用户资料
 */
@interface TIMUserProfile : NSObject

/**
 *  用户identifier
 */
@property(nonatomic,retain) NSString* identifier;

/**
 *  用户昵称
 */
@property(nonatomic,retain) NSString* nickname;

/**
 *  用户备注（获取自己的资料时，该字段为空）
 */
@property(nonatomic,retain) NSString* remark;

/**
 *  好友验证方式
 */
@property(nonatomic,assign) TIMFriendAllowType allowType;

@end

@interface TIMFriendshipManager : NSObject

/**
 *  获取自己的资料
 *
 *  @param succ  成功回调，返回 TIMUserProfile
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) GetSelfProfile:(TIMGetProfileSucc)succ fail:(TIMFail)fail;

@end
```
**参数说明：**
 
参数 | 说明
--- | ---
succ | 成功回调，返回 TIMUserProfile 结构，包含用户资料 
fail | 失败回调，会返回错误码和错误信息，详见错误码表 

**返回值：**

返回 | 说明
--- | ---
0 | 表示发送数据成功 

**TIMUserProfile 属性说明：**

属性 | 说明
--- | ---
identifier | 自己的用户标识 
nickname | 自己的昵称 
remark | 为空，获取好友资料时有效 
allowType | 好友验证方式 

**示例：**

```
[[TIMFriendshipManager sharedInstance] GetSelfProfile:^(TIMUserProfile * profile) {
	NSLog(@"GetSelfProfile identifier=%@ nickname=%@ allowType=%d", profile.identifier, profile.nickname, profile.allowType);
} fail:^(int code, NSString * err) {
	NSLog(@"GetSelfProfile fail: code=%d err=%@", code, err);
}];
```


### 获取好友的资料
 
可通过 TIMFriendshipManager的 GetFriendsProfile 方法获取好友的资料： 

**原型：**

```
@interface TIMFriendshipManager : NSObject

/**
 *  获取好友资料
 *
 *  @param users 要获取的好友列表 NSString* 列表
 *  @param succ  成功回调，返回 TIMUserProfile* 列表
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) GetFriendsProfile:(NSArray*)users succ:(TIMFriendSucc)succ fail:(TIMFail)fail;

@end
```
**参数说明：**

参数 | 说明
--- | ---
users | 用户列表，NSString* 数组 
succ | 成功回调，返回 TIMUserProfile 数组，包含用户资料 
fail | 失败回调，会返回错误码和错误信息，详见错误码表 

**返回值：**

返回 | 说明
--- | ---
0 | 表示发送数据成功 

**TIMUserProfile 参数说明：** 

字段 | 说明
--- | ---
identifier | 好友的identifier 
nickname | 好友昵称 
remark | 好友备注 
allowType | 好友验证方式 

**示例：** 

```
NSMutableArray * arr = [[NSMutableArray alloc] init];

[arr addObject:@"iOS_002"];
[arr addObject:@"iOS_003"];

[[TIMFriendshipManager sharedInstance] GetFriendsProfile:arr succ:^(NSArray * arr) {
	for (TIMUserProfile * profile in arr) {
		NSLog(@"user=%@", profile);
	}
}fail:^(int code, NSString * err) {
	NSLog(@"GetFriendsProfile fail: code=%d err=%@", code, err);
}];
```
示例中获取@"iOS_002"和@"iOS_003"两个用户的资料。 

### 获取任何人的资料

1.9 以后版本可通过 TIMFriendshipManager的 GetUsersProfile 方法获取任何用户公开资料： 

**原型：**

```
@interface TIMFriendshipManager : NSObject

/**
 *  获取指定用户资料
 *
 *  @param users 要获取的用户列表 NSString* 列表
 *  @param succ  成功回调，返回 TIMUserProfile* 列表
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) GetUsersProfile:(NSArray*)users succ:(TIMFriendSucc)succ fail:(TIMFail)fail;

@end
```
**参数说明：**

参数 | 说明
--- | ---
users | 用户列表，NSString* 数组 
succ | 成功回调，返回 TIMUserProfile 数组，包含用户资料 
fail | 失败回调，会返回错误码和错误信息，详见错误码表 

**返回值：**

返回 | 说明
--- | ---
0 | 表示发送数据成功 

**TIMUserProfile 参数说明：** 

字段 | 说明
--- | ---
identifier | 好友的identifier 
nickname | 好友昵称 
remark | 好友备注 
allowType | 好友验证方式 

**示例：** 

```
NSMutableArray * arr = [[NSMutableArray alloc] init];

[arr addObject:@"iOS_002"];
[arr addObject:@"iOS_003"];

[[TIMFriendshipManager sharedInstance] GetUsersProfile:arr succ:^(NSArray * arr) {
	for (TIMUserProfile * profile in arr) {
		NSLog(@"user=%@", profile);
	}
}fail:^(int code, NSString * err) {
	NSLog(@"GetFriendsProfile fail: code=%d err=%@", code, err);
}];
```
示例中获取@"iOS_002"和@"iOS_003"两个用户的资料。 

### 按照字段获取好友资料

1.9 以后版本可以设置所需要拉取的资料字段，方便更灵活的获取资料。

**原型：**
```
@interface TIMFriendshipSetting : NSObject

/**
 *  需要获取的好友信息标志（TIMProfileFlag）
 */
@property(nonatomic,assign) uint64_t friendFlags;

/**
 *  需要获取的好友自定义信息（NSString*）列表
 */
@property(nonatomic,retain) NSArray * friendCustom;

/**
 *  需要获取的用户自定义信息（NSString*）列表
 */
@property(nonatomic,retain) NSArray * userCustom;

@end

@interface TIMManager : NSObject

/**
 *  设置TIMFriendshipManager和TIMFriendshipProxy默认拉取的字段（不设置：默认拉取所有基本字段，不拉取自定义字段）
 *
 *  @param setting 设置参数
 *
 *  @return 0 成功
 */
-(int) initFriendshipSetting:(TIMFriendshipSetting*)setting;

@end

```

**参数说明：**

参数|说明
---|---
setting|需要设置的配置：TIMFriendshipSetting
|friendFlags 要拉取的基本字段，按位设置，说明详见 friendFlags
|friendCustom 好友的自定义字段key列表
|userCustom 用户自定义字段key列表

## 关系链相关资料

### 好友备注
 
可通过 TIMFriendshipManager的 SetFriendRemark 方法设置好友备注： 

**原型：**

```
@interface TIMFriendshipManager : NSObject

/**
 *  设置好友备注
 *
 *  @param identifier 用户标识
 *  @param nick 备注
 *  @param succ 成功回调
 *  @param fail 失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) SetFriendRemark:(NSString*)identifier remark:(NSString*)remark succ:(TIMSucc)succ fail:(TIMFail)fail;

@end
```
**参数说明：**
 
参数 | 说明
--- | ---
identifier | 要设置备注的好友标识 
remark | 要设置的备注 
succ | 成功回调 
fail | 失败回调，会返回错误码和错误信息，详见错误码表 

**返回值：**

返回 | 说明
--- | ---
0 | 表示发送数据成功 
非0 | 表示发送数据失败 

**示例：** 

```
NSString * remark= @"002 remark";
NSString * identifier = @"iOS_002";

[[TIMFriendshipManager sharedInstance] SetFriendRemark:identifier remark:remark succ:^() {
	NSLog(@"SetFriendRemark Succ");
} fail:^(int code, NSString * err) {
	NSLog(@"SetFriendRemark fail: code=%d err=%@", code, err);
}];
```
示例中设置好友 @"iOS_002" 的备注为 @"002 remark"。 


### 设置好友自定义资料

通过Server配置（内测功能）可以设置自己的自定义字段，通过自定义字段可以做到很多非内置功能，如用户性别、地址等字段。

**原型：**

```
@interface TIMFriendshipManager : NSObject

/**
 *  设置好友自定义属性
 *
 *  @param identifier 用户标识
 *  @param custom     自定义属性（NSString*,NSData*）
 *  @param succ       成功回调
 *  @param fail       失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) SetFriendCustom:(NSString*)identifier custom:(NSDictionary*)custom succ:(TIMSucc)succ fail:(TIMFail)fail;

@end
```

**参数说明：**
 
参数 | 说明
--- | ---
identifier | 好设置的好友identifier
custom | 自定义属性，字典类型 key 为`NSString*`， value为 `NSData*`
succ | 成功回调，返回 TIMUserProfile 结构，包含用户资料 
fail | 失败回调，会返回错误码和错误信息，详见错误码表 

**返回值：**

返回 | 说明
--- | ---
0 | 表示发送数据成功

## 好友关系

### 添加好友
 
通过 TIMFriendshipManager的 AddFriend 方法可以批量添加好友，目前所能支持的最大好友列表为3000个： 

**原型：**

```
/**
 *  加好友请求
 */
@interface TIMAddFriendRequest : NSObject

/**
 *  用户identifier
 */
@property(nonatomic,retain) NSString* identifier;

/**
 *  用户备注，用户备注最大96字节
 */
@property(nonatomic,retain) NSString* remark;

/**
 *  请求说明（最大 120 字节）
 */
@property(nonatomic,retain) NSString* addWording;

/**
 *  添加来源
 */
@property(nonatomic,retain) NSString* addSource;

@end


@interface TIMFriendshipManager : NSObject

/**
 *  添加好友
 *
 *  @param users 要添加的用户列表 TIMAddFriendRequest* 列表
 *  @param succ  成功回调，返回 TIMFriendResult* 列表
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) AddFriend:(NSArray*) users succ:(TIMFriendSucc)succ fail:(TIMFail)fail;

@end
```
**参数说明：**

参数 | 说明
--- | ---
users | 用户列表，TIMAddFriendRequest* 数组 
succ | 成功回调，返回 TIMFriendResult*数组，包含用户添加结果 
fail | 失败回调，会返回错误码和错误信息，详见错误码表 

**返回值：**

返回 | 说明
--- | ---
0 | 表示发送数据成功 

**TIMAddFriendRequest 参数说明：**

字段 | 说明
--- | ---
identifier | 用户标识 
remark | 添加成功后给用户的备注信息，最大96字节 
addWording | 添加请求说明，最大 120 字节，如果用户设置为添加好友需要审核，对方会收到此信息并决定是否通过。 
addSource | 添加来源，固定字串，在页面上申请，留空表示未知来源 

**返回码说明：**
 
成功回调会返回操作用户的TIMFriendResult结果数据，添加好友的错误码如下： 

```
typedef NS_ENUM(NSInteger, TIMFriendStatus) {
    /**
     *  操作成功
     */
    TIM_FRIEND_STATUS_SUCC                              = 0,
    
    
    /**
     *  加好友时有效：被加好友在自己的黑名单中
     */
    TIM_ADD_FRIEND_STATUS_IN_SELF_BLACK_LIST                = 30515,
    
    /**
     *  加好友时有效：被加好友设置为禁止加好友
     */
    TIM_ADD_FRIEND_STATUS_FRIEND_SIDE_FORBID_ADD            = 30516,

    /**
     *  加好友时有效：好友数量已满
     */
    TIM_ADD_FRIEND_STATUS_SELF_FRIEND_FULL                  = 30519,
    
    /**
     *  加好友时有效：已经是好友
     */
    TIM_ADD_FRIEND_STATUS_ALREADY_FRIEND                    = 30520,
    
    /**
     *  加好友时有效：已被被添加好友设置为黑名单
     */
    TIM_ADD_FRIEND_STATUS_IN_OTHER_SIDE_BLACK_LIST          = 30525,
    
    /**
     *  加好友时有效：等待好友审核同意
     */
    TIM_ADD_FRIEND_STATUS_PENDING                           = 30539,
};
```
开发者可根据对应情况提示用户。 

**示例：**

```
NSMutableArray * users = [[NSMutableArray alloc] init];

TIMAddFriendRequest* req = [[TIMAddFriendRequestalloc] init];

// 添加好友 iOS_002
req.identifier = [NSString stringWithUTF8String:"iOS_002"];
// 添加备注 002Remark
req.remark = [NSString stringWithUTF8String:"002Remark"];
// 添加理由
req.addWording = [NSString stringWithUTF8String:"i am 002"];

[users addObject:req];

[[TIMFriendshipManager sharedInstance] AddFriend:users succ:^(NSArray * arr) {
	for (TIMFriendResult * res in arr) {
		if (res.status != TIM_FRIEND_STATUS_SUCC) {
			NSLog(@"AddFriend failed: user=%@ status=%d", res.identifier, res.status);
		}
		else {
			NSLog(@"AddFriend succ: user=%@ status=%d", res.identifier, res.status);
		}
	}
} fail:^(int code, NSString * err) {
	NSLog(@"add friend fail: code=%d err=%@", code, err);
}];
```

### 删除好友
 
可通过 TIMFriendshipManager的 DelFriend 方法可以批量删除好友： 

**原型：**

```
@interface TIMFriendshipManager : NSObject

/**
 *  删除好友
 *
 *  @param delType 删除类型（单向好友、双向好友）
 *  @param users 要删除的用户列表 NSString* 列表
 *  @param succ  成功回调，返回 TIMFriendResult* 列表
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) DelFriend:(TIMDelFriendType)delType users:(NSArray*) users succ:(TIMFriendSucc)succ fail:(TIMFail)fail;

@end
```
**参数说明：**

参数 | 说明
--- | ---
delType | 删除类型，可选择删除双向好友或者单向好友 
users | 要删除的用户列表 NSString* 列表 
succ | 成功回调，返回 TIMFriendResult*数组，包含用户添加结果 
fail | 失败回调，会返回错误码和错误信息，详见错误码表 

**返回值：**

返回 | 说明
--- | ---
0 | 表示发送数据成功 

**返回码说明**：
 
成功回调会返回操作用户的TIMFriendResult结果数据，删除好友的错误码如下： 

```
typedef NS_ENUM(NSInteger, TIMFriendStatus) {
    /**
     *  操作成功
     */
    TIM_FRIEND_STATUS_SUCC                              = 0,
    

    /**
     *  删除好友时有效：删除好友时对方不是好友
     */
    TIM_DEL_FRIEND_STATUS_NO_FRIEND                         = 31704,
};
```
开发者可根据情况提示用户。 

**示例：**

```
NSMutableArray * del_users = [[NSMutableArray alloc] init];

// 删除好友 iOS_002
[del_users addObject:@"iOS_002"];

// TIM_FRIEND_DEL_BOTH 指定删除双向好友
[[TIMFriendshipManager sharedInstance] DelFriend: TIM_FRIEND_DEL_BOTH users:del_users succ:^(NSArray* arr) {
	for (TIMFriendResult * res in arr) {
		if (res.status != TIM_FRIEND_STATUS_SUCC) {
			NSLog(@"DelFriend failed: user=%@ status=%d", res.identifier, res.status);
		}
		else {
			NSLog(@"DelFriend succ: user=%@ status=%d", res.identifier, res.status);
		}
	}
} fail:^(int code, NSString * err) {
	NSLog(@"DelFriend failed: code=%d err=%@", code, err);
}];
```

### 获取所有好友
 
可通过 TIMFriendshipManager的 GetFriendList 方法可以获取所有好友： 

**原型：**

```
@interface TIMFriendshipManager : NSObject

/**
 *  获取好友列表
 *
 *  @param succ 成功回调，返回好友列表，TIMUserProfile* 列表，只包含identifier，nickname，remark 三个字段
 *  @param fail 失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) GetFriendList:(TIMFriendSucc)succ fail:(TIMFail)fail;

@end
```
**参数说明：**

参数 | 说明
--- | ---
succ | 成功回调，返回好友列表，TIMUserProfile* 列表，只包含identifier，nickname，remark 三个字段 
fail | 失败回调，会返回错误码和错误信息，详见错误码表 

**返回值：**

返回 | 说明
--- | ---
0 | 表示发送数据成功 

**TIMUserProfile 参数说明：**

字段 | 说明
--- | ---
identifier | 自己的用户标识 
nickname | 自己的昵称 
remark | 用户备注 

其他字段需要通过拉取好友的详细资料获得。 

**示例：**

```
[[TIMFriendshipManager sharedInstance] GetFriendList:^(NSArray * arr) {
	for (TIMUserProfile * profile in arr) {
		NSLog(@"friend: %@", profile.identifier);
	}
}fail:^(int code, NSString * err) {
	NSLog(@"GetFriendList fail: code=%d err=%@", code, err);;
}];
```

### 同意/拒绝 好友申请
 
可通过 TIMFriendshipManager的 DoResponse方法可以获取所有好友： 

**原型：**

```
typedef NS_ENUM(NSInteger, TIMFriendResponseType) {
    /**
     *  同意加好友（建立单向好友）
     */
    TIM_FRIEND_RESPONSE_AGREE                       = 0,
    
    /**
     *  同意加好友并加对方为好友（建立双向好友）
     */
    TIM_FRIEND_RESPONSE_AGREE_AND_ADD               = 1,
    
    /**
     *  拒绝对方好友请求
     */
    TIM_FRIEND_RESPONSE_REJECT                      = 2,
};

@interface TIMFriendResponse : NSObject

/**
 *  响应类型
 */
@property(nonatomic,assign) TIMFriendResponseType responseType;

/**
 *  用户identifier
 */
@property(nonatomic,retain) NSString* identifier;

/**
 *  （可选）如果要加对方为好友，表示备注，其他type无效
 */
@property(nonatomic,retain) NSString* remark;

@end

@interface TIMFriendshipManager : NSObject

/**
 *  响应对方好友邀请
 *
 *  @param users     响应的用户列表，TIMFriendResponse列表
 *  @param succ      成功回调，返回 TIMFriendResult* 列表
 *  @param fail      失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) DoResponse:(NSArray*)users succ:(TIMFriendSucc)succ fail:(TIMFail)fail;

@end
```
**参数说明：**

users    响应的用户列表，TIMFriendResponse列表 
succ    成功回调，返回 TIMFriendResult* 列表 
fail     失败回调，会返回错误码和错误信息，详见错误码表 

**返回值：**
 
0 表示发送数据成功 

**返回码说明：**
 
成功回调会返回操作用户的TIMFriendResult结果数据，处理用户请求的错误码如下： 
```
typedef NS_ENUM(NSInteger, TIMFriendStatus) {
    /**
     *  操作成功
     */
    TIM_FRIEND_STATUS_SUCC                              = 0,
   
    /**
     *  响应好友申请时有效：对方没有申请过好友
     */
    TIM_RESPONSE_FRIEND_STATUS_NO_REQ                       = 30614,
    
    /**
     *  响应好友申请时有效：自己的好友满
     */
    TIM_RESPONSE_FRIEND_STATUS_SELF_FRIEND_FULL             = 30615,
    
    /**
     *  响应好友申请时有效：好友已经存在
     */
    TIM_RESPONSE_FRIEND_STATUS_FRIEND_EXIST                 = 30617,
    
    /**
     *  响应好友申请时有效：对方好友满
     */
    TIM_RESPONSE_FRIEND_STATUS_OTHER_SIDE_FRIEND_FULL       = 30630,
};
```
开发者可根据情况提示用户。 


### 添加用户到黑名单

可以把任意用户拉黑，如果此前是好友关系，拉黑后自动解除好友，拉黑后对方发消息无法收到。

**原型：**
```
@interface TIMFriendshipManager : NSObject

/**
 *  添加用户到黑名单
 *
 *  @param users 用户列表
 *  @param succ  成功回调，返回 TIMFriendResult* 列表
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) AddBlackList:(NSArray*) users succ:(TIMFriendSucc)succ fail:(TIMFail)fail;

@end
```

**参数说明：**

参数 | 说明
--- | ---
users | 要拉黑的用户identifier列表
succ | 成功回调
fail | 失败回调

**返回值：**

返回 | 说明
--- | ---
0 | 发送请求成功

### 把用户从黑名单删除

**原型：**
```
@interface TIMFriendshipManager : NSObject

/**
 *  把用户从黑名单中删除
 *
 *  @param users 用户列表
 *  @param succ  成功回调，返回 TIMFriendResult* 列表
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) DelBlackList:(NSArray*) users succ:(TIMFriendSucc)succ fail:(TIMFail)fail;

@end
```

**参数说明：**

参数 | 说明
--- | ---
users | 要从黑名单删除的用户identifier列表
succ | 成功回调
fail | 失败回调

**返回值：**

返回 | 说明
--- | ---
0 | 发送请求成功

### 获取黑名单列表

**原型：**
```
@interface TIMFriendshipManager : NSObject

/**
 *  获取黑名单列表
 *
 *  @param succ 成功回调，返回NSString*列表
 *  @param fail 失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) GetBlackList:(TIMFriendSucc)succ fail:(TIMFail)fail;

@end
```

**参数说明：**

参数 | 说明
--- | ---
succ | 成功回调，返回`NSString*`类型，为黑名单列表
fail | 失败回调

**返回值：**

返回 | 说明
--- | ---
0 | 发送请求成功

## 好友分组

### 创建好友分组

创建分组时，可以同时指定添加的用户，同一用户可以添加到多个分组。

**原型：**
```
@interface TIMFriendshipManager : NSObject

/**
 *  新建好友分组
 *
 *  @param groupNames  分组名称列表,必须是当前不存在的分组
 *  @param users       要添加到分组中的好友列表
 *  @param succ  成功回调，返回 TIMFriendResult* 列表
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) CreateFriendGroup:(NSArray*)groupNames users:(NSArray*)users succ:(TIMFriendSucc)succ fail:(TIMFail)fail;

@end
```

**参数说明：**

参数 | 说明
--- | ---
groupNames | 分组名称，必须是不存在的分组
users | 要添加分组中的用户列表
succ | 成功回调
fail | 失败回调

**返回值：**

返回 | 说明
--- | ---
0 | 发送请求成功

### 删除好友分组

**原型：**
```
@interface TIMFriendshipManager : NSObject

/**
 *  删除好友分组
 *
 *  @param groupNames  要删除的好友分组名称列表
 *  @param succ  成功回调
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) DeleteFriendGroup:(NSArray*)groupNames succ:(TIMSucc)succ fail:(TIMFail)fail;

@end
```

**参数说明：**

参数 | 说明
--- | ---
groupNames | 要删除的分组名称
succ | 成功回调
fail | 失败回调

**返回值：**

返回 | 说明
--- | ---
0 | 发送请求成功

### 添加好友到某分组

**原型：**
```
@interface TIMFriendshipManager : NSObject

/**
 *  添加好友到一个好友分组
 *
 *  @param groupName   好友分组名称
 *  @param users       要添加到分组中的好友列表
 *  @param succ  成功回调，返回 TIMFriendResult* 列表
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) AddFriendsToFriendGroup:(NSString*)groupName users:(NSArray*)users succ:(TIMFriendSucc)succ fail:(TIMFail)fail;

@end
```

**参数说明：**

参数 | 说明
--- | ---
groupName | 分组名称
users |  要添加到分组中的好友列表
succ | 成功回调
fail | 失败回调

**返回值：**

返回 | 说明
--- | ---
0 | 发送请求成功

### 从某分组删除好友

**原型：**
```
@interface TIMFriendshipManager : NSObject

/**
 *  从好友分组中删除好友
 *
 *  @param groupName   好友分组名称
 *  @param users       要移出分组的好友列表
 *  @param succ  成功回调，返回 TIMFriendResult* 列表
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) DelFriendsFromFriendGroup:(NSString*)groupName users:(NSArray*)users succ:(TIMFriendSucc)succ fail:(TIMFail)fail;

@end
```

**参数说明：**

参数 | 说明
--- | ---
groupName | 分组名称
users |  要从分组删除的好友列表
succ | 成功回调
fail | 失败回调

**返回值：**

返回 | 说明
--- | ---
0 | 发送请求成功

### 重命名好友分组

**原型：**
```
@interface TIMFriendshipManager : NSObject

/**
 *  修改好友分组的名称
 *
 *  @param oldName   原来的分组名称
 *  @param newName   新的分组名称
 *  @param succ  成功回调
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) RenameFriendGroup:(NSString*)oldName newName:(NSString*)newName succ:(TIMSucc)succ fail:(TIMFail)fail;

@end
```

**参数说明：**

参数 | 说明
--- | ---
oldName | 旧分组名称
newName |  新分组名称
succ | 成功回调
fail | 失败回调

**返回值：**

返回 | 说明
--- | ---
0 | 发送请求成功

### 获取指定的好友分组信息

**原型：**
```
@interface TIMFriendshipManager : NSObject

/**
 *  获取指定的好友分组信息
 *
 *  @param groupNames      要获取信息的好友分组名称列表,传入nil获得所有分组信息
 *  @param succ  成功回调，返回 TIMFriendGroup* 列表
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) GetFriendGroups:(NSArray*)groupNames succ:(TIMFriendGroupSucc)succ fail:(TIMFail)fail;

@end
```

**参数说明：**

参数 | 说明
--- | ---
groupNames | 要获取的分组好友名称，传入nil获取所有分组信息
succ | 成功回调
fail | 失败回调

**返回值：**

返回 | 说明
--- | ---
0 | 发送请求成功

### 获取所有好友分组

通过 [6.6 获取指定的好友分组信息](#.E8.8E.B7.E5.8F.96.E6.8C.87.E5.AE.9A.E7.9A.84.E5.A5.BD.E5.8F.8B.E5.88.86.E7.BB.84.E4.BF.A1.E6.81.AF) 可以获取所有分组信息，另外，通过 [5.3 获取所有好友](#.E8.8E.B7.E5.8F.96.E6.89.80.E6.9C.89.E5.A5.BD.E5.8F.8B)，也可以获取分组信息。

## 关系链变更系统通知
 
TIMMessage中Elem类型 TIMSNSSystemElem 为关系链变更系统消息： 

**原型：**

```
typedef NS_ENUM(NSInteger, TIM_SNS_SYSTEM_TYPE){
    /**
     *  增加好友消息
     */
    TIM_SNS_SYSTEM_ADD_FRIEND                           = 0x01,
    /**
     *  删除好友消息
     */
    TIM_SNS_SYSTEM_DEL_FRIEND                           = 0x02,
    /**
     *  增加好友申请
     */
    TIM_SNS_SYSTEM_ADD_FRIEND_REQ                       = 0x03,
    /**
     *  删除未决申请
     */
    TIM_SNS_SYSTEM_DEL_FRIEND_REQ                       = 0x04,
};


/**
 *  关系链变更详细信息
 */
@interface TIMSNSChangeInfo : NSObject

/**
 *  用户 identifier
 */
@property(nonatomic,retain) NSString * identifier;

/**
 *  申请添加时有效，添加理由
 */
@property(nonatomic,retain) NSString * wording;

/**
 *  申请时填写，添加来源
 */
@property(nonatomic,retain) NSString * source;

@end


/**
 *  关系链变更消息
 */
@interface TIMSNSSystemElem : TIMElem

/**
 * 操作类型
 */
@property(nonatomic,assign) TIM_SNS_SYSTEM_TYPE type;

/**
 * 被操作用户列表：TIMSNSChangeInfo 列表
 */
@property(nonatomic,retain) NSArray * users;

@end
```
**成员说明：**

成员 | 说明
--- | ---
type | 变更类型 
users | 变更的用户列表 

**示例：**

```
@interface TIMMessageListenerImpl : NSObject- (void)onNewMessage:(NSArray*) msgs;
@end

@implementation TIMMessageListenerImpl
- (void)onNewMessage:(NSArray*) msgs {
    for (TIMMessage * msg in msgs) {
		for (int i = 0; i < [msg elemCount]; i++) {
            TIMElem * elem = [msg getElem:i];
            if ([elem isKindOfClass:[TIMSNSSystemElem class]]) {
                TIMSNSSystemElem * system_elem = (TIMSNSSystemElem * )elem;
                switch ([system_elem type]) {
                    case TIM_SNS_SYSTEM_ADD_FRIEND:
                        for (TIMSNSChangeInfo * info in [system_elem users]) {
                            NSLog(@"user %@ become friends", [info identifier]);
                        }
                        break;
                    case TIM_SNS_SYSTEM_DEL_FRIEND:
                        for (TIMSNSChangeInfo * info in [system_elem users]) {
                            NSLog(@"user %@ delete friends", [info identifier]);
                        }
                        break;
                    case TIM_SNS_SYSTEM_ADD_FRIEND_REQ:
                        for (TIMSNSChangeInfo * info in [system_elem users]) {
                            NSLog(@"user %@ request friends: reason=%@", [info identifier], [info wording]);
                        }
                        break;
                    default:
                        NSLog(@"ignore type");
                        break;
                }
            }
        }
    }
}
@end

TIMMessageListenerImpl * impl = [[TIMMessageListenerImpl alloc] init];

[[TIMManager sharedInstance] setMessageListener:impl];

[[TIMManager sharedInstance] initSdk];

TIMLoginParam * login_param = [[TIMLoginParam alloc ]init];

login_param.accountType = @"107";
login_param.identifier = @"iOS_001";
login_param.userSig = @"";
login_param.appidAt3rd = @"123456";
login_param.sdkAppId = 123456;

[[TIMManager sharedInstance] login: login_param succ:^(){
 NSLog(@"login succ");
} fail:^(int code, NSString * err) {
 NSLog(@"login failed: %d->%@", code, err);
}];
```
示例中，当成为好友或者解除好友关系时，打印日志，当有用户申请成为好友时，打印申请理由。 

### 添加好友系统通知
 
当两个用户成为好友时，两个用户均可收到添加好友系统消息： 

**触发时机：**
 
当自己的关系链变更，增加好友时，收到消息（如果已经是单向好友，关系链没有变更的一方不会收到） 

**参数说明：**
 
参数 | 说明
--- | ---
type | TIM_SNS_SYSTEM_ADD_FRIEND 
users | 成为好友的用户列表 

**TIMSNSChangeInfo 参数说明：**
 
成员 | 说明
--- | ---
identifier | 用户identifier 

### 删除好友系统通知
 
当两个用户解除好友关系时，会收到删除好友系统消息： 

**触发时机：**
 
当自己的关系链变更，删除好友时，收到消息（如果删除的是单向好友，关系链没有变更的一方不会收到） 

**参数说明：**

参数 | 说明
type | TIM_SNS_SYSTEM_DEL_FRIEND 
users | 删除好友的用户列表 

**TIMSNSChangeInfo 参数说明：**
 
成员 | 说明
--- | ---
identifier |  用户identifier 

### 好友申请系统通知
 
当申请好友时对方需要验证，自己和对方会收到好友申请系统通知： 

**触发时机：**
 
当申请好友时对方需要验证，自己和对方会收到好友申请系统通知，对方可选择同意或者拒绝，自己不能操作，只做信息同步之用。 

**参数说明：**
 
参数 | 说明
--- | ---
type | TIM_SNS_SYSTEM_ADD_FRIEND_REQ 
users | 申请的好友列表 

**TIMSNSChangeInfo 参数说明：**

参数 | 说明
--- | ---
identifier |  用户identifier 
wording |  申请理由 
source | 申请来源，申请时填写，由系统页面分配的固定字串 

### 删除未决请求通知
 
**触发时机：**
 
当申请对方为好友，申请审核通过后，自己会收到删除未决请求消息，表示之前的申请已经通过。 

**参数说明：**
 
参数|说明
---|---
type | TIM_SNS_SYSTEM_DEL_FRIEND_REQ 
users | 删除未决请求的好友列表 

**TIMSNSChangeInfo 参数说明：**
 
参数 | 说明
--- | ---
identifier |  用户identifier 

## 好友资料变更系统通知
 
TIMMessage中Elem类型 TIMProfileSystemElem 为关系链变更系统消息： 

**原型：**

```
typedef NS_ENUM(NSInteger, TIM_PROFILE_SYSTEM_TYPE){
    /**
     *  好友资料变更
     */
    TIM_PROFILE_SYSTEM_FRIEND_PROFILE_CHANGE        = 0x01,
};

/**
 *  资料变更系统消息
 */
@interface TIMProfileSystemElem : NSObject

/**
 *  变更类型
 */
@property(nonatomic,assign) TIM_PROFILE_SYSTEM_TYPE type;

/**
 *  资料变更的用户
 */
@property(nonatomic,retain) NSString * fromUser;

/**
 *  资料变更的昵称（如果昵称没有变更，该值为nil）
 */
@property(nonatomic,retain) NSString * nickName;

@end
```
**成员说明：**

成员  | 说明
--- | ---
type | 资料变更类型 
fromUser|  资料变更的用户 
nickName | 昵称变更，注意，如果昵称没有变更，为nil 

## 昵称检索 

ImSDK支持使用昵称搜索用户，使用SearchUser实现。 

**原型：**

```
/**
 *  按昵称信息搜索用户资料
 *
 *  @param nickName    用户名称内容
 *  @param pageIndex   分页号
 *  @param pageSize    每页用户数目
 *  @param succ  成功回调，返回 TIMUserProfile* 列表
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) SearchUser:(NSString*)nickName pageIndex:(uint64_t)pageIndex pageSize:(uint64_t)pageSize succ:(TIMUserSearchSucc)succ fail:(TIMFail)fail;
```
**参数说明：**

参数 | 说明
--- | ---
nickName  | 要搜索的昵称关键字 
pageIndex  |  分页号，从0开始 
pageSize      | 每页的数量 
succ            | 成功回调，返回搜索结果 
fail              | 失败回调 

**示例： **

```
[[TIMFriendshipManager sharedInstance] SearchUser:@"test" pageIndex:0 pageSize:10 succ:^(uint64_t totalNum, NSArray * users) {
    NSLog(@"total num=%llu", totalNum);
    NSLog(@"users=%@", users);
} fail:^(int code, NSString * msg) {
    NSLog(@"SearchUser failed: code=%d, err=%@", code, msg);
}];
```

示例中检索名称中包含@"test"的用户列表。 


## 未决请求

未决请求即为等待处理的请求，比如设置了需要验证好友，对方申请时会有未决请求，如果同意或者拒绝这个申请，未决请求会变为已决。

通过 TIMFriendshipManager 的 GetFutureFriends 方法可以从Server获取未决请求列表。

**原型：***

```
@interface TIMFriendshipManager : NSObject

/**
 *  未决请求和好友推荐拉取
 *
 *  @param flags        获取的资料标识
 *  @param futureFlag   获取的类型，按位设置
 *  @param custom       自定义字段，（尚未实现，填nil）
 *  @param meta         请求信息，参见TIMFriendFutureMeta
 *  @param succ  成功回调
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
-(int) GetFutureFriends:(TIMProfileFlag)flags futureFlag:(TIMFutureFriendType)futureFlag custom:(NSArray*)custom meta:(TIMFriendFutureMeta*)meta succ:(TIMGetFriendFutureListSucc)succ fail:(TIMFail)fail;

@end
```

**参数说明：**

参数|说明
---|---
flags | 获取的资料标志，详见TIMProfileFlag
futureFlag | 获取的未决标记，如未决，已决，推荐等类型
custom | 自定义字段，如要获取填写
meta | 请求信息，参见 TIMFriendFutureMeta 定义
succ | 成功回调
fail | 失败回调


