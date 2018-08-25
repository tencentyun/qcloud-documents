
## 1. 准备工作
TICSDK 使用了实时音视频服务（iLiveSDK）、云通讯服务（IMSDK）、COS 服务等腾讯云服务能力，在使用腾讯互动课堂服务时，请先阅读指 [方案简介](https://cloud.tencent.com/document/product/680/14776)，了解相关服务的基本概念和基本业务流程。
相关链接如下：

- [实时音视频](https://cloud.tencent.com/document/product/268/8424)
- [云通讯服务（IMSDK）](https://cloud.tencent.com/document/product/269/1504)
- [COS 服务](https://cloud.tencent.com/document/product/436/6225)

### 1.1 资源下载	

为了方便开发者的集成使用，我们开发了一个面向开发者的 Demo，开发者可以参照该 Demo 使用 TICSDK，[单击下载开发者 Demo](http://dldir1.qq.com/hudongzhibo/TICSDK/PC/TICSDK_PC_Demo_1.0.0.zip)。

>**注意：**
> 开发者 Demo 的主要主要为向开发者展示 TICSDK 的基本使用方法，所以简化了很多不必要的 UI 代码，使开发者更加专注于了解 TICSDK 的使用方法。

SDK 下载：[TICSDK >>](http://dldir1.qq.com/hudongzhibo/TICSDK/PC/TICSDK_PC.zip)

## 2. 集成 SDK

### 2.1 编译
在 VisualStudio 工程里面，选择编译平台为 x86。

![](https://main.qcloudimg.com/raw/944398e69196f1cb5a1d6a3db63d1dd6.png)

在 VisualStudio 工程里面，`配置属性`->`C/C++`里面添加 TICSDK、iLiveSDK、BoardSDK 头文件地址。

![](https://main.qcloudimg.com/raw/98866e32ed59d559b3dd18069717ca70.png)

在 VisualStudio工程里面，`配置属性`->`链接器`里面添加`TICSDK.lib`、`iLiveSDK.lib`这两个链接库，并指定好库文件地址。

![](https://main.qcloudimg.com/raw/1cd17fb7e0f9e5ed2ffa0b4aa95834dd.png)

![](https://main.qcloudimg.com/raw/69db29e18bef8083fbbd54374294e778.png)

## 3 快速开发
### 3.1 初始化参数
开发需要包含如下头文件。通过`TICSDK::GetSDKInstance()`方法获得 TICSDK 实例指针并进行初始化。在此之前，之前必须保证已经在 [腾讯云后台](https://console.cloud.tencent.com/rav) 注册成功并创建了应用，这样才能拿到腾讯云后台分配的 SDKAppID 和 accountType。

```C++
	#include "TICSDK.h"
	#include "TICClassroomOption.h"
	
	m_sdk = TICSDK::GetSDKInstance();
	m_sdk->initSDK(1400042982, 17802);
```
通过 getTICManager() 获得白板管理类实例指针，就可以对 iLiveSDK 进行一些基本操作，例如下面注册 iliveSDK 的几个回调事件。

```C++
	m_sdk->getTICManager()->setLocalVideoCallBack(onLocalVideo, this);
	m_sdk->getTICManager()->setDeviceOperationCallback(OnDeviceOperation, this);
	m_sdk->getTICManager()->setForceOfflineCallback(onForceOffline);
```

设置课堂配置类参数，注册监听回调。

```C++
	m_opt.setClassroomEventListener(this);
	m_opt.setClassroomIMListener(this);
	m_opt.setClassroomWhiteboardListener(this);
	m_opt.setIsTeacher(m_bTeacher);
	m_opt.setRoomID(roomid);
```

### 3.2 创建和加入房间
TICSDK 进出房间状态流程可参考下图：

![房间流程](https://main.qcloudimg.com/raw/62a414b2cf7c28cf63846bfb870eda95.png) 

登录/登出，创建，加入/退出房间的详细接口函数见后面 4.4，4.5 介绍，加入房间后要注意监听如下一些事件回调：

* 房间网络断开
```C++
	void onLiveVideoDisconnect(int reason, const char *errorinfo, void* data)
```

* 被踢下线
```C++
	void onForceOffline();
```

* 房间解散消息
```C++
	void onRecvGroupSystemMsg(const char * msg)
```

### 3.3 加载白板
进入房间后就可以初始化白板，传入参数为自己 ID 和白板窗口的父窗口句柄（也可以不传）。白板的`getRenderWindow`方法会返回白板本身的窗口句柄，可以将此窗口句柄添加为白板父窗口的子窗口。

```C++
	m_sdk->initWhiteBoard(m_identifier.c_str(), GetSafeHwnd());
	
	m_sdk->getTICWhiteBoardManager()->getRenderWindow();
```

### 3.4 视频渲染
注册 iliveSDK 的两个回调可以得到本地和远程的视频数据：
```C++
	/**
	* \brief 设置本地视频预览回调
	* \param OnLocalVideo   回调函数接口
	* \param data   用户自定义数据
	*/
	virtual void setLocalVideoCallBack(ilive::iLivePreviewCallback OnLocalVideo, void* data = nullptr) = 0;
	
	/**
	@brief 设置远程视频数据接收
	@param OnRemoteVideo   回调函数接口
	@param data   用户自定义数据
	*/
	virtual void setRemoteVideoCallBack(ilive::iLivePreviewCallback OnRemoteVideo, void* data = nullptr) = 0;
```
iliveSDK 提供了一个 iLiveRootView 对象实现了对视频数据的渲染，传入播放窗口句柄进行初始化：
```C++
	m_pRootView = ilive::iLiveCreateRootView();
	m_pRootView->init(hwnd);
```
目前提供 2 种渲染实现：D3D 和 GDI。D3D 仅支持渲染 i420 格式，GDI 仅支持渲染 RGB24 格式，可以设置视频渲染格式：
```C++
	E_ColorFormat fmt = (m_pRootView->getRootViewType() == ROOT_VIEW_TYPE_D3D) ? COLOR_FORMAT_I420 : COLOR_FORMAT_RGB24;
	sdk->getTICManager()->GetILive()->setVideoColorFormat(fmt);
```
渲染前填入视频发送者 ID 和视频类型进行设置：
```C++
	iLiveView view;
	view.mode = VIEW_MODE_HIDDEN;	//按比例缩放，填充黑边;
	                                //拉伸画面到控件大小;
	view.exclusive = true;
	m_pRootView->setView(identifier, type, view, false);
```
设置好后在 ilive 视频数据回调里面调用`doRender`进行渲染。

## 4. 进一步了解和使用 SDK
### 4.1 头文件概览

先总体说明下 SDK 中暴露的公开头文件的主要功能：

类名 | 主要功能
--------- | ---------
TICSDK.h | 整个 SDK 的入口类，提供了 SDK【初始化】以及【获取版本号】的方法。
TICManager.h | 互动课堂管理类，互动课堂SDK对外主要接口类，提供了【登录/登出SDK】、【创建/加入/销毁课堂】、【音视频操作】、【IM操作】等接口。
TICClassroomOption.h | 加入课堂时的课堂配置类，主要用来配置加入课堂时的角色（学生 or 老师），另外课堂配置对象还带有三个可选的代理对象，一个是复制监听课堂内部事件，一个则负责监听课堂内的IM消息，还有一个负责监听课堂内白板消息。
TICSDKCosConfig.h | COS 管理类，内部封装了腾讯云对象云存储 COSSDK，负责文件（PPT、wrod、Excel、pdf、图片等）的上传、下载、在线转码预览等（移动端目前只支持上传和下载）。
TICWhiteboardManager.h|白板管理类，对白板 BoardSDK.dll 进行了封装。

### 4.2 使用流程

TICSDK 业务使用的流程如下：

![教师业务流程](https://main.qcloudimg.com/raw/78f1227b825f9ea4699004dcfb484b63.png) 

其中【创建课堂】为教师角色特有流程，学生角色不需调用。

下面将 SDK 按照功能划分，遵循一般的使用顺序，介绍一下`TICSDK`中各功能的使用方法和注意点。

### 4.3 初始化 SDK
要使用`TICSDK`，首先得进行初始化，初始化方法位于`TICSDK`单例类中：

```C++
	> TICSDK.h (该行表示方法所处文件名，下同)
	
	/**
	* \brief 初始化TICSDK
	* \param iLiveSDKAppId 腾讯云控制台注册的应用ID
	* \param iLiveAccountType腾讯云控制台注册的应用的账号类型
	* \return 初始化结果，0代表成功，其他代表失败
	*/
	virtual int initSDK(int iLiveSDKAppId, int iLiveAccountType) = 0;

```
初始化方法很简单，传入应用的 SDKAppID 和 accountType 即可。但是开发者在初始化之前必须保证已经在腾讯云后台注册成功并创建了应用（见3.1），这样才能拿到腾讯云后台分配的 SDKAppID 和 accountType。

### 4.4 登录/登出
初始化完成之后，因为涉及到IM消息的收发，所以还必须先登录：

```C++
	> TICManager.h
	
	/**
	* \brief 登录iliveSDK
	 
	* \param uid    用户id
	* \param userSig    用户签名（由腾讯云后台生成）
	* \param success 登录成功回调
	* \param err      登录错误回调
	* \param data   用户自定义数据
	* \return 登录结果，0表示成功
	 */
	int login(const char * id, const char * userSig, ilive::iLiveSucCallback success, ilive::iLiveErrCallback err, void* data);
```
该方法需要传入 uid 和 userSig，uid 为用户 ID，userSig 为腾讯云后台用来鉴权的用户签名，相当于登录 TICSDK 的用户密码，需要开发者服务器遵守腾讯云生成 userSig 的规则来生成，并传给客户端用于登录，详情请参考 [生成签名](https://cloud.tencent.com/document/product/647/17275)。
success 和 err 为登录 SDK 成功和失败回调，data 为用户自定义数据。

> **注意：**
> 1. 开发调试阶段， 开发者可以使用腾讯云实时音视频控制台的开发辅助工具来生成临时的 uid 和 userSig 用于开发测试。
> 2. 如果此用户在其他终端被踢，登录将会失败，返回错误码（ERR_IMSDK_KICKED_BY_OTHERS：6208）。为了保证用户体验，建议开发者进行登录错误码 ERR_IMSDK_KICKED_BY_OTHERS 的判断，在收到被踢错误码时，提示用户是否重新登录。
> 3. 如果用户保存用户票据，可能会存在过期的情况，如果用户票据过期，login 将会返回 70001 错误码，开发者可根据错误码进行票据更换。
> 4. 关于以上错误的详细描述，参见 [用户状态变更](https://cloud.tencent.com/document/product/269/9148#.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4)。


登出方法比较简单，如下：

```C++
> TICManager.h

/**
* \brief 登出iliveSDK
* \param success 成功回调
* \param err 错误回调
* \param data   用户自定义数据
 */
void logout(ilive::iLiveSucCallback success, ilive::iLiveErrCallback err, void* data);
```
其中参数 success 和 err 为登录 SDK 成功和失败回调，data 为用户自定义数据。

### 4.5 课堂管理

* 创建课堂

登录成功之后，就可以创建或者加入课堂了，创建课堂接口如下，需要用户生成课堂房间 roomID 并传入：

```C++
> TICManager.h

/**
* \brief 创建课堂
* \param roomID 课堂房间ID
* \param listener 创建课堂回调指针
*/
virtual void createClassroom(uint32_t roomID, IClassroomEventListener* listener) = 0;
```

创建课堂接口只是进行了一些准备工作，老师端创建课堂后还需调用`加入课堂`方法加入课堂。

* 加入课堂

```C++
> TICManager.h

/**
* \brief 加入课堂
* \param opt 课堂配置类对象
* \param success 加入课堂成功回调
* \param err 加入课堂失败回调
*/
virtual void joinClassroom(TICClassroomOption& opt, ilive::iLiveSucCallback success, ilive::iLiveErrCallback err, void* data) = 0;
```

该接口需要参数中，opt是`TICClassroomOption`对象，代表加入课堂时的一些配置：

```C++
/**
 课堂配置类
 */
class TICSDK_API TICClassroomOption
{
public:
	TICClassroomOption();
	~TICClassroomOption();

	bool getIsTeacher(); 
	void setIsTeacher(bool bTeacher); // 设置课堂内角色是否为老师

	uint32_t getRoomID;
	void setRoomID(uint32_t roomId);  ();  //设置课堂房间ID
	
	void setRoomOption(ilive::iLiveRoomOption& opt); //设置进课堂参数项
	ilive::iLiveRoomOption& getRoomOption();

	void setClassroomEventListener(IClassroomEventListener* listener); //设置监听课堂内部事件
	IClassroomEventListener* getClassroomEventListener() const;

	void setClassroomIMListener(IClassroomIMListener* listener); //设置监听课堂内IM消息
	IClassroomIMListener* getClassroomIMListener() const;

	void setClassroomWhiteboardListener(IClassroomWhiteboardListener* listener); //设置监听课堂内白板消息
	IClassroomWhiteboardListener* getClassroomWhiteboardListener();
}


/**
* \brief 课堂事件监听对象
*/
class IClassroomEventListener

/**
* \brief 课堂IM消息监听对象
*/
class IClassroomIMListener

/**
* \brief 课堂白板消息监听对象
*/
class IClassroomWhiteboardListener
```

基础配置有 3 个，加入课堂时是否为老师（只有老师才可以创建课堂，其他人以学生身份加入），进入课的房间 ID，以及透传给 iliveSDK 的 roomOption 参数项。该类还有三个代理对象，用来监听课堂内的一些事件。其中 roomOption 参数下面有个成员 privateMapKey，是用户配置票据，为必填信息。进入课堂前要先从自己的业务服务器或者该信息，然后调用ticsdk的进入课堂接口。详见- [privateMapKey](https://cloud.tencent.com/document/product/647/17230#privatemapkey)

* 退出课堂

```C++
> TICManager.h

/**
* \brief 退出课堂
* \param success 退出课堂成功回调
* \param err 退出课堂失败回调
*/
virtual void quitClassroom(ilive::iLiveSucCallback success, ilive::iLiveErrCallback err, void* data) = 0;
```

学生退出课堂时，只是本人退出了课堂，老师调用`退出课堂`方法退出课堂时，该课堂将会被销毁，另外退出课堂成功后，课堂的资源将会被回收，所以开发者应尽量保证再加入另一个课堂前，已经退出了前一个课堂。

### 4.6 COS 上传相关操作
COS 为 [腾讯云对象存储](https://cloud.tencent.com/document/product/436/6225)，TICSDK 内部会将调用 SDK 接口将图片，文件上传到COS 云存储桶中。COS 上传和预览功能被封装在了 TICWhiteboardManager 里面，如需上传图片、PPT 文件，调用`uploadFile`这个接口将文件名路径填入即可。

开发者可以使用我们维护的公共账号（每个客户对应一个存储桶，推荐），也可以自己申请配置COS账号并自行维护。

```C++
> TICWhiteboardManager.h

/**
* \brief 设置cos参数
* \param cosAppId	cos appid
* \param bucket		bucket
* \param path		文件上传路径
* \param region	    	园区
*/
virtual void setCosConfig(uint32_t cosAppId, const char* bucket, const char* path, const char* region) = 0;

/**
* \brief 上传文件到cos
* \param fileName   文件名
*/
virtual void uploadFile(const std::wstring& fileName) = 0;

/**
* \brief 带签名上传文件到cos，兼容旧版V4
* \param fileName   文件名
* \param sig			cos签名
*/
virtual void uploadFile(const std::wstring& fileName, std::string& sig) = 0;

```

上传结果通过`IClassroomWhiteboardListener`的回调传给上层处理：
```C++
/**
* \brief 通知文件上传进度
* \param percent	进度按百分比
*/
virtual void onUploadProgress(int percent) = 0;

/**
* \brief 通知文件上传结果
* \param success	上传结果
* \param code	    错误码
* \param objName	cos文件名
* \param fileName	本地文件名
*/
virtual void onUploadResult(bool success, int code, std::wstring objName, std::wstring fileName) = 0;

/**
* \brief 通知PPT文件上传结果
* \param success	上传结果
* \param objName	cos文件名
* \param fileName	本地文件名
* \param pageCount	  文件页数，若结果失败则为错误码
*/
virtual void onFileUploadResult(bool success, std::wstring objName,std::wstring fileName, int pageCount) = 0;
```

### 4.7 白板相关操作

TICSDK 中将白板 SDK 封装在一个白板管理类当中，用户可在进入房间后调 TICSDK.h 里面的 initWhiteBoard 方法进行初始化，也可以自己初始化白板 SDK 后通过 initWhiteBoard 方法传入。

```C++
> TICSDK.h

/**
* \brief 初始化白板SDK，在加入房间之后
* \param id 用户id
* \param classID 课堂ID
* \param parentHWnd 白板父窗口句柄
* \return 结果，0表示成功
*/
virtual int initWhiteBoard(const char* id, HWND parentHWnd = nullptr) = 0;

/**
* \brief 初始化白板SDK
* \param boardsdk 外部初始化的sdk指针
* \return 结果，0表示成功
*/
virtual int initWhiteBoard(BoardSDK* boardsdk) = 0;

/**
* \brief 获取白板管理类实例指针
* \return 白板管理类指针
*/
virtual TICWhiteboardManager* getTICWhiteBoardManager() = 0;
```

如果要在进房间前初始化白板，除了调用`initWhiteBoard`接口之外，还要调用如下接口启动数据同步上报和cos上传
```C++
> TICWhiteboardManager.h
/**
* \brief 启用数据上报通道
* \param appId
* \param classId
* \param userSig
*/
virtual void enableDefaultReporter(int appId, uint32_t classId, const char* userSig) = 0;

/**
* \brief 启用cos上传
* \param appId
* \param classId
* \param userSig
*/
virtual void enableCosUploader(int appId, const char* userSig) = 0;

```

开发者可以通过 getTICWhiteBoardManager() 获得白板管理类里面封装好的方法，也可以直接调用 BoardSDK.h 里面的接口对白板进行操作，BoardSDK 详见 [白板SDK文档](/document/product/680/17884) 。

```C++
> TICWhiteboardManager.h
	/**
	* \brief 获得白板窗口句柄
	*/
	virtual HWND getRenderWindow() = 0;
	
	/**
	* \brief 清空白板数据
	*/
	virtual void clearWhiteBoard() = 0;
	
	/**
	* \brief 使用画板工具
	* \param tool  画板工具
	*/
	virtual void useTool(BoardTool tool) = 0;
	
	/**
	* \brief 设置线宽
	* \param width  宽度
	*/
	virtual void setWidth(uint32_t width) = 0;
	
	/**
	* \brief 设置颜色
	* \param rgba  颜色RGBA值
	*/
	virtual void setColor(uint32_t rgba) = 0;
	
	/**
	* \brief 设置填充
	* \param fill  是否填充
	*/
	virtual void setFill(bool fill) = 0;
	
	/**
	* \brief 撤销
	*/
	virtual void undo() = 0;
	
	/**
	* \brief 重做
	*/
	virtual void redo() = 0;
	
	/**
	* \brief 删除
	*/
	virtual void remove() = 0;
	
	/**
	* \brief 清除白板
	*/
	virtual void clear() = 0;
	
	/**
	* \brief 清除涂鸦
	*/
	virtual void clearDraws() = 0;
	
	/**
	* \brief 设置白板背景
	* \param url  背景图地址
	* \param pageID 白板ID，默认为当前白板
	*/
	virtual void useBackground(const wchar_t *url, const char *pageID = nullptr) = 0;
	
	/**
	* \brief 设置白板背景色
	* \param rgba  颜色RGBA值
	*/
	virtual void setBackgroundColor(uint32_t rgba) = 0;
	
	/**
	* \brief 设置全局背景色
	* \param rgba  颜色RGBA值
	*/
	virtual void setAllBackgroundColor(uint32_t rgba) = 0;
	
	/**
	* \brief 拉取离线数据
	*/
	virtual void getBoardData() = 0;
	
	/**
	* \brief 获取当前页码
	* \return 当前页码
	*/
	virtual uint32_t getPageIndex() = 0;

	/**
	* \brief 获取总页数
	* \return 总页数
	*/
	virtual uint32_t getPageCount() = 0;

	/**
	* \brief 刷新页码
	*/
	virtual void refreshPageInfo() = 0;

	/**
	* \brief 页码跳转
	* \param pageIndex  跳转的页码
	*/
	virtual void gotoPage(uint32_t pageIndex) = 0;

	/**
	* \brief 跳转上一页
	*/
	virtual void gotoLastPage() = 0;

	/**
	* \brief 跳转下一页
	*/
	virtual void gotoNextPage() = 0;

	/**
	* \brief 插入新的一页
	*/
	virtual void insertPage() = 0;

	/**
	* \brief 删除当前页
	*/
	virtual void deletePage() = 0;
```

#### 4.8 IM 相关操作

IM 相关的接口封装于腾讯云通信 SDK`IMSDK`，同样，TICSDK 中也只封装了一些常用接口：

```C++
	/**
	* \brief 发送C2C文本消息
	* \param identifier   消息接收者
	* \param msg  发送内容
	* \param OnSuccess 发送成功回调
	* \param OnError   发送失败回调
	*/
	virtual void sendC2CTextMsg(const char * identifier, const char * msg) = 0;
	
	/**
	* \brief 发送群文本消息
	* \param msg  发送内容
	* \param OnSuccess 发送成功回调
	* \param OnError   发送失败回调
	*/
	virtual void sendGroupTextMsg(const char * msg) = 0;
	
	/**
	* \brief 发送C2C自定义消息
	* \param identifier   消息接收者
	* \param msg  发送内容
	* \param OnSuccess 发送成功回调
	* \param OnError   发送失败回调
	*/
	virtual void sendC2CCustomMsg(const char * identifier, const char * msg) = 0;
	
	/**
	* \brief 发送群组自定义消息
	* \param msg  发送内容
	* \param OnSuccess 发送成功回调
	* \param OnError   发送失败回调
	*/
	virtual void sendGroupCustomMsg(const char * msg) = 0;
```
课堂内成员在调用以上方法发送消息时，会触发 IM 事件，如果在加入课堂前设置了 IM 事件监听代理 `IClassroomIMListener`，一端发送 IM 消息时，另一端就可以在课堂内 IM 消息回调对应方法中得到通知:

```C++
	/**
	@brief 课堂IM消息监听对象
	*/
	class IClassroomIMListener
	
	/**
	* \brief 接收C2C文本消息
	* \param identifier	消息发送者
	* \param msg	消息内容
	*/
	virtual void onRecvC2CTextMsg(const char * identifier, const char * msg) = 0;
	
	/**
	* \brief 接收群组文本消息
	* \param identifier	消息发送者
	* \param msg	消息内容
	*/
	virtual void onRecvGroupTextMsg(const char * identifier, const char * msg) = 0;
	
	/**
	* \brief 接收C2C自定义消息
	* \param identifier	消息发送者
	* \param msg	消息内容
	*/
	virtual void onRecvC2CCustomMsg(const char * identifier, const char * msg) = 0;
	
	/**
	* \brief 接收群组自定义消息
	* \param identifier	消息发送者
	* \param msg	消息内容
	*/
	virtual void onRecvGroupCustomMsg(const char * identifier, const char * msg) = 0;
	
	/**
	* \brief 接收群组系统消息
	* \param msg	消息内容
	*/
	virtual void onRecvGroupSystemMsg(const char * msg) = 0;
	
	/**
	* \brief 发送消息回调
	* \param err	错误码
	* \param errMsg	错误描述
	*/
	virtual void onSendMsg(int err, const char * errMsg) = 0;
	
	/**
	* \brief 发送白板消息回调
	* \param err	错误码
	* \param errMsg	错误描述
	*/
	virtual void onSendWBData(int err, const char * errMsg) = 0;

```

前 4 个代理方法，分别对应了前面 4 个消息发送的方法，对应类型的消息会在对应类型的代理方法中回调给课堂内所有成员（发消息本人除外），其他端收到后可以将消息展示在界面上。接下来`onRecvGroupSystemMsg`监听了课堂内群组系统消息，`onSendMsg`和`onSendWBData`则对应发普通消息和 IM 消息是否成功的回调。

### 4.9 音视频相关操作

这部分功能封装于腾讯云实时音视频 SDK `ILiveSDK`，TICSDK 中只封装了一些常用的接口：打开/关闭摄像头、麦克风，扬声器， 屏幕分享等，如下：
```C++
	/**
	* \brief 打开/关闭摄像头
	* \param enable   true：打开默认摄像头；false：关闭
	*/
	virtual void enableCamera(bool bEnable) = 0;
	
	/**
	* \brief 切换摄像头
	* \param cameraId   摄像头设备标识
	*/
	virtual void switchCamera(const char* cameraId) = 0;
	
	/**
	* \brief 打开/关闭麦克风
	* \param enable   true：打开默认麦克风；false：关闭
	*/
	virtual void enableMic(bool bEnable) = 0;
	
	/**
	* \brief 切换麦克风
	* \param deviceID   麦克风设备标识
	*/
	virtual void switchMic(const char* deviceID) = 0;
	
	/**
	* \brief 打开/关闭扬声器
	* \param enable   true：打开默认扬声器；false：关闭
	*/
	virtual void enablePlayer(bool bEnable) = 0;
	
	/**
	* \brief 打开屏幕分享(指定窗口)
	* \param hWnd 所要捕获的窗口句柄(NULL表示全屏)
	* \param fps 捕获帧率
	*/
	virtual void openScreenShare(HWND hWnd, uint32& fps) = 0;
	
	/**
	* \brief 打开屏幕共享(指定区域)
	* \param left/top/right/bottom 所要捕获屏幕画面的区域的左上角坐标(left, top)和右下角坐标(right, bottom)
	* \param fps 捕获帧率
	*/
	virtual void openScreenShare(int32& left, int32& top, int32& right, int32& bottom, uint32& fps) = 0;
	
	/**
	* \brief 动态修改屏幕分享的区域
	* \param left/top/right/bottom 所要捕获屏幕画面的区域的左上角坐标(left, top)和右下角坐标(right, bottom)
	* \param fps 捕获帧率
	*/
	virtual int changeScreenShareSize(int32& left, int32& top, int32& right, int32& bottom) = 0;
	
	/**
	@brief 关闭屏幕共享
	*/
	virtual void closeScreenShare() = 0;
```

课堂内成员在进行打开/关闭摄像头、麦克风操作时，会触发音视频事件，如果在加入课堂前设置了课堂事件监听代理`IClassroomEventListener`，一端进行音视频操作时，另一端就可以在课堂内音视频事件回调中得到通知：

```C++
	
	class IClassroomEventListener
	
	/**
	* \brief 创建房间返回回调
	* \param code		错误码，0为OK
	* \param desc	错误描述
	*/
	virtual void onCreateClassroom(DWORD code, const char *desc) = 0;
	
	/**
	* \brief 视频房间断开回调
	* \param reason		错误码
	* \param errorinfo	错误描述
	* \param data		用户自定义数据的指针
	*/
	virtual void onLiveVideoDisconnect(int reason, const char *errorinfo, void* data) = 0;
	
	/**
	* \brief 成员状态改变回调
	* \param event_id		事件id
	* \param ids		发生状态变化的成员id列表
	* \param data		用户自定义数据的指针
	*/
	virtual void onMemStatusChange(ilive::E_EndpointEventId event_id, const ilive::Vector<ilive::String> &ids, void* data) = 0;

	/**
	* \brief 成员加入房间
	* \param identifier		加入房间成员id列表
	*/
	virtual void onMemberJoin(const char ** identifier, uint32_t num) = 0;

	/**
	* \brief 成员退出房间
	* \param identifier		退出房间成员id列表
	*/
	virtual void onMemberQuit(const char ** identifier, uint32_t num) = 0;

	/**
	* \brief 课堂房间被销毁
	*/
	virtual void onClassroomDestroy() = 0;
```
创建课堂这步通过`onCreateClassroom`方法通知上层是否成功；课堂内断线事件会通过`onLiveVideoDisconnect`方法通知给上层也便做异常处理。课堂内的成员音视频事件都会通过`onMemStatusChange`方法回调到其他端（包括操作者的），event_id 表示事件类型（开关摄像头等），ids 表示触发事件的用户 ID 集合，其他端触发回调之后，可以根据事件类型，进行相应的处理，比如，收到开摄像头事件，就添加一个对应用户的渲染视图，收到关摄像头时间，就移除对应用户的渲染视图（详细用法可以参照 emo）。房间内成员进出消息通过`onMemberJoin`和`onMemberQuit`方法通知房间内所有成员；而老师销毁课堂消息通过`onClassroomDestroy`方法通知房间内所有成员。


