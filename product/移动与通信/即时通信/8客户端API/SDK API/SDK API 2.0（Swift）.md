>!**新老版本 API 请勿混合使用**。

## 初始化登录接口

初始化并成功登录，是正常使用腾讯云 IM 服务的前提。

| API | 描述 |
|---------|---------|
| [initSDK](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.initsdk(sdkappid:config:)) | 初始化 |
| [unInitSDK](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.uninitsdk()) | 反初始化 |
| [addIMSDKListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.addimsdklistener(listener:)) | 添加 IM 监听 |
| [removeIMSDKListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.removeimsdklistener(listener:)) | 移除 IM 监听 |
| [getVersion](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.getversion()) |获取版本号 |
| [getServerTime](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.getservertime()) |获取服务器当前时间 |
| [login](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.login(userid:usersig:succ:fail:)) | 登录 |
| [logout](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.logout(succ:fail:)) | 退出登录 |
| [getLoginUser](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.getloginuser()) | 获取登录用户 |
| [getLoginStatus](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.getloginstatus()) | 获取登录状态 |
| [getUserStatus](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.getuserstatus(useridlist:succ:fail:)) | 查询用户状态 |
| [setSelfStatus](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.setselfstatus(status:succ:fail:)) | 设置自己的状态 |
| [subscribeUserStatus](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.subscribeuserstatus(useridlist:succ:fail:)) | 订阅用户状态 |
| [unsubscribeUserStatus](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.unsubscribeuserstatus(useridlist:succ:fail:)) | 取消订阅用户状态 |

## 简单消息收发接口

如果您只需要使用文本和信令（即一段自定义buffer）消息，只需要使用这套简单消息收发接口即可。

| API | 描述 |
|---------|---------|
| [addSimpleMsgListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.addsimplemsglistener(listener:)) | 设置基本消息（文本消息和自定义消息）的事件监听器，<br/> 请不要同 [addAdvancedMsgListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.addadvancedmsglistener(listener:)) 混用 |
| [removeSimpleMsgListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.removesimplemsglistener(listener:)) | 移除基本消息（文本消息和自定义消息）的事件监听器 |
| [sendC2CTextMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.sendc2ctextmessage(text:to:succ:fail:)) | 发送单聊（C2C）普通文本消息 |
| [sendC2CCustomMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.sendc2ccustommessage(customdata:to:succ:fail:)) | 发送单聊（C2C）自定义（信令）消息 |
| [sendGroupTextMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.sendgrouptextmessage(text:to:priority:succ:fail:)) | 发送群聊普通文本消息 |
| [sendGroupCustomMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.sendgroupcustommessage(customdata:to:priority:succ:fail:)) | 发送群聊自定义（信令）消息 |

## 信令接口

| API | 描述 |
|---------|---------|
| [addSignalingListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Signaling.html#v2timmanager.addsignalinglistener(listener:)) | 添加信令监听                            |
| [removeSignalingListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Signaling.html#v2timmanager.removesignalinglistener(listener:)) | 移除信令监听 |
| [invite](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Signaling.html#v2timmanager.invite(invitee:data:onlineuseronly:offlinepushinfo:timeout:succ:fail:)) | 邀请某个人 |
| [inviteInGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Signaling.html#v2timmanager.inviteingroup(groupid:inviteelist:data:onlineuseronly:timeout:succ:fail:)) | 邀请群内的某些人 |
| [cancel](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Signaling.html#v2timmanager.cancel(inviteid:data:succ:fail:)) | 邀请方取消邀请 |
| [accept](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Signaling.html#v2timmanager.accept(inviteid:data:succ:fail:)) | 接收方接收邀请 |
| [reject](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Signaling.html#v2timmanager.reject(inviteid:data:succ:fail:)) | 接收方拒绝邀请 |
| [getSignalingInfo](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Signaling.html#v2timmanager.getsignallinginfo(msg:)) | 获取信令信息 |
| [addInvitedSignaling](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Signaling.html#v2timmanager.addinvitedsignaling(signalinginfo:succ:fail:)) | 添加邀请信令（可以用于群离线推送消息触发的邀请信令） |
| [modifyInvitation](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Signaling.html#v2timmanager.modifyinvitation(inviteid:data:succ:fail:)) | 修改邀请信令 |

## 高级消息收发接口

如果您需要收发图片、视频、文件等富媒体消息，并需要撤回消息、标记已读、查询历史消息等高级功能，推荐使用下面这套高级消息接口（简单消息接口和高级消息接口请不要混用）。

| API | 描述 |
|---------|---------|
| [addAdvancedMsgListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.addadvancedmsglistener(listener:)) | 设置高级消息的事件监听器，<br/> 请不要同 [addSimpleMsgListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.addsimplemsglistener(listener:)) 混用 |
| [removeAdvancedMsgListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.removeadvancedmsglistener(listener:)) | 移除高级消息监听器 |
| [createTextMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createtextmessage(text:)) | 创建文本消息 |
| [createCustomMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createcustommessage(data:)) | 创建自定义消息 |
| [createImageMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createimagemessage(imagepath:)) | 创建图片消息 |
| [createSoundMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createsoundmessage(audiofilepath:duration:)) | 创建语音消息 |
| [createVideoMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createvideomessage(videofilepath:type:duration:snapshotpath:)) | 创建视频消息 |
| [createFileMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createfilemessage(filepath:filename:)) | 创建文件消息 |
| [createLocationMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createlocationmessage(desc:longitude:latitude:)) | 创建地理位置消息 |
| [createFaceMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createfacemessage(index:data:)) | 创建表情消息 |
| [createMergerMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createmergermessage(messagelist:title:abstractlist:compatibletext:)) | 创建合并转发消息 |
| [createForwardMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createforwardmessage(message:)) | 创建单条转发消息 |
| [createTargetedGroupMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createtargetedgroupmessage(message:receiverlist:)) | 创建定向群消息 |
| [createAtSignedGroupMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.createatsignedgroupmessage(message:atuserlist:)) | 创建带 @ 标记的群消息 |
| [sendMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.sendmessage(message:receiver:groupid:priority:onlineuseronly:offlinepushinfo:progress:succ:fail:)) | 发送消息，消息对象可以由 createXXXMessage 接口创建得来 |
| [setC2CReceiveMessageOpt](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.setc2creceivemessageopt(useridlist:opt:succ:fail:)) | 设置单聊消息秒打扰 |
| [getC2CReceiveMessageOpt](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.getc2creceivemessageopt(useridlist:succ:fail:)) | 获取单聊消息免打扰状态 |
| [setGroupReceiveMessageOpt](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.setgroupreceivemessageopt(groupid:opt:succ:fail:)) | 设置群聊消息免打扰状态 |
| [getC2CHistoryMessageList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.getc2chistorymessagelist(userid:count:lastmsg:succ:fail:)) | 获取单聊（C2C）历史消息 |
| [getGroupHistoryMessageList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.getgrouphistorymessagelist(groupid:count:lastmsg:succ:fail:)) | 获取群组历史消息 |
| [getHistoryMessageList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.gethistorymessagelist(option:succ:fail:)) | 获取历史消息高级接口 |
| [revokeMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.revokemessage(msg:succ:fail:)) | 撤回消息，消息对象可以由 createXXXMessage 接口创建得来 |
| [modifyMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.modifymessage(msg:completion:)) | 修改消息，消息对象可以由 createXXXMessage 接口创建得来 |
| [markC2CMessageAsRead](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.markc2cmessageasread(userid:succ:fail:)) | 设置单聊（C2C）消息已读          |
| [markGroupMessageAsRead](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.markgroupmessageasread(groupid:succ:fail:)) | 设置群组消息已读 |
| [markAllMessageAsRead](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.markallmessageasread(succ:fail:)) | 标记所有会话为已读 |
| [deleteMessageFromLocalStorage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.deletemessagefromlocalstorage(msg:succ:fail:)) | 删除本地消息 |
| [deleteMessages](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.deletemessages(msglist:succ:fail:)) | 删除本地及云端的消息 |
| [clearC2CHistoryMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.clearc2chistorymessage(userid:succ:fail:)) | 清空单聊本地及云端的消息 |
| [clearGroupHistoryMessage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.cleargrouphistorymessage(groupid:succ:fail:)) | 清空群组本地及云端的消息 |
| [insertGroupMessageToLocalStorage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.insertgroupmessagetolocalstorage(msg:to:sender:succ:fail:)) | 向群组消息列表中添加一条消息 |
| [insertC2CMessageToLocalStorage](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.insertc2cmessagetolocalstorage(msg:to:sender:succ:fail:)) | 向单聊消息列表中添加一条消息 |
| [findMessages](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.findmessages(messageidlist:succ:fail:)) | 根据 msgID 查找本地消息 |
| [searchLocalMessages](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.searchlocalmessages(param:succ:fail:)) | 搜索本地消息 |
| [sendMessageReadReceipts](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.sendmessagereadreceipts(messagelist:succ:fail:)) | 发送消息已读回执 |
| [getMessageReadReceipts](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.getmessagereadreceipts(messagelist:succ:fail:)) | 获取消息已读回执 |
| [getGroupMessageReadMemberList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.getgroupmessagereadmemberlist(message:filter:nextseq:count:succ:fail:)) | 获取群消息已读群成员列表 |
| [setMessageExtensions](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.setmessageextensions(message:extensions:succ:fail:)) | 设置消息扩展 |
| [getMessageExtensions](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.getmessageextensions(message:succ:fail:)) | 获取消息扩展 |
| [deleteMessageExtensions](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.deletemessageextensions(message:keys:succ:fail:)) | 删除消息扩展 |
| [translateText](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.translatetext(sourcetextlist:sourcelanguage:targetlanguage:completion:)) | 翻译文本消息 |



## 群组相关接口

腾讯云 IM SDK 支持四种预设的群组类型，每种类型都有其适用场景：

- 工作群（Work） ：类似普通微信群，创建后不能自由加入，必须由已经在群的用户邀请入群。
- 公开群（Public）   ：类似 QQ 群，用户申请加入，但需要群主或管理员审批。
- 会议群（Meeting）：适合跟 [TRTC](https://cloud.tencent.com/product/trtc) 结合实现视频会议和在线教育等场景，支持随意进出，支持查看进群前的历史消息。
- 直播群（AVChatRoom）：适合直播弹幕聊天室等场景，支持随意进出，人数无上限。

| API | 描述 |
|---------|---------|
| [addGroupListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.addgrouplistener(listener:)) | 添加群组相关的事件监听器 |
| [removeGroupListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.removegrouplistener(listener:)) | 移除群组相关的事件监听器 |
| [createGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.creategroup(grouptype:groupid:groupname:succ:fail:)) | 创建群组（简单版本） |
| [createGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.creategroup(info:memberlist:succ:fail:)) | 创建群组（高级版本），可在建群同时设置群信息和初始的群成员 |
| [joinGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.joingroup(groupid:msg:succ:fail:)) | 加入群组 |
| [quitGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.quitgroup(groupid:succ:fail:)) | 退出群组 |
| [dismissGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.dismissgroup(groupid:succ:fail:)) | 解散群组（仅群组和管理员可以解散） |
| [getJoinedGroupList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.getjoinedgrouplist(succ:fail:)) | 获取已经加入的群列表（不包括已加入的直播群） |
| [getGroupsInfo](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.getgroupsinfo(groupidlist:succ:fail:)) | 拉取群资料 |
| [searchGroups](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.searchgroups(searchparam:succ:fail:)) | 搜索群列表 |
| [setGroupInfo](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.setgroupinfo(info:succ:fail:)) | 修改群资料 |
| [ initGroupAttributes](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.initgroupattributes(groupid:attributes:succ:fail:)) | 初始化群属性 |
| [ setGroupAttributes](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.setgroupattributes(groupid:attributes:succ:fail:)) | 设置群属性 |
| [ deleteGroupAttributes](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.deletegroupattributes(groupid:keys:succ:fail:)) | 删除群属性 |
| [ getGroupAttributes](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.getgroupattributes(groupid:keys:succ:fail:)) | 获取群属性 |
| [getGroupOnlineMemberCount](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.getgrouponlinemembercount(groupid:succ:fail:)) | 获取群在线人数 |
| [getGroupMemberList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.getgroupmemberlist(groupid:filter:nextseq:succ:fail:)) | 获取群成员列表 |
| [getGroupMembersInfo](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.getgroupmembersinfo(groupid:memberlist:succ:fail:)) | 获取指定的群成员资料 |
| [searchGroupMembers](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.searchgroupmembers(searchparam:succ:fail:)) | 搜索指定的群成员资料 |
| [setGroupMemberInfo](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.setgroupmemberinfo(groupid:info:succ:fail:)) | 修改指定的群成员资料 |
| [muteGroupMember](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.mutegroupmember(groupid:memberuserid:mutetimeseconds:succ:fail:)) | 禁言 |
| [inviteUserToGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.inviteusertogroup(groupid:userlist:succ:fail:)) | 邀请他人入群                         |
| [kickGroupMember](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.kickgroupmember(groupid:memberlist:reason:succ:fail:)) | 踢人 |
| [setGroupMemberRole](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.setgroupmemberrole(groupid:memberuserid:newrole:succ:fail:)) | 切换群成员的角色 |
| [markGroupMemberList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.markgroupmemberlist(groupid:memberlist:marktype:enablemark:succ:fail:)) | 标记群成员 |
| [transferGroupOwner](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.transfergroupowner(groupid:memberuserid:succ:fail:)) | 转让群主 |
| [getGroupApplicationList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.getgroupapplicationlist(succ:fail:)) | 获取加群的申请列表 |
| [acceptGroupApplication](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.acceptgroupapplication(application:reason:succ:fail:)) | 同意某一条加群申请 |
| [refuseGroupApplication](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.refusegroupapplication(application:reason:succ:fail:)) | 拒绝某一条加群申请 |
| [setGroupApplicationRead](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.setgroupapplicationread(succ:fail:)) | 标记申请列表为已读 |
| [getJoinedCommunityList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.getjoinedcommunitylist(succ:fail:)) | 获取当前用户已经加入的支持话题的社群列表 |
| [createTopicInCommunity](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.createtopicincommunity(groupid:topicinfo:succ:fail:)) | 创建话题 |
| [deleteTopicFromCommunity](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.deletetopicfromcommunity(groupid:topicidlist:succ:fail:)) | 删除话题 |
| [setTopicInfo](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.settopicinfo(topicinfo:succ:fail:)) | 修改话题信息 |
| [getTopicInfoList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.gettopicinfolist(groupid:topicidlist:succ:fail:)) | 获取话题列表 |

## 会话列表相关接口

会话列表，即登录微信或 QQ 后首屏看到的列表，包含会话节点、会话名称、群名称、最后一条消息以及未读消息数等元素。

| API | 描述 |
|---------|---------|
| [addConversationListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.addconversationlistener(listener:)) | 添加会话监听器 |
| [removeConversationListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.removeconversationlistener(listener:)) | 移除会话监听器 |
| [getConversationList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.getconversationlist(nextseq:count:succ:fail:)) | 获取会话列表 |
| [getConversation](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.getconversation(conversationid:succ:fail:)) | 获取指定单个会话 |
| [getConversationList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.getconversationlist(conversationidlist:succ:fail:)) | 获取指定多个会话 |
| [getConversationListByFilter](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.getconversationlistbyfilter(filter:succ:fail:)) | 获取会话列表（高级接口） |
| [deleteConversation](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.deleteconversation(conversation:succ:fail:)) | 删除会话 |
| [setConversationDraft](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.setconversationdraft(conversationid:drafttext:succ:fail:)) | 设置会话草稿 |
| [setConversationCustomData](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.setconversationcustomdata(conversationidlist:customdata:succ:fail:)) | 设置回话自定义数据 |
| [pinConversation](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.pinconversation(conversationid:ispinned:succ:fail:)) | 置顶会话 |
| [markConversation](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.markconversation(conversationidlist:marktype:enablemark:succ:fail:)) | 标记会话 |
| [getTotalUnreadMessageCount](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.gettotalunreadmessagecount(succ:fail:)) | 获取会话总未读数 |
| [createConversationGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.createconversationgroup(groupname:conversationidlist:succ:fail:)) | 创建会话分组 |
| [getConversationGroupList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.getconversationgrouplist(succ:fail:)) | 获取会话分组列表 |
| [deleteConversationGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.deleteconversationgroup(groupname:succ:fail:)) | 删除会话分组 |
| [renameConversationGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.renameconversationgroup(oldname:newname:succ:fail:)) | 重命名会话分组 |
| [addConversationsToGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.addconversationstogroup(groupname:conversationidlist:succ:fail:)) | 添加会话到一个会话分组 |
| [deleteConversationsFromGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Conversation.html#v2timmanager.deleteconversationsfromgroup(groupname:conversationidlist:succ:fail:)) | 从一个会话分组中删除会话 |


## 用户资料相关接口

包含查询用户资料、修改个人资料以及屏蔽某人消息（即把某用户加入黑名单中）的相关接口。

| API | 描述 |
|---------|---------|
| [getUsersInfo](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.getusersinfo(useridlist:succ:fail:)) | 获取用户资料 |
| [setSelfInfo](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.setselfinfo(info:succ:fail:)) | 修改个人资料 |
| [addToBlackList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.addtoblacklist(useridlist:succ:fail:)) | 屏蔽某人的消息（添加该用户到黑名单中） |
| [deleteFromBlackList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.deletefromblacklist(useridlist:succ:fail:)) | 取消某人的消息屏蔽（把该用户从黑名单中移除） |
| [getBlackList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.getblacklist(succ:fail:)) | 获取黑名单列表 |

## 离线推送相关接口
如果想要在 App 切后台时依然能够实时收到 IM 消息，可以使用离线推送服务，详细配置请参考 [离线推送](https://cloud.tencent.com/document/product/269/9154)。

| API | 描述 |
|---------|---------|
| [setAPNSListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+APNS.html#v2timmanager.setapnslistener(apnslistener:)) | 设置 APNs 监听 |
| [setAPNS](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+APNS.html#v2timmanager.setapns(config:succ:fail:)) | 配置 APNs 推送信息 |
| [setVOIP](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+VOIP.html#v2timmanager.setvoip(config:succ:fail:)) | 配置 VoIP 推送信息 |

## 好友管理相关接口
腾讯云 IM 在收发消息时默认不检查是不是好友关系，您可以在 [**控制台**](https://console.cloud.tencent.com/im)  > **功能配置** > **登录与消息** > **好友关系检查**中开启"发送单聊消息检查关系链"开关，并使用如下接口增删好友和管理好友列表。

| API | 描述 |
|---------|---------|
| [addFriendListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.addfriendlistener(listener:)) | 添加关系链的监听器，用于接收好友列表和黑名单的变更事件 |
| [removeFriendListener](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.removefriendlistener(listener:)) | 移除关系链的监听器 |
| [getFriendList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.getfriendlist(succ:fail:)) | 获取好友列表 |
| [getFriendsInfo](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.getfriendsinfo(useridlist:succ:fail:)) | 获取指定好友资料 |
| [setFriendInfo](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.setfriendinfo(info:succ:fail:)) | 设置指定好友资料 |
| [searchFriends](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.searchfriends(searchparam:succ:fail:)) | 搜索好友列表 |
| [addFriend](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.addfriend(application:succ:fail:)) | 添加好友 |
| [deleteFromFriendList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.deletefromfriendlist(useridlist:deletetype:succ:fail:)) | 删除好友 |
| [checkFriend](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.checkfriend(useridlist:checktype:succ:fail:)) | 检查指定用户的好友关系           |
| [getFriendApplicationList](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.getfriendapplicationlist(succ:fail:)) | 获取好友申请列表                      |
| [acceptFriendApplication](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.acceptfriendapplication(application:accepttype:succ:fail:)) | 同意好友申请                                |
| [refuseFriendApplication](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.refusefriendapplication(application:succ:fail:)) | 拒绝好友申请                                |
| [deleteFriendApplication](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.deletefriendapplication(application:succ:fail:)) | 删除好友申请 |
| [setFriendApplicationRead](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.setfriendapplicationread(succ:fail:)) | 设置好友申请已读 |
| [createFriendGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.createfriendgroup(groupname:useridlist:succ:fail:)) | 新建好友分组 |
| [get​Friend​Group​List](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.getfriendgrouplist(groupnamelist:succ:fail:)) | 获取分组列表 |
| [deleteFriendGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.deletefriendgroup(groupnamelist:succ:fail:)) | 删除好友分组 |
| [renameFriendGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.renamefriendgroup(oldname:newname:succ:fail:)) | 修改好友分组的名称 |
| [addFriendsToFriendGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.addfriendstofriendgroup(groupname:useridlist:succ:fail:)) | 添加好友到一个好友分组 |
| [deleteFriendsFromFriendGroup](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.deletefriendsfromfriendgroup(groupname:useridlist:succ:fail:)) | 从好友分组中删除好友 |

