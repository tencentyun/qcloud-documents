## 消息发送
### 通用消息发送
**会话获取：**指面向一个人或者一个群组的对话，通过与单个人或群组之间会话收发消息，发消息时首先需要先获取会话，获取会话需要指定会话类型（群组或者单聊），以及会话对方标志（对方帐号或者群号）。获取会话由 `getConversation` 实现。

**原型：**
```
public TIMConversation getConversation(TIMConversationType type, String peer)
```

**参数说明：**

参数|说明
---|---
type | 会话类型，如果是单聊，填写 TIMConversationType.C2C，如果是群聊，填写 TIMConversationType.Group。
peer | 会话标识，单聊情况下为对方帐号 identifier，群聊情况下为群组 ID。

**示例：**

```
//获取单聊会话
String peer = "sample_user_1";  //获取与用户 "sample_user_1" 的会话
conversation = TIMManager.getInstance().getConversation(
        TIMConversationType.C2C,    //会话类型：单聊
        peer);                      //会话对方用户帐号//对方 ID
//获取群聊会话
String groupId = "TGID1EDABEAEO";  //获取与群组 "TGID1LTTZEAEO" 的会话

conversation = TIMManager.getInstance().getConversation(
        TIMConversationType.Group,      //会话类型：群组
        groupId);                       //群组 ID
```

**消息发送：**通过 `TIMManager` 获取会话 `TIMConversation` 后，可发送消息和获取会话缓存消息。ImSDK 中消息的解释可参阅（[ImSDK 对象简介](/doc/product/269/概述（Android%20SDK）#2.1-imsdk对象简介))。ImSDK 中的消息由 `TIMMessage` 表达， 一个 `TIMMessage` 由多个 `TIMElem` 组成，每个 `TIMElem` 可以是文本和图片，也就是说每一条消息可包含多个文本和多张图片。发消息通过 `TIMConversation` 的成员 `sendMessage` 实现。
![](//avc.qcloud.com/wiki2.0/im/imgs/20151013075817_75666.png)

**原型：**

```
public void sendMessage(TIMMessage msg,
               TIMValueCallBack<TIMMessage> callback)
```

**参数说明：**

参数|说明
---|---
msg | 要发送的消息
callback | 回调

### 文本消息发送
文本消息由 `TIMTextElem` 定义。

**TIMTextElem 成员方法：**
```
//获取文本内容
java.lang.String    getText()

//设置文本内容，text 传递需要发送的文本消息
void    setText(java.lang.String text)
```

**示例：**
```
//构造一条消息
TIMMessage msg = new TIMMessage();
//添加文本内容
TIMTextElem elem = new TIMTextElem();
elem.setText("a new msg");
//将 Elem 添加到消息
if(msg.addElement(elem) != 0) {
   Log.d(tag, "addElement failed");
   return;
}
//发送消息
conversation.sendMessage(msg, new TIMValueCallBack<TIMMessage>() {//发送消息回调
    @Override
    public void onError(int code, String desc) {//发送消息失败
        //错误码 code 和错误描述 desc，可用于定位请求失败原因
        //错误码 code 含义请参见错误码表
        Log.d(tag, "send message failed. code: " + code + " errmsg: " + desc);
    }
    @Override
    public void onSuccess(TIMMessage msg) {//发送消息成功
        Log.e(tag, "SendMsg ok");
    }
});
```

### 图片消息发送
图片消息由 `TIMImageElem` 定义。它是 `TIMElem` 的一个子类，也就是说图片也是消息的一种内容。 发送图片的过程，就是将 `TIMImageElem` 加入到 `TIMMessage` 中，然后随消息一起发送出去。

>注：
>- 存储要发送的图片路径，必须是本地路径。
>- 发送时不用关注，接收时保存生成的图片所有规格。
>- 发送图片时，只需要设置图片路径 `path`。发送成功后可通过 `imageList` 获取所有图片类型。
>- `path` 不支持 `file://` 开头的文件路径，需要去掉 `file://` 前缀。
>- `TIMImage` 存储了图片列表的类型，大小，宽高信息，如需要图片二进制数据，需通过 `getImage` 接口下载。

**`TIMImageElem` 成员方法：**

```
public void setPath(String path)
java.util.ArrayList<TIMImage> getImageList()
```

**`TIMImage` 成员方法：**

```
//获取图片高度
long    getHeight()
//获取图片大小
long    getSize()
//获取图片类型
TIMImageType    getType()
//获取 uuid
java.lang.String    getUuid()
//获取图片宽度
long    getWidth()
//获取图片，callback 的 OnSuccess 接口中将返回图片二进制数据
void    getImage(TIMValueCallBack<byte[]> callback)
//获取图片，存放于 path 指向的文件中
void    getImage(final String path, final TIMCallBack cb)
```

**示例：**

```
//构造一条消息
TIMMessage msg = new TIMMessage();
//添加图片
TIMImageElem elem = new TIMImageElem();
elem.setPath(Environment.getExternalStorageDirectory() + "/DCIM/Camera/1.jpg");
//将 Elem 添加到消息
if(msg.addElement(elem) != 0) {
    Log.d(tag, "addElement failed");
    return;
}
//发送消息
conversation.sendMessage(msg, new TIMValueCallBack<TIMMessage>() {//发送消息回调
    @Override
    public void onError(int code, String desc) {//发送消息失败
        //错误码 code 和错误描述 desc，可用于定位请求失败原因
        //错误码 code 列表请参见错误码表
        Log.d(tag, "send message failed. code: " + code + " errmsg: " + desc);
    }
    @Override
    public void onSuccess(TIMMessage msg) {//发送消息成功
        Log.e(tag, "SendMsg ok");
    }
});
```

### 表情消息发送
表情消息由 `TIMFaceElem` 定义，SDK 并不提供表情包，如果开发者有表情包，可使用 `index` 存储表情在表情包中的索引，由用户自定义，或者直接使用 `data` 存储表情二进制信息以及字符串 `key`，都由用户自定义，SDK 内部只做透传。

**`TIMFaceElem` 成员方法：**

```
// 获取表情自定义数据
byte[]  getData()
// 获取表情索引
int getIndex()
// 设置表情自定义数据
void    setData(byte[] data)
// 设置表情索引
void    setIndex(int index)
```

**示例：**

```
//构造一条消息
TIMMessage msg = new TIMMessage();
//添加表情
TIMFaceElem elem = new TIMFaceElem();
elem.setData(sampleByteArray); //自定义 byte[]
elem.setIndex(10);   //自定义表情索引
//将 Elem 添加到消息
if(msg.addElement(elem) != 0) {
    Log.d(tag, "addElement failed");
    return;
}
//发送消息
conversation.sendMessage(msg, new TIMValueCallBack<TIMMessage>() {//发送消息回调
    @Override
    public void onError(int code, String desc) {//发送消息失败
        //错误码 code 和错误描述 desc，可用于定位请求失败原因
        //错误码 code 含义请参见错误码表
        Log.d(tag, "send message failed. code: " + code + " errmsg: " + desc);
    }
    @Override
    public void onSuccess(TIMMessage msg) {//发送消息成功
        Log.e(tag, "SendMsg ok");
    }
});
```

### 语音消息发送

语音消息由 `TIMSoundElem` 定义，其中 `data` 存储语音数据，语音数据需要提供时长信息，以秒为单位，**注意，一条消息只能有一个语音 `Elem`，添加多条语音 `Elem` 时，`AddElem` 函数返回错误 1，添加不生效，另外，语音和文件 `Elem` 不一定会按照添加时的顺序获取，建议逐个判断 `Elem` 类型展示，而且语音和文件 `Elem` 也不保证按照发送的 `Elem` 顺序排序**。

> **注意：**
> `path` 不支持 `file://` 开头的文件路径，需要去掉 `file://` 前缀。

**`TIMSoundElem` 成员方法：**

```
//获取二进制数据长度
long    getDataSize()
//获取语音时长
long    getDuration()
//下载语音
void    getSound(TIMValueCallBack<byte[]> callback)
//获取 uuid
java.lang.String    getUuid()
//设置二进制数据
void    setData(byte[] data)
//设置需要发送的语音文件的路径（上传时，如果设置了文件路径，优先上传路径所指定的语音文件）
void setPath(String path)
//设置语音时长
void    setDuration(long duration)
```

**示例：**

```
//构造一条消息
TIMMessage msg = new TIMMessage();
//添加语音
TIMSoundElem elem = new TIMSoundElem();
elem.setPath(filePath); //填写语音文件路径
elem.setDuration(20);  //填写语音时长
//将 Elem 添加到消息
if(msg.addElement(elem) != 0) {
    Log.d(tag, "addElement failed");
    return;
}
//发送消息
conversation.sendMessage(msg, new TIMValueCallBack<TIMMessage>() {//发送消息回调
    @Override
    public void onError(int code, String desc) {//发送消息失败
        //错误码 code 和错误描述 desc，可用于定位请求失败原因
        //错误码 code 含义请参见错误码表
        Log.d(tag, "send message failed. code: " + code + " errmsg: " + desc);
    }
    @Override
    public void onSuccess(TIMMessage msg) {//发送消息成功
        Log.e(tag, "SendMsg ok");
    }
});
```

### 地理位置消息发送
地理位置消息由 `TIMLocationElem` 定义，其中 `desc` 存储位置的描述信息，`longitude`、`latitude` 分别表示位置的经度和纬度。

**`TIMLocationElem` 成员方法：**

```
//获取位置描述
java.lang.String    getDesc()
//获取纬度
double  getLatitude()
//获取经度
double  getLongitude()
//设置位置描述
void    setDesc(java.lang.String desc)
//设置纬度
void    setLatitude(double latitude)
//设置经度
void    setLongitude(double longitude)
```

**示例：**

```
//构造一条消息
TIMMessage msg = new TIMMessage();
//添加位置信息
TIMLocationElem elem = new TIMLocationElem();
elem.setLatitude(113.93);   //设置纬度
elem.setLongitude(22.54);   //设置经度
elem.setDesc("腾讯大厦");
//将elem添加到消息
if(msg.addElement(elem) != 0) {
    Log.d(tag, "addElement failed");
    return;
}
//发送消息
conversation.sendMessage(msg, new TIMValueCallBack<TIMMessage>() {//发送消息回调
    @Override
    public void onError(int code, String desc) {//发送消息失败
        //错误码 code 和错误描述 desc，可用于定位请求失败原因
        //错误码 code 含义请参见错误码表
        Log.d(tag, "send message failed. code: " + code + " errmsg: " + desc);
    }
    @Override
    public void onSuccess(TIMMessage msg) {//发送消息成功
        Log.e(tag, "SendMsg ok");
    }
});
```

### 小文件消息发送

文件消息由 `TIMFileElem` 定义，另外还可以提供额外的显示文件名信息。**注意：一条消息只能添加一个文件 `Elem`，添加多个文件时，`AddElem` 函数返回错误 1，另外，语音和文件 `Elem` 不一定会按照添加时的顺序获取，建议逐个判断 `Elem` 类型展示。**

> **注意：**
> `path` 不支持 `file://` 开头的文件路径，需要去掉 `file://` 前缀。

**`TIMFileElem` 成员方法：**

```
//获取文件
void    getFile(TIMValueCallBack<byte[]> callback)
//获取文件名
java.lang.String    getFileName()
//获取文件大小
long    getFileSize()
//获取 uuid
java.lang.String    getUuid()
//设置待发送的文件二进制数据
void    setData(byte[] data)
//设置上传文件所在路径（上传时，如果设置了文件路径，优先上传路径所指定的文件）
void setPath(String path)
//设置文件名
void    setFileName(java.lang.String fileName)
```

**示例：**

```
//构造一条消息
TIMMessage msg = new TIMMessage();
//添加文件内容
TIMFileElem elem = new TIMFileElem();
elem.setPath(filePath); //设置文件路径
elem.setFileName("myfile.bin"); //设置消息展示用的文件名称
//将elem添加到消息
if(msg.addElement(elem) != 0) {
    Log.d(tag, "addElement failed");
    return;
}
//发送消息
conversation.sendMessage(msg, new TIMValueCallBack<TIMMessage>() {//发送消息回调
    @Override
    public void onError(int code, String desc) {//发送消息失败
        //错误码 code 和错误描述 desc，可用于定位请求失败原因
        //错误码 code 含义请参见错误码表
        Log.d(tag, "send message failed. code: " + code + " errmsg: " + desc);
    }
    @Override
    public void onSuccess(TIMMessage msg) {//发送消息成功
        Log.e(tag, "SendMsg ok");
    }
});
```

### 短视频消息发送

短视频消息由 `TIMVideoElem` 定义，它是 `TIMElem` 的一个子类，也就是说视频截图与视频内容也是消息的一种内容。发送短视频的过程，就是将 `TIMVideoElem` 加入到 `TIMMessage` 中，然后随消息一起发送出去。

**`TIMVideoElem` 原型：**

```
/**
 * 获取微视频上传任务 ID, 调用 sendMessage 后此接口的返回值有效
 * @return 微视频上传任务ID
 */
public long getTaskId()
/**
 * 设置微视频信息，在发送消息时进行设置
 * @param video 微视频信息，详见{@see TIMVideo}
 */
public void setVideo(TIMVideo video)
/**
 * 获取视频信息
 * @return 视频信息，详见{@see TIMVideo}
 */
public TIMVideo getVideoInfo()
/**
 * 设置视频文件路径，在发送消息时进行设置
 * @param path 视频文件路径
 */
public void setVideoPath(String path)
/**
 * 获取视频文件路径
 * @return 视频文件路径
 */
public String getVideoPath()
/**
 * 设置微视频截图信息，在发送消息时进行设置
 * @param snapshot 微视频截图信息，详见{@see TIMSnapshot}
 */
public void setSnapshot(TIMSnapshot snapshot)
/**
 * 获取视频截图信息
 * @return 视频截图信息，详见{@see TIMSnapshot}
 */
public TIMSnapshot getSnapshotInfo()
/**
 * 设置微视频截图文件路径，在发送消息时进行设置
 * @param path 微视频截图文件路径
 */
public void setSnapshotPath(String path)
/**
 * 获取微视频截图文件路径
 * @return 微视频截图文件路径
 */
public String getSnapshotPath()
/**
 * 获取上传进度
 * @return 上传进度
 */
public int getUploadingProgress()
```

**示例：**

```
//构造一条消息
TIMMessage message = new TIMMessage();
//构建一个视频 Elem
TIMVideoElem elem = new TIMVideoElem();
//添加视频内容, 其中的 FileUtil 类可以参考 Demo 中的实现
TIMVideo video = new TIMVideo();
video.setType("MP4");
video.setDuaration(MediaUtil.getInstance().getDuration(FileUtil.getCacheFilePath(fileName)));
elem.setVideo(video);
elem.setVideoPath(FileUtil.getCacheFilePath(fileName));
//添加视频截图, 其中的 FileUtil 类可以参考 Demo 中的实现
Bitmap thumb = ThumbnailUtils.createVideoThumbnail(FileUtil.getCacheFilePath(fileName), MediaStore.Images.Thumbnails.MINI_KIND);
elem.setSnapshotPath(FileUtil.createFile(thumb, new SimpleDateFormat("yyyyMMdd_HHmmss").format(new Date())));
TIMSnapshot snapshot = new TIMSnapshot();
snapshot.setType("PNG");
snapshot.setHeight(thumb.getHeight());
snapshot.setWidth(thumb.getWidth());
elem.setSnapshot(snapshot);
//将短视频 Elem 添加到消息中
if(message.addElement(elem) != 0){
    Log.e("tag", "addElement failed");
    return;
}
//发送消息
conversation.sendMessage(msg, new TIMValueCallBack<TIMMessage>() {//发送消息回调
    @Override
    public void onError(int code, String desc) {//发送消息失败
        //错误码 code 和错误描述 desc，可用于定位请求失败原因
        //错误码 code 含义请参见错误码表
        Log.d(tag, "send message failed. code: " + code + " errmsg: " + desc);
    }
    @Override
    public void onSuccess(TIMMessage msg) {//发送消息成功
        Log.e(tag, "SendMsg ok");
    }
});
```

### 自定义消息发送
**自定义消息：**指当内置的消息类型无法满足特殊需求，开发者可以自定义消息格式，内容全部由开发者定义，ImSDK 只负责透传。另外如果需要 iOS APNs 推送，还需要提供一段推送文本描述，方便展示。自定义消息由 `TIMCustomElem` 定义，其中 `data` 存储消息的二进制数据，其数据格式由开发者定义，`desc` 存储描述文本。一条消息内可以有多个自定义 `Elem`，并且可以跟其他 `Elem` 混合排列，离线 Push 时叠加每个 `Elem` 的 `desc` 描述信息进行下发。

**`TIMCustomElem` 成员方法：**

```
//获取自定义数据
byte[]  getData()
//获取自定义描述
java.lang.String    getDesc()
//设置自定义数据
void    setData(byte[] data)
//设置自定义描述
void    setDesc(java.lang.String desc)
```

以下示例中拼接一段 xml 消息，具体展示由开发者决定。
**示例：**

```
//构造一条消息
TIMMessage msg = new TIMMessage();
// xml 协议的自定义消息
String sampleXml = "<!--?xml version='1.0' encoding="utf-8"?-->testTitlethis is custom msgtest msg body";
//向 TIMMessage 中添加自定义内容
TIMCustomElem elem ＝ new TIMCustomElem();
elem.setData(sampleXml.getBytes());      //自定义 byte[]
elem.setDesc("this is one custom message"); //自定义描述信息
//将 elem 添加到消息
if(msg.addElement(elem) != 0) {
    Log.d(tag, "addElement failed");
    return;
}
//发送消息
conversation.sendMessage(msg, new TIMValueCallBack<TIMMessage>() {//发送消息回调
    @Override
    public void onError(int code, String desc) {//发送消息失败
        //错误码 code 和错误描述 desc，可用于定位请求失败原因
        //错误码 code 含义请参见错误码表
        Log.d(tag, "send message failed. code: " + code + " errmsg: " + desc);
    }
    @Override
    public void onSuccess(TIMMessage msg) {//发送消息成功
        Log.e(tag, "SendMsg ok");
    }
});
```

### Elem 顺序
目前文件和语音 `Elem` 不一定会按照添加顺序传输，其他 `Elem` 按照顺序，不过建议不要过于依赖 `Elem` 顺序进行处理，应该逐个按照 `Elem` 类型处理，防止异常情况下进程 Crash。

### 在线消息
对于某些场景，需要发送在线消息，即用户在线时收到消息，如果用户不在线，下次登录也不会看到消息，可用于通知类消息，这种消息不会进行存储，也不会计入未读计数。发送接口与 `sendMessage` 类似。

> **注意：**
>- ImSDK 2.5.3 之前版本只对单聊消息有效。
>- ImSDK 2.5.3 及之后版本，增加对群消息的支持(暂不支持 AVChatRoom 和 BChatRoom 类型)。**如果需要支持这种群消息，请注意各平台都需要升级到 2.5.3 及以上版本。**

**原型：**
```
//发送在线消息（服务器不保存消息）
public void sendOnlineMessage(TIMMessage msg, TIMValueCallBack<TIMMessage> callback)
```

### 消息转发
在 2.4.0 及以上版本，在 `TIMMessage` 中提供了 `copyFrom` 接口，可以方便地拷贝其他消息的内容到当前消息，然后将消息重新发送给其他人。

**原型：**
```
/**
 * 复制消息内容到当前消息（Elem, priority, online, offlinePushInfo 等）
 * @param srcMsg 源消息
 * @return true 复制成功
 */
public boolean copyFrom(@NonNull TIMMessage srcMsg)
```

## 接收消息

在多数情况下，用户需要感知新消息的通知，这时只需注册新消息通知回调 `TIMMessageListener`，如果用户是登录状态，ImSDK 收到新消息会通过此方法抛出，另外需要注意，通过 `onNewMessages` 抛出的消息不一定是未读的消息，只是本地曾经没有过的消息（例如在另外一个终端已读，拉取最近联系人消息时可以获取会话最后一条消息，如果本地没有，会通过此方法抛出）。在用户登录之后，ImSDK 会拉取离线消息，为了不漏掉消息通知，需要在登录之前注册新消息通知。

添加一个消息监听器，默认情况下所有消息监听器都将按添加顺序被回调一次 除非用户在 `onNewMessages` 回调中返回 true，此时将不再继续回调下一个消息监听器。
**原型：**
```
public void addMessageListener(TIMMessageListener listener)
```

回调消息内容通过参数 `TIMMessage` 传递，通过 `TIMMessage` 可以获取消息和相关会话的详细信息，如消息文本，语音数据，图片等等。**收到新消息回调：**
```
public boolean onNewMessages(java.util.Listmsgs)
```

消息监听器被删除后，将不再被调用。
**删除一个消息监听器：**
```
public void removeMessageListener(TIMMessageListener listener)
```

### 消息解析
收到消息后，可用过 `getElem` 从 `TIMMessage` 中获取所有的 `Elem` 节点。
**遍历 `Elem` 原型：**
```
//获取消息元素
TIMElem getElement(int i)
//获取元素个数
long    getElementCount()
```

**示例：**
```
TIMMessage msg = /* 消息 */
for(int i = 0; i < msg.getElementCount(); ++i) {
	TIMElem elem = msg.getElement(i);
	//获取当前元素的类型
	TIMElemType elemType = elem.getType();
	Log.d(tag, "elem type: " + elemType.name());
	if (elemType == TIMElemType.Text) {
		//处理文本消息
	} else if (elemType == TIMElemType.Image) {
		//处理图片消息
	}//...处理更多消息
}
```

### 接收图片消息
接收方收到消息后，可通过 `getElem` 从 `TIMMessage` 中获取所有的 `Elem` 节点，其中类型为 `TIMImageElem` 的是图片消息节点。然后通过 `imageList` 获取该图片的所有规格用来展示。

**`TIMImageElem` 成员方法：**
```
java.util.ArrayListgetImageList()
```

保存本图片的所有规格，目前最多包含三种规格：原图、大图、缩略图， 每种规格保存在一个 `TIMImage` 对象中。收消息时不用关注。其中 path 只在发送消息时有效，收到消息时此字段为空。
```
void    setPath(java.lang.String path)
```

** `TIMImage`：** 获取到消息时通过 `imageList` 得到所有的图片规格，为 `TIMImage` 数据，得到 `TIMImage` 后可通过图片大小进行占位，通过接口 `getImage` 下载不同规格的图片进行展示。**下载的数据需要由开发者缓存，ImSDK 每次调用 `getImage` 都会从服务端重新下载数据。建议通过图片的 `uuid` 作为 key 进行图片文件的存储。**

**`TIMImage` 成员方法：**

```
//获取图片高度
long    getHeight()
//获取图片，保存于 path 指向的文件中
void    getImage(java.lang.String path, TIMCallBack cb)
//获取图片
void    getImage(TIMValueCallBack<byte[]> cb)
//获取图片大小
long    getSize()
//图片规格，有三种 Thumb、Large、Original，分别代表缩略图、大图、原图
TIMImageType    getType()
//图片 ID，全局唯一，图片标识，相同 uuid 的图片可以不再重复下载
java.lang.String    getUuid()
//获取图片宽度
long    getWidth()
```

**图片规格说明：**每幅图片有三种规格，分别是 Original(原图)、Large(大图)、Thumb(缩略图)。

- **原图：**指用户发送的原始图片，尺寸和大小都保持不变。
- **大图：**是将原图等比压缩，压缩后宽、高中较小的一个等于 720 像素。
- **缩略图：**是将原图等比压缩，压缩后宽、高中较小的一个等于 198 像素。

>- 如果原图尺寸就小于 198 像素，则三种规格都保持原始尺寸，不需压缩。
>- 如果原图尺寸在 198~720 之间，则大图和原图一样，不需压缩。
>- 在手机上展示图片时，建议优先展示缩略图，用户单击缩略图时再下载大图，单击大图时再下载原图。当然开发者也可以选择跳过大图，单击缩略图时直接下载原图。
>- 在 Pad 或 PC 上展示图片时，由于分辨率较大，且基本都是 Wi-Fi 或有线网络，建议直接显示大图，用户单击大图时再下载原图。

**示例：  **
```
//遍历一条消息的元素列表
for(int i = 0; i < msg.getElementCount(); ++i) {
    TIMElem elem = msg.getElement(i);
    if (elem.getType() == TIMElemType.Image) {
        //图片元素
        TIMImageElem e = (TIMImageElem) elem;
        for(TIMImage image : e.getImageList()) {
            //获取图片类型, 大小, 宽高
            Log.d(tag, "image type: " + image.getType() +
                    " image size " + image.getSize() +
                    " image height " + image.getHeight() +
                    " image width " + image.getWidth());
            image.getImage(new TIMValueCallBack<byte[]>() {
                    @Override
                    public void onError(int code, String desc) {//获取图片失败
                    //错误码 code 和错误描述 desc，可用于定位请求失败原因
                    //错误码 code 含义请参见错误码表
                    Log.d(tag, "getImage failed. code: " + code + " errmsg: " + desc);
                    }
                    @Override
                    public void onSuccess(byte[] data) {//成功，参数为图片数据
                    //doSomething
                    Log.d(tag, "getImage success. data size: " + data.length);
                    }
                    });
        }
    }
}
```

### 接收语音消息
收到消息后，可用过 `getElem` 从 `TIMMessage` 中获取所有的 `Elem` 节点，其中 `TIMSoundElem` 为语音消息节点。

**`TIMSoundElem` 成员方法：**

```
//获取二进制数据长度
long    getDataSize()
//获取语音时长
long    getDuration()
//下载语音文件到指定的保存路径
public void getSoundToFile(String path, TIMCallBack callback)
//获取 uuid，可作为唯一标识，方便用户缓存
java.lang.String    getUuid()
//设置二进制数据
void    setData(byte[] data)
//设置语音时长
void    setDuration(long duration)
```

**下载语音文件到指定的保存路径：**获取到消息时可通过时长占位，通过接口 `getSoundToFile` 下载语音资源，`getSoundToFile` 接口每次都会从服务端下载，如需缓存或者存储，开发者可根据 `uuid` 作为 key 进行外部存储，ImSDK 并不会存储资源文件。

**原型：   **
```
public void getSoundToFile(String path, TIMCallBack callback)
```

**参数说明：**

参数|说明
---|---
path|指定保存路径
callback| 回调

**语音消息已读状态：**语音是否已经播放，可使用 [消息自定义字段](/doc/product/269/消息收发（Android%20SDK）#.E6.B6.88.E6.81.AF.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5) 实现，如 `customInt` 的值 0 表示未播放，1 表示播放，当用户单击播放后可设置 `customInt` 的值为 1。设置自定义整数， 默认为0。

**原型：**
```
public void setCustomInt(int value)
```

### 接收小文件消息
收到消息后，可用过 `getElem` 从 `TIMMessage` 中获取所有的 `Elem` 节点，其中 `TIMFileElem` 为文件消息节点。

**`TIMFileElem` 成员方法：**
```
//下载文件到指定的保存路径
void getToFile(String path, TIMCallBack callback)
//获取文件名
java.lang.String    getFileName()
//获取文件大小
long    getFileSize()
//获取 uuid
java.lang.String    getUuid()
//设置待发送的文件二进制数据
void    setData(byte[] data)
//设置文件名
void    setFileName(java.lang.String fileName)
```

**下载文件到指定的保存路径：**获取到消息时可只展示文件大小和显示名，通过接口 `getToFile` 下载文件资源。`getToFile` 接口每次都会从服务端下载，如需缓存或者存储，开发者可根据 `uuid` 作为 key 进行外部存储，ImSDK 并不会存储资源文件。

**原型： **
```
public void getToFile(String path, TIMCallBack callback)
```

**参数说明：**

参数|说明
---|---
path|指定保存路径
callback| 回调


### 接收短视频消息

收到消息后，可用过 `getElement` 从 `TIMMessage` 中获取所有的 `Elem` 节点，其中 `TIMVideoElem` 为文件消息节点，通过其中的 `TIMVideo` 和 `TIMSnapshot` 对象获取视频和截图内容。

**`TIMVideo` 原型:**
```
/**
* 设置视频文件类型，发送消息时进行设置
* @param type 视频文件类型
*/
public void setType(String type)
/**
* 获取视频文件类型
* @return 返回视频文件类型
*/
public String getType()
/**
* 设置视频时长，发送消息时进行设置
* @param duaration 视频时长
*/
public void setDuaration(long duaration)
/**
* 获取视频时长
* @return 返回视频时长
*/
public long getDuaration()
/**
* 获取视频文件 uuid
* @return uuid，可作为唯一标示用于缓存的 key
*/
public String getUuid()
/**
* 获取视频文件大小
* @return 返回视频文件大小
*/
public long getSize()
/**
* 获取视频
* @param path 视频保存路径
* @param cb 回调
*/
public void getVideo(@NonNull final String path, @NonNull final TIMCallBack cb)
```

**`TIMSnapshot` 原型:**
```
/**
 * 构造函数(多用户)
 * @param strIdentifer 帐号
 */
public TIMSnapshot(String strIdentifer)
/**
 * 获取截图文件 uuid
 * @return uuid，可作为唯一标示用于缓存的key
 */
public String getUuid()
/**
 * 设置截图文件类型，发送消息时进行设置
 * @param type 视频文件类型
 */
public void setType(String type)
/**
 * 获取截图文件类型
 * @return 返回视频文件类型
 */
public String getType()
/**
 * 获取截图文件大小
 * @return 返回截图文件大小
 */
public long getSize()
/**
 * 获取截图高度
 * @return 截图高度
 */
public long getHeight()
/**
 * 设置截图高度，发送消息时进行设置
 * @param height 截图高度
 */
public void setHeight(long height)
/**
 * 获取截图宽度
 * @return 截图宽度
 */
public long getWidth()
/**
 * 设置截图宽度，发送消息时进行设置
 * @param width 截图宽度
 */
public void setWidth(long width)
/**
 * 获取截图
 * @param path 保存截图的路径
 * @param cb 回调
 */
public void getImage(final String path, final TIMCallBack cb)
```

**示例：**

```
//遍历一条消息的元素列表
for(int i = 0; i < msg.getElementCount(); ++i) {
    TIMElem elem = msg.getElement(i);
    if (elem.getType() == TIMElemType.Video) {
        //视频元素
        TIMVideoElem e = (TIMVideoElem) elem;
        //获取视频截图信息
        TIMSnapshot snapshot = e.getSnapshotInfo();
        String snapshot_uuid = snapshot.getUuid();
        String snapshot_type = snapshot.getType();
        long height = snapshot.getHeight();
        long width = snapshot.getWidth();
        long snapshot_size = snapshot.getSize();
        //下载视频截图，并保存到 snapshotSavePath
        snapshot.getImage(snapshotSavePath, new TIMCallBack() {
            @Override
            public void onError(int code, String desc) {
                Log.e(tag, "getImage failed, code:" + code + "|desc:" + desc);
            }
            @Override
            public void onSuccess() {
                Log.e(tag, "getImage succ");
            }
        });
        //获取视频信息
        TIMVideo video = e.getVideoInfo();
        String video_type = video.getType();
        String video_uuid = video.getUuid();
        long duaration = video.getDuaration();
        long video_size = video.getSize();
        video.getVideo(videoSavePath, new TIMCallBack() {
            @Override
            public void onError(int code, String desc) {
                Log.e(tag, "getVideo failed, code:" + code + "|desc:" + desc);
            }
            @Override
            public void onSuccess() {
                Log.e(tag, "getVideo succ");
            }
        });
    }
}
```

## 消息属性
可通过 `TIMMessage` 成员方法获取消息属性。

### 消息是否已读
通过 `TIMMessage` 的方法 `isRead` 可以获取消息是否已读。这里已读与否取决于 App 侧进行的 [已读上报](/doc/product/269/未读消息计数（Android%20SDK）#.E5.B7.B2.E8.AF.BB.E4.B8.8A.E6.8A.A5)。

**原型：**

```
public boolean isRead()
```

### 消息状态
通过 `TIMMessage` 的方法 `status` 可以获取当前消息的状态，如发送中、发送成功、发送失败和删除，对于删除的消息，需要 UI 判断状态并隐藏。

```
//发送中
TIMMessageStatus.Sending

//发送成功
TIMMessageStatus.SendSucc

//发送失败
TIMMessageStatus.SendFail

//删除
TIMMessageStatus.HasDeleted

//消息被撤回
TIMMessageStatus.HasRevoked
```

### 是否自己发出的消息
通过 `TIMMessage` 的方法 `isSelf` 可以判断消息是否是自己发出的消息，界面显示时可用。

**原型：**
```
public boolean isSelf()
```

### 消息发送者及其相关资料
对于群消息，可以通过 `TIMMessage` 的方法 `getSender` 得到发送用户，另外也可以通过方法 `getSenderProfile` 和 `getSenderGroupMemberProfile` 获取用户自己的资料和所在群的资料。对于单聊消息，通过 `TIMMessage` 的 `getConversation` 获取到对应会话，会话的 `getPeer` 可以得到正在聊天的用户。

> **注意：**
>- 此字段是消息发送时获取用户资料写入消息体，如后续用户资料更新，此字段不会相应变更，只有产生的新消息中才会带最新的昵称。
>- 1.9 版本之前，只有在线消息 `onNewMessages` 抛出的消息可以获取到用户资料。
>- 1.9 版本以后，通过 `getMessage` 得到的消息也可以拿到资料（更新版本之前已经收到本地的消息无法获取到）。

```
//获取消息发送方
public String getSender()
//获取发送者个人资料
public TIMUserProfile getSenderProfile()
//获取发送者群内资料
public TIMGroupMemberInfo getSenderGroupMemberProfile()
```

### 消息时间
通过 `TIMMessage` 的方法 `timestamp` 可以得到消息时间，该时间是 Server 时间，而非本地时间。在创建消息时，此时间为根据 Server 时间校准过的时间，发送成功后会改为准确的 Server 时间。

```
//消息在服务端生成的时间戳
public long timestamp()
```

### 消息删除
目前暂不支持 Server 消息删除，只能在本地删除，有两种删除方法，一种是 `remove`，通过这种方法删除的消息，仅是打上删除的标记，并未真正删除。另外一种是 `DeleteFromStorage`，从本地数据库彻底删除，但是如果使用 `getMessage`，可能从 Server 漫游消息获取到本地，此消息可能重新出现。所以如果使用了 `getMessage`，建议使用 `remove` 方法进行删除和界面过滤。

```
//将消息状态标记为删除
public boolean remove()
//从本地数据库删除消息：注意群组消息通过 getMessage 接口会从 svr 同步到本地
public boolean DeleteFromStorage()
```

### 消息 ID
消息 ID 也有两种，一种是当消息生成时，就已经固定（`msgId`），这种方式可能跟其他用户产生的消息冲突，需要再加一个时间未读，可以认为 10 分钟以内的消息可以使用 `msgId` 区分。另外一种，当消息发送成功以后才能固定下来（`uniqueId`），这种方式能保证全局唯一。这两种方式都需要在同一个会话内判断。

```
//获取消息 ID
public String getMsgId()
//获取消息 uniqueId
public long getMsgUniqueId()
```

### 消息自定义字段
开发者可以对消息增加自定义字段，如自定义整数、自定义二进制数据，可以根据这两个字段做出各种不通效果，比如语音消息是否已经播放等等。另外需要注意，此自定义字段仅存储于本地，不会同步到 Server，更换终端获取不到。

```
//设置自定义整数， 默认为 0
public void setCustomInt(int value)
//获取自定义整数值
public int getCustomInt()
//设置自定义数据内容，默认为""
public void setCustomStr(String str)
//获取自定义数据内容的值
public String getCustomStr()
```

### 消息优先级
对于直播场景，会有点赞和发红包功能，点赞相对优先级较低，红包消息优先级较高，具体消息内容可以使用 `TIMCustomElem` 进行定义，发送消息时，可使用不同接口定义消息优先级。具体消息优先级的策略，可参阅 [互动直播集成多人聊天方案](/doc/product/269/互动直播集成多人聊天方案)。**注意：只针对群聊消息有效。**

```
//设置消息优先级
public void setPriority(TIMMessagePriority priority)
//获取消息优先级
public TIMMessagePriority getPriority()
```

### 群组消息会话的接收消息选项
对于群组会话消息，可以通过消息属性判断本群组设置的接收消息选项，可参阅 [群组管理](/doc/product/269/1563)。**注意：只针对群聊消息有效。**

```
//获取消息通知类型
public TIMGroupReceiveMessageOpt getRecvFlag()
```

### 已读回执

由 2.3.0 版本开始，提供**针对于 C2C 消息**的已读回执功能。通过 `TIMManager` 中的 `enableReadReceipt` 接口可以启用消息已读回执功能。启用已读回执功能后，在进行 [消息已读上报](/doc/product/269/1562#.E5.B7.B2.E8.AF.BB.E4.B8.8A.E6.8A.A5) 的时候会发送已读回执给聊天对方。通过 `TIMManager` 的接口 `setMessageReceiptListener` 可以注册已读回执监听器。通过 `TIMMessage` 中的 `isPeerReaded` 可以查询当前消息对方是否已读。

**原型：**

```
/**
 * 启用已读回执，启用后在已读上报时会发送回执给对方，只对单聊会话有效
 */
public void enableReadReceipt()
/**
 * 设置已读回执监听器
 * @param receiptListener 已读回执监听器
 */
public void setMessageReceiptListener(TIMMessageReceiptListener receiptListener)
/**
 * 获取对方是否已读（仅对 C2C 消息有效）
 * @return true - 对方已读， false - 对方未读
 */
public boolean isPeerReaded()
```

### 消息序列号

通过 ImSDK 2.5.3 提供的 `TIMMessage` 中的接口 `getSeq` 可以获取到当前消息的序列号。

```
/**
 * 获取当前消息的序列号
 * @return 当前消息的序列号
 */
public long getSeq()
```

### 消息随机码

通过 ImSDK 2.5.3 提供的 `TIMMessage` 中的接口 `getRand` 可以获取到当前消息的随机码。

```
/**
 * 获取当前消息的随机码
 * @return 当前消息的随机码
 */
public long getRand()
```

### 消息查找参数

ImSDK 中的消息需要通过 `{seq, rand, timestamp, isSelf}` 四元组来唯一确定一条具体的消息，我们把这个四元组称为消息的查找参数。通过 ImSDK 2.5.3 提供的 `TIMMessage` 中的 `getMessageLocator` 接口可以从当前消息中获取到当前消息的查找参数。

```
/**
 * 获取当前消息的查找参数
 * @return 当前消息的查找参数
 */
public TIMMessageLocator getMessageLocator()
```

## 会话操作
### 获取所有会话
通过 `ConversationCount` 获取当前会话数量，从而得到所有本地会话。

**原型：**

```
//根据索引获取会话
TIMConversation getConversationByIndex(long i)
//获取本地保存的会话数
long    getConversationCount()
```

**示例：**

```
//获取会话个数
long cnt = TIMManager.getInstance().getConversationCount();
//遍历会话列表
for(long i = 0; i < cnt; ++i) {
    //根据索引获取会话
    TIMConversation conversation =
            TIMManager.getInstance().getConversationByIndex(i);
    Log.d(tag, "get conversation. type: " + conversation.getType());
}
```

**2.0 以上版本提供获取当前所有会话的列表 `getConversationList` 原型：**

```
//获取所有会话
public List<TIMConversation> getConversationList()
```

### 最近联系人漫游
ImSDK 登录以后默认会获取最近联系人漫游，同时每个会话会获取到最近的一条消息。如果不需要此功能，可以调用方法禁用。

```
//禁止在登录后拉取最近联系人，默认会进行拉取，需登录前设置
public void disableRecentContact()
```

### 获取会话本地消息

ImSDK 会在本地进行消息存储，可通过 `TIMConversation` 方法的 `getLocalMessage` 获取，此方法为异步方法，需要通过设置回调得到消息数据，对于单聊，登录后可以获取离线消息，对于群聊，开启最近联系人漫游的情况下，登录后只能获取最近一条消息，可通过 `getMessage` 获取漫游消息。

**获取本地聊天记录原型： **

```
public void getLocalMessage(int count, TIMMessage lastMsg, TIMValueCallBack<List<TIMMessage>> callback)
```

**参数说明：**

参数|说明
---|---
count | 从最后一条消息往前的消息条数
lastMsg | 已获取的最后一条消息，当传 null 的时候，从最新的消息开始读取
callback | 回调, 参数中返回获取的消息列表

**示例：**

>**注意：**
>对于图片、语音等资源类消息，消息体只会包含描述信息，需要通过额外的接口下载数据，可参与消息解析部分，下载后的真实数据不会缓存，需要调用方进行缓存。

```
//获取此会话的消息
conversation.getLocalMessage(10, //获取此会话最近的 10 条消息
        null, //不指定从哪条消息开始获取 - 等同于从最新的消息开始往前
        new TIMValueCallBack<List<TIMMessage>>() {//回调接口
    @Override
    public void onError(int code, String desc) {//获取消息失败
        //接口返回了错误码 code 和错误描述 desc，可用于定位请求失败原因
        //错误码 code 含义请参见错误码表
        Log.d(tag, "get message failed. code: " + code + " errmsg: " + desc);
    }
    @Override
    public void onSuccess(List<TIMMessage> msgs) {//获取消息成功
        //遍历取得的消息
        for(TIMMessage msg : msgs) {
            lastMsg = msg;
            //可以通过timestamp()获得消息的时间戳, isSelf()是否为自己发送的消息
            Log.e(tag, "get msg: " + msg.timestamp() + " self: " + msg.isSelf() + " seq: " + msg.msg.seq());
        }
    }
});
```

### 获取会话漫游消息

对于群组，登录后可以获取漫游消息，对于 C2C，开通漫游服务后可以获取漫游消息。通过 ImSDK 的 `getMessage` 接口可以获取漫游消息。如果本地消息全部都是连续的，则不会通过网络获取，如果本地消息不连续，会通过网络获取断层消息。

**原型： **

```
public void getMessage(int count, TIMMessage lastMsg, TIMValueCallBack<List<TIMMessage>> callback)
```

**参数说明：**

参数|说明
---|---
count | 从最后一条消息往前的消息条数
lastMsg | 已获取的最后一条消息，当传 null 的时候，从最新的消息开始读取
callback | 回调，参数中返回获取的消息列表

**示例：**

> **注意：**
> 对于图片、语音等资源类消息，消息体只会包含描述信息，需要通过额外的接口下载数据，可参与消息解析部分，下载后的真实数据不会缓存，需要调用方进行缓存。

```
//获取此会话的消息
conversation.getMessage(10, //获取此会话最近的 10 条消息
        null, //不指定从哪条消息开始获取 - 等同于从最新的消息开始往前
        new TIMValueCallBack<List<TIMMessage>>() {//回调接口
    @Override
    public void onError(int code, String desc) {//获取消息失败
        //接口返回了错误码 code 和错误描述 desc，可用于定位请求失败原因
        //错误码 code 含义请参见错误码表
        Log.d(tag, "get message failed. code: " + code + " errmsg: " + desc);
    }
    @Override
    public void onSuccess(List<TIMMessage> msgs) {//获取消息成功
        //遍历取得的消息
        for(TIMMessage msg : msgs) {
            lastMsg = msg;
            //可以通过 timestamp()获得消息的时间戳, isSelf()是否为自己发送的消息
            Log.e(tag, "get msg: " + msg.timestamp() + " self: " + msg.isSelf() + " seq: " + msg.msg.seq());

        }
    }
});
```

### 删除会话

删除会话有两种方式，一种只删除会话，但保留了所有消息，另一种在删除会话的同时，也删除掉会话相关的消息。可以根据不同应用场景选择合适的方式。另外需要注意的是，如果删除本地消息，对于群组，通过 `getMessage` 会拉取到漫游消息，所以存在删除消息成功，但是拉取到消息的情况，取决于是否重新从漫游拉回到本地。如果不需要拉取漫游，可以通过 `getLocalMessage` 获取消息，或者只通过 `getMessage` 拉取指定条数（如未读条数数量）的消息。其中 `deleteConversation` 仅删除会话，`deleteConversationAndMessages` 删除会话以及消息。

**原型：**
```
//删除会话
public boolean deleteConversation(TIMConversationType type, String peer)
//删除会话和消息
public boolean deleteConversationAndLocalMsgs(TIMConversationType type, String peer)
```

**参数说明：**

参数|说明
---|---
type|会话类型，如果是单聊，填写 TIMConversationType.C2C，如果是群聊，填写 TIMConversationType.Group
peer|会话标识，单聊情况下，peer 为对方用户 identifier，群聊情况下，peer 为群组 ID。

以下示例中删除与用户 hello 的 C2C 会话，**示例：**

```
TIMManager.getInstance().deleteConversation(TIMConversationType.C2C, "hello");
```

### 同步获取会话最后的消息
UI 展示最近联系人列表时，时常会展示用户的最后一条消息，在 1.9.2 以后版本增加了同步获取接口，用户可以通过此接口方便获取最后一条消息进行展示。**目前没有网络无法获取，另外如果禁用了最近联系人，登录后在有新消息过来之前无法获取**。此接口获取并不会过滤删除状态消息，需要 App 层进行屏蔽。

**从 Cache 中获取最后几条消息原型： **

```
public List<TIMMessage> getLastMsgs(long count)
```

**参数说明：**

参数|说明
---|---
count | 需要获取的消息数，注意这里最多为 20

### 禁用会话本地存储

直播场景下，群组类型会话的消息量很大，为了提升效率时常需要禁用直播群的本地消息存储功能。在 ImSDK 2.2.0 及更高级版本中增加了针对单个会话禁用本地存储的功能，开发者可以根据需要调用 `TIMConversation` 中的 `disableStorage` 接口禁用相应的会话本地存储。

**原型： **

```
/**
 * 禁止当前会话的存储，只对当前初始化有效，重启后需要重新设置。
 * 需要初始后调用
 */
public void disableStorage()
```

### 设置会话草稿

ImSDK 2.2.0 及以上版本增加了会话草稿功能，开发者可以通过 `TIMConversation` 中的相关接口进行草稿操作。

> **注意：**
>- 草稿只能本地有效，更换终端或者清除数据后将看不到草稿。
>- 草稿信息会存本地数据库，重新登录后依然可以获取。

**原型： **

```
/**
 * 设置草稿
 * @param draft 草稿内容, 为 null 则表示取消草稿
 */
public void setDraft(TIMMessageDraft draft)
/**
 * 获取草稿
 * @return 返回草稿内容
 */
public TIMMessageDraft getDraft()
/**
 * 当前会话是否存在草稿
 * @return true - 存在，false - 不存在
 */
public boolean hasDraft()
```

**参数说明：**

参数|说明
---|---
draft | 需要设置的草稿 ，需要清空会话草稿时传入 null

**`TIMMessageDraft` 原型：**

```
/**
 * 获取草稿中的消息元素列表
 * @return 消息元素列表
 */
public List<TIMElem> getElems()
/**
 * 设置草稿中的消息元素
 * @param elem 要添加到草稿中的消息元素
 */
public void addElem(TIMElem elem)
/**
 * 获取草稿中用户自定义数据
 * @return 用户自定义数据
 */
public byte[] getUserDefinedData()
/**
 * 设置草稿中用户自定义数据
 * @param userDefinedData 用户自定义数据
 */
public void setUserDefinedData(byte[] userDefinedData)
/**
 * 获取草稿的编辑时间
 * @return 草稿编辑时间
 */
public long getTimestamp()
```

### 消息查找

ImSDK 提供了根据提供参数查找相应消息的功能，只能精准查找，暂时不支持模糊查找。开发者可以通过调用 ImSDK 2.5.3 提供 `TIMConversation` 中的 `findMessages` 方法进行消息查找。

```
/**
 * 根据提供的参数查找相应消息
 * @param locators 消息查找参数
 * @param cb 回调，返回查找到的消息
 */
public void findMessages(@NonNull List<TIMMessageLocator> locators, TIMValueCallBack<List<TIMMessage>> cb)
```
其中参数中的 `TIMMessageLocator` 可以通过消息中的 `getMessageLocator` 方法来获取，或者自行构造。

**`TIMMessageLocator` 原型:**

```
/**
 * 设置要查找的消息的时间戳
 * @param timestamp 消息时间戳
 */
public TIMMessageLocator setTimestamp(long timestamp)
/**
 * 设置要查找的消息的序列号
 * @param seq 消息的序列号
 */
public TIMMessageLocator setSeq(long seq)
/**
 * 设置要查找的消息随机码
 * @param rand 消息随机码
 */
public TIMMessageLocator setRand(long rand)
/**
 * 设置要查找的消息的发送者是否是自己
 * @param self true - 发送者是自己， false - 发送者不是自己
 */
public TIMMessageLocator setSelf(boolean self)
```

### 撤回消息

ImSDK v2系列在v2.7.2版本开始提供撤回消息的接口。可以通过调用 `TIMConversation` 的 `revokeMessage` 接口来撤回自己发送的消息。

> **注意：**
> - 仅 C2C 和 GROUP 会话有效、onlineMessage 无效、AVChatRoom 和 BChatRoom 无效。
> - 默认只能撤回 2 分钟内的消息。

**原型：**

```
/**
 * 消息撤回（仅 C2C 和 GROUP 会话有效，其中 onlineMessage、AVChatRoom 和 BChatRoom 无效）
 * @param msg 需要撤回的消息
 * @param cb 回调
 * @since 2.7.2
 */
public void revokeMessage(@NonNull TIMMessage msg, @NonNull TIMCallBack cb)
```

成功撤回消息后，群组内其他用户和 C2C 会话对端用户会收到一条消息撤回通知，并通过消息撤回通知监听器 `TIMMessageRevokeListener` 通知到上层应用。消息撤回通知监听器可以在登录前，通过 `TIMManager` 的 `setMessageRevokedListener` 来进行配置。

**原型：**

```
/**
 * 消息被撤回通知监听器
 * @since 2.7.2
 */
public interface TIMMessageRevokedListener extends IMBaseListener {
    /**
     * 消息撤回通知
     * @param locator 被撤回的消息的消息定位符
     */
     void onMessageRevoked(TIMMessageLocator locator);
}

/**
* 设置消息撤回通知监听器
* @param listener 消息撤回通知监听器
* @since 2.7.2
*/
public void setMessageRevokedListener(@NonNull TIMMessageRevokedListener listener)

```

收到一条消息撤回通知后，通过 `TIMMessage` 中的 `checkEquals` 方法判断当前消息是否是被对方撤回了，然后根据需要对 UI 进行刷新。

**原型：**

```
/**
 * 比较当前消息与提供的消息定位符表示的消息是否是同一条消息
 * @param locator 消息定位符
 * @return true - 表示是同一条消息； false - 表示不是同一条消息
 * @since 2.7.2
 */
public boolean checkEquals(@NonNull TIMMessageLocator locator)

```

另外，需要注意的是，**掉线重连的时候，如果用户处于群组聊天界面，需要业务端主动同步该群组会话的消息撤回通知**。其他场景不需要主动同步消息撤回通知。

**原型：**

```
/**
 * 同步本会话的消息撤回通知（仅 GROUP 会话有效，同步回来的通知会通过 TIMMessageRevokedListener 抛出）
 * @param cb 回调
 * @since 2.7.2
 */
public void syncMsgRevokedNotification(@NonNull TIMCallBack cb)

```

## 系统消息
会话类型（TIMConversationType）除了 C2C 单聊和 Group 群聊以外，还有一种系统消息。系统消息不能由用户主动发送，是系统后台在相应的事件发生时产生的通知消息。系统消息目前分为两种，一种是**关系链变更系统消息**，一种是**群系统消息**。

- **关系链变更系统消息：**当有用户加自己为好友，或者有用户删除自己好友的情况下，系统会发出变更通知，开发者可更新好友列表。相关细节可参阅 [关系链变更系统通知](/doc/product/269/用户资料与关系链（Android%20SDK）#8.-.E5.85.B3.E7.B3.BB.E9.93.BE.E5.8F.98.E6.9B.B4.E7.B3.BB.E7.BB.9F.E9.80.9A.E7.9F.A5)。
- **群事件消息：**当群资料变更，如群名变更或者群内成员变更，在群里会有系统发出一条群事件消息，开发者可在收到消息时可选择是否展示给用户，同时可刷新群资料或者群成员。详细内容可参阅 [群事件消息](/doc/product/269/群组管理（Android%20SDK）#8.-.E7.BE.A4.E4.BA.8B.E4.BB.B6.E6.B6.88.E6.81.AF)。
- **群系统消息：**当被管理员踢出群组，被邀请加入群组等事件发生时，系统会给用户发出群系统消息，相关细节可参阅 [群系统消息](/doc/product/269/群组管理（Android%20SDK）#9.-.E7.BE.A4.E7.B3.BB.E7.BB.9F.E6.B6.88.E6.81.AF)。


## 设置后台消息通知栏提醒
ImSDK 后台在线时可以持续接收消息通知，如果此时程序在后台运行，可以以系统通知栏提醒的形式给用户呈现新的消息。新消息可以显示在顶部通知栏，通知中心或锁屏上。具体的实现方式可参见 Demo 中 `PushUtil.java`。

**示例：**

```
NotificationManager mNotificationManager = (NotificationManager) context.getSystemService(context.NOTIFICATION_SERVICE);
NotificationCompat.Builder mBuilder = new NotificationCompat.Builder(context);
Intent notificationIntent = new Intent(context, MainActivity.class);
notificationIntent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP| Intent.FLAG_ACTIVITY_SINGLE_TOP);
PendingIntent intent = PendingIntent.getActivity(context, 0, notificationIntent, 0);
mBuilder.setContentTitle(senderStr)//设置通知栏标题
            .setContentText(contentStr)
            .setContentIntent(intent) //设置通知栏单击意图
            .setNumber(++pushNum) //设置通知集合的数量
            .setTicker(senderStr+":"+contentStr) //通知首次出现在通知栏，带上升动画效果的
            .setWhen(System.currentTimeMillis())//通知产生的时间，会在通知信息里显示，一般是系统获取到的时间
            .setDefaults(Notification.DEFAULT_ALL)//向通知添加声音、闪灯和振动效果的最简单、最一致的方式是使用当前的用户默认设置，使用defaults属性，可以组合                        
            .setSmallIcon(R.drawable.ic_launcher);//设置通知小 ICON
Notification notify = mBuilder.build();
notify.flags |= Notification.FLAG_AUTO_CANCEL;
mNotificationManager.notify(pushId, notify);
```
