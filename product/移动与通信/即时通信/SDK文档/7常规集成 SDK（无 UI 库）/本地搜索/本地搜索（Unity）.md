Unity SDK 支持本地搜索，但是需要将套餐升级到旗舰版，请参见 [购买指引](https://cloud.tencent.com/document/product/269/32458)。

搜索接口的界面分为以下部分，最上面是搜索好友，中间部分是搜索群组、群成员，最下面是搜索消息且按照会话分组。

## SDK 接入指引

### 搜索好友

使用 FriendshipSearchFriends 接口进行好友搜索，可指定用户 ID、昵称、备注进行搜索，调用案例如下：

```c#
FriendSearchParam searchparam  = new FriendSearchParam();
searchparam.friendship_search_param_keyword_list = ["小何"];
searchparam.friendship_search_param_search_field_list = [TIMFriendshipSearchFieldKey.kTIMFriendshipSearchFieldKey_Identifier,TIMFriendshipSearchFieldKey.kTIMFriendshipSearchFieldKey_NikeName,TIMFriendshipSearchFieldKey.kTIMFriendshipSearchFieldKey_Remark]
TencentIMSDK.FriendshipSearchFriends(searchparam,(int code, string desc, string json_param, string user_data)=>{
  // 搜索结果
});
```



### 搜索本地消息

可使用 MsgSearchLocalMessages 进行本地消息搜索，详细参数可参见 [MessageSearchParam](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.types.MessageSearchParam.html)。

- 通过 msg_search_param_message_type_array 指定搜索消息类型
- 通过 msg_search_param_conv_id 指定搜索会话
- 通过 msg_search_param_search_time_position 指定搜索消息的起始时间

```c#
MessageSearchParam searchparam  = new MessageSearchParam();
searchparam.msg_search_param_keyword_array = ["小何"]; // 关键词
searchparam.msg_search_param_message_type_array = [TIMElemType.kTIMElem_Text]; // 只对文本消息进行搜索
searchparam.msg_search_param_conv_id = ""; // 指定会话进行搜索
// ...
TencentIMSDK.FriendshipSearchFriends(searchparam,(int code, string desc, string json_param, string user_data)=>{
  // 搜索结果
});
```



### 搜索群资料

可使用 [GroupSearchGroups](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_GroupSearchGroups_com_tencent_imsdk_unity_types_GroupSearchParam_com_tencent_imsdk_unity_callback_ValueCallback_) 进行群资料搜索，详细参数可参见 [GroupSearchParam](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.types.GroupSearchParam.html)。

```c#
GroupSearchParam searchparam  = new GroupSearchParam();
searchparam.group_search_params_keyword_list = ["小何"];
searchparam.group_search_params_field_list = [TIMGroupSearchFieldKey.kTIMGroupSearchFieldKey_GroupId,TIMGroupSearchFieldKey.kTIMGroupSearchFieldKey_GroupName];//指定搜索区域
TencentIMSDK.GroupSearchGroups(searchparam,(int code, string desc, string json_param, string user_data)=>{
  // 搜索结果
});
```


### 搜索群成员

可使用 [GroupSearchGroupMembers](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.TencentIMSDK.html#com_tencent_imsdk_unity_TencentIMSDK_GroupSearchGroupMembers_com_tencent_imsdk_unity_types_GroupMemberSearchParam_com_tencent_imsdk_unity_callback_ValueCallback_) 进行群成员搜索，详细参数可参见 [GroupMemberSearchParam](https://comm.qq.com/im/sdk/unity_plus/_site/api/com.tencent.imsdk.unity.types.GroupMemberSearchParam.html)。

```c#
GroupSearchParam searchparam  = new GroupMemberSearchParam();
searchparam.group_search_member_params_keyword_list = ["小何"];
searchparam.group_search_member_params_groupid_list = ['id','id2'];//指定群
searchparam.group_search_member_params_field_list = [] // 搜索区域 TIMGroupMemberSearchFieldKey
TencentIMSDK.GroupSearchGroups(searchparam,(int code, string desc, string json_param, string user_data)=>{
  // 搜索结果
});
```

