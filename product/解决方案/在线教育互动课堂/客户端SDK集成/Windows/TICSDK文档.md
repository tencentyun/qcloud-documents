
## 1. 准备工作
TICSDK 使用了实时音视频服务（iLiveSDK）、云通讯服务（IMSDK）、COS 服务等腾讯云服务能力，在使用腾讯互动课堂服务时，请先阅读 [方案简介](https://cloud.tencent.com/document/product/680/14776)，了解相关服务的基本概念和基本业务流程。
相关链接如下：
- [实时音视频](https://cloud.tencent.com/document/product/268/8424)
- [云通讯服务（IMSDK）](https://cloud.tencent.com/document/product/269/1504)
- [COS 服务](https://cloud.tencent.com/document/product/436/6225)

###  资源下载	

为方便开发者集成使用，腾讯云准备了面向开发者的 Demo，开发者可以参照该 Demo 使用 TICSDK，[下载开发者 Demo](http://dldir1.qq.com/hudongzhibo/TICSDK/PC/TICSDK_PC_Demo.zip)。

>!开发者 Demo 主要向开发者展示 TICSDK 的基本使用方法，简化了很多不必要的 UI 代码，使开发者更加专注于了解 TICSDK 的使用方法。

SDK 下载：[TICSDK ](http://dldir1.qq.com/hudongzhibo/TICSDK/PC/TICSDK_PC.zip)


## 2. 开发指南
### 2.1 编译集成
在 VisualStudio 工程里面，选择编译平台为 x86。

![](https://main.qcloudimg.com/raw/944398e69196f1cb5a1d6a3db63d1dd6.png)

在 VisualStudio 工程里面，`配置属性`>`C/C++`里面添加 TICSDK、iLiveSDK、BoardSDK 头文件地址。

![](https://main.qcloudimg.com/raw/98866e32ed59d559b3dd18069717ca70.png)

在 VisualStudio工程里面，`配置属性`>`链接器`里面添加`TICSDK.lib`、`iLiveSDK.lib`、`BoardSDK.lib`这三个链接库，并指定好库文件地址。

![](https://main.qcloudimg.com/raw/1cd17fb7e0f9e5ed2ffa0b4aa95834dd.png)

![](https://main.qcloudimg.com/raw/69db29e18bef8083fbbd54374294e778.png)

### 2.2 初始化SDK
开发需要包含如下头文件，通过`TICManager::GetTICManager()`方法获得 TICManager 实例指针并进行初始化。在此之前，必须保证已经在 [腾讯云后台](https://console.cloud.tencent.com/rav) 注册成功并创建了应用，这样才能拿到腾讯云后台分配的 SDKAppID 和 accountType。

```C++
	#include "TICSDK.h"
	
	m_sdk = TICManager::GetTICManager();
	m_sdk->initSDK(1400042982);
```
通过 getTICManager() 可以对 iLiveSDK 进行一些基本操作，例如下面注册 iliveSDK 的几个回调事件。

```C++
	m_sdk->getTICManager()->setLocalVideoCallBack(onLocalVideo, this);
	m_sdk->getTICManager()->setDeviceOperationCallback(OnDeviceOperation, this);
	m_sdk->getTICManager()->setForceOfflineCallback(onForceOffline);
```

设置课堂配置类参数，注册监听回调。

```C++
	m_opt.setClassroomEventListener(this);
	m_opt.setClassroomIMListener(this);
	m_opt.setIsTeacher(m_bTeacher);
	m_opt.setRoomID(roomid);
```

### 2.3 创建或加入课堂
TICSDK 进出房间状态流程可参考下图：

![房间流程](https://main.qcloudimg.com/raw/62a414b2cf7c28cf63846bfb870eda95.png) 

因为涉及到IM消息的收发，所以必须先登录：

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

>!
> 1. 开发调试阶段， 开发者可以使用腾讯云实时音视频控制台的开发辅助工具来生成临时的 uid 和 userSig 用于开发测试。
> 2. 如果此用户在其他终端被踢，登录将会失败，返回错误码（ERR_IMSDK_KICKED_BY_OTHERS：6208）。为了保证用户体验，建议开发者进行登录错误码 ERR_IMSDK_KICKED_BY_OTHERS 的判断，在收到被踢错误码时，提示用户是否重新登录。
> 3. 如果用户保存用户票据，可能会存在过期的情况，如果用户票据过期，login 将会返回 70001 错误码，开发者可根据错误码进行票据更换。
> 4. 关于以上错误的详细描述，参见 [用户状态变更](https://cloud.tencent.com/document/product/269/9148#.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4)。

登录成功之后，就可以创建或者加入课堂了，创建课堂调用方法如下，需要用户生成课堂房间 roomID 并传入：

```C++
	m_opt.setRoomID(roomid);
	m_sdk->createClassroom(roomid, onIliveSucCallback, onIliveErrCallback, this);
```
创建课堂接口只是进行了一些准备工作，老师端创建课堂后还需调用`加入课堂`方法加入课堂。
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
该接口需要参数中，opt 是`TICClassroomOption`对象，代表加入课堂时的一些配置.

基础配置有 3 个，加入课堂时是否为老师（只有老师才可以创建课堂，其他人以学生身份加入），进入课的房间 ID，以及透传给 iliveSDK 的 roomOption 参数项。该类还有三个代理对象，用来监听课堂内的一些事件。

加入房间后要注意监听如下一些事件回调：

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
	void onClassroomDestroy()
```

### 2.4 使用音视频
音视频功能封装于腾讯云实时音视频 SDK `ILiveSDK`，TICSDK 中只封装了一些常用的接口：打开/关闭摄像头、麦克风，扬声器， 屏幕分享等，具体调用方法如下：
```C++

	m_sdk->enableCamera(true);

	m_sdk->enableMic(true);

	m_sdk->enablePlayer(true);

	uint32 fps = 10;
	m_sdk->openScreenShare(0, 0, 1920, 1080, fps);

	m_sdk->changeScreenShareSize(0, 0, 1920, 1080);

	m_sdk->closeScreenShare();
```
如果想渲染视频画面，注册 iliveSDK 的两个回调可以得到本地和远程的视频数据：
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
渲染前填入视频发送者 ID 和视频类型进行设置：
```C++
	iLiveView view;
	view.mode = VIEW_MODE_HIDDEN;	//按比例缩放，填充黑边;
	                                //拉伸画面到控件大小;
	view.exclusive = true;
	m_pRootView->setView(identifier, type, view, false);
```
设置好后在 ilive 视频数据回调里面调用`doRender`进行渲染。

### 2.5 使用互动白板
进入房间后就可以初始化白板，传入参数为房间 ID 和白板窗口的父窗口句柄（也可以不传）。白板的`getRenderWindow`方法会返回白板本身的窗口句柄，可以将此窗口句柄添加为白板父窗口的子窗口。

```C++
	m_sdk->initWhiteBoard(roomId, GetSafeHwnd());
	
	m_sdk->getTICWhiteBoardManager()->getRenderWindow();
```
如果需要白板离线数据，在进房前还需要调用
```C++
	m_sdk->getTICWhiteBoardManager()->getBoardData();
```
开发者可以通过 getTICWhiteBoardManager() 获得白板管理类里面封装好的方法，也可以直接调用 BoardSDK.h 里面的接口对白板进行操作，BoardSDK 详见 [白板SDK文档](/document/product/680/17884) 。

### 2.6 使用 PPT
用户想使用 PPT，可先将 PPT 上传到腾讯云对象存储 COS。TICSDK 内部集成了 COSSDK。开发者可以使用我们维护内置的公共账号（每个客户对应一个存储桶，推荐），也可以自己申请配置 COS 账号并自行维护。
使用如下接口可以将 PPT 上传至 COS：
```C++
boardSDk->uploadFile(filePath);//上传文件
```
这里会将文件上传至公共账号的 COS 路径下，通过回调`onUploadResult`和`onFileUploadResult`通知上传和预览结果。
如果想使用自己申请的 COS 账号存储地址，可以调如下接口设置自定义账号参数：
```C++
boardSDk->setCosConfig(appId, bucket, path, region);//设置COS参数
```
然后再调用如下上传接口，传入指定的secretId,secretKey,tempToken
```C++
boardSDk->uploadFile(filePath, secretId, secretKey, token);
```
对于使用了 V4 旧版的 COS 系统，上传需要先计算签名 sig，再使用以下代码：
```C++
boardSDk->uploadFile(filePath, sig);
```
上传结果会通过回调函数`onUploadResult`和`onFileUploadResult`通知给上层。

### 2.7 使用窗口分享涂鸦
窗口分享涂鸦需要机器支持 OpenGL，调用如下接口可以选择指定的窗口分享出去：
```C++
	/**
	* \brief 打开白板分享(指定窗口，必须支持OpenGL)
	* \return 非0表示失败，0表示成功
	*/
	virtual int openWhiteBoardShare() = 0;
```
也支持直接传入窗口句柄：
```C++
	/**
	* \brief 打开白板分享(传入窗口句柄，必须支持OpenGL)
	*/
	virtual void openWhiteBoardShare(HWND hwnd) = 0;
```
打开窗口分享涂鸦后可调用 BoarSDK 接口函数对画笔进行操作。BoardSDK 接口详见 [白板SDK文档](/document/product/680/17884) 。

### 2.8 收发消息
IM 相关的接口封装于腾讯云通信 SDK`IMSDK`，同样，TICSDK 中也只封装了一些常用接口：

```C++
	/**
	* \brief 发送文本消息
	* \param userId   消息接收者，填空（null或者""表示发送群消息）
	* \param msg	  发送内容
	*/
	virtual void sendTextMessage(const char * userId, const char * msg) = 0;

	/**
	* \brief 发送自定义消息
	* \param userId   消息接收者，填空（null或者""表示发送群消息）
	* \param msg	  发送内容
	*/
	virtual void sendCustomMessage(const char * userId, const char * msg) = 0;

	/**
	* \brief 发送消息(所有类型)
	* \param type	  消息类型
	* \param userId   消息接收者
	* \param msg	  消息对象
	*/
	virtual void sendMessage(TIMConversationType type, const char * userId, TIMConversationHandle msg) = 0;
```
课堂内成员在调用以上方法发送消息时，会触发 IM 事件，如果在加入课堂前设置了 IM 事件监听代理 `IClassroomIMListener`，一端发送 IM 消息时，另一端就可以在课堂内 IM 消息回调对应方法中得到通知:

```C++
	/**
	@brief 课堂IM消息监听对象
	*/
	class IClassroomIMListener
	
	/**
	* \brief 接收文本消息
	* \param fromId	消息发送者
	* \param msg	消息内容
	* \param type	消息类型（群聊或者单聊）
	*/
	virtual void onRecvTextMessage(const char * fromId, const char * msg, TIMConversationType type) {};

	/**
	* \brief 接收自定义消息
	* \param fromId	消息发送者
	* \param msg	消息内容
	* \param type	消息类型（群聊或者单聊）
	*/
	virtual void onRecvCustomMessage(const char * fromId, const char * msg, TIMConversationType type) {};

	/**
	* \brief 接收到非白板全部消息回调
	* \param handles	消息句柄
	* \param elemCount	元素个数
	*/
	virtual void onRecvMessage(TIMMessageHandle handle, uint32_t elemCount) {};
	
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

### 2.9 监听事件
TICSDK 提供了三个事件监听对象，如下
```C++
/**
* \brief 课堂事件监听对象
*/
class IClassroomEventListener

/**
* \brief 课堂IM消息监听对象
*/
class IClassroomIMListener
```
在加入课堂前设置了课堂事件监听代理`IClassroomEventListener`，一端进行课堂房间相关操作时，另一端就可以在课堂内事件回调中得到通知：
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

创建课堂这步通过`onCreateClassroom`方法通知上层是否成功；课堂内断线事件会通过`onLiveVideoDisconnect`方法通知给上层也便做异常处理。

课堂内的成员音视频事件都会通过`onMemStatusChange`方法回调到其他端（包括操作者的），event_id 表示事件类型（开关摄像头等），ids 表示触发事件的用户 ID 集合。其他端触发回调之后，可以根据事件类型，进行相应的处理。比如，收到开摄像头事件，就添加一个对应用户的渲染视图，收到关摄像头时间，就移除对应用户的渲染视图（详细用法可以参照 emo）。

房间内成员进出消息通过`onMemberJoin`和`onMemberQuit`方法通知房间内所有成员；而老师销毁课堂消息通过`onClassroomDestroy`方法通知房间内所有成员。

设置 IM 事件监听代理`IClassroomIMListener`，IM 收到的消息，无论个人，群组还是系统消息，都会通过事件代理通知上层，详请参见 [使用窗口分享涂鸦](https://cloud.tencent.com/document/product/680/17883#2.7-.E4.BD.BF.E7.94.A8.E7.AA.97.E5.8F.A3.E5.88.86.E4.BA.AB.E6.B6.82.E9.B8.A6) 。

设置白板事件监听代理`IClassroomWhiteboardListener`，可以监听到白板操作和 PPT 上传事件的回调。

### 2.10 结束课堂
退出课堂调用方法如下：
```C++
> TICManager.h

	/**
	* \brief 退出课堂
	* \param success 退出课堂成功回调
	* \param err 退出课堂失败回调
	*/
	virtual void quitClassroom(ilive::iLiveSucCallback success, ilive::iLiveErrCallback err, void* data) = 0;
```
若要销毁创建好的课堂，则调用
```C++
	/**
	* \brief 老师销毁课堂
	* \param success 销毁课堂成功回调
	* \param err 销毁课堂失败回调
	* \param data   用户自定义数据
	*/
	virtual void destroyClassroom(ilive::iLiveSucCallback success = nullptr, ilive::iLiveErrCallback err = nullptr, void* data = nullptr) = 0;
```
要退出程序还需要登出 iliveSDK，登出方法比较简单，如下：
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


