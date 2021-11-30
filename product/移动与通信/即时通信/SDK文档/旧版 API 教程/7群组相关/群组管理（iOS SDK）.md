
## 群组综述

即时通信 IM 有多种群组类型，其特点以及限制因素可参考 [群组系统](https://cloud.tencent.com/document/product/269/1502)。群组使用唯一 ID 标识，通过群组 ID 可以进行不同操作。

## 群组消息

群组消息与 C2C （单聊）消息相同，仅在获取 `Conversation` 时的会话类型不同，请参见 [消息发送](https://cloud.tencent.com/document/product/269/9150#.E6.B6.88.E6.81.AF.E5.8F.91.E9.80.81) 。

## 群组管理

群组相关操作都由 `TIMGroupManager` 实现，需要用户登录成功后操作。

**获取单例原型：**

```
@interface TIMGroupManager : NSObject
+ (TIMGroupManager*)sharedInstance;
@end
```

### 创建内置类型群组

即时通信 IM 中内置了**私有群（Private）、公开群（Public）、 聊天室（ChatRoom）、音视频聊天室（AVChatRoom）和在线成员广播大群（BChatRoom）**群组类型，详情请参见 [群组类型介绍](https://cloud.tencent.com/document/product/269/1502#GroupType)。创建时可指定群组名称以及要加入的用户列表，创建成功后返回群组 ID，可通过群组 ID 获取 `Conversation` 收发消息等。

**创建群组说明：**

| 方法 | 说明 |
| --- | --- |
| CreatePrivateGroup | 创建私有群 |
| CreatePublicGroup | 创建公开群 |
| CreateChatRoomGroup | 创建聊天室 |
| CreateAVChatRoomGroup | 创建直播大群，此类型群可以加入人数不做限制，但是有一些能力上的限制，如不能拉人，不能查询总人数等 |

**原型：**

```
@interface TIMGroupManager : NSObject
/**
 *  创建私有群
 *
 *  @param members   群成员，NSString* 数组
 *  @param groupName 群名
 *  @param succ      成功回调
 *  @param fail      失败回调
 *
 *  @return 0 成功
 */
- (int)createPrivateGroup:(NSArray*)members groupName:(NSString*)groupName succ:(TIMCreateGroupSucc)succ fail:(TIMFail)fail;
/**
 *  创建公开群
 *
 *  @param members   群成员，NSString* 数组
 *  @param groupName 群名
 *  @param succ      成功回调
 *  @param fail      失败回调
 *
 *  @return 0 成功
 */
- (int)createPublicGroup:(NSArray*)members groupName:(NSString*)groupName succ:(TIMCreateGroupSucc)succ fail:(TIMFail)fail;
/**
 *  创建聊天室
 *
 *  @param members   群成员，NSString* 数组
 *  @param groupName 群名
 *  @param succ      成功回调
 *  @param fail      失败回调
 *
 *  @return 0 成功
 */
- (int)createChatRoomGroup:(NSArray*)members groupName:(NSString*)groupName succ:(TIMCreateGroupSucc)succ fail:(TIMFail)fail;
/**
 *  创建音视频聊天室（可支持超大群，详情可参考wiki文档）
 *
 *  @param groupName 群名
 *  @param succ      成功回调
 *  @param fail      失败回调
 *
 *  @return 0 成功
 */
- (int)createAVChatRoomGroup:(NSString*)groupName succ:(TIMCreateGroupSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数 | 说明
---|---
members | NSString 列表，指定加入群组的成员，创建者默认加入，无需指定（公开群、聊天室、私有群内最多6000人，直播大群没有限制）
groupName | NSString 类型，指定群组名称（最长 30 字节）
groupId | NSString 类型，指定群组 ID
succ | 成功回调，返回群组 ID
fail | 失败回调

以下示例创建一个私有群组，并且把用户『iOS_002』拉入群组。 **示例：**

>?
>- 创建者默认加入群组，无需显式指定。
>- 公开群和聊天室调用方式和参数相同，仅方法名不同。

```
NSMutableArray * members = [[NSMutableArray alloc] init];
// 添加一个用户 iOS_002
[members addObject:@"iOS_002"];
[[TIMGroupManager sharedInstance] createPrivateGroup:members groupName:@"GroupName" succ:^(NSString * group) {
	NSLog(@"create group succ, sid=%@", group);
} fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

### 创建指定属性群组

在创建群组时，除了设置默认的成员以及群名外，还可以设置如群公告、群简介等字段。

```
/**
 *  创建群参数
 */
@interface TIMCreateGroupInfo : TIMCodingModel
/**
 *  群组 ID,nil 则使用系统默认 ID
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
 *  是否设置入群选项，Private 类型群组请设置为 false
 */
@property(nonatomic,assign) BOOL setAddOpt;
/**
 *  入群选项
 */
@property(nonatomic,assign) TIMGroupAddOpt addOpt;
/**
 *  最大成员数，填 0 则系统使用默认值
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
 *  自定义字段集合,key 是 NSString* 类型，value 是 NSData* 类型
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
- (int)createGroup:(TIMCreateGroupInfo*)groupInfo succ:(TIMCreateGroupSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
groupInfo|可设置群 ID、群名、群类型、入群选项、最大成员数、群公告、群简介、群头像等
succ|成功回调
fail|失败回调

以下示例创建一个指定属性的私有群，并把用户 『iOS_001』加入群组，创建者默认加入群，无需显示指定。**示例：**

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
[[TIMGroupManager sharedInstance] createGroup:groupInfo succ:^(NSString * group) {
	NSLog(@"create group succ, sid=%@", group);
} fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

### 自定义群组 ID 创建群组

默认创建群组时，通讯云 IM 服务器会生成一个唯一的 ID，以便后续操作，另外，如果用户需要自定义群组 ID，在创建时可指定 ID，通过 [创建指定属性群组](#.E5.88.9B.E5.BB.BA.E6.8C.87.E5.AE.9A.E5.B1.9E.E6.80.A7.E7.BE.A4.E7.BB.84) 也可以实现自定义群组 ID 的功能。

```
@interface TIMGroupManager : NSObject
/**
 *  创建群组
 *
 *  @param type       群类型,Private,Public,ChatRoom,AVChatRoom
 *  @param groupId    自定义群组 ID，为空时系统自动分配
 *  @param groupName  群组名称
 *  @param succ       成功回调
 *  @param fail       失败回调
 *
 *  @return 0 成功
 */
- (int)createGroup:(NSString*)type groupId:(NSString*)groupId groupName:(NSString*)groupName succ:(TIMCreateGroupSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
type|群组类型
members|初始成员列表
groupName|群组名称
groupId|自定义群组 ID
succ|成功回调
fail|失败回调

### 邀请用户入群

`TIMGroupManager` 的接口 `inviteGroupMember` 可以邀请用户进入群组。

**权限说明：**

详情请参见 [加群方式差异](https://cloud.tencent.com/document/product/269/1502#.E5.8A.A0.E7.BE.A4.E6.96.B9.E5.BC.8F.E5.B7.AE.E5.BC.82)。 

**原型：**

```
@interface TIMGroupManager : NSObject
/**
 *  邀请好友入群
 *
 *  @param group   群组 ID
 *  @param members 要加入的成员列表（NSString* 类型数组）
 *  @param succ    成功回调
 *  @param fail    失败回调
 *
 *  @return 0 成功
 */
- (int)inviteGroupMember:(NSString*)group members:(NSArray*)members succ:(TIMGroupMemberSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | NSString 类型，群组 ID
members | NSString 列表，加入群组用户列表
succ | 成功回调，TIMGroupMemberResult 数组，返回成功加入群组的用户列表以及成功状态
fail | 失败回调

以下示例中邀请好友『iOS_002』加入群组 ID『TGID1JYSZEAEQ』，成功后返回操作列表以及成功状态，其中 `result.status` 表示当前用户操作是否成功。 **示例：**

```
NSMutableArray * members = [[NSMutableArray alloc] init];
// 添加一个用户 iOS_002
[members addObject:@"iOS_002"];
// @"TGID1JYSZEAEQ" 为群组 ID
[[TIMGroupManager sharedInstance] inviteGroupMember:@"TGID1JYSZEAEQ" members:members succ:^(NSArray* arr) {
	for (TIMGroupMemberResult * result in arr) {
		NSLog(@"user %@ status %d", result.member, result.status);
	}
} fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

**`result.status` 原型：**

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
    /**
    *  等待处理，邀请入群时等待对方处理
    */
    TIM_GROUP_MEMBER_STATUS_PENDING           = 3,
};
```

### 申请加入群组

`TIMGroupManager` 的接口 `joinGroup` 可以主动申请进入群组。此操作只对公开群、聊天室和音视频聊天室。

**权限说明：**
详情请参见 [加群方式差异](https://cloud.tencent.com/document/product/269/1502#.E5.8A.A0.E7.BE.A4.E6.96.B9.E5.BC.8F.E5.B7.AE.E5.BC.82)。

**原型：**

```
@interface TIMGroupManager : NSObject
/**
 *  申请加群
 *
 *  @param group 申请加入的群组 ID
 *  @param msg   申请消息
 *  @param succ  成功回调（申请成功等待审批）
 *  @param fail  失败回调
 *
 *  @return 0 成功
 */
- (int)joinGroup:(NSString*)group msg:(NSString*)msg succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | NSString 类型，群组 ID
msg  | 申请理由
succ | 成功回调
fail | 失败回调

以下示例中用户申请加入群组『TGID1JYSZEAEQ』，申请理由为『Apply Join Group』。**示例：**

```
[[TIMGroupManager sharedInstance] joinGroup:@"TGID1JYSZEAEQ" msg:@"Apply Join Group" succ:^(){
	NSLog(@"Join Succ");
}fail:^(int code, NSString * err) {
	NSLog(@"code=%d, err=%@", code, err);
}];
```

### 退出群组

群组成员可以主动退出群组。

**权限说明：**

- **私有群：**全员可退出群组。
- **公开群、聊天室、直播大群：**群主不能退出。

详情请参见 [成员管理能力差异](https://cloud.tencent.com/document/product/269/1502#.E6.88.90.E5.91.98.E7.AE.A1.E7.90.86.E8.83.BD.E5.8A.9B.E5.B7.AE.E5.BC.82)。

**原型：**

```
@interface TIMGroupManager : NSObject
/**
 *  主动退出群组
 *
 *  @param group 群组 ID
 *  @param succ  成功回调
 *  @param fail  失败回调
 *
 *  @return 0 成功
 */
- (int)quitGroup:(NSString*)group succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | NSString 类型，群组 ID
succ | 成功回调
fail | 失败回调

以下示例中主动退出群组 『TGID1JYSZEAEQ』。 **示例：**

```
// @"TGID1JYSZEAEQ" 为群组 ID
[[TIMGroupManager sharedInstance] quitGroup:@"TGID1JYSZEAEQ" succ:^() {
	NSLog(@"succ");
} fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

### 删除群组成员

群组成员也可以删除其他成员，函数参数信息与加入群组相同。

**权限说明：**
详情请参见 [成员管理能力差异](https://cloud.tencent.com/document/product/269/1502#.E6.88.90.E5.91.98.E7.AE.A1.E7.90.86.E8.83.BD.E5.8A.9B.E5.B7.AE.E5.BC.82)。

**原型：**

```
@interface TIMGroupManager : NSObject
/**
 *  删除群成员
 *
 *  @param group   群组 ID
 *  @param reason  删除原因
 *  @param members 要删除的成员列表
 *  @param succ    成功回调
 *  @param fail    失败回调
 *
 *  @return 0 成功
 */
- (int)deleteGroupMemberWithReason:(NSString*)group reason:(NSString*)reason members:(NSArray*)members succ:(TIMGroupMemberSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | NSString 类型，群组 ID
reason | NSString 类型，原因
members | `NSString*` 数组，被操作的用户列表
succ | 成功回调，`TIMGroupMemberResult` 数组，返回成功加入群组的用户列表已经成功状态
fail | 失败回调

以下示例中把好友『iOS_002』从群组『TGID1JYSZEAEQ』中删除，执行成功后返回操作列表以及操作状态。 **示例：**

```
NSMutableArray * members = [[NSMutableArray alloc] init];
// 添加一个用户 iOS_002
[members addObject:@"iOS_002"];
// @"TGID1JYSZEAEQ" 为群组 ID
[[TIMGroupManager sharedInstance] deleteGroupMemberWithReason:@"TGID1JYSZEAEQ" reason:@"违反群规则" members:members succ:^(NSArray* arr) {
	for (TIMGroupMemberResult * result in arr) {
		NSLog(@"user %@ status %d", result.member, result.status);
	}
} fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

### 获取群成员列表

`getGroupMembers` 方法可获取群内成员列表。

**权限说明：**

- **任何群组类型：**都可以获取成员列表。
- **直播大群：**只能拉取部分成员（包括群主、管理员和部分成员）。

详情请参见 [群组基础能力操作差异](https://cloud.tencent.com/document/product/269/1502#.E7.BE.A4.E7.BB.84.E5.9F.BA.E7.A1.80.E8.83.BD.E5.8A.9B.E6.93.8D.E4.BD.9C.E5.B7.AE.E5.BC.82)。 

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
 *  自定义字段集合,key 是 NSString*类型,value 是 NSData*类型
 */
@property(nonatomic,retain) NSDictionary* customInfo;
@end

@interface TIMGroupManager : NSObject
/**
 *  获取群成员列表
 *
 *  @param group 群组 ID
 *  @param succ  成功回调(TIMGroupMemberInfo列表)
 *  @param fail  失败回调
 *
 *  @return 0 成功
 */
- (int)getGroupMembers:(NSString*)groupId succ:(TIMGroupMemberSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | NSString\* 类型，群组 ID
succ | 成功回调（返回 TIMGroupMemberInfo\* 数组）
fail | 失败回调

以下示例中获取群『TGID1JYSZEAEQ』的成员列表，`list` 为 `TIMGroupMemberInfo*` 数据，存储成员的相关信息。 **示例：**

```
// @"TGID1JYSZEAEQ" 为群组 ID
[[TIMGroupManager sharedInstance] getGroupMembers:@"TGID1JYSZEAEQ" succ:^(NSArray* list) {
	for (TIMGroupMemberInfo * info in list) {
		NSLog(@"user=%@ joinTime=%lu role=%d", info.member, info.joinTime, info.role);
	}
} fail:^(int code, NSString * err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

如果群组人数过多，建议使用**分页接口**。**原型：**

```
@interface TIMGroupManager : NSObject
/**
 *  获取指定类型的成员列表（支持按字段拉取，分页）
 *
 *  @param group      群组 ID：（NSString*) 列表
 *  @param filter     群成员角色过滤方式
 *  @param flags      拉取资料标志
 *  @param custom     要获取的自定义 key（NSString*）列表
 *  @param nextSeq    分页拉取标志，第一次拉取填0，回调成功如果不为零，需要分页，传入再次拉取，直至为0
 *  @param succ       成功回调
 *  @param fail       失败回调
 */
- (int)getGroupMembers:(NSString*)group ByFilter:(TIMGroupMemberFilter)filter flags:(TIMGetGroupMemInfoFlag)flags custom:(NSArray*)custom nextSeq:(uint64_t)nextSeq succ:(TIMGroupMemberSuccV2)succ fail:(TIMFail)fail;
@end
```

### 获取加入的群组列表

通过 `getGroupList` 可以获取当前用户加入的所有群组。

**权限说明：**

- 可以获取自己所加入的群列表，返回的 `TIMGroupInfo` 只包含 `group`、`groupName`、`groupType` 信息。
- 只能获得加入的部分直播大群的列表。

**原型：**

```
@interface TIMGroupManager : NSObject
/**
 *  获取群列表
 *
 *  @param succ 成功回调，NSArray 列表为 TIMGroupInfo，结构体只包含 group\groupName\groupType\faceUrl\selfInfo 信息
 *  @param fail 失败回调
 *
 *  @return 0 成功
 */
- (int)getGroupList:(TIMGroupListSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
succ | 成功回调，返回群组 ID 列表，TIMGroupInfo 数组
fail | 失败回调

以下示例中获取群组列表，并打印群组 ID，群类型（Private、Public、ChatRoom）以及群名。**示例：**

```
[[TIMGroupManager sharedInstance] getGroupList:^(NSArray * list) {
	for (TIMGroupInfo * info in list) {
		NSLog(@"group=%@ type=%@ name=%@", info.group, info.groupType, info.groupName);
	}
} fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

### 解散群组

通过 `DeleteGroup` 可以解散群组。

**权限说明：**

详情请参见 [群组基础能力操作差异](https://cloud.tencent.com/document/product/269/1502#.E7.BE.A4.E7.BB.84.E5.9F.BA.E7.A1.80.E8.83.BD.E5.8A.9B.E6.93.8D.E4.BD.9C.E5.B7.AE.E5.BC.82)。 


**原型：**

```
@interface TIMGroupManager : NSObject

/**
 *  解散群组
 *
 *  @param group 群组 ID
 *  @param succ  成功回调
 *  @param fail  失败回调
 *
 *  @return 0 成功
 */
- (int)deleteGroup:(NSString*)group succ:(TIMSucc)succ fail:(TIMFail)fail;

@end
```

**参数说明：**

参数 | 说明
---|---
group | 群组 ID
succ | 成功回调，返回群组 ID 列表，NSString 数组
fail | 失败回调

以下示例中解散群组『TGID1JYSZEAEQ』。**示例：**

```
[[TIMGroupManager sharedInstance] deleteGroup:@"TGID1JYSZEAEQ" succ:^() {
	NSLog(@"delete group succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

### 转让群组

通过 `modifyGroupOwner` 可以转让群组。

**权限说明：**

- 只有**群主**才有权限进行群转让操作。
- **直播大群**不能进行群转让操作。

**原型：**

```
@interface TIMGroupManager : NSObject
/**
 *  转让群给新群主
 *
 *  @param group      群组 ID
 *  @param identifier 新的群主 ID
 *  @param succ       成功回调
 *  @param fail       失败回调
 *
 *  @return 0 成功
 */
- (int)modifyGroupOwner:(NSString*)group user:(NSString*)identifier succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | 群组 ID
user| 用户 ID
succ | 成功回调
fail | 失败回调

以下示例中转让群组『TGID1JYSZEAEQ』给用户『iOS_001』。 **示例：**

```
[[TIMGroupManager sharedInstance] modifyGroupOwner:@"TGID1JYSZEAEQ" user:@"iOS_001" succ:^() {
	NSLog(@"set new owner succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

### 全员禁言

通过 `modifyGroupAllShutup` 可以设置群组全员禁言。

**权限说明：**

- **群主、管理员：**有权限进行全员禁言的操作。
- **所有群组类型：**都支持全员禁言的操作。

**原型：**

```
@interface TIMGroupManager : NSObject
/**
 *  修改群组全员禁言属性
 *
 *  @param group   群组 ID
 *  @param shutup  是否禁言
 *  @param succ    成功回调
 *  @param fail    失败回调
 *
 *  @return 0 成功
 */
- (int)modifyGroupAllShutup:(NSString*)group shutup:(BOOL)shutup succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | 群组 ID
shutup | 是否设置为禁言
succ | 成功回调
fail | 失败回调

示例中设置群组『TGID1JYSZEAEQ』为全员禁言的状态。客户端可以通过 `getGroupList` 和 `getGroupInfo` 接口获取当前群组全员禁言的属性。**示例：**

```
[[TIMGroupManager sharedInstance] modifyGroupAllShutup:@"TGID1JYSZEAEQ" shutup:YES succ:^() {
	NSLog(@"set all shutup succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

## 获取群资料

### 获取群组资料

通过 `TIMGroupManager` 的方法 `getGroupInfo` 方法可以获取服务器存储的群组资料，`queryGroupInfo`  方法可以获取本地存储的群组资料，群资料信息由 `TIMGroupInfo` 定义。  

**权限说明：**

- 无论是公开群还是私有群，群成员均可以拉到群组资料。
- 如果是公开群，非群组成员可以拉到 group、groupName、owner、groupType、createTime、maxMemberNum、memberNum、introduction、faceURL、addOpt、onlineMemberNum、customInfo 这些资料字段。如果是私有群，非群组成员拉取不到群组资料。

**原型：**

```
/**
 *  群资料信息
 */
@interface TIMGroupInfo : TIMCodingModel
/**
 *  群组 ID
 */
@property(nonatomic,retain) NSString* group;
/**
 *  群名
 */
@property(nonatomic,retain) NSString* groupName;
/**
 *  群创建人/管理员
 */
@property(nonatomic,retain) NSString * owner;
/**
 *  群类型：Private、Public 和 ChatRoom
 */
@property(nonatomic,retain) NSString* groupType;
/**
 *  群创建时间
 */
@property(nonatomic,assign) uint32_t createTime;
/**
 *  最近一次群资料修改时间
 */
@property(nonatomic,assign) uint32_t lastInfoTime;
/**
 *  最近一次发消息时间
 */
@property(nonatomic,assign) uint32_t lastMsgTime;
/**
 *  最大成员数
 */
@property(nonatomic,assign) uint32_t maxMemberNum;
/**
 *  群成员数量
 */
@property(nonatomic,assign) uint32_t memberNum;
/**
 *  入群类型
 */
@property(nonatomic,assign) TIMGroupAddOpt addOpt;
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
 *  最后一条消息
 */
@property(nonatomic,retain) TIMMessage* lastMsg;
/**
 *  在线成员数量
 */
@property(nonatomic,assign) uint32_t onlineMemberNum;
/**
 *  群组是否被搜索类型
 */
@property(nonatomic,assign) TIMGroupSearchableType isSearchable;
/**
 *  群组成员可见类型
 */
@property(nonatomic,assign) TIMGroupMemberVisibleType isMemberVisible;
/**
 *  是否全员禁言
 */
@property(nonatomic,assign) BOOL allShutup;
/**
 *  群组中的本人信息
 */
@property(nonatomic,retain) TIMGroupSelfInfo* selfInfo;
/**
 *  自定义字段集合，key 是 NSString* 类型，value 是 NSData* 类型
 */
@property(nonatomic,retain) NSDictionary* customInfo;
@end

@interface TIMGroupManager : NSObject
/**
 *  获取服务器存储的群资料
 *
 *  @param groups 群组 ID 列表
 *  @param succ 成功回调，不包含 selfInfo 信息
 *  @param fail 失败回调
 *
 *  @return 0 成功
 */
- (int)getGroupInfo:(NSArray*)groups succ:(TIMGroupListSucc)succ fail:(TIMFail)fail;
/**
 *  获取本地存储的群资料
 *
 *  @param group 群组 ID
 *
 *  @return 群组资料
 */
- (TIMGroupInfo *)queryGroupInfo:(NSString *)group;
@end
```

**参数说明：**

参数|说明
---|---
groups |NSString 数组，需要获取资料的群组列表
succ | 成功回调，返回群组资料列表，TIMGroupInfo 数组
fail | 失败回调

以下示例中获取群组『TGID1JYSZEAEQ』的详细信息。 **示例：**

```
NSMutableArray * groupList = [[NSMutableArray alloc] init];
[groupList addObject:@"TGID1JYSZEAEQ"];
[[TIMGroupManager sharedInstance] getGroupInfo:groupList succ:^(NSArray * groups) {
	for (TIMGroupInfo * info in groups) {
		NSLog(@"get group succ, infos=%@", info);
	}
} fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

### 获取本人在群里的资料

**权限说明：**

**直播大群：**不能拉取到本人资料。

**原型：**

```
@interface TIMGroupManager : NSObject
/**
 *  获取本人在群组内的成员信息
 *
 *  @param group 群组 ID
 *  @param succ  成功回调，返回信息
 *  @param fail  失败回调
 *
 *  @return 0 成功
 */
- (int)getGroupSelfInfo:(NSString*)groupId succ:(TIMGroupSelfSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
groupId | 群组 ID
succ |  成功回调，返回用户本人在群内的资料
fail | 失败回调

### 获取指定成员在群里的资料

**权限说明：**

**直播大群：**只能获得部分成员的资料（包括群主、管理员和部分群成员）。

**原型：**

```
@interface TIMGroupManager : NSObject
/**
 *
 *  获取群组指定成员的信息，需要设置群成员 members，其他限制参考 getGroupMembers
 *
 *  @param groupId 群组 ID
 *  @param members 成员 ID（NSString*）列表
 *  @param succ    成功回调 (TIMGroupMemberInfo 列表)
 *  @param fail    失败回调
 *
 *  @return 0：成功；1：失败
 */
- (int)getGroupMembersInfo:(NSString*)groupId members:(NSArray<NSString *>*)members succ:(TIMGroupMemberSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
groupId | 群组 ID
members | 成员 ID 列表
succ |  成功回调，返回群成员资料列表
fail | 失败回调

## 修改群资料

### 修改群名

通过 `modifyGroupName` 可以修改群组名称。

**权限说明：**

- **公开群、聊天室和直播大群：**只有群主或者管理员可以修改群名。
- **私有群：**任何人可修改群名。

**原型：**

```
@interface TIMGroupManager : NSObject
/**
 *  修改群名
 *
 *  @param group     群组 ID
 *  @param groupName 新群名
 *  @param succ      成功回调
 *  @param fail      失败回调
 *
 *  @return 0 成功
 */
- (int)modifyGroupName:(NSString*)group groupName:(NSString*)groupName succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数 | 说明
---|---
group | 群组 ID
groupName | 修改后的群名
succ | 成功回调
fail | 失败回调

以下示例修改群『TGID1JYSZEAEQ』的名字为『ModifyGroupName』。**示例：**

```
[[TIMGroupManager sharedInstance] modifyGroupName:@"TGID1JYSZEAEQ" groupName:@"ModifyGroupName" succ:^() {
	NSLog(@"modify group name succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

### 修改群简介

通过 `modifyGroupIntroduction` 可以修改群组简介。

**权限说明：**

- **公开群、聊天室、直播大群：**只有群主或者管理员可以修改群简介。
- **私有群：**任何人可修改群简介。

**原型：**

```
@interface TIMGroupManager : NSObject

/**
 *  修改群简介
 *
 *  @param group            群组 ID
 *  @param introduction     群简介
 *  @param succ             成功回调
 *  @param fail             失败回调
 *
 *  @return 0 成功
 */
- (int)modifyGroupIntroduction:(NSString*)group introduction:(NSString*)introduction succ:(TIMSucc)succ fail:(TIMFail)fail;

@end
```

**参数说明：**

参数 |说明
---|---
group |  群组 ID
introduction | 群简介，简介最长120字节
succ | 成功回调
fail | 失败回调

**示例：**

```
[[TIMGroupManager sharedInstance] modifyGroupIntroduction:@"TGID1JYSZEAEQ" introduction :@"this is one group" succ:^() {
	NSLog(@"modify group introduction succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

### 修改群公告

通过 `modifyGroupNotification` 可以修改群组公告。

**权限说明：**

- **公开群、聊天室、直播大群：**只有群主或者管理员可以修改群公告。
- **私有群：**任何人可修改群公告。

**原型：**

```
@interface TIMGroupManager : NSObject
/**
 *  修改群公告
 *
 *  @param group            群组 ID
 *  @param notification     群公告（最长150字节）
 *  @param succ             成功回调
 *  @param fail             失败回调
 *
 *  @return 0 成功
 */
- (int)modifyGroupNotification:(NSString*)group notification:(NSString*)notification succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | 群组 ID
notification | 群公告，群公告最长150字节
succ | 成功回调
fail | 失败回调

以下示例修改群『TGID1JYSZEAEQ』的公告为『test notification』。 **示例：**

```
[[TIMGroupManager sharedInstance] modifyGroupNotification:@"TGID1JYSZEAEQ" notification:@"test notification" succ:^() {
	NSLog(@"modify group notification succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

### 修改群头像

通过 `modifyGroupFaceUrl` 可以修改群头像。

**权限说明：**

- **公开群、聊天室、直播大群：**只有群主或者管理员可以修改群头像。
- **私有群：**任何人可修改群头像。

**原型：**

```
@interface TIMGroupManager : NSObject
/**
 *  修改群头像
 *
 *  @param group            群组 ID
 *  @param url              群头像地址（最长100字节）
 *  @param succ             成功回调
 *  @param fail             失败回调
 *
 *  @return 0 成功
 */
- (int)modifyGroupFaceUrl:(NSString*)group url:(NSString*)url succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | 群组 ID
url| 群头像地址（最长100字节）
succ | 成功回调
fail | 失败回调

**示例：**

```
[[TIMGroupManager sharedInstance] modifyGroupFaceUrl:@"TGID1JYSZEAEQ" notification:@"http://test/x.jpg" succ:^() {
	NSLog(@"modify group face url succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

### 修改加群选项

通过 `modifyGroupAddOpt` 可以修改加群选项。

**权限说明：**

- **公开群、聊天室、直播大群：**只有群主或者管理员可以修改加群选项。
- **私有群：**只能通过邀请加入群组，不能主动申请加入某个群组。

**原型：**

```
@interface TIMGroupManager : NSObject

/**
 *  修改加群选项
 *
 *  @param group            群组 ID
 *  @param opt              加群选项，详见 TIMGroupAddOpt
 *  @param succ             成功回调
 *  @param fail             失败回调
 *
 *  @return 0 成功
 */
- (int)modifyGroupAddOpt:(NSString*)group opt:(TIMGroupAddOpt)opt succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | 群组 ID
opt| 加群选项，可设置为允许任何人加入、需要审核、禁止任何人加入
succ | 成功回调
fail | 失败回调

以下示例修改群『TGID1JYSZEAEQ』为禁止任何人加入。 **示例：**

```
[[TIMGroupManager sharedInstance] modifyGroupAddOpt:@"TGID1JYSZEAEQ" opt:TIM_GROUP_ADD_FORBID succ:^() {
	NSLog(@"modify group opt succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

### 修改群维度自定义字段

通过 `modifyGroupCustomInfo` 可以对群维度自定义字段进行修改。

**权限说明：**

- 通过后台配置相关的 key 和权限。

**原型： **

```
@interface TIMGroupManager : NSObject
/**
 *  修改群自定义字段集合
 *
 *  @param group      群组 ID
 *  @param customInfo 自定义字段集合，key 是 NSString* 类型，value 是 NSData* 类型
 *  @param succ       成功回调
 *  @param fail       失败回调
 *
 *  @return 0 成功
 */
- (int)modifyGroupCustomInfo:(NSString*)group customInfo:(NSDictionary*)customInfo succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | 群组 ID
customInfo| 自定义字段集合，key 是 NSString\* 类型，value 是 NSData\* 类型
succ | 成功回调
fail | 失败回调

以下示例修改群『TGID1JYSZEAEQ』为禁止任何人加入。**示例：**

```
// 设置自定义数据
NSMutalbeDictionary *customInfo = [[NSMutableDictionary alloc] init];
NSString *key = @"custom key";
NSData *data = [NSData dataWithBytes:"custom value" length:13];
[customInfo setObject:data forKey:key];
[[TIMGroupManager sharedInstance] modifyGroupCustomInfo:@"TGID1JYSZEAEQ" customInfo:customInfo succ:^() {
	NSLog(@"modify group customInfo succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

### 修改用户群内身份

通过 `modifyGroupMemberInfoSetRole` 可以对群成员的身份进行修改。

**权限说明：**

- **群主、管理员：**可以进行对群成员的身份进行修改。
- **直播大群：**不支持修改用户群内身份。

**原型：**

```
@interface TIMGroupManager : NSObject
- (int)modifyGroupMemberInfoSetRole:(NSString*)group user:(NSString*)identifier role:(TIMGroupMemberRole)role succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | 群组 ID
identifier | 要修改的群成员的 ID
role | 修改后的身份类型，不能修改为群主类型
succ | 成功回调
fail | 失败回调

以下示例设置群『TGID1JYSZEAEQ』的成员『iOS_001』为管理员。 **示例：**

```
[[TIMGroupManager sharedInstance] modifyGroupMemberInfoSetRole:@"TGID1JYSZEAEQ" user:@"iOS_001" role:TIM_GROUP_MEMBER_ADMIN succ:^() {
	NSLog(@"modify group member role succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```



### 对群成员进行禁言

通过 `modifyGroupMemberInfoSetSilence` 可以对群成员进行禁言并设置禁言时长。

**权限说明：**

**群主、管理员：**可以进行对群成员进行禁言。

**原型：**

```
@interface TIMGroupManager : NSObject
- (int)modifyGroupMemberInfoSetSilence:(NSString*)group user:(NSString*)identifier stime:(uint32_t)stime succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | 群组 ID
identifier | 要禁言的群成员的 ID
stime | 禁言时间，单位秒
succ | 成功回调
fail | 失败回调

以下示例设置群『TGID1JYSZEAEQ』的成员『iOS_001』禁言120秒。 **示例：**

```
[[TIMGroupManager sharedInstance] modifyGroupMemberInfoSetSilence:@"TGID1JYSZEAEQ" user:@"iOS_001" stime:120 succ:^() {
	NSLog(@"modify group member silence succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

### 修改群名片

通过 `modifyGroupMemberInfoSetNameCard` 可以对群成员资料的群名片进行修改。

**原型： **

```
@interface TIMGroupManager : NSObject
- (int)modifyGroupMemberInfoSetNameCard:(NSString*)group user:(NSString*)identifier nameCard:(NSString*)nameCard succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | 群组 ID
identifier | 要修改的群成员的 ID
nameCard | 要设置的群名片
succ | 成功回调
fail | 失败回调

以下示例设置群『TGID1JYSZEAEQ』的成员『iOS_001』群名片为『iOS_001_namecard』。 **示例：**

```
[[TIMGroupManager sharedInstance] modifyGroupMemberInfoSetNameCard:@"TGID1JYSZEAEQ" user:@"iOS_001" nameCard:@"iOS_001_namecard" succ:^() {
	NSLog(@"modify group member namecard succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```



### 修改群成员维度自定义字段

通过 `modifyGroupMemberInfoSetCustomInfo` 可以对群成员维度自定义字段进行修改。

**原型：**

```
@interface TIMGroupManager : NSObject
- (int)modifyGroupMemberInfoSetCustomInfo:(NSString*)group user:(NSString*)identifier customInfo:(NSDictionary<NSString*,NSData*> *)customInfo succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | 群组 ID
identifier | 要设置自定义属性的群成员的 ID
customInfo | 自定义字段集合，key 是 NSString\* 类型，value 是 NSData\* 类型
succ | 成功回调
fail | 失败回调

以下示例设置群『TGID1JYSZEAEQ』的成员『iOS_001』的自定义属性。**示例：**

```
[[TIMGroupManager sharedInstance] modifyGroupMemberInfoSetCustomInfo:@"TGID1JYSZEAEQ" user:@"iOS_001" customInfo:customInfo succ:^() {
	NSLog(@"modify group member customInfo succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

### 修改接收群消息选项

通过 `modifyReceiveMessageOpt` 可以设置群消息的接收选项。默认情况下，公开群和私有群是接收并离线推送群消息，聊天室和直播大群是接收但不离线推送群消息。

**原型：**

```
@interface TIMGroupManager : NSObject
- (int)modifyReceiveMessageOpt:(NSString*)group opt:(TIMGroupReceiveMessageOpt)opt succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
group | 群组 ID
opt | 接收消息选项
succ | 成功回调
fail | 失败回调

以下示例设置群『TGID1JYSZEAEQ』的接收消息选项为接收在线消息，不接收离线推送。**示例：**

```
[[TIMGroupManager sharedInstance] modifyReciveMessageOpt:@"TGID1JYSZEAEQ" opt:TIM_GROUP_RECEIVE_NOT_NOTIFY_MESSAGE succ:^() {
	NSLog(@"modify receive group message option succ");
}fail:^(int code, NSString* err) {
	NSLog(@"failed code: %d %@", code, err);
}];
```

## 群组未决信息

### 拉取群未决相关信息

通过 `getPendencyFromServer` 接口可拉取群未决相关信息。此处的群未决消息泛指所有需要审批的群相关的操作（例如：加群待审批，拉人入群待审批等等）。即便审核通过或者拒绝后，该条信息也可通过此接口拉回，拉回的信息中有已决标志。

**权限说明：**

**审批人：**有权限拉取相关信息。

>?
>- 如果 UserA 申请加入群 GroupA，则群管理员可获取此未决相关信息，UserA 因为没有审批权限，不需要拉取未决信息。
>- 如果 AdminA 拉 UserA 进去 GroupA，则 UserA 可以拉取此未决相关信息，因为该未决信息待 UserA 审批。

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
- (int)getPendencyFromServer:(TIMGroupPendencyOption*)option succ:(TIMGetGroupPendencyListSucc)succ fail:(TIMFail)fail;
@end
```

**参数说明：**

参数|说明
---|---
option|未决参数配置
succ|成功回调，返回未决列表
fail|失败回调

 **option参数说明：**

| 参数 | 说明 |
| --- | --- |
| timestamp | 拉取的开始时戳。若从最新的未决条目开始拉取，则填0或不填。若分页，则回调中返回下一个分页的拉取起始时戳 |
| numPerPage | 一次拉取的最多条目数，用于分页 |

**回调原型：**

```
/**
 *  获取群组未决请求列表成功
 *
 *  @param meta       未决请求元信息
 *  @param pendencies 未决请求列表（TIMGroupPendencyItem）数组
 */
typedef void (^TIMGetGroupPendencyListSucc)(TIMGroupPendencyMeta * meta, NSArray * pendencies);
```

**回调参数说明：**

参数|说明
---|---
meta|拉取操作返回的相关信息，包含分页信息和拉取状态等
pendencies|拉取的未决条目数组

**属性说明： **

属性|说明
---|---
nextStartTime|拉取下一个分页的起始时戳，为0时表示没有后面的分页了
readTimeSeq|已读时戳，用来判定未决条目是否已读
unReadCnt|所有未读条目个数，不限制于本次分页中

**未决条目相关属性：**

```
/**
  *  未决申请
  */
@interface TIMGroupPendencyItem : TIMCodingModel
/**
 *  相关群组 ID
 */
@property(nonatomic,retain) NSString* groupId;
/**
  *  请求者 ID，请求加群:请求者，邀请加群:邀请人
  */
@property(nonatomic,retain) NSString* fromUser;
/**
  *  判决者 ID，请求加群：0，邀请加群：被邀请人
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
/**
  *  用户自己的id
  */
@property(nonatomic,strong) NSString* selfIdentifier;
@end
```

**属性说明： **

属性|说明
---|---
groupId|群 ID
fromUser|未决发起者 ID
toUser|未决审批者 ID
addTime|添加未决时间
getType|枚举未决条目类型： 请求加群、邀请加群
handleStatus|枚举未决条目状态：未决、他人已决、操作者已决（例如：UserA 申请加入 Group，AdminA 审批通过。则 AdminB 拉取的此未决条目的类型为，他人已决。）
handleResult|枚举审批结果：同意、拒绝
requestMsg/handleMsg|申请、审批时的留言信息

**示例：**

```
  TIMGroupPendencyOption option = [[TIMGroupPendencyOption alloc] init];
  option.timestamp = 0;
  option.numPerPage = 10;
  [[TIMGroupManager sharedInstance] getPendencyFromServer:option succ:^(TIMGroupPendencyMeta *meta, NSArray *pendencies) {
      NSLog(@"get pendencies succ");
  } fail:^(int code, NSString *msg) {
      NSLog(@"get pendencies failed: %d->%@", code, msg);
  }];
```

### 上报群未决已读

对于未决信息，IM SDK 可对其和之前的所有未决信息上报已读。上报已读后，仍然可以拉取到这些未决信息，但可通过对已读时戳的判断判定未决信息是否已读。

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
- (int)pendencyReport:(uint64_t)timestamp succ:(TIMSucc)succ fail:(TIMFail)fail;
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
[[TIMGroupManager sharedInstance] pendencyReport:timestamp succ:^{
        NSLog(@"pendency report succ");
    } fail:^(int code, NSString *msg) {
        NSLog(@"pendency report failed: %d->%@", code, msg);
    }];
```

### 处理群未决信息

对于群的未决信息，IM SDK 增加了处理接口。审批人可以选择对单条信息进行同意或者拒绝。已处理成功过的未决信息不能再次处理。

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
- (void)accept:(NSString*)msg succ:(TIMSucc)succ fail:(TIMFail)fail;
/**
 *  拒绝申请
 *
 *  @param msg      拒绝理由，选填
 *  @param succ     成功回调
 *  @param fail     失败回调，返回错误码和错误描述
 */
- (void)refuse:(NSString*)msg succ:(TIMSucc)succ fail:(TIMFail)fail;
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

## 群事件消息

当有用户被邀请加入群组，或者有用户被移出群组时，群内会产生有提示消息，调用方可选择是否予以展示，以及如何展示（例如：忽略或者根据需要展示给用户）。 提示消息使用一个特殊的 `Elem` 标识，通过新消息回调返回消息，参见 [新消息通知](https://cloud.tencent.com/doc/product/269/9148#.E6.96.B0.E6.B6.88.E6.81.AF.E9.80.9A.E7.9F.A5)。如下图中，展示一条修改群名的事件消息。

![](https://main.qcloudimg.com/raw/5a103b18bc1728baa742c7671443788e.jpg)

**消息原型：**

```
/**
 *  群 Tips 类型
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
 *  群 Tips
 */
@interface TIMGroupTipsElem : TIMElem
/**
  *  群组 ID
  */
@property(nonatomic,strong) NSString * group;
/**
  *  群 Tips 类型
  */
@property(nonatomic,assign) TIM_GROUP_TIPS_TYPE type;
/**
  *  操作人用户名
  */
@property(nonatomic,strong) NSString * opUser;
/**
  *  被操作人列表 NSString* 数组
  */
@property(nonatomic,strong) NSArray * userList;
/**
  *  在群名变更时表示变更后的群名，否则为 nil
  */
@property(nonatomic,strong) NSString * groupName;
/**
  *  群信息变更： TIM_GROUP_TIPS_TYPE_INFO_CHANGE 时有效，为 TIMGroupTipsElemGroupInfo 结构体列表
  */
@property(nonatomic,strong) NSArray * groupChangeList;
/**
  *  成员变更： TIM_GROUP_TIPS_TYPE_MEMBER_INFO_CHANGE 时有效，为 TIMGroupTipsElemMemberInfo 结构体列表
  */
@property(nonatomic,strong) NSArray * memberChangeList;
/**
  *  操作者用户资料
  */
@property(nonatomic,strong) TIMUserProfile * opUserInfo;
/**
  *  操作者群成员资料
  */
@property(nonatomic,strong) TIMGroupMemberInfo * opGroupMemberInfo;
/**
  *  变更成员资料
  */
@property(nonatomic,strong) NSDictionary * changedUserInfo;
/**
  *  变更成员群内资料
  */
@property(nonatomic,strong) NSDictionary * changedGroupMemberInfo;
/**
  *  当前群人数： TIM_GROUP_TIPS_TYPE_INVITE、TIM_GROUP_TIPS_TYPE_QUIT_GRP、
  *             TIM_GROUP_TIPS_TYPE_KICKED时有效
  */
@property(nonatomic,assign) uint32_t memberNum;
/**
  *  操作方平台信息
  *  取值： iOS Android Windows Mac Web RESTAPI Unknown
  */
@property(nonatomic,strong) NSString * platform;
@end
```

以下示例中注册新消息回调，打印用户进入群组和离开群组的事件通知，其他事件通知用法相同。 **示例：**

```
@interface TIMMessageListenerImpl : NSObject
- (void)onNewMessage:(NSArray*) msgs;
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
```

### 用户加入群组

**触发时机：**当有用户加入群组时（包括申请入群和被邀请入群），群组内会由系统发出通知，开发者可选择展示样式。可以更新群成员列表。收到的消息 type 为 `TIM_GROUP_TIPS_TYPE_INVITE`。

**`TIMGroupTipsElem` 参数说明：**

参数 | 说明
---|---
type | TIM_GROUP_TIPS_TYPE_INVITE
opUser | 申请入群：申请人 / 邀请入群：邀请人
groupName | 群名
userList | 入群的用户列表

### 用户退出群组

**触发时机：**当有用户主动退群时，群组内会由系统发出通知。可以选择更新群成员列表。 收到的消息 type 为 `TIM_GROUP_TIPS_TYPE_QUIT_GRP`。

**`TIMGroupTipsElem` 参数说明：**

参数 | 说明
---|---
type | TIM_GROUP_TIPS_TYPE_QUIT_GRP
opUser | 退出用户 identifier
groupName | 群名

### 用户被踢出群组

**触发时机：**当有用户被踢时，群组内会由系统发出通知。可以选择更新群成员列表。 收到的消息 type 为 `TIM_GROUP_TIPS_TYPE_KICKED`。

**`TIMGroupTipsElem` 参数说明：**

参数 | 说明
---|---
type | TIM_GROUP_TIPS_TYPE_KICKED
opUser | 被踢用户 identifier
groupName | 群名

### 被设置/取消管理员

**触发时机：**当有用户被设置为管理员或者被取消管理员身份时，群组内会由系统发出通知。如果界面有显示是否管理员，此时可更新管理员标识。 收到的消息 type 为 `TIM_GROUP_TIPS_TYPE_SET_ADMIN` 和 `TIM_GROUP_TIPS_TYPE_CANCEL_ADMIN`。

**`TIMGroupTipsElem` 参数说明： **

参数 | 说明
---|---
type | 设置：TIM_GROUP_TIPS_TYPE_SET_ADMIN
取消 | TIM_GROUP_TIPS_TYPE_CANCEL_ADMIN
opUser | 操作用户 identifier
groupName | 群名
userList | 被设置/取消管理员身份的用户列表

### 群资料变更

**触发时机：**当群资料变更（如群名、群简介等），会有系统消息发出，此时可以更新相关展示字段，选择性把消息展示给用户。

**`TIMGroupTipsElem` 参数说明：**

参数 | 说明
---|---
type | TIM_GROUP_TIPS_TYPE_INFO_CHANGE
opUser | 操作用户 identifier
groupName | 群名
groupChangeInfo | 群变更的具体资料信息，为 TIMGroupTipsElemGroupInfo 结构体列表

**`TIMGroupTipsElemGroupInfo` 原型：**

```
/**
  *  群 tips，群变更信息
  */
@interface TIMGroupTipsElemGroupInfo : NSObject
/**
  *  变更类型
  */
@property(nonatomic, assign) TIM_GROUP_INFO_CHANGE_TYPE type;

/**
  *  根据变更类型表示不同含义
  */
@property(nonatomic,strong) NSString * value;
@end
```

**参数说明：**

参数 | 说明
---|---
type | 变更类型
value | 变更后的值，根据变更类型表示不同含义

### 群成员资料变更

**触发时机：**当群成员的群相关资料变更时，包括群内用户被禁言、群内成员角色变更，会有系统消息发出，可更新相关字段展示，或者选择性把消息展示给用户。

>!
>- 这里的资料仅跟群相关资料，例如禁言时间、成员角色变更等，不包括用户昵称等本身资料，对于群内人数可能过多，不建议实时更新，建议的做法是直接显示消息体内的资料，参考：[消息发送者以及相关资料](https://cloud.tencent.com/doc/product/269/9150#.E6.B6.88.E6.81.AF.E5.8F.91.E9.80.81.E8.80.85.E4.BB.A5.E5.8F.8A.E7.9B.B8.E5.85.B3.E8.B5.84.E6.96.99)
>- 如果本地有保存用户资料，可根据消息体内资料判断是否有变更，在收到此用户一条消息后更新资料。

**`TIMGroupTipsElem` 参数说明：**

参数 | 说明
---|---
type | TIM_GROUP_TIPS_TYPE_MEMBER_INFO_CHANGE
opUser | 操作用户 identifier
groupName | 群名
memberInfoList | 变更的群成员的具体资料信息，为 `TIMGroupTipsElemMemberInfo` 结构体列表

**`TIMGroupTipsElemMemberInfo` 原型：**

```
/**
 *  群 tips，成员变更信息
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

参数 | 说明
---|---
identifier | 变更的用户 identifier
shutupTime | 被禁言的时间

### 群事件消息监听器

聊天室和直播大群的群事件消息需要通过注册监听器获得（设置监听位置在 TIMManager > setUserConfig > TIMUserConfig > groupEventListener），消息 `Elem` 中包含群的成员数。

```
/**
 *  群事件通知回调
 */
@protocol TIMGroupEventListener <NSObject>
@optional
/**
 *  群 tips 回调
 *
 *  @param elem  群 tips 消息
 */
- (void)onGroupTipsEvent:(TIMGroupTipsElem*)elem {
    // 群组 ID
    NSString *groupID = elem.group;
    // 操作者
    NSString *opUser = elem.opUser;
    // 被操作者
    NSArray *userList = elem.userList;
    switch (elem.type) {
        case TIM_GROUP_TIPS_TYPE_INVITE:
            // userList 加入群组，如果是私有群（Private），可以展示为 "opUser 邀请 userList 入群"。
            // 如果是其他群组类型，可以展示为 "userList 加入群组"
            break;
        case TIM_GROUP_TIPS_TYPE_QUIT_GRP:
            // opUser 退出群组
            break;
        case TIM_GROUP_TIPS_TYPE_KICKED:
            // opUser 把 userList 踢出群组
            break;
        case TIM_GROUP_TIPS_TYPE_SET_ADMIN:
            // opUser 设置 userList 为管理员
            break;
        case TIM_GROUP_TIPS_TYPE_CANCEL_ADMIN:
            // opUser 取消 userList 管理员身份
            break;
        case TIM_GROUP_TIPS_TYPE_INFO_CHANGE:
            // groupID 群信息发生了变化
            break;
        case TIM_GROUP_TIPS_TYPE_MEMBER_INFO_CHANGE:
            // groupID 群成员群信息发生了变化
            break;
        default:
            break;
    }
}
@end
```

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
    /**
    *  用户自定义通知(默认全员接收)
    */
    TIM_GROUP_SYSTEM_CUSTOM_INFO                         = 0xff,
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
  * 群组 ID
  */
@property(nonatomic,strong) NSString * group;
/**
  * 操作人
  */
@property(nonatomic,strong) NSString * user;
/**
  * 操作理由
  */
@property(nonatomic,strong) NSString * msg;
/**
  *  消息标识，客户端无需关心
  */
@property(nonatomic,assign) uint64_t msgKey;
/**
  *  消息标识，客户端无需关心
  */
@property(nonatomic,strong) NSData * authKey;
/**
  *  用户自定义透传消息体（type ＝ TIM_GROUP_SYSTEM_CUSTOM_INFO 时有效）
  */
@property(nonatomic,strong) NSData * userData;
/**
  *  操作人资料
  */
@property(nonatomic,strong) TIMUserProfile * opUserInfo;
/**
  *  操作人群成员资料
  */
@property(nonatomic,strong) TIMGroupMemberInfo * opGroupMemberInfo;
/**
  *  操作方平台信息
  *  取值： iOS、Android、Windows、Mac、Web、RESTAPI、Unknown
  */
@property(nonatomic,strong) NSString * platform;
@end
```

**参数说明：**

参数 | 说明
---|---
type | 消息类型
group | 群组 ID
user | 操作人
msg | 操作理由
msgKey & authKey | 消息的标识，客户端无需关心，调用 accept 和 refuse 时由 IM SDK 读取

以下示例中处理收到群系统消息，如果是入群申请则默认同意，如果是群解散通知则打印信息。其他类型消息解析方式相同。 **示例： **

```
@interface TIMMessageListenerImpl : NSObject
- (void)onNewMessage:(NSArray*) msgs;
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
```

### 申请加群消息

**触发时机：**当有用户申请加群时，群管理员会收到申请加群消息，可展示给用户，由用户决定是否同意对方加群。 消息类型为 `TIM_GROUP_SYSTEM_ADD_GROUP_REQUEST_TYPE`。

**参数说明：**

参数 | 说明
---|---
type | TIM_GROUP_SYSTEM_ADD_GROUP_REQUEST_TYPE
group | 群组 ID，表示是哪个群的申请
user | 申请人
msg | 申请理由（可选）

**方法说明：**

- 同意申请人入群，可调用 accept 方法
- 不同意申请人入群，可调用 refuse 方法。

### 申请加群同意/拒绝消息

**触发时机：**当管理员同意加群请求时，申请人会收到同意入群的消息，当管理员拒绝时，收到拒绝入群的消息。

**参数说明：**

参数 | 说明
---|---
type | 同意：TIM_GROUP_SYSTEM_ADD_GROUP_ACCEPT_TYPE<br>拒绝：TIM_GROUP_SYSTEM_ADD_GROUP_REFUSE_TYPE
group | 群组 ID，表示是哪个群通过/拒绝了
user | 处理请求的管理员 identifier
msg | 同意或者拒绝理由（可选）

### 邀请入群消息

**触发时机：**当有用户被邀请群时，该用户会收到邀请入群消息，可展示给用户，由用户决定是否同意入群，如果同意，调用 accept 方法，拒绝调用 refuse 方法。 消息类型为 `TIM_GROUP_SYSTEM_INVITE_TO_GROUP_REQUEST_TYPE`

**参数说明：**

参数 | 说明
---|---
type | TIM_GROUP_SYSTEM_INVITE_TO_GROUP_REQUEST_TYPE
group | 群组 ID，表示是哪个群的邀请
user | 邀请人

**方法说明：**

- 同意申请人入群，可调用 accept 方法。
- 不同意申请人入群，可调用 refuse 方法。

### 邀请入群同意/拒绝消息

**触发时机：**当被邀请者同意入群请求时，邀请者会收到同意入群的消息，当被邀请者拒绝时，邀请者会收到拒绝入群的消息。

**参数说明：**

参数 | 说明
---|---
type | 同意：TIM_GROUP_SYSTEM_INVITE_TO_GROUP_ACCEPT_TYPE<br>拒绝：TIM_GROUP_SYSTEM_INVITE_TO_GROUP_REFUSE_TYPE
group | 群组 ID，表示是对哪个群通过/拒绝了
user | 处理请求的用户 identifier
msg | 同意或者拒绝理由（可选）

### 被管理员踢出群组

**触发时机：**当用户被管理员踢出群组时，申请人会收到被踢出群的消息。

**参数说明：**

参数 | 说明
---|---
type | TIM_GROUP_SYSTEM_KICK_OFF_FROM_GROUP_TYPE
group | 群组 ID，表示在哪个群里被踢了
user | 操作管理员 identifier

### 群被解散

**触发时机：**当群被解散时，全员会收到解散群消息。

**参数说明：**

参数 | 说明
---|---
type | TIM_GROUP_SYSTEM_DELETE_GROUP_TYPE
group | 群组 ID，表示哪个群被解散了
user | 操作管理员 identifier

### 创建群消息

**触发时机：**当群创建时，创建者会收到创建群消息。当调用创建群方法成功回调后，即表示创建成功，此消息主要为多终端同步，如果有在其他终端登录，作为更新群列表的时机，本终端可以选择忽略。

**参数说明：**

参数 | 说明
---|---
type | TIM_GROUP_SYSTEM_CREATE_GROUP_TYPE
group | 群组 ID，表示创建的群 ID
user | 创建者，这里也就是用户自己

### 邀请加群

**触发时机：**当用户被邀请加入群组时，该用户会收到邀请消息，**创建群组时初始成员无需邀请即可入群。 **

**参数说明：**

参数 | 说明
---|---
type | TIM_GROUP_SYSTEM_INVITED_TO_GROUP_TYPE
group | 群组 ID，邀请进入哪个群
user | 操作人，表示哪个用户的邀请

**方法说明：**

- 同意申请人入群，可调用 accept 方法。
- 不同意申请人入群，可调用 refuse 方法。

### 主动退群

**触发时机：**当用户主动退出群组时，该用户会收到退群消息，只有退群的用户自己可以收到。当用户调用 `QuitGroup` 时成功回调返回，表示已退出成功，此消息主要为了多终端同步，其他终端可以作为更新群列表的时机，本终端可以选择忽略。

**参数说明：**

参数 | 说明
---|---
type | TIM_GROUP_SYSTEM_QUIT_GROUP_TYPE
group | 群组 ID，表示退出的哪个群
user | 操作人，这里即为用户自己

### 设置/取消管理员

**触发时机：**当用户被设置为管理员时，可收到被设置管理员的消息通知，当用户被取消管理员时，可收到取消通知，可提示用户。

**参数说明：**

参数 | 说明
---|---
type | 取消管理员身份：TIM_GROUP_SYSTEM_GRANT_ADMIN_TYPE<br>授予管理员身份：TIM_GROUP_SYSTEM_CANCEL_ADMIN_TYPE
group | 群组 ID，表示哪个群的事件
user | 操作人

### 群被回收

**触发时机：**当群组被系统回收时，全员可收到群组被回收消息。

**参数说明：**

参数 | 说明
---|---
type | TIM_GROUP_SYSTEM_REVOKE_GROUP_TYPE
group | 群组 ID，表示哪个群被回收了


