
## 1. 群组综述 

IM云通讯有多种群组类型，其特点以及限制因素可参考[群组系统](/doc/product/269/群组系统)。群组使用唯一Id标识，通过群组Id可以进行不同操作。

## 2. 群组消息 

群组消息与C2C消息相同，仅在获取Conversation时的会话类型不同，可参照 [消息发送](/doc/product/269/消息收发（iOS%20SDK）#1.-.E6.B6.88.E6.81.AF.E5.8F.91.E9.80.81) 部分。

## 3. 群组管理

群组相关操作都定义在`tim_group_c.h` 实现，需要用户登录成功后操作。

### 3.1 创建内置类型群组

TIMCreateGroup创建群，创建时可指定群组名称以及要加入的用户列表，创建成功后返回群组Id，可通过群组Id获取Conversation收发消息等。云通信中内置了私有群、公开群、聊天室互动直播聊天室和在线成员广播大群五种群组类型，详情请见[群组形态介绍](/doc/product/269/群组系统#2-.E7.BE.A4.E7.BB.84.E5.BD.A2.E6.80.81.E4.BB.8B.E7.BB.8D)

另外使用`"AVChatRoom"`类型创建直播大群，此类型群可以加入人数不做限制，但是有一些能力上的限制，如不能拉人进去，不能查询总人数等，可参阅 [互动直播集成多人聊天方案](/doc/product/269/互动直播集成多人聊天方案)。

**原型：**

```
/**
Description:	创建群组
@param	[in]	group_type		群组
@param	[in]	members			成员ID数组
@param	[in]	members_count	成员个数
@param	[in]	group_name		群组名
@param	[in]	callback		回调
@return			void
@exception      none
*/
TIM_DECL void TIMCreateGroup(const char* group_type, const char** members, uint32_t members_count, const char* group_name, TIMCreateGroupCB* callback);
```

**参数说明：**

参数 | 说明
---|---
group_type | 群组类型
| "Private" 私有群
| "Public" 公开群
| "ChatRoom" 聊天室
| "AVChatRoom" 直播大群
members | 用户ID列表，指定加入群组的成员，创建者默认加入，无需指定（群内最多10000人） 
members_count | 成员个数
group_name |  指定群组名称（最长30字节） 
cb | 回调，返回群组Id 

**示例：  **  

```
#define DEMO_MEM_COUNT 10
void DemoCreaeGroup()
{
	//创建群组
	const char** members = new const char*[DEMO_MEM_COUNT];
	members[0] = "c9_1";
	members[1] = "c9_2";
	members[2] = "c9_3";
	TIMCreateGroupCB callbacck;
	callbacck.OnSuccess = CBCreateGroupOnSuccessImp;
	callbacck.OnError = CBCreateGroupOnErroImp;
	TIMCreateGroup(TIM_PRIVATE_GROUP,  members, 3, "c9_group_0", &callbacck);
	//wait for callback
	SLEEP(1);

	deletemembers;
}

void CBCreateGroupOnSuccessImp(const char* group_id, void* data)
{
	printf("Create Group Success! group_id = <%s>", group_id);
}

void CBCreateGroupOnErroImp(int code, const char* desc, void* data)
{
	printf("CBCreateGroupOnErroImp Error! code = <%d> desc = <%s>", code, desc);
}
```

示例创建一个私有群组，并且把用户"c9_1"等三人拉入群组，创建者默认加入群组，无需显式指定。 
公开群和聊天室调用方式和参数相同，仅参数不同。 

### 3.2 创建指定属性群组

在创建群组时，除了设置默认的成员以及群名外，还可以设置如群公告、群简介等字段，通过以下接口可以设置：

**原型：**

```
TIM_DECL void SetNewGroupInfoGroupType(TIMNewGroupInfoHandle handle, const char* group_type);
TIM_DECL void SetNewGroupInfoGroupName(TIMNewGroupInfoHandle handle, const char* group_name, const uint32_t name_len);
TIM_DECL void SetNewGroupInfoGroupMembers(TIMNewGroupInfoHandle handle, TIMNewGroupMemberInfoHandle* members, const uint32_t num);
TIM_DECL void SetNewGroupInfoGroupNotification(TIMNewGroupInfoHandle handle, const char* notification, const uint32_t nofi_len);
TIM_DECL void SetNewGroupInfoGroupIntroduction(TIMNewGroupInfoHandle handle, const char* introduction, const uint32_t intro_len);
TIM_DECL void SetNewGroupInfoFaceUrl(TIMNewGroupInfoHandle handle, const char* face_url, const uint32_t face_url_len);
TIM_DECL void SetNewGroupInfoId(TIMNewGroupInfoHandle handle, const char* id);
TIM_DECL void SetNewGroupInfoAddOption(TIMNewGroupInfoHandle handle, const TIMGroupAddOpt opt);
TIM_DECL void SetNewGroupInfoMaxMemberNum(TIMNewGroupInfoHandle handle, const uint32_t max_member_num);
TIM_DECL void SetNewGroupInfoGroupCustomInfo(TIMNewGroupInfoHandle handle, TIMGroupCustomInfoHandle custom_info_handle);

/**
Description:	创建指定属性群组
@param	[in]	handle		创建群指定属性
@param	[in]	callback	回调
@return			void
@exception      none
*/
TIM_DECL void TIMCreateGroupV2(TIMNewGroupInfoHandle handle, TIMCreateGroupCB* callback);
```

**参数说明：**

参数|说明
---|---
handle|可设置的参数，详见 TIMNewGroupInfoHandle 定义。
callback|回调

**属性说明：**

属性|说明
---|---
group_type | 群组类型 同上 Private,Public,ChatRoom,AVChatRoom
group_name | 群名
notification | 群公告
introduction | 群简介
id | 指定群ID
add_opt | 入群选项
max_member_num | 最大成员数

### 3.3 自定义群组Id创建群组

默认创建群组时，IM通讯云服务器会生成一个唯一的Id，以便后续操作，另外，如果用户需要自定义群组Id，在创建时可指定Id，通过 3.2 创建指定属性群组可以实现自定义群组Id的功能。

### 3.4 邀请用户入群

TTIMInviteGroupMember接口 可以拉（邀请）用户进入群组，对私有群，对方直接进入群组，对于共有群，需要对方同意才可进入。

**权限说明：**
 
只有私有群可以拉用户入群； 
公开群、聊天室邀请用户入群，需要用户同意；
直播大群不能邀请用户入群；

**原型：**

```
/**
Description:	邀请用户入群
@param	[in]	groupid			群ID
@param	[in]	members			成员ID数组
@param	[in]	members_count	成员个数
@param	[in]	callback		回调
@return			void
@exception      none
*/
TIM_DECL void TIMInviteGroupMember(const char* groupid, const char** members, uint32_t members_count, TIMInviteGroupMemberCB* callback);
```

**参数说明：**
 
参数|说明
---|---
groupid | 群组Id 
members | 成员ID数组
members_count	| 成员个数
cb | 回调，TIMGroupMemberResult 数组，返回成功加入群组的用户列表以及成功状态 
·
**示例：**   

```
void DemoInviteGroupMember()
{
	const char** members = new const char*[DEMO_MEM_COUNT];
	members[0] = "c9_1";
	members[1] = "c9_2";
	members[2] = "c9_3";

	TIMInviteGroupMemberCB callback;
	callback.OnSuccess = CBInviteGroupMemberOnSuccessImp;
	callback.OnError = CBInviteGroupMemberOnErrorImp;

	TIMInviteGroupMember("test_groupid", members, 3, &callback);
	//wait for callback
	SLEEP(1);

	delete members;
}

void CBInviteGroupMemberOnSuccessImp(TIMGroupMemberResultHandle* handle_array, uint32_t array_size, void* data)
{
	char buf[BUF_LEN] = {0};
	for (uint32_ti = 0; i <array_size; i++)
	{
		uint32_t len = BUF_LEN;
		GetGroupMemberResultID(handle_array[i], buf, &len);
		printf("Member OpenId = <%s>", buf);
printf("Member Result = <%u>", GetGroupMemberResult(handle_array[i]));
	}
}

void CBInviteGroupMemberOnErrorImp(int code, const char* desc, void* data)
{
	printf("CBInviteGroupMemberOnErrorImp Error! code = <%d> desc = <%s>", code, desc);
}
```
示例中邀请"c9_1"等三人加入群组Id"test_groupid" ，成功后返回操作列表以及成功状态。 

### 3.5 申请加入群组 

TIMApplyJoinGroup接口可以主动申请进入群组，此操作只对公开群和聊天室有效。 

**权限说明：**
 
私有群不能由用户主动申请入群； 
公开群和聊天室可以主动申请进入； 
如果群组设置为需要审核，申请后管理员和群主会受到申请入群系统消息，需要等待管理员或者群主审核，如果群主设置为任何人可加入，则直接入群成功；
直播大群可以任意加入群组。

**原型：**

```
/**
Description:	申请加入群组
@param	[in]	groupid		群组ID
@param	[in]	hello_msg	申请消息
@param	[in]	callback	回调
@return			void
@exception      none
*/
TIM_DECL void TIMApplyJoinGroup(const char* groupid, const char* hello_msg, TIMCommCB* callback);
```
**参数说明：**

参数|说明
---|---
groupid | 群组ID
hello_msg  | 申请理由 
callback | 回调 

### 3.6 退出群组 

群组成员可以主动退出群组。 

**权限说明：**
 
对于私有群，全员可退出群组； 
对于公开群、聊天室和直播大群，群主不能退出； 

**原型：**

```
/**
Description:	退出群组
@param	[in]	groupid		群组ID	
@param	[in]	callback	回调
@return			void
@exception      none
*/
TIM_DECL void TIMQuitGroup(const char* groupid, TIMCommCB* callback);
```

**参数说明：**

参数|说明
---|---
groupid | 群组Id 
callback | 回调 

**示例：**

```
void DemoQuiteGroup()
{
	TIMCommCB callback;
	callback.OnSuccess = CBCommOnSuccessImp;
	callback.OnError = CBCommOnErrorImp;

	TIMQuitGroup("TGID1JYSZEAEQ", &callback);
	//wait for callback
	SLEEP(1);
}
```
示例中主动退出群组 "TGID1JYSZEAEQ"。  

### 3.7 删除群组成员 

群组成员也可以删除其他成员，函数参数信息与加入群组相同。 

**权限说明：**
 
对于私有群：只有创建者可删除群组成员 
对于公开群和聊天室：只有管理员和群主可以踢人 
对于直播大群：不能踢人

**原型：**

```
/**
Description:	删除群组成员 
@param	[in]	groupid		群组ID
@param	[in]	members		群成员ID
@param	[in]	members_count	群成员个数
@param	[in]	reason			踢人原因描述
@param	[in]	reason_len		原因长度
@param	[in]	callback		回调
@return			void
@exception      none
*/
TIM_DECL void TIMDeleteGroupMember(const char* groupid, const char** members, uint32_t members_count, const char* reason, uint32_t reason_len, TIMDeleteGroupMemberCB* callback);
```

**参数说明：**

参数|说明
---|---
groupid | 群组Id 
members | 群成员ID
members_count |	群成员个数
reason | 踢人原因描述
reason_len | 原因长度
callback | 回调

**示例：** 

```
void DemoDeleteGroupMember()
{
	const char** members = new const char*[DEMO_MEM_COUNT];
	members[0] = "WIN_001";
	members[1] = "WIN_002";
	members[2] = "WIN_003";

	TIMDeleteGroupMemberCB callback;
	callback.OnSuccess = CBDeleteGroupMemberOnSuccessImp;
	callback.OnError = CBDeleteGroupMemberOnErrorImp;

	TIMDeleteGroupMember("TGID1JYSZEAEQ", members, 3, &callback);
	//wait for callback
	SLEEP(1);
	deletemembers;
}

#define BUF_LEN  100
void CBDeleteGroupMemberOnSuccessImp(TIMGroupMemberResultHandle* handle_array, uint32_t array_size, void* data)
{
	char buf[BUF_LEN] = {0};
	for (uint32_t i = 0; i < array_size; i++)
	{
		uint32_t len = BUF_LEN;
		GetGroupMemberResultID(handle_array[i], buf, &len);
		printf("Member OpenId = <%s>", buf);
		printf("Member Result = <%u>", GetGroupMemberResult(handle_array[i]));
	}
}

void CBDeleteGroupMemberOnErrorImp(int code, const char* desc, void* data)
{
	printf("CBDeleteGroupMemberOnErrorImp Error! code = <%d> desc = <%s>", code, desc);
}
```
示例中把好友 "WIN_001"等3人从群组 @"TGID1JYSZEAEQ" 中删除，执行成功后返回操作列表以及操作状

### 3.8 获取群成员列表 

TIMGetGroupMembers 方法可获取群内成员列表，默认拉取内置字段，但不拉取自定义字段，想要获取自定义字段，可通过【4.1 设置拉取字段】进行设置（1.9版本以上引入）。

**权限说明：**
 
任何群组类型都可以获取成员列表； 
直播大群只能拉取部分成员列表：包括群主、管理员和部分成员；

**原型：**
```
 /**
 Description:	获取群成员列表 
 @param	[in]	groupid	群组ID
 @param	[in]	cb		回调
 @return			void
 @exception      none
 */
 TIM_DECL void TIMGetGroupMembers(const char* groupid, TIMGetGroupMemberInfoCB *cb);
```

**参数说明：**

参数|说明
---|---
groupid	| 群组ID
cb | 回调

**示例：**

```
void DemoGetGroupMemberList()
{
	TIMGetGroupMemberInfoCB callback;
	callback.OnSuccess = CBGetGroupMemberInfoOnSuccessImp;
	callback.OnError = CBGetGroupMemberInfoOnErrorImp;
	TIMGetGroupMembers("TGID1JYSZEAEQ", &callback);
	//wait for callback
	SLEEP(1);
 }

void CBGetGroupMemberInfoOnSuccessImp(TIMGroupMemberInfoHandle* handle_array, uint32_t array_size, void* data)
{
	char buf[BUF_LEN] = {0};
	for (uint32_t i = 0; i<array_size; i++)
	{
		uint32_t len = BUF_LEN;
		GetGroupMemberID(handle_array[i], buf, &len);
		printf("ID = <%s>\n", buf);
	}
}

void CBGetGroupMemberInfoOnErrorImp(int code, const char* desc, void* data)
{
	printf("CBGetGroupMemberInfoOnErrorImp Error! code = <%d> desc = <%s>", code, desc);
}
```
示例中获取群 @"TGID1JYSZEAEQ" 的成员列表，handle_array存储成员的相关信息。 

### 3.9 获取加入的群组列表 

通过 GetGroupList 可以获取当前用户加入的所有群组： 

**权限说明：**
 
此接口可以获取自己所加入的群列表，返回的TIMGroupInfo只包含group\groupName\groupType 信息，想要获取更加详细的字段，可通过【4.1 设置拉取字段】进行设置（1.9版本以上引入）；
此接口只能获得加入的部分直播大的列表；
 
**原型：**

```
/**
Description:	获取加入的群组列表
@param	[in]	callback 回调
@return			void
@exception      none
*/
TIM_DECL void TIMGetGroupList(TIMGetGroupListCB *callback);

typedef void (*CBGetGroupListOnSuccess) (TIMGroupBaseInfoHandle* handle_array, uint32_t array_size, void* data);
typedef void (*CBGetGroupListOnError) (int code, const char* desc, void* data);

typedef struct _TIMCallBack_GetGroupList
{
	CBGetGroupListOnSuccess OnSuccess;
	CBGetGroupListOnError OnError;
	void* data;
}TIMGetGroupListCB;

int GetGroupBaseInfoID(TIMGroupBaseInfoHandle handle, char* id, uint32_t* len);
int GetGroupBaseInfoName(TIMGroupBaseInfoHandle handle, char* name, uint32_t* len);
int GetGroupBaseInfoType(TIMGroupBaseInfoHandle handle, char* type, uint32_t* len);
```

**参数说明：**

参数|说明
---|---
cb | 回调，返回群组Id列表，TIMGroupBaseInfoHandle数组 

**属性说明 :**

属性|说明
---|---
id | 群组ID
name | 群组名
type | 群组类型

**示例：**

```
void DemoGetGroupList()
{
	TIMGetGroupListCB callback;
	callback.OnSuccess = CBGetGroupListOnSuccessImp;
	callback.OnError = CBGetGroupListOnErrorImp;
	TIMGetGroupList(&callback);
	//wait for callback
	SLEEP(1);
}
void CBGetGroupListOnSuccessImp(TIMGroupBaseInfoHandle* handle_array, uint32_t array_size, void* data)
{
	char buf[BUF_LEN] = {0};
	for (uint32_t i = 0; i <array_size; i++)
	{
		TIMGroupBaseInfoHandle handle = handle_array[i];
		uint32_t len = BUF_LEN;GetGroupBaseInfoName(handle, buf, &len);
		printf("GroupName = <%s>\n", buf);
		len = BUF_LEN; GetGroupBaseInfoID(handle, buf, &len);
		printf("GroupId = <%s>\n", buf);
		len = BUF_LEN; GetGroupBaseInfoType(handle, buf, &len);
		printf("GroupType = <%s>\n", buf);
	}
}

void CBGetGroupListOnErrorImp(int code, const char* desc, void* data)
{
	printf("CBGetGroupListOnErrorImp Error! code = <%d> desc = <%s>", code, desc);
}

```

示例中获取群组列表，并打印群组Id，群类型（Private/Public/ChatRoom/AVChatRoom）以及群名。 

### 3.10 解散群组

通过 DeleteGroup 可以解散群组。 

**权限说明：**
 
对于私有群，任何人都无法解散群组 
对于公开群、聊天室和直播大群，群主可以解散群组： 

**原型：**

```
/**
Description:	解散群组
@param	[in]	groupid		群组ID
@param	[in]	callback	回调
@return			void
@exception      none
*/
TIM_DECL void TIMDeleteGroup(const char* groupid, TIMCommCB * callback);
```
**参数说明：**

参数 | 说明
---|---
groupid | 群组Id 
callback | 回调，返回群组Id列表，NSString数组 

### 3.11 转让群组 

通过 ModifyGroupOwner可以转让群组。 

**权限说明：**
 
只有群主才有权限进行群转让操作；
直播大群不能进行群转让操作；

**原型：**

```
/**
Description:	转让群组
@param	[in]	groupid		群组ID
@param	[in]	new_owner_id	新群主ID
@param	[in]	callback		回调
@return			void
@exception      none
*/
TIM_DECL void TIMModifyGroupOwner(const char* groupid, const char* new_owner_id, TIMCommCB* callback);
```

**参数说明：**

参数|说明
---|---
groupid		|  群组ID
new_owner_id	| 新群主ID
callback	|	回调

### 3.12 删除群组成员（带原因）

同**3.7 删除群组成员**

### 3.13 其他接口

-获取指定类型成员（可按照管理员、群主、普通成员拉取）

**原型：**

```
/**
Description:	获取指定类型成员
@param	[in]	groupid		群ID
@param	[in]	flag		获取标志使能位
@param	[in]	role_filter	filter标志 （拉取全部 只群组 只管理员 只普通成员）
@param	[in]	custom		群成员自定义信息标志
@param	[in]	next_seq	拉取seq 用户翻页
@param	[in]	cb
@return			void
@exception      none
*/
TIM_DECL void TIMGetGroupMembersByFilter(const char* groupid, TIMGetGroupMemInfoFlag flag, TIMGroupMemRoleFilter role_filter, TIMGroupCustomInfoHandle custom, uint64_t next_seq, TIMGetGroupMemberInfoCBV2 *cb);
```

## 4. 获取群资料

### 4.1 设置拉取字段

拉取用户资料默认返回部分内置字段，如果需要自定义字段，或者不拉取某些字段，可以通过接口进行设置（**此接口1.9版本以上提供**），此设置对所有资料相关接口有效，全局有效：

```

struct TIMUpdateInfoOpt{
	uint64_t flag;
	const char** tag_name;
	uint32_t num;
};

struct TIMGroupSettings{
	TIMUpdateInfoOpt memberInfoOpt;
	TIMUpdateInfoOpt groupInfoOpt;
};
/**
Description:	设置拉取字段
@param	[in]	config	拉取设置
@return			void
@exception      none
*/
void TIMInitGroupSetting(TIMGroupSettings* config);
```

**属性说明**

属性|说明
---|---
groupInfoOpt| 拉取群信息设置
| flag 设置需要获取的群组信息标志（TIMGetGroupBaseInfoFlag）
| tag 需要获取群组资料的自定义信息tag 数组
memberinfoopt| 拉取群成员信息设置
|flag 需要获取的群成员标志（TIMGetGroupMemInfoFlag）
|tag  需要获取群成员资料的自定义信息tag 数组

### 4.2 群成员获取群组资料

TIMGetGroupDetailInfo方法可以获取群组资料。默认拉取基本资料，如果想拉取自定义资料，可通过【4.1 设置拉取字段】进行设置（1.9版本以上引入）。

**权限说明：**
 
注意：获取群组资料接口只能由群成员调用，非群成员无法通过此方法获取资料，需要调用；
群资料信息由TIMGroupDetailInfoHandleo定义： 

通过 TIMGetGroupDetailInfo 可获取群组资料： 

**原型：**

```
// 群组Id
TIM_DECL int GetGroupDetailInfoID(TIMGroupDetailInfoHandle handle, char* id, uint32_t* len);
// 群名
TIM_DECL int GetGroupDetailInfoName(TIMGroupDetailInfoHandle handle, char* name, uint32_t* len);
// 创建人
TIM_DECL int GetGroupDetailInfoOwner(TIMGroupDetailInfoHandle handle, char* owner, uint32_t* len);
// 群公告
TIM_DECL int GetGroupDetailInfoNotification(TIMGroupDetailInfoHandle handle, char* buf, uint32_t* len);
// 群简介
TIM_DECL int GetGroupDetailInfoIntroduction(TIMGroupDetailInfoHandle handle, char* buf, uint32_t* len);
TIM_DECL int GetGroupDetailInfoFaceURL(TIMGroupDetailInfoHandle handle, char* url, uint32_t* len);
// 群组类型
TIM_DECL int GetGroupDetailInfoType(TIMGroupDetailInfoHandle handle, char* type, uint32_t* len);
TIM_DECL uint32_t GetGroupDetailInfoCreateTime(TIMGroupDetailInfoHandle handle);
// 最近一次修改资料时间
TIM_DECL uint32_t GetGroupDetailInfoLastInfoTime(TIMGroupDetailInfoHandle handle);
// 最近一次发消息时间
TIM_DECL uint32_t GetGroupDetailInfoLastMsgTime(TIMGroupDetailInfoHandle handle);
// 群成员数量
TIM_DECL uint32_t GetGroupDetailInfoMemberNum(TIMGroupDetailInfoHandle handle);
TIM_DECL uint32_t GetGroupDetailInfoMaxMemberNum(TIMGroupDetailInfoHandle handle);
TIM_DECL uint32_t GetGroupDetailInfoOnlineNum(TIMGroupDetailInfoHandle handle);
TIM_DECL TIMComStatus GetGroupDetailInfoVisiableFlag(TIMGroupDetailInfoHandle handle);
TIM_DECL TIMComStatus GetGroupDetailInfoSearchableFlag(TIMGroupDetailInfoHandle handle);
TIM_DECL TIMGroupCustomInfoHandle GetGroupDetailInfoCustomInfo(TIMGroupDetailInfoHandle handle);
TIM_DECL TIMMessageHandle CloneMessageHandleFromGroupDetailInfo(TIMGroupDetailInfoHandle handle);
 /**
 Description:	获取群信息
 @param	[in]	groupids		群组ID数组
 @param	[in]	groupid_count	群组ID个数
 @param	[in]	cb				回调
 @return			void
 @exception      none
 */
 TIM_DECL void TIMGetGroupDetailInfo(const char** groupids, uint32_t groupid_count, TIMGetGroupDetailInfoCB * cb);
```

**参数说明：**

参数|说明
---|---
groupids |群组ID数组，需要获取资料的群组列表 
groupid_count | 群组ID个数
cb | 回调，返回群组资料列表，TIMGetGroupDetailInfo 

**属性说明：**

参数|说明
---|---
id | 群组ID
group |  群组Id
groupName | 群名
groupType | 群组类型
owner | 创建人
createTime| 群创建时间
lastInfoTime|最近一次修改资料时间
lastMsgTime| 最近一次发消息时间
memberNum| 群成员数量
notification| 群公告
introduction| 群简介
faceURL|群头像

**示例：  **

```
void DemoGetGroupDetailInfo()
{
	const char** groups = new const char*[DEMO_MEM_COUNT];
	groups[0] = "TGID1JYSZEAEQ";
	TIMGetGroupDetailInfoCB callback;
	callback.OnSuccess = CBGetGroupDetailInfoOnSuccessImp;
	callback.OnError = CBGetGroupDetailInfoOnErrorImp;
	TIMGetGroupDetailInfo(groups, 1, &callback);
	//wait for callback
	SLEEP(1);

	delete []groups;
 }

void CBGetGroupDetailInfoOnSuccessImp(TIMGroupDetailInfoHandle* handle_array, uint32_t array_size, void* data)
{
	for (uint32_t i = 0; i <array_size; i++)
	{
		TIMGroupDetailInfoHandle handle = handle_array[i];
		printf("group :%d createtime : %u", i, GetGroupDetailInfoCreateTime(handle));
	}
}

void CBGetGroupDetailInfoOnErrorImp(int code, const char* desc, void* data)
{
	printf("CBGetGroupDetailInfoOnErrorImp Error! code = <%d> desc = <%s>", code, desc);
}
```
示例中获取群组 "TGID1JYSZEAEQ" 的详细信息。 

### 4.3 非群成员获取群组资料

TIMGetGroupDetailInfo方法只对群成员有效，非成员需要调用 TIMGetGroupPublicInfo 实现，只能获取公开信息。默认拉取基本资料，如果想拉取自定义资料，可通过【4.1 设置拉取字段】进行设置（1.9版本以上引入）。

**权限说明：**
 
任意用户可以获取群公开资料

**原型：**

```
/**
Description:	获取群组资料
@param	[in]	groupids	群组ID数组
@param	[in]	group_num	群组ID个数
@param	[in]	flag		群信息标记位
@param	[in]	custom		群扩展信息
@param	[in]	callback	回调
@return			void
@exception      none
*/
TIM_DECL void TIMGetGroupPublicInfo(const char** groupids, const uint32_t group_num, const TIMGetGroupBaseInfoFlag flag, TIMGroupCustomInfoHandle custom, TIMGetGroupDetailInfoCB *callback);
```

**参数说明：**

参数|说明
---|---
groupids |群组ID数组，需要获取资料的群组列表 
group_num | 群组ID个数
flag|群信息标记位
custom|群扩展信息 接口预留，暂不支持。
callback|回调

### 4.4 获取本人在群里的资料

如果需要获取在所有群内的资料，可以通过TIMGetGroupMemberInfo。默认拉取基本资料，如果想拉取自定义资料，可通过【4.1 设置拉取字段】进行设置（1.9版本以上引入）。

**权限说明：**

直播大群拉取不到本人资料：包括群主、管理员和部分群成员；

### 4.5 获取群内某个人的资料

（1.9版本提供）默认拉取基本资料，如果想拉取自定义资料，可通过【4.1 设置拉取字段】进行设置（1.9版本以上引入）。

**权限说明：**

直播大群只能获得部分成员的资料：包括群主、管理员和部分群成员；

## 5. 修改群资料 

### 5.1 修改群名 

通过 TIMModifyGroupName可以修改群组名称： 

**权限说明：**
 
对于公开群、聊天室和直播大群，只有群主或者管理员可以修改群名； 
对于私有群，任何人可修改群名； 

**原型：**

```
/**
Description:	修改群名
@param	[in]	groupid		群ID
@param	[in]	groupname	修改后的群名
@param	[in]	name_len	修改后的群名长度
@param	[in]	callback	回调
@return			void
@exception      none
*/
TIM_DECL void TIMModifyGroupName(const char* groupid, const char* groupname, uint32_t name_len, TIMCommCB * callback);
```

**参数说明：**

参数 | 说明
---|---
groupid		|群ID
groupname	|修改后的群名
name_len	|修改后的群名长度
callback	|回调

**示例：**

```
void DemoModifyGroupName()
{
	TIMCommCB callback;
	callback.OnSuccess = CBCommOnSuccessImp;
	callback.OnError = CBCommOnErrorImp;
	const std::string new_name = "new_name";
	TIMModifyGroupName("test_group_id", new_name.c_str(), new_name.length(), &callback);
	//wait for callback
	SLEEP(1);
}
```

示例修改群` test_group_id`的名字为 `new_name`。

### 5.2 修改群简介 

通过 TIMModifyGroupIntroduction 可以修改群组简介： 

**权限说明：**
 
对于公开群、聊天室和直播大群，只有群主或者管理员可以修改群简介； 
对于私有群，任何人可修改群简介； 

**原型：**

```
/**
Description:	修改群简介 
@param	[in]	groupid			群ID
@param	[in]	introduction	群简介
@param	[in]	introduction_len群简介长度
@param	[in]	callback		回调
@return			void
@exception      none
*/
TIM_DECL void TIMModifyGroupIntroduction(const char* groupid, const char* introduction, uint32_t introduction_len, TIMCommCB * callback);
```
**参数说明：**

参数 |说明
---|---
groupid			|群ID
introduction	|群简介，简介最长120字节 
introduction_len|群简介长度
callback	|	回调

### 5.3 修改群公告 

通过 ModifyGroupNotification可以修改群组公告： 

**权限说明：**
 
对于公开群、聊天室和直播大群，只有群主或者管理员可以修改群公告； 
对于私有群，任何人可修改群公告； 

**原型：**

```
/**
Description:	修改群公告
@param	[in]	groupid			群ID
@param	[in]	notification	群公告
@param	[in]	notification_len群公告长度
@param	[in]	callback		回调
@return			void
@exception      none
*/
TIM_DECL void TIMModifyGroupNotification(const char* groupid, const char* notification, uint32_t notification_len, TIMCommCB * callback);
```

**参数说明：**

参数|说明
---|---
groupid | 群ID 
notification | 群公告，群公告最长150字节 
notification_len | 群公告长度
callback | 回调 

### 5.4 修改群头像 

通过 TIMModifyGroupFaceUrl 可以修改群头像： 

**权限说明：**
 
对于公开群、聊天室和直播大群，只有群主或者管理员可以修改群头像； 
对于私有群，任何人可修改群头像； 

**原型：**

```
/**
Description:	修改群头像
@param	[in]	groupid			群ID
@param	[in]	face_url		群头像URL
@param	[in]	face_url_len	群头像URL长度
@param	[in]	callback		回调
@return			void
@exception      none
*/
TIM_DECL void TIMModifyGroupFaceUrl(const char* groupid, const char* face_url, uint32_t face_url_len, TIMCommCB * callback);
```

**参数说明：**

参数|说明
---|---
groupid | 群ID 
face_url| 群头像地址（最长100字节） 
face_url_len|群头像URL长度
callback | 回调

### 5.5 修改加群选项 

通过 TIMModifyGroupAddOpt 可以修改加群选项： 

**权限说明：**
 
对于公开群、聊天室和直播大群，只有群主或者管理员可以修改加群选项； 
对于私有群，只能通过邀请加入群组，不能主动申请加入某个群组； 

**原型：**

```
/**
Description:	修改加群选项
@param	[in]	groupid		群ID
@param	[in]	opt			加群选项
@param	[in]	callback	回调
@return			void
@exception      none
*/
TIM_DECL void TIMModifyGroupAddOpt(const char* groupid, const TIMGroupAddOpt opt, TIMCommCB * callback);
```

**参数说明：**

参数|说明
---|---
groupid | 群ID 
opt| 加群选项，可设置为允许任何人加入、需要审核、禁止任何人加入 
callback | 回调 

### 5.6 修改群维度自定义字段 

通过TIMModifyGroupDatilInfoV2可对群未读自定义字段进行修改，详细使用情况见后面介绍。

**权限说明：**
 
后台配置相关的key和权限； 

### 5.7 修改群员信息

通过TIMModifyGroupMemberInfo可以对群成员的信息进行修改。

**原型：**

```
typedef enum _E_TIMModifyGroupMemberFlag
{
	kModifyMsgFlag = 0x01,		// 消息屏蔽选项（0：接收；1，拒绝）. 最小权限: ROOT    自己可以修改
	kModifyRole = 0x01 << 1,	// 群内身份：300表示设置其为管理员.  最小权限: ROOT    自己不可修改
	kModifyShutupTime = 0x01 << 2,  // 禁言时间,单位:秒.           最小权限: 管理员  自己不可修改
	kModifyNameCard = 0x01 << 3 // 群名片
}TIMModifyGroupMemberFlag;
	
TIM_DECL TIMModifyGroupMemberInfoOptionHandle CreateModifyGroupMemberInfoOptionHandle();
TIM_DECL void DestroyModifyGroupMemberInfoOptionHandle(TIMModifyGroupMemberInfoOptionHandle handle);
TIM_DECL int SetGroupID4ModifyGroupMemberInfoOptionHandle(TIMModifyGroupMemberInfoOptionHandle handle, char* group_id);
TIM_DECL int SetMemberID4ModifyGroupMemberInfoOptionHandle(TIMModifyGroupMemberInfoOptionHandle handle, char* member_id);
TIM_DECL int SetFlag4ModifyGroupMemberInfoOptionHandle(TIMModifyGroupMemberInfoOptionHandle handle, TIMModifyGroupMemberFlag flag);
TIM_DECL int SetMsgFlag4ModifyGroupMemberInfoOptionHandle(TIMModifyGroupMemberInfoOptionHandle handle, uint32_t flag);
TIM_DECL int SetRole4ModifyGroupMemberInfoOptionHandle(TIMModifyGroupMemberInfoOptionHandle handle, uint32_t role);
TIM_DECL int SetShutupTime4ModifyGroupMemberInfoOptionHandle(TIMModifyGroupMemberInfoOptionHandle handle, uint32_t time);
TIM_DECL int SetNameCard4ModifyGroupMemberInfoOptionHandle(TIMModifyGroupMemberInfoOptionHandle handle, const char* name_card, uint32_t len);
TIM_DECL int SetCustomInfo4ModifyGroupMemberInfoOptionHandle(TIMModifyGroupMemberInfoOptionHandle handle, TIMGroupCustomInfoHandle custom_info_handle);
·
/**
Description:	修改群员信息
@param	[in]	opt			修改群员信息选项
@param	[in]	callback	回调
@return			void
@exception      none
*/
TIM_DECL void TIMModifyGroupMemberInfo(TIMModifyGroupMemberInfoOptionHandle opt, TIMCommCB * callback);
```

**此接口可以修改具体如下信息：**

#### 5.7.1 修改用户群内身份 

**权限说明：**
 
只有群主或者管理员可以进行对群成员的身份进行修改； 
直播大群不支持修改用户群内身份；

**原型：**

```
kModifyRole = 0x01 << 1

TIM_DECL int SetRole4ModifyGroupMemberInfoOptionHandle(TIMModifyGroupMemberInfoOptionHandle handle, uint32_t role);
```

**参数说明：**

参数|说明
---|---
role | 群内身份
| 200 普通群成员
| 300 群管理员
| 400 群主

#### 5.8.2 对群成员进行禁言 

**权限说明：**
 
只有群主或者管理员可以进行对群成员进行禁言； 

**原型：**

```
kModifyShutupTime = 0x01 << 2,

TIM_DECL int SetShutupTime4ModifyGroupMemberInfoOptionHandle(TIMModifyGroupMemberInfoOptionHandle handle, uint32_t time);
```

**参数说明：**

参数|说明
---|---
time | 禁言时间， 单位秒 

#### 5.8.3 修改群名片 

**原型：**

```
kModifyNameCard = 0x01 << 3 // 群名片

TIM_DECL int SetNameCard4ModifyGroupMemberInfoOptionHandle(TIMModifyGroupMemberInfoOptionHandle handle, const char* name_card, uint32_t len);
```

**参数说明：**

参数|说明
---|---
name_card | 要设置的群名片 
len| 群名片长度

#### 5.8.4 修改群成员维度自定义字段 

**原型：**

```
TIM_DECL int SetCustomInfo4ModifyGroupMemberInfoOptionHandle(TIMModifyGroupMemberInfoOptionHandle handle, TIMGroupCustomInfoHandle custom_info_handle);
```

**参数说明：**

参数|说明
---|---
custom_info_handle | 自定义字段集合,key 和 value 是二进制类型

#### 5.8.5 修改接收群消息选项

**原型：**

```
kModifyMsgFlag = 0x01,		// 消息屏蔽选项（0：接收；1，拒绝）

TIM_DECL int SetMsgFlag4ModifyGroupMemberInfoOptionHandle(TIMModifyGroupMemberInfoOptionHandle handle, uint32_t flag);
```

参数|说明
---|---
flag | 消息屏蔽选项（0：接收；1，拒绝）

## 6. 群组未决信息 

### 6.1 拉取群未决相关信息 

TIMGetGroupPendency 接口可拉取群未决相关信息。此处的群未决消息泛指所有需要审批的群相关的操作。例如：加群待审批，拉人入群待审批等等。即便审核通过或者拒绝后，该条信息也可通过此接口拉回，拉回的信息中有已决标志。

**权限说明：**

**只有审批人有权限拉取相关信息。**
例如：UserA申请加入群GroupA，则群管理员可获取此未决相关信息，UserA因为没有审批权限，不需要过去未决信息。 
         如果AdminA拉UserA进去GroupA，则UserA可以拉取此未决相关信息，因为该未决信息待UserA审批。 

**原型：**

```
/**
Description:	拉取群未决相关信息
@param	[in]	opt			拉取群未决相关选项
@param	[in]	callback
@return			void
@exception      none
*/
TIM_DECL void TIMGetGroupPendency(TIMGetGroupPendencyOptHandle opt, TIMGetGroupPendencyCB* callback);
```

**参数说明：**

参数|说明
---|---
opt|未决参数配置
callback|回调，返回未决列表
 
**拉取未决的option相关操作： **

```
TIM_DECL TIMGetGroupPendencyOptHandle CreateGetGroupPendencyOptHandle();
TIM_DECL void DestroyGetGroupPendencyOptHandle(TIMGetGroupPendencyOptHandle opt);
TIM_DECL int SetStartTime4GetGroupPendencyOptHandle(TIMGetGroupPendencyOptHandle opt, uint64_t start_time);
TIM_DECL int SetMaxCount4GetGroupPendencyOptHandle(TIMGetGroupPendencyOptHandle opt, uint32_t max);
```

属性说明： 
start_time：拉取的开始时戳。如果从最新的未决条目开始拉取，则填0或不填。若分页，则回调中返回下一个分页的拉取起始时戳。 
max：一次拉取的最多条目数，用于分页。 

**拉取未决的回调说明： **

```
	typedef void(*CBGetGroupPendencyOnSuccess)(TIMGroupPendencyMetaHandle meta, TIMGroupPendencyItemHandle* items, uint32_t item_size, void* data);
```

**参数说明：**

参数|说明
---|---
meta|拉取操作返回的相关信息，包含分页信息和拉取状态等。 
items|拉取的未决条目TIMGroupPendencyItemHandle数组 .

**meta属性说明： **

```
//拉取起点时戳 单位：ms 未0时全部拉完
TIM_DECL TIMGroupPendencyMetaHandle CloneGroupPendencyMetaHandle(TIMGroupPendencyMetaHandle meta);
TIM_DECL void DestroyGroupPendencyMetaHandle(TIMGroupPendencyMetaHandle meta);
TIM_DECL uint64_t GetNextStartTime4GroupPendencyMetaHandle(TIMGroupPendencyMetaHandle meta);
//已读时戳 单位:ms
TIM_DECL uint64_t GetReportTimeStamp4GroupPendencyMetaHandle(TIMGroupPendencyMetaHandle meta);
TIM_DECL uint32_t GetUnreadCount4GroupPendencyMetaHandle(TIMGroupPendencyMetaHandle meta);
```

属性|说明
---|---
NextStartTime|拉取下一个分页的起始时戳，用于传入拉取配置中。为0时表示没有后面的分页了。 
ReportTimeStamp|已读时戳，用来判定未决条目是否已读。 
UnreadCount|所有未读条目个数。不限制于本次分页中。 

**未决条目相关属性：**

```
TIM_DECL TIMGroupPendencyItemHandle CloneGroupPendencyItemHandle(TIMGroupPendencyItemHandle handle);
TIM_DECL void DestroyGroupPendencyItemHandle(TIMGroupPendencyItemHandle handle);
TIM_DECL int GetGroupId4GroupPendencyItemHandle(TIMGroupPendencyItemHandle handle, char* id, uint32_t* id_len);
//获取申请者ID
TIM_DECL int GetReqId4GroupPendencyItemHandle(TIMGroupPendencyItemHandle handle, char* id, uint32_t* id_len);
//获取判决者ID
TIM_DECL int GetRspId4GroupPendencyItemHandle(TIMGroupPendencyItemHandle handle, char* id, uint32_t* id_len);
//未决请求时间 单位:ms
TIM_DECL uint64_t GetTime4GroupPendencyItemHandle(TIMGroupPendencyItemHandle handle);
TIM_DECL TIMGroupPendencyType GetPendencyType4GroupPendencyItemHandle(TIMGroupPendencyItemHandle handle);
TIM_DECL TIMGroupPendencyHandleFlag GetHandleFlag4GroupPendencyItemHandle(TIMGroupPendencyItemHandle handle);
TIM_DECL TIMGroupPendencyHandleResult GetHandleResult4GroupPendencyItemHandle(TIMGroupPendencyItemHandle handle);

TIM_DECL int GetApplyInviteMsg4GroupPendencyItemHandle(TIMGroupPendencyItemHandle handle, char* msg, uint32_t* msg_len);
TIM_DECL int GetReqUserData4GroupPendencyItemHandle(TIMGroupPendencyItemHandle handle, char* data, uint32_t* data_len);
TIM_DECL int GetApprovalMsg4GroupPendencyItemHandle(TIMGroupPendencyItemHandle handle, char* msg, uint32_t* msg_len);
TIM_DECL int GetRspUserData4GroupPendencyItemHandle(TIMGroupPendencyItemHandle handle, char* data, uint32_t* data_len);
```

**属性说明： **

属性|说明
---|---
GroupId|群ID 
ReqId|未决发起者ID 
RspId|未决审批者ID 
Time|添加未决时间 
PendencyType|枚举未决条目类型： 请求加群；邀请加群 
PendencyHandleFlag|枚举未决条目状态：未决；他人已决；操作者已决 说明：UserA申请加入Group，AdminA审批通过。则AdminB拉取的此未决条目的类型为，他们已决。
PendencyHandleResult|枚举审批结果：同意；拒绝 
ApplyInviteMsg/ApprovalMsg|申请、审批时的hello word

**示例：**

```
void CBGetGroupPendencyOnSuccessImp(TIMGroupPendencyMetaHandle meta, TIMGroupPendencyItemHandle* items, uint32_t item_size, void* data)
{
	printf("report time:%llu, unread count:%u, next time:%llu \n",
	GetReportTimeStamp4GroupPendencyMetaHandle(meta), GetUnreadCount4GroupPendencyMetaHandle(meta), GetNextStartTime4GroupPendencyMetaHandle(meta));
	for (uint32_t i = 0; i < item_size; i++)
	{
		char buf[BUF_LEN] = { 0 };
		auto handle = items[i];
		uint32_t len = BUF_LEN; GetReqId4GroupPendencyItemHandle(handle, buf, &len);
		printf("request user id:%s\n", buf);
		len = BUF_LEN; GetApplyInviteMsg4GroupPendencyItemHandle(handle, buf, &len);
		std::string apply_invite_msg = buf;
		len = BUF_LEN; GetReqUserData4GroupPendencyItemHandle(handle, buf, &len);
		std::string req_user_data = buf;
		printf("type:%u, handle flag:%u, handle result:%u hello_msg:%s data:%s",
		GetPendencyType4GroupPendencyItemHandle(handle),
		GetHandleFlag4GroupPendencyItemHandle(handle),
		GetHandleResult4GroupPendencyItemHandle(handle),
		apply_invite_msg.c_str(), req_user_data.c_str());
	}
}
void CBGetGroupPendencyOnErrorImp(int code, const char* desc, void* data)
{
	printf("CBGetGroupPendencyOnErrorImp Error! code = <%d> desc = <%s>", code, desc);
}
void DemoGetGroupPendency()
{
	auto opt = CreateGetGroupPendencyOptHandle();
	int ret = SetStartTime4GetGroupPendencyOptHandle(opt, 0);
	SetStartTime4GetGroupPendencyOptHandle(opt, 0);
	SetMaxCount4GetGroupPendencyOptHandle(opt, 1);
	
	TIMGetGroupPendencyCB cb;
	void* handle_copy = 0;
	cb.OnSuccess = CBGetGroupPendencyOnSuccessImp;
	cb.OnError = CBGetGroupPendencyOnErrorImp;
	cb.data = &handle_copy;
	TIMGetGroupPendency(opt, &cb);

	DestroyGetGroupPendencyOptHandle(opt);
	SLEEP(5);
}
```

### 6.2上报群未决已读 

对于未决信息，sdk可对其和之前的所有未决信息上报已读。上报已读后，仍然可以拉取到这些未决信息，但可通过对已读时戳的判断判定未决信息是否已读。 

**原型：**

```
/**
Description:	上报群未决已读
@param	[in]	report_time	上报已读时间戳
@param	[in]	cb			回调
@return			void
@exception      none
*/
TIM_DECL void TIMGroupPendencyReport(uint64_t report_time, TIMCommCB* cb);
```

**参数说明：**

参数|说明
---|---
report_time|上报已读时戳。对于单条未决信息，时戳包含在其属性里。 
cb|回调 


**示例：**

```
void DemoReportGroupPendency()
{
	TIMCommCB cb;
	cb.OnSuccess = CBCommOnSuccessImp;
	cb.OnError = CBCommOnErrorImp;
	cb.data = &cb;
	TIMGroupPendencyReport(0, &cb); //填写已读时戳，可从未决信息中获取
	
	SLEEP(5);
}
```

### 6.3 处理群未决信息 

对于群的未决信息，sdk增加了处理接口。审批人可以选择对单条信息进行同意或者拒绝。已处理成功过的未决信息不能再次处理。 

**原型：**

```
/**
Description:	处理群未决请求
@param	[in]	pendency_item_handle	未决条目
@param	[in]	result					审批结果
@param	[in]	approval_msg			审批信息
@param	[in]	msg_len					审批信息长
@param	[in]	user_data				审批自定义数据
@param	[in]	data_len				审批自定义数据长度
@param	[in]	cb						回调
@return			void
@exception      none
*/
TIM_DECL void TIMGroupHandlePendency(TIMGroupPendencyItemHandle pendency_item_handle, TIMGroupPendencyHandleResult result, const char* approval_msg, uint32_t msg_len, const char* user_data, uint32_t data_len, TIMCommCB* cb);
```

**示例：**

```
void DemoHandleGroupPendency()
{
	const char* msg = "ok";
	const char* data = "whatever";

	TIMCommCB cb;
	cb.OnSuccess = CBCommOnSuccessImp;
	cb.OnError = CBCommOnErrorImp;
	cb.data = &cb;
	//pendency item 可以从获取未决信息接口取得
	TIMGroupHandlePendency(gitem, TIMGroupPendencyConfirmed, msg, strlen(msg), data, strlen(data), &cb);

	SLEEP(5);

}
```
## 7. 群资料存储

在1.9版本之前，并未存储用户的群资料数据，每次调用接口都是从服务端重新获取，需要APP端进行存储，1.9以后版本，增加了群资料存储，可以设置存储的具体字段，参考 [4.1 设置拉取字段](#4.1-.E8.AE.BE.E7.BD.AE.E6.8B.89.E5.8F.96.E5.AD.97.E6.AE.B5)。另外，这里仅存储群资料，并未对群成员的资料获取，1.9版本以后会在群消息中增加用户的相关字段，建议直接从消息中获取。

### 7.1 启用群资料存储

**原型：**

```
/**
Description:	启用群资料存储
@return			void
@exception      none
*/
void TIMEnableGroupAssistantStorage();
```

###  7.2 群组资料获取同步接口

为了方便读取，1.9以后版本增加了群组资料的同步接口（需要开启群资料存储），

**原型：**

```
typedef void* TIMGroupAssistantGroupInfo;
TIMGroupAssistantGroupInfo CreateTIMGroupAssistantGroupInfo();
void DestroyTIMGroupAssistantGroupInfo(TIMGroupAssistantGroupInfo info);
uint32_t TIMGetGroupNumber4TIMGroupAssistantGroupInfo(TIMGroupAssistantGroupInfo info);
TIMGroupDetailInfoHandle TIMGetGroupDetailInfo4TIMGroupAssistantGroupInfo(TIMGroupAssistantGroupInfo info, uint32_t index);
/**
Description:	同步获取群信息
@param	[in]	info	同步信息
@return			void
@exception      none
*/
void TIMGroupAssistantGetGroups(TIMGroupAssistantGroupInfo info);
```

### 7.3 群通知回调

如果开启了存储，可以设置监听感知群事件，当有对应事件发生时，会进行回调：

**原型：**

```
typedef void(*CBOnMemberJoin)(const char* groupId, const char** id, uint32_t num);
typedef void(*CBOnMemberQuit)(const char* groupId, const char** id, uint32_t num);
typedef void(*CBOnMemberUpdate)(const char* groupId, const char** id, uint32_t num);

//group info notify
typedef void(*CBOnGroupAdd)(const char* groupId);
typedef void(*CBOnGroupDelete)(const char* groupId);
typedef void(*CBOnGroupUpdate)(const char* groupId);

typedef struct _T_TIMGroupAssistantCallBack
{
	CBOnMemberJoin onMemberJoin;	//有新用户加入群时的通知回调
	CBOnMemberQuit onMemberQuit;	//有群成员退群时的通知回调
	CBOnMemberUpdate onMemberUpdate;//群成员信息更新的通知回调
	CBOnGroupAdd onAdd;				//加入群的通知回调
	CBOnGroupDelete onQuit;			//解散群的通知回调
	CBOnGroupUpdate onUpdate;		//群资料更新的通知回调
}TIMGroupAssistantCallBack;

/**
Description:	群通知回调
@param	[in]	cb		回调
@return			void
@exception      none
*/
void TIMSetGroupAssistantCallBack(TIMGroupAssistantCallBack* cb);
```

**参数说明：**

群成员变更时通过onMemberUpdate回调

## 8. 群事件消息 

当有用户被邀请加入群组，或者有用户被移出群组时，群内会产生有提示消息，调用方可以根据需要展示给群组用户，或者忽略。提示消息使用一个特殊的Elem标识，通过新消息回调返回消息（参见新消息通知）：
如下图中，展示一条修改群名的事件消息： 
![](//mccdn.qcloud.com/static/img/cc5b0e33ed6bd492fca7d8fb8469307a/image.jpg)
**消息原型：**

```
typedef enum_E_TIM_GROUPTIPS_TYPE
{
	TIM_GROUP_TIPS_TYPE_INVITE              = 0x01, //邀请加入群
	TIM_GROUP_TIPS_TYPE_QUIT_GRP            = 0x02, //退出群
	TIM_GROUP_TIPS_TYPE_KICKED              = 0x03, //踢出群 
	TIM_GROUP_TIPS_TYPE_SET_ADMIN           = 0x04, //设置管理员
	TIM_GROUP_TIPS_TYPE_CANCEL_ADMIN        = 0x05, //取消管理员
	TIM_GROUP_TIPS_TYPE_INFO_CHANGE         = 0x06, //群资料变更
	TIM_GROUP_TIPS_TYPE_MEMBER_INFO_CHANGE  = 0x07, //群成员资料变更 
}E_TIM_GROUPTIPS_TYPE;

//群Tips类型
typedef void* TIMMsgGroupTipsElemHandle;
E_TIM_GROUPTIPS_TYPEGetGroupTipsInfoType(TIMMsgGroupTipsElemHandle handle);
//群名
int	GetGroupTipsInfoGroupName(TIMMsgGroupTipsElemHandle handle, char* group_name, uint32_t * len);
//操作人ID
int	GetGroupTipsInfoOperatorID(TIMMsgGroupTipsElemHandle handle, char* id, uint32_t * len);
//被操作人列表
uint32_t GetGroupTipsInfoUsersNum(TIMMsgGroupTipsElemHandle handle);
int	GetGroupTipsInfoUsers(TIMMsgGroupTipsElemHandle handle, TIMGroupTipsUserInfoHandle* handles, uint32_t* num);
//被操作人ID
typedef void* TIMGroupTipsUserInfoHandle;
int GetGroupTipsUserInfoID(TIMGroupTipsUserInfoHandle handle, char* id, uint32_t * len);
//群信息变更列表
uint32_t GetGroupTipsInfoGroupChangeInfoNum(TIMMsgGroupTipsElemHandle handle);
int GetGroupTipsInfoGroupChangeInfo(TIMMsgGroupTipsElemHandle handle, TIMGroupChangeInfoHandle* handles, uint32_t* num);
//群成员变更列表
uint32_t GetGroupTipsInfoMemberChangeInfoNum(TIMMsgGroupTipsElemHandle handle);
int GetGroupTipsInfoMemberChangeInfo(TIMMsgGroupTipsElemHandle handle, TIMGroupMemberInfoChangeHanlde* handles, uint32_t* num);
```
调用方可选择是否予以展示，以及如何展示。 
消息元素属性说明： 
群Tips类型 : 见枚举定义 
操作人 ：引起发该Tips的用户 
被操作人列表：该操作影响到的用户   
该属性目前只包含被操作人的ID 
群信息变更列表：群相关的变更信息 
群信息变更类型： 定义如下： 

```
#defineTIM_GROUP_INFO_CHAGE_TYPE_GROUP_NAME	0x1 //群名更改
#defineTIM_GROUP_INFO_CHAGE_TYPE_INTRODUCTION	0x2 //群简介更改
#defineTIM_GROUP_INFO_CHAGE_TYPE_NOTIFACTION	0x3 //群通知更改
#defineTIM_GROUP_INFO_CHAGE_TYPE_FACE_URL		0x4 //群头像更改
#defineTIM_GROUP_INFO_CHAGE_TYPE_OWNER			0x5 //群主更改
```
变更的群信息：在各种群信息变更类型下对应的信息 
群员变更列表：TIM_GROUP_TIPS_TYPE_MEMBER_INFO_CHANGE类型时对应的信息 包括的属性有： 
群成员禁言时间 

**示例：**

```
void DemoGetGroupTips(TIMMsgElemHandle handle)
{
	const uint32_t MAX_CHANGE_NUM = 100; //实际根据情况动态创建
	TIMElemType type = GetElemType(handle);
	if (kElemGroupTips != type)
	{
		printf("not group tips!");
		return;
	}
	E_TIM_GROUPTIPS_TYPE tips_type=GetGroupTipsInfoType(handle);
	switch (tips_type)
	{
	case TIM_GROUP_TIPS_TYPE_INVITE:
	case TIM_GROUP_TIPS_TYPE_KICKED:
	case TIM_GROUP_TIPS_TYPE_QUIT_GRP:
		{
			printf("invited kicked or quit");
		}
		break;
	case TIM_GROUP_TIPS_TYPE_SET_ADMIN:
	case TIM_GROUP_TIPS_TYPE_CANCEL_ADMIN:
		{
			printf("set or cancel ADMIN");
		}
		break;
	case TIM_GROUP_TIPS_TYPE_INFO_CHANGE:
		{
	uint32_t change_num=GetGroupTipsInfoGroupChangeInfoNum(handle);
TIMGroupChangeInfoHandle* change_infos = new TIMGroupChangeInfoHandle[change_num];
			GetGroupTipsInfoGroupChangeInfo(handle, change_infos, &change_num);
			for (uint32_t i = 0; i<change_num; i++)
			{		printf("type :%d",GetGroupChangeInfoType(change_infos[i]));
			}
			delete []change_infos;
			break;
		}
	case TIM_GROUP_TIPS_TYPE_MEMBER_INFO_CHANGE:
		{
			uint32_tchange_num = GetGroupTipsInfoMemberChangeInfoNum(handle);
			TIMGroupMemberInfoChangeHanlde* change_infos = newTIMGroupMemberInfoChangeHanlde[change_num];
			GetGroupTipsInfoMemberChangeInfo(handle, change_infos, &change_num);
			for (uint32_t i = 0; i<change_num; i++)
			{
				printf("shutup time :%d", TIMGetGroupMemberChangeInfoShutTime(change_infos[i]));
			}
			delete []change_infos;
			break; 
		}
	}
}

```

### 8.1 用户加入群组 

当有用户加入群组时（包括申请入群和被邀请入群），群组内会由系统发出通知，开发者可选择展示样式。收到的消息type为 TIM_GROUP_TIPS_TYPE_INVITE。 
该类型下可获取**参数说明：**

Type ：TIM_GROUP_TIPS_TYPE_INVITE 
操作人 ：申请入群：申请人/邀请入群：邀请人 
群名 ：群名 
被操作人列表：入群的用户列表 

### 8.2 用户退出群组 

当有用户主动退群时，群组内会由系统发出通知。收到的消息type为 TIM_GROUP_TIPS_TYPE_QUIT_GRP。 

该类型下可获取**参数说明： **

Type ：TIM_GROUP_TIPS_TYPE_QUIT_GRP 
操作人 ：退出用户identifier 
群名 ：群名 

### 8.3 用户被踢出群组 

当有用户被踢出群组时，群组内会由系统发出通知。收到的消息type为 TIM_GROUP_TIPS_TYPE_KICKED。 

TIMGroupTipsElem **参数说明：**
 
Type ： TIM_GROUP_TIPS_TYPE_KICKED 
操作人 ： 踢人的用户identifier 
群名 ： 群名 
被操作人列表：被踢用户列表 

### 8.4 被设置/取消管理员 

当有用户被设置为管理员或者被取消管理员身份时，群组内会由系统发出通知。收到的消息type为 TIM_GROUP_TIPS_TYPE_SET_ADMIN和 TIM_GROUP_TIPS_TYPE_CANCEL_ADMIN 。
 
TIMGroupTipsElem **参数说明：**
 
type： 设置：TIM_GROUP_TIPS_TYPE_SET_ADMIN 
取消：TIM_GROUP_TIPS_TYPE_CANCEL_ADMIN 
操作人 ： 操作用户identifier 
群名 ： 群名 
被操作人列表：被设置/取消管理员身份的用户列表 

### 8.5 群资料变更 

当群资料变更，如群名、群简介等，会有系统消息发出，可更新相关字段展示，或者选择性把消息展示给用户。 

TIMGroupTipsElem **参数说明：**
 
type： TIM_GROUP_TIPS_TYPE_INFO_CHANGE 
操作人 ： 操作用户identifier 
群名 ： 群名 
群信息变更列表： 群变更的具体资料信息，为TIMGroupChangeInfoHandle数组 
TIMGroupChangeInfoHandle原型：  

```
#define TIM_GROUP_INFO_CHAGE_TYPE_GROUP_NAME	0x1
#define TIM_GROUP_INFO_CHAGE_TYPE_INTRODUCTION	0x2
#define TIM_GROUP_INFO_CHAGE_TYPE_NOTIFACTION	0x3
#define TIM_GROUP_INFO_CHAGE_TYPE_FACE_URL		0x4
#define TIM_GROUP_INFO_CHAGE_TYPE_OWNER			0x5

int	GetGroupChangeInfoType(TIMGroupChangeInfoHandle handle);
uint32_t GetGroupChangeInfoLen(TIMGroupChangeInfoHandle handle);
uint32_t GetGroupChangeInfo(TIMGroupChangeInfoHandle handle, char* info, uint32_t *len);
```
**说明：**
 
Type： 变更类型 
groupName： 变更后的群名，如果没有变更则为NULL 
introduction： 变更后的群简介，如果没有变更则为NULL 
notification： 变更后的群公告，如果没有变更则为NULL 
faceUrl： 变更后的群头像URL，如果没有变更则为NULL 
owner： 变更后的群主，如果没有变更则为NULL 

### 8.6 群成员资料变更 

当群成员的资料变更时，会有系统消息发出，可更新相关字段展示，或者选择性把消息展示给用户。 

TIMGroupTipsElem **参数说明：**
 
type： TIM_GROUP_TIPS_TYPE_MEMBER_INFO_CHANGE 
操作人 ： 操作用户identifier 
群名： 群名 
群成员资料变更列表：变更的群成员的具体资料信息，为 
TIMGroupMemberInfoChangeHanlde列表 
TIMGroupMemberInfoChangeHanlde原型： 

```
typedef void* TIMGroupMemberInfoChangeHanlde;
int GetGroupMemberChangeInfoID(TIMGroupMemberInfoChangeHanlde handle, char* id, uint32_t * len);
uint32_t TIMGetGroupMemberChangeInfoShutTime(TIMGroupMemberInfoChangeHanlde handle);
```
**说明：**
 
identifier： 变更的用户identifier 
shutupTime： 被禁言的时间 

## 9 群系统消息 

当有用户申请加群等事件发生时，管理员会收到邀请加群系统消息，用户可根据情况接受请求或者拒绝，相应的消息通过群系统消息展示给用户。 
群系统消息类型定义： 

```
//群系统消息类型
typedef enum _E_TIM_GROUP_SYSTEM_TYPE
{
	TIM_GROUP_SYSTEM_ADD_GROUP_REQUEST_TYPE		= 0x01, //申请加群请求（只有管理员会收到）
	TIM_GROUP_SYSTEM_ADD_GROUP_ACCEPT_TYPE      = 0x02,//申请加群被同意（只有申请人能够收到）
	TIM_GROUP_SYSTEM_ADD_GROUP_REFUSE_TYPE      = 0x03,//申请加群被拒绝（只有申请人能够收到）
	TIM_GROUP_SYSTEM_KICK_OFF_FROM_GROUP_TYPE	= 0x04,//被管理员踢出群（只有被踢的人能够收到）
	TIM_GROUP_SYSTEM_DELETE_GROUP_TYPE			= 0x05,//群被解散（全员能够收到）
	TIM_GROUP_SYSTEM_CREATE_GROUP_TYPE			= 0x06,//创建群消息（创建者能够收到）
	TIM_GROUP_SYSTEM_INVITED_TO_GROUP_TYPE		= 0x07,//邀请加群（被邀请者能够收到）
	TIM_GROUP_SYSTEM_QUIT_GROUP_TYPE			= 0x08,//主动退群（主动退群者能够收到）
	TIM_GROUP_SYSTEM_GRANT_ADMIN_TYPE			= 0x09,//设置管理员(被设置者接收)
	TIM_GROUP_SYSTEM_CANCEL_ADMIN_TYPE			= 0x0a,//取消管理员(被取消者接收)
	TIM_GROUP_SYSTEM_REVOKE_GROUP_TYPE			= 0x0b,//群已被回收(全员接收)
	TIM_GROUP_SYSTEM_INVITED_NEED_CONFIRM		= 0x0c,//邀请加群(只有被邀请者会接收到)
	TIM_GROUP_SYSTEM_INVITED_CONFIRMED			= 0x0d,//邀请加群被同意(只有发出邀请者会接收到)
	TIM_GROUP_SYSTEM_INVITED_REJECTED			= 0x0e,//邀请加群被拒绝(只有发出邀请者会接收到)
	TIM_GROUP_SYSTEM_CUSTOM_INFO				= 0xff,//用户自定义通知(默认全员接收)
}E_TIM_GROUP_SYSTEM_TYPE;

//操作类型
E_TIM_GROUP_SYSTEM_TYPEGetGroupReportType(TIMMsgGroupReportElemHandle handle);
//群组Id
intGetGroupReportID(TIMMsgGroupReportElemHandle handle, char* id, uint32_t* len);
//操作人
int	GetGroupReportOperatorID(TIMMsgGroupReportElemHandle handle, char* id, uint32_t* len);
//操作理由
int GetGroupReportRemarkInfoLen(TIMMsgGroupReportElemHandle handle);
int	GetGroupReportRemarkInfo(TIMMsgGroupReportElemHandle handle, char* remark_info, uint32_t* len);

//审批入群申请，目前只对申请加群消息生效
int HandleJoinRequest(TIMMsgGroupReportElemHandle handle, int flag, TIMCommCB* cb);
```
**参数说明：**
 
Flag 0x00:拒绝入群0x01:同意入群 

**示例：**
 
示例中收到群系统消息，如果是入群申请，默认同意，如果是群解散通知，打印信息。其他类型消息解析方式相同。 

### 9.1 申请加群消息 

触发时机：当有用户申请加群时，群管理员会收到申请加群消息，可展示给用户，由用户决定是否同意对方加群，如果管理员同意，可调用HandleJoinRequest方法。 
消息类型为：TIM_GROUP_SYSTEM_ADD_GROUP_REQUEST_TYPE 

**参数说明：**

参数 | 说明
---|---
type | TIM_GROUP_SYSTEM_ADD_GROUP_REQUEST_TYPE 
group | 群组Id，表示是哪个群的申请 
user | 申请人 
msg | 申请理由，（可选） 

 
### 9.2 申请加群同意/拒绝消息 

触发时机：当管理员同意加群请求时，申请人会收到同意入群的消息，当管理员拒绝时，收到拒绝入群的消息。 

**参数说明：**

参数 | 说明
---|---
type | 同意：TIM_GROUP_SYSTEM_ADD_GROUP_ACCEPT_TYPE 
| 拒绝：TIM_GROUP_SYSTEM_ADD_GROUP_REFUSE_TYPE 
group | 群组Id，表示是哪个群通过/拒绝了 
user | 处理请求的管理员identifier 
msg | 同意或者拒绝理由（可选） 
 
### 9.3 邀请入群消息 

触发时机：当有用户被邀请群时，该用户会收到邀请入群消息，可展示给用户，由用户决定是否同意入群，如果同意，调用可调用HandleJoinRequest方法。 
消息类型为：TIM_GROUP_SYSTEM_INVITE_TO_GROUP_REQUEST_TYPE 

**参数说明：**

参数 | 说明
---|---
type | TIM_GROUP_SYSTEM_INVITE_TO_GROUP_REQUEST_TYPE 
group | 群组Id，表示是哪个群的邀请 
user | 邀请人 

审批同意入群，可调用HandleJoinRequest。 

### 9.4 邀请入群同意/拒绝消息 

触发时机：当被邀请者同意入群请求时，邀请者会收到同意入群的消息；当被邀请者拒绝时，邀请者会收到拒绝入群的消息。 

**参数说明：**

参数 | 说明
---|---
type | 同意：TIM_GROUP_SYSTEM_INVITE_TO_GROUP_ACCEPT_TYPE 
| 拒绝：TIM_GROUP_SYSTEM_INVITE_TO_GROUP_REFUSE_TYPE 
group | 群组Id，表示是对哪个群通过/拒绝了 
user | 处理请求的用户identifier 
msg | 同意或者拒绝理由（可选） 

### 9.5 被管理员踢出群组 

触发时机：当用户被管理员踢出群组时，申请人会收到被踢出群的消息。 

**参数说明：**

参数 | 说明
---|---
type | TIM_GROUP_SYSTEM_KICK_OFF_FROM_GROUP_TYPE 
group | 群组Id，表示在哪个群里被踢了 
user | 操作管理员identifier 
### 9.6 群被解散 

触发时机：当群被解散时，全员会收到解散群消息。 

**参数说明：**

参数 | 说明
---|---
type | TIM_GROUP_SYSTEM_DELETE_GROUP_TYPE 
group | 群组Id，表示哪个群被解散了 
user | 操作管理员identifier 

### 9.7 创建群消息 

触发时机：当群创建时，创建者会收到创建群消息。 
当调用创建群方法成功回调后，即表示创建成功，此消息主要为多终端同步，如果有在其他终端登录，做为更新群列表的时机，本终端可以选择忽略。 

**参数说明：**

参数 | 说明
---|---
type | TIM_GROUP_SYSTEM_CREATE_GROUP_TYPE 
group | 群组Id，表示创建的群Id 
user | 创建者，这里也就是用户自己 

### 9.8 邀请加群 

触发时机：当用户被邀请加入群组时，该用户会收到邀请消息，注意：创建群组时初始成员无需邀请即可入群。 

**参数说明：**

参数 | 说明
---|---
type | TIM_GROUP_SYSTEM_INVITED_TO_GROUP_TYPE 
group | 群组Id，邀请进入哪个群 
user | 操作人，表示哪个用户的邀请 

**方法说明：**

当用户同意入群，可调用accept方法 
当用户不同意，可调用refuse方法。 

### 9.9 主动退群 

触发时机：当用户主动退出群组时，该用户会收到退群消息，只有退群的用户自己可以收到。 
当用户调用QuitGroup时成功回调返回，表示已退出成功，此消息主要为了多终端同步，其他终端可以做为更新群列表的时机，本终端可以选择忽略。 

**参数说明：**

参数 | 说明
---|---
type | TIM_GROUP_SYSTEM_QUIT_GROUP_TYPE 
group | 群组Id，表示退出的哪个群 
user | 操作人，这里即为用户自己 

### 9.10 设置/取消管理员 

触发时机：当用户被设置为管理员时，可收到被设置管理员的消息通知，当用户被取消管理员时，可收到取消通知，可提示用户。 

**参数说明：**

参数 | 说明
---|---
type | 取消管理员身份:TIM_GROUP_SYSTEM_GRANT_ADMIN_TYPE 
授予管理员身份|TIM_GROUP_SYSTEM_CANCEL_ADMIN_TYPE 
group | 群组Id，表示哪个群的事件 
user | 操作人 

### 9.11 群被回收 

触发时机：当群组被系统回收时，全员可收到群组被回收消息。 

**参数说明：**

参数 | 说明
---|---
type | TIM_GROUP_SYSTEM_REVOKE_GROUP_TYPE 
group | 群组Id，表示哪个群被回收了 

## 10 搜索群

通过 SearchGroup 成员方法可以模糊搜索群组，目前只支持群名匹配关键字。

原型：

@interface TIMGroupManager : NSObject


```
/**
Description:	通过名称信息获取群资料（可指定字段拉取）
@param	[in]	name		群名
@param	[in]	name_len	群名长度
@param	[in]	flag		要获取的群基本信息flag
@param	[in]	custom		要获取的群扩展信息
@param	[in]	page_num	分页号
@param	[in]	num_perpage	每页群组数目
@param	[in]	cb			回调
@return			TIM_DECL void
@exception      none
*/
TIM_DECL void TIMSearchGroupByName(const char* name, uint32_t name_len, TIMGetGroupBaseInfoFlag flag, IMGroupCustomInfoHandle custom, uint32_t page_num, uint32_t num_perpage, TIMSearcgGroupByNameCB* cb);
```

**参数说明：**

参数 | 说明
---|---
name| 要检索的群名中关键字 
name_len| 关键字长度
flag | 要获取的群资料字段，详情可参考TIMGetGroupBaseInfoFlag 
custom | 要获取的群扩展信息 
page_num | 分页号，从0开始 
num_perpage | 每页的大小 
cb | 回调，返回群列表 
fail | 失败回调，返回错误码和错误原因 

