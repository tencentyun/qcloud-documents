## 1. 群组综述 

IM云通讯有多种群组类型，其特点以及限制因素可参考[群组系统](/doc/product/269/群组系统)。群组使用唯一Id标识，通过群组Id可以进行不同操作。

## 2. 群组消息 

群组消息与C2C消息相同，仅在获取Conversation时的会话类型不同，可参照 [消息发送](/doc/product/269/消息收发（Android%20SDK）#1-.E6.B6.88.E6.81.AF.E5.8F.91.E9.80.81) 部分。

## 3. 群组管理

群组相关操作都由 TIMGroupManager 实现，需要用户登录成功后操作。

**获取单例原型：**

```
public static TIMGroupManager getInstance()
```

### 3.1 创建内置类型群组


可通过createGroup接口创建群组，创建时可指定群组类型，群组名称以及要加入的用户列表，创建成功后返回群组Id，可通过群组Id获取Conversation收发消息等。

另外 CreateAVChatRoomGroup 创建直播大群，此类型群可以加入人数不做限制，但是有一些能力上的限制，如不能拉人进去，不能查询总人数等，可参阅 [直播场景下的 IM 集成方案](/doc/product/269/4104)。

**原型： **

```
//创建群组
public void createGroup(java.lang.String type,
               java.util.List<java.lang.String> members,
               java.lang.String groupName,
               TIMValueCallBack<java.lang.String> cb)

//创建音视频聊天室（可支持超大群，详见wiki文档）
public void createAVChatroomGroup(String groupName, TIMValueCallBack<String> cb)
```

**参数说明：**

参数|说明
---|---
type | 群类型: 私有群（Private）、公开群（Public）、聊天室（ChatRoom）、互动直播聊天室（AVChatRoom）和在线成员广播大群（BChatRoom）
members | 待加入群组的成员列表，创建者默认加入，无需指定（群内最多10000人）
groupName | 群组名称（最长30字节）
cb | 回调，OnSuccess函数的参数中将返回创建成功的群组Id

**示例：**


```
//创建待加入群组的用户列表
ArrayList<String> list = new ArrayList<String>();
 
String user = "";
 
//添加用户
user = "sample_user_1";
list.add(user);
user = "sample_user_2";
list.add(user);
user = "sample_user_3";
list.add(user);
 
//创建回调
TIMValueCallBack<String> cb = new TIMValueCallBack<String>() {
    @Override
    public void onError(int code, String desc) {
        Log.e(tag, "create group failed: " + code + " desc");
    }
 
    @Override
    public void onSuccess(String s) { //回调返回创建的群组Id
        Log.e(tag, "create group succ: " + s);
    }
};
 
//创建群组
TIMGroupManager.getInstance().createGroup(
    "Private",          //群组类型: 目前仅支持私有群
        list,               //待加入群组的用户列表
        "test_group",       //群组名称
        cb);                //回调
				
//创建直播大群
TIMGroupManager.getInstance().createAVChatroomGroup("TVShow", new TIMValueCallBack<String>() {
    @Override
    public void onError(int code, String desc) {
        Log.d(tag, "create av group failed. code: " + code + " errmsg: " + desc);
    }

    @Override
    public void onSuccess(String s) {
        Log.d(tag, "create av group succ, groupId:" + s);
    }
});

```

### 3.2 创建指定属性群组

在创建群组时，除了设置默认的成员以及群名外，如果还需要设置如群ID、群公告、群简介等字段，可以通过以下接口来创建群组：

**原型：**
```
public void createGroup(TIMGroupManager.CreateGroupParam param, TIMValueCallBack<String> cb)
```
根据指定的信息创建群组

**参数说明：**

参数|说明
---|---
param | 创建群组需要的信息集, 详见TIMGroupManager.CreateGroupParam
cb | 回调，OnSuccess函数的参数中将返回创建成功的群组Id

TIMGroupManager.CreateGroupParam 提供的属性设置方法：
```
/**
 * 设置要创建的群的类型（必填）
 * @param type 群类型, 目前支持的群类型："Public", "Private", "ChatRoom", "AVChatRoom", "BChatRoom"
 */
public void setGroupType(String type)

/**
 * 设置要创建的群的名称（必填）
 * @param name 群名称
 */
public void setGroupName(String name)

/**
 * 设置要创建的群的群ID
 * @param groupId 群ID
 */
public void setGroupId(String groupId)

/**
 * 设置要创建的群的群公告
 * @param notification 群公告
 */
public void setNotification(String notification)

/**
 * 设置要创建的群的群简介
 * @param introduction 群简介
 */
public void setIntroduction(String introduction)

/**
 * 设置要创建的群的群头像URL
 * @param url 群头像URL
 */
public void setFaceUrl(String url)

/**
 * 设置要创建的群的加群选项
 * @param option 加群选项
 */
public void setAddOption(TIMGroupAddOpt option)

/**
 * 设置要创建的群允许的最大成员数
 * @param maxMemberNum 最大成员数
 */
public void setMaxMemberNum(long maxMemberNum)

/**
 * 设置要创建的群的自定义信息
 * @param key 自定义信息key, 最长16字节
 * @param value 自定义信息value，最长512字节
 */
public void setCustomInfo(String key, byte[] value)

/**
 * 设置要创建的群的初始成员
 * @param infos 初始成员的信息列表
 */
public void setMembers(List<TIMGroupMemberInfo> infos)
```

**示例：**
```
TIMGroupManager.CreateGroupParam param = TIMGroupManager.getInstanceById(identifier).new CreateGroupParam();
param.setGroupType("Public");
param.setGroupName("hello");
param.setIntroduction("hello world");
param.setNotification("welcome to hello group");

//添加群成员
List<TIMGroupMemberInfo> infos = new ArrayList<TIMGroupMemberInfo>();
TIMGroupMemberInfo member = new TIMGroupMemberInfo();
member.setUser(identifier2);
member.setRoleType(TIMGroupMemberRoleType.NotMember);
infos.add(member);        
param.setMembers(infos);

//设置群自定义字段，需要先到控制台配置相应的key
try {
    param.setCustomInfo("GroupKey1", "wildcat".getBytes("utf-8"));
} catch (UnsupportedEncodingException e) {
    e.printStackTrace();
}

//创建群组
TIMGroupManager.getInstance().createGroup(param, new TIMValueCallBack<String>() {
    @Override
    public void onError(int code, String desc) {
        Log.d(tag, "create group failed. code: " + code + " errmsg: " + desc);
    }

    @Override
    public void onSuccess(String s) {
        Log.d(tag, "create group succ, groupId:" + s);
    }
});
```

### 3.3 自定义群组Id创建群组

默认创建群组时，IM通讯云服务器会生成一个唯一的Id，以便后续操作，另外，如果用户需要自定义群组Id，在创建时可指定Id，通过 [创建指定属性群组](#3.2-.E5.88.9B.E5.BB.BA.E6.8C.87.E5.AE.9A.E5.B1.9E.E6.80.A7.E7.BE.A4.E7.BB.84) 也可以实现自定义群组Id的功能。

**原型：**
```
public void createGroup(String type, List<String> members, String groupName, String groupId, TIMValueCallBack<String> cb)
```
创建群组，可以指定群组类型、群组名和群组Id

**参数说明：**

参数|说明
---|---
type | 群类型: 私有群（Private）、公开群（Public）、聊天室（ChatRoom）、互动直播聊天室（AVChatRoom）和在线成员广播大群（BChatRoom）
members | 待加入群组的成员列表，创建者默认加入，无需指定（群内最多10000人）
groupName | 群组名称（最长30字节）
groupId | 自定义群组id
cb | 回调，OnSuccess函数的参数中将返回创建成功的群组Id

**示例：**
```
//创建待加入群组的用户列表
ArrayList<String> list = new ArrayList<String>();
 
String user = "";
 
//添加用户
user = "sample_user_1";
list.add(user);
user = "sample_user_2";
list.add(user);
user = "sample_user_3";
list.add(user);
 
//创建回调
TIMValueCallBack<String> cb = new TIMValueCallBack<String>() {
    @Override
    public void onError(int code, String desc) {
        Log.e(tag, "create group failed: " + code + " desc");
    }
 
    @Override
    public void onSuccess(String s) { //回调返回创建的群组Id
        Log.e(tag, "create group succ: " + s);
    }
};
 
//创建群组
TIMGroupManager.getInstance().createGroup(
    "Private",          //群组类型: 目前仅支持私有群
        list,               //待加入群组的用户列表
        "test_group",       //群组名称
				"12345678",         //群组ID
        cb);                //回调
```

### 3.4 邀请用户入群

TIMGroupManager 的接口 InviteGroupMember 可以拉（邀请）用户进入群组。

**权限说明：**

私有群：群成员无需受邀用户同意，直接将其拉入群中。
公开群/聊天室：不允许群成员邀请他人入群。
互动直播聊天室：不允许任何人（包括APP管理员）邀请他人入群。

**原型： **  

```
public void inviteGroupMember(java.lang.String groupId,
                     java.util.List<java.lang.String> memList,
                     TIMValueCallBack<java.util.List<TIMGroupMemberResult>> cb)
```
邀请加入群组

**参数说明：**

参数|说明
---|---
groupId | 群组id
memList | 待加入群组的用户id列表
cb | 回调，OnSuccess函数的参数中返回成功加入群组的用户列表以及操作结果状态

**TIMGroupMemberResult：**
```
/**
 * 获取操作结果
 * @return 操作结果 ： 0：失败；1：成功；2：添加成员时，该成员已经在群组中 或 删除成员时，该成员不在群组中
 */
public long getResult()

/**
 * 获取用户帐号
 * @return 用户帐号
 */
public String getUser()
```


**示例：**

```
//创建待加入群组的用户列表
ArrayListlist = new ArrayList();
 
String user = "";
 
//添加用户
user = "sample_user_1";
list.add(user);
user = "sample_user_2";
list.add(user);
user = "sample_user_3";
list.add(user);
 
//回调
TIMValueCallBack<List<TIMGroupMemberResult>> cb = new TIMValueCallBack<List<TIMGroupMemberResult>>() {
    @Override
    public void onError(int code, String desc) {
    }
 
    @Override
    public void onSuccess(List<TIMGroupMemberResult> results) { //群组成员操作结果
        for(TIMGroupMemberResult r : results) {
            Log.d(tag, "result: " + r.getResult()  //操作结果:  0:添加失败；1：添加成功；2：原本是群成员
                    + " user: " + r.getUser());    //用户帐号
        }
    }
};
 
//将list中的用户加入群组
TIMGroupManager.getInstance().inviteGroupMember(
        groupId,   //群组Id
        list,      //待加入群组的用户列表
        cb);       //回调
```

### 3.5 申请加入群组

TIMGroupManager 的接口 applyJoinGroup可以主动申请进入群组，此操作只对公开群和聊天室有效。

**权限说明：**
 
私有群不能由用户主动申请入群； 
公开群和聊天室可以主动申请进入， 如果群组设置为需要审核，申请后管理员和群主会受到申请入群系统消息，需要等待管理员或者群主审核，如果群组设置为任何人可加入，则直接入群成功；
直播大群可以任意加入群组。

**原型：**

```
public void applyJoinGroup(java.lang.String groupId,
                  java.lang.String reason,
                  TIMCallBack cb)
```
加入群组

**参数说明：**

参数|说明
---|---
groupId | 群组id
reason | 申请理由（选填）
cb | 回调


**示例：**

```
TIMGroupManager.getInstance().applyJoinGroup("TGID1JYSZEAEQ", "some reason", new TIMCallBack() {
    @java.lang.Override
    public void onError(int code, String desc) {
        //接口返回了错误码code和错误描述desc，可用于原因
        //错误码code列表请参见错误码表
        Log.e(tag, "disconnected");
    }
 
    @java.lang.Override
    public void onSuccess() {
        Log.i(tag, "join group");
    }
});
```

示例中用户申请加入群组@"TGID1JYSZEAEQ"，申请理由为"some reason"。

### 3.6 退出群组

群组成员可以主动退出群组。

**权限说明：**

对于私有群，全员可退出群组； 
对于公开群、聊天室和直播大群，群主不能退出；

**原型：**

```
public void quitGroup(java.lang.String groupId,
             TIMCallBack cb)
```
退出群组

**参数说明：**

参数|说明
---|---
groupId | 群组Id
cb | 回调

**示例：**

```
//创建回调
TIMCallBack cb = new TIMCallBack() {
    @Override
    public void onError(int code, String desc) {
            //错误码code和错误描述desc，可用于定位请求失败原因
            //错误码code含义请参见错误码表
    }
 
    @Override
    public void onSuccess() {
        Log.e(tag, "quit group succ");
    }
};
 
//退出群组
TIMGroupManager.getInstance().quitGroup(
        groupId,  //群组Id
        cb);      //回调
```

### 3.7 删除群组成员

群组成员也可以删除其他成员，函数参数信息与加入群组相同。

**权限说明：**

对于私有群：只有创建者可删除群组成员 
对于公开群和聊天室：只有管理员和群主可以踢人 
对于直播大群：不能踢人

**原型：  **

```
public void deleteGroupMember(java.lang.String groupId,
                              java.util.List<java.lang.String> memList,
                              TIMValueCallBack<java.util.List<TIMGroupMemberResult>> cb)
```
删除群组成员

**参数说明：**

参数|说明
---|---
groupId | 群组Id
memList | 待删除的群成员列表
cb | 回调，OnSuccess函数的参数中返回成功删除的群成员列表

**示例：**

```
//创建待踢出群组的用户列表
ArrayListlist = new ArrayList();
 
String user = "";
//添加用户
user = "sample_user_1";
list.add(user);
user = "sample_user_2";
list.add(user);
user = "sample_user_3";
list.add(user);
 
//创建回调
TIMValueCallBack<List<TIMGroupMemberResult>> cb = new TIMValueCallBack<List<TIMGroupMemberResult>>() {
        @Override
        public void onError(int code, String desc) {
        }
 
        @Override
        public void onSuccess(List<TIMGroupMemberResult> results) { //群组成员操作结果
            for(TIMGroupMemberResult r : results) {
                Log.d(tag, "result: " + r.getResult()  //操作结果:  0：删除失败；1：删除成功；2：不是群组成员
                        + " user: " + r.getUser());    //用户帐号
            }
        }
};
 
//将list中的用户踢出群组
TIMGroupManager.getInstance().deleteGroupMember(
            groupId,  //群组Id
            list,     //待踢出群组的用户列表
            cb);      //回调
```

### 3.8 获取群成员列表

getGroupMembers 方法可获取群内成员列表，默认拉取内置字段，但不拉取自定义字段，想要获取自定义字段，可通过[设置拉取字段](#4.1-.E8.AE.BE.E7.BD.AE.E6.8B.89.E5.8F.96.E5.AD.97.E6.AE.B5)进行设置（1.9版本以上引入）。

**权限说明：**

任何群组类型都可以获取成员列表； 
直播大群只能拉取部分成员列表：包括群主、管理员和部分成员；

**原型：   **

```
public void getGroupMembers(java.lang.String groupId,
                   TIMValueCallBack<java.util.List<TIMGroupMemberInfo>> cb)
```
获取群组成员

**参数说明：**

参数|说明
---|---
groupId | 群组Id
cb | 回调，OnSuccess函数的参数中返回群组成员列表

**示例：**

```
//创建回调
TIMValueCallBack<List<TIMGroupMemberInfo>> cb = new TIMValueCallBack<List<TIMGroupMemberInfo>> () {
    @Override
    public void onError(int code, String desc) {
    }
 
    @Override
    public void onSuccess(List<TIMGroupMemberInfo> infoList) {//参数返回群组成员信息
 
        for(TIMGroupMemberInfo info : infoList) {
            Log.d(tag, "user: " + info.getUser() +
            "join time: " + info.getJoinTime() +
            "role: " + info.getRole());
        }
    }
};
 
//获取群组成员信息
TIMGroupManager.getInstance().getGroupMembers(
        groupId, //群组Id
        cb);     //回调
```

### 3.9 获取加入的群组列表

通过 getGroupList 可以获取当前用户加入的所有群组：

**权限说明：**

此接口可以获取自己所加入的群列表，返回的信息只包含部分基本信息，详细群组信息可以根据[群成员获取群组资料](#4.2-.E7.BE.A4.E6.88.90.E5.91.98.E8.8E.B7.E5.8F.96.E7.BE.A4.E7.BB.84.E8.B5.84.E6.96.99)进行获取。

> 私有群、公开群和聊天室支持使用本接口获取用户加入的群组；
互动直播聊天室和在线成员广播大群因为内部实现的差异，获取用户加入的群组时不会获取到这两种类型的群组。

**原型： **   

```
public void getGroupList(TIMValueCallBack<java.util.List<TIMGroupBaseInfo>> cb)
```
获取已加入的群组列表

**参数说明：**

参数|说明
---|---
cb | 回调，OnSuccess函数的参数中返回已加入的群组信息，详见 TIMGroupBaseInfo

TIMGroupBaseInfo提供的方法如下：
```
/**
 * 获取群组Id
 * @return 群组Id
 */
public String getGroupId()

/**
 * 获取群组名称
 * @return 群组名称
 */
public String getGroupName()

/**
 * 获取群组类型
 * @return 群组类型
 */
public String getGroupType()

/**
 * 获取群头像URL
 * @return 群头像URL
 */
public String getFaceUrl()

/**
 * 获取自己在这个群内的群内资料
 * @return 自己在这个群内的简单群内资料，详见{@see TIMGroupBasicSelfInfo}
 */
public TIMGroupBasicSelfInfo getSelfInfo()
```

**示例：**

```
//创建回调
TIMValueCallBack<List<TIMGroupBaseInfo>> cb = new TIMValueCallBack<List<TIMGroupBaseInfo>>() {
    @Override
    public void onError(int code, String desc) {
        //错误码code和错误描述desc，可用于定位请求失败原因
        //错误码code含义请参见错误码表
        Log.e(tag, "get gruop list failed: " + code + " desc");
    }
 
    @Override
    public void onSuccess(List<TIMGroupBaseInfo> timGroupInfos) {//参数返回各群组基本信息
        Log.d(tag, "get gruop list succ");
 
        for(TIMGroupBaseInfo info : timGroupInfos) {
            Log.d(tag, "group id: " + info.getGroupId() +
            " group name: " + info.getGroupName() +
            " group type: " + info.getGroupType());
        }
    }
};
 
//获取已加入的群组列表
TIMGroupManager.getInstance().getGroupList(cb);
```

### 3.10 解散群组

通过 `deleteGroup` 可以解散群组。

**权限说明：**

对于私有群，任何人都无法解散群组 
对于公开群、聊天室和直播大群，群主可以解散群组

**原型：   **

```
public void deleteGroup(java.lang.String groupId,TIMCallBack cb)
```
删除群组

**参数说明：**

参数|说明
---|---
groupId | 群组Id
cb | 回调

**示例：**

```
//解散群组
TIMGroupManager.getInstance().deleteGroup(groupId, new TIMCallBack() {
    @Override
    public void onError(int code, String desc) {
 
        //错误码code和错误描述desc，可用于定位请求失败原因
        //错误码code列表请参见错误码表
        Log.d(tag, "login failed. code: " + code + " errmsg: " + desc);
    }
 
    @Override
    public void onSuccess() {
        //解散群组成功
    }
});
```

###  3.11 转让群组 

通过modifyGroupOwner可以进行群转让，更换群主。 

**权限说明：**
 
只有群主可以进行群转让操作。 

**原型：**

```
public void modifyGroupOwner(java.lang.String groupId,
                             java.lang.String identifier,
                             TIMCallBack cb)
```
修改群组基本信息-转让群组 

**参数说明：**

参数|说明
---|---
groupId | 群组ID 
identifier | 新群主的identifier 
cb | 回调 

**示例：**
无 

### 3.12 删除群组成员（带原因）

群组成员也可以删除其他成员，函数参数信息与加入群组相同。

**权限说明：**

对于私有群：只有创建者可删除群组成员 
对于公开群和聊天室：只有管理员和群主可以踢人 
对于直播大群：不能踢人

**原型：  ** 

```
public void deleteGroupMemberWithReason(java.lang.String groupId,
                               java.lang.String reason,
                               java.util.List<java.lang.String> memList,
                               TIMValueCallBack<java.util.List<TIMGroupMemberResult>> cb)
```
删除群组成员

**参数说明：**

参数|说明
---|---
groupId | 群组Id
reason | 删除原因
memList | 待删除的群成员列表
cb | 回调，OnSuccess函数的参数中返回成功删除的群成员列表

**示例：**
```
//创建待踢出群组的用户列表
ArrayList<String> list = new ArrayList<String>();
String user = "";
 
//添加用户
user = "sample_user_1";
list.add(user);
 
TIMGroupManager.getInstance().deleteGroupMemberWithReason("TGID1JYSZEAEQ", "some reason", list, new TIMValueCallBack<List<TIMGroupMemberResult>>() {
    @java.lang.Override
    public void onError(int code, String desc) {
        Log.e(tag, "error code: " + code + " desc: " + desc);
    }
 
    @java.lang.Override
    public void onSuccess(List<TIMGroupMemberResult> timGroupMemberResultList) {
        for(TIMGroupMemberResult r : timGroupMemberResultList) {
            Log.i(tag, "user: " + r.getUser() + " result: " + r.getResult());
        }
    }
});
```

示例中把用户 "sample_user_1" 从群组 "TGID1JYSZEAEQ" 中删除，执行成功后返回操作列表以及操作状态。
TIMGroupMemberResult 含义参照 [邀请用户入群](#3.4-.E9.82.80.E8.AF.B7.E7.94.A8.E6.88.B7.E5.85.A5.E7.BE.A4)。



### 3.13 其他接口

- 获取指定类型成员（可按照管理员、群主、普通成员拉取）
```
/**
 * 根据过滤条件获取群成员列表(支持按字段拉取，分页)
 * @param groupId 群组Id
 * @param flags 拉取资料标志， 如{@see TIMGroupManager#TIM_GET_GROUP_MEM_INFO_FLAG_NAME_CARD}等标志的或组合位图
 * @param filter 角色过滤类型，详见{@see TIMGroupMemberRoleFilter}
 * @param custom 要获取的自定义key列表
 * @param nextSeq 分页拉取标志，第一次拉取填0，回调成功如果不为零，需要分页，传入再次拉取，直至为0
 * @param cb 回调
 */
public void getGroupMembersByFilter(String groupId, long flags, TIMGroupMemberRoleFilter filter,
																		List<String> custom, long nextSeq, TIMValueCallBack<TIMGroupMemberSuccV2> cb)
```

## 4. 获取群组资料

###  4.1 设置拉取字段

拉取用户资料默认返回部分内置字段，如果需要自定义字段，或者不拉取某些字段，可以通过 `TIMManager` 中的 `initGroupSettings` 接口进行设置（**此接口1.9版本以上提供**），此设置对所有资料相关接口（`getGroupList` 除外）有效，全局有效。

**原型：**
```
public void initGroupSettings(TIMGroupSettings settings)
```
初始化群设置（**需登录前设置。不设置：默认拉取所有基本字段，不拉取自定义字段**）

**参数说明：**

参数|说明
---|---
settings | 群设置，详见javadoc中的TIMGroupSettings

**TIMGroupSettings：**
```
/**
 * 设置群资料操作选项
 * @param groupInfoOptions 群操作选项，{@see TIMGroupSettings#Options}
 */
public void setGroupInfoOptions(TIMGroupSettings.Options groupInfoOptions)

/**
 * 设置群成员资料操作选项
 * @param memberInfoOptions 群成员操作选项，{@see TIMGroupSettings#Options}
 */
public void setMemberInfoOptions(TIMGroupSettings.Options memberInfoOptions)
```

**TIMGroupSettings.Options：**
```
/**
 * 设置群信息或者群成员信息的拉取标志，默认全部拉取
 * @param flags 拉取资料标志, 群资料标志如{@see TIMGroupManager#TIM_GET_GROUP_BASE_INFO_FLAG_NAME}等，
 *              群成员资料标志如{@see TIMGroupManager#TIM_GET_GROUP_MEM_INFO_FLAG_NAME_CARD}等
 */
public void setFlags(long flags)

/**
 * 设置自定义资料标签
 * @param customTags 自定义资料标签
 */
public void setCustomTags(List<String> customTags)
```

**示例：**

```
TIMGroupSettings settings = new TIMGroupSettings();

//设置群资料拉取字段，这里只关心群头像、群类型、群主ID
TIMGroupSettings.Options groupOpt = settings.new Options();
long groupFlags = 0;
groupFlags |= TIMGroupManager.TIM_GET_GROUP_BASE_INFO_FLAG_FACE_URL
				| TIMGroupManager.TIM_GET_GROUP_BASE_INFO_FLAG_GROUP_TYPE
				| TIMGroupManager.TIM_GET_GROUP_BASE_INFO_FLAG_OWNER_UIN;
groupOpt.setFlags(groupFlags);
settings.setGroupInfoOptions(groupOpt);

//设置群成员资料拉取字段，这里只关心群名片、群角色
TIMGroupSettings.Options memberOpt = settings.new Options();
long memberFlags = 0;
memberFlags |= TIMGroupManager.TIM_GET_GROUP_MEM_INFO_FLAG_NAME_CARD
				| TIMGroupManager.TIM_GET_GROUP_MEM_INFO_FLAG_ROLE_INFO;
memberOpt.setFlags(memberFlags);
settings.setMemberInfoOptions(memberOpt);

//初始化群设置
TIMManager.getInstance().initGroupSettings(settings);
```

### 4.2 群成员获取群组资料

getGroupDetailInfo方法可以获取群组资料。默认拉取基本资料，如果想拉取自定义资料，可通过 [设置拉取字段](#4.1-.E8.AE.BE.E7.BD.AE.E6.8B.89.E5.8F.96.E5.AD.97.E6.AE.B5)进行设置（1.9版本以上引入）。

**权限说明：**

>注意：此接口只能由群成员调用，非群成员获取群组资料请参考 [非群成员获取群组资料](#4.3-.E9.9D.9E.E7.BE.A4.E6.88.90.E5.91.98.E8.8E.B7.E5.8F.96.E7.BE.A4.E7.BB.84.E8.B5.84.E6.96.99)。

**原型：    **

```
public void getGroupDetailInfo(java.util.List<java.lang.String> groupIdList,
                      TIMValueCallBack<java.util.List<TIMGroupDetailInfo>> cb)
```
获取群组详细信息

**参数说明：**

参数|说明
---|---
groupIdList | 需要拉取详细信息的群组Id列表
cb | 回调，OnSuccess函数的参数中返回群组信息列表

**TIMGroupDetailInfo:**
```
/**
 * 获取群组Id
 * @return 群组Id
 */
public String getGroupId()

/**
 * 获取群组名称
 * @return 群组名称
 */
public String getGroupName()

/**
 * 获取群组创建者帐号
 * @return 群组创建者帐号
 */
public String getGroupOwner()

/**
 * 获取群组创建时间
 * @return 群组创建时间
 */
public long getCreateTime()

/**
 * 获取群组信息最后修改时间
 * @return 群组信息最后修改时间
 */
public long getLastInfoTime()

/**
 * 获取最新群组消息时间
 * @return 最新群组消息时间
 */
public long getLastMsgTime()

/**
 * 获取群组成员数量
 * @return 群组成员数量
 */
public long getMemberNum()

/**
 * 获取允许的最大群成员数
 * @return 最大群成员数
 */
public long getMaxMemberNum()

/**
 * 获取群简介内容
 * @return 群简介内容
 */
public String getGroupIntroduction()

/**
 * 获取群公告内容
 * @return 群公告内容
 */
public String getGroupNotification()

/**
 * 获取群头像URL
 * @return 群头像URL
 */
public String getFaceUrl()

/**
 * 获取群类型
 * @return 群类型
 */
public String getGroupType()

/**
 * 获取加群选项
 * @return 加群选项
 */
public TIMGroupAddOpt getGroupAddOpt()

/**
 * 获取群组内最新一条消息
 * @return 群组内最新一条消息
 */
public TIMMessage getLastMsg()

/**
 * 获取群组自定义字段map
 * @return 群组自定义字段map
 */
public Map<String, byte[]> getCustom()

/**
 * 获取在线群成员数（需要通过填写工单申请开通才会返回有效值，其中音视频直播大群无法申请开通）
 * @return  在线群成员数
 */
public long getOnlineMemberNum() 
```

**示例：**

```
//创建待获取信息的群组Id列表
ArrayList<String> groupList = new ArrayList<String>();
 
//创建回调
TIMValueCallBack<List<TIMGroupDetailInfo>> cb = new TIMValueCallBack<List<TIMGroupDetailInfo>>() {
    @Override
    public void onError(int code, String desc) {
            //错误码code和错误描述desc，可用于定位请求失败原因
            //错误码code列表请参见错误码表
    }
 
    @Override
    public void onSuccess(List<TIMGroupDetailInfo> infoList) { //参数中返回群组信息列表
        for(TIMGroupDetailInfo info : infoList) {
            Log.d(tag, "groupId: " + info.getGroupId()           //群组Id
            + " group name: " + info.getGroupName()              //群组名称
            + " group owner: " + info.getGroupOwner()            //群组创建者帐号
            + " group create time: " + info.getCreateTime()      //群组创建时间
            + " group last info time: " + info.getLastInfoTime() //群组信息最后修改时间
            + " group last msg time: " + info.getLastMsgTime()  //最新群组消息时间
            + " group member num: " + info.getMemberNum());      //群组成员数量
        }
    }
};
 
//添加群组Id
String groupId = "TGID1EDABEAEO";
groupList.add(groupId);
 
//获取群组详细信息
TIMGroupManager.getInstance().getGroupDetailInfo(
        groupList, //需要获取信息的群组Id列表
        cb);       //回调
```


### 4.3 非群成员获取群组资料

当用户不在群组时，可以通过接口getGroupPublicInfo获取群的公开资料。获取结果为TIMGroupDetailInfo结构，此时该结构只含有公开资料，其余字段为空。默认拉取基本资料，如果想拉取自定义资料，可通过 [设置拉取字段](#4.1-.E8.AE.BE.E7.BD.AE.E6.8B.89.E5.8F.96.E5.AD.97.E6.AE.B5)进行设置（1.9版本以上引入）。

**原型：**

```
public void getGroupPublicInfo(List<String> groupIdList, TIMValueCallBack<List<TIMGroupDetailInfo>> cb)
```
获取群组公开信息（非群组成员也可以调用）

**参数说明：**

参数|说明
---|---
groupList | 需要拉取详细信息的群组Id列表
cb | 回调，OnSuccess函数的参数中返回群组公开信息列表

**示例：**

```
//创建待获取公开信息的群组列表
List<String> groupList = new ArrayList<String>();
 
groupList.add(groupId);
 
//获取群组公开信息
TIMGroupManager.getInstance().getGroupPublicInfo(groupList, new TIMValueCallBack<List<TIMGroupDetailInfo>>() {
    @Override
    public void onError(int code, String desc) {
        //错误码code和错误描述desc，可用于定位请求失败原因
        //错误码code列表请参见错误码表
        Log.e(tag, "get gruop list failed: " + code + " desc" + desc);
 
    }
 
    @Override
    public void onSuccess(List<TIMGroupDetailInfo> timGroupDetailInfos) {
        //此时TIMGroupDetailInfo只含有群公开资料，其余字段为空
    }
});
```

### 4.4 获取本人在群里的资料

如果需要获取本人在所有群内的资料，可以通过 [GetGroupList](#3.9-.E8.8E.B7.E5.8F.96.E5.8A.A0.E5.85.A5.E7.9A.84.E7.BE.A4.E7.BB.84.E5.88.97.E8.A1.A8) 拉取加入的群列表时得到（1.9版本以后支持）。另外，如果需要单独获取某个群组，可使用以下接口，建议通过GetGroupList获取，没有必要调用以下接口单独获取。默认拉取基本资料，如果想拉取自定义资料，可通过 [设置拉取字段](#4.1-.E8.AE.BE.E7.BD.AE.E6.8B.89.E5.8F.96.E5.AD.97.E6.AE.B5)进行设置（1.9版本以上引入）。

**权限说明：**

直播大群无法获取本人在群内的资料；

**原型：**
```
public void getSelfInfo(String groupId, TIMValueCallBack<TIMGroupSelfInfo> cb)
```
获取自己在群组中的信息

**参数说明：**

参数|说明
---|---
groupId | 群组Id
cb | 回调， 在OnSuccess函数的参数中返回自身信息

### 4.5 获取群内某个人的资料

（1.9版本提供）默认拉取基本资料，如果想拉取自定义资料，可通过 [设置拉取字段](#4.1-.E8.AE.BE.E7.BD.AE.E6.8B.89.E5.8F.96.E5.AD.97.E6.AE.B5) 进行设置（1.9版本以上引入）。

**权限说明：**

直播大群只能获得部分成员的资料：包括群主、管理员和部分群成员；

**原型：**
```
public void getGroupMembersInfo(String groupId, List<String> identifiers,
                                    TIMValueCallBack<List<TIMGroupMemberInfo>> cb)
```
获取指定的群成员的群内信息

**参数说明：**

参数|说明
---|---
groupId | 指定群ID
identifiers | 指定群成员identifier，一次最多100个
cb | 回调，OnSuccess函数的参数中返回群组成员列表


## 5. 修改群资料

### 5.1 修改群名

通过 modifyGroupName可以修改群组名称：

**权限说明：**

对于公开群、聊天室和直播大群，只有群主或者管理员可以修改群名； 
对于私有群，任何人可修改群名； 

**原型：**

```
public void modifyGroupName(java.lang.String groupId,
                   java.lang.String groupName,
                   TIMCallBack cb)
```
修改群组基本信息 － 修改群名称

**参数说明：**

参数|说明
---|---
groupId | 群组Id
groupName | 新群组名称
cb | 回调

**示例：**

```
//创建回调
TIMCallBack cb = new TIMCallBack() {
    @Override
    public void onError(int code, String desc) {
    }
 
    @Override
    public void onSuccess() {
    }
};
 
//修改群组名称
TIMGroupManager.getInstance().modifyGroupName(
    groupId,                //群组Id
    "new_group_name",       //新名称
    cb);                    //回调
```

### 5.2 修改群简介

通过 modifyGroupIntroduction可以修改群组简介：

**权限说明：**

对于公开群、聊天室和直播大群，只有群主或者管理员可以修改群简介； 
对于私有群，任何人可修改群简介；

**原型：**

```
public void modifyGroupIntroduction(java.lang.String groupId,
                                    java.lang.String introduction,
                                    TIMCallBack cb)
```
修改群组基本信息 － 修改群简介

**参数说明：**

参数|说明
---|---
groupId | 群组Id
introduction | 新群组简介（最长120字节）
cb | 回调

**示例：**

```
//创建回调
TIMCallBack cb = new TIMCallBack(){
    @Override
    public void onError(int code, String desc){
        //错误码code和错误描述desc，可用于定位请求失败原因
        //错误码code列表请参见错误码表
        Log.e(tag, "Modify group info failed: " + code + " desc" + desc);
    }
     
    @Override
    public void onSuccess(){
        Log.e(tag, "Modify group info succ");
    }
};
 
//修改群简介
TIMGroupManager.getInstance().modifyGroupIntroduction(groupId, "hello everyone", cb);
```

### 5.3 修改群公告

通过 modifyGroupNotification可以修改群组公告：

**权限说明：**

对于公开群、聊天室和直播大群，只有群主或者管理员可以修改群公告； 
对于私有群，任何人可修改群公告；

**原型：**

```
public void modifyGroupNotification(java.lang.String groupId,
                                    java.lang.String notice,
                                    TIMCallBack cb)
```
修改群组基本信息 － 修改群公告

**参数说明：**

参数|说明
---|---
groupId | 群组Id
notice | 新群组公告（最长150字节）
cb | 回调

**示例：**

```
//创建回调
TIMCallBack cb = new TIMCallBack(){
    @Override
    public void onError(int code, String desc){
        //错误码code和错误描述desc，可用于定位请求失败原因
        //错误码code列表请参见错误码表
        Log.e(tag, "Modify group info failed: " + code + " desc" + desc);
    }
     
    @Override
    public void onSuccess(){
        Log.e(tag, "Modify group info succ");
    }
};
 
//修改群公告
TIMGroupManager.getInstance().modifyGroupNotification(groupId, "be attention to this", cb);
```

### 5.4 修改群头像

通过 modifyGroupFaceUrl可以修改群头像：

**权限说明：**

对于公开群、聊天室和直播大群，只有群主或者管理员可以修改群头像； 
对于私有群，任何人可修改群头像； 

**原型：**

```
public void modifyGroupFaceUrl(java.lang.String groupId,
                               java.lang.String url,
                               TIMCallBack cb)
```
修改群组基本信息 － 修改群头像

**参数说明：**

参数|说明
---|---
groupId | 群组Id
url | 新群组头像URL（最长100字节）
cb | 回调

**示例：**

```
//创建回调
TIMCallBack cb = new TIMCallBack(){
    @Override
    public void onError(int code, String desc){
        //错误码code和错误描述desc，可用于定位请求失败原因
        //错误码code列表请参见错误码表
        Log.e(tag, "Modify group info failed: " + code + " desc" + desc);
    }
     
    @Override
    public void onSuccess(){
        Log.e(tag, "Modify group info succ");
    }
};
 
//修改群头像url
TIMGroupManager.getInstance().modifyGroupFaceUrl(groupId, "http://newface.url/", cb);
```

### 5.5 修改加群选项

通过 modifyGroupAddOpt可以修改加群选项：

**权限说明：**

对于公开群、聊天室和直播大群，只有群主或者管理员可以修改加群选项； 
对于私有群，只能通过邀请加入群组，不能主动申请加入某个群组； 

**原型：**


```
public void modifyGroupAddOpt(java.lang.String groupId,
                              TIMGroupAddOpt opt,
                              TIMCallBack cb)
```
修改群组基本信息 － 修改群头像

**参数说明：**

参数|说明
---|---
groupId | 群组Id
opt | 加群选项，可设置为允许任何人加入、需要审核、禁止任何人加入
cb | 回调

**示例：**


```
//创建回调
TIMCallBack cb = new TIMCallBack(){
    @Override
    public void onError(int code, String desc){
        //错误码code和错误描述desc，可用于定位请求失败原因
        //错误码code列表请参见错误码表
        Log.e(tag, "Modify group info failed: " + code + " desc" + desc);
    }
     
    @Override
    public void onSuccess(){
        Log.e(tag, "Modify group info succ");
    }
};
 
//修改加群选项：允许任何人加入
TIMGroupManager.getInstance().modifyGroupAddOpt(groupId, TIMGroupAddOpt.TIM_GROUP_ADD_ANY, cb);
```



###  5.6 修改群维度自定义字段 

通过modifyGroupCustomInfo可以对群维度自定义字段进行修改。

**权限说明：**
 
后台配置相关的key和权限； 

**原型：**

```
public void modifyGroupCustomInfo(java.lang.String groupId,
                                 java.lang.String key,
                                 byte[] value,
                                 TIMCallBack cb)
```
修改群组基本信息-设置群组自定义字段 

**参数说明：**

参数|说明
---|---
groupId | 群组ID 
key | 群组自定义字段的 
value | 群组自定义字段的value 
cb | 回调 

**示例：**

```
//定义回调
TIMCallBack cb = new TIMCallBack() {
    @Override
    public void onError(int code, String desc) {
        Log.e(tag, "modify group info failed, code:" + code +"|desc:" + desc);
    }

    @Override
    public void onSuccess() {
        Log.e(tag, "modify group info succ");
    }
}
//调用接口修改群资料自定义信息
try {
    TIMGroupManager.getInstance().modifyGroupCustomInfo(groupId, "tag", "cats".getBytes("utf-8"), cb);
} catch (UnsupportedEncodingException e) {
    e.printStackTrace();
}
```


### 5.7 修改用户群内身份 

通过modifyGroupMemberInfoSetRole可以对群成员的身份进行修改。 

**权限说明：**

只有群主或者管理员可以进行对群成员的身份进行修改； 
直播大群不支持修改用户群内身份；

**原型：**

```
public void modifyGroupMemberInfoSetRole(java.lang.String groupId,
                                         java.lang.String identifier,
                                         TIMGroupMemberRoleType type,
                                         TIMCallBack cb)
```
修改群成员信息-设置群成员身份（只有群主和管理员可以调用） 

**参数说明：**

参数|说明
---|---
groupId | 所在群的群 
identifier | 要修改的群成员的identifier 
type | 修改后的身份类型。不能修改为群主类型，详见TIMGroupMemberRoleType 
cb | 回调 

**示例：**

```
//修改群成员身份，设置为管理员
TIMGroupManager.getInstance().modifyGroupMemberInfoSetRole(groupId, user, TIMGroupMemberRoleType.Admin, new TIMCallBack() {
    @Override
    public void onError(int code, String desc) {
        //错误码code和错误描述desc，可用于定位请求失败原因
        //错误码code列表请参见错误码表
        Log.e(tag, "modifyGroupMemberInfoSetRole failed: " + code + " desc" + desc);
    }

    @Override
    public void onSuccess() {
        Log.e(tag, "modifyGroupMemberInfoSetRole succ");
    }
});
```

###  5.8 对群成员进行禁言

通过modifyGroupMemberInfoSetSilence可以对群成员进行禁言并设置禁言时长。 

**权限说明：**

只有群主或者管理员可以进行对群成员进行禁言。 

**原型： **

```
public void modifyGroupMemberInfoSetSilence(java.lang.String groupId,
                                            java.lang.String identifier,
                                            long seconds,
                                            TIMCallBack cb)
```
修改群成员信息-设置禁言时间（只有群主和管理员可以调用） 。

**参数说明：**

参数|说明
---|---
groupId | 所在群的群Id 
identifier | 要修改的群成员的identifier 
seconds | 禁言时间， 单位秒 
cb | 回调 

**示例：**

```
//对user禁言10秒
TIMGroupManager.getInstance().modifyGroupMemberInfoSetSilence(groupId, user, 10, new TIMCallBack() {
    @Override
    public void onError(int code, String desc) {
        //错误码code和错误描述desc，可用于定位请求失败原因
        //错误码code列表请参见错误码表
        Log.e(tag, "modifyGroupMemberInfoSetSilence failed: " + code + " desc" + desc);
    }

    @Override
    public void onSuccess() {
        Log.e(tag, "modifyGroupMemberInfoSetSilence succ");
    }
});
```

###  5.9 修改群名片

通过modifyGroupMemberInfoSetNameCard可以对群成员资料的群名片进行修改。 

**原型：**

```
public void modifyGroupMemberInfoSetNameCard(java.lang.String groupId,
                                             java.lang.String identifier,
                                             java.lang.String nameCard,
                                             TIMCallBack cb)
```
修改群成员信息-设置群名片 

**参数说明：**

参数|说明
---|---
groupId | 群组ID 
identifier | 要设置群名片的成员identifier 
nameCard | 要设置的群名片 
cb | 回调 

**示例：**

```
//修改群名片
TIMGroupManager.getInstance().modifyGroupMemberInfoSetNameCard(groupId,
        identifier, "wildcat", new TIMCallBack() {
            @Override
            public void onError(int code, String desc) {
                Log.e(tag, "set name card failed, code: " + code + "|descr: " + desc);
            }

            @Override
            public void onSuccess() {
                Log.e(tag, "set name card succ");
            }
        });
```


###  5.10 修改群成员维度自定义字段 

通过modifyGroupMemberInfoSetCustomInfo可以对群成员资料的自定义信息进行修改。 

**原型：**

```
public void modifyGroupMemberInfoSetCustomInfo(java.lang.String groupId,
                                               java.lang.String identifier,
                                               java.lang.String key,
                                               byte[] value,
                                               TIMCallBack cb)
```
修改群成员信息-设置自定义信息 

**参数说明：**
 
 参数|说明
 ---|---
groupId | 群组ID 
identifier | 要设置自定义属性的群成员的identifier 
key | 自定义属性的key 
value | 自定义属性的value 
cb | 回调 

**示例：**

```
//设置或者修改群成员的自定义属性”tag“的值为”wildcat“
TIMGroupManager.getInstance().modifyGroupMemberInfoSetCustomInfo(groupId,
    identifier, "tag", "wildcat".getBytes("utf-8"), new TIMCallBack() {
        @Override
        public void onError(int code, String desc) {
            Log.e(tag, "set custom failed, code: " + code + "|descr: " + desc);
        }

        @Override
        public void onSuccess() {
            Log.e(tag, "set custom succ");
        }
    });
```

###  5.11 修改群消息接收选项 

通过modifyReceiveMessageOpt可以修改所在群的群消息接收及提醒方式，对公开群和私有群，默认方式为接收并提醒，对于聊天室和互动直播聊天室，默认为接收不提醒。

**原型：**

```
public void modifyReceiveMessageOpt(java.lang.String groupId,
                                    TIMGroupReceiveMessageOpt opt,
                                    TIMCallBack cb)
```
修改群成员信息-设置是否接收群消息选项 

**参数说明：** 

参数|说明
---|---
groupId | 所在群的群Id 
opt | 接收群消息选项，详见 TIMGroupReceiveMessageOpt
cb | 回调 

**TIMGroupReceiveMessageOpt：**
```
//不接收群消息， 服务器不会进行转发
TIMGroupReceiveMessageOpt.NotReceive

//接收群消息，不提醒
TIMGroupReceiveMessageOpt.ReceiveNotNotify

//接收群消息并提醒
TIMGroupReceiveMessageOpt.ReceiveAndNotify
```

**示例：** 

```
//修改群接收消息选项为不接收群消息
TIMGroupManager.getInstance().modifyReceiveMessageOpt(groupId, TIMGroupReceiveMessageOpt.NotReceive, new TIMCallBack() {
    @Override
    public void onError(int code, String desc) {
        Log.d(tag, "modify receive option failed. code:" + code + "|desc:" + desc);
    }

    @Override
    public void onSuccess() {
        Log.d(tag, "modify receive option succ");
    }
});
```

## 6. 群组未决信息

群组未决信息泛指所有需要审批的群相关的操作。例如：加群待审批，拉人入群待审批等等。 群组未决信息由类TIMGroupPendencyItem表示。

TIMGroupPendencyItem的成员方法：
```
//同意申请，目前只对申请/邀请加群消息生效
void	accept(java.lang.String msg, TIMCallBack cb)

//获取群未决添加的时间
long	getAddTime()

//获取请求者identifier，请求加群:请求者，邀请加群:邀请人
java.lang.String	getFromUser()

//获取群组ID
java.lang.String	getGroupId()

//获取处理者添加的附加信息，只有处理状态不为TIMGroupPendencyHandledStatus.NOT_HANDLED的时候有效
java.lang.String	getHandledMsg()

//获取群未决处理状态：未决；他人已决；操作者已决 说明：UserA申请加入Group，AdminA审批通过。则AdminB拉取的此未决条目的类型为，他们已决。
TIMGroupPendencyHandledStatus	getHandledStatus()

//获取群未决处理操作类型：同意；拒绝。只有处理状态不为TIMGroupPendencyHandledStatus.NOT_HANDLED的时候有效
TIMGroupPendencyOperationType	getOperationType()

//获取群未决请求类型
TIMGroupPendencyGetType	getPendencyType()

//获取请求者添加的附加信息
java.lang.String	getRequestMsg()

//获取处理者identifier, 请求加群:0，邀请加群:被邀请人
java.lang.String	getToUser()

//拒绝申请，目前只对申请/邀请加群消息生效
void	refuse(java.lang.String msg, TIMCallBack cb)
```

###  6.1 拉取群未决列表 

通过getGroupPendencyList 接口可拉取群未决相关信息。即便审核通过或者拒绝后，该条信息也可通过此接口拉回，拉回的信息中有已决标志。  

**权限说明：**

**只有审批人有权限拉取相关信息。**
例如：UserA申请加入群GroupA，则群管理员可获取此未决相关信息，UserA因为没有审批权限，不需要过去未决信息。 
         如果AdminA拉UserA进去GroupA，则UserA可以拉取此未决相关信息，因为该未决信息待UserA审批。  
 
**原型：**

```
public void getGroupPendencyList(TIMGroupPendencyGetParam param,
                                 TIMValueCallBack<TIMGroupPendencyListGetSucc> cb)
```
分页获取群未决请求列表 。

**参数说明：**
 
 参数|说明
 ---|---
param | 获取群未决请求列表参数类，详见TIMGroupPendencyGetParam 
cb | 回调，在onSuccess的参数中返回群未决的列表及元数据，详见TIMGroupPendencyMeta 及TIMGroupPendencyItem
 
**TIMGroupPendencyGetParam:**
```
/**
 * 设置翻页时间戳，只用来翻页，第一次请求填0，后边根据server返回的{@see TIMGroupPendencyMeta}中的时间戳进行填写
 * @param timestamp 翻页时间戳
 */
public void setTimestamp(long timestamp)

/**
 * 设置每页的数量（建议值，server可根据需要返回或多或少，不能作为完成与否的标志）
 * @param numPerPage 每页的数量
 */
public void setNumPerPage(long numPerPage)
```
  
**示例：**

```
TIMGroupPendencyGetParam param = new TIMGroupPendencyGetParam();
param.setTimestamp(0);//首次获取填0
param.setNumPerPage(10);
TIMGroupManager.getInstance().getGroupPendencyList(param, new TIMValueCallBack<TIMGroupPendencyListGetSucc>() {
    @Override
    public void onError(int code, String desc) {

    }

    @Override
    public void onSuccess(TIMGroupPendencyListGetSucc timGroupPendencyListGetSucc) {
        //meta中的nextStartTimestamp如果不为0,可以先保存起来，
        // 作为获取下一页数据的参数设置到TIMGroupPendencyGetParam中
        TIMGroupPendencyMeta meta = timGroupPendencyListGetSucc.getPendencyMeta();
        Log.d(tag, meta.getNextStartTimestamp()
                + "|" + meta.getReportedTimestamp() + "|" + meta.getUnReadCount());

        List<TIMGroupPendencyItem> pendencyItems = timGroupPendencyListGetSucc.getPendencies();
        for(TIMGroupPendencyItem item : pendencyItems){
            //对群未决进行相应操作，比如查看/通过/拒绝等
        }
    }
});
```

###  6.2 上报群未决已读 

对于未决信息，通过reportGroupPendency可对其和之前的所有未决信息上报已读。上报已读后，仍然可以拉取到这些未决信息，但可通过对已读时戳的判断判定未决信息是否已读。
 
**原型：**

```
public void reportGroupPendency(long timestamp,
                                TIMCallBack cb)
```
群未决请求已读上报 

**参数说明：**

参数|说明
---|---
timestamp | 已读时间戳(单位秒)，此时间戳以前的群未决请求都将置为已读 
cb | 回调 

**示例：**
无 

###  6.3 处理群未决信息 

通过getGroupPendencyList获取一个群未决请求（TIMGroupPendencyItem）的列表，对于列表中的每一个元素，都可以通过TIMGroupPendencyItem类中的accept/refuse接口来对群未决进行审批。已处理成功过的未决信息不能再次处理。 
 
**TIMGroupPendencyItem**
```
//同意申请，目前只对申请/邀请加群消息生效
public void accept(java.lang.String msg,
                   TIMCallBack cb)

//拒绝申请，目前只对申请/邀请加群消息生效
public void refuse(java.lang.String msg,
                   TIMCallBack cb)
```

**参数说明：**
 
参数|说明
---|---
msg | 同意/拒绝理由，选填 
cb | 回调 

**示例：**
无 


## 7. 群资料存储

在1.9版本之前，并未存储用户的群资料数据，每次调用接口都是从服务端重新获取，需要APP端进行存储，1.9以后版本，增加了群资料存储，可以设置存储的具体字段，参考 [设置拉取字段](#4.1-.E8.AE.BE.E7.BD.AE.E6.8B.89.E5.8F.96.E5.AD.97.E6.AE.B5)。另外，这里仅存储群资料，并未对群成员的资料获取，1.9版本以后会在群消息中增加用户的相关字段，建议直接从消息中获取。

### 7.1 启用群资料存储

如果需要SDK进行群资料存储，可以在登录前，通过 TIMManager 中的 enableGroupInfoStorage 方法开启，**默认不进行群资料存储**。

**原型：**
```
public void enableGroupInfoStorage(boolean enable)
```
设置是否启用群信息本地存储，默认不启用（登录前调用）

**参数说明：**

参数|说明
---|---
enable | true - 启用群信息本地存储， false - 不启用群信息本地存储

### 7.2 群组资料获取同步接口

为了方便读取，1.9以后版本增加了群组资料的同步接口（需要开启群资料存储）。
同步接口均由 `TIMGroupAssistant` 提供。

**原型：**
```
public List<TIMGroupCacheInfo> getGroups(List<String> groupIds)
```
同步获取指定的群的群信息

**参数说明：**

参数|说明
---|---
groupIds | 指定要获取的群ID，如果为null，则获取全部的群信息

**返回说明：**

返回|说明
---|---
`List<TIMGroupCacheInfo>` | 群信息列表，如果出错返回null

**TIMGroupCacheInfo:**
```
/**
 * 获取群详细信息
 * @return 群详细信息
 */
public TIMGroupDetailInfo getGroupInfo()

/**
 * 获取个人在群内的简单信息
 * @return 个人在群内的简单信息
 */
public TIMGroupBasicSelfInfo getSelfInfo()
```

### 7.3 群通知回调

如果开启了存储，可以通过 TIMManager 中的 setGroupAssistantListener 方法设置监听感知群事件，当有对应事件发生时，会进行回调：

**原型：**

```
public void setGroupAssistantListener(TIMGroupAssistantListener listener)
```
设置群助手回调监听器

**参数说明：**

参数|说明
---|---
listener | 群助手回调监听器

**TIMGroupAssistantListener: **
```
/**
 * 有新用户加群时的通知回调
 * @param groupId 群ID
 * @param memberInfos 加群的用户的群内资料列表
 */
void onMemberJoin(String groupId, List<TIMGroupMemberInfo> memberInfos);

/**
 * 有群成员退群时的通知回调
 * @param groupId 群ID
 * @param members 退群的成员的identifier列表
 */
void onMemberQuit(String groupId, List<String> members) ;

/**
 * 群成员信息更新的通知回调
 * @param groupId 群ID
 * @param memberInfos 更新后的群成员群内资料列表
 */
void onMemberUpdate(String groupId, List<TIMGroupMemberInfo> memberInfos);

/**
 * 加入群的通知回调
 * @param groupCacheInfo 加入的群组的缓存群资料
 */
void onGroupAdd(TIMGroupCacheInfo groupCacheInfo);

/**
 * 解散群的通知回调
 * @param groupId 解散群的群ID
 */
void onGroupDelete(String groupId);

/**
 * 群缓存资料更新的通知回调
 * @param groupCacheInfo 更新后的群缓存资料信息
 */
void onGroupUpdate(TIMGroupCacheInfo groupCacheInfo);
```

## 8. 群事件消息

当有用户被邀请加入群组，或者有用户被移出群组时，群内会产生有提示消息，调用方可以根据需要展示给群组用户，或者忽略。提示消息使用一个特殊的Elem标识，通过新消息回调返回消息（参见[新消息通知](/doc/product/269/初始化（Android%20SDK）#2-.E6.96.B0.E6.B6.88.E6.81.AF.E9.80.9A.E7.9F.A5)）。另外，除了从**新消息通知**中获取群事件消息，还可以通过`TIMManager`中的`setGroupEventListener`接口设置群事件监听器来统一监听相应的事件。**2.4版本后，从群事件消息中可以拿到当前群成员数**。

>注：
聊天室（ChatRoom）和互动直播聊天室（AVChatRoom）类型的群组的群组事件消息不会通过**新消息通知**下发，只能通过注册群事件监听器对相应群事件进行监听。

如下图中，展示一条修改群名的事件消息：

![](//avc.qcloud.com/wiki2.0/im/imgs/20151014031645_92316.jpg)

TIMGroupTipsElem 成员方法：    

```
//获取群资料变更信息列表，仅当tipsType值为TIMGroupTipsType.ModifyGroupInfo时有效
java.util.List<TIMGroupTipsElemGroupInfo> getGroupInfoList()
 
//获取群组名称
java.lang.String    getGroupName()
 
//获取群成员变更信息列表，仅当tipsType值为TIMGroupTipsType.ModifyMemberInfo时有效
java.util.List<TIMGroupTipsElemMemberInfo>    getMemberInfoList()
 
//获取操作者
java.lang.String    getOpUser()
 
//获取群组事件通知类型
TIMGroupTipsType    getTipsType()
 
//获取被操作的帐号列表
java.util.List<java.lang.String>  getUserList()
```
 
TIMGroupTipsType 原型：
```
//取消管理员
CancelAdmin
 
//加入群组
Join
 
//被踢出群组
Kick
 
//修改群资料
ModifyGroupInfo
 
//修改成员信息
ModifyMemberInfo
 
//主动退出群组
Quit
 
//设置管理员
SetAdmin
```

### 8.1 用户加入群组通知

触发时机：当有用户加入群组时（包括申请入群和被邀请入群），群组内会由系统发出通知，开发者可选择展示样式。可以更新群成员列表。

收到的消息type为 `TIMGroupTipsType.Join`。

**TIMGroupTipsElem 成员方法返回说明：**

方法|返回说明
---|---
getType |	TIMGroupTipsType.Join
getOpUser |	申请入群：申请人/邀请入群：邀请人
getGroupName |	群名
getUserList | 入群的用户列表

### 8.2 用户退出群组

触发时机：当有用户主动退群时，群组内会由系统发出通知。可以选择更新群成员列表。

收到的消息type为 `TIMGroupTipsType.Quit`。

**TIMGroupTipsElem 成员方法返回说明：**

方法|返回说明
---|---
getType|	TIMGroupTipsType.Quit
getOpUser |	退出用户identifier
getGroupName |	群名

### 8.3 用户被踢出群组

触发时机：当有用户被踢出群组时，群组内会由系统发出通知。可以更新群成员列表。

收到的消息type为 `TIMGroupTipsType.Kick`。

**TIMGroupTipsElem 成员方法返回说明：**

方法|返回说明
---|---
getType|	TIMGroupTipsType.Kick
getOpUser |	踢人的identifier
getGroupName |	群名
getUserList | 被踢用户列表

### 8.4 被设置/取消管理员

触发时机：当有用户被设置为管理员或者被取消管理员身份时，群组内会由系统发出通知。如果界面有显示是否管理员，此时可更新管理员标识。

收到的消息type为`TIMGroupTipsType.SetAdmin` 和 `TIMGroupTipsType.CancelAdmin`。

**TIMGroupTipsElem 成员方法返回说明：**

方法|返回说明
---|---
getType|	设置：TIMGroupTipsType.SetAdmin<br>取消：TIMGroupTipsType.CancelAdmin
getOpUser |	操作用户identifier
getGroupName |	群名
getUserList | 被设置/取消管理员身份的用户列表

### 8.5 群资料变更

触发时机：当群资料变更，如群名、群简介等，会有系统消息发出，可更新相关展示字段。或者选择性把消息展示给用户。

**TIMGroupTipsElem 成员方法返回说明：**

方法|返回说明
---|---
getType|	TIMGroupTipsType.ModifyGroupInfo
getOpUser |	操作用户identifier
getGroupName |	群名
getGroupInfoList|	群变更的具体资料信息，为TIMGroupTipsElemGroupInfo 结构体列表

TIMGroupTipsElemGroupInfo 原型：

```
//获取消息内容
java.lang.String    getContent()
 
//获取群资料变更消息类型
TIMGroupTipsGroupInfoType   getType()
```
 
TIMGroupTipsGroupInfoType 原型：
```
//修改群头像URL
ModifyFaceUrl
 
//修改群简介
ModifyIntroduction
 
//修改群名称
ModifyName
 
//修改群公告
ModifyNotification
 
//修改群主
ModifyOwner
```

### 8.6 群成员资料变更

触发时机：当群成员的群相关资料变更时，包括群内用户被禁言、群内成员角色变更，会有系统消息发出，可更新相关字段展示，或者选择性把消息展示给用户。（**注意：这里的资料仅跟群相关资料，比如禁言时间、成员角色变更等，不包括用户昵称等本身资料，对于群内人数可能过多，不建议实时更新，建议的做法是直接显示消息体内的资料，参考：[消息发送者以及相关资料](/doc/product/269/消息收发（Android%20SDK）#3.4-.E6.B6.88.E6.81.AF.E5.8F.91.E9.80.81.E8.80.85.E5.8F.8A.E5.85.B6.E7.9B.B8.E5.85.B3.E8.B5.84.E6.96.99)，如果本地有保存用户资料，可根据消息体内资料判断是否有变更，在收到此用户一条消息后更新资料。**）。

**TIMGroupTipsElem  成员方法返回说明：**

方法|返回说明
---|---
getType|	TIMGroupTipsType.ModifyMemberInfo
getOpUser |	操作用户identifier
getGroupName |	群名
getMemberInfoList|	变更的群成员的具体资料信息，为TIMGroupTipsElemMemberInfo结构体列表

**TIMGroupTipsElemMemberInfo 原型：**
```
//获取被禁言群成员的identifier
java.lang.String    getIdentifier()
 
//获取被禁言时间
long    getShutupTime()
```

## 9. 群系统消息

当有用户申请加群等事件发生时，管理员会收到邀请加群系统消息，用户可根据情况接受请求或者拒绝，相应的消息通过群系统消息展示给用户。

**群系统消息类型定义：**

```
//申请加群被同意（只有申请人能够收到）
TIM_GROUP_SYSTEM_ADD_GROUP_ACCEPT_TYPE

//申请加群被拒绝（只有申请人能够收到）
TIM_GROUP_SYSTEM_ADD_GROUP_REFUSE_TYPE

//申请加群请求（只有管理员会收到）
TIM_GROUP_SYSTEM_ADD_GROUP_REQUEST_TYPE

//取消管理员(被取消者接收)
TIM_GROUP_SYSTEM_CANCEL_ADMIN_TYPE

//创建群消息（初始成员能够收到）
TIM_GROUP_SYSTEM_CREATE_GROUP_TYPE

//群被解散（全员能够收到）
TIM_GROUP_SYSTEM_DELETE_GROUP_TYPE

//设置管理员(被设置者接收)
TIM_GROUP_SYSTEM_GRANT_ADMIN_TYPE

//邀请加群（被邀请者能够收到）
TIM_GROUP_SYSTEM_INVITED_TO_GROUP_TYPE

//被管理员踢出群（只有被踢的人能够收到）
TIM_GROUP_SYSTEM_KICK_OFF_FROM_GROUP_TYPE

//主动退群（主动退群者能够收到）
TIM_GROUP_SYSTEM_QUIT_GROUP_TYP

//群已被回收(全员接收)
TIM_GROUP_SYSTEM_REVOKE_GROUP_TYPE

//邀请入群请求（被邀请者接收）
TIM_GROUP_SYSTEM_INVITE_TO_GROUP_REQUEST_TYPE

//邀请加群被同意(只有发出邀请者会接收到)
TIM_GROUP_SYSTEM_INVITATION_ACCEPTED_TYPE

//邀请加群被拒绝(只有发出邀请者会接收到)
TIM_GROUP_SYSTEM_INVITATION_REFUSED_TYPE
```

**TIMGroupSystemElem 成员方法：**
```
//同意申请，目前只对申请加群消息生效
void    accept(java.lang.String msg, TIMCallBack cb)

//获取消息群Id
java.lang.String    getGroupId()

//获取操作理由
java.lang.String    getOpReason()

//获取操作人
java.lang.String    getOpUser()

//获取消息子类型
TIMGroupSystemElemType  getSubtype()

//拒绝申请，目前只对申请加群消息生效
void    refuse(java.lang.String msg, TIMCallBack cb)
```

### 9.1 申请加群消息

触发时机：当有用户申请加群时，群管理员会收到申请加群消息，可展示给用户，由用户决定是否同意对方加群，如果同意，调用accept方法，拒绝调用refuse方法。

消息类型为：`TIM_GROUP_SYSTEM_ADD_GROUP_REQUEST_TYPE`。

**TIMGroupSystemElem 成员方法返回说明：**

方法|返回说明
---|---
getSubtype	| TIM_GROUP_SYSTEM_ADD_GROUP_REQUEST_TYPE
getGroupId	| 群组Id，表示是哪个群的申请
getOpUser	| 申请人
getOpReason	| 申请理由（可选）

**方法说明：**

当同意申请人入群，可调用accept方法
当不同意申请人入群，可调用refuse方法。


### 9.2 申请加群同意/拒绝消息

触发时机：当管理员同意加群请求时，申请人会收到同意入群的消息，当管理员拒绝时，收到拒绝入群的消息。

**TIMGroupSystemElem 成员方法返回说明：**

方法|返回说明
---|---
getSubtype	| 同意：TIM_GROUP_SYSTEM_ADD_GROUP_ACCEPT_TYPE<br>拒绝：TIM_GROUP_SYSTEM_ADD_GROUP_REFUSE_TYPE
getGroupId	| 群组Id，表示是哪个群通过/拒绝了
getOpUser	| 处理请求的管理员identifier
getOpReason	| 同意或者拒绝理由（可选）

### 9.3 邀请入群请求消息

触发时机：当用户被邀请加入群组（**此时用户还没有加入到群组，需要用户审批**）时，该用户会收到邀请消息，注意：创建群组时初始成员无需邀请即可入群。

**TIMGroupSystemElem 成员方法返回说明：**

方法|返回说明
---|---
getSubtype	| TIM_GROUP_SYSTEM_INVITE_TO_GROUP_REQUEST_TYPE
getGroupId	| 群组Id，邀请进入哪个群
getOpUser	| 操作人，表示哪个用户的邀请

方法说明：

当用户同意入群，可调用accept方法
当用户不同意，可调用refuse方法。


### 9.4 邀请入群同意/拒绝消息 

触发时机：当被邀请者同意入群请求时，邀请者会收到同意入群的消息；当被邀请者拒绝时，邀请者收到拒绝入群的消息。 

**TIMGroupSystemElem 成员方法返回说明：**

方法|返回说明
---|---
getSubtype	| 同意：TIM_GROUP_SYSTEM_INVITATION_ACCEPTED_TYPE<br>拒绝：TIM_GROUP_SYSTEM_INVITATION_REFUSED_TYPE
getGroupId	| 群组Id，表示是哪个群通过/拒绝了
getOpUser	| 处理请求的管理员identifier
getOpReason	| 同意或者拒绝理由（可选）


### 9.5 被管理员踢出群组

触发时机：当用户被管理员踢出群组时，申请人会收到被踢出群的消息。

**TIMGroupSystemElem 成员方法返回说明：**

方法|返回说明
---|---
getSubtype	| TIM_GROUP_SYSTEM_KICK_OFF_FROM_GROUP_TYPE
getGroupId	| 群组Id，表示在哪个群里被踢了
getOpUser	| 操作管理员identifier


### 9.6 群被解散

触发时机：当群被解散时，全员会收到解散群消息。

**TIMGroupSystemElem 成员方法返回说明：**

方法|返回说明
---|---
getSubtype	| TIM_GROUP_SYSTEM_DELETE_GROUP_TYPE
getGroupId	| 群组Id，表示哪个群被解散了
getOpUser	| 操作管理员identifier

### 9.7 创建群消息

触发时机：当群创建时，创建者会收到创建群消息。

当调用创建群方法成功回调后，即表示创建成功，此消息主要为多终端同步，如果有在其他终端登录，做为更新群列表的时机，本终端可以选择忽略。

**TIMGroupSystemElem 成员方法返回说明：**

方法|返回说明
---|---
getSubtype	| TIM_GROUP_SYSTEM_CREATE_GROUP_TYPE
getGroupId	| 群组Id，表示创建的群Id
getOpUser	| 创建者，这里也就是用户自己


### 9.8 邀请入群消息

触发时机：当用户被邀请加入到群组（**此时用户已经加入到群组**）时，该用户会收到邀请消息，注意：创建群组时初始成员无需邀请即可入群。

**TIMGroupSystemElem 成员方法返回说明：**

方法|返回说明
---|---
getSubtype	| TIM_GROUP_SYSTEM_INVITED_TO_GROUP_TYPE
getGroupId	| 群组Id，邀请进入哪个群
getOpUser	| 操作人，表示哪个用户的邀请

### 9.9 主动退群

触发时机：当用户主动退出群组时，该用户会收到退群消息，只有退群的用户自己可以收到。

当用户调用QuitGroup时成功回调返回，表示已退出成功，此消息主要为了多终端同步，其他终端可以做为更新群列表的时机，本终端可以选择忽略。

**TIMGroupSystemElem 成员方法返回说明：**

方法|返回说明
---|---
getSubtype	| TIM_GROUP_SYSTEM_QUIT_GROUP_TYPE
getGroupId	| 群组Id，表示退出的哪个群
getOpUser	| 操作人，这里即为用户自己

### 9.10 设置/取消管理员

触发时机：当用户被设置为管理员时，可收到被设置管理员的消息通知，当用户被取消管理员时，可收到取消通知，可提示用户。

**TIMGroupSystemElem 成员方法返回说明：**

方法|返回说明
---|---
getSubtype	|	取消管理员身份:TIM_GROUP_SYSTEM_GRANT_ADMIN_TYPE<br>授予管理员身份：TIM_GROUP_SYSTEM_CANCEL_ADMIN_TYPE
getGroupId	| 群组Id，表示哪个群的事件
getOpUser	| 操作人

### 9.11 群被回收

触发时机：当群组被系统回收时，全员可收到群组被回收消息。

**TIMGroupSystemElem 成员方法返回说明：**

方法|返回说明
---|---
getSubtype	|	TIM_GROUP_SYSTEM_REVOKE_GROUP_TYPE
getGroupId	| 群组Id，表示哪个群被回收了

## 10. 搜索群

通过SearchGroup成员方法可以检索群列表，目前只支持群名匹配关键字，可自定义获取的群资料字段。

**原型：**

```
public void searchGroup(java.lang.String groupName,
                       long flags,
                       java.util.List<java.lang.String> custom,
                       int pageIndex,
                       int pageSize,
                       TIMValueCallBack<TIMGroupSearchSucc> cb)
```
根据群组名称信息搜索群组资料（可以指定字段拉取）

**参数说明：**

参数|说明
---|---
groupName | 群组名称关键字
flags | 拉取资料标志, 如TIMGroupManager.TIM_GET_GROUP_BASE_INFO_FLAG_NAME
custom | 要获取的自定义key
pageIndex | 分页号
pageSize | 每个分页的群组数目
cb | 回调，在onSuccess回调参数中返回搜索结果，详见TIMGroupSearchSucc

**示例：**

```
long flag =0;
flag |= TIMGroupManager.TIM_GET_GROUP_BASE_INFO_FLAG_GROUP_TYPE;
flag |= TIMGroupManager.TIM_GET_GROUP_BASE_INFO_FLAG_OWNER_UIN;
flag |= TIMGroupManager.TIM_GET_GROUP_BASE_INFO_FLAG_INTRODUCTION;
flag |= TIMGroupManager.TIM_GET_GROUP_BASE_INFO_FLAG_APP_ID;
TIMGroupManager.getInstance().searchGroup("test", flag, null, 0, 10, new TIMValueCallBack<TIMGroupSearchSucc>(){
 
    @Override
    public void onError(int arg0, String arg1) {
        // TODO Auto-generated method stub
        Log.d(tag,"searchGroup failed, error:"+ arg0 +":" + arg1);
    }
 
    @Override
    public void onSuccess(TIMGroupSearchSucc arg0) {
        // TODO Auto-generated method stub
        Log.d(tag,"searchGroup succ:"+ arg0.getInfoList().size());
        //  mListGroup.clear();
        List<TIMGroupDetailInfo>  infos = arg0.getInfoList();
        for(TIMGroupDetailInfo info:infos){
            Log.d(tag, "type:" + info.getGroupType()
                    + " |owner: " + info.getGroupOwner()
                    + "|groupname: " + info.getGroupName()
                    + "|introduction: " + info.getGroupIntroduction()
            );
        }
    }
 
});

```