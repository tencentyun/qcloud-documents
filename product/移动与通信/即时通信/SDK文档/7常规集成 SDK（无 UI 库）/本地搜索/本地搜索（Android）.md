从增强版5.4.666版本开始支持本地搜索。使用前需要购买旗舰版套餐包，请参见 [购买指引](https://cloud.tencent.com/document/product/269/32458)。

## 功能展示
搜索接口的界面分为以下部分，最上面是搜索好友，中间部分是搜索群组、群成员，最下面是搜索消息且按照会话分组。
您可通过 [下载安装应用](https://cloud.tencent.com/document/product/269/36852) 即刻体验，其使用效果如下：
![](https://im.sdk.qcloud.com/tools/resource/search.gif)

## 对接指引
### 方案一、对接 TUIKit 搜索源码
#### 步骤1：购买套餐包
请单击前往 [购买旗舰版套餐包](https://cloud.tencent.com/document/product/269/32458)。
#### 步骤2：下载源码
[下载源码](https://github.com/tencentyun/TIMSDK) 集成 tuikit module。TUIKit 从5.4.666版本开始支持本地搜索。
```
implementation project(':tuikit')
```
#### 步骤3：初始化 TUIKit 并登录

```
// 初始化
TUIKitConfigs configs = TUIKit.getConfigs();
TUIKit.init(this, SDKAPPID, configs);
// 登录
TUIKit.login(userID, userSig, new IUIKitCallBack() {
@Override
public void onSuccess(Object data) {
    // 登录成功
}

@Override
public void onError(String module, final int code, final String desc) {
    // 登录失败
}
});
```

#### 步骤4：启动搜索界面
启动 `SearchMainActivity` 即可。

### 方案二、对接 IM SDK 搜索接口
#### 步骤1：购买套餐包
请单击前往 [购买旗舰版套餐包](https://cloud.tencent.com/document/product/269/32458)。
#### 步骤2：集成增强版 IM SDK
从5.4.666版本开始支持本地搜索。

```
dependencies {
  api 'com.tencent.imsdk:imsdk-plus:版本号'
}
```

#### 步骤3：调用搜索本地用户资料接口
调用接口 [searchFriends](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a815b7c4ff79f1441ee1416ff679eda6a) 可以搜索本地用户资料，支持搜索 [userID](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendSearchParam.html#ae2ee7265c0c966aa5a4e5200bf40b7d2)、[nickName](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendSearchParam.html#a1463093770c45df5fca39bdca9103980)、[remark](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendSearchParam.html#a09a945c5cb71a13de5e32c80491363fd) 字段。效果如下：
![](https://main.qcloudimg.com/raw/7a973cd30c63bed2c0a6745ddb8cf670.png)

#### 步骤4：调用搜索本地群组和群成员接口

| 图1：搜索群组 | 图2：搜索更多群组 |
|---------|---------|
| ![](https://main.qcloudimg.com/raw/70768e7f9aa8cb8c9c30cd9cc78b21a6.png) | ![](https://main.qcloudimg.com/raw/e1256f6579a4f98c3bd1e331e4c4bb07.png) |

调用接口 [searchGroups](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a94a72082b7e2682942f35196a7e28023) 可以搜索本地群组资料。
调用接口 [searchGroupMembers](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a493fb73258019961f3ca8934ff625b0a) 可以搜索本地群成员资料，根据 [V2TIMGroupMemberSearchParam](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupMemberSearchParam.html) 中的 `groupIDList` 是否为 `null`，分为两种情况：
- 如果设置 groupIDList == null，代表搜索全部群中的群成员，返回的结果会按照 groupID 进行分类；
- 如果设置 groupIDList != null，代表搜索指定群中的群成员。

#### 步骤5：调用搜索本地消息接口
在搜索框输入关键字可以调用 [searchLocalMessages](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a9364c8a0c6a0899b17c0a479b8ca848a) 搜索本地消息。根据搜索参数 [V2TIMMessageSearchParam](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchParam.html) 中的 [conversationID](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchParam.html#ad0beca2cedf96a08d1e44709c16105d7) 是否为 `null`，分为两种情况：
- 如果设置 conversationID == null，代表搜索全部会话，返回的结果会按照消息所属的会话进行分类。
- 如果设置 conversationID != null，代表搜索指定会话。

界面的展示通常分为如下图的几个场景：

| 图1：搜索聊天记录 | 图2：搜索更多聊天记录 | 图3：搜索指定会话的消息 |
|---------|---------|---------|
| ![](https://main.qcloudimg.com/raw/dbd1a42199b1ec31bb620d42558f58bc.png) | ![](https://main.qcloudimg.com/raw/97382a01f71299da55c729d8d7cbc56f.png) | ![](https://main.qcloudimg.com/raw/1619faf73d148ab0447b1cb38bdef29c.png) |

**展示最近几个活跃的会话**
如图1所示，最下方是搜索到的消息所属的最近3个会话列表，实现方式如下：
- 搜索参数 [V2TIMMessageSearchParam](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchParam.html) 中的 [conversationID](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchParam.html#ad0beca2cedf96a08d1e44709c16105d7) 设置为 `null` 表示搜索所有会话的消息，[pageIndex](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchParam.html#ad5e6b317d430d9e0cda8221a5fff6b19) 设置为0表示搜索到的消息所属的会话的第0页数据，[pageSize](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchParam.html#a3aca5a82692437f0fb8501533b9f0063) 则表示返回最近的会话数量，UI 上一般显示3条。
- 在搜索回调结果 [V2TIMMessageSearchResult](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchResult.html) 中的 [totalCount](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchResult.html#a97f66183ea41a7c123bab9dd5313a74a) 表示匹配到的消息所属的所有会话数量；[messageSearchResultItems](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchResult.html#a6cc0e2f70f0695a74a18a219c31b3ae3) 为最近 [pageSize](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchParam.html#a3aca5a82692437f0fb8501533b9f0063) 个会话信息。其中 [V2TIMMessageSearchResultItem](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchResultItem.html) 的 [conversationID](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchResultItem.html#ae599509f3d5e39bbcfb176b8976ff620) 表示会话 ID；[messageCount](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchResultItem.html#a41300a43e3530ab3ba00b61f4337a083) 表示当前会话搜索到的消息总数量；[messageList](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchResultItem.html#aceeced8f371a986511be5c63de354587) 则有两种表现：
	- 如果搜索到的消息条数 > 1，则 `messageList` 为空，您可以在 UI 上显示“messageCount 条相关聊天记录”；
	- 如果搜索到的消息条数 = 1，则 `messageList` 为匹配到的那条消息，您可以在 UI 上显示消息内容并高亮搜索关键词例如图中的“test”。

**示例**

```
List<String> keywordList = new ArrayList<>();
keywordList.add("test");
V2TIMMessageSearchParam v2TIMMessageSearchParam = new V2TIMMessageSearchParam();
// conversationID 设置为 null 表示搜索所有会话中的消息，结果会按照会话分类
v2TIMMessageSearchParam.setConversationID(null);
v2TIMMessageSearchParam.setKeywordList(keywordList);
v2TIMMessageSearchParam.setPageSize(3);
v2TIMMessageSearchParam.setPageIndex(0);
V2TIMManager.getMessageManager().searchLocalMessages(v2TIMMessageSearchParam, new V2TIMValueCallback<V2TIMMessageSearchResult>() {
    @Override
    public void onSuccess(V2TIMMessageSearchResult v2TIMMessageSearchResult) {
        // 匹配到的消息所属的所有会话数量
        int totalCount = v2TIMMessageSearchResult.getTotalCount();
        // 最近3个根据消息会话分类的信息
        List<V2TIMMessageSearchResultItem> resultItemList = v2TIMMessageSearchResult.getMessageSearchResultItems();
        for (V2TIMMessageSearchResultItem resultItem : resultItemList) {
            // 会话 ID
            String conversationID = resultItem.getConversationID();
            // 该会话匹配到的所有消息数量
            int totalMessageCount = resultItem.getMessageCount();
            // 消息列表：如果 totalMessageCount > 1，该列表为空；如果 totalMessageCount = 1，该列表元素为此消息
            List<V2TIMMessage> v2TIMMessageList = resultItem.getMessageList();
        }
    }

    @Override
    public void onError(int code, String desc) {}
```

**展示所有搜索到的消息所属的会话列表**
例如点击图1中的“更多聊天记录”跳转到图2来展示所有搜索到的消息所属的会话列表，其中的搜索参数和搜索结果描述跟上面的场景类似。为了防止内存膨胀，强烈建议对会话列表分页加载。比如您希望每页展示10条会话结果，搜索参数 [V2TIMMessageSearchParam](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchParam.html) 可以参考如下设置：
- 首次调用：设置参数 pageSize = 10，pageIndex = 0，调用 [searchLocalMessages](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a9364c8a0c6a0899b17c0a479b8ca848a) 从结果回调中的 totalCount 可以获取会话总数量；
- 计算页数：totalPage = (totalCount % pageSize == 0) ? (totalCount / pageSize) : (totalCount / pageSize + 1) 。
- 再次调用：可以通过指定参数 pageIndex（pageIndex < totalPage）返回后续页号的结果

**示例**

```
......
// 每页展示数量为10条，计算总页数
int totalPage = (totalCount % 10 == 0) ? (totalCount / 10) : (totalCount / 10 + 1);
......

private void searchConversation(int index) {
    if (index >= totalPage) {
        return;
    }
    List<String> keywordList = new ArrayList<>();
    keywordList.add("test");
    V2TIMMessageSearchParam v2TIMMessageSearchParam = new V2TIMMessageSearchParam();
    v2TIMMessageSearchParam.setConversationID(null);
    v2TIMMessageSearchParam.setKeywordList(keywordList);
    v2TIMMessageSearchParam.setPageSize(10);
    v2TIMMessageSearchParam.setPageIndex(index);
    V2TIMManager.getMessageManager().searchLocalMessages(v2TIMMessageSearchParam, new V2TIMValueCallback<V2TIMMessageSearchResult>() {
        @Override
        public void onSuccess(V2TIMMessageSearchResult v2TIMMessageSearchResult) {
					// 匹配到的消息所属的所有会话数量
					int totalCount = v2TIMMessageSearchResult.getTotalCount();
					// 每页展示数量为10条，计算总页数
					int totalPage = (totalCount % 10 == 0) ? (totalCount / 10) : (totalCount / 10 + 1);
					// 该页的根据消息会话分类的信息
					List<V2TIMMessageSearchResultItem> resultItemList = v2TIMMessageSearchResult.getMessageSearchResultItems();
					for (V2TIMMessageSearchResultItem resultItem : resultItemList) {
						// 会话 ID
						String conversationID = resultItem.getConversationID();
						// 该会话匹配到的所有消息数量
						int totalMessageCount = resultItem.getMessageCount();
						// 消息列表：如果 totalMessageCount > 1，该列表为空；如果 totalMessageCount = 1，该列表元素为此消息
						List<V2TIMMessage> v2TIMMessageList = resultItem.getMessageList();
					}

				@Override
				public void onError(int code, String desc) {}
    });
}

// 当需要加载下一页时
public void loadMore() {
    searchConversation(++pageIndex);
}
```

**搜索指定会话中的消息**
与图2展示会话列表不同的是，图3所示为在指定会话中搜索的消息列表。为了防止内存膨胀，强烈建议对消息列表分页加载。实现方式如下：
- 搜索参数 [V2TIMMessageSearchParam](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchParam.html) 中的 [conversationID](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchParam.html#ad0beca2cedf96a08d1e44709c16105d7) 设置为搜索的会话 ID，[pageIndex](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchParam.html#ad5e6b317d430d9e0cda8221a5fff6b19) 和 [pageSize](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchParam.html#a3aca5a82692437f0fb8501533b9f0063) 参考上述计算方式设置分页参数；
- 搜索结果 [V2TIMMessageSearchResult](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchResult.html) 中的 [totalCount](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchResult.html#a97f66183ea41a7c123bab9dd5313a74a) 表示该会话匹配到的所有消息数量；[messageSearchResultItems](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchResult.html#a6cc0e2f70f0695a74a18a219c31b3ae3) 列表只有该会话的结果。其中 [V2TIMMessageSearchResultItem](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchResultItem.html) 的 [messageCount](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchResultItem.html#a41300a43e3530ab3ba00b61f4337a083) 为该分页的消息数量，[messageList](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchResultItem.html#aceeced8f371a986511be5c63de354587) 为该分页的消息列表。

**示例**

```
......
// 每页展示数量为10条，计算总页数
int totalMessagePage = (totalMessageCount % 10 == 0) ? (totalMessageCount / 10) : (totalMessageCount / 10 + 1);
......

private void searchMessage(int index) {
	if (index >= totalMessagePage) {
			return;
	}
	List<String> keywordList = new ArrayList<>();
	keywordList.add("test");
	V2TIMMessageSearchParam v2TIMMessageSearchParam = new V2TIMMessageSearchParam();
	v2TIMMessageSearchParam.setConversationID(conversationID);
	v2TIMMessageSearchParam.setKeywordList(keywordList);
	v2TIMMessageSearchParam.setPageSize(10);
	v2TIMMessageSearchParam.setPageIndex(index);
	V2TIMManager.getMessageManager().searchLocalMessages(v2TIMMessageSearchParam, new V2TIMValueCallback<V2TIMMessageSearchResult>() {
			@Override
			public void onSuccess(V2TIMMessageSearchResult v2TIMMessageSearchResult) {
				// 该会话匹配到的所有消息数量
				int totalMessageCount = v2TIMMessageSearchResult.getTotalCount();
				// 每页展示数量为10条，计算总页数
				int totalMessagePage = (totalMessageCount % 10 == 0) ? (totalMessageCount / 10) : (totalMessageCount / 10 + 1);
				// 该页消息信息
				List<V2TIMMessageSearchResultItem> resultItemList = v2TIMMessageSearchResult.getMessageSearchResultItems();
				for (V2TIMMessageSearchResultItem resultItem : resultItemList) {
					// 会话 ID
					String conversationID = resultItem.getConversationID();
					// 该页的消息数量
					int totalMessageCount = resultItem.getMessageCount();
					// 该页的消息数据列表
					List<V2TIMMessage> v2TIMMessageList = resultItem.getMessageList();
			}

			@Override
			public void onError(int code, String desc) {
			}
	});
}

// 当需要加载下一页时
public void loadMore() {
    searchMessage(++pageIndex);
}
```

## 常见问题
### 1、如何搜索自定义消息
需要使用接口 [createCustomMessage (byte[] data, String description, byte[] extension)](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a313b1ea616f082f535946c83edd2cc7f) 来创建并发送，把需要搜索的文本放到 `description` 参数中。而使用接口 [createCustomMessage (byte[] data)](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a5c2495d4b7ecd66e5636aeb865c17efd) 创建的自定义消息由于本地保存的是参数传的二进制数据流，因此无法被搜索到。
如果您配置了离线推送功能，参数 `description` 设置后，自定义消息也会有离线推送且通知栏展示该参数内容。如果不需要离线推送可以用发消息接口 [sendMessage](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a28e01403acd422e53e999f21ec064795) 的参数 [V2TIMOfflinePushInfo](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html) 中的 [disablePush](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#a5d0ea30668513f45eda447875528b9c7) 来控制；如果推送的通知栏内容不想展示为被搜索的文本，可以用参数  [V2TIMOfflinePushInfo](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html) 中的 [setDesc](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#a78c8e202aa4e0859468ce40bde6fd602) 来另外设置推送内容。

### 2、如何搜索富媒体消息
富媒体消息包含文件、图片、语音、视频消息。
对于文件消息，界面通常显示文件名，因此创建时可以设置 `fileName` 参数，作为被搜索的内容，如果 `fileName` 不设置则会从 `filePath` 提取文件名，并且都会保存到本地和服务器。
而对于图片、语音、视频消息，界面通常显示缩略图或时长，可以指定消息类型做分类搜索，但不能通过关键字搜索。
