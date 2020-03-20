
## 群组综述 

IM云通讯有多种群组类型，其特点以及限制因素可参考[群组系统](/doc/product/269/群组系统)。群组使用唯一Id标识，通过群组Id可以进行不同操作。

## 群组消息 

群组消息与C2C消息相同，仅在获取Conversation时的会话类型不同，可参照（4.1. 消息发送）部分。

## 群组管理

群组相关操作都由 TIMGroupManager 实现，需要用户登录成功后操作。

**获取单例原型：**

```
@interface TIMGroupManager : NSObject
+(TIMGroupManager*)sharedInstance;
@end
```

### 创建内置类型群组

CreatePrivateGroup 创建私有群，CreatePublicGroup创建公有群，CreateChatRoomGroup创建聊天室，创建时可指定群组名称以及要加入的用户列表，创建成功后返回群组Id，可通过群组Id获取Conversation收发消息等。
 
**原型：**

```
@interface TIMGroupManager : NSObject
/**
*  创建私有群
*/
-(int) CreatePrivateGroup:(NSArray*)members groupName:(NSString*)groupName succ:(TIMCreateGroupSucc)succ fail:(TIMFail)fail;
/**
*  创建公有群
*/
-(int) CreatePublicGroup:(NSArray*)members groupName:(NSString*)groupName succ:(TIMCreateGroupSucc)succ fail:(TIMFail)fail;
/**
*  创建聊天室
*/
-(int) CreateChatRoomGroup:(NSArray*)members groupName:(NSString*)groupName succ:(TIMCreateGroupSucc)succ fail:(TIMFail)fail;

@end
```

**参数说明：**

参数 | 说明
---|---
members | NSString列表，指定加入群组的成员，创建者默认加入，无需指定（群内最多2000人） 
groupName | NSString 类型，指定群组名称（最长30字节） 
groupId | NSString 类型，指定群组Id
succ | 成功回调，返回群组Id 
fail | 失败回调示例：

```
NSMutableArray * members = [[NSMutableArray alloc] init];
// 添加一个用户iOS_002
[members addObject:@"iOS_002"];
[[TIMGroupManager sharedInstance] CreatePrivateGroup:members groupName:@"GroupName" succ:^(NSString * group) {
	NSLog(@"create group succ, sid=%@", group);
} fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

示例创建一个私有群组，并且把用户@"iOS_002"拉入群组，创建者默认加入群组，无需显式指定。 
公有群和聊天室调用方式和参数相同，仅方法名不同。 

### 创建指定属性群组

在创建群组时，除了设置默认的成员以及群名外，还可以设置如群公告、群简介等字段，通过以下接口可以设置：

```

/**
 *  创建群参数
 */
@interface TIMCreateGroupInfo : TIMCodingModel

/**
 *  群组Id,nil则使用系统默认Id
 */
@property(nonatomic,retain) NSString* group;

/**
 *  群名
 */
@property(nonatomic,retain) NSString* groupName;

/**
 *  群类型：Private,Public,ChatRoom,AVChatRoom
 */
@property(nonatomic,retain) NSString* groupType;

/**
 *  是否设置入群选项，Private类型群组请设置为false
 */
@property(nonatomic,assign) BOOL setAddOpt;

/**
 *  入群选项
 */
@property(nonatomic,assign) TIMGroupAddOpt addOpt;

/**
 *  最大成员数，填0则系统使用默认值
 */
@property(nonatomic,assign) uint32_t maxMemberNum;

/**
 *  群公告
 */
@property(nonatomic,retain) NSString* notification;

/**
 *  群简介
 */
@property(nonatomic,retain) NSString* introduction;

/**
 *  群头像
 */
@property(nonatomic,retain) NSString* faceURL;

/**
 *  自定义字段集合,key是NSString*类型,value是NSData*类型
 */
@property(nonatomic,retain) NSDictionary* customInfo;

/**
 *  创建成员（TIMCreateGroupMemberInfo*）列表
 */
@property(nonatomic,retain) NSArray* membersInfo;

@end

@interface TIMGroupManager : NSObject

/**
 *  创建群组
 *
 *  @param groupInfo 群组信息
 *  @param succ      成功回调
 *  @param fail      失败回调
 *
 *  @return 0 成功
 */
-(int) CreateGroup:(TIMCreateGroupInfo*)groupInfo succ:(TIMCreateGroupSucc)succ fail:(TIMFail)fail;

@end
```

**参数说明：**

参数|说明
---|---
groupInfo|可设置的参数，详见 TIMCreateGroupInfo 定义。
succ|成功回调
fail|失败回调

**示例：**

```
// 创建群组信息
TIMCreateGroupInfo *groupInfo = [[TIMCreateGroupInfo alloc] init];
groupInfo.group = nil;
groupInfo.groupName = @"group_private";
groupInfo.groupType = @"Private";
groupInfo.addOpt = TIM_GROUP_ADD_FORBID;
groupInfo.maxMemberNum = 3;
groupInfo.notification = @"this is a notification";
groupInfo.introduction = @"this is a introduction";
groupInfo.faceURL = nil;

// 创建群成员信息
TIMCreateGroupMemberInfo *memberInfo = [[TIMCreateGroupMemberInfo alloc] init];
memberInfo.member = @"iOS_001";
memberInfo.role = TIM_GROUP_MEMBER_ROLE_ADMIN;

// 添加群成员信息
NSMutableArray *membersInfo = [[NSMutableArray alloc] init];
[membersInfo addObject:memberInfo];
groupInfo.membersInfo = membersInfo;

// 创建指定属性群组
[[TIMGroupManager sharedInstance] CreateGroup:groupInfo succ:^(NSString * group) {
	NSLog(@"create group succ, sid=%@", group);
} fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```
示例创建一个指定属性的私有群，并把用户 @"iOS_001" 加入群组，创建者默认加入群，无需显示指定。

### 自定义群组Id创建群组

默认创建群组时，IM通讯云服务器会生成一个唯一的Id，以便后续操作，另外，如果用户需要自定义群组Id，在创建时可指定Id，通过 3.2 创建指定属性群组 也可以实现自定义群组Id的功能。

```
@interface TIMGroupManager : NSObject

/**
 *  创建群组，可以指定群组类型、群组名和群组Id
 *
 *  @param type       群类型,Private,Public,ChatRoom
 *  @param members    待加入群组的成员列表
 *  @param groupName  群组名称
 *  @param groupId    自定义群组id
 *  @param succ       成功回调
 *  @param fail       失败回调
 *
 *  @return 0 成功
 */
-(int) CreateGroup:(NSString*)type members:(NSArray*)members groupName:(NSString*)groupName groupId:(NSString*)groupId succ:(TIMCreateGroupSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
type|群组类型
members|初始成员列表
groupName|群组名称
groupId|自定义群组Id
succ|成功回调
fail|失败回调

### 邀请用户入群

TIMGroupManager 的接口 InviteGroupMember 可以拉（邀请）用户进入群组，对私有群，对方直接进入群组，对于共有群，需要对方同意才可进入。

**权限说明：**
 
只有私有群可以拉用户入群； 
公有群、聊天室邀请用户入群，需要用户同意；

**原型：**

```
@interface TIMGroupManager : NSObject
-(int) InviteGroupMember:(NSString*)group members:(NSArray*)members succ:(TIMGroupMemberSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**
 
参数|说明
---|---
group | NSString 类型，群组Id 
members | NSString 列表，加入群组用户列表 
succ | 成功回调，TIMGroupMemberResult 数组，返回成功加入群组的用户列表以及成功状态 
fail | 失败回调 

**示例：**

```
NSMutableArray * members = [[NSMutableArray alloc] init];
// 添加一个用户iOS_002
[members addObject:@"iOS_002"];
// @"TGID1JYSZEAEQ" 为群组Id
[[TIMGroupManager sharedInstance] InviteGroupMember:@"TGID1JYSZEAEQ" members:members succ:^(NSArray* arr) {
	for (TIMGroupMemberResult * result in arr) {
		NSLog(@"user %@ status %d", result.member, result.status);
	}
} fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

示例中邀请好友 @"iOS_002" 加入群组Id @"TGID1JYSZEAEQ"，成功后返回操作列表以及成功状态。 
其中 result.status表示当前用户操作是否成功，具体定义如下： 

```
/**
*  群组操作结果
*/
typedef NS_ENUM(NSInteger, TIMGroupMemberStatus) {
	/**
	*  操作失败
	*/
	TIM_GROUP_MEMBER_STATUS_FAIL              = 0,
	/**
	*  操作成功
	*/
	TIM_GROUP_MEMBER_STATUS_SUCC              = 1,
	/**
	*  无效操作，加群时已经是群成员，移除群组时不在群内
	*/
	TIM_GROUP_MEMBER_STATUS_INVALID           = 2,
};
```

### 申请加入群组 

TIMGroupManager 的接口 JoinGroup可以主动申请进入群组，此操作只对公有群和聊天室有效。 

**权限说明：**
 
私有群不能由用户主动申请入群； 
公有群和聊天室可以主动申请进入； 
如果群组设置为需要审核，申请后管理员和群主会受到申请入群系统消息，需要等待管理员或者群主审核，如果群主设置为任何人可加入，则直接入群成功。 

**原型：**

```
@interface TIMGroupManager : NSObject
/**
*  申请加群
*
*  @param group 申请加入的群组Id
*  @param msg   申请消息
*  @param succ  成功回调（申请成功等待审批）
*  @param fail  失败回调
*
*  @return 0 成功
*/
-(int) JoinGroup:(NSString*)group msg:(NSString*)msg succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```
**参数说明：**

参数|说明
---|---
group | NSString 类型，群组Id 
msg  | 申请理由 
succ | 成功回调 
fail | 失败回调

**示例：**

```
[[TIMGroupManager sharedInstance] JoinGroup:@"TGID1JYSZEAEQ" msg:@"Apply Join Group" succ:^(){
	NSLog(@"Join Succ");
}fail:^(int code, NSString * err) {
	NSLog(@"code=%d, err=%@", code, err);
}];
```

示例中用户申请加入群组@"TGID1JYSZEAEQ"，申请理由为@"Apply Join Group"。

### 退出群组 

群组成员可以主动退出群组。 

**权限说明：**
 
对于私有群，全员可退出群组； 
对于公有群和聊天室，群主不能退出； 

**原型：**

```
@interface TIMGroupManager : NSObject
-(int) QuitGroup:(NSString*)group succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | NSString 类型，群组Id 
succ | 成功回调 
fail | 失败回调 

**示例：**

```
// @"TGID1JYSZEAEQ" 为群组Id
[[TIMGroupManager sharedInstance] QuitGroup:@"TGID1JYSZEAEQ" succ:^() {
	NSLog(@"succ");
} fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

示例中主动退出群组 @"TGID1JYSZEAEQ"。 

### 删除群组成员 

群组成员也可以删除其他成员，函数参数信息与加入群组相同。 

**权限说明：**
 
对于私有群：只有创建者可删除群组成员 
对于公有群和聊天室：只有管理员和群主可以踢人 

**原型：**

```
@interface TIMGroupManager : NSObject
-(int) DeleteGroupMember:(NSString*)group members:(NSArray*)members succ:(TIMGroupMemberSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | NSString 类型，群组Id 
members | `NSString*` 数组，被操作的用户列表 
succ | 成功回调，`TIMGroupMemberResult` 数组，返回成功加入群组的用户列表已经成功状态 
fail | 失败回调 

**示例：**

```
NSMutableArray * members = [[NSMutableArray alloc] init];

// 添加一个用户iOS_002
[members addObject:@"iOS_002"];

// @"TGID1JYSZEAEQ" 为群组Id
[[TIMGroupManager sharedInstance] DeleteGroupMember:@"TGID1JYSZEAEQ" members:members succ:^(NSArray* arr) {
	for (TIMGroupMemberResult * result in arr) {
		NSLog(@"user %@ status %d", result.member, result.status);
	}
} fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

示例中把好友 @"iOS_002" 从群组 @"TGID1JYSZEAEQ" 中删除，执行成功后返回操作列表以及操作状态。 

### 获取群成员列表 

GetGroupMembers 方法可获取群内成员列表，默认拉取内置字段，但不拉取自定义字段，想要获取自定义字段，可通过【4.1 设置拉取字段】进行设置（1.9版本以上引入）。

**权限说明：**
 
任何群组类型都可以获取成员列表； 

**原型：**

```
/**
 *  成员操作返回值
 */
@interface TIMGroupMemberInfo : TIMCodingModel

/**
 *  被操作成员
 */
@property(nonatomic,retain) NSString* member;

/**
 *  群名片
 */
@property(nonatomic,retain) NSString* nameCard;

/**
 *  加入群组时间
 */
@property(nonatomic,assign) time_t joinTime;

/**
 *  成员类型
 */
@property(nonatomic,assign) TIMGroupMemberRole role;

/**
 *  禁言时间（剩余秒数）
 */
@property(nonatomic,assign) uint32_t silentUntil;

/**
 *  自定义字段集合,key是NSString*类型,value是NSData*类型
 */
@property(nonatomic,retain) NSDictionary* customInfo;

@end

@interface TIMGroupManager : NSObject
-(int) GetGroupMembers:(NSString*)group succ:(TIMGroupMemberSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | `NSString*` 类型，群组Id 
succ | 成功回调（返回`TIMGroupMemberInfo*`数组） 
fail | 失败回调 

**示例：**

```
// @"TGID1JYSZEAEQ" 为群组Id
[[TIMGroupManager sharedInstance] GetGroupMembers:@"TGID1JYSZEAEQ" succ:^(NSArray* list) {
	for (TIMGroupMemberInfo * info in list) {
		NSLog(@"user=%@ joinTime=%lu role=%d", info.member, info.joinTime, info.role);
	}
} fail:^(int code, NSString * err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

示例中获取群 @"TGID1JYSZEAEQ" 的成员列表，list 为 `TIMGroupMemberInfo*` 数据，存储成员的相关信息。 

另外，如果群组人数过多，建议使用分页接口：

```

@interface TIMGroupManager : NSObject

/**
 *  获取群成员列表（支持按字段拉取，分页）
 *
 *  @param group    群组Id
 *  @param flags    拉取资料标志
 *  @param custom   要获取的自定义key列表，暂不支持，传nil
 *  @param nextSeq  分页拉取标志，第一次拉取填0，回调成功如果不为零，需要分页，传入再次拉取，直至为0
 *  @param succ     成功回调
 *  @param fail     失败回调
 *
 *  @return 0 成功
 */
-(int) GetGroupMembersV2:(NSString*)group flags:(TIMGetGroupMemInfoFlag)flags custom:(NSArray*)custom nextSeq:(uint64_t)nextSeq succ:(TIMGroupMemberSuccV2)succ fail:(TIMFail)fail;

@end
```

### 获取加入的群组列表 

通过 GetGroupList 可以获取当前用户加入的所有群组： 

**权限说明：**
 
此接口可以获取自己所加入的群列表，返回的TIMGroupInfo只包含group\groupName\groupType 信息，想要获取更加详细的字段，可通过【4.1 设置拉取字段】进行设置（1.9版本以上引入）。
 
**原型：**

```
@interface TIMGroupManager : NSObject

/**
 *  获取群列表
 *
 *  @param succ 成功回调，NSArray列表为 TIMGroupInfo，结构体只包含 group\groupName\groupType 信息
 *  @param fail 失败回调
 *
 *  @return 0 成功
 */
-(int) GetGroupList:(TIMGroupListSucc)succ fail:(TIMFail)fail;
@end
```
**参数说明：**

参数|说明
---|---
succ | 成功回调，返回群组Id列表，TIMGroupInfo数组 
fail | 失败回调 

**示例：**

```
[[TIMGroupManager sharedInstance] GetGroupList:^(NSArray * list) {
	for (TIMGroupInfo * info in list) {
		NSLog(@"group=%@ type=%@ name=%@", info.group, info.groupType, info.groupName);
	}
} fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

示例中获取群组列表，并打印群组Id，群类型（Private/Public/ChatRoom）以及群名。 

### 解散群组

通过 DeleteGroup 可以解散群组。 

**权限说明：**
 
对于私有群，任何人都无法解散群组 
对于公有群和聊天室，群主可以解散群组： 

**原型：**

```
@interface TIMGroupManager : NSObject

/**
 *  解散群组
 */
-(int) DeleteGroup:(NSString*)group succ:(TIMSucc)succ fail:(TIMFail)fail;

@end
```
**参数说明：**

参数 | 说明
---|---
group | 群组Id 
succ | 成功回调，返回群组Id列表，NSString数组 
fail | 失败回调 

**示例：**

```
[[TIMGroupManager sharedInstance] DeleteGroup:@"TGID1JYSZEAEQ" succ:^() {
	NSLog(@"delete group succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```
示例中解散群组 @"TGID1JYSZEAEQ"。

### 转让群组 

通过 ModifyGroupOwner可以转让群组。 

**权限说明：**
 
只有群主才有权限进行群转让操作 
群主可以转让群组： 

**原型：**

```
@interface TIMGroupManager : NSObject

/**
 *  转让群给新群主
 */
-(int) ModifyGroupOwner:(NSString*)group user:(NSString*)identifier succ:(TIMSucc)succ fail:(TIMFail)fail;

@end
```

**参数说明：**

参数|说明
---|---
group | 群组Id 
user| 用户Id 
succ | 成功回调 
fail | 失败回调 

**示例：**

```
[[TIMGroupManager sharedInstance] ModifyGroupOwner:@"TGID1JYSZEAEQ" user:@"iOS_001" succ:^() {
	NSLog(@"set new owner succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```
示例中转让群组 @"TGID1JYSZEAEQ"给用户@"iOS_001"。 

### 删除群组成员（带原因）

群组成员也可以删除其他成员，函数参数信息与加入群组相同。 

**权限说明：**
 
对于私有群：只有创建者可删除群组成员 
对于公有群和聊天室：只有管理员和群主可以踢人 

**原型：**

```
/**
 *  删除群成员
 *
 *  @param group   群组Id
 *  @param reason  删除原因
 *  @param members 要删除的成员列表
 *  @param succ    成功回调
 *  @param fail    失败回调
 *
 *  @return 0 成功
 */
-(int) DeleteGroupMemberWithReason:(NSString*)group reason:(NSString*)reason members:(NSArray*)members succ:(TIMGroupMemberSucc)succ fail:(TIMFail)fail;
```
**参数说明：**
 
group ： NSString 类型，群组Id 
reason ： 操作原因 
members ： NSString* 数组，被操作的用户列表 
succ ： 成功回调，TIMGroupMemberResult 数组，返回成功加入群组的用户列表已经成功状态 
fail ： 失败回调 

**示例： **

```
NSMutableArray * members = [[NSMutableArray alloc] init];

// 添加一个用户iOS_002
[members addObject:@"iOS_002"];

// @"TGID1JYSZEAEQ" 为群组Id
[[TIMGroupManager sharedInstance] DeleteGroupMember:@"TGID1JYSZEAEQ" reason:@"Quit" members:members succ:^(NSArray* arr) {
	for (TIMGroupMemberResult * result in arr) {
		NSLog(@"user %@ status %d", result.member, result.status);
	}
} fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```
示例中把好友 @"iOS_002" 从群组 @"TGID1JYSZEAEQ" 中删除，执行成功后返回操作列表以及操作状态。 。 


## 获取群资料

### 设置拉取字段

拉取用户资料默认返回部分内置字段，如果需要自定义字段，或者不拉取某些字段，可以通过接口进行设置（**此接口1.9版本以上提供**），此设置对所有资料相关接口有效，全局有效：

```
@interface TIMGroupSetting : NSObject
/**
 *  需要获取的群组信息标志（TIMGetGroupBaseInfoFlag）
 */
@property(nonatomic,assign) uint64_t groupFlags;

/**
 *  需要获取群组资料的自定义信息（NSString*）列表
 */
@property(nonatomic,retain) NSArray * groupCustom;

/**
 *  需要获取的群成员标志（TIMGetGroupMemInfoFlag）
 */
@property(nonatomic,assign) uint64_t memberFlags;

/**
 *  需要获取群成员资料的自定义信息（NSString*）列表
 */
@property(nonatomic,retain) NSArray * memberCustom;

@end

@interface TIMManager : NSObject
/**
 *  设置TIMGroupManager和TIMGroupAssistant默认拉取的字段（不设置：默认拉取所有基本字段，不拉取自定义字段）
 *
 *  @param setting 设置参数
 *
 *  @return 0 成功
 */
-(int) initGroupSetting:(TIMGroupSetting*)setting;
@end
```

**参数说明**

参数|说明
---|---
setting|设置TIMGroupManager和TIMGroupAssistant默认拉取的字段

### 群成员获取群组资料

GetGroupInfo方法可以获取群组资料。默认拉取基本资料，如果想拉取自定义资料，可通过【4.1 设置拉取字段】进行设置（1.9版本以上引入）。

**权限说明：**
 
注意：获取群组资料接口只能由群成员调用，非群成员无法通过此方法获取资料，需要调用。 
群资料信息由TIMGroupInfo定义： 

通过 TIMGroupManager 的方法 GetGroupInfo 可获取群组资料： 

**原型：**

```
@interface TIMGroupInfo : NSObject {
    NSString*       group;          // 群组Id
    NSString*       groupName;      // 群名
    NSString*       groupType;      // 群组类型
    NSString*       owner;          // 创建人
    uint32_t        createTime;     // 群创建时间
    uint32_t        lastInfoTime;   // 最近一次修改资料时间
    uint32_t        lastMsgTime;    // 最近一次发消息时间
    uint32_t        memberNum;      // 群成员数量
    NSString*       notification;      // 群公告
    NSString*       introduction;      // 群简介
    NSString*       faceURL;            // 群头像
}

@interface TIMGroupManager : NSObject
-(int) GetGroupInfo:(NSArray*)groups succ:(TIMGroupListSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
groups |NSString 数组，需要获取资料的群组列表 
succ | 成功回调，返回群组资料列表，TIMGroupInfo数组 
fail | 失败回调 

**示例：**

```
NSMutableArray * groupList = [[NSMutableArray alloc] init];
[groupList addObject:@"TGID1JYSZEAEQ"];

[[TIMGroupManager sharedInstance] GetGroupInfo:groupList succ:^(NSArray * groups) {
	for (TIMGroupInfo * info in groups) {
		NSLog(@"get group succ, infos=%@", info);
	}
} fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```
示例中获取群组 @"TGID1JYSZEAEQ" 的详细信息。 

### 非群成员获取群组资料

GetGroupInfo方法只对群成员有效，非成员需要调用 GetGroupPublicInfo 实现，只能获取公开信息。默认拉取基本资料，如果想拉取自定义资料，可通过【4.1 设置拉取字段】进行设置（1.9版本以上引入）。

**权限说明：**
 
任意用户可以获取群公开资料

**原型：**

```
@interface TIMGroupManager : NSObject
/**
 *  获取群公开信息
 *  @param groups 群组Id
 *  @param succ 成功回调
 *  @param fail 失败回调
 *
 *  @return 0 成功
 */
-(int) GetGroupPublicInfo:(NSArray*)groups succ:(TIMGroupListSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
groups |NSString 数组，需要获取资料的群组列表 
succ | 成功回调，返回群组资料列表，TIMGroupInfo数组 
fail | 失败回调 

**示例：**

```
NSMutableArray * groupList = [[NSMutableArray alloc] init];
[groupList addObject:@"TGID1JYSZEAEQ"];

[[TIMGroupManager sharedInstance] GetGroupPublicInfo:groupList succ:^(NSArray * groups) {
	for (TIMGroupInfo * info in groups) {
		NSLog(@"get group succ, infos=%@", info);
	}
} fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```
示例中获取群组 @"TGID1JYSZEAEQ" 的公开信息。 


### 获取本人在群里的资料

如果需要获取在所有群内的资料，可以通过 [GetGroupList](#.E8.8E.B7.E5.8F.96.E5.8A.A0.E5.85.A5.E7.9A.84.E7.BE.A4.E7.BB.84.E5.88.97.E8.A1.A8) 拉取加入的群列表时得到（1.9版本以后支持）。另外，如果需要单独获取某个群组，可使用以下接口，建议通过GetGroupList获取，没有必要调用以下接口单独获取。默认拉取基本资料，如果想拉取自定义资料，可通过【4.1 设置拉取字段】进行设置（1.9版本以上引入）。

**原型：**

```
@interface TIMGroupManager : NSObject
/**
 *  获取本人在群组内的成员信息
 *
 *  @param group 群组Id
 *  @param succ  成功回调，返回信息
 *  @param fail  失败回调
 *
 *  @return 0 成功
 */
-(int) GetGroupSelfInfo:(NSString*)group succ:(TIMGroupSelfSucc)succ fail:(TIMFail)fail;
@end

/**
 *  获取接受消息选项
 *
 *  @param group            群组Id
 *  @param succ             成功回调
 *  @param fail             失败回调
 *
 *  @return 0 成功
 */
-(int) GetReciveMessageOpt:(NSString*)group succ:(TIMGroupReciveMessageOptSucc)succ fail:(TIMFail)fail;
```

**参数说明：**

参数|说明
---|---
group | 群组Id
succ |  成功回调，返回用户本人在群内的资料
fail | 失败回调

### 获取群内某个人的资料

（1.9版本提供）默认拉取基本资料，如果想拉取自定义资料，可通过【4.1 设置拉取字段】进行设置（1.9版本以上引入）。

 

## 修改群资料 

### 修改群名 

通过 ModifyGroupName可以修改群组名称： 

**权限说明：**
 
对于公有群和聊天室，只有群主或者管理员可以修改群名； 
对于私有群，任何人可修改群名； 

**原型：**

```
@interface TIMGroupManager : NSObject
-(int) ModifyGroupName:(NSString*)group groupName:(NSString*)groupName succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数 | 说明
group | 群组Id 
groupName | 修改后的群名 
succ | 成功回调 
fail | 失败回调 

**示例：**

```
[[TIMGroupManager sharedInstance] ModifyGroupName:@"TGID1JYSZEAEQ" groupName:@"ModifyGroupName" succ:^() {
	NSLog(@"modify group name succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

示例修改群 @"TGID1JYSZEAEQ" 的名字为 @"ModifyGroupName"。

### 修改群简介 

通过 ModifyGroupIntroduction可以修改群组简介： 

**权限说明：**
 
对于公有群和聊天室，只有群主或者管理员可以修改群简介； 
对于私有群，任何人可修改群简介； 

**原型：**

```
@interface TIMGroupManager : NSObject

/**
 *  修改群简介
 *
 *  @param group            群组Id
 *  @param introduction     群简介
 *  @param succ             成功回调
 *  @param fail             失败回调
 *
 *  @return 0 成功
 */
-(int) ModifyGroupIntroduction:(NSString*)group introduction:(NSString*)introduction succ:(TIMSucc)succ fail:(TIMFail)fail;

@end
```
**参数说明：**

参数 |说明
---|---
group ｜ 群组Id 
introduction | 群简介，简介最长120字节 
succ | 成功回调 
fail | 失败回调 

**示例：**

```
[[TIMGroupManager sharedInstance] ModifyGroupIntroduction:@"TGID1JYSZEAEQ" introduction :@"this is one group" succ:^() {
	NSLog(@"modify group introduction succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

### 修改群公告 

通过 ModifyGroupNotification可以修改群组公告： 

**权限说明：**
 
对于公有群和聊天室，只有群主或者管理员可以修改群公告； 
对于私有群，任何人可修改群公告； 

**原型：**

```
@interface TIMGroupManager : NSObject

/**
 *  修改群公告
 *
 *  @param group            群组Id
 *  @param notification     群公告（最长150字节）
 *  @param succ             成功回调
 *  @param fail             失败回调
 *
 *  @return 0 成功
 */
-(int) ModifyGroupNotification:(NSString*)group notification:(NSString*)notification succ:(TIMSucc)succ fail:(TIMFail)fail;

@end
```

**参数说明：**

参数|说明
---|---
group | 群组Id 
notification | 群公告，群公告最长150字节 
succ | 成功回调 
fail | 失败回调 

**示例：**

```
[[TIMGroupManager sharedInstance] ModifyGroupNotification:@"TGID1JYSZEAEQ" notification:@"test notification" succ:^() {
	NSLog(@"modify group notification succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

示例修改群 @"TGID1JYSZEAEQ" 的公告为 @"test notification"。 

### 修改群头像 

通过 ModifyGroupFaceUrl可以修改群头像： 

**权限说明：**
 
对于公有群和聊天室，只有群主或者管理员可以修改群头像； 
对于私有群，任何人可修改群头像； 

**原型：**

```
/**
 *  修改群头像
 *
 *  @param group            群组Id
 *  @param url              群头像地址（最长100字节）
 *  @param succ             成功回调
 *  @param fail             失败回调
 *
 *  @return 0 成功
 */
-(int) ModifyGroupFaceUrl:(NSString*)group url:(NSString*)url succ:(TIMSucc)succ fail:(TIMFail)fail;

@end
```
**参数说明：**

参数|说明
---|---
group | 群组Id 
url| 群头像地址（最长100字节） 
succ | 成功回调 
fail | 失败回调 

**示例：**

```
[[TIMGroupManager sharedInstance] ModifyGroupFaceUrl:@"TGID1JYSZEAEQ" notification:@"http://test/x.jpg" succ:^() {
	NSLog(@"modify group face url succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

### 修改加群选项 

通过 ModifyGroupAddOpt可以修改加群选项： 

**权限说明：**
 
对于公有群和聊天室，只有群主或者管理员可以修改加群选项； 
对于私有群，只能通过邀请加入群组，不能主动申请加入某个群组； 

**原型：**

```
@interface TIMGroupManager : NSObject

/**
 *  修改加群选项
 *
 *  @param group            群组Id
 *  @param opt              加群选项，详见 TIMGroupAddOpt
 *  @param succ             成功回调
 *  @param fail             失败回调
 *
 *  @return 0 成功
 */
-(int) ModifyGroupAddOpt:(NSString*)group opt:(TIMGroupAddOpt)opt succ:(TIMSucc)succ fail:(TIMFail)fail;

@end
```

**参数说明：**

参数|说明
---|---
group | 群组Id 
opt| 加群选项，可设置为允许任何人加入、需要审核、禁止任何人加入 
succ | 成功回调 
fail | 失败回调 

**示例：**

```
[[TIMGroupManager sharedInstance] ModifyGroupAddOpt:@"TGID1JYSZEAEQ" opt:TIM_GROUP_ADD_FORBID succ:^() {
	NSLog(@"modify group opt succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

示例修改群 @"TGID1JYSZEAEQ" 为禁止任何人加入。 

### 修改群维度自定义字段 

通过 ModifyGroupCustomInfo可以对群维度自定义字段进行修改： 

**权限说明：**
 
后台配置相关的key和权限； 

**原型： **

```
@interface TIMGroupManager : NSObject

/**
 *  修改群自定义字段集合
 *
 *  @param group      群组Id
 *  @param customInfo 自定义字段集合,key是NSString*类型,value是NSData*类型
 *  @param succ       成功回调
 *  @param fail       失败回调
 *
 *  @return 0 成功
 */
-(int) ModifyGroupCustomInfo:(NSString*)group customInfo:(NSDictionary*)customInfo succ:(TIMSucc)succ fail:(TIMFail)fail;

@end
```

**参数说明：**

参数|说明
---|---
group | 群组Id 
customInfo| 自定义字段集合,key是NSString*类型,value是NSData*类型 
succ | 成功回调 
fail | 失败回调 

**示例：**

```
// 设置自定义数据
NSMutalbeDictionary *customInfo = [[NSMutableDictionary alloc] init];
NSString *key = @"custom key";
NSData *data = [NSData dataWithBytes:"custom value" length:13];
[customInfo setObject:data forKey:key];

[[TIMGroupManager sharedInstance] ModifyGroupCustomInfo:@"TGID1JYSZEAEQ" customInfo:customInfo succ:^() {
	NSLog(@"modify group customInfo succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

示例修改群 @"TGID1JYSZEAEQ" 为禁止任何人加入。

### 修改用户群内身份 

通过 ModifyGroupMemberInfoSetRole可以对群成员的身份进行修改： 

**权限说明：**
 
只有群主或者管理员可以进行对群成员的身份进行修改； 

**原型：**

```
@interface TIMGroupManager : NSObject
-(int) ModifyGroupMemberInfoSetRole:(NSString*)group user:(NSString*)identifier role:(TIMGroupMemberRole)role succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | 群组Id 
identifier | 要修改的群成员的Id 
role | 修改后的身份类型。不能修改为群主类型，详见TIMGroupMemberRole 
succ | 成功回调 
fail | 失败回调 

**示例：**

```
[[TIMGroupManager sharedInstance] ModifyGroupMemberInfoSetRole:@"TGID1JYSZEAEQ" user:@"iOS_001" role:TIM_GROUP_MEMBER_ADMIN succ:^() {
	NSLog(@"modify group member role succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

示例设置群 @"TGID1JYSZEAEQ" 的成员 @"iOS_001" 为管理员。 

### 对群成员进行禁言 

通过 ModifyGroupMemberInfoSetSilence可以对群成员进行禁言并设置禁言时长： 

**权限说明：**
 
只有群主或者管理员可以进行对群成员进行禁言； 

**原型：**

```
@interface TIMGroupManager : NSObject
-(int) ModifyGroupMemberInfoSetSilence:(NSString*)group user:(NSString*)identifier stime:(uint32_t)stime succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | 群组Id 
identifier | 要禁言的群成员的Id 
stime | 禁言时间， 单位秒 
succ | 成功回调 
fail | 失败回调 

**示例：**

```
[[TIMGroupManager sharedInstance] ModifyGroupMemberInfoSetSilence:@"TGID1JYSZEAEQ" user:@"iOS_001" stime:120 succ:^() {
	NSLog(@"modify group member silence succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

示例设置群 @"TGID1JYSZEAEQ" 的成员 @"iOS_001" 禁言120s。 

### 修改群名片 

通过 ModifyGroupMemberInfoSetNameCard可以对群成员资料的群名片进行修改： 

**原型： **

```
@interface TIMGroupManager : NSObject
-(int) ModifyGroupMemberInfoSetNameCard:(NSString*)group user:(NSString*)identifier nameCard:(NSString*)nameCard succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | 群组Id 
identifier | 要修改的群成员的Id 
nameCard | 要设置的群名片 
succ | 成功回调 
fail | 失败回调

**示例：**

```
[[TIMGroupManager sharedInstance] ModifyGroupMemberInfoSetNameCard:@"TGID1JYSZEAEQ" user:@"iOS_001" nameCard:@"iOS_001_namecard" succ:^() {
	NSLog(@"modify group member namecard succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

示例设置群 @"TGID1JYSZEAEQ" 的成员 @"iOS_001" 群名片为 @"iOS_001_namecard"。 

### 修改群成员维度自定义字段 

通过 ModifyGroupMemberInfoSetCustomInfo可以对群成员维度自定义字段进行修改： 

**原型：**

```
@interface TIMGroupManager : NSObject
-(int) ModifyGroupMemberInfoSetCustomInfo:(NSString*)group user:(NSString*)identifier customInfo:(NSDictionary*)customInfo succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | 群组Id 
identifier | 要设置自定义属性的群成员的Id 
customInfo | 自定义字段集合,key是NSString*类型,value是NSData*类型 
succ | 成功回调 
fail | 失败回调 

**示例：**

```
[[TIMGroupManager sharedInstance] ModifyGroupMemberInfoSetSilence:@"TGID1JYSZEAEQ" user:@"iOS_001" customInfo:customInfo succ:^() {
	NSLog(@"modify group member customInfo succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

示例设置群 @"TGID1JYSZEAEQ" 的成员 @"iOS_001" 的自定义属性。


## 群组未决信息 

### 拉取群未决相关信息 

通过GetPendencyFromServer 接口可拉取群未决相关信息。此处的群未决消息泛指所有需要审批的群相关的操作。例如：加群待审批，拉人入群待审批等等。即便审核通过或者拒绝后，该条信息也可通过此接口拉回，拉回的信息中有已决标志。

**权限说明：**

**只有审批人有权限拉取相关信息。**
例如：UserA申请加入群GroupA，则群管理员可获取此未决相关信息，UserA因为没有审批权限，不需要过去未决信息。 
         如果AdminA拉UserA进去GroupA，则UserA可以拉取此未决相关信息，因为该未决信息待UserA审批。 

**原型：**

```
@interface TIMGroupManager : NSObject

/**
 *  获取群组未决列表
 *
 *  @param option 未决参数配置
 *  @param succ   成功回调，返回未决列表
 *  @param fail   失败回调
 *
 *  @return 0 成功
 */
-(int) GetPendencyFromServer:(TIMGroupPendencyOption*)option succ:(TIMGetGroupPendencyListSucc)succ fail:(TIMFail)fail;

@end
```

**参数说明：**

参数|说明
---|---
option|未决参数配置
succ|成功回调，返回未决列表
fail|失败回调
 
拉取未决的option相关操作： 
属性说明： 
timestamp：拉取的开始时戳。如果从最新的未决条目开始拉取，则填0或不填。若分页，则回调中返回下一个分页的拉取起始时戳。 
numPerPage：一次拉取的最多条目数，用于分页。 

拉取未决的回调说明： 

```
/**
 *  获取群组未决请求列表成功
 *
 *  @param meta       未决请求元信息
 *  @param pendencies 未决请求列表（TIMGroupPendencyItem）数组
 */
typedef void (^TIMGetGroupPendencyListSucc)(TIMGroupPendencyMeta * meta, NSArray * pendencies);
```

**参数说明：**

参数|说明
---|---
meta|拉取操作返回的相关信息，包含分页信息和拉取状态等。 
pendencies|拉取的未决条目数组 .

**属性说明： **

属性|说明
---|---
nextStartTime|拉取下一个分页的起始时戳，用于传入拉取配置中。为0时表示没有后面的分页了。 
readTimeSeq|已读时戳，用来判定未决条目是否已读。 
unReadCnt|所有未读条目个数。不限制于本次分页中。 

未决条目相关属性： 

```
/**
  *  未决申请
  */
@interface TIMGroupPendencyItem : TIMCodingModel

/**
 *  相关群组id
 */
@property(nonatomic,retain) NSString* groupId;

/**
  *  请求者id，请求加群:请求者，邀请加群:邀请人
  */
@property(nonatomic,retain) NSString* fromUser;

/**
  *  判决者id，请求加群:0，邀请加群:被邀请人
  */
@property(nonatomic,retain) NSString* toUser;

/**
  *  未决添加时间
  */
@property(nonatomic,assign) uint64_t addTime;

/**
  *  未决请求类型
  */
@property(nonatomic,assign) TIMGroupPendencyGetType getType;

/**
  *  已决标志
  */
@property(nonatomic,assign) TIMGroupPendencyHandleStatus handleStatus;

/**
  *  已决结果
  */
@property(nonatomic,assign) TIMGroupPendencyHandleResult handleResult;

/**
  *  申请或邀请附加信息
  */
@property(nonatomic,retain) NSString* requestMsg;

/**
  *  审批信息：同意或拒绝信息
  */
@property(nonatomic,retain) NSString* handledMsg;
@end
```

**属性说明： **

属性|说明
---|---
groupId|群ID 
fromUser|未决发起者ID 
toUser|未决审批者ID 
addTime|添加未决时间 
getType|枚举未决条目类型： 请求加群；邀请加群 
handleStatus|枚举未决条目状态：未决；他人已决；操作者已决 说明：UserA申请加入Group，AdminA审批通过。则AdminB拉取的此未决条目的类型为，他们已决。
handleResult|枚举审批结果：同意；拒绝 
requestMsg/handleMsg|申请、审批时的hello word
 
**示例：**

```
  TIMGroupPendencyOption option = [[TIMGroupPendencyOption alloc] init];
  option.timestamp = 0;
  option.numPerPage = 10;
    
  [[TIMGroupManager sharedInstance] GetPendencyFromServer:option succ:^(TIMGroupPendencyMeta *meta, NSArray *pendencies) {
      NSLog(@"get pendencies succ");
  } fail:^(int code, NSString *msg) {
      NSLog(@"get pendencies failed: %d->%@", code, msg);
  }];
```

### 上报群未决已读 

对于未决信息，sdk可对其和之前的所有未决信息上报已读。上报已读后，仍然可以拉取到这些未决信息，但可通过对已读时戳的判断判定未决信息是否已读。 

**原型：**

```
@interface TIMGroupManager : NSObject

/**
 *  群未决已读上报
 *
 *  @param timestamp 上报已读时间戳
 *  @param succ      成功回调
 *  @param fail      失败回调
 *
 *  @return 0 成功
 */
-(int) PendencyReport:(uint64_t)timestamp succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
timestamp|上报已读时戳。对于单条未决信息，时戳包含在其属性里。 
succ|成功回调 
fail|失败回调 

**示例：** 

```
[[TIMGroupManager sharedInstance] PendencyReport:timestamp succ:^{
        NSLog(@"pendency report succ");
    } fail:^(int code, NSString *msg) {
        NSLog(@"pendency report failed: %d->%@", code, msg);
    }];
```

### 处理群未决信息 

对于群的未决信息，sdk增加了处理接口。审批人可以选择对单条信息进行同意或者拒绝。已处理成功过的未决信息不能再次处理。 

**原型：**

```
@interface TIMGroupPendencyItem: NSObject

/**
 *  同意申请
 *
 *  @param msg      同意理由，选填
 *  @param succ     成功回调
 *  @param fail     失败回调，返回错误码和错误描述
 */
-(void) accept:(NSString*)msg succ:(TIMSucc)succ fail:(TIMFail)fail;

/**
 *  拒绝申请
 *
 *  @param msg      拒绝理由，选填
 *  @param succ     成功回调
 *  @param fail     失败回调，返回错误码和错误描述
 */
-(void) refuse:(NSString*)msg succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**示例：**

```
TIMGroupPendencyItem *item = [pendencies firstObject];
    
[item accept:@"thanks for inviting" succ:^{
    NSLog(@"accept succ");
} fail:^(int code, NSString *msg) {
    NSLog(@"accept fail: %d->%@", code, msg);
}];
    
[item refuse:@"i dont want to join" succ:^{
    NSLog(@"refuse succ");
} fail:^(int code, NSString *msg) {
    NSLog(@"refuse fail: %d->%@", code, msg);
}];
```

## 群资料存储

在1.9版本之前，并未存储用户的群资料数据，每次调用接口都是从服务端重新获取，需要APP端进行存储，1.9以后版本，增加了群资料存储，可以设置存储的具体字段，参考 [4.1 设置拉取字段](#.E8.AE.BE.E7.BD.AE.E6.8B.89.E5.8F.96.E5.AD.97.E6.AE.B5)。另外，这里仅存储群资料，并未对群成员的资料获取，1.9版本以后会在群消息中增加用户的相关字段，建议直接从消息中获取。

### 启用群资料存储

**原型：**

```
@interface TIMManager : NSObject

/**
 *  开启群组助手
 *
 *  @return 0 成功
 */
-(int) enableGroupAssistant;

@end
```

###   群组资料获取同步接口

为了方便读取，1.9以后版本增加了群组资料的同步接口（需要开启群资料存储），

**原型：**

```
/**
 *  群组助手
 */
@interface TIMGroupAssistant : NSObject

/**
 *  获取群组助手实例
 *
 *  @return 群主助手实例
 */
+(TIMGroupAssistant*) sharedInstance;

/**
 *  获取用户所在群组信息
 *
 *  @param groups 群组id（NSString*）列表
 *
 *  @return 群组信息（TIMGroupInfo*)列表，assistant未同步时返回nil
 */
-(NSArray*) GetGroupInfo:(NSArray*)groups;

/**
 *  获取用户群组列表
 *
 *  @return 群组信息（TIMGroupInfo*）列表，assistant未同步时返回nil
 */
-(NSArray*) GetGroupList;

@end
```

### 群通知回调

如果开启了存储，可以设置监听感知群事件，当有对应事件发生时，会进行回调：

**原型：**

```
@protocol TIMGroupAssistantListener <NSObject>
@optional
/**
 *  有新用户加入群时的通知回调
 *
 *  @param groupId     群ID
 *  @param membersInfo 加群用户的群资料（TIMGroupMemberInfo*）列表
 */
-(void) OnMemberJoin:(NSString*)groupId membersInfo:(NSArray*)membersInfo;

/**
 *  有群成员退群时的通知回调
 *
 *  @param groupId 群ID
 *  @param members 退群成员的identifier（NSString*）列表
 */
-(void) OnMemberQuit:(NSString*)groupId members:(NSArray*)members;

/**
 *  群成员信息更新的通知回调
 *
 *  @param groupId     群ID
 *  @param membersInfo 更新后的群成员资料（TIMGroupMemberInfo*）列表
 */
-(void) OnMemberUpdate:(NSString*)groupId membersInfo:(NSArray*)membersInfo;

/**
 *  加入群的通知回调
 *
 *  @param groupInfo 加入群的群组资料
 */
-(void) OnGroupAdd:(TIMGroupInfo*)groupInfo;

/**
 *  解散群的通知回调
 *
 *  @param groupId 解散群的群ID
 */
-(void) OnGroupDelete:(NSString*)groupId;

/**
 *  群资料更新的通知回调
 *
 *  @param groupInfo 更新后的群资料信息
 */
-(void) OnGroupUpdate:(TIMGroupInfo*)groupInfo;

@end
```

**参数说明：**

群成员变更时通过onMemberUpdate回调，参数`TIMGroupMemberInfo*`为变更后的成员信息，可以根据字段更新界面。


## 群事件消息 

当有用户被邀请加入群组，或者有用户被移出群组时，群内会产生有提示消息，调用方可以根据需要展示给群组用户，或者忽略。提示消息使用一个特殊的Elem标识，通过新消息回调返回消息（参见2.3. 新消息通知）：
如下图中，展示一条修改群名的事件消息： 
![](//mccdn.qcloud.com/static/img/cc5b0e33ed6bd492fca7d8fb8469307a/image.jpg)

**消息原型：** 	

```
/**
 *  群Tips类型
 */
typedef NS_ENUM(NSInteger, TIM_GROUP_TIPS_TYPE){
    /**
     *  邀请加入群 (opUser & groupName & userList)
     */
    TIM_GROUP_TIPS_TYPE_INVITE              = 0x01,
    /**
     *  退出群 (opUser & groupName & userList)
     */
    TIM_GROUP_TIPS_TYPE_QUIT_GRP            = 0x02,
    /**
     *  踢出群 (opUser & groupName & userList)
     */
    TIM_GROUP_TIPS_TYPE_KICKED              = 0x03,
    /**
     *  设置管理员 (opUser & groupName & userList)
     */
    TIM_GROUP_TIPS_TYPE_SET_ADMIN           = 0x04,
    /**
     *  取消管理员 (opUser & groupName & userList)
     */
    TIM_GROUP_TIPS_TYPE_CANCEL_ADMIN        = 0x05,
    /**
     *  群资料变更 (opUser & groupName & introduction & notification & faceUrl & owner)
     */
    TIM_GROUP_TIPS_TYPE_INFO_CHANGE         = 0x06,
    /**
     *  群成员资料变更 (opUser & groupName & memberInfoList)
     */
    TIM_GROUP_TIPS_TYPE_MEMBER_INFO_CHANGE         = 0x07,
};


/**
 *  群Tips
 */
@interface TIMGroupTipsElem : TIMElem

/**
 *  群Tips类型
 */
@property(nonatomic,assign) TIM_GROUP_TIPS_TYPE type;

/**
 *  操作人用户名
 */
@property(nonatomic,retain) NSString * opUser;

/**
 *  被操作人列表 NSString* 数组
 */
@property(nonatomic,retain) NSArray * userList;

/**
 *  在群名变更时表示变更后的群名，否则为 nil
 */
@property(nonatomic,retain) NSString * groupName;

/**
 *  群信息变更： TIM_GROUP_TIPS_TYPE_INFO_CHANGE 时有效，为 TIMGroupTipsElemGroupInfo 结构体列表
 */
@property(nonatomic,retain) NSArray * groupChangeList;

/**
 *  成员变更： TIM_GROUP_TIPS_TYPE_MEMBER_INFO_CHANGE 时有效，为 TIMGroupTipsElemMemberInfo 结构体列表
 */
@property(nonatomic,retain) NSArray * memberChangeList;

/**
 *  操作者用户资料
 */
@property(nonatomic,retain) TIMUserProfile * opUserInfo;
/**
 *  操作者群成员资料
 */
@property(nonatomic,retain) TIMGroupMemberInfo * opGroupMemberInfo;
/**
 *  变更成员资料
 */
@property(nonatomic,retain) NSDictionary * changedUserInfo;
/**
 *  变更成员群内资料
 */
@property(nonatomic,retain) NSDictionary * changedGroupMemberInfo;

@end
```
调用方可选择是否予以展示，以及如何展示。 

**示例：** 

```
@interface TIMMessageListenerImpl : NSObject- (void)onNewMessage:(NSArray*) msgs;
@end

@implementation TIMMessageListenerImpl
- (void)onNewMessage:(NSArray*) msgs {
    for (TIMMessage * msg in msgs) {
        TIMConversation * conversation = [msg getConversation];
        
        for (int i = 0; i < [msg elemCount]; i++) {
            TIMElem * elem = [msg getElem:i];
            if ([elem isKindOfClass:[TIMGroupTipsElem class]]) {
                TIMGroupTipsElem * tips_elem = (TIMGroupTipsElem * )elem;
                switch ([tips_elem type]) {
                    case TIM_GROUP_TIPS_TYPE_INVITE:
                        NSLog(@"invite %@ into group %@", [tips_elem userList], [conversation getReceiver]);
                        break;
                    case TIM_GROUP_TIPS_TYPE_QUIT_GRP:
                        NSLog(@"%@ quit group %@", [tips_elem userList], [conversation getReceiver]);
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
示例中注册新消息回调，打印用户进入群组和离开群组的事件通知，其他事件通知用法相同，具体含义可参见下面章节： 

### 用户被邀请加入群组 

触发时机：当有用户被邀请加入群组时，群组内会由系统发出通知，开发者可选择展示样式。可以更新群成员列表。 

收到的消息type为 TIM_GROUP_TIPS_TYPE_INVITE。 

**TIMGroupTipsElem 参数说明：** 

type： TIM_GROUP_TIPS_TYPE_INVITE 
opUser ： 邀请人 
groupName ： 群名 
userList ： 被邀请入群的用户列表 

### 用户退出群组 

触发时机：当有用户主动退群时，群组内会由系统发出通知。可以选择更新群成员列表。 
收到的消息type为 TIM_GROUP_TIPS_TYPE_QUIT_GRP。 

**TIMGroupTipsElem 参数说明：**
type： TIM_GROUP_TIPS_TYPE_QUIT_GRP 
opUser ： 退出用户identifier 
groupName ： 群名 

### 用户退出群组 

触发时机：当有用户主动退群时，群组内会由系统发出通知。可以选择更新群成员列表。 
收到的消息type为 TIM_GROUP_TIPS_TYPE_QUIT_GRP。 

**TIMGroupTipsElem 参数说明：**
type： TIM_GROUP_TIPS_TYPE_QUIT_GRP 
opUser ： 退出用户identifier 
groupName ： 群名 

### 被设置/取消管理员 

触发时机：当有用户被设置为管理员或者被取消管理员身份时，群组内会由系统发出通知。如果界面有显示是否管理员，此时可更新管理员标识。 
收到的消息type为 TIM_GROUP_TIPS_TYPE_SET_ADMIN 和 TIM_GROUP_TIPS_TYPE_CANCEL_ADMIN 。 

**TIMGroupTipsElem 参数说明： **
type： 设置：TIM_GROUP_TIPS_TYPE_SET_ADMIN 
取消：TIM_GROUP_TIPS_TYPE_CANCEL_ADMIN 
opUser ： 操作用户identifier 
groupName ： 群名 
userList ： 被设置/取消管理员身份的用户列表 

### 群资料变更 

触发时机：当群资料变更，如群名、群简介等，会有系统消息发出，可更新相关展示字段。或者选择性把消息展示给用户。 

**TIMGroupTipsElem 参数说明：**
 
type： TIM_GROUP_TIPS_TYPE_INFO_CHANGE 
opUser ： 操作用户identifier 
groupName ： 群名 
groupChangeInfo： 群变更的具体资料信息，为TIMGroupTipsElemGroupInfo 结构体列表 

**TIMGroupTipsElemGroupInfo 原型：**

```
/**
 *  群tips，群变更信息
 */
@interface TIMGroupTipsElemGroupInfo : NSObject

/**
 *  群名，如果没有变更，为 nil
 */
@property(nonatomic,retain) NSString * groupName;

/**
 *  群简介： 没有变更时为 nil
 */
@property(nonatomic,retain) NSString * introduction;

/**
 *  群公告： 没有变更时为 nil
 */
@property(nonatomic,retain) NSString * notification;

/**
 *  群头像： 没有变更时为 nil
 */
@property(nonatomic,retain) NSString * faceUrl;

/**
 *  群主： 没有变更时为 nil
 */
@property(nonatomic,retain) NSString * owner;

@end
```

**参数说明：** 
groupName： 变更后的群名，如果没有变更则为nil 
introduction： 变更后的群简介，如果没有变更则为nil 
notification： 变更后的群公告，如果没有变更则为nil 
faceUrl： 变更后的群头像URL，如果没有变更则为nil 
owner： 变更后的群主，如果没有变更则为nil 

### 群成员资料变更 

触发时机：当群成员的群相关资料变更时，会有系统消息发出，可更新相关字段展示，或者选择性把消息展示给用户。（注意：这里的资料仅跟群相关资料，比如禁言时间、成员角色变更等，不包括用户昵称等本身资料）。
 
**TIMGroupTipsElem 参数说明：**
 
type： TIM_GROUP_TIPS_TYPE_MEMBER_INFO_CHANGE 
opUser ： 操作用户identifier 
groupName ： 群名 
memberInfoList： 变更的群成员的具体资料信息，为TIMGroupTipsElemMemberInfo结构体列表
 
**TIMGroupTipsElemMemberInfo 原型：**
 
```
/**
 *  群tips，成员变更信息
 */
@interface TIMGroupTipsElemMemberInfo : NSObject

/**
 *  变更用户
 */
@property(nonatomic,retain) NSString * identifier;
/**
 *  禁言时间（秒，还剩多少秒可以发言）
 */
@property(nonatomic,assign) uint32_t shutupTime;

@end
```
**参数说明：**
 
identifier： 变更的用户identifier 
shutupTime： 被禁言的时间 

## 群系统消息 

当有用户申请加群等事件发生时，管理员会收到邀请加群系统消息，用户可根据情况接受请求或者拒绝，相应的消息通过群系统消息展示给用户。 
**群系统消息类型定义： **

```
/**
 *  群系统消息类型
 */
typedef NS_ENUM(NSInteger, TIM_GROUP_SYSTEM_TYPE){
    /**
     *  申请加群请求（只有管理员会收到）
     */
    TIM_GROUP_SYSTEM_ADD_GROUP_REQUEST_TYPE              = 0x01,
    /**
     *  申请加群被同意（只有申请人能够收到）
     */
    TIM_GROUP_SYSTEM_ADD_GROUP_ACCEPT_TYPE               = 0x02,
    /**
     *  申请加群被拒绝（只有申请人能够收到）
     */
    TIM_GROUP_SYSTEM_ADD_GROUP_REFUSE_TYPE               = 0x03,
    /**
     *  被管理员踢出群（只有被踢的人能够收到）
     */
    TIM_GROUP_SYSTEM_KICK_OFF_FROM_GROUP_TYPE            = 0x04,
    /**
     *  群被解散（全员能够收到）
     */
    TIM_GROUP_SYSTEM_DELETE_GROUP_TYPE                   = 0x05,
    /**
     *  创建群消息（创建者能够收到）
     */
    TIM_GROUP_SYSTEM_CREATE_GROUP_TYPE                   = 0x06,
    /**
     *  邀请加群（被邀请者能够收到）
     */
    TIM_GROUP_SYSTEM_INVITED_TO_GROUP_TYPE               = 0x07,
    /**
     *  主动退群（主动退群者能够收到）
     */
    TIM_GROUP_SYSTEM_QUIT_GROUP_TYPE                     = 0x08,
    /**
     *  设置管理员(被设置者接收)
     */
    TIM_GROUP_SYSTEM_GRANT_ADMIN_TYPE                    = 0x09,
    /**
     *  取消管理员(被取消者接收)
     */
    TIM_GROUP_SYSTEM_CANCEL_ADMIN_TYPE                   = 0x0a,
    /**
     *  群已被回收(全员接收)
     */
    TIM_GROUP_SYSTEM_REVOKE_GROUP_TYPE                   = 0x0b,
    /**
     *  邀请入群请求(被邀请者接收)
     */
    TIM_GROUP_SYSTEM_INVITE_TO_GROUP_REQUEST_TYPE        = 0x0c,
    /**
     *  邀请加群被同意(只有发出邀请者会接收到)
     */
    TIM_GROUP_SYSTEM_INVITE_TO_GROUP_ACCEPT_TYPE         = 0x0d,
    /**
     *  邀请加群被拒绝(只有发出邀请者会接收到)
     */
    TIM_GROUP_SYSTEM_INVITE_TO_GROUP_REFUSE_TYPE         = 0x0e,
 };


/**
 *  群系统消息
 */
@interface TIMGroupSystemElem : TIMElem

/**
 * 操作类型
 */
@property(nonatomic,assign) TIM_GROUP_SYSTEM_TYPE type;

/**
 * 群组Id
 */
@property(nonatomic,retain) NSString * group;

/**
 * 操作人
 */
@property(nonatomic,retain) NSString * user;

/**
 * 操作理由
 */
@property(nonatomic,retain) NSString * msg;


/**
 *  消息标识，客户端无需关心
 */
@property(nonatomic,assign) uint64_t msgKey;

/**
 *  消息标识，客户端无需关心
 */
@property(nonatomic,retain) NSData * authKey;

/**
 *  操作人资料
 */
@property(nonatomic,retain) TIMUserProfile * opUserInfo;

/**
 *  操作人群成员资料
 */
@property(nonatomic,retain) TIMGroupMemberInfo * opGroupMemberInfo;

/**
 *  同意申请，目前只对申请加群和被邀请入群消息生效
 *
 *  @param msg  同意理由，选填
 *  @param succ 成功回调
 *  @param fail 失败回调，返回错误码和错误描述
 */
- (void) accept:(NSString*)msg succ:(TIMSucc)succ fail:(TIMFail)fail;

/**
 *  拒绝申请，目前只对申请加群和被邀请入群消息生效
 *
 *  @param msg  拒绝理由，选填
 *  @param succ 成功回调
 *  @param fail 失败回调，返回错误码和错误描述
 */
- (void) refuse:(NSString*)msg succ:(TIMSucc)succ fail:(TIMFail)fail;

@end
```
**参数说明：**
type ： 消息类型 
group ： 群组Id 
user ： 操作人 
msg ： 操作理由 
msgKey & authKey ： 消息的标识，客户端无需关心，调用accept和refuse时由SDK读取 

**示例： **

```
@interface TIMMessageListenerImpl : NSObject- (void)onNewMessage:(NSArray*) msgs;
@end

@implementation TIMMessageListenerImpl
- (void)onNewMessage:(NSArray*) msgs {
    for (TIMMessage * msg in msgs) {
        for (int i = 0; i < [msg elemCount]; i++) {
            TIMElem * elem = [msg getElem:i];
            if ([elem isKindOfClass:[TIMGroupSystemElem class]]) {
                TIMGroupSystemElem * system_elem = (TIMGroupSystemElem * )elem;
                switch ([system_elem type]) {
                    case TIM_GROUP_SYSTEM_ADD_GROUP_REQUEST_TYPE:
                        NSLog(@"user %@ request join group  %@", [system_elem user], [system_elem group]);
                        break;
                    case TIM_GROUP_SYSTEM_DELETE_GROUP_TYPE:
                        NSLog(@"group %@ deleted by %@", [system_elem group], [system_elem user]);
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
示例中收到群系统消息，如果是入群申请，默认同意，如果是群解散通知，打印信息。其他类型消息解析方式相同。 

### 申请加群消息 

触发时机：当有用户申请加群时，群管理员会收到申请加群消息，可展示给用户，由用户决定是否同意对方加群，如果同意，调用accept方法，拒绝调用refuse方法。 
消息类型为：TIM_GROUP_SYSTEM_ADD_GROUP_REQUEST_TYPE 

**参数说明：**
 
type ： TIM_GROUP_SYSTEM_ADD_GROUP_REQUEST_TYPE 
group ： 群组Id，表示是哪个群的申请 
user ： 申请人 
msg ： 申请理由，（可选） 

**方法说明：**
 
当同意申请人入群，可调用accept方法 
当不同意申请人入群，可调用refuse方法。 

### 申请加群同意/拒绝消息 

触发时机：当管理员同意加群请求时，申请人会收到同意入群的消息，当管理员拒绝时，收到拒绝入群的消息。 

**参数说明：**
 
type ： 同意：TIM_GROUP_SYSTEM_ADD_GROUP_ACCEPT_TYPE 
拒绝：TIM_GROUP_SYSTEM_ADD_GROUP_REFUSE_TYPE 
group ： 群组Id，表示是哪个群通过/拒绝了 
user ： 处理请求的管理员identifier 
msg ： 同意或者拒绝理由（可选） 

### 邀请入群消息 

触发时机：当有用户被邀请群时，该用户会收到邀请入群消息，可展示给用户，由用户决定是否同意入群，如果同意，调用accept方法，拒绝调用refuse方法。 
消息类型为：TIM_GROUP_SYSTEM_INVITE_TO_GROUP_REQUEST_TYPE 

**参数说明：**
 
type ： TIM_GROUP_SYSTEM_INVITE_TO_GROUP_REQUEST_TYPE 
group ： 群组Id，表示是哪个群的邀请 
user ： 邀请人 

**方法说明：**
 
当同意邀请入群，可调用accept方法 
当不同意邀请入群，可调用refuse方法。

### 邀请入群同意/拒绝消息 

触发时机：当被邀请者同意入群请求时，申请人会收到同意入群的消息，当管理员拒绝时，收到拒绝入群的消息。 

**参数说明：**
 
type ： 同意：TIM_GROUP_SYSTEM_INVITE_TO_GROUP_ACCEPT_TYPE 
拒绝：TIM_GROUP_SYSTEM_INVITE_TO_GROUP_REFUSE_TYPE 
group ： 群组Id，表示是对哪个群通过/拒绝了 
user ： 处理请求的用户identifier 
msg ： 同意或者拒绝理由（可选） 

### 被管理员踢出群组 

触发时机：当用户被管理员踢出群组时，申请人会收到被踢出群的消息。 

**参数说明：**
 
type ： TIM_GROUP_SYSTEM_KICK_OFF_FROM_GROUP_TYPE 
group ： 群组Id，表示在哪个群里被踢了 
user ： 操作管理员identifier 

### 群被解散 

触发时机：当群被解散时，全员会收到解散群消息。 

**参数说明：**
 
type ： TIM_GROUP_SYSTEM_DELETE_GROUP_TYPE 
group ： 群组Id，表示哪个群被解散了 
user ： 操作管理员identifier 

### 创建群消息 

触发时机：当群创建时，创建者会收到创建群消息。 
当调用创建群方法成功回调后，即表示创建成功，此消息主要为多终端同步，如果有在其他终端登录，作为更新群列表的时机，本终端可以选择忽略。 

**参数说明：**
 
type ： TIM_GROUP_SYSTEM_CREATE_GROUP_TYPE 
group ： 群组Id，表示创建的群Id 
user ： 创建者，这里也就是用户自己 

### 邀请加群 

触发时机：当用户被邀请加入群组时，该用户会收到邀请消息，注意：创建群组时初始成员无需邀请即可入群。 

**参数说明：**
 
type ： TIM_GROUP_SYSTEM_INVITED_TO_GROUP_TYPE 
group ： 群组Id，邀请进入哪个群 
user ： 操作人，表示哪个用户的邀请 

**方法说明：**
 
当用户同意入群，可调用accept方法 
当用户不同意，可调用refuse方法。 

### 主动退群 

触发时机：当用户主动退出群组时，该用户会收到退群消息，只有退群的用户自己可以收到。 
当用户调用QuitGroup时成功回调返回，表示已退出成功，此消息主要为了多终端同步，其他终端可以作为更新群列表的时机，本终端可以选择忽略。 

**参数说明：**
 
type ： TIM_GROUP_SYSTEM_QUIT_GROUP_TYPE 
group ： 群组Id，表示退出的哪个群 
user ： 操作人，这里即为用户自己 

### 设置/取消管理员 

触发时机：当用户被设置为管理员时，可收到被设置管理员的消息通知，当用户被取消管理员时，可收到取消通知，可提示用户。 

**参数说明：**
 
type ： 取消管理员身份:TIM_GROUP_SYSTEM_GRANT_ADMIN_TYPE 
授予管理员身份：TIM_GROUP_SYSTEM_CANCEL_ADMIN_TYPE 
group ： 群组Id，表示哪个群的事件 
user ： 操作人 

### 群被回收 

触发时机：当群组被系统回收时，全员可收到群组被回收消息。 

**参数说明：**
 
type ： TIM_GROUP_SYSTEM_REVOKE_GROUP_TYPE 
group ： 群组Id，表示哪个群被回收了 


## 群事件通知回调 

当群内资料或者成员变更时，会有群事件通知的回调，用户可以监听回调进行业务逻辑处理，如更新成员列表、更新群组资料显示等操作。 

**原型： **

```
@interface TIMManager : NSObject
/**
 *  设置群组事件回调
 *
 *  @param listener 回调
 *
 *  @return 0 成功
 */
-(int) setGroupEventListener: (id)listener;

@end
```
**参数说明：** 

listener   群事件通知回调，参考TIMGroupTipsListener协议，TIMGroupTipsElem 内容和含义同群事件消息。 

