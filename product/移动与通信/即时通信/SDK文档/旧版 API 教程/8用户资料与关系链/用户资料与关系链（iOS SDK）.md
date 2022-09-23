即时通信 IM 提供了关系链和用户资料托管，App 开发者使用简单的接口就可实现关系链和用户资料存储功能，另外，为了方便不同用户定制化资料，也提供用户资料和用户关系链的自定义字段（用户自定义字段需要先在控制台配置，详情请参考 [用户自定义字段](https://cloud.tencent.com/document/product/269/38656#.E7.94.A8.E6.88.B7.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5)）。本节所有的接口不论对独立帐号体系还是托管帐号体系都有效。 


## 用户资料

### 获取自己的资料 

可通过 `TIMFriendshipManager` 的 `getSelfProfile` 方法获取用户自己的资料。

```
/**
 *  获取自己的资料
 *
 *  @param succ  成功回调，返回 TIMUserProfile
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
- (int)getSelfProfile:(TIMGetProfileSucc)succ fail:(TIMFail)fail;
```

如果获取成功，succ 回调会返回获取到的`TIMUserProfile`对象。`TIMUserProfile`的定义如下：

```
/**
 *  用户资料
 */
@interface TIMUserProfile : TIMCodingModel

/**
 *  用户 identifier
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
 *  自定义字段集合,key 是 NSString 类型,value 是 NSData 类型或者 NSNumber 类型
 *  (key 值按照后台配置的字符串传入)
 */
@property(nonatomic,strong) NSDictionary* customInfo;

@end
```



### 获取指定用户的资料

可通过 `TIMFriendshipManager` 的 `getUsersProfile` 方法获取指定用户的资料。该方法支持从缓存和后台两种方式获取，当 forceUpdate = YES 时，会强制从后台拉取数据，并把返回的数据缓存下来；当 forceUpdate = NO 时，则先在本地查找，如果没有再向后台请求数据。建议只在显示资料的时候强制拉取，以减少等待时间。


```
/**
 *  获取指定好友资料
 *
 *  @param users 用户 ID
 *  @prarm forceUpdate 强制从后台拉取
 *  @param succ 成功回调
 *  @param fail 失败回调
 *
 *  @return 0 发送请求成功
 */
- (int)getUsersProfile:(NSArray<NSString *> *)users forceUpdate:(BOOL)forceUpdate succ:(TIMGetProfileArraySucc)succ fail:(TIMFail)fail;
@end
```

示例：获取『iOS_002』和『iOS_003』两个用户的资料

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

该示例关闭了强制后台拉取，优先从缓存中查找用户资料，可减少等待时间。缓存的时间可通过 TIMFriendProfileOption 设置，默认缓存时间一天。
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
设置的过期时间方法是 `-[TIMManager setUserConfig:]`，示例代码：
```
TIMUserConfig *config = ...;
TIMFriendProfileOption *option = [TIMFriendProfileOption new];
option.expiredSeconds = 60*60; //1小时
config.friendProfileOpt = option;
[[TIMManager sharedInstance] setUserConfig:config];
```

### 修改自己的资料

修改自己的资料通过`modifySelfProfile`方法完成
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
通过 values 字典，可以一次设置多个字段。举例来说，设置昵称的代码如下：
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
TIMProfileTypeKey_Custom_Prefix | NSString、NSData 或 NSNumber | 自定义字段前缀

自定义字段需要您加上我们的前缀。例如后台有一个自定义字段`Blood`，类型为整数，设置代码是
```
NSString *key = [TIMProfileTypeKey_Custom_Prefix stringByAppendingString:@"Blood"];
[[TIMFriendshipManager sharedInstance] modifySelfProfile:@{key:@1} succ:nil fail:nil];
```
>?当设置自定义字段值是 NSString 对象时，后台会将其转为 UTF8 保存在数据库中。由于部分用户迁移资料时可能不是 UTF8 类型，所以在获取资料时，统一返回 NSData 类型。

## 好友关系

### 获取所有好友

可通过 `TIMFriendshipManager` 的 `getFriendList` 方法获取所有好友列表

```
@interface TIMFriendshipManager : NSObject
/**
 *  获取好友列表
 *
 *  @param succ 成功回调，返回好友(TIMFriend)列表 
 *  @param fail 失败回调
 *
 *  @return 0 发送请求成功
 */
-(int)getFriendList:(TIMFriendArraySucc)succ fail:(TIMFail)fail;
@end
```

如果获取成功，succ 回调返回好友列表。好友对象用`TIMFriend`存储，`TIMFriend`的定义如下

```
@interface TIMFriend : TIMCodingModel

/**
 *  好友 identifier
 */
@property(nonatomic,strong) NSString *identifier;

/**
 *  好友备注
 */
@property(nonatomic,strong) NSString *remark;

/**
 *  分组名称 NSString* 列表
 */
@property(nonatomic,strong) NSArray *groups;

/**
 *  申请理由
 */
@property(nonatomic,strong) NSString * addWording;

/**
 *  申请来源
 */
@property(nonatomic,strong) NSString * addSource;

/**
 * 添加时间
 */
@property(nonatomic,assign) uint64_t addTime;

/**
 * 自定义字段集合,key 是 NSString 类型,value 是 NSData 类型或者 NSNumber 类型(key 值按照后台配置的字符串传入)
 */
@property(nonatomic,strong) NSDictionary* customInfo;

/**
 * 好友资料
 */
@property(nonatomic,strong) TIMUserProfile *profile;

@end
```

示例代码
```
[[TIMFriendshipManager sharedInstance] getFriendList:^(NSArray<TIMFriend *> *friends) {
    NSMutableString *msg = [NSMutableString new];
    [msg appendString:@"好友列表: "];
    for (TIMFriend *friend in friends) {
        [msg appendFormat:@"[%@,%@,%d,%@,%@,%@]", friend.identifier, friend.remark, friend.addTime, friend.addSource, friend.addWording, friend.groups];
    }
    self.msgLabel.text = msg;
} fail:^(int code, NSString *msg) {
    self.msgLabel.text = [NSString stringWithFormat:@"失败：%d, %@", code, msg];
}];
```

### 修改好友

修改好友调用`modifyFriend`方法进行。与修改自己资料方法类似，该方法通过传入字典方式修改，可一次更新多个字段。


```
@interface TIMFriendshipManager : NSObject
/**
 *  修改好友
 *
 *  @param identifier 好友的 identifier
 *  @param values  需要更新的属性，可一次更新多个字段. 参见 TIMFriendshipDefine.h 的 TIMFriendTypeKey_XXX
 *  @param succ 成功回调
 *  @param fail 失败回调
 *
 *  @return 0 发送请求成功
 */
- (int)modifyFriend:(NSString *)identifier values:(NSDictionary<NSString *, id> *)values succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

设置不存在的键值可能会导致失败，后台定义了一些常用的键值

Key | Value  | 说明
--- | --- | --
TIMFriendTypeKey_Remark | NSString | 备注 
TIMFriendTypeKey_Group | NSArray | 分组 
TIMFriendTypeKey_Custom_Prefix | NSNumber、NSData | 自定义字段前缀


示例：设置好友『iOS_002』的备注为『002 remark』 

```
[[TIMFriendshipManager sharedInstance] modifyFriend:@"iOS_002" values:@{ TIMFriendTypeKey_Remark: @"002 remark"} succ:^{
    self.msgLabel.text = @"OK";
} fail:^(int code, NSString *msg) {
    self.msgLabel.text = [NSString stringWithFormat:@"失败：%d, %@", code, msg];
}];
```

> 修改好友自定义资料，需先通过 Server 配置关系链自定义字段，才能修改成功。


### 添加好友

通过 `TIMFriendshipManager` 的 `addFriend` 方法可以添加好友。 

```
@interface TIMFriendshipManager : NSObject

/**
 *  添加好友
 *
 *  @param request 添加好友请求
 *  @param succ  成功回调(TIMFriendResult)
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
- (int)addFriend:(TIMFriendRequest *)request succ:(TIMFriendResultSucc)succ fail:(TIMFail)fail;

@end
```

加好友需要传入 request 参数，该参数类型定义如下：
```
/**
 *  加好友请求
 */
@interface TIMFriendRequest : TIMCodingModel

/**
 *  用户 identifier
 */
@property(nonatomic,strong) NSString* identifier;

/**
 *  用户备注（备注最大96字节）
 */
@property(nonatomic,strong) NSString* remark;

/**
 *  请求说明（最大120字节）
 */
@property(nonatomic,strong) NSString* addWording;

/**
 *  添加来源
 *  来源不能超过8个字节，并且需要添加“AddSource_Type_”前缀
 */
@property(nonatomic,strong) NSString* addSource;

/**
 *  分组名
 */
@property(nonatomic,strong) NSString* group;

@end
```


成功回调会返回操作用户的 `TIMFriendResult` 结果数据，开发者可根据对应情况提示用户。添加好友的返回码如下。

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
     *  加好友、响应好友时有效：自己的好友数已达系统上限
     */
    TIM_ADD_FRIEND_STATUS_SELF_FRIEND_FULL                  = 30010,     
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

示例代码

```
TIMFriendRequest *q = [TIMFriendRequest new];
q.identifier = @"abc"; // 加好友 abc
q.addWording = @"求通过";
q.addSource = @"AddSource_Type_iOS";
q.remark = @"你是abc";
[[TIMFriendshipManager sharedInstance] addFriend:q succ:^(TIMFriendResult *result) {
    if (result.result_code == 0)
        self.msgLabel.text = @"添加成功";
    else
        self.msgLabel.text = [NSString stringWithFormat:@"异常：%ld, %@", (long)result.result_code, result.result_info];
} fail:^(int code, NSString *msg) {
    self.msgLabel.text = [NSString stringWithFormat:@"失败：%d, %@", code, msg];
}];
```

### 删除好友

可通过 `TIMFriendshipManager` 的 `deleteFriends` 方法批量删除好友。 

```
@interface TIMFriendshipManager : NSObject
/**
 *  删除好友
 *
 *  @param user 要删除的好友的 identifier
 *  @param delType 删除类型（单向好友、双向好友）
 *  @param succ  成功回调([TIMFriendResult])
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
- (int)delFriend:(NSString *)user delType:(TIMDelFriendType)delType succ:(TIMHandleFriendArraySucc)succ fail:(TIMFail)fail;
@end
```

成功回调会返回操作用户的 `TIMFriendResult` 结果数据，开发者可根据情况提示用户。 删除好友的错误码如下。

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

示例代码

```
NSMutableArray * del_users = [[NSMutableArray alloc] init];
// 删除好友 iOS_002
[del_users addObject:@"iOS_002"];
// TIM_FRIEND_DEL_BOTH 指定删除双向好友
[[TIMFriendshipManager sharedInstance] deleteFriends:del_users delType:TIM_FRIEND_DEL_BOTH succ:^(NSArray<TIMFriendResult *> *results) {
	for (TIMFriendResult * res in results) {
		if (res.result_code != TIM_FRIEND_STATUS_SUCC) {
			NSLog(@"deleteFriends failed: user=%@ result_code=%d", res.identifier, res.result_code);
		}
		else {
			NSLog(@"deleteFriends succ: user=%@ result_code=%d", res.identifier, res.result_code);
		}
	}
} fail:^(int code, NSString * err) {
	NSLog(@"deleteFriends failed: code=%d err=%@", code, err);
}];
```

### 同意/拒绝 好友申请

可通过 `TIMFriendshipManager` 的 `doResponse` 方法同意/拒绝好友申请

```
@interface TIMFriendshipManager : NSObject
/**
 *  响应对方好友邀请
 *
 *  @param response  响应请求
 *  @param succ      成功回调
 *  @param fail      失败回调
 *
 *  @return 0 发送请求成功
 */
- (int)doResponse:(TIMFriendResponse *)response succ:(TIMFriendResultSucc)succ fail:(TIMFail)fail;
@end
```
参数 response 的定义如下：
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
/**
 * 响应好友请求
 */
@interface TIMFriendResponse : NSObject

/**
 *  响应类型
 */
@property(nonatomic,assign) TIMFriendResponseType responseType;

/**
 *  用户 identifier
 */
@property(nonatomic,strong) NSString* identifier;

/**
 *  备注好友（可选，如果要加对方为好友）。备注最大96字节
 */
@property(nonatomic,strong) NSString* remark;

@end
```

成功回调会返回操作用户的 `TIMFriendResult` 结果数据，处理用户请求的错误码如下。
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
     *  加好友、响应好友时有效：自己的好友数已达系统上限
     */
    TIM_ADD_FRIEND_STATUS_SELF_FRIEND_FULL                  = 30010,      
    /**
     *  加好友、响应好友时有效：对方的好友数已达系统上限
     */
    TIM_ADD_FRIEND_STATUS_THEIR_FRIEND_FULL                 = 30014,
};
```

### 校验好友关系

可通过 `TIMFriendshipManager` 的 `checkFriends` 方法校验好友关系。

```
/**
 *  检查指定用户的好友关系
 *
 *  @param checkInfo 好友检查信息
 *  @param succ  成功回调，返回检查结果
 *  @param fail  失败回调
 *
 *  @return 0 发送成功
 */
- (int)checkFriends:(TIMFriendCheckInfo *)checkInfo succ:(TIMCheckFriendResultArraySucc)succ fail:(TIMFail)fail;
```

参数 `checkInfo` 定义如下：

```
/**
 *  好友关系检查
 */
@interface TIMFriendCheckInfo : NSObject
/**
 *  检查用户的 ID 列表（NSString*）
 */
@property(nonatomic,strong) NSArray* users;

/**
 *  检查类型
 */
@property(nonatomic,assign) TIMFriendCheckType checkType;

@end
```

参数 `TIMFriendCheckType` 定义如下：

```
/**
 *  好友检查类型
 */
typedef NS_ENUM(NSInteger,TIMFriendCheckType) {
    /**
     *  单向好友
     */
    TIM_FRIEND_CHECK_TYPE_UNIDIRECTION     = 0x1,
    /**
     *  互为好友
     */
    TIM_FRIEND_CHECK_TYPE_BIDIRECTION      = 0x2,
};
```

成功回调会返回操作用户的 `TIMCheckFriendResult` 列表数据，定义如下。

```
@interface TIMCheckFriendResult : NSObject
/**
 *  用户 ID
 */
@property NSString* identifier;

/**
 * 返回码
 */
@property NSInteger result_code;

/**
 * 返回信息
 */
@property NSString *result_info;

/**
 *  检查结果
 */
@property(nonatomic,assign) TIMFriendRelationType resultType;

@end
```

参数 `TIMFriendRelationType` 定义如下：

```
/**
 *  好友关系类型
 */
typedef NS_ENUM(NSInteger,TIMFriendRelationType) {
    /**
     *  不是好友
     */
    TIM_FRIEND_RELATION_TYPE_NONE           = 0x0,
    /**
     *  对方在我的好友列表中
     */
    TIM_FRIEND_RELATION_TYPE_MY_UNI         = 0x1,
    /**
     *  我在对方的好友列表中
     */
    TIM_FRIEND_RELATION_TYPE_OTHER_UNI      = 0x2,
    /**
     *  互为好友
     */
    TIM_FRIEND_RELATION_TYPE_BOTHWAY        = 0x3,
};
```

## 好友未决

### 获取未决列表
其它用户通过`addFriend`方法添加自己为好友，此时会在后台增加一条未决记录。当自己向其它用户请求好友时，后台也会记录一条未决信息。可通过`getPendencyList`方法获取未决列表
```
@interface TIMFriendshipManager : NSObject

/**
 *  获取未决列表
 *
 *  @param pendencyRequest  请求信息，详细参考 TIMFriendPendencyRequest
 *  @param succ 成功回调
 *  @param fail 失败回调
 *
 *  @return 0 发送请求成功
 */
- (int)getPendencyList:(TIMFriendPendencyRequest *)pendencyRequest succ:(TIMGetFriendPendencyListSucc)succ fail:(TIMFail)fail;
@end
```
由于后台可能存储多条好未决，超出界面显示范围，所以此接口支持翻页操作。需要传入参数 pendencyRequest 定义如下
```
/**
 * 未决请求信息
 */
@interface TIMFriendPendencyRequest : TIMCodingModel

/**
 * 序列号，未决列表序列号
 *    建议客户端保存 seq 和未决列表，请求时填入 server 返回的 seq
 *    如果 seq 是 server 最新的，则不返回数据
 */
@property(nonatomic,assign) uint64_t seq;

/**
 * 翻页时间戳，只用来翻页，server 返回0时表示没有更多数据，第一次请求填0
 *    特别注意的是，如果 server 返回的 seq 跟填入 seq 不同，翻页过程中，需要使用客户端原始 seq 请求，直到数据请求完毕，才能更新本地 seq
 */
@property(nonatomic,assign) uint64_t timestamp;

/**
 * 每页的数量，即本次请求最多返回都个数据
 */
@property(nonatomic,assign) uint64_t numPerPage;

/**
 * 未决请求拉取类型
 */
@property(nonatomic,assign) TIMPendencyGetType type;

@end
```
操作成功后，succ 回调返回分页信息和未决记录
```
/**
 * 未决返回信息
 */
@interface TIMFriendPendencyResponse : TIMCodingModel

/**
 * 本次请求的未决列表序列号
 */
@property(nonatomic,assign) uint64_t seq;

/**
 * 本次请求的翻页时间戳
 */
@property(nonatomic,assign) uint64_t timestamp;

/**
 * 未决请求未读数量
 */
@property(nonatomic,assign) uint64_t unreadCnt;

@end
```

```
/**
 * 未决请求
 */
@interface TIMFriendPendencyItem : TIMCodingModel

/**
 * 用户标识
 */
@property(nonatomic,strong) NSString* identifier;
/**
 * 增加时间
 */
@property(nonatomic,assign) uint64_t addTime;
/**
 * 来源
 */
@property(nonatomic,strong) NSString* addSource;
/**
 * 加好友附言
 */
@property(nonatomic,strong) NSString* addWording;

/**
 * 加好友昵称
 */
@property(nonatomic,strong) NSString* nickname;

/**
 * 未决请求类型
 */
@property(nonatomic,assign) TIMPendencyGetType type;

@end
```

### 未决删除
```
@interface TIMFriendshipManager : NSObject
/**
 *  未决删除
 *
 *  @param type  未决好友类型
 *  @param identifiers 要删除的未决列表
 *  @param succ  成功回调
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
- (int)deletePendency:(TIMPendencyGetType)type users:(NSArray *)identifiers succ:(TIMSucc)succ fail:(TIMFail)fail;
@end 
```

### 未决已读上报
当用户拉取到未决记录，可以将本次拉取的未决在后台标记为已读。
```
@interface TIMFriendshipManager : NSObject
/**
 *  未决已读上报
 *
 *  @param timestamp 已读时间戳，此时间戳以前的消息都将置为已读
 *  @param succ  成功回调
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
- (int)pendencyReport:(uint64_t)timestamp succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```
上报后，下次调用`getPendencyList`返回的未读计数将会改变。



## 黑名单

### 添加用户到黑名单

可以把任意用户拉黑，如果此前是好友关系，拉黑后自动解除好友，拉黑后对方发消息无法收到。

```
@interface TIMFriendshipManager : NSObject
/**
 *  添加用户到黑名单
 *
 *  @param identifiers 用户列表
 *  @param succ  成功回调
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
- (int)addBlackList:(NSArray *)identifiers succ:(TIMFriendResultArraySucc)succ fail:(TIMFail)fail;
@end
```


### 把用户从黑名单删除

```
@interface TIMFriendshipManager : NSObject
/**
 *  把用户从黑名单中删除
 *
 *  @param identifiers 用户列表
 *  @param succ  成功回调
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
- (int)deleteBlackList:(NSArray *)identifiers succ:(TIMFriendResultArraySucc)succ fail:(TIMFail)fail;
@end
```


### 获取黑名单列表

```
@interface TIMFriendshipManager : NSObject
/**
 *  获取黑名单列表
 *
 *  @param succ 成功回调，返回 NSString* 列表
 *  @param fail 失败回调
 *
 *  @return 0 发送请求成功
 */
- (int)getBlackList:(TIMFriendArraySucc)succ fail:(TIMFail)fail;
@end
```


## 好友分组

### 创建好友分组

创建分组时，可以同时指定添加的用户。同一用户可以添加到多个分组。

```
/**
 *  新建好友分组
 *
 *  @param groupNames  分组名称列表,必须是当前不存在的分组
 *  @param identifiers 要添加到分组中的好友
 *  @param succ  成功回调
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
- (int)createFriendGroup:(NSArray *)groupNames users:(NSArray *)identifiers succ:(TIMFriendResultArraySucc)succ fail:(TIMFail)fail;
@end
```

### 删除好友分组

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
- (int)deleteFriendGroup:(NSArray *)groupNames succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```


### 添加好友到某分组

```
@interface TIMFriendshipManager : NSObject
/**
 *  添加好友到一个好友分组
 *
 *  @param groupName   好友分组名称
 *  @param identifiers  要添加到分组中的好友
 *  @param succ  成功回调
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
- (int)addFriendsToFriendGroup:(NSString *)groupName users:(NSArray *)identifiers succ:(TIMFriendResultArraySucc)succ fail:(TIMFail)fail;
@end
```


### 从某分组删除好友


```
@interface TIMFriendshipManager : NSObject
/**
 *  从好友分组中删除好友
 *
 *  @param groupName   好友分组名称
 *  @param identifiers  要移出分组的好友
 *  @param succ  成功回调
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
- (int)delFriendsFromFriendGroup:(NSString *)groupName users:(NSArray *)identifiers succ:(TIMFriendResultArraySucc)succ fail:(TIMFail)fail;
@end
```


### 重命名好友分组

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
- (int)renameFriendGroup:(NSString*)oldName newName:(NSString*)newName succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```


### 获取指定的好友分组

```
@interface TIMFriendshipManager : NSObject
/**
 *  获取指定的好友分组信息
 *
 *  @param groupNames      要获取信息的好友分组名称列表,传入 nil 获得所有分组信息
 *  @param succ  成功回调，返回 TIMFriendGroup* 列表
 *  @param fail  失败回调
 *
 *  @return 0 发送请求成功
 */
- (int)getFriendGroups:(NSArray *)groupNames succ:(TIMFriendGroupArraySucc)succ fail:(TIMFail)fail;
@end
```


## 关系链变更系统通知

`TIMMessage` 中 `Elem` 类型 `TIMSNSSystemElem` 为关系链变更系统消息。

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

示例中，当成为好友或者解除好友关系时，打印日志，当有用户申请成为好友时，打印申请理由。 **示例：**

```
@interface TIMMessageListenerImpl : NSObject
- (void)onNewMessage:(NSArray*) msgs;
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

### 添加好友系统通知

当两个用户成为好友时，两个用户均可收到添加好友系统消息。

**触发时机：**

当自己的关系链变更，增加好友时，收到消息（如果已经是单向好友，关系链没有变更的一方不会收到）。

**参数说明：**

参数 | 说明
--- | ---
type | TIM_SNS_SYSTEM_ADD_FRIEND 
users | 成为好友的用户列表 

**`TIMSNSChangeInfo` 参数说明：**

成员 | 说明
--- | ---
identifier | 用户 identifier 

### 删除好友系统通知

当两个用户解除好友关系时，会收到删除好友系统消息： 

**触发时机：**

当自己的关系链变更，删除好友时，收到消息（如果删除的是单向好友，关系链没有变更的一方不会收到）。

**参数说明：**

参数 | 说明
type | TIM_SNS_SYSTEM_DEL_FRIEND 
users | 删除好友的用户列表 

**`TIMSNSChangeInfo` 参数说明：**

成员 | 说明
--- | ---
identifier |  用户 identifier 

### 好友申请系统通知

当申请好友时对方需要验证，自己和对方会收到好友申请系统通知。

**触发时机：**当申请好友时对方需要验证，自己和对方会收到好友申请系统通知，对方可选择同意或者拒绝，自己不能操作，只做信息同步之用。 

**参数说明：**

参数 | 说明
--- | ---
type | TIM_SNS_SYSTEM_ADD_FRIEND_REQ 
users | 申请的好友列表 

**`TIMSNSChangeInfo` 参数说明：**

参数 | 说明
--- | ---
identifier |  用户 identifier 
wording |  申请理由 
source | 申请来源

### 删除未决请求通知

**触发时机：**当申请对方为好友，申请审核通过或者被拒后，自己会收到删除未决请求消息。 

## 用户资料变更系统通知

`TIMMessage` 中 `Elem` 类型 `TIMProfileSystemElem` 为用户资料变更系统消息。

```
/**
 * 自身和好友资料修改，后台 push 下来的消息元素
 */
@interface TIMProfileSystemElem : TIMElem
/**
 *  变更类型
 */
@property(nonatomic,assign) TIM_PROFILE_SYSTEM_TYPE type;
/**
 *  资料变更的用户
 */
@property(nonatomic,strong) NSString * fromUser;
/**
 *  资料变更的昵称（暂未实现）
 */
@property(nonatomic,strong) NSString * nickName;
@end
/**
 *  资料变更
 */
typedef NS_ENUM(NSInteger, TIM_PROFILE_SYSTEM_TYPE){
    /**
     好友资料变更
     */
    TIM_PROFILE_SYSTEM_FRIEND_PROFILE_CHANGE        = 0x01,
};
```

当自己的资料或者好友的资料变更时，会收到用户资料变更系统消息。



