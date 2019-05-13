## 消息发送 

### 通用消息发送

#### 会话获取

会话是指面向一个人或者一个群组的对话，通过与单个人或群组之间会话收发消息，发消息时首先需要先获取会话，获取会话需要指定会话类型（群组或者单聊），以及会话对方标志（对方帐号或者群号）。获取会话由 `TIMGetConversation`，通过指定类型，获取相应会话。 

**原型：**

```
int	TIMGetConversation(TIMConversationHandle handle, TIMConversationType type, const char* peer);
```

以下示例获取对方 `identifier` 为『WIN_001』的**单聊会话示例：** 

```
void CreateC2CConversation()
{
	const char* peer = "WIN_001"; //your conv peer
	TIMConversationHandle conv = CreateConversation();
	int rt = TIMGetConversation(conv, kCnvC2C, peer);
	//conv 使用完毕以后资源释放
	DestroyConversation(conv); 
}
```

以下示例获取群组 ID 为『TGID1JYSZEAEQ』的**群聊会话示例**： 

```
void CreateGRPConversation()
{
	const char* peer = "TGID1JYSZEAEQ"; //your conv peer
	TIMConversationHandle conv = CreateConversation();
	intrt = TIMGetConversation(conv, kCnvGroup, peer);
	//conv 使用完毕以后资源释放
	DestroyConversation(conv);
}
```

#### 消息发送

通过获取会话 `TIMConversation` 后，可发送消息和获取会话缓存消息。ImSDK 中消息的解释可参阅 [ImSDK 对象简介](/doc/product/269/1579#imsdk-.E5.9F.BA.E6.9C.AC.E6.A6.82.E5.BF.B5)。ImSDK 中的消息由 `TIMMessage` 表达， 一个 `TIMMessage` 由多个 `TIMElem` 组成，每个 `TIMElem` 可以是文本和图片，也就是说每一条消息可包含多个文本和多张图片。发消息通过 `SendMsg` 实现。

![](//mccdn.qcloud.com/static/img/7226ab79d4294cc53980c888892f5c6d/image.png)

**原型：**

```
void SendMsg(TIMConversationHandle conv_handle, TIMMessageHandle msg_handle, TIMCommCB *callback);
```

**参数说明：**

参数 | 说明
---|---
conv_handle | 会话句柄 
msg_handle | 消息句柄 
callback | 消息回调 

### 文本消息发送 

文本消息由 **`TIMMsgTextElemHandle` 定义： **

```
typedef void* TIMMsgTextElemHandle;
TIMMsgTextElemHandle	CreateMsgTextElem();
void	SetContent(TIMMsgTextElemHandle handle, const char* content);
uint32_t	GetContentLen(TIMMsgTextElemHandle handle);
int	GetContent(TIMMsgTextElemHandle handle, char* content, uint32_t* len);
```


以下示例中 `content` 表示需要发送的文本消息。 **示例：  ** 

```
void DemoSendMsg()
{
	const char* peer = "c9_0"; //your conv peer
	TIMConversationHandle conv = CreateConversation();
	intrt = TIMGetConversation(conv, kCnvC2C, peer);

	TIMMessageHandle msg = CreateTIMMessage();
	TIMMsgTextElemHandle elem = CreateMsgTextElem();
	char content[20] = {0};
	sprintf(content, "%s%s", "msg from ", peer);
	SetContent(elem, content);
	AddElem(msg, elem);
	TIMCommCB callback;
	callback.OnSuccess = CBCommOnSuccessImp;
	callback.OnError = CBCommOnErrorImp;
	SendMsg(conv, msg, &callback);
	//....wait for callback
	SLEEP(1);
	DestroyConversation(conv);
	DestroyTIMMessage(msg);
	DestroyElem(elem);
}
```

### 图片消息发送 

图片消息由 `TIMImageElem` 定义。它是一种 `TIMElem`，也就是说图片也是消息的一种内容。 发送图片的过程，就是将 `TIMImageElem` 加入到 `TIMMessage` 中，然后随消息一起发送出去。`TIMImageHandle` 存储了图片列表的类型，大小，宽高信息，如需要图片二进制数据，需通过 `GetImageFile` 接口下载。详细如下：

```
int		GetImageElemUUID(TIMMsgImageElemHandle handle, char* buf, uint32_t* len);
void	SetImageElemPath(TIMMsgImageElemHandle handle, const char* path, uint32_t len);
int		GetImageElemPath(TIMMsgImageElemHandle handle, char* path, uint32_t* len);
void		SetImageCompressLeval(TIMMsgImageElemHandle handle, const TIM_IMAGE_COMPRESS_TYPE leval);
uint32_t	GetImageNum(TIMMsgImageElemHandle handle);
int		GetImages(TIMMsgImageElemHandle handle, TIMImageHandle* images, uint32_t* num);
```

**参数说明：**

| 参数 | 说明 |
| --- | --- |
| buf | 图片 ID，内部标识，可用于外部缓存 key  |
| path | 要发送的图片路径 |
| len | 要发送的图片路径字符串长度 |
| Leval | 图片压缩等级，详见 TIM_IMAGE_COMPRESS_TYPE  |
| images | 发送成功后各种类型的图片，发送图片时，只需要设置图片路径 path。发送成功后可通过 GetImages 获取所有图片类型，目前只支持缩略图，大图，原图。  |

```
typedef enum _TIMImageType
	{
		kOriginalImage = 0,
		kThumbImage,
		kLargeImage,
	}TIMImageType;
typedef void* TIMImageHandle;
TIMImageType	GetImageType(TIMImageHandle handle);
uint32_t	GetImageSize(TIMImageHandle handle);
uint32_t	GetImageHeight(TIMImageHandle handle);
uint32_t	GetImageWidth(TIMImageHandle handle);
uint32_t	GetImageURLLen(TIMImageHandle handle);
int		GetImageURL(TIMImageHandle handle, char* url, uint32_t* len);
int		GetImageFile(TIMImageHandle handle, char* filename, TIMCommCB* cb);
```

**参数说明：**

| 参数 | 说明 |
| --- | --- |
| type | 图片类型，原图、缩略图、大图，参见 TIM_IMAGE_TYPE  |
| size | 图片大小 |
| width | 图片宽 |
| height | 图片高 |
| url | 图片 URL，建议使用 GetImageFile 接口下载  |

示例中发送一张相对路径是 `./xxx/imgPath.jpg` 的图片。 **示例：**

```
void DemoSendImage()
{
	const char* peer = "c9_0"; //your conv peer
	TIMConversationHandle conv = CreateConversation();
	intrt = TIMGetConversation(conv, kCnvC2C, peer);
	TIMMessageHandle msg = CreateTIMMessage();
	TIMMsgImageElemHandle elem = CreateMsgImageElem();
	const char* PATH = "./xxx/imgPath.jpg";
	SetImageElemPath(elem, PATH, strlen(PATH));
	AddElem(msg, elem);
	TIMCommCB callback;
	callback.OnSuccess = CBCommOnSuccessImp;
	callback.OnError = CBCommOnErrorImp;
	SendMsg(conv, msg, &callback);
	//....wait for callback
	SLEEP(1);
	DestroyConversation(conv);
	DestroyTIMMessage(msg);
	DestroyElem(elem);
 }
```

### 表情消息发送 

表情消息由 `TIMMsgFaceElemHandle` 定义，SDK 并不提供表情包，如果开发者有表情包，可使用 `index` 存储表情在表情包中的索引，由用户自定义，或者直接使用 `data` 存储表情二进制信息以及字符串 `key`，都由用户自定义，SDK 内部只做透传。
 
```
typedef void* TIMMsgFaceElemHandle;
TIMMsgFaceElemHandle	CreateFaceElemHandle();
int		GetFaceElemIndex(TIMMsgFaceElemHandle handle);
uint32_t	GetFaceElemDataLen(TIMMsgFaceElemHandle handle);
int		GetFaceElemData(TIMMsgCustomElemHandle handle, char* date, uint32_t* len);
void	SetFaceElemIndex(TIMMsgFaceElemHandle handle, int index);
void	SetFaceElemIndexData(TIMMsgCustomElemHandle handle, const char* date, uint32_t len);
```

示例中发送了索引为 10 的表情。 **示例：  **   

```
void DemoSendFace()
{
	const char* peer = "c9_0"; //your conv peer
	TIMConversationHandle conv = CreateConversation();
	intrt = TIMGetConversation(conv, kCnvC2C, peer);
	TIMMessageHandlemsg = CreateTIMMessage();
	TIMMsgFaceElemHandleelem = CreateFaceElemHandle();
	SetFaceElemIndex(elem, 10);
	AddElem(msg, elem);
	TIMCommCBcallback;
	callback.OnSuccess = CBCommOnSuccessImp;
	callback.OnError = CBCommOnErrorImp;
	SendMsg(conv, msg, &callback);
	//....wait for callback
	SLEEP(1);
	DestroyConversation(conv);
	DestroyTIMMessage(msg);
	DestroyElem(elem);
}
```

### 语音消息发送 

语音消息由 `TIMSoundElemHandle` 定义，其中 `data` 存储语音数据，语音数据需要提供时长信息，以秒为单位。

> **注意：**
>- 一条消息只能有一个语音 `Elem`，添加多条语音 `Elem` 时，`AddElem` 函数返回错误 1，添加不生效。
>- 语音和文件 `Elem` 不一定会按照添加时的顺序获取，建议逐个判断 `Elem` 类型展示，而且语音和文件 `Elem` 也不保证按照发送的 `Elem` 顺序排序。 
 
```
	TIM_DECL void		SetSoundElemData(TIMMsgSoundElemHandle handle, const char* data, uint32_t len);
	TIM_DECL void		SetSoundElemPath(TIMMsgSoundElemHandle handle, const char* path, uint32_t len);
	TIM_DECL void		SetSoundElemDuration(TIMMsgSoundElemHandle handle, const uint32_t duration);
	TIM_DECL uint32_t	GetSoundElemDuration(TIMMsgSoundElemHandle handle);
	TIM_DECL int		GetSoundElemUUID(TIMMsgSoundElemHandle handle, char* id, uint32_t* id_len);
	TIM_DECL void		GetSoundFromSoundElem(TIMMsgSoundElemHandle handle, TIMGetMsgDataCB* cb);
```

### 地理位置消息发送 

winsdk C 接口暂无封装。

### 小文件消息发送 

文件消息由 `TIMFileElem` 定义，另外还可以提供额外的显示文件名信息。

>**注意：**
> 一条消息只能添加一个文件 `Elem`，添加多个文件时，`AddElem` 函数返回错误 1，另外，语音和文件 `Elem` 不一定会按照添加时的顺序获取，建议逐个判断 `Elem` 类型展示。
 
```
	TIM_DECL void		SetFileElemFileName(TIMMsgFileElemHandle handle, const char* name, uint32_t name_len);
	TIM_DECL int		GetFileElemFileName(TIMMsgFileElemHandle handle, char* name, uint32_t* name_len);
	TIM_DECL void		SetFileElemFilePath(TIMMsgFileElemHandle handle, const char* path, uint32_t path_len);
	TIM_DECL void		SetFileElemData(TIMMsgFileElemHandle handle, const char* data, uint32_t data_len);
	TIM_DECL int		GetFileElemUUID(TIMMsgFileElemHandle handle, char* id, uint32_t* len);
	TIM_DECL void		GetFileFromFileElem(TIMMsgFileElemHandle handle, TIMGetMsgDataCB* cb);
```

**参数说明：**

参数|说明
---|---
path | 文件路径
data | 要发送的文件二进制数据。如设置 path，可不用设置 data，二者只需要设置一个字段即可，推荐使用 path
filename | 文件名，SDK 不校验是否正确，只透传。 

**示例：**

```
void DemoSendFile()
{
	const char* peer = "c9_0"; //your conv peer
	TIMConversationHandle conv = CreateConversation();
	int rt = TIMGetConversation(conv, kCnvC2C, peer);
	TIMMessageHandle msg = CreateTIMMessage();
	TIMMsgFileElemHandle elem = CreateFileElemHandle();
	std::string file_name = "1.dat";
	std::fstream send_file(file_name.c_str(), std::fstream::in | std::fstream::binary);
	std::string file_data((std::istream_iterator<char>(send_file)), std::istream_iterator<char>());
	SetFileElemFileName(elem, file_data.c_str(), file_name.length());
	SetFileElemData(elem, file_data.data(), file_data.length());
	AddElem(msg, elem);
	TIMCommCB callback;
	callback.OnSuccess = CBCommOnSuccessImp;
	callback.OnError = CBCommOnErrorImp;
	SendMsg(conv, msg, &callback);
	//....wait for callback
	SLEEP(1);
	DestroyConversation(conv);
	DestroyTIMMessage(msg);
	DestroyElem(elem);
}
```

### 自定义消息发送 

自定义消息是指当内置的消息类型无法满足特殊需求，开发者可以自定义消息格式，内容全部由开发者定义，ImSDK 只负责透传。另外如果需要 iOS APNs 推送，还需要提供一段推送文本描述，方便展示。自定义消息由 `TIMCustomElemHandle` 定义，其中 `data` 存储消息的二进制数据，其数据格式由开发者定义，`desc` 存储描述文本。一条消息内可以有多个自定义 `Elem`，并且可以跟其他 `Elem` 混合排列，离线 Push 时叠加每个 `Elem` 的 `desc` 描述信息进行下发。
 
```
typedef void* TIMMsgCustomElemHandle;
TIMMsgCustomElemHandle CreateCustomElemHandle();
uint32_t	GetCustomElemDataLen(TIMMsgCustomElemHandle handle);
int		GetCustomElemData(TIMMsgCustomElemHandle handle, char* date, uint32_t* len);
void	SetCustomElemData(TIMMsgCustomElemHandle handle, const char* date, uint32_t len);
int		GetCustomElemDesc(TIMMsgCustomElemHandle handle, char* desc, uint32_t* len);
void	SetCustomElemDesc(TIMMsgCustomElemHandle handle, const char* desc, uint32_t len);
```

**参数说明：**

参数|说明
---|---
data | 自定义消息二进制数据 
desc | 自定义消息描述信息 

示例中读取文件内容当做消息内容，具体展示由开发者决定。 **示例：**

```
void DemoSendCustomData()
{
	const char* peer = "c9_0"; //your conv peer
	TIMConversationHandle conv = CreateConversation();
	intrt = TIMGetConversation(conv, kCnvC2C, peer);
	TIMMsgElemHandle msg = CreateTIMMessage();
	TIMMsgCustomElemHandle elem = CreateCustomElemHandle();
	FILE* file = fopen("custom.data", "rb");
	fseek(file, 0, SEEK_END);
	uint32_t file_size = ftell(file);
	fseek(file, 0, SEEK_SET);
	void* buf = malloc(file_size);
	fread(buf, 1, file_size, file);
	fclose(file);
	SetCustomElemData(elem, (const char*)buf, file_size);
	AddElem(msg, elem);
	TIMCommCB callback;
	callback.OnSuccess = CBCommOnSuccessImp;
	callback.OnError = CBCommOnErrorImp;
	SendMsg(conv, msg, &callback);
	//....wait for callback
	SLEEP(1);
	free(buf);
	DestroyConversation(conv);
	DestroyTIMMessage(msg);
	DestroyElem(elem);
}
```

### Elem 顺序 

目前文件和语音 `Elem` 不一定会按照添加顺序传输，其他 `Elem` 按照顺序，不过建议不要过于依赖 `Elem` 顺序进行处理，应该逐个按照 `Elem` 类型处理，防止异常情况下进程 Crash。

### 针对群组的红包和点赞消息

对于直播场景，会有点赞和发红包功能，点赞相对优先级较低，红包消息优先级较高，具体消息内容可以使用 `TIMCustomElem` 进行定义，发送消息时，可使用不同接口定义消息优先级。具体消息优先级的策略，可参阅 [互动直播集成多人聊天方案](/doc/product/269/互动直播集成多人聊天方案)。

> **注意：**
> 只针对群聊消息有效。

```
/**
	Description:	发送红包消息
	@param	[in]	conv_handle		conversation handle
	@param	[in]	msg_handle		msg handle
	@param	[in]	callback		用户回调
	@return			void
	@exception      none
	*/
	TIM_DECL void SendRedPacketMsg(TIMConversationHandle conv_handle, TIMMessageHandle msg_handle, TIMCommCB *callback);	
	/**
	Description:	发送点赞消息
	@param	[in]	conv_handle		conversation handle
	@param	[in]	msg_handle		msg handle
	@param	[in]	callback		用户回调
	@return			void
	@exception      none
	*/
	TIM_DECL void SendLikeMsg(TIMConversationHandle conv_handle, TIMMessageHandle msg_handle, TIMCommCB *callback);
```

### 在线消息

对于某些场景，需要发送在线消息，即用户在线时收到消息，如果用户不在线，下次登录也不会看到消息，可用于通知类消息，这种消息不会进行存储，也不会计入未读计数。发送接口与 `SendMsg` 类似。

> **注意：**
> 只针对单聊消息有效。

```
	/**
	Description:	发送在线消息（服务器不保存消息）
	@param	[in]	conv_handle		conversation handle
	@param	[in]	msg_handle		msg handle
	@param	[in]	callback		用户回调
	@return			void
	@exception      none
	*/
	TIM_DECL void SendOnlineMsg(TIMConversationHandle conv_handle, TIMMessageHandle msg_handle, TIMCommCB *callback);
```

## 接收消息

在多数情况下，用户需要感知新消息的通知，这时只需注册新消息通知回调 `TIMSetMessageCallBack`，如果用户是登录状态，ImSDK 收到新消息会通过此方法抛出，另外需要注意，通过 `onNewMessage` 抛出的消息不一定是未读的消息，只是本地曾经没有过的消息（例如在另外一个终端已读，拉取最近联系人消息时可以获取会话最后一条消息，如果本地没有，会通过此方法抛出）。在用户登录之后，ImSDK 会拉取离线消息，为了不漏掉消息通知，需要在登录之前注册新消息通知。回调消息内容通过参数 `TIMMessageHandle` 传递，通过 `TIMMessageHandle` 可以获取消息和相关会话的详细信息，如消息文本，语音数据，图片等等，可参阅 [消息解析](/doc/product/269/1587#.E6.B6.88.E6.81.AF.E8.A7.A3.E6.9E.90) 部分。

**原型：**

```
	/**
	Description:	设置用户新消息回调函数
	@param	[in]	callback	新消息回调函数
	@return			void
	@exception      none
	*/
	TIM_DECL void			TIMSetMessageCallBack(TIMMessageCB *callback);
		/**
	Description:	用户新消息回调函数
	@param	[in]	handles		TIMMessageHandle 数组指针
	@param	[in]	msg_num		TIMMessageHandle 数组大小
	@param	[in]	data		用户自定义数据
	@return			void
	@exception      none
	*/
	typedef void (*CBOnNewMessage) (TIMMessageHandle* handles, uint32_t msg_num, void* data);
	typedef struct _TIMMessageCB_C
	{
		CBOnNewMessage OnNewMessage;
		void* data;
	}TIMMessageCB;
```

### 消息解析 

收到消息后，可用过 `getElem` 从 `TIMMessage` 中获取所有的 `Elem` 节点。

**遍历 `Elem` 原型：**

```
	/**
	Description:	获取 Message 中包含的 Elem 个数
	@param	[in]	handle		消息句柄
	@return			int			elem个数
	@exception      none
	*/
	TIM_DECL int				GetElemCount(TIMMessageHandle handle);
	/**
	Description:	获取Message中包含的指定elem句柄
	@param	[in]	handle		消息句柄
	@param	[in]	index		elem索引
	@return			TIMMsgElemHandle	elem句柄
	@exception      none
	*/
	TIM_DECL TIMMsgElemHandle	GetElem(TIMMessageHandle handle, int index);
```

### 接收图片消息

接收方收到消息后，可通过 `GetElem` 从 `TIMMessageHandle` 中获取所有的 `Elem` 节点，其中类型为 `TIMImageElem` 的是图片消息节点。然后通过 `imageList` 获取该图片的所有规格用来展示。详细如下：

** `TIMImageElem` 类原型：**

```
	/**
	Description:	获取图片路径（接受消息时不需要关注）
	@param	[in]	handle	TIMMsgImageElemHandle
	@param	[in]	path	路径 buffer
	@param	[in\out]len		路径长度
	@return			int 0:成功 非0:失败
	@exception      none
	*/
	TIM_DECL int		GetImageElemPath(TIMMsgImageElemHandle handle, char* path, uint32_t* len);
	/**
	Description:	设置发送图片路径
	@param	[in]	handle	TIMMsgImageElemHandle
	@param	[in]	path	路径
	@param	[in]	len		路径长度
	@return			void	
	@exception      none
	*/
	TIM_DECL void		SetImageElemPath(TIMMsgImageElemHandle handle, const char* path, uint32_t len);
	/**
	Description:	获取包含Image的个数
	@param	[in]	handle		TIMMsgImageElemHandle
	@return			uint32_t	Image个数
	@exception      none
	*/
	TIM_DECL uint32_t	GetImageNum(TIMMsgImageElemHandle handle);
	/**
	Description:	获取ImageElem包含的ImageHandle
	@param	[in]	handle	TIMMsgImageElemHandle
	@param	[in]	images	image handle的buffer
	@param	[in]	num		image个数
	@return			int 0:成功 非0:失败
	@exception      none
	*/
	TIM_DECL int		GetImages(TIMMsgImageElemHandle handle, TIMImageHandle* images, uint32_t* num);
```

**参数说明：**

参数|说明
---|---
path | 收消息时不用关注，为 nil 
images | 保存本图片的所有规格，目前最多包含三种规格：缩略图、大图、原图， 每种规格保存在一个 `TIMImageHandle` 句柄中 

**`TIMImageHandle` 说明： **

获取到消息时通过 `GetImages` 得到所有的图片规格，为 `TIMImageHandle` 数据，得到为 `TIMImageHandle` 数据后可通过图片大小进行占位，通过接口 `GetImageFile` 下载不同规格的图片进行展示。**下载的数据需要由开发者缓存，ImSDK 每次调用 `getImage` 都会从服务端重新下载数据。建议通过图片的 `uuid` 作为 `key` 进行图片文件的存储。**

**原型：** 

```
	typedef void* TIMImageHandle;
	/**
	Description:	获取图片规格
	@param	[in]	handle	TIMImageHandle
	@return			TIMImageType	图片规格，有三种 Thumb、Large、Original，分别代表缩略图、大图、原图
	@exception      none
	*/
	TIM_DECL TIMImageType	GetImageType(TIMImageHandle handle);
	/**
	Description:	获取图片大小
	@param	[in]	handle		TIMImageHandle
	@return			uint32_t	大小
	@exception      none
	*/
	TIM_DECL uint32_t	GetImageSize(TIMImageHandle handle);
	/**
	Description:	获取图片高度
	@param	[in]	handle		TIMImageHandle
	@return			uint32_t	图片高度
	@exception      none
	*/
	TIM_DECL uint32_t	GetImageHeight(TIMImageHandle handle);
	/**
	Description:	获取图片宽度
	@param	[in]	handle		TIMImageHandle
	@return			uint32_t	图片宽度
	@exception      none
	*/
	TIM_DECL uint32_t	GetImageWidth(TIMImageHandle handle);
	TIM_DECL uint32_t	GetImageURLLen(TIMImageHandle handle);
	TIM_DECL int		GetImageURL(TIMImageHandle handle, char* url, uint32_t* len);
	/**
	Description:	获取图片
	@param	[in]	handle		TIMImageHandle
	@param	[in]	filename	文件名	
	@param	[in]	cb			用户回调
	@return			int 0:成功 非 0:失败
	@exception      none
	*/
	TIM_DECL int		GetImageFile(TIMImageHandle handle, char* filename, TIMCommCB* cb);
```
 
**图片规格说明：**每幅图片有三种规格，分别是 Original（原图）、Large（大图）、Thumb（缩略图）。

- **原图：**指用户发送的原始图片，尺寸和大小都保持不变。
- **大图：**是将原图等比压缩，压缩后宽、高中较小的一个等于 720 像素。
- **缩略图：**是将原图等比压缩，压缩后宽、高中较小的一个等于 198 像素。

> 注：
>- 如果原图尺寸就小于 198 像素，则三种规格都保持原始尺寸，不需压缩。
>- 如果原图尺寸在 198~720 之间，则大图和原图一样，不需压缩。
>- 在手机上展示图片时，建议优先展示缩略图，用户单击缩略图时再下载大图，单击大图时再下载原图。当然开发者也可以选择跳过大图，单击缩略图时直接下载原图。
>- 在 Pad 或 PC 上展示图片时，由于分辨率较大，且基本都是 Wi-Fi 或有线网络，建议直接显示大图，用户单击大图时再下载原图。

### 接收语音消息

收到消息后，可用过 `GetElem` 从 `TIMMessageHandle` 中获取所有的 `Elem` 节点，其中 `TIMSoundElem` 为语音消息节点，原型如下。

**原型：**

```

	/**
	Description:	设置语音数据
	@param	[in]	handle	TIMMsgSoundElemHandle
	@param	[in]	data	语音二进制数据
	@param	[in]	len		语音数据长度
	@return			void
	@exception      none
	*/
	TIM_DECL void		SetSoundElemData(TIMMsgSoundElemHandle handle, const char* data, uint32_t len);
	/**
	Description:	设置语音文件路径（设置path时，优先上传语音文件）
	@param	[in]	handle	TIMMsgSoundElemHandle
	@param	[in]	path	文件路径
	@param	[in]	len		路径长度
	@return			void
	@exception      none
	*/
	TIM_DECL void		SetSoundElemPath(TIMMsgSoundElemHandle handle, const char* path, uint32_t len);
	/**
	Description:	设置语音长度（秒），发送消息时设置
	@param	[in]	handle		TIMMsgSoundElemHandle
	@param	[in]	duration	时长
	@return			void
	@exception      none
	*/
	TIM_DECL void		SetSoundElemDuration(TIMMsgSoundElemHandle handle, const uint32_t duration);
	/**
	Description:	获取语音长度（秒）
	@param	[in]	handle		TIMMsgSoundElemHandle
	@return			uint32_t	时长	
	@exception      none
	*/
	TIM_DECL uint32_t	GetSoundElemDuration(TIMMsgSoundElemHandle handle);
	TIM_DECL int		GetSoundElemUUID(TIMMsgSoundElemHandle handle, char* id, uint32_t* id_len);
	/**
	Description:	获取语音数据
	@param	[in]	handle	TIMMsgSoundElemHandle
	@param	[in]	cb		用户回调
	@return			void
	@exception      none
	*/
	TIM_DECL void		GetSoundFromSoundElem(TIMMsgSoundElemHandle handle, TIMGetMsgDataCB* cb);
```

**语音消息已读状态：**

语音是否已经播放，可使用 [消息自定义字段](#.E6.B6.88.E6.81.AF.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AD.97.E6.AE.B5) 实现，如 customInt 的值 0 表示未播放，1表示播放，当用户单击播放后可设置 customInt 的值为1。

## 消息属性 

### 消息是否已读

通过消息属性 `IsMsgRead`  是否消息已读。这里已读与否取决于 App 侧的逻辑判断。

```
	/**
	Description:	是否已读
	@param	[in]	handle	TIMMessageHandle
	@return			bool	已读标志
	@exception      none
	*/
	TIM_DECL bool				IsMsgRead(TIMMessageHandle handle);
```

### 消息状态

通过消息属性 `status` 可以获取消息的当前状态，如，发送中、发送成功、发送失败和删除，对于删除的消息，需要 UI 判断状态并隐藏。

```
// 消息发送中
#define TIM_MSG_STATUS_SENDING 1
// 消息发送成功
#define TIM_MSG_STATUS_SEND_SUCC 2
// 消息发送失败
#define TIM_MSG_STATUS_SEND_FAIL 3
// 消息被删除
#define TIM_MSG_STATUS_HAS_DELETED 4
@interface TIMMessage : NSObject
/**
 *  消息状态
 *
 *  @return TIMMessageStatus 消息状态
 */
-(TIMMessageStatus) status;
@end
```

### 是否是自己发出的消息

通过消息属性 `isSelf` 可以判断消息是否是自己发出的消息，界面显示时可用。

```
	/**
	Description:	是否发送方
	@param	[in]	handle	TIMMessageHandle
	@return			bool	TRUE 表示是发送消息    FALSE 表示是接收消息
	@exception      none
	*/
	TIM_DECL bool				IsMsgFromSelf(TIMMessageHandle handle);
```

### 消息发送者以及相关资料

对于群消息，可以通过 `GetMsgSender` 方法得到发送用户，另外也可以通过方法 `GetSenderProfile` 和 `GetSenderGroupMemberProfile` 获取用户自己的资料和所在群的资料。1.9 版本之前，只有在线消息 `onNewMessage` 抛出的消息可以获取到用户资料，1.9 版本以后，通过 `getMessage` 得到的消息也可以拿到资料（更新版本之前已经收到本地的消息无法获取到）。对于单聊消息，通过通过 `GetConversationFromMsg` 获取到对应会话，会话的 `GetConversationPeer` 可以得到正在聊天的用户。

> **注意：**此字段是消息发送时获取用户资料写入消息体，如后续用户资料更新，此字段不会相应变更，只有产生的新消息中才会带最新的昵称。

```
	/**
	Description:	获取发送方
	@param	[in]	handle	TIMMessageHandle
	@param	[in]	buf		发送方 ID buffer
	@param	[in]	len		发送方 ID 长
	@return			int		0:成功 非 0:失败
	@exception      none
	*/
	TIM_DECL int				GetMsgSender(TIMMessageHandle handle, char* buf, uint32_t* len);
	/**
	Description:	获取发送者资料
	@param	[in]	handle	TIMMessageHandle
	@param	[in]	profile	发送者资料 目前只有字段：identifier、nickname、faceURL、customInfo
	@return			int		0:成功 非 0:失败
	@exception      none
	*/
	TIM_DECL int				GetSenderProfile(TIMMessageHandle handle, TIMProfileHandle profile);
	/**
	Description:	获取发送者群内资料
	@param	[in]	handle	TIMMessageHandle
	@param	[in]	member_profile	发送者群内资料 目前只有字段：member、nameCard、role、customInfo
	@return			int		0:成功 非 0:失败
	@exception      none
	*/
	TIM_DECL int				GetSenderGroupMemberProfile(TIMMessageHandle handle, TIMGroupMemberInfoHandle member_profile);
```

### 消息时间

通过消息属性 `timestamp` 可以得到消息时间，该时间是 Server 时间，而非本地时间。在创建消息时，此时间为根据 Server 时间校准过的时间，发送成功后会改为准确的 Server 时间。

```
	/**
	Description:	当前消息的时间戳
	@param	[in]	handle	TIMMessageHandle
	@return			uint32_t	时间戳
	@exception      none
	*/
	TIM_DECL uint32_t			GetMsgTime(TIMMessageHandle handle);
```

### 消息删除

目前暂不支持 Server 消息删除，只能在本地删除，有两种删除方法，一种是 `RemoveMsg`，通过这种方法删除的消息，仅是打上删除的标记，并未真正删除。另外一种是 `delFromStorage`，从本地数据库彻底删除，但是如果使用 `getMessage`，可能从 Server 漫游消息获取到本地，此消息可能重新出现。所以如果使用了 `getMessage`，建议使用 `remove` 方法进行删除和界面过滤。

```
	/**
	Description:	删除消息：注意这里仅修改状态
	@param	[in]	handle	TIMMessageHandle
	@return			bool	TRUE 成功
	@exception      none
	*/
	TIM_DECL bool				RemoveMsg(TIMMessageHandle handle);
	/**
	Description:	从本地数据库删除消息：注意群组消息通过getMessage接口会从svr同步到本地
	@param	[in]	handle	TIMMessageHandle
	@return			bool	TRUE 成功
	@exception      none
	*/
	TIM_DECL bool				DelMsgFromStorage(TIMMessageHandle handle);
```

### 消息 ID

消息 ID 也有两种，一种是当消息生成时，就已经固定（`msgId`），这种方式可能跟其他用户产生的消息冲突，需要再加一个时间未读，可以认为 10 分钟以内的消息可以使用 `msgId` 区分。另外一种，当消息发送成功以后才能固定下来（`uniqueId`），这种方式能保证全局唯一。这两种方式都需要在同一个会话内判断。

```
	/**
	Description:	消息 ID 最大长度 30
	@param	[in]	handle	TIMMessageHandle
	@param	[in]	id		ID buffer
	@param	[in\out]len		ID 长度
	@return			int		0:成功
	@exception      none
	*/
	TIM_DECL int				GetMsgID(TIMMessageHandle handle, char* id, uint32_t* len);
		/**
	Description:	获取消息uniqueId
	@param	[in]	handle		TIMMessageHandle
	@return			uint64_t	uniqueId
	@exception      none
	*/
	TIM_DECL uint64_t			GetMsgUniqueID(TIMMessageHandle handle);
```

### 消息自定义字段

开发者可以对消息增加自定义字段，如自定义整数、自定义二进制数据，可以根据这两个字段做出各种不通效果，比如语音消息是否已经播放等等。另外需要注意，此自定义字段仅存储于本地，不会同步到 Server，更换终端获取不到。

```
	/**
	Description:	获取 CustomInt
	@param	[in]	handle	TIMMessageHandle
	@return			int		CustomInt
	@exception      none
	*/
	TIM_DECL int				GetMsgCustomInt(TIMMessageHandle handle);
	/**
	Description:	获取 CustomData
	@param	[in]	handle	TIMMessageHandle
	@param	[in]	str		CustomData buffer
	@param	[in]	len		CustomData 长度
	@return			int		0:成功 非 0:失败
	@exception      none	
	*/
	TIM_DECL int				GetMsgCustomStr(TIMMessageHandle handle, char* str, uint32_t* len);
	/**
	Description:	设置自定义数据，默认为 0
	@param	[in]	handle	TIMMessageHandle
	@param	[in]	custom	自定义数据
	@return			bool	TRUE 成功
	@exception      none
	*/
	TIM_DECL bool				SetMsgCustomInt(TIMMessageHandle handle, int custom);
	/**
	Description:	设置自定义数据，默认为""
	@param	[in]	handle	TIMMessageHandle
	@param	[in]	custom	CustomData buffer
	@param	[in]	len		CustomData 长度
	@return			bool	TRUE 成功
	@exception      none
	*/
	TIM_DECL bool				SetMsgCustomStr(TIMMessageHandle handle, const char* custom, uint32_t len);
```

## 会话操作

### 获取所有会话 

可以通过 `TIMGetConversationCount` 获取当前会话数量，从而得到所有本地会话。
 
```
	/**
	Description:	获取会话个数
	@return			uint64_t 回话个数
	@exception      none
	*/
	TIM_DECL uint64_t	TIMGetConversationCount();
```

**示例：**

```
void DemoGetConversations()
{
	uint64_t count = TIMGetConversationCount();
	for (uint64_t i = 0; i<count; i++)
	{
		//获得会话
		TIMConversationHandle conv = CreateConversation();
		TIMGetConversationByIndex(conv, i);
		/*处理会话
		 ....
		*/
		//释放会话
		DestroyConversation(conv);
	}
}
```

### 最近联系人漫游

ImSDK 登录以后默认会获取最近联系人漫游，同时每个会话会获取到最近的一条消息。如果不需要此功能，可以调用方法禁用。

```
	/**
	Description:	登录时禁止拉取最近联系人列表
	@return			void
	@exception      none
	*/
	TIM_DECL void		TIMDisableRecentContact();
```

### 获取会话本地消息

ImSDK 会在本地进行消息存储，可通过 `TIMConversation` 方法的 `getLocalMessage` 获取，此方法为异步方法，需要通过设置回调得到消息数据，对于单聊，登录后可以获取离线消息，对于群聊，开启最近联系人漫游的情况下，登录后只能获取最近一条消息，可通过 `getMessage` 获取漫游消息。对于图片、语音等资源类消息，消息体只会包含描述信息，需要通过额外的接口下载数据，可参与消息解析部分，下载后的真实数据不会缓存，需要调用方进行缓存。 
 
**原型： **

```
	/**
	Description:	获取本地会话消息
	@param	[in]	conv_handle	TIMConversationHandle
	@param	[in]	count		获取数量
	@param	[in]	last_msg	上次最后一条消息
	@param	[in]	callback	用户回调
	@return			void
	@exception      none
	*/
	TIM_DECL void GetLocalMsgs(TIMConversationHandle conv_handle, int count, TIMMessageHandle last_msg, TIMGetMsgCB * callback);
```

**参数说明：**

参数|说明
---|---
count | 指定获取消息的数量 
last | 指定上次获取的最后一条消息，如果 last 传 nil，从最新的消息开始读取 
callback | 回调 

### 获取会话漫游消息

对于群组，登录后可以获取漫游消息，对于 C2C，开通漫游服务后可以获取漫游消息，通过 ImSDK 的 `GetMsgs` 接口可以获取漫游消息，如果本地消息全部都是连续的，则不会通过网络获取，如果本地消息不连续，会通过网络获取断层消息。对于图片、语音等资源类消息，消息体只会包含描述信息，需要通过额外的接口下载数据，可参与消息解析部分，下载后的真实数据不会缓存，需要调用方进行缓存。 
 
**原型： **

```
	/**
	Description:	获取会话消息
	@param	[in]	conv_handle	TIMConversationHandle
	@param	[in]	count		获取数量
	@param	[in]	last_msg	上次最后一条消息
	@param	[in]	callback	用户回调
	@return			void
	@exception      none
	*/
	TIM_DECL void GetMsgs(TIMConversationHandle conv_handle, int count, TIMMessageHandle last_msg, TIMGetMsgCB * callback);
```

**参数说明：**

参数|说明
---|---
count | 指定获取消息的数量 
last | 指定上次获取的最后一条消息，如果 last 传 nil，从最新的消息开始读取 
callbakc | 回调 

### 删除会话

删除会话有两种方式，一种只删除会话，但保留了所有消息，另一种在删除会话的同时，也删除掉会话相关的消息。可以根据不同应用场景选择合适的方式。另外需要注意的是，如果删除本地消息，对于群组，通过 `GetMsgs` 会拉取到漫游消息，所以存在删除消息成功，但是拉取到消息的情况，取决于是否重新从漫游拉回到本地。如果不需要拉取漫游，可以通过 `GetLocalMsgs` 获取消息，或者只通过 `GetMsgs` 拉取指定条数（如未读条数数量）的消息。其中 `deleteConversation` 仅删除会话，`deleteConversationAndMessages` 删除会话以及消息。

**原型：**

```
	/**
	Description:	删除会话
	@param	[in]	type	会话类型，kCnvC2C 表示单聊 kCnvGroup 表示群聊
	@param	[in]	peer	用户 identifier 或者 群组 ID
	@return			bool	TRUE:删除成功  FALSE:删除失败
	@exception      none
	*/
	TIM_DECL bool		TIMDeleteConversation(TIMConversationType type, const char* peer);
	/**
	Description:	删除会话和消息
	@param	[in]	type	会话类型，kCnvC2C 表示单聊 kCnvGroup 表示群聊
	@param	[in]	peer	用户 identifier 或者 群组 ID
	@return			bool	TRUE:删除成功  FALSE:删除失败
	@exception      none
	*/
	TIM_DECL bool		TIMDeleteConversationAndMsgs(TIMConversationType type, const char* peer);
```

**参数解释：**

参数|说明
---|---
type|会话类型，如果是单聊，填写 kCnvC2C，如果是群聊，kCnvGroup 
peer|会话标识，单聊情况下，peer 为对方用户 identifier，群聊情况下，peer 为群组 ID 

### 同步获取会话最后的消息

UI 展示最近联系人列表时，时常会展示用户的最后一条消息，在 1.9 以后版本增加了同步获取接口，用户可以通过此接口方便获取最后一条消息进行展示。**目前没有网络无法获取，另外如果禁用了最近联系人，登录后在有新消息过来之前无法获取**。此接口获取并不会过滤删除状态消息，需要 App 层进行屏蔽。
 
**原型： **

```
	/**
	Description:	同步获取最后 N 条消息
	@param	[in]	conv_handle	TIMConversationHandle
	@param	[in\out]count		获取个数
	@param	[in]	last_msg	上次最后一条消息
	@param	[in]	msgs		TIMMessageHandle buffer
	@return			int
	@exception      none
	*/
	TIM_DECL int  GetMsgsFromCache(TIMConversationHandle conv_handle, int* count, TIMMessageHandle last_msg, TIMMessageHandle* msgs);
```

**参数说明：**

参数|说明
---|---
count | 需要获取的消息数，注意这里最多为 20 

## 系统消息 

会话类型（TIMConversationType）除了 C2C 单聊和 Group 群聊以外，还有一种系统消息，系统消息不能由用户主动发送，是系统后台在相应的事件发生时产生的通知消息。系统消息目前分为两种，一种是关系链系统消息，一种是群系统消息。

- **关系链变更系统消息：**当有用户加自己为好友，或者有用户删除自己好友的情况下，系统会发出变更通知，开发者可更新好友列表。相关细节可参阅 [关系链变更系统通知](/doc/product/269/用户资料与关系链（Windows%20SDK）#.E5.85.B3.E7.B3.BB.E9.93.BE.E5.8F.98.E6.9B.B4.E7.B3.BB.E7.BB.9F.E9.80.9A.E7.9F.A5) 部分。

- **群事件消息：**当群资料变更，如群名变更或者群内成员变更，在群里会有系统发出一条群事件消息，开发者可在收到消息时可选择是否展示给用户，同时可刷新群资料或者群成员。详细内容可参阅：[群组管理-群事件消息](/doc/product/269/群组管理（Windows%20SDK）#.E7.BE.A4.E4.BA.8B.E4.BB.B6.E6.B6.88.E6.81.AF)。

- **群系统消息：**当被管理员踢出群组，被邀请加入群组等事件发生时，系统会给用户发出群系统消息，相关细节可参阅：[群组管理-群系统消息](/doc/product/269/群组管理（Windows%20SDK）#.E7.BE.A4.E7.B3.BB.E7.BB.9F.E6.B6.88.E6.81.AF)。 
