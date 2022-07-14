## 功能展示
其功能效果可参见 [Android SDK Tuikit](https://cloud.tencent.com/document/product/269/56936)。

## 对接指引
### 步骤1：购买套餐包
请将套餐升级到旗舰版，请参见  [购买指引](https://cloud.tencent.com/document/product/269/32458)。

### 步骤2：调用搜索本地用户资料接口
调用接口 [searchFriends](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_friendship_manager/V2TIMFriendshipManager/searchFriends.html) 可以搜索本地用户资料，其中的接口参数 [searchParams](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_friend_search_param/V2TimFriendSearchParam-class.html) 支持搜索`nickName、userID、remark`字段。可以使用此接口实现好友搜索功能，如昵称搜索等。

```dart
 V2TimFriendSearchParam searchParam = new V2TimFriendSearchParam(
        keywordList: ["你的关键字"],
        isSearchUserID: true,  // 搜索中是否包括userId
        isSearchNickName: true, // 搜索中是否包括nickName
        isSearchRemark: true); // 搜索中是否包括remark
    var res = await TencentImSDKPlugin.v2TIMManager
        .getFriendshipManager()
        .searchFriends(searchParam: searchParam);
```

### 步骤3：调用搜索本地群组和群成员接口

调用接口 [searchGroups](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/searchGroups.html) 可以搜索本地群组资料。
调用接口 [searchGroupMembers](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_group_manager/V2TIMGroupManager/searchGroupMembers.html) 可以搜索本地群成员资料，根据 [V2TimGroupMemberSearchParam](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_group_member_search_param/V2TimGroupMemberSearchParam-class.html) 中的 `groupIDList` 是否为 `null`，分为两种情况：
- 如果设置 groupIDList == null，代表搜索全部群中的群成员，返回的结果会按照 groupID 进行分类；
- 如果设置 groupIDList != null，代表搜索指定群中的群成员。


### 步骤4：调用搜索本地消息接口
在搜索框输入关键字可以调用 [searchLocalMessages](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/searchLocalMessages.html) 搜索本地消息。根据搜索参数 [V2TIMMessageSearchParam](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message_search_param/V2TimMessageSearchParam-class.html) 中的 [conversationID](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message_search_param/V2TimMessageSearchParam/conversationID.html) 是否为 `null`，分为两种情况：
- 如果设置 conversationID == null，代表搜索全部会话，返回的结果会按照消息所属的会话进行分类。
- 如果设置 conversationID != null，代表搜索指定会话。   

**展示最近几个活跃的会话**
搜索到的消息所属的最近会话列表，实现方式如下：
- 搜索参数 [V2TimMessageSearchParam](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message_search_param/V2TimMessageSearchParam-class.html) 中的 [conversationID](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message_search_param/V2TimMessageSearchParam/conversationID.html) 设置为 `null` 表示搜索所有会话的消息，[pageIndex](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message_search_param/V2TimMessageSearchParam/pageIndex.html) 设置为0表示搜索到的消息所属的会话的第0页数据，[pageSize](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message_search_param/V2TimMessageSearchParam/pageSize.html) 则表示返回最近的会话数量。
- 在搜索回调结果 [V2TimMessageSearchResult](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message_search_result/V2TimMessageSearchResult-class.html) 表示匹配到的消息所属的所有会话数量；[messageSearchResultItems](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message_search_result/V2TimMessageSearchResult/messageSearchResultItems.html) 为最近 [pageSize](ttps://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message_search_param/V2TimMessageSearchParam/pageSize.html) 个会话信息。其中 [V2TimMessageSearchResultItem](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message_search_result_item/V2TimMessageSearchResultItem-class.html) 表示会话 ID；messageCount 表示当前会话搜索到的消息总数量；messageList 在进行`全部会话`搜索时则有两种表现：
	- 如果搜索到的消息条数 > 1，则 `messageList` 为空，您可以在 UI 上显示“messageCount 条相关聊天记录”；
	- 如果搜索到的消息条数 = 1，则 `messageList` 为匹配到的那条消息，您可以在 UI 上显示消息内容并高亮搜索关键词例如图中的“test”。
messageList 在进行`特定会话`搜索时则会表搜索到本会话中所有满足搜索条件的消息列表。

**示例**

```dart
    V2TimMessageSearchParam searchParam = V2TimMessageSearchParam(
      keywordList: [keyword],
      type:1, // 对应 V2TIMKeywordListMatchType.KEYWORD_LIST_MATCH_TYPE_AND sdk层处理  代表 或 与关系
      pageSize: 50, 
      pageIndex: 0, 
      conversationID: null, // 不传代表指定所有会话
    );
    V2TimValueCallback<V2TimMessageSearchResult> res = await TencentImSDKPlugin.v2TIMManager
        .getMessageManager()
        .searchLocalMessages(searchParam: searchParam);
```

**展示所有搜索到的消息所属的会话列表**
![](https://qcloudimg.tencent-cloud.cn/raw/9329201c0ce22f251c31930b53472102.png)
例如单击图1中的“更多聊天记录”跳转到图2来展示所有搜索到的消息所属的会话列表，其中的搜索参数和搜索结果描述跟上面的场景类似。为了防止内存膨胀，强烈建议对会话列表分页加载。例如您希望每页展示10条会话结果，搜索参数 [V2TIMMessageSearchParam](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message_search_param/V2TimMessageSearchParam-class.html) 可以参见如下设置：
- 首次调用：设置参数 pageSize = 10，pageIndex = 0，调用 [searchLocalMessages](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/searchLocalMessages.html) 从结果回调中的 totalCount 可以获取会话总数量；
- 计算页数：totalPage = (totalCount % pageSize == 0) ? (totalCount / pageSize) : (totalCount / pageSize + 1) 。
- 再次调用：可以通过指定参数 pageIndex（pageIndex < totalPage）返回后续页号的结果

  

**示例**

```dart
......
static int totalCount = 0;
int index = 0;
// 每页展示数量为10条，计算总页数
 double totalPage = (totalCount % 10 == 0) ? (totalCount / 10) : (totalCount / 10 + 1);
......
    searchLocaltMessage(int index) async {
    if (index >= totalPage) {
      return;
    }

    V2TimMessageSearchParam searchParam = V2TimMessageSearchParam(
      keywordList: ["你的keyword"],
      type:
          1, // 对应 V2TIMKeywordListMatchType.KEYWORD_LIST_MATCH_TYPE_AND sdk层处理  代表 或 与关系
      pageSize: 10,
      pageIndex: index,
      conversationID: null, // 不传代表指定所有会话
    );
    V2TimValueCallback<V2TimMessageSearchResult> res = await TencentImSDKPlugin
        .v2TIMManager
        .getMessageManager()
        .searchLocalMessages(searchParam: searchParam);
    // 该会话匹配到的所有消息数量
    totalCount = res.data?.totalCount ?? 0;
    List<V2TimMessageSearchResultItem> list =
        res.data!.messageSearchResultItems!;
    totalPage =
        (totalCount % 10 == 0) ? (totalCount / 10) : (totalCount / 10 + 1);
    for (V2TimMessageSearchResultItem resultItem in list) {
      // 会话 ID
      String conversationID = resultItem.conversationID!;
      // 该会话匹配到的所有消息数量
      int totalMessageCount = resultItem.messageCount!;
      // 消息列表：如果 totalMessageCount > 1，该列表为空；如果 totalMessageCount = 1，该列表元素为此消息
      List<V2TimMessage> v2TIMMessageList = resultItem.messageList!;
      // ...
    }
  }

  void loadMore() {
    index = index++;
    searchLocaltMessage(index);
  }

```

**搜索指定会话中的消息**
现在我们来介绍如何搜索指定会话中的消息。为了防止内存膨胀，强烈建议对消息列表分页加载。实现方式如下：
- 搜索参数 [V2TimMessageSearchParam](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message_search_param/V2TimMessageSearchParam-class.html) 中的 `conversationID` 设置为搜索的会话 ID，`pageIndex` 和 `pageSize` 参见上述计算方式设置分页参数；
- 搜索结果 [V2TimMessageSearchResult](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message_search_result/V2TimMessageSearchResult-class.html) 中的 `totalCount`表示该会话匹配到的所有消息数量；[messageSearchResultItems](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message_search_result/V2TimMessageSearchResult/messageSearchResultItems.html) 列表只有该会话的结果。其中 [V2TIMMessageSearchResultItem](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_message_search_result_item/V2TimMessageSearchResultItem-class.html) 的 `messageCount` 为该分页的消息数量，`messageList` 为该分页的消息列表。

**示例**

```dart
......
static int totalCount = 0;
int index = 0;
// 每页展示数量为10条，计算总页数
 double totalPage = (totalCount % 10 == 0) ? (totalCount / 10) : (totalCount / 10 + 1);
......
    searchLocaltMessage(int index) async {
    if (index >= totalPage) {
      return;
    }

    V2TimMessageSearchParam searchParam = V2TimMessageSearchParam(
      keywordList: ["你的keyword"],
      type:
          1, // 对应 V2TIMKeywordListMatchType.KEYWORD_LIST_MATCH_TYPE_AND sdk层处理  代表 或 与关系
      pageSize: 10,
      pageIndex: index,
      conversationID: "传入你要搜索的conversationID", // 指定conversationID
    );
    V2TimValueCallback<V2TimMessageSearchResult> res = await TencentImSDKPlugin
        .v2TIMManager
        .getMessageManager()
        .searchLocalMessages(searchParam: searchParam);
    // 该会话匹配到的所有消息数量
    totalCount = res.data?.totalCount ?? 0;
    List<V2TimMessageSearchResultItem> list =
        res.data!.messageSearchResultItems!;
    totalPage =
        (totalCount % 10 == 0) ? (totalCount / 10) : (totalCount / 10 + 1);
    for (V2TimMessageSearchResultItem resultItem in list) {
      // 会话 ID
      String conversationID = resultItem.conversationID!;
      // 该会话匹配到的所有消息数量
      int totalMessageCount = resultItem.messageCount!;
      // 消息列表：如果 totalMessageCount > 1，该列表为空；如果 totalMessageCount = 1，该列表元素为此消息
      List<V2TimMessage> v2TIMMessageList = resultItem.messageList!;
      // ...
    }
  }

  void loadMore() {
    index = index++;
    searchLocaltMessage(index);
  }

```

## 常见问题
### 1. 如何搜索自定义消息
需要使用接口 [createCustomMessage({required String data,String desc,String extension})](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createCustomMessage.html) 来创建并发送，把需要搜索的文本放到 `desc` 参数中。而使用接口 [createCustomMessage (required String data)](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/createCustomMessage.html) 创建的自定义消息由于本地保存的是参数传的二进制数据流，因此无法被搜索到。
如果您配置了离线推送功能，参数 `description` 设置后，自定义消息也会有离线推送且通知栏展示该参数内容。如果不需要离线推送可以用发消息接口 [sendMessage](https://pub.dev/documentation/tencent_im_sdk_plugin/latest/manager_v2_tim_message_manager/V2TIMMessageManager/sendMessage.html) 的参数 [V2TIMOfflinePushInfo](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_offline_push_info/V2TimOfflinePushInfo-class.html) 中的 [disablePush](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_offline_push_info/V2TimOfflinePushInfo/disablePush.html) 来控制；如果推送的通知栏内容不想展示为被搜索的文本，可以用参数  [V2TIMOfflinePushInfo](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_offline_push_info/V2TimOfflinePushInfo-class.html) 中的 [desc](https://pub.dev/documentation/tencent_im_sdk_plugin_platform_interface/latest/models_v2_tim_offline_push_info/V2TimOfflinePushInfo/desc.html) 来另外设置推送内容。

### 2. 如何搜索富媒体消息
富媒体消息包含文件、图片、语音、视频消息。
对于文件消息，界面通常显示文件名，因此创建时可以设置 `fileName` 参数，作为被搜索的内容，如果 `fileName` 不设置则会从 `filePath` 提取文件名，并且都会保存到本地和服务器，需要注意的是在 Web 无法搜索文件，而对于图片、语音、视频消息，界面通常显示缩略图或时长，可以指定消息类型做分类搜索，但不能通过关键字搜索。
