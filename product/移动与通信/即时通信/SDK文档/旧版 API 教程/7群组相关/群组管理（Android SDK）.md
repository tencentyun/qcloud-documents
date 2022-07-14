## 群组综述

即时通信 IM 有多种群组类型，其特点以及限制因素请参见 [群组系统](https://cloud.tencent.com/document/product/269/1502)。群组使用唯一 ID 标识，通过群组 ID 可以进行不同操作。

## 群组消息

群组消息与 C2C 消息相同，仅在获取 Conversation 时的会话类型不同，请参见 [消息发送](https://cloud.tencent.com/document/product/269/9232#.E6.B6.88.E6.81.AF.E5.8F.91.E9.80.81)。

## 群组管理

群组相关操作都由 `TIMGroupManager` 实现，需要用户登录成功后操作。

**获取单例原型：**

```
/** 获取实例
 * @return TIMGroupManager 实例
 */
public static TIMGroupManager getInstance()

```

### 创建群组

即时通信 IM 中内置了**私有群（Private）、公开群（Public）、 聊天室（ChatRoom）、音视频聊天室（AVChatRoom）和在线成员广播大群（BChatRoom）**这几种群组类型，详情请参见 [群组类型介绍](https://cloud.tencent.com/document/product/269/1502#GroupType)。

- **音视频聊天室（AVChatRoom）：**也叫直播大群，此类型群对于加入人数不做限制，但是有一些能力上的限制，如不能拉人进去，不能查询总人数等。
- 可通过 `TIMGroupManager` 中的接口 `createGroup` 接口创建群组，创建时可指定一些群资料（例如群组类型、群组名称、群简介、加入的用户列表等，甚至可以指定群 ID），创建成功后返回群组 ID，可通过群组 ID 获取 Conversation 收发消息等。

>!自定义群组 ID 的时候，需要遵循一定的规则，具体请参考 [自定义群组 ID](https://cloud.tencent.com/document/product/269/1502#.E8.87.AA.E5.AE.9A.E4.B9.89.E7.BE.A4.E7.BB.84-id)。

**原型：**

```
/**
 * 创建群组
 * @param param 创建群组需要的信息集, 详见{@see CreateGroupParam}
 * @param cb 回调，OnSuccess 函数的参数中将返回创建成功的群组 ID
 */
public void createGroup(@NonNull CreateGroupParam param, @NonNull TIMValueCallBack<String> cb)
```

**`TIMGroupManager.CreateGroupParam` 提供的接口如下：**
```
/**
 * 创建群组参数类的构造函数
 * @param type 群类型, 目前支持的群类型：私有群（Private）、公开群（Public）、
 *             聊天室（ChatRoom）、音视频聊天室（AVChatRoom）和在线成员广播大群（BChatRoom）
 * @param name 群名称
 */
public CreateGroupParam(@NonNull String type, @NonNull String name)

/**
 * 设置要创建的群的群 ID
 * @param groupId 群 ID
 */
public CreateGroupParam setGroupId(String groupId)

/**
 * 设置要创建的群的群公告
 * @param notification 群公告
 */
public CreateGroupParam setNotification(String notification)

/**
 * 设置要创建的群的群简介
 * @param introduction 群简介
 */
public CreateGroupParam setIntroduction(String introduction)

/**
 * 设置要创建的群的群头像 URL
 * @param url 群头像 URL
 */
public CreateGroupParam setFaceUrl(String url)

/**
 * 设置要创建的群的加群选项
 * @param option 加群选项
 */
public CreateGroupParam setAddOption(TIMGroupAddOpt option)

/**
 * 设置要创建的群允许的最大成员数
 * @param maxMemberNum 最大成员数
 */
public CreateGroupParam setMaxMemberNum(long maxMemberNum)

/**
 * 设置要创建的群的自定义信息
 * @param key 自定义信息 key, 最长 16 字节
 * @param value 自定义信息 value，最长 512 字节
 */
public CreateGroupParam setCustomInfo(String key, byte[] value)

/**
 * 设置要创建的群的初始成员
 * @param infos 初始成员的信息列表
 */
public CreateGroupParam setMembers(List<TIMGroupMemberInfo> infos)
```

**示例：**
```
//创建公开群，且不自定义群 ID
TIMGroupManager.CreateGroupParam param = new TIMGroupManager.CreateGroupParam("Public", "test_group");
//指定群简介
param.setIntroduction("hello world");
//指定群公告
param.setNotification("welcome to our group");

//添加群成员
List<TIMGroupMemberInfo> infos = new ArrayList<TIMGroupMemberInfo>();
TIMGroupMemberInfo member = new TIMGroupMemberInfo("cat");
infos.add(member);
param.setMembers(infos);

//设置群自定义字段，需要先到控制台配置相应的 key
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

### 邀请用户入群

`TIMGroupManager` 的接口 `inviteGroupMember` 可以拉（邀请）用户进入群组。

**权限说明：**

详情请参见 [加群方式差异](https://cloud.tencent.com/document/product/269/1502#.E5.8A.A0.E7.BE.A4.E6.96.B9.E5.BC.8F.E5.B7.AE.E5.BC.82)。 

**原型：**

```
/**
 * 邀请加入群组
 * @param groupId 群组 ID
 * @param memList 待加入群组的用户 ID 列表
 * @param cb 回调，OnSuccess 函数的参数中返回成功加入群组的用户帐号
 */
public void inviteGroupMember(@NonNull String groupId, @NonNull List<String> memList,
							  @NonNull TIMValueCallBack<List<TIMGroupMemberResult>> cb)
```

**`TIMGroupMemberResult`接口定义如下：**

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
ArrayList list = new ArrayList();

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

//将 list 中的用户加入群组
TIMGroupManager.getInstance().inviteGroupMember(
        groupId,   //群组 ID
        list,      //待加入群组的用户列表
        cb);       //回调
```

### 申请加入群组

`TIMGroupManager` 的接口 `applyJoinGroup` 可以主动申请进入群组，此操作只对公开群、聊天室和音视频聊天室有效。

**权限说明：**

详情请参见 [加群方式差异](https://cloud.tencent.com/document/product/269/1502#.E5.8A.A0.E7.BE.A4.E6.96.B9.E5.BC.8F.E5.B7.AE.E5.BC.82)。

**原型：**

```
/**
 * 加入群组
 * @param groupId 群组 ID
 * @param reason 申请理由（选填）
 * @param cb 回调
 */
public void applyJoinGroup(@NonNull String groupId, String reason, @NonNull TIMCallBack cb)
```

以下示例中用户申请加入群组『@TGS#1JYSZEAEQ』，申请理由为『some reason』。**示例：**

```
TIMGroupManager.getInstance().applyJoinGroup("@TGS#1JYSZEAEQ", "some reason", new TIMCallBack() {
    @java.lang.Override
    public void onError(int code, String desc) {
        //接口返回了错误码 code 和错误描述 desc，可用于原因
        //错误码 code 列表请参见错误码表
        Log.e(tag, "applyJoinGroup err code = " + code + ", desc = " + desc);
    }

    @java.lang.Override
    public void onSuccess() {
        Log.i(tag, "applyJoinGroup success");
    }
});
```

### 退出群组

群组成员可以主动退出群组。退出群组的接口由 `TIMGroupManager` 提供。

**权限说明：**

- **私有群：**全员可退出群组。
- **公开群、聊天室和直播大群：**群主不能退出。

详情请参见 [成员管理能力差异](https://cloud.tencent.com/document/product/269/1502#.E6.88.90.E5.91.98.E7.AE.A1.E7.90.86.E8.83.BD.E5.8A.9B.E5.B7.AE.E5.BC.82)。

**原型：**

```
/**
 * 退出群组
 * @param groupId 群组 ID
 * @param cb 回调
 */
public void quitGroup(@NonNull String groupId, @NonNull TIMCallBack cb)
```

**示例：**

```
//创建回调
TIMCallBack cb = new TIMCallBack() {
    @Override
    public void onError(int code, String desc) {
            //错误码 code 和错误描述 desc，可用于定位请求失败原因
            //错误码 code 含义请参见错误码表
    }

    @Override
    public void onSuccess() {
        Log.e(tag, "quit group succ");
    }
};

//退出群组
TIMGroupManager.getInstance().quitGroup(
        groupId,  //群组 ID
        cb);      //回调
```

### 删除群组成员

函数参数信息与加入群组相同，删除群组成员的接口由 `TIMGroupManager` 提供。

**权限说明：**
详情请参见 [成员管理能力差异](https://cloud.tencent.com/document/product/269/1502#.E6.88.90.E5.91.98.E7.AE.A1.E7.90.86.E8.83.BD.E5.8A.9B.E5.B7.AE.E5.BC.82)。

**原型：**

```
/**
 * 删除群组成员
 * @param param 删除群成员参数
 * @param cb 回调，OnSuccess 函数的参数中返回成功删除的群成员列表
 */
public void deleteGroupMember(@NonNull DeleteMemberParam param,
							  @NonNull TIMValueCallBack<List<TIMGroupMemberResult>> cb)
```

**`DeleteMemberParam` 接口定义如下：**
```
/**
 * 构造参数
 * @param groupId 群 ID
 * @param members 用户 ID 列表
 */
public DeleteMemberParam(@NonNull String groupId, @NonNull List<String> members)

/**
 * 设置删除群成员的原因（选填）
 * @param reason 删除原因
 */
public DeleteMemberParam setReason(@NonNull String reason)
```

**示例：**

```
//创建待踢出群组的用户列表
ArrayList list = new ArrayList();

String user = "";
//添加用户
user = "sample_user_1";
list.add(user);
user = "sample_user_2";
list.add(user);
user = "sample_user_3";
list.add(user);

TIMGroupManager.DeleteMemberParam param = new TIMGroupManager.DeleteMemberParam(groupId, list);
param.setReason("some reason");

TIMGroupManager.getInstance().deleteGroupMember(param, new TIMValueCallBack<List<TIMGroupMemberResult>>() {
	@Override
	public void onError(int code, String desc) {
		Log.e(tag, "deleteGroupMember onErr. code: " + code + " errmsg: " + desc);
	}

	@Override
	public void onSuccess(List<TIMGroupMemberResult> results) { //群组成员操作结果
		for(TIMGroupMemberResult r : results) {
			Log.d(tag, "result: " + r.getResult()  //操作结果:  0：删除失败；1：删除成功；2：不是群组成员
					+ " user: " + r.getUser());    //用户帐号
		}
	}
});
```

### 获取群成员列表

获取群成员列表的接口为`getGroupMembers`，默认拉取内置字段以及自定义字段，自定义字段要通过 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) >【功能配置】> 【群成员维度自定义字段】配置相关的 key 和权限，5分钟后生效。

**权限说明：**

- **任何群组类型：**可以获取成员列表。
- **直播大群：**只能拉取部分成员列表，包括群主、管理员和部分成员。

详情请参见 [群组基础能力操作差异](https://cloud.tencent.com/document/product/269/1502#.E7.BE.A4.E7.BB.84.E5.9F.BA.E7.A1.80.E8.83.BD.E5.8A.9B.E6.93.8D.E4.BD.9C.E5.B7.AE.E5.BC.82)。 

**原型：**

```
/**
 * 获取群组成员列表
 * @param groupId 群组 ID
 * @param cb 回调，OnSuccess 函数的参数中返回群组成员列表
 */
public void getGroupMembers(@NonNull String groupId, @NonNull TIMValueCallBack<List<TIMGroupMemberInfo>> cb)
```

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
        groupId, //群组 ID
        cb);     //回调
```

### 获取加入的群组列表

获取当前用户加入的所有群组的接口由 `TIMGroupManager` 提供。此接口可以获取自己所加入的群列表，返回的信息只包含部分基本信息，详细群组信息可以根据 [群成员获取群组资料](https://cloud.tencent.com/document/product/269/9236#.E8.8E.B7.E5.8F.96.E7.BE.A4.E7.BB.84.E8.B5.84.E6.96.992) 进行获取。

**权限说明：**

- **私有群、公开群和聊天室：**支持使用本接口获取用户加入的公开群、聊天室、已激活的私有群信息。
- **音视频聊天室和在线成员广播大群：**因为内部实现的差异，获取用户加入的群组时不会获取到这两种类型的群组。

**原型：**

```
/**
 * 获取已加入的群组列表
 * @param cb 回调，OnSuccess 函数的参数中返回已加入的群组信息
 */
public void getGroupList(@NonNull TIMValueCallBack<List<TIMGroupBaseInfo>> cb)
```

**`TIMGroupBaseInfo` 提供的方法如下：**
```
/**
 * 获取群组 ID
 * @return 群组 ID
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
 * 获取群头像 URL
 * @return 群头像 URL
 */
public String getFaceUrl()

/**
 * 获取当前群组是否设置了全员禁言
 * @return true - 设置了全员禁言
 * @since 3.1.1
 */
public boolean isSilenceAll()
```

**示例：**

```
//创建回调
TIMValueCallBack<List<TIMGroupBaseInfo>> cb = new TIMValueCallBack<List<TIMGroupBaseInfo>>() {
    @Override
    public void onError(int code, String desc) {
        //错误码 code 和错误描述 desc，可用于定位请求失败原因
        //错误码 code 含义请参见错误码表
        Log.e(tag, "get group list failed: " + code + " desc");
    }

    @Override
    public void onSuccess(List<TIMGroupBaseInfo> timGroupInfos) {//参数返回各群组基本信息
        Log.d(tag, "get group list succ");

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

### 解散群组

 解散群组的接口由`TIMGroupManager`提供。

**权限说明：**
详情请参见 [群组基础能力操作差异](https://cloud.tencent.com/document/product/269/1502#.E7.BE.A4.E7.BB.84.E5.9F.BA.E7.A1.80.E8.83.BD.E5.8A.9B.E6.93.8D.E4.BD.9C.E5.B7.AE.E5.BC.82)。 

**原型：**

```
/**
 * 删除群组
 * @param groupId 群组 ID
 * @param cb 回调
 */
public void deleteGroup(@NonNull String groupId, @NonNull TIMCallBack cb)
```

**示例：**

```
//解散群组
TIMGroupManager.getInstance().deleteGroup(groupId, new TIMCallBack() {
    @Override
    public void onError(int code, String desc) {

        //错误码 code 和错误描述 desc，可用于定位请求失败原因
        //错误码 code 列表请参见错误码表
        Log.d(tag, "login failed. code: " + code + " errmsg: " + desc);
    }

    @Override
    public void onSuccess() {
        //解散群组成功
    }
});
```

### 转让群组

转让群组的接口由`TIMGroupManager`提供。

**权限说明：**

只有**群主**可以进行群转让操作。

**原型：**

```
/**
 * 群主变更
 * @param groupId 群组 ID
 * @param identifier 新群主的 identifier
 * @param cb 回调
 */
public void modifyGroupOwner(@NonNull String groupId, @NonNull String identifier, @NonNull TIMCallBack cb)
```

### 其他接口

**获取指定类型成员（可按照管理员、群主、普通成员拉取）接口定义如下：**

```
/**
 * 根据过滤条件获取群成员列表(支持按字段拉取，分页)
 * @param groupId 群组 ID
 * @param flags 拉取资料标志， 如{@see TIMGroupManager#TIM_GET_GROUP_MEM_INFO_FLAG_NAME_CARD}等标志的或组合位图
 * @param filter 角色过滤类型，详见{@see TIMGroupMemberRoleFilter}
 * @param custom 要获取的自定义 key 列表
 * @param nextSeq 分页拉取标志，第一次拉取填0，回调成功如果不为零，需要分页，传入再次拉取，直至为0
 * @param cb 回调
 */
public void getGroupMembersByFilter(@NonNull String groupId, long flags, @NonNull TIMGroupMemberRoleFilter filter,
									List<String> custom, long nextSeq, TIMValueCallBack<TIMGroupMemberSucc> cb)
```

## 获取群组资料

### 获取群组资料

`TIMGroupManager`提供的`getGroupInfo`方法可以获取服务器存储的群组资料，`queryGroupInfo`方法可以获取本地缓存的群组资料。群成员可以拉取到群组信息。非群成员无权限拉取私有群的信息，其他群类型仅可以拉取公开字段，`groupId\groupName\groupOwner\groupType\createTime\memberNum\maxMemberNum\onlineMemberNum\groupIntroduction\groupFaceUrl\addOption\custom` 。

**说明：**

默认拉取基本资料以及自定义字段，自定义字段要通过 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) >【功能配置】> 【群维度自定义字段】配置相关的 key 和权限，5分钟后生效。

**原型：**

```
/**
 * 获取服务器存储的群组信息
 * @param groupIdList 需要拉取详细信息的群组 ID 列表，一次最多 50 个
 * @param cb 回调，OnSuccess 函数的参数中返回群组信息{@see TIMGroupDetailInfo}列表
 */
public void getGroupInfo(@NonNull List<String> groupIdList,
							   @NonNull TIMValueCallBack<List<TIMGroupDetailInfo>> cb)
/**
 * 获取本地存储的群组信息
 * @param groupId 需要拉取详细信息的群组 ID
 * @return 群组信息，本地没有返回 null
 */
 public TIMGroupDetailInfo queryGroupInfo(@NonNull String groupId)
```

**`TIMGroupDetailInfo` 的接口定义如下：**
```
/**
 * 获取群组 ID
 * @return 群组 ID
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
 * 获取群头像 URL
 * @return 群头像 URL
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
 * 获取群组自定义字段 map
 * @return 群组自定义字段 map
 */
public Map<String, byte[]> getCustom()

/**
 * 获取此群组是否被设置了全员禁言
 * @return true - 群组被设置了全员禁言
 * @since 3.1.1
 */
public boolean isSilenceAll()
```

**示例：**

```
//创建待获取信息的群组 ID 列表
ArrayList<String> groupList = new ArrayList<String>();

//创建回调
TIMValueCallBack<List<TIMGroupDetailInfo>> cb = new TIMValueCallBack<List<TIMGroupDetailInfo>>() {
    @Override
    public void onError(int code, String desc) {
            //错误码 code 和错误描述 desc，可用于定位请求失败原因
            //错误码 code 列表请参见错误码表
    }

    @Override
    public void onSuccess(List<TIMGroupDetailInfo> infoList) { //参数中返回群组信息列表
        for(TIMGroupDetailInfo info : infoList) {
            Log.d(tag, "groupId: " + info.getGroupId()           //群组 ID
            + " group name: " + info.getGroupName()              //群组名称
            + " group owner: " + info.getGroupOwner()            //群组创建者帐号
            + " group create time: " + info.getCreateTime()      //群组创建时间
            + " group last info time: " + info.getLastInfoTime() //群组信息最后修改时间
            + " group last msg time: " + info.getLastMsgTime()  //最新群组消息时间
            + " group member num: " + info.getMemberNum());      //群组成员数量
        }
    }
};

//添加群组 ID
String groupId = "TGID1EDABEAEO";
groupList.add(groupId);

//获取服务器群组信息
TIMGroupManager.getInstance().getGroupInfo(
        groupList, //需要获取信息的群组 ID 列表
        cb);       //回调

//获取本地缓存的群组信息
TIMGroupDetailInfo timGroupDetailInfo = TIMGroupManager.getInstance().queryGroupInfo(groupId);
```

### 获取本人在群里的资料

如果需要获取本人在所在群内的资料，可以在通过 [获取群组列表](#.E8.8E.B7.E5.8F.96.E5.8A.A0.E5.85.A5.E7.9A.84.E7.BE.A4.E7.BB.84.E5.88.97.E8.A1.A8)  拉取加入的群列表时得到。另外，如果需要单独获取某个群组，可使用以下 `TIMGroupManager` 提供的 `getSelfInfo` 获取。如果应用需要获取群组列表，建议在获取群组列表的时候获取个人在所在群内的资料，没有必要调用以下接口单独获取。

**权限说明：**

**直播大群：**无法获取本人在群内的资料。

**原型：**

```
/**
 * 获取自己在群组中的信息
 * @param groupId 群组 ID
 * @param cb 回调， 在 OnSuccess 函数的参数中返回自身信息
 */
public void getSelfInfo(@NonNull String groupId, @NonNull TIMValueCallBack<TIMGroupSelfInfo> cb)
```

### 获取群内某个人的资料

获取群成员资料的接口由 `TIMGroupManager` 提供，默认拉取基本资料。

**权限说明：**

**直播大群**只能获得部分成员的资料，包括群主、管理员和部分群成员。

**原型：**
```
/**
 * 获取指定的群成员的群内信息
 * @param groupId 指定群 ID
 * @param identifiers 指定群成员 identifier，一次最多 100 个
 * @param cb 回调，OnSuccess函数的参数中返回群组成员列表
 */
public void getGroupMembersInfo(@NonNull String groupId, @NonNull List<String> identifiers,
								@NonNull TIMValueCallBack<List<TIMGroupMemberInfo>> cb)
```


## 修改群资料

修改群资料的接口由 `TIMGroupManager` 提供，可以对群名称、群简介、群公告等资料进行修改。

**原型：**

```
/**
 * 修改群组基本信息
 * @param param 参数类
 * @param cb 回调
 */
public void modifyGroupInfo(@NonNull ModifyGroupInfoParam param, @NonNull TIMCallBack cb)
```

**`TIMGroupManager.ModifyGroupInfoParam` 接口定义如下：**

```
/**
 * 构造参数实例
 * @param groupId 群 ID
 */
public ModifyGroupInfoParam(@NonNull String groupId)

/**
 * 设置修改后的群名称
 * @param groupName 群名称
 */
public ModifyGroupInfoParam setGroupName(@NonNull String groupName)

/**
 * 设置修改后的群公告
 * @param notification 群公告
 */
public ModifyGroupInfoParam setNotification(@NonNull String notification)

/**
 * 设置修改后的群简介
 * @param introduction 群简介
 */
public ModifyGroupInfoParam setIntroduction(@NonNull String introduction)

/**
 * 设置修改后的群头像 URL
 * @param faceUrl 群头像 URL
 */
public ModifyGroupInfoParam setFaceUrl(@NonNull String faceUrl)

/**
 * 设置加群选项
 * @param addOpt 加群选项
 */
public ModifyGroupInfoParam setAddOption(@NonNull TIMGroupAddOpt addOpt)

/**
 * 设置最大群成员数
 * @param maxMemberNum 最大群成员数
 */
public ModifyGroupInfoParam setMaxMemberNum(long maxMemberNum)

/**
 * 设置设置群组成员是否对外可见
 * @param visable 群组成员是否对外可见
 */
public ModifyGroupInfoParam setVisable(boolean visable)

/**
 * 设置群组自定义字段
 * @param customInfos 群组自定义字段字典
 */
public ModifyGroupInfoParam setCustomInfo(@NonNull Map<String, byte[]> customInfos)

/**
 * 设置群组全员禁言
 * @param silenceAll true - 设置全员禁言， false - 解除全员禁言
 * @since 3.1.1
 */
public ModifyGroupInfoParam setSilenceAll(boolean silenceAll)
```

### 修改群名

**权限说明：**

- **公开群、聊天室和直播大群：**只有群主或者管理员可以修改群名。
- **私有群：**任何人可修改群名。

**示例：**

```
TIMGroupManager.ModifyGroupInfoParam param = new TIMGroupManager.ModifyGroupInfoParam(getGroupId());
param.setGroupName("Great Team")
TIMGroupManager.getInstance().modifyGroupInfo(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		Log.e(tag, "modify group info failed, code:" + code +"|desc:" + desc);
	}

	@Override
	public void onSuccess() {
		Log.e(tag, "modify group info succ");
	}
});
```

### 修改群简介

**权限说明：**

- **公开群、聊天室和直播大群：**只有群主或者管理员可以修改群简介。
- **私有群：**任何人可修改群简介。

**示例：**

```
TIMGroupManager.ModifyGroupInfoParam param = new TIMGroupManager.ModifyGroupInfoParam(getGroupId());
param.setIntroduction("this is a introduction");
TIMGroupManager.getInstance().modifyGroupInfo(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		Log.e(tag, "modify group info failed, code:" + code +"|desc:" + desc);
	}

	@Override
	public void onSuccess() {
		Log.e(tag, "modify group info succ");
	}
});
```

### 修改群公告

**权限说明：**

- **公开群、聊天室和直播大群：**只有群主或者管理员可以修改群公告。
- **私有群：**任何人可修改群公告。

**示例：**

```
TIMGroupManager.ModifyGroupInfoParam param = new TIMGroupManager.ModifyGroupInfoParam(getGroupId());
param.setNotification("this is a notification");
TIMGroupManager.getInstance().modifyGroupInfo(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		Log.e(tag, "modify group info failed, code:" + code +"|desc:" + desc);
	}

	@Override
	public void onSuccess() {
		Log.e(tag, "modify group info succ");
	}
});
```

### 修改群头像

**权限说明：**

- **公开群、聊天室和直播大群：**只有群主或者管理员可以修改群头像。
- **私有群：**任何人可修改群头像。


**示例：**

```
TIMGroupManager.ModifyGroupInfoParam param = new TIMGroupManager.ModifyGroupInfoParam(getGroupId());
param.setFaceUrl("http://faceurl");
TIMGroupManager.getInstance().modifyGroupInfo(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		Log.e(tag, "modify group info failed, code:" + code +"|desc:" + desc);
	}

	@Override
	public void onSuccess() {
		Log.e(tag, "modify group info succ");
	}
});
```

### 修改加群选项

**权限说明：**

- **公开群、聊天室和直播大群：**只有群主或者管理员可以修改加群选项。
- **私有群：**只能通过邀请加入群组，不能主动申请加入某个群组。

**示例：**

```
TIMGroupManager.ModifyGroupInfoParam param = new TIMGroupManager.ModifyGroupInfoParam(getGroupId());
param.setAddOption(TIMGroupAddOpt.TIM_GROUP_ADD_ANY);
TIMGroupManager.getInstance().modifyGroupInfo(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		Log.e(tag, "modify group info failed, code:" + code +"|desc:" + desc);
	}

	@Override
	public void onSuccess() {
		Log.e(tag, "modify group info succ");
	}
});
```

### 修改群维度自定义字段

**权限说明：**

- 需要后台配置相关的 key 和权限。

**示例：**

```
TIMGroupManager.ModifyGroupInfoParam param = new TIMGroupManager.ModifyGroupInfoParam(getGroupId());
Map<String, byte[]> customInfo = new HashMap<String, byte[]>();
try {
	customInfo.put("Test", "Test_value".getBytes("utf-8"));
	param.setCustomInfo(customInfo);
} catch (UnsupportedEncodingException e) {
	e.printStackTrace();
}

TIMGroupManager.getInstance().modifyGroupInfo(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		Log.e(tag, "modify group info failed, code:" + code +"|desc:" + desc);
	}

	@Override
	public void onSuccess() {
		Log.e(tag, "modify group info succ");
	}
});
```

### 全员禁言

**权限说明：**

- **只有群主和管理员**才有权限进行全员禁言的操作。
- **所有群组类型**都支持全员禁言的操作。

**示例：**

```
TIMGroupManager.ModifyGroupInfoParam param = new TIMGroupManager.ModifyGroupInfoParam(groupId);
param.setSilenceAll(true);
TIMGroupManager.getInstance().modifyGroupInfo(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		Log.e(tag, "modify group info failed, code:" + code +"|desc:" + desc);
	}

	@Override
	public void onSuccess() {
		Log.e(tag, "modify group info succ");
	}
});
```

## 修改群成员资料

修改群成员资料的接口由 `TIMGroupManager` 提供，可以对修改群成员的身份、群名片、对群成员禁言等。

**原型：**

```
/**
 * 修改群成员资料
 * @param param 修改群成员资料参数
 * @param cb 回调
 */
public void modifyMemberInfo(@NonNull ModifyMemberInfoParam param, @NonNull TIMCallBack cb)
```

**`TIMGroupManager.ModifyMemberInfoParam` 接口定义如下：**

```
/**
 * 构造修改群成员资料参数
 * @param groupId 群成员所在群的群 ID
 * @param identifier 要修改的群成员的用户 ID
 */
public ModifyMemberInfoParam(@NonNull String groupId, @NonNull String identifier)

/**
 * 修改群成员群名片
 * @param nameCard 群名片
 */
public ModifyMemberInfoParam setNameCard(@NonNull String nameCard)

/**
 * 修改群消息接收选项
 * @param receiveMessageOpt 群消息接收选项，详见{@see TIMGroupReceiveMessageOpt}
 */
public ModifyMemberInfoParam setReceiveMessageOpt(@NonNull TIMGroupReceiveMessageOpt receiveMessageOpt)

/**
 * 修改群成员角色身份（只有群主和管理员可以修改）
 * @param roleType 身份类型。不能修改为群主类型，详见{@see TIMGroupMemberRoleType}
 */
public ModifyMemberInfoParam setRoleType(TIMGroupMemberRoleType roleType)

/**
 * 设置群成员的禁言时间（只有群主和管理员可以设置）
 * @param silence 禁言时间
 */
public ModifyMemberInfoParam setSilence(long silence)

/**
 * 设置群组自定义字段
 * @param customInfo 群组自定义字段字典
 */
public ModifyMemberInfoParam setCustomInfo(Map<String, byte[]> customInfo)
```

### 修改用户群内身份

**权限说明：**

- **只有群主或者管理员**可以进行对群成员的身份进行修改。
- **直播大群**不支持修改用户群内身份。

**示例：**

```
TIMGroupManager.ModifyMemberInfoParam param = new TIMGroupManager.ModifyMemberInfoParam(groupId, identifier);
param.setRoleType(TIMGroupMemberRoleType.Admin);

TIMGroupManager.getInstance().modifyMemberInfo(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		Log.e(tag, "modifyMemberInfo failed, code:" + code + "|msg: " + desc);
	}

	@Override
	public void onSuccess() {
		Log.d(tag, "modifyMemberInfo succ");
	}
});
```

###  对群成员进行禁言

通过 `modifyMemberInfoParam.setSilence()` 可以对群成员进行禁言并设置禁言时长。

**权限说明：**

- **只有群主或者管理员**可以进行对群成员进行禁言。

**示例：**

```
//禁言 100 秒
TIMGroupManager.ModifyMemberInfoParam param = new TIMGroupManager.ModifyMemberInfoParam(groupId, identifier);
param.setSilence(100);

TIMGroupManager.getInstance().modifyMemberInfo(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		Log.e(tag, "modifyMemberInfo failed, code:" + code + "|msg: " + desc);
	}

	@Override
	public void onSuccess() {
		Log.d(tag, "modifyMemberInfo succ");
	}
});
```

###  修改群名片


**示例：**

```
TIMGroupManager.ModifyMemberInfoParam param = new TIMGroupManager.ModifyMemberInfoParam(groupId, identifier);
param.setNameCard("cat");

TIMGroupManager.getInstance().modifyMemberInfo(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		Log.e(tag, "modifyMemberInfo failed, code:" + code + "|msg: " + desc);
	}

	@Override
	public void onSuccess() {
		Log.d(tag, "modifyMemberInfo succ");
	}
});
```

###  修改群成员维度自定义字段

**示例：**

```
TIMGroupManager.ModifyMemberInfoParam param = new TIMGroupManager.ModifyMemberInfoParam(groupId, identifier);
Map<String, byte[]> customInfo = new HashMap<>();
try {
	customInfo.put("Test", "Custom".getBytes("utf-8"));
	param.setCustomInfo(customInfo);
} catch (UnsupportedEncodingException e) {
	e.printStackTrace();
}

TIMGroupManager.getInstance().modifyMemberInfo(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		Log.e(tag, "modifyMemberInfo failed, code:" + code + "|msg: " + desc);
	}

	@Override
	public void onSuccess() {
		Log.d(tag, "modifyMemberInfo succ");
	}
});
```

###  修改群消息接收选项

**权限说明：**

- **公开群和私有群：**默认消息接收方式为接收并离线推送群消息。
- **聊天室和音视频聊天室：**默认为接收但不离线推送群消息。

**`TIMGroupReceiveMessageOpt` 接口定义如下：**

```
//不接收群消息， 服务器不会进行转发
TIMGroupReceiveMessageOpt.NotReceive

//接收群消息，但若离线情况下则不会推送离线消息
TIMGroupReceiveMessageOpt.ReceiveNotNotify

//接收群消息，若离线情况下会推送离线消息
TIMGroupReceiveMessageOpt.ReceiveAndNotify
```

**示例：**

```
TIMGroupManager.ModifyMemberInfoParam param = new TIMGroupManager.ModifyMemberInfoParam(groupId, identifier);
param.setReceiveMessageOpt(TIMGroupReceiveMessageOpt.ReceiveAndNotify);

TIMGroupManager.getInstance().modifyMemberInfo(param, new TIMCallBack() {
	@Override
	public void onError(int code, String desc) {
		Log.e(tag, "modifyMemberInfo failed, code:" + code + "|msg: " + desc);
	}

	@Override
	public void onSuccess() {
		Log.d(tag, "modifyMemberInfo succ");
	}
});
```

## 群组未决信息

群组未决信息泛指所有需要审批的群相关的操作。例如：加群待审批，拉人入群待审批等等。 群组未决信息由类 `TIMGroupPendencyItem` 表示。

**`TIMGroupPendencyItem` 的成员方法如下：**
```
/**
 * 获取群组 ID
 * @return 群组 ID
 */
public String getGroupId()

/**
 * 获取请求者 identifier，请求加群:请求者，邀请加群:邀请人
 * @return 请求者identifier
 */
public String getFromUser()

/**
 * 获取处理者 identifier, 请求加群:0，邀请加群:被邀请人
 * @return 处理者 identifier
 */
public String getToUser()

/**
 * 获取群未决添加的时间
 * @return 群未决添加的时间
 */
public long getAddTime()

/**
 * 获取群未决请求类型
 * @return 群未决请求类型，详见 TIMGroupPendencyGetType
 */
public TIMGroupPendencyGetType getPendencyType()

/**
 * 获取群未决处理状态
 * @return 群未决处理状态，详见{@see TIMGroupPendencyHandledStatus}
 */
public TIMGroupPendencyHandledStatus getHandledStatus()

/**
 * 获取群未决处理操作类型，只有处理状态不为{@see TIMGroupPendencyHandledStatus#NOT_HANDLED}的时候有效
 * @return 群未决处理操作类型，详见{@see TIMGroupPendencyOperationType}
 */
public TIMGroupPendencyOperationType getOperationType()

/**
 * 获取请求者添加的附加信息
 * @return 请求者添加的附加信息
 */
public String getRequestMsg()

/**
 * 获取请求者添加的自定义信息
 * @return 请求者添加的自定义信息
 */
private String getRequestUserData()

/**
 * 获取处理者添加的附加信息，只有处理状态不为{@see TIMGroupPendencyHandledStatus#NOT_HANDLED}的时候有效
 * @return 处理者添加的附加信息
 */
public String getHandledMsg()

/**
 * 获取处理者添加的自定义信息，只有处理状态不为{@see TIMGroupPendencyHandledStatus#NOT_HANDLED}的时候有效
 * @return 处理者添加的自定义信息
 */
private String getHandledUserData()

/**
 * 同意申请，目前只对申请/邀请加群消息生效
 *
 * @param msg 同意理由，选填
 * @param cb 回调
 */
public void accept(String msg, TIMCallBack cb)

/**
 * 拒绝申请，目前只对申请/邀请加群消息生效
 *
 * @param msg  同意理由，选填
 * @param cb 回调
 */
public void refuse(String msg, TIMCallBack cb)
```

### 拉取群未决列表

通过 `TIMGroupManager` 提供的 `getGroupPendencyList` 接口可拉取群未决相关信息。即便审核通过或者拒绝后，该条信息也可通过此接口拉回，拉回的信息中有已决标志。

**权限说明：**

**只有审批人**有权限拉取相关信息。

>例如：
>- UserA 申请加入群 GroupA，则群管理员可获取此未决相关信息，UserA 因为没有审批权限，不需要获取未决信息。
>- 如果 AdminA 拉 UserA 进去 GroupA，则 UserA 可以拉取此未决相关信息，因为该未决信息待 UserA 审批。

**原型：**

```
/**
 * 分页获取群未决请求列表
 * @param param 获取群未决请求列表参数类，详见{@see TIMGroupPendencyGetParam}
 * @param cb 回调，在 onSuccess 的参数中返回群未决的列表及元数据，详见{@see TIMGroupPendencyMeta} 及{@see TIMGroupPendencyItem}
 */
public void getGroupPendencyList(@NonNull TIMGroupPendencyGetParam param,
								 @NonNull TIMValueCallBack<TIMGroupPendencyListGetSucc> cb)
```

**`TIMGroupPendencyGetParam` 的接口定义如下：**

```
/**
 * 设置翻页时间戳，只用来翻页，第一次请求填 0，后边根据 server 返回的{@see TIMGroupPendencyMeta}中的时间戳进行填写
 * @param timestamp 翻页时间戳
 */
public void setTimestamp(long timestamp)

/**
 * 设置每页的数量（建议值，server 可根据需要返回或多或少，不能作为完成与否的标志）
 * @param numPerPage 每页的数量
 */
public void setNumPerPage(long numPerPage)
```

**示例：**

```
TIMGroupPendencyGetParam param = new TIMGroupPendencyGetParam();
param.setTimestamp(0);//首次获取填 0
param.setNumPerPage(10);

TIMGroupManager.getInstance().getGroupPendencyList(param, new TIMValueCallBack<TIMGroupPendencyListGetSucc>() {
    @Override
    public void onError(int code, String desc) {

    }

    @Override
    public void onSuccess(TIMGroupPendencyListGetSucc timGroupPendencyListGetSucc) {
        //meta中的nextStartTimestamp如果不为 0,可以先保存起来，
        // 作为获取下一页数据的参数设置到 TIMGroupPendencyGetParam 中
        TIMGroupPendencyMeta meta = timGroupPendencyListGetSucc.getPendencyMeta();
        Log.d(tag, meta.getNextStartTimestamp()
                + "|" + meta.getReportedTimestamp() + "|" + meta.getUnReadCount());

        List<TIMGroupPendencyItem> pendencyItems = timGroupPendencyListGetSucc.getPendencies();
        for(TIMGroupPendencyItem item : pendencyItems){
            //对群未决进行相应操作，例如查看/通过/拒绝等
        }
    }
});
```

###  上报群未决已读

对于未决信息，通过 `TIMGroupManager` 提供的 `reportGroupPendency` 可对其和之前的所有未决信息上报已读。上报已读后，仍然可以拉取到这些未决信息，但可通过对已读时戳的判断判定未决信息是否已读。

**原型：**

```
/**
 * 群未决请求已读上报
 * @param timestamp 已读时间戳(单位秒)，此时间戳以前的群未决请求都将置为已读
 * @param cb 回调
 */
public void reportGroupPendency(long timestamp, @NonNull TIMCallBack cb)
```


### 处理群未决信息

通过 `getGroupPendencyList` 获取到一个群未决请求（`TIMGroupPendencyItem`）的列表，对于列表中的每一个元素，都可以通过 `TIMGroupPendencyItem` 类中的 `accept/refuse` 接口来对群未决进行审批。已处理成功过的未决信息不能再次处理。

**原型：**

```
/**
 * 同意申请，目前只对申请/邀请加群消息生效
 *
 * @param msg 同意理由，选填
 * @param cb 回调
 */
public void accept(String msg, TIMCallBack cb)

/**
 * 拒绝申请，目前只对申请/邀请加群消息生效
 *
 * @param msg  同意理由，选填
 * @param cb 回调
 */
public void refuse(String msg, TIMCallBack cb)
```

## 群事件消息

当有用户被邀请加入群组，或者有用户被移出群组时，群内会产生提示消息，调用方可以根据需要展示给群组用户，或者忽略。提示消息使用一个特殊的 `Elem` 标识，通过新消息回调返回消息（请参见 [新消息通知](https://cloud.tencent.com/doc/product/269/9229#.E6.96.B0.E6.B6.88.E6.81.AF.E9.80.9A.E7.9F.A5)）。除了可以从新消息通知中获取群事件消息外，还可以在**登录前**通过 `TIMUserConfig` 中的 `setGroupEventListener` 接口设置群事件监听器来统一监听相应的事件（请参见 [初始化（Android）](https://cloud.tencent.com/document/product/269/9229#.E7.94.A8.E6.88.B7.E9.85.8D.E7.BD.AE)）。

>!聊天室（ChatRoom）和音视频聊天室（AVChatRoom）的群组事件消息不会通过新消息通知下发，只能通过注册群事件监听器对相应群事件进行监听。

如下图中，展示一条修改群名的事件消息。
![](https://main.qcloudimg.com/raw/78865ba68ed75700137e5afbd2ac3e43.jpg)


**`TIMGroupTipsElem` 成员方法：**

```
//获取群资料变更信息列表，仅当 tipsType 值为 TIMGroupTipsType.ModifyGroupInfo 时有效
java.util.List<TIMGroupTipsElemGroupInfo> getGroupInfoList()

//获取群组名称
java.lang.String    getGroupName()

//获取群成员变更信息列表，仅当 tipsType 值为 TIMGroupTipsType.ModifyMemberInfo 时有效
java.util.List<TIMGroupTipsElemMemberInfo>    getMemberInfoList()

//获取操作者
java.lang.String    getOpUser()

//获取群组事件通知类型
TIMGroupTipsType    getTipsType()

//获取被操作的帐号列表
java.util.List<java.lang.String>  getUserList()
```

**`TIMGroupTipsType` 原型：**

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

### 用户加入群组通知

**触发时机：**当有用户加入群组时（包括申请入群和被邀请入群），群组内会由系统发出通知，开发者可选择展示样式。可以更新群成员列表。收到的消息 type 为 `TIMGroupTipsType.Join`。

**`TIMGroupTipsElem` 成员方法返回说明：**

方法|返回说明
---|---
getType |	TIMGroupTipsType.Join
getOpUser |	申请入群：申请人</br>邀请入群：邀请人
getGroupName |	群名
getUserList | 入群的用户列表

### 用户退出群组

**触发时机：**当有用户主动退群时，群组内会由系统发出通知。可以选择更新群成员列表。收到的消息 type 为 `TIMGroupTipsType.Quit`。

**`TIMGroupTipsElem` 成员方法返回说明：**

方法|返回说明
---|---
getType|	TIMGroupTipsType.Quit
getOpUser |	退出用户 identifier
getGroupName |	群名

### 用户被踢出群组

**触发时机：**当有用户被踢出群组时，群组内会由系统发出通知。可以更新群成员列表。收到的消息 type 为 `TIMGroupTipsType.Kick`。

**`TIMGroupTipsElem` 成员方法返回说明：**

方法|返回说明
---|---
getType|	TIMGroupTipsType.Kick
getOpUser |	踢人的 identifier
getGroupName |	群名
getUserList | 被踢用户列表

### 被设置/取消管理员

**触发时机：**当有用户被设置为管理员或者被取消管理员身份时，群组内会由系统发出通知。如果界面有显示是否管理员，此时可更新管理员标识。收到的消息 type 为 `TIMGroupTipsType.SetAdmin` 和 `TIMGroupTipsType.CancelAdmin`。

**`TIMGroupTipsElem` 成员方法返回说明：**

方法|返回说明
---|---
getType|	设置：TIMGroupTipsType.SetAdmin<br>取消：TIMGroupTipsType.CancelAdmin
getOpUser |	操作用户 identifier
getGroupName |	群名
getUserList | 被设置/取消管理员身份的用户列表

### 群资料变更

**触发时机：**当群资料变更，如群名、群简介等，会有系统消息发出，可更新相关展示字段，或者选择性把消息展示给用户。

**`TIMGroupTipsElem` 成员方法返回说明：**

方法|返回说明
---|---
getType|	TIMGroupTipsType.ModifyGroupInfo
getOpUser |	操作用户 identifier
getGroupName |	群名
getGroupInfoList|	群变更的具体资料信息，为 TIMGroupTipsElemGroupInfo 结构体列表

**`TIMGroupTipsElemGroupInfo` 原型：**

```
//获取消息内容
java.lang.String    getContent()

//获取群资料变更消息类型
TIMGroupTipsGroupInfoType   getType()
```

**`TIMGroupTipsGroupInfoType` 原型：**
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

### 群成员资料变更

**触发时机：**当群成员的群相关资料变更时，包括群内用户被禁言、群内成员角色变更，会有系统消息发出，可更新相关字段展示，或者选择性把消息展示给用户。

>!
>- **这里的资料仅包括群相关资料，例如禁言时间、成员角色变更等，不包括用户昵称等本身资料**，对于群内人数可能过多，不建议实时更新，建议的做法是直接显示消息体内的资料，参考：[消息发送者以及相关资料](https://cloud.tencent.com/doc/product/269/9232#.E6.B6.88.E6.81.AF.E5.8F.91.E9.80.81.E8.80.85.E5.8F.8A.E5.85.B6.E7.9B.B8.E5.85.B3.E8.B5.84.E6.96.99)。
>- 如果本地有保存用户资料，可根据消息体内资料判断是否有变更，在收到此用户一条消息后更新资料。

**`TIMGroupTipsElem` 成员方法返回说明：**

方法|返回说明
---|---
getType|	TIMGroupTipsType.ModifyMemberInfo
getOpUser |	操作用户 identifier
getGroupName |	群名
getMemberInfoList|	变更的群成员的具体资料信息，为 TIMGroupTipsElemMemberInfo 结构体列表

**`TIMGroupTipsElemMemberInfo` 原型：**

```
//获取被禁言群成员的 identifier
java.lang.String    getIdentifier()

//获取被禁言时间
long    getShutupTime()
```

## 群系统消息

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

**`TIMGroupSystemElem` 成员方法定义如下：**

```
/**
 *  操作方平台信息
 *  取值： iOS Android Windows Mac Web RESTAPI Unknown
 * @return 返回操作方平台信息
 */
public String getPlatform()

/**
 * 获取消息子类型
 * @return 群系统消息子类型
 */
public TIMGroupSystemElemType getSubtype()

/**
 * 获取消息群 ID
 * @return
 */
public String getGroupId()

/**
 * 获取操作人
 * @return 操作人的 identifier
 */
public String getOpUser()

/**
 * 获取操作理由
 * @return 操作理由
 */
public String getOpReason()

/**
 * 获取自定义通知
 * @return 自定义通知
 */
public byte[] getUserData()

/**
 * 获取操作者个人资料
 * @return 操作者个人资料
 */
public TIMUserProfile getOpUserInfo()

/**
 * 获取操作者群内资料
 * @return 操作者群内资料
 */
public TIMGroupMemberInfo getOpGroupMemberInfo()
```

### 申请加群消息

**触发时机：**当有用户申请加群时，群管理员会收到申请加群消息，可展示给用户，由用户决定是否同意对方加群。消息类型为：`TIM_GROUP_SYSTEM_ADD_GROUP_REQUEST_TYPE`。

**TIMGroupSystemElem 成员方法返回说明：**

方法|返回说明
---|---
getSubtype	| TIM_GROUP_SYSTEM_ADD_GROUP_REQUEST_TYPE
getGroupId	| 群组 ID，表示是哪个群的申请
getOpUser	| 申请人
getOpReason	| 申请理由（可选）


### 申请加群同意/拒绝消息

**触发时机：**当管理员同意加群请求时，申请人会收到同意入群的消息，当管理员拒绝时，收到拒绝入群的消息。

**`TIMGroupSystemElem` 成员方法返回说明：**

方法|返回说明
---|---
getSubtype	| 同意：TIM_GROUP_SYSTEM_ADD_GROUP_ACCEPT_TYPE<br>拒绝：TIM_GROUP_SYSTEM_ADD_GROUP_REFUSE_TYPE
getGroupId	| 群组 ID，表示是哪个群通过/拒绝了
getOpUser	| 处理请求的管理员 identifier
getOpReason	| 同意或者拒绝理由（可选）

### 邀请入群请求消息

**触发时机：**当用户被邀请加入群组（**此时用户还没有加入到群组，需要用户审批**）时，该用户会收到邀请消息。

>!创建群组时初始成员无需邀请即可入群。

**`TIMGroupSystemElem` 成员方法返回说明：**

方法|返回说明
---|---
getSubtype	| TIM_GROUP_SYSTEM_INVITE_TO_GROUP_REQUEST_TYPE
getGroupId	| 群组 ID，邀请进入哪个群
getOpUser	| 操作人，表示哪个用户的邀请


### 邀请入群同意/拒绝消息

**触发时机：**当被邀请者同意入群请求时，邀请者会收到同意入群的消息。当被邀请者拒绝时，邀请者收到拒绝入群的消息。

**`TIMGroupSystemElem` 成员方法返回说明：**

方法|返回说明
---|---
getSubtype	| 同意：TIM_GROUP_SYSTEM_INVITATION_ACCEPTED_TYPE<br>拒绝：TIM_GROUP_SYSTEM_INVITATION_REFUSED_TYPE
getGroupId	| 群组 ID，表示是哪个群通过/拒绝了
getOpUser	| 处理请求的管理员 identifier
getOpReason	| 同意或者拒绝理由（可选）


### 被管理员踢出群组

**触发时机：**当用户被管理员踢出群组时，申请人会收到被踢出群的消息。

**`TIMGroupSystemElem` 成员方法返回说明：**

方法|返回说明
---|---
getSubtype	| TIM_GROUP_SYSTEM_KICK_OFF_FROM_GROUP_TYPE
getGroupId	| 群组 ID，表示在哪个群里被踢了
getOpUser	| 操作管理员 identifier


### 群被解散

**触发时机：**当群被解散时，全员会收到解散群消息。

**`TIMGroupSystemElem` 成员方法返回说明：**

方法|返回说明
---|---
getSubtype	| TIM_GROUP_SYSTEM_DELETE_GROUP_TYPE
getGroupId	| 群组 ID，表示哪个群被解散了
getOpUser	| 操作管理员 identifier

### 创建群消息

**触发时机：**当群创建时，创建者会收到创建群消息。

当调用创建群方法成功回调后，即表示创建成功，此消息主要为多终端同步，如果有在其他终端登录，作为更新群列表的时机，本终端可以选择忽略。

**`TIMGroupSystemElem` 成员方法返回说明：**

方法|返回说明
---|---
getSubtype	| TIM_GROUP_SYSTEM_CREATE_GROUP_TYPE
getGroupId	| 群组 ID，表示创建的群 ID
getOpUser	| 创建者，这里也就是用户自己

### 邀请入群消息

**触发时机：**当用户被邀请加入到群组（**此时用户已经加入到群组**）时，该用户会收到邀请消息。

>!创建群组时初始成员无需邀请即可入群。

**`TIMGroupSystemElem` 成员方法返回说明：**

方法|返回说明
---|---
getSubtype	| TIM_GROUP_SYSTEM_INVITED_TO_GROUP_TYPE
getGroupId	| 群组 ID，邀请进入哪个群
getOpUser	| 操作人，表示哪个用户的邀请

### 主动退群

**触发时机：**当用户主动退出群组时，该用户会收到退群消息，只有退群的用户自己可以收到。

当用户调用 `QuitGroup` 时成功回调返回，表示已退出成功，此消息主要为了多终端同步，其他终端收到该消息时可以更新群列表，本终端可以选择忽略。

**`TIMGroupSystemElem` 成员方法返回说明：**

方法|返回说明
---|---
getSubtype	| TIM_GROUP_SYSTEM_QUIT_GROUP_TYPE
getGroupId	| 群组 ID，表示退出的哪个群
getOpUser	| 操作人，这里即为用户自己

### 设置/取消管理员

**触发时机：**当用户被设置为管理员时，可收到被设置管理员的消息通知，当用户被取消管理员时，可收到取消通知，可提示用户。

**`TIMGroupSystemElem` 成员方法返回说明：**

方法|返回说明
---|---
getSubtype	|	取消管理员身份：TIM_GROUP_SYSTEM_GRANT_ADMIN_TYPE<br>授予管理员身份：TIM_GROUP_SYSTEM_CANCEL_ADMIN_TYPE
getGroupId	| 群组 ID，表示哪个群的事件
getOpUser	| 操作人

### 群被回收

**触发时机：**当群组被系统回收时，全员可收到群组被回收消息。

**`TIMGroupSystemElem` 成员方法返回说明：**

方法|返回说明
---|---
getSubtype	|	TIM_GROUP_SYSTEM_REVOKE_GROUP_TYPE
getGroupId	| 群组 ID，表示哪个群被回收了

