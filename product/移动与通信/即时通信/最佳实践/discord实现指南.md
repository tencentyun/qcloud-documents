## Discord 介绍

Discord 是一款专为社群设计的免费网络实时通话软件与数字发行平台，主要针对游戏玩家、教育人士、朋友及商业人士，用户之间可以在软体的聊天频道通过讯息、图片、影片和音讯进行交流。

![image-20221209174651267](https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-09-094651.png)

## Discord 概念

### 服务器

在 Discord 中有一种别于一般通讯软体之群组的群体聊天，称作伺服器（类似社团），伺服器拥有者可以在伺服器中创造属于自己的社群。

### 频道

在服务器中可以建立名为频道的聊天管道，分为语音、文字，其中的语音频道可以用来直播游戏与聊天等，频道可以设定与身份组整合各种权限，让 Discord 社群系统更加多样化

### 子区

用户可以对特定的话题在子区内进行讨论。

## 准备工作

### 创建腾讯云 IM 应用

本篇教程以腾讯云 IM 为基础展开，因此，需要在 [腾讯云 IM 控制台](https://console.cloud.tencent.com/im) 进行应用创建。如图所示：

<img src="https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-04-173643.png" alt="image-20221205013642537" style="zoom:50%;" /> 

创建应用后，在 [腾讯云 IM 控制台应用基本信息页面](https://console.cloud.tencent.com/im/detail)，查看应用基础信息。

### 了解相关配置和能力

使用腾讯云 IM 实现 Discord 相关的功能，您需要提前了解腾讯云 IM 相关的基础概念以及本教程后续会提到的一些专有名词，包括但不限于如下内容：

- SDKAppID：腾讯云 IM 会给每个应用分配一个 SDKAppID，在控制台创建应用后再应用详情页查看，开发者可以在初始化腾讯云IM客户端 SDK 和计算用户登录票据时使用。详情可参考无 UISDK [初始化](https://cloud.tencent.com/document/product/269/75291) 以及 [登录](https://cloud.tencent.com/document/product/269/75294) 文档。
- 密钥：在腾讯云 IM 控制台应用详情页可查看当前应用密钥，在计算用户登录 SDK 票据时会用到
- 用户账号：登录腾讯云 IM 用户必须在腾讯云 IM 的账号体系中，当用户使用客户端 SDK [登录](https://cloud.tencent.com/document/product/269/75294)成功时，腾讯云 IM 后台会自动创建 IM 用户。同时，可以使用腾讯云 IM 提供的服务端 API 将用户[导入到 IM 的用户体系](https://cloud.tencent.com/document/product/269/1608)中。
- 群组：到目前为止，IM根据不同场景的需要，提供了 [5种类型的群](https://cloud.tencent.com/document/product/269/1502)，用户在群里发言，群成员均可收到消息。
- 回调配置：开发者除了可以主动集成 IM 提供的客户端 SDK 与服务端 API，IM 也会主动在特定的业务逻辑出发时将必要的信息回到给开发者服务端。只需要开发者在腾讯云 IM 控制台 [回调配置](https://console.cloud.tencent.com/im/callback-setting) 模块完成相应的配置即可。腾讯云 IM 提供了丰富的回调配置，并且保证回调的高可靠，开发者可通过回调实现很多自定义需求。
- 自定义字段：默认情况下，腾讯云 IM 提供给开发者使用的字段能满足绝大部分需求，如用户需要扩展字段，腾讯云 IM 也为各个模块提供了自定一字段，如：
    - [用户自定义字段](https://console.cloud.tencent.com/im/user-data)
    - [好友自定义字段](https://console.cloud.tencent.com/im/friends-diy-vars)
    - [群自定义字段](https://console.cloud.tencent.com/im/qun-setting)
    - [群成员自定义字段](https://console.cloud.tencent.com/im/qun-setting)
  >?用户使用自定义字段，可现在控制台进行配置，再使用 SDK\API 进行读写即可。

### 集成客户端&服务端 SDK

在实现 Discord 相关的功能时，需要集成 IMSDK，腾讯云 IM 提供了丰富且易用的 SDK 以及服务端 API，使用同一 SDKAppID 登录的应用，在各个端上消息互通。开发者可根据自己的业务需求场景以及技术栈进行评估，选择合适的 SDK。

## Discord 功能分析

<img src="https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-04-181211.png" alt="image-20221205021211108" style="zoom:50%;" /> 

如上图所示，Discord 的功能主要分为服务器、频道、以及子区，服务器与服务器之间是内容上的区别，如王者荣耀服务器，和平精英服务器等，在服务器内可以创建不同类型的频道，如文字频道，语音频道、公示频道等。用户的交流实际是在各个频道中进行的。当用户对交流的某一个内容有更多的想法时，可以选择对该内容创建子区来进行更多的交流。Discord 的核心玩法就如分析的这样，接下来本教程会逐一分析如何通过腾讯云 IM 来实现相关的功能。

>?**如涉及到代码演示，本教程以 Android 端（Java SDK）为例进行展示，其他版本的SDK接口调用可参考文档 [无 UI 集成方案](https://cloud.tencent.com/document/product/269/75283) 部分。**

### 服务器

#### 创建服务器

<img src="https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-04-184623.png" alt="image-20221205024621985" style="zoom:50%;" /> 

经过分析可以知道，Discord 的服务器列表有这样一些特性：

1. 服务器中人数可能特别多。
2. 用户实际不会在服务器中交流，只会在服务器内的频道或者子区中聊天。
3. 服务器中的聊天历史需要存漫游。
4. 可自由进入。
5. 可以在服务器中创建频道。

虽然 IM 提供了五种不同类型的群，但从 Discord 的服务器特性来看，只有 [社群（Community）](https://cloud.tencent.com/document/product/269/1502) 符合服务器的特性，腾讯云 IM 社群创建后可以随意进出，最多支持10w人，支持历史消息存储，用户搜索群 ID 发起加群申请后，无需管理员审批即可进群。

可通过腾讯云 IM 提供的 createGroup 接口进行服务器（群）创建，需要注意的是，创建的群类型为Community、[setSupportTopic](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupInfo.html#af97a85fc91302dbbdf0f6c0a0a022ccd) 需要设置为 true，这样才可在服务器中创建频道。演示代码如下：

```java
V2TIMGroupInfo  groupinfo = new V2TIMGroupInfo();
groupinfo.setGroupName("测试服务器");
groupinfo.setSupportTopic(true);
// 初始群成员
List<V2TIMCreateGroupMemberInfo> memberList = new LinkedList<V2TIMCreateGroupMemberInfo>();
// 其他配置，如服务器头像等
V2TIMManager.getGroupManager().createGroup(groupinfo, memberList, new V2TIMValueCallback<String>() {
            @Override
            public void onError(int i, String s) {
                // 创建失败
            }

            @Override
            public void onSuccess(String s) {
            	// 创建成功，返回服务器ID
            }
});
```

接口调用成功后，会在 onSuccess 回调中返回服务器 ID，在后续的在服务器中创建频道的功能中会用到。

>!开发者也可以使用 IM 提供的服务端 API，[在服务端创建服务器](https://cloud.tencent.com/document/product/269/1615)。关键参数如下：
>
>```json
{
    "Type": "Community",     // 群组类型 (必填)
    "Name": "TestCommunityGroup", // 群组名称 (必填)
    "SupportTopic": 1            // 是否支持话题选项, 1代表支持,0代表不支持
}
```

###### 服务器列表

在 Discord 最左侧有个服务器列表的功能，展示的是用户已加入的服务器列表。针对与社群场景，腾讯云 IM 提供了专门的 API 进行查询

```java
V2TIMManager.getGroupManager().getJoinedCommunityList(new V2TIMValueCallback<List<V2TIMGroupInfo>>() {
            @Override
            public void onSuccess(List<V2TIMGroupInfo> v2TIMGroupInfos) {
                // 获取服务器列表成功，返回的List<V2TIMGroupInfo>代表服务器列表的基本信息
            }

            @Override
            public void onError(int i, String s) {
              // 获取服务器列表失败
            }
});
```

在返回的 [V2TIMGroupInfo](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupInfo.html) 列表，代表的是服务器的基本信息。但是在基本信息中，并没有服务器的未读数以及自定义状态等相关信息。因此想要实现 Discord 一样的效果需要借助 IM 提供的其他 API 来实现，服务器列表的未读数，在后面的小节中讲到。

#### 服务器分类

创建服务器时，会个服务器创建默认的分类，创建后也可在创建新的分类，服务器在腾讯云 IM 中本质上是一个社群，因此可以通过设置社群的自定义字段来进行实现。使用群自定义字段可分为两步：

1. 在控制台开启自定义字段 key。
2. 使用客户端 SDK\服务端 API 进行读写。

<img src="https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-05-025625.png" alt="image-20221205105625456" style="zoom:50%;" /> 

设置群自定义字段的 [服务端 API](https://cloud.tencent.com/document/product/269/1620) 以及 [客户端 SDK](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#ad4ceef92975fa00c4a5dddc8f7e1edcf)。

>!社群为旗舰版能力，设置社群的自定义字段需要先购买旗舰版。

#### 服务器消息未读数&自定义状态展示

![image-20221205031412051](https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-04-191412.png)

![image-20221205031429070](https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-04-191429.png)

上一小节提到在获取已加入的服务器列表 API 中，没有返回未读数以及服务器状态等信息。需要注意的是，我们不仅仅要获取到这个数据，还需要监听这个数据的变化从而及时的更新客户端 UI，由于服务器使用IM社群实现，且社群在 IM 中不会产生会话，因此需要统计所有公有的频道的会话以及私有的频道会话之和。通过 [V2TIMTopicInfo](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMTopicInfo.html) 的 [getUnreadCount](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMTopicInfo.html#ac2e3266d20b348145d75079020ac50c7) 获取公有频道的未读数，由于私有频道由 work 群实现所以可通过 [getConversation](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#a619aaff2bb5664e094d2341819b95096) 来获取私有频道的未读数。

```java
// 公有频道
List<String> conversationIDList = new LinkedList();
conversationIDList.add("GROUP_$GROUPID");
V2TIMManager.getConversationManager().getConversationList(conversationIDList, new V2TIMValueCallback<List<V2TIMConversation>>() {
            @Override
            public void onError(int i, String s) {
                // 获取服务器对应的会话信息失败
            }

            @Override
            public void onSuccess(V2TIMConversationList List<V2TIMConversation>) {
               // 获取服务器对应的会话信息成功
            }
});
// 私有频道
V2TIMManager.getGroupManager().getTopicInfoList(groupID, topicIDList, new V2TIMValueCallback<List<V2TIMTopicInfoResult>>() {
                @Override
                public void onSuccess(List<V2TIMTopicInfoResult> v2TIMTopicInfoResults) {
                    
                }

                @Override
                public void onError(int i, String s) {
                }
});
```

对于服务器的自定义状态功能，可以通过设置服务器会话的自定义数据来实现，对应 API 为 [setConversationCustomData](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#ac11ca7227145e3f359f6a3473ed600a5)。

```java
List<String> conversationIDList = new LinkedList();
String customData = "通话中"
V2TIMManager.getConversationManager().setConversationCustomData(conversationIDList, customData, new V2TIMValueCallback<List<V2TIMConversationOperationResult>>() {
            @Override
            public void onSuccess(List<V2TIMConversationOperationResult> v2TIMConversationOperationResults) {
                // 设置群会话自定义数据成功
            }

            @Override
            public void onError(int i, String s) {
                // 设置群会话自定义数据失败
            }
});
```

当服务器会话的相关数据发生改变时，客户端需要试试更新 UI 的展示，对于监听服务器会话的改变，IM 提供了对应的事件监听函数 [addConversationListener](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#a806534684e5d4d01b94126cd1397fee4)，当以下信息修改时，会触发该回调函数。

1. 服务器消息增删改
2. 服务器消息未读数改变
3. 服务器自定义信息改变
4. 服务器置顶
5. 服务器接受消息配置改变
6. 服务器标记改变
7. 服务器分组改变
8. ...

```java
V2TIMConversationListener conversationLister = new V2TIMConversationListener() {
            @Override
            public void onSyncServerStart() {
            }

            @Override
            public void onSyncServerFinish() {
            }

            @Override
            public void onSyncServerFailed() {
            }

            @Override
            public void onNewConversation(List<V2TIMConversation> conversationList) {
            }

            @Override
            public void onConversationChanged(List<V2TIMConversation> conversationList) {
            }
            @Override
            public void onTotalUnreadMessageCountChanged(long totalUnreadCount) {
            }

            @Override
            public void onConversationGroupCreated(String groupName, List<V2TIMConversation> conversationList) {
            }

            @Override
            public void onConversationGroupDeleted(String groupName) {
            }

            @Override
            public void onConversationGroupNameChanged(String oldName, String newName) {
            }

            @Override
            public void onConversationsAddedToGroup(String groupName, List<V2TIMConversation> conversationList) {、
            }

            @Override
            public void onConversationsDeletedFromGroup(String groupName, List<V2TIMConversation> conversationList) {
            }
}
V2TIMManager.getConversationManager().addConversationListener(conversationLister);
```

综上通过 getJoinedCommunityList、getConversationList 接口以及 addConversationListener 回调，可以实现 Discord 的展示服务器列表的功能。

### 频道

在服务器内，可创建多个频道。如图所示，在该服务器下创建了四个频道，并且将四个频道放到了两个分类中。

<img src="https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-05-013402.png" alt="image-20221205093402247" style="zoom:50%;" /> 

对于频道，用户可以邀请用户加入以及对频道进行基本的设置。用户大多数的聊天是在频道内进行的，因此频道的能力在 Discord 中是最重要的。对应于腾讯云 IM，即是话题的能力。在 IM 社群支持在在社群内创建话题的能力。

#### 默认频道

Discord 会在创建服务器时，默认创建四个频道，使用腾讯云 IM 也可以实现这样的功能，具体流程如下：

1. 使用 [创建群后回调](https://console.cloud.tencent.com/im/callback-setting) 通知业务服务端创服务器成功。
2. 业务侧判断是是否创建的社群，以免影响其他群相关的业务。
3. 根据服务器属性，[在服务端创建话题](https://cloud.tencent.com/document/product/269/78203)。

服务端创建话题主要参数如下：

```json
{
    "GroupId": "@TGS#_@TGS#cQVLVHIM62CJ", // 话题所属的群ID（必填）
    "TopicId": "@TGS#_@TGS#cQVLVHIM62CJ@TOPIC#_TestTopic",     // 用户自定义话题 ID（选填）
    "TopicName": "TestTopic",         // 话题的名称（必填）
    "From_Account": "test_user", // 创建话题的成员
    "CustomString": "This is a custom string",    // 自定义字符串
    "FaceUrl": "http://this.is.face.url", // 话题头像 URL（选填）
    "Notification": "This is topic Notification", // 话题公告（选填）
    "Introduction": "This is topic Introduction" // 话题简介（选填）
}
```

![image-20221205094226037](https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-05-014226.png)

#### 创建频道

在 Discord 客户端，用户可以在频道分类下创建频道，如图：

<img src="https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-05-014944.png" alt="image-20221205094944046" style="zoom:50%;" /> 

如上所分析，创建频道在 IM 中即为在社群中创建话题。并且在创建时，可以对话题进行分类，设置话题基本信息。

<img src="https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-05-021239.png" alt="image-20221205101238339" style="zoom:50%;" /> 

可以通过 [createTopicInCommunity](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a52eed1b07ad64a3aa3d3561d8cd147f0) 来实现相关的功能。

```java
String groupID = "服务器ID"
V2TIMTopicInfo info = new V2TIMTopicInfo();
info.setCustomString("{'categray':'游戏','type':'text'}") // 设置频道分类以及类型
// 这里可以设置V2TIMTopicInfo的具体信息
V2TIMManager.getGroupManager().createTopicInCommunity(groupID, info, new V2TIMValueCallback<String>() {
            @Override
            public void onSuccess(String s) {
                // 创建频道成功
            }

            @Override
            public void onError(int i, String s) {
                // 创建频道失败
            }
});
```

创建频道时，可以通过调用 [V2TIMTopicInfo](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMTopicInfo.html) 的成员方法来设置频道的信息，频道分类以及频道类型，可以通过 [setCustomString](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMTopicInfo.html#aad0cc8249c21c5ccae385fdfb8ba32ea)，进行设置。

<img src="https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-05-023659.png" alt="image-20221205103658717" style="zoom:50%;" /> 

在创建频道时，可设置频道是否是私密频道，私密频道和普通频道不同。

1. 用户加入服务器后，不会加入私密频道。
2. 私密频道需要服务器管理员邀请进入。

因此，我们可以使用一个 work 群来实现私密频道的功能，但是一个服务器绑定了哪些私密频道的信息需要业务侧来存储。

#### 频道类型

Discord 在创建频道时，可选择频道类型为语音频道或者文字频道，文字频道即为普通的文字、表情、图片聊天，语音频道则为音视频聊天。需要注意的是，同一用户同一时间内只能在一个语音频道内。用户加入新的语音频道需要退出当前已加入的语音频道。

<img src="https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-05-030833.png" alt="image-20221205110832673" style="zoom:50%;" /> 

因此这里有4个注意点：

1. 创建频道时需设置频道类型，在创建频道小节中有讲到如何设置频道类型。
2. 用户加入语音频道时需判断是否已经在其他语音频道。
3. 语音频道是全局的。
4. 腾讯云 IM 暂时未提供用户是否在语音频道以及在哪个语音频道的 API，因此此部分的数据需要业务侧来维护。

针对第4点，开发者可以使用腾讯云 IM 提供的进群后回调以及退群回调，维护用户是否在语音频道的状态，并且将该状态存在业务侧存储内。需要注意的是，腾讯云 IM 的回调可能存在延迟，即用户退出语音频道后，短时间内仍可能不能加入其他语音频道。因此也可以用过客户端上报的方式来处理，即将用户的进退语音频道的状态实时上报给业务服务端。

#### 邀请用户进入频道

用户进入频道有三种方式：

1. 邀请用户进入服务器，进入服务器的用户会进入所有的公开的频道。
2. 用户通过搜索进入服务器。
3. 私有频道通过服务器管理员邀请进入。

通过社群的特性可知，用户进入共有频道，只需加入服务器即可。

1. 支持精准搜索群 ID 加入。
2. 支持邀请人进入。
3. 支持主动申请进入，且无需审批。



#### 频道设置

可以对频道进行静音设置以及通知相关设置，对应的 API 为 [setAllMute](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMTopicInfo.html#a13fbe06ce357215cfd7053954552030b) 以及 [setGroupReceiveMessageOpt](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a2735427ac22485626aea278a9d465b3e)。

```java
// 设置频道基本信息
V2TIMManager.getGroupManager().setTopicInfo(topicInfo, new V2TIMCallback() {
    @Override
    public void onSuccess() {
        // 设置成功
    }

    @Override
    public void onError(int i, String s) {
        // 设置失败
    }
});
```

```java
// 设置频道如何接受消息
String groupID = "topicid"
int opt = 0; 
V2TIMManager.getMessageManager().setGroupReceiveMessageOpt(groupID, opt, new V2TIMCallback() {
    @Override
    public void onSuccess() {
        
    }

    @Override
    public void onError(int i, String s) {
        
    }
});
```

#### 频道消息列表

可通过 [getHistoryMessageList](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a97fe2d6a7bab8f45b758f84df48c0b12) 来获取频道的历史消息记录。

```java
final V2TIMMessageListGetOption option = new V2TIMMessageListGetOption();
option.setGroupID("频道ID");
option.setCount(20);
// 其他配置
V2TIMManager.getMessageManager().getHistoryMessageList(option, new V2TIMValueCallback<List<V2TIMMessage>>() {
    @Override
    public void onSuccess(List<V2TIMMessage> v2TIMMessages) {
        // 获取频道历史消息成功
    }

    @Override
    public void onError(int code, String desc) {
        // 获取频道历史消息失败
    }
});
```

#### 频道消息未读数

频道内消息未读数和服务器消息未读数不同，服务器未读数在会话信息中，而频道的未读数在频道的基本信息中，切通过腾讯云 IM 的群组回调 [onTopicInfoChanged](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupListener.html#a29285e4e127337e299bd2b695a1afdeb) 来实时获取未读数。

```java
String groupID = "服务器ID";
List< String > topicIDList= new LinkedList(); // 频道消息列表
V2TIMManager.getGroupManager().getTopicInfoList(groupID, topicIDList, new V2TIMValueCallback<List<V2TIMTopicInfoResult>>() {
    @Override
    public void onSuccess(List<V2TIMTopicInfoResult> v2TIMTopicInfoResults) {
        // 获取频道信息，如频道id、频道名字、未读数等
    }

    @Override
    public void onError(int i, String s) {
        
    }
});
```

#### 频道成员名单

加入服务器的用户默认会加入到所有的公有频道中，因此查看服务器的群成员列表即可。功能频道获取成员列表：

```java
String groupID = "服务器ID";
int filter = 0; // 群成员角色 管理员 普通成员 ...
long nextSeq = 0;// 分页参数
V2TIMManager.getGroupManager().getGroupMemberList(groupID, filter, nextSeq , new V2TIMValueCallback<V2TIMGroupMemberInfoResult>() {
    @Override
    public void onError(int i, String s) {
        CommonUtil.returnError(result,i,s);
    }

    @Override
    public void onSuccess(V2TIMGroupMemberInfoResult v2TIMGroupMemberInfoResult) {
        
    }
});
```

私有频道获取群成员列表也是调用 [getGroupMemberList](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a69fc0831aacaa0585c1855f4c91320be)，传入私有频道的群 ID 即可。

### 子区

<img src="https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-05-152729.png" alt="image-20221205232729217" style="zoom:50%;" />

子区是对于频道内消息进行进一步讨论的群组，用户可以集中浏览一个频道内用户讨论的重点，在频道内消息列表中，也可以看到子区的概要。子区在腾讯云IM里也是群的概念，一个子区即为一个群。

#### 创建子区

子区的创建可以邦迪频道内的一条消息，也可以单独创建，可以通过腾讯云 IM 提供的创建群 createGroup 接口创建子区,但需要注意以下几点：

1. 新创建的子区，服务器内的所有成员，默认都在子区内。
2. 子区创建后加入服务器的成员也都会加入到子区。
3. 后加入子区的用户能看到子区创建后的历史聊天记录。

综上，创建一个子区，需要创建群时，将服务器中群成员加入子区，用户加入服务器时，需要在用户进群后回调中，将用户加入到服务器所有子区中。这两个步骤最好是在业务服务端进行，需要用到的 API 如下：

1. 查询 [服务器中成员](https://cloud.tencent.com/document/product/269/1617)。
2. [创建群并设置群成员](https://cloud.tencent.com/document/product/269/1615)。
3. [邀请用户进群](https://cloud.tencent.com/document/product/269/1621)。

服务端回调为 [进群后回调](https://cloud.tencent.com/document/product/269/1667)。

#### 子区数量

![image-20221205234620940](https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-05-154621.png)

在频道列表中，可以获取到频道下的子区列表，因此需要绑定子区与服务器的多对一的关系。如果子区对应有历史消息，也要绑定子区与消息的一对一关系，腾讯云 IM 暂未提供绑定上述关系的能力，因此需要业务侧额外维护。通过业务提供的 HTTP 接口来获取子区的数量以及子区列表。通过发送在线消息，来实时刷新子区列表。

#### 子区概要

![image-20221205235217731](https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-05-155218.png)

当对一条消息进行创建子区时，会在消息列表中看到子区的消息概要：

1. 该子区有多少条消息。
2. 该子区中 lastMessage 的相关信息。
3. 信息需要实时显示在消息列表中。

要实现子区的消息概要能力，需要结合群内发消息后回调、以及消息编辑的能力。用户在子区发消息后，IM 服务触发发消息后回调，将相关信息同步给业务侧，业务进行消息计数，并且维护 lastMessage 相关信息，同时将信息通过消息编辑 API 保存到消息上。

### 消息相关

#### 消息反馈

消息反馈即为用户对消息进行扩展，如图所示：
<img src="https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-06-021926.png" style="width:50%"> 

因为所有有的消息类型均可以进行编辑和反馈，并且需要支持社群，因此我们建议将数据保存在 cloudCustomData 字段上，详细的的数据存储格式可以参考：

```json
{
  "reaction": {
    "simle":["user1","user2"]
  }
}
```

```java
V2TIMManager.getMessageManager().modifyMessage(modifiedMessage, new V2TIMCompleteCallback<V2TIMMessage>() {
    @Override
    public void onComplete(int i, String s, V2TIMMessage v2TIMMessage) {
        // 消息修改完成
    }
});
```

#### 消息编辑

![image-20221206102008770](https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-06-022009.png)

消息编辑与消息反馈原理一样，仅仅设置的自定义数据上有些区别，同样为了所有消息都能够适用消息编辑，建议编辑 cloudCustomData 字段，数据格式如下：

```json
{
  "isEdited": true
}
```

```java
V2TIMManager.getMessageManager().modifyMessage(modifiedMessage, new V2TIMCompleteCallback<V2TIMMessage>() {
    @Override
    public void onComplete(int i, String s, V2TIMMessage v2TIMMessage) {
        // 消息编辑完成
    }
});
```

#### 消息标注
<img src="https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-06-025114.png" style="width:60%"> 

<img src="https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-06-025141.png" style="width:60%"> 


消息标注即用户在群聊中将消息进行标注，其他用户可以看到被标注的消息。由于社群暂不支持群属性，因此这里使用自定义消息实现消息标注能力。

使用群自定义消息需要现在 [腾讯云 IM 控制台](https://console.cloud.tencent.com/im/qun-setting) 进行配置如图：

![image-20221206161541807](https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-06-081542.png)

其次进行设置：

```java
V2TIMGroupInfo info =  new V2TIMGroupInfo();
info.setCustomInfo("pin data");
V2TIMManager.getGroupManager().setGroupInfo(info, new V2TIMCallback() {
    @Override
    public void onError(int i, String s) {
        // 设置失败
    }

    @Override
    public void onSuccess() {
        // 设置成功
    }
});
```

设置成功后群成员可收到 [onMemberInfoChanged](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupListener.html#a4ac777faad07e32408ae7ef5e2e3fc86) 事件，同时，未在线的用户也可以在通过群资料获取到标注的消息内容：

```java
List< String > groupIDList = new LinkedList();
V2TIMManager.getGroupManager().getGroupsInfo(groupIDList, new V2TIMValueCallback<List<V2TIMGroupInfoResult>>() {
    @Override
    public void onError(int i, String s) {
        
    }

    @Override
    public void onSuccess(List<V2TIMGroupInfoResult> v2TIMGroupInfoResults) {
        
    }
});
```

需要注意的是，目前自定义字段只能配置在服务器上，不能配置在频道上。

#### 正在输入中状态

![WeChatWorkScreenshot_a8f0eedd-3f59-45a9-9ea2-fcfc311b5f81](https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-06-090114.png)

当好友正在输入时，其他用户端可以看见用户正在输入中的状态，如上如所示，可以使用腾讯云IM提供的在线消息提供，此消息：

1. 仅在线用户才会收到。
2. 不会存入消息漫游。

同时，为了优化性能，我们也可以有一些优化如：

- 20s之内发送给消息的用户双方才会触发正在输入中状态消息的发送。
- 同一文本消息不触发多次在线消息发送。

### 私信

私信即 Discord 用户与用户之间可以发送消息，不管用户之间是否有好友关系。

- 如果用户没有好友关系，发送消息除了需要知道用户 ID 之外，还需要在腾讯云 IM 控制台关闭 [发送消息检测](https://console.cloud.tencent.com/im/login-message) 关系链的选项，否则会发送消息失败。
- 用户也可以先通过 [addFriend](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a19d0f22aaea285e8cee85a5dd6ed9208) 接口添加好友，通过 [getFriendList](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#ae478de55db21d42b72a6c5a6a5d16624) 来获取自己的好友列表。

相关代码如下：

```java
// 添加好友
V2TIMManager.getFriendshipManager().addFriend(info, new V2TIMValueCallback<V2TIMFriendOperationResult>() {
            @Override
            public void onError(int i, String s) {
                // 添加好友失败
            }

            @Override
            public void onSuccess(V2TIMFriendOperationResult v2TIMFriendOperationResult) {
               // 添加好友成功
            }
});
```

```java
// 获取好友列表
V2TIMManager.getFriendshipManager().getFriendList(new V2TIMValueCallback<List<V2TIMFriendInfo>>() {
            @Override
            public void onError(int i, String s) {
               // 获取好友列表失败
            }

            @Override
            public void onSuccess(List<V2TIMFriendInfo> v2TIMFriendInfos) {
               // 获取好友列表成功
            }
});
```

### 个人中心

#### 在线状态
<img src="https://qcloudimg.tencent-cloud.cn/raw/796e695d65c5127f91eb512c3a35fae1.png" style="width:50%"> 

Discord 用户面板的在线状态能力，可以通过腾讯云 IM 提供的在线状态 API 来实现：

- 通过 [setSelfStatus](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a7520045679f1493c890f2b3b5eee7b84) 来设置自己的自定义在线状态，用户的自己的在线\离线状态是 IM 设置的，开发者不能更改。
- 通过 [getUserStatus](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a2428c7f87859dd85bed1730ad8d3b92a) 来获取好友的在线状态。
- 通过 [onUserStatusChanged](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSDKListener.html#a94251d1971d7b6692b3278ed0d42b73e) 来监听好友的在线状态改变。

相关代码如下：

```java
// 设置个人在线状态
V2TIMUserStatus customStatus = new V2TIMUserStatus();
V2TIMManager.getInstance().setSelfStatus(customStatus, new V2TIMCallback() {
    @Override
    public void onSuccess() {
        
    }

    @Override
    public void onError(int i, String s) {
        
    }
});
```

```java
// 获取好友在线状态
List<String> userIDList = new LinkerList();
V2TIMManager.getInstance().getUserStatus(userIDList, new V2TIMValueCallback<List<V2TIMUserStatus>>() {
    @Override
    public void onSuccess(List<V2TIMUserStatus> v2TIMUserStatuses) {
       
    }

    @Override
    public void onError(int i, String s) {
        
    }
});
```

#### 个人信息相关

个人信息相关的功能可通过腾讯云 IM 提供的资料关系链相关的 API 实现：

- 获取个人资料 [getUsersInfo](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a7ca8c0f71a9875021fc35dfcaff68d1e)。
- 设置个人资料 [setSelfInfo](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#af004ab2f1d1458de354883f1995b678a)。

```java
// 设置个人资料
final V2TIMUserFullInfo userFullInfo = new V2TIMUserFullInfo();
V2TIMManager.getInstance().setSelfInfo(userFullInfo, new V2TIMCallback() {
    @Override
    public void onError(int i, String s) {
        
    }

    @Override
    public void onSuccess() {
        
    }
});
```

```java
// 获取用户资料
List<String> userIDList = new LinkedList();
V2TIMManager.getInstance().getUsersInfo(userIDList, new V2TIMValueCallback<List<V2TIMUserFullInfo>>() {
    @Override
    public void onError(int i, String s) {
        
    }

    @Override
    public void onSuccess(List<V2TIMUserFullInfo> v2TIMUserFullInfos) {
        
    }
});
```

### 其他

#### 搜索功能

Discord 的搜索能力如下：

<img src="https://markdown-1252238885.cos.ap-guangzhou.myqcloud.com/2022-12-06-031845.png" style="width:50%"> 

腾讯云 IM 提供了丰富的搜索能力，包括：

- 搜索消息 [searchLocalMessages](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a9364c8a0c6a0899b17c0a479b8ca848a)。
- 搜索群组 [searchGroups](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a94a72082b7e2682942f35196a7e28023)。
- 搜索群成员 [searchGroupMembers](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a493fb73258019961f3ca8934ff625b0a)。
- 搜索好友 [searchFriends](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a3e657c9ec5d68a4c423a64d71f5f9c6e)。

详细的使用 API 可参考官文档 [搜索部分](https://cloud.tencent.com/document/product/269/75436)。

#### 离线推送功能

在用户离线时，腾讯云 IM 的在线消息触达不到用户，这是便需要终端设备厂商提供的离线推送能力，腾讯云 IM 接入离线推送也十分方便，详情可参见 [离线推送](https://cloud.tencent.com/document/product/269/75428)。

#### 敏感词校验

在发送信息、配置资料时，需要对内容进行过滤，腾讯云IM也提供了这样的方案，帮助用户更加合规的使用 IM，详情可参见 [内容安全过滤](https://cloud.tencent.com/document/product/269/78633)。
